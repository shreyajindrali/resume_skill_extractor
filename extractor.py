import re
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_resume_data(pdf_file):
    text = extract_text_from_pdf(pdf_file)

    name = text.split('\n')[0]  # crude assumption
    email = re.findall(r"[A-Za-z0-9\._]+@[A-Za-z0-9]+\.[A-Za-z]{2,}", text)
    phone = re.findall(r"\b\d{10}\b", text)
    skills = re.findall(r"(?i)skills\s*[:\-]?\s*(.*)", text)
    work = re.findall(r"(?i)(work experience|professional experience)\s*[:\-]?\s*(.*)", text)

    return {
        "name": name.strip(),
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": skills[0] if skills else "",
        "work_experience": work[0][1] if work else ""
    }
