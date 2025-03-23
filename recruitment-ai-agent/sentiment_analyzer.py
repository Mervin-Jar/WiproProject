from pydub import AudioSegment
import cv2
import subprocess
import speech_recognition as sr
import requests
# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def analyze_sentiment(transcript):
    """
    Analyze the sentiment of an interview transcript.
    """
    # Create a prompt for the model
    prompt = f"""
    Analyze the sentiment of the following interview transcript:
    {transcript}

    Provide the emotional tone (e.g., positive, negative, neutral) and confidence level (e.g., high, medium, low).
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
        return "Error: Unable to analyze sentiment."

def extract_audio_from_video(video_file, output_audio_file="extracted_audio.wav"):
    """
    Extract audio from a video file using opencv-python and ffmpeg.
    """
    # Use OpenCV to get video properties
    cap = cv2.VideoCapture(video_file)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()
    
    # Use ffmpeg to extract audio
    command = [
        "ffmpeg",
        "-i", video_file,
        "-q:a", "0",
        "-map", "a",
        output_audio_file
    ]
    try:
        subprocess.run(command, check=True)
        return output_audio_file
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e}")
        return None

def transcribe_audio(audio_file):
    """
    Transcribe audio to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            transcript = recognizer.recognize_google(audio)
            return transcript
        except sr.UnknownValueError:
            return "Error: Unable to transcribe audio (unknown value)."
        except sr.RequestError:
            return "Error: Unable to transcribe audio (API request failed)."