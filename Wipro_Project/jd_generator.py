import gradio as gr
import requests

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_job_description(job_title, skills, experience_level):
    """
    Generate a job description using the LLaMA 3 model.
    """
    # Create a prompt for the model
    prompt = f"""
    Generate a detailed job description for the following role:
    - Job Title: {job_title}
    - Required Skills: {skills}
    - Experience Level: {experience_level}

    Include responsibilities, qualifications, and preferred skills.
    """
    
    # Send the prompt to the Ollama API
    data = {
        "model": "llama3",  # Use the LLaMA 3 model
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to generate job description."