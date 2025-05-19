

# Resume Skill Extractor

Resume Skill Extractor is a web-based application developed using Python and Streamlit, designed to automate the extraction of key details from PDF resumes. The tool enables users to upload resumes and extract relevant fields such as name, email address, phone number, skills, and work experience. It also includes functionalities for filtering resumes based on specific skill sets and saving/loading extracted data locally for future use. This project is ideal for recruiters, HR teams, or developers working on recruitment automation tools.

The core extraction logic uses a combination of PDF parsing libraries and regular expressions to identify and extract structured information from unstructured resume text. The application is fully containerized using Docker, making it easy to build, deploy, and run on any platform with minimal setup.

## Features

* Upload PDF resumes through a user-friendly web interface.
* Automatically extract important fields:

  * Full Name
  * Email Address
  * Phone Number
  * Skills
  * Work Experience (including role, company, and duration; defaults to "Not mentioned" if duration is unavailable)
* Filter resumes based on required skills to shortlist candidates.
* Save extracted information to a local JSON file.
* Load previously saved data for reference or reuse.
* Dockerized setup for consistent and portable deployment.

## Technologies Used

The following technologies and libraries are used in this project:

* **Python 3** – Programming language used for backend logic.
* **Streamlit** – For creating the interactive web interface.
* **PyMuPDF (fitz)** – To read and extract text from PDF files.
* **Regular Expressions (re)** – For identifying patterns like email addresses, phone numbers, etc.
* **Docker** – For containerizing the application for easy deployment and environment consistency.

## How to Run the Application Using Docker

To build and run the application using Docker, follow these steps:

1. Open your terminal and navigate to the project directory.
2. Build the Docker image using the following command:

   ```bash
   docker build -t resume-extractor .
   ```
3. Once the image is built, run the container:

   ```bash
   docker run -p 8501:8501 resume-extractor
   ```
4. Open your browser and navigate to `http://localhost:8501` to access the application.

## Project Structure

The project consists of the following files:

* `app.py`: The main application file that handles the Streamlit interface and user interaction.
* `extractor.py`: Contains the core logic for parsing PDF resumes and extracting relevant data using regular expressions and PDF text processing.
* `storage.py`: Provides functionality to save extracted data to a local JSON file and load it when needed.
* `resume_db.json`: Acts as a lightweight local database storing previously extracted resume details.
* `Dockerfile`: Specifies the configuration needed to containerize and run the application using Docker.
* `requirements.txt`: Lists all the Python dependencies required to run the project.
* `README.md`: This documentation file that provides an overview of the project and setup instructions.

---
