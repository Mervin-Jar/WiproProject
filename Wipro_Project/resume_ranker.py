import requests
import PyPDF2
from docx import Document

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def extract_text_from_file(file):
    """
    Extract text from a file (TXT, PDF, or DOCX).
    """
    if file.name.endswith(".pdf"):
        # Extract text from PDF
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.name.endswith(".docx"):
        # Extract text from DOCX
        doc = Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    elif file.name.endswith(".txt"):
        # Read text from TXT
        return file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file format. Please upload a TXT, PDF, or DOCX file.")

def rank_resumes(job_description, resume_files):
    """
    Rank resumes based on their match with the job description.
    """
    ranked_resumes = []
    for file in resume_files:
        try:
            resume_text = extract_text_from_file(file)
            prompt = f"""
            Evaluate how well the following resume matches the job description:
            
            Job Description:
            {job_description}

            Resume:
            {resume_text}

            Provide a score out of 10 and a brief explanation.
            """
            data = {
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(OLLAMA_API_URL, json=data)
            if response.status_code == 200:
                response_text = response.json()["response"]
                # Extract the score from the response (if available)
                if "Score:" in response_text:
                    score = float(response_text.split("Score: ")[1].split("/")[0])
                else:
                    score = 0  # Default score if no score is found
                ranked_resumes.append((file.name, response_text, score))
            else:
                ranked_resumes.append((file.name, "Error: Unable to evaluate resume.", 0))
        except Exception as e:
            ranked_resumes.append((file.name, f"Error processing file: {str(e)}", 0))
    
    # Sort resumes by score
    ranked_resumes.sort(key=lambda x: x[2], reverse=True)
    return ranked_resumes