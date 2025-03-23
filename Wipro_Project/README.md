# Recruitment System with AI Agents

This project is a **Recruitment System** powered by AI agents. It uses the **LLaMA 3 model** (via Ollama) and **Gradio** to automate various tasks in the recruitment process, such as generating job descriptions, ranking resumes, scheduling interviews, conducting AI-driven interviews, and analyzing candidate sentiment.

## Features

The system includes the following AI agents:

1. **Job Description Generator**:
   - Generates tailored job descriptions based on job title, required skills, and experience level.

2. **ResumeRanker**:
   - Ranks resumes based on their match with a given job description.

3. **Email Automation**:
   - Simulates sending personalized emails to candidates and hiring teams.

4. **Interview Scheduler**:
   - Simulates scheduling interviews and sending calendar invites.

5. **Interview Agent**:
   - Conducts interactive AI-driven interviews by asking follow-up questions or providing feedback.

6. **Hire Recommendation**:
   - Provides a Hire/No-Hire decision based on interview transcripts.

7. **Sentiment Analyzer**:
   - Analyzes the sentiment of interview transcripts to determine emotional tone and confidence level.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/recruitment-ai-agent.git
   cd recruitment-ai-agent

2. Clone this repository:
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install the required dependencies:
    pip install -r requirements.txt

4. Pull the LLaMA 3 model using Ollama:
    ollama pull llama3

5. Start the Ollama server (if not already running):
    ollama serve

### Running the Application

1. Run the Gradio app:
    python tabbed_interface.py

2. Open your browser and navigate to http://localhost:7860.

3. Use the tabs to interact with the different AI agents.

### Usage

## Job Description Generator
Enter the job title, required skills, and experience level.

Click "Generate Job Description" to create a job description.

## ResumeRanker
Paste the job description (generated from the JD Generator tab or manually entered).

Upload one or more resume files (TXT, PDF, or DOCX).

Click "Rank Resumes" to rank the resumes based on their match with the job description.

## Email Automation
Enter the recipient’s email, subject, and body.

Click "Send Email" to send the email.

## Interview Scheduler
Enter the candidate’s email, interview date, and time.

Click "Schedule Interview" to schedule the interview.

## Interview Agent
Enter an interview question and the candidate’s response.

Click "Submit" to get a follow-up question or feedback.

## Hire Recommendation
Paste the interview transcript.

Click "Evaluate" to get a Hire/No-Hire decision.

## Sentiment Analyzer
Paste the interview transcript.

Click "Analyze" to analyze the sentiment.

### Dependencies
Python libraries: See requirements.txt.

Ollama: For running the LLaMA 3 model locally.

