import streamlit as st
import re
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_name(text):
    lines = text.split('\n')
    for line in lines:
        if line.strip() and not re.search(r'\d', line):
            if len(line.split()) <= 4:
                return line.strip()
    return "Not found"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?[\d\s-]{7,}', text)
    if match:
        phone = match.group(0)
        phone = re.sub(r'[^\d+]', '', phone)
        return phone
    return "Not found"

def extract_skills(text):
    skills_list = [
        "Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL", "Bash", "Shell Scripting",
        "Git", "GitHub", "Docker", "Kubernetes", "React", "Angular", "Node.js", "Express.js",
        "Flask", "Django", "FastAPI", "REST APIs", "GraphQL", "MongoDB", "MySQL", "PostgreSQL",
        "Firebase", "Redis", "Apache Kafka", "RabbitMQ", "Linux", "Windows Server", "AWS", "Azure",
        "Google Cloud Platform", "Heroku", "Terraform", "Ansible", "Jenkins", "GitLab CI/CD",
        "CI/CD Pipelines", "Machine Learning", "Deep Learning", "Scikit-learn", "TensorFlow",
        "PyTorch", "OpenCV", "NLP", "Spacy", "NLTK", "Transformers", "BERT", "Data Analysis",
        "Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "Tableau", "Excel", "Statistics",
        "Probability", "Linear Algebra", "Data Structures", "Algorithms", "Object-Oriented Programming",
        "Functional Programming", "Unit Testing", "TDD", "Agile", "Scrum", "Jira", "Postman", "Figma",
        "UI/UX Design", "Cybersecurity", "Ethical Hacking", "Penetration Testing", "Blockchain",
        "Solidity", "Smart Contracts", "Web3.js", "Metamask", "Truffle", "Hardhat", "SEO",
        "Digital Marketing", "Communication", "Teamwork", "Leadership", "Problem Solving",
        "Critical Thinking", "Adaptability", "Time Management", "Creativity", "Emotional Intelligence",
        "Conflict Resolution", "Decision Making", "Active Listening", "Empathy", "Negotiation",
        "Public Speaking", "Presentation Skills", "Collaboration", "Self-Motivation", "Organization",
        "Stress Management", "Accountability", "Patience", "Open-Mindedness", "Interpersonal Skills",
        "Work Ethic", "Attention to Detail", "Positive Attitude", "Resilience", "Strategic Thinking",
        "Multitasking", "Goal-Oriented", "Flexibility", "Curiosity", "Initiative"
    ]
    text_lower = text.lower()
    skills_found = [skill for skill in skills_list if skill.lower() in text_lower]
    return list(set(skills_found)) if skills_found else ["Not found"]

def extract_work_experience(text):
    experiences = []
    sections = re.split(r'(?i)(?<=\n)(work experience|experience|professional experience)(?=\n)', text)
    for sec in sections:
        lines = sec.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if any(keyword in line.lower() for keyword in ['intern', 'engineer', 'developer', 'analyst', 'manager', 'consultant', 'scientist']):
                exp = {}
                exp['role'] = line
                exp['company'] = lines[i+1].strip() if i+1 < len(lines) else ""
                experiences.append(exp)
    return experiences if experiences else ["Not found"]

def main():
    st.title("Resume Skill Extractor")

    if 'stored_resumes' not in st.session_state:
        st.session_state.stored_resumes = []

    uploaded_file = st.file_uploader("Upload a PDF Resume", type=["pdf"])

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)
        work_exp = extract_work_experience(text)

        st.subheader("Extracted Information")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Skills:** {', '.join(skills)}")
        st.write("**Work Experience:**")
        if isinstance(work_exp[0], dict):
            for exp in work_exp:
                st.markdown(f"- **Role:** {exp['role']}")
                st.markdown(f"  **Company:** {exp['company']}")
        else:
            for exp in work_exp:
                st.write(f"- {exp}")

        if st.button("Save Extracted Data"):
            st.session_state.stored_resumes.append({
                'Name': name,
                'Email': email,
                'Phone': phone,
                'Skills': skills,
                'Work Experience': work_exp
            })
            st.success("Resume data saved!")

    if st.session_state.stored_resumes:
        st.subheader("Stored Resumes")

        skill_filter = st.text_input("Filter resumes by skill (e.g. python, java)").strip().lower()

        if skill_filter:
            matching = []
            non_matching = []

            for res in st.session_state.stored_resumes:
                if any(skill_filter in skill.lower() for skill in res['Skills']):
                    matching.append(res)
                else:
                    non_matching.append(res)

            st.markdown("### ✅ Resumes Matching the Skill")
            for idx, res in enumerate(matching):
                st.markdown(f"#### Resume {idx + 1}")
                st.write(f"**Name:** {res['Name']}")
                st.write(f"**Email:** {res['Email']}")
                st.write(f"**Phone:** {res['Phone']}")
                st.write(f"**Skills:** {', '.join(res['Skills'])}")

            st.markdown("### ❌ Resumes Not Matching the Skill")
            for idx, res in enumerate(non_matching):
                st.markdown(f"#### Resume {idx + 1}")
                st.write(f"**Name:** {res['Name']}")
                st.write(f"**Email:** {res['Email']}")
                st.write(f"**Phone:** {res['Phone']}")
                st.write(f"**Skills:** {', '.join(res['Skills'])}")
        else:
            for idx, res in enumerate(st.session_state.stored_resumes):
                st.markdown(f"### Resume {idx + 1}")
                st.write(f"**Name:** {res['Name']}")
                st.write(f"**Email:** {res['Email']}")
                st.write(f"**Phone:** {res['Phone']}")
                st.write(f"**Skills:** {', '.join(res['Skills'])}")

if __name__ == "__main__":
    main()
