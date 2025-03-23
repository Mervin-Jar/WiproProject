import gradio as gr
import requests

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def hire_recommendation(interview_transcript):
    """
    Provide a Hire/No-Hire decision based on the interview transcript.
    """
    # Create a prompt for the model
    prompt = f"""
    Interview Transcript:
    {interview_transcript}

    Provide a Hire/No-Hire decision with strengths and weaknesses.
    """
    
    # Send the prompt to the Ollama API
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to generate recommendation."