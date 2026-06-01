import spacy
import re
import json
from Skillset import job_roles_skills, skills_db
import dotenv
import os
import google.generativeai as genai

# Load environment variables
dotenv.load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Load spaCy model
nlp = spacy.load('en_core_web_sm')



# BASIC EXTRACTION FUNCTIONS
def extract_email(text):
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )
    return emails[0] if emails else None


def extract_phone(text):
    phones = re.findall(r"\+?\d[\d\s-]{8,}\d", text)
    return phones[0] if phones else None


def extract_linkedin(text):
    urls = re.findall(
        r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?",
        text
    )

    if urls:
        url = urls[0]

        if not url.startswith("http"):
            url = "https://" + url

        return url

    return None


def extract_github(text):
    urls = re.findall(
        r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+/?",
        text
    )

    if urls:
        url = urls[0]

        if not url.startswith("http"):
            url = "https://" + url

        return url

    return None


def extract_name(text):
    doc = nlp(text[:1000])

    person_entities = [
        ent.text for ent in doc.ents if ent.label_ == "PERSON"
    ]

    if person_entities:
        return person_entities[0]

    return None



# SKILL EXTRACTION
escaped_skills = [re.escape(skill) for skill in skills_db]

SKILLS_REGEX = re.compile(
    r"\b(" + "|".join(escaped_skills) + r")\b",
    re.IGNORECASE
)


def extract_skills(text):
    text = text.lower()

    found_skills = SKILLS_REGEX.findall(text)

    return list(set(found_skills))


def analyse_skills(text, job_role):

    job_role = job_role.lower()

    if job_role not in job_roles_skills:
        raise ValueError(f"Unsupported job role {job_role}")

    text = text.lower()

    required_skills = job_roles_skills[job_role]

    found_skills = []

    missing_skills = []

    for skill in required_skills:

        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

        else:
            missing_skills.append(skill)

    return found_skills, missing_skills


# CLEAN JSON RESPONSE
def clean_llm_output(text):

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return None

    json_str = text[start:end + 1]

    try:
        return json.loads(json_str)

    except json.JSONDecodeError:
        return None



# ANALYSE RESUME SECTIONS
def analyse_sections(text):

    prompt = f"""
    Extract structured resume data.

    Return ONLY valid JSON matching this schema:

    {{
      "education": [
        {{
          "degree": "",
          "institution": "",
          "year": ""
        }}
      ],
      "experience": [
        {{
          "title": "",
          "company": "",
          "duration": "",
          "description": ""
        }}
      ],
      "projects": [
        {{
          "title": "",
          "description": "",
          "technologies": []
        }}
      ],
      "certifications": []
    }}

    Important Rules:
    - Return ONLY valid JSON
    - No explanation text
    - No markdown
    - No extra notes
    - If value not found use empty string
    - technologies must be array

    Resume:
    {text[:4000]}
    """

    try:

        print("\n----- Sending Prompt To Gemini -----\n")

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.1,
                "response_mime_type": "application/json"
            }
        )

        print("\n----- Gemini Response -----\n")
        print(response.text)

        content = response.text.strip()

        parsed_data = json.loads(content)

        return parsed_data

    except Exception as e:

        print("\n----- Exception Occurred -----\n")
        print(e)

        return {
            "error": str(e),
            "education": [],
            "experience": [],
            "projects": [],
            "certifications": []
        }