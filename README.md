# Resume Skill Extractor 📝

A web app that extracts name, email, phone number, skills, and experience from PDF resumes using Python and Streamlit.
## 🚀 Features

- Upload PDF resumes
- Extract:
  - Name
  - Email
  - Phone Number
  - Skills
  - Work Experience
- Filter resumes by skills
- Save/load extracted data
- Dockerized for easy setup
## 🛠️ Technologies Used

- Python 3
- Streamlit
- PyMuPDF (`fitz`)
- Regular Expressions
- Docker
## 🐳 How to Run (Using Docker)

1. Build the image:
   ```bash
   docker build -t resume-extractor .
docker run -p port:8501 resume-extractor

🟢 **Why**: This gives step-by-step instructions to run the app.

---

**Project File Structure**  
**What to write:**

```markdown
## 📁 Project Structure

.
├── app.py             # Main app (Streamlit interface)
├── extractor.py       # Logic for extracting resume fields
├── storage.py         # For saving/loading resume data
├── resume_db.json     # Local database of extracted info
├── Dockerfile         # To run app in a container
├── requirements.txt   # List of Python dependencies
└── README.md          # Project info (this file)

