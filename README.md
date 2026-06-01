# Smart Resume Analyzer

An AI-powered Resume Analyzer built using FastAPI, React.js, spaCy NLP, and Google Gemini AI.
The application analyzes resumes, extracts important information, calculates skill match percentage for different job roles, and generates AI-based interview questions and project suggestions.

---

# Features

* Resume parsing from PDF and DOCX files
* Extracts:

  * Name
  * Email
  * Phone Number
  * LinkedIn Profile
  * GitHub Profile
  * Skills
  * Education
  * Experience
  * Projects
  * Certifications
* Skill match analysis for multiple job roles
* AI-generated:

  * Missing skills analysis
  * Project suggestions
  * Interview questions & answers
* Uses Google Gemini AI for intelligent resume understanding
* Clean React frontend with FastAPI backend

---

# Tech Stack

## Frontend

* React.js
* Vite
* Tailwind CSS

## Backend

* FastAPI
* Python
* spaCy NLP
* pdfminer
* python-docx

## AI / LLM

* Google Gemini API

---

# Project Structure

```bash
Smart-Resume-Analyzer/
│
├── backend/
│   ├── app.py
│   ├── ResumePar.py
│   ├── Interview_QA.py
│   ├── Skillset.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer
```

---

# Backend Setup

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate.bat
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 5. Add Gemini API Key

Create a `.env` file inside the `backend` folder:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

## 6. Run Backend

```bash
cd backend
python -m uvicorn app:app --reload --port 8000
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

## 7. Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

## 8. Run Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# Supported Job Roles

The system supports multiple AI/ML and software-related job roles with custom skill matching.

Examples:

* AI Engineer
* Data Scientist
* Machine Learning Engineer
* Frontend Developer
* Backend Developer
* Full Stack Developer

---

# API Endpoints

## Get Job Roles

```http
GET /api/job-roles
```

---

## Analyze Resume

```http
POST /api/analyse
```

### Form Data

| Field           | Type     |
| --------------- | -------- |
| file            | PDF/DOCX |
| job_role        | String   |
| job_description | String   |

---

# Future Improvements

* Resume scoring dashboard
* ATS compatibility analysis
* AI-based resume improvement suggestions
* Authentication system
* Resume history tracking
* Deployment using Docker and Render

---

# Author

Vishwa Sone

.
