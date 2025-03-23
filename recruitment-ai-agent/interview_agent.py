import gradio as gr
import requests

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def conduct_interview(question, candidate_response):
    """
    Conduct an interactive interview using the LLaMA 3 model.
    """
    # Create a prompt for the model
    prompt = f"""
    Candidate Response: {candidate_response}
    Ask a follow-up question or provide feedback.
    """
    
    # Send the prompt to the Ollama API
    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to conduct interview. {str(e)}"