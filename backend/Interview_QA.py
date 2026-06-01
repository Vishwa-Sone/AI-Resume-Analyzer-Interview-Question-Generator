import dotenv
import os
import json
import google.generativeai as genai

# Load environment variables
dotenv.load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def Generate_QA(resume_info, job_role, job_description=None):

    prompt = f"""
    Analyze this candidate for the role: {job_role}

    Resume:
    {resume_info}

    Job Description:
    {job_description or "Not provided"}

    Return ONLY valid JSON:

    {{
      "missing_skills": [
        {{
          "skill": "",
          "reason": "",
          "priority": "high|medium|low"
        }}
      ],
      "project_suggestions": [
        {{
          "title": "",
          "description": "",
          "skills_targeted": [],
          "difficulty": "beginner|intermediate|advanced"
        }}
      ],
      "interview_QA": [
        {{
          "question": "",
          "answer": "",
          "category": "technical|behavioral|situational",
          "difficulty": "easy|medium|hard"
        }}
      ]
    }}

    Tasks:
    - Identify missing skills
    - Suggest 3 high impact projects which improve the resume and skills
    - Generate 3 interview questions per category
    - Keep answers concise
    - Do not invent experience
    - Return ONLY valid JSON
    - No markdown
    - No explanation text
    """

    try:

        print("\n----- Sending Prompt To Gemini -----\n")
        print(prompt)

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

        parsed_json = json.loads(content)

        return parsed_json

    except Exception as e:

        print("\n----- Exception Occurred -----\n")
        print(e)

        return {
            "missing_skills": [
                {
                    "skill": "",
                    "reason": "",
                    "priority": ""
                }
            ],
            "project_suggestions": [
                {
                    "title": "",
                    "description": "",
                    "skills_targeted": [],
                    "difficulty": ""
                }
            ],
            "interview_QA": [
                {
                    "question": "",
                    "answer": "",
                    "category": "",
                    "difficulty": ""
                }
            ]
        }