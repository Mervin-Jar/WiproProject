import streamlit as st
from datetime import datetime
from jd_generator import generate_job_description
from resume_ranker import rank_resumes
from email_automation import send_email
from interview_scheduler import schedule_interview
from interview_agent import conduct_interview
from hire_recommendation_agent import hire_recommendation
from sentiment_analyzer import transcribe_audio

# Set page title and layout
st.set_page_config(page_title="Recruitment System", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Job Description Generator", "ResumeRanker", "Email Automation",
    "Interview Scheduler", "Interview Agent", "Hire Recommendation", "Sentiment Analyzer"
])

# Job Description Generator
if page == "Job Description Generator":
    st.title("Job Description Generator")
    job_title = st.text_input("Job Title")
    skills = st.text_input("Required Skills")
    experience_level = st.selectbox("Experience Level", ["Entry-Level", "Mid-Level", "Senior-Level"])
    if st.button("Generate Job Description"):
        jd = generate_job_description(job_title, skills, experience_level)
        st.write("Generated Job Description:")
        st.write(jd)

# ResumeRanker
elif page == "ResumeRanker":
    st.title("ResumeRanker")
    job_description = st.text_area("Job Description", height=200)
    resume_files = st.file_uploader("Upload Resumes", type=["txt", "pdf", "docx"], accept_multiple_files=True)
    if st.button("Rank Resumes"):
        if job_description and resume_files:
            ranked_resumes = rank_resumes(job_description, resume_files)
            st.write("Ranked Resumes:")
            for resume, result, score in ranked_resumes:
                st.write(f"**{resume}** (Score: {score}/10):")
                st.write(result)
        else:
            st.error("Please provide a job description and upload resumes.")

# Email Automation
elif page == "Email Automation":
    st.title("Email Automation")
    to = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Email Body", height=200)
    if st.button("Send Email"):
        result = send_email(to, subject, body)
        st.write(result)

# Interview Scheduler
if "conversation" not in st.session_state:
    st.session_state.conversation = []
    # Add a starting question
    st.session_state.conversation.append("Interviewer: Welcome to the interview! Can you tell me about yourself?")

if page == "Interview Agent":
    st.title("Interview Agent")
    
    # Use a separate key for the widget
    candidate_response = st.text_area("Candidate Response", height=200, key="candidate_input")
    
    def submit_response():
        if st.session_state.candidate_input:
            # Add the candidate's response to the conversation history
            st.session_state.conversation.append(f"Candidate: {st.session_state.candidate_input}")
            
            # Conduct the interview
            result = conduct_interview("", st.session_state.candidate_input)
            st.session_state.conversation.append(f"Interviewer: {result}")
            
            # Clear the input box
            st.session_state.candidate_input = ""
        else:
            st.warning("Please enter a response.")
    
    if st.button("Submit", on_click=submit_response):
        pass  # The callback handles everything
    
    # Display the conversation history
    st.write("### Conversation History")
    for message in st.session_state.conversation:
        st.write(message)
    
    # Add a button to reset the conversation
    if st.button("Reset Conversation"):
        st.session_state.conversation = []
        st.session_state.candidate_input = ""
        st.success("Conversation reset.")

# Hire Recommendation
elif page == "Hire Recommendation":
    st.title("Hire Recommendation")
    interview_transcript = st.text_area("Interview Transcript", height=200)
    if st.button("Evaluate"):
        result = hire_recommendation(interview_transcript)
        st.write(result)

# Sentiment Analyzer
elif page == "Sentiment Analyzer":
    st.title("Sentiment Analyzer")
    
    # Allow users to upload audio or video files
    uploaded_file = st.file_uploader("Upload an audio or video file", type=["wav", "mp3", "mp4"])
    
    if uploaded_file is not None:
        # Display file details
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        
        # Save the uploaded file temporarily
        with open("temp_file", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the file based on its type
        if uploaded_file.type.startswith("audio"):
            # Transcribe audio file
            transcript = transcribe_audio("temp_file")
        else:
            st.error("Unsupported file type. Please upload an audio or video file.")
            transcript = ""
        
        # Display the transcript
        st.write("### Transcript")
        st.write(transcript)