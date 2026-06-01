import os
import json
import tempfile
import shutil
import traceback
import re

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pdfminer.high_level import extract_text
from docx import Document

from ResumePar import (
    analyse_sections,
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    analyse_skills,
    clean_llm_output,
    extract_linkedin,
    extract_github
)

from Interview_QA import Generate_QA
from Skillset import job_roles_skills


app = FastAPI(title="Resume Analyser API")



# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# EXTRACT TEXT FROM FILE
def extract_text_from_file(file_path: str) -> str:

    print("extracting text from file", file_path)

    text = ""

    if file_path.endswith(".pdf"):

        text = extract_text(file_path)

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        text = "\n".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported file type. Use .pdf or .docx")

    text = re.sub(r"[ \t]+", " ", text)

    text = text.strip()

    print("TEXT LENGTH:", len(text))

    return text



# GET JOB ROLES
@app.get("/api/job-roles")
def get_job_roles():

    return {
        "roles": sorted(job_roles_skills.keys())
    }



# ANALYSE RESUME
@app.post("/api/analyse")
async def analyse_resume(
    file: UploadFile = File(...),
    job_role: str = Form(...),
    job_description: str = Form("")
):

    if not file.filename.lower().endswith((".pdf", ".docx")):

        raise HTTPException(
            status_code=400,
            detail="Only .pdf and .docx files are supported."
        )

    if job_role.lower() not in job_roles_skills:

        raise HTTPException(
            status_code=400,
            detail=f"Unsupported job role: '{job_role}'"
        )

    suffix = os.path.splitext(file.filename)[1]

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    )

    try:

        # Save uploaded file temporarily
        shutil.copyfileobj(file.file, tmp)

        tmp.close()

        # Extract text
        text = extract_text_from_file(tmp.name)

        text = text[:12000]

       
        # ANALYSE RESUME SECTIONS
        try:

            raw_sections = analyse_sections(text)

        except Exception as llm_err:

            err_msg = str(llm_err)

            if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:

                raise HTTPException(
                    status_code=429,
                    detail="API rate limit exceeded. Please wait and try again."
                )

            raise

        # Parse section data
        if isinstance(raw_sections, dict):

            section_info = raw_sections

        else:

            try:

                section_info = json.loads(raw_sections)

            except (json.JSONDecodeError, TypeError):

                section_info = {}

       
        # BASIC PARSED INFO
        parsed = {
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "skills": extract_skills(text),
            "linkedin": extract_linkedin(text),
            "github": extract_github(text),
        }

        # Merge Gemini section info
        for key, value in section_info.items():

            if key not in ("error", "raw_output"):

                parsed[key] = value

       
        # SKILL MATCHING
        found_skills, missing_skills = analyse_skills(
            text,
            job_role.lower()
        )

        total_required = len(found_skills) + len(missing_skills)

        match_percentage = round(
            (len(found_skills) / total_required * 100),
            1
        ) if total_required > 0 else 0

        parsed["all_skills"] = parsed["skills"]

        parsed["skills"] = found_skills

       
        # PREPARE DATA FOR GEMINI QA
        main_sec = {
            "skills": parsed.get("skills", [])[:20],
            "education": parsed.get("education", [])[:2],
            "experience": parsed.get("experience", [])[:3],
            "projects": parsed.get("projects", [])[:2],
        }


        try:

            qa_raw = Generate_QA(
                main_sec,
                job_role,
                job_description or None
            )

        except Exception as llm_err:

            err_msg = str(llm_err)

            if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:

                raise HTTPException(
                    status_code=429,
                    detail="API rate limit exceeded. Please wait and try again."
                )

            raise

        # -----------------------------
        # HANDLE GEMINI JSON RESPONSE
        # -----------------------------

        if isinstance(qa_raw, dict):

            qa_content = qa_raw

        else:

            cleaned_qa = clean_llm_output(qa_raw)

            if cleaned_qa is not None:

                qa_content = cleaned_qa

            else:

                try:

                    qa_content = json.loads(qa_raw)

                except (json.JSONDecodeError, TypeError):

                    qa_content = {
                        "error": "Could not parse QA response."
                    }

        # -----------------------------
        # FINAL RESPONSE
        # -----------------------------

        return {
            "parsed": parsed,
            "match": {
                "percentage": match_percentage,
                "found": found_skills,
                "missing": missing_skills,
            },
            "qa": qa_content,
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except HTTPException:

        raise

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Internal error: {str(e)}"
        )

    finally:

        os.unlink(tmp.name)