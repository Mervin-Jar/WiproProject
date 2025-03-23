from icalendar import Calendar, Event
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def create_ics_file(candidate_email, interview_time):
    """
    Create an .ics file for the interview event.
    """
    cal = Calendar()
    event = Event()
    event.add("summary", "Interview with Candidate")
    event.add("dtstart", interview_time)
    event.add("dtend", interview_time + timedelta(hours=1))
    event.add("location", "Online")
    event.add("description", "Interview for the open position.")
    event.add("attendee", candidate_email)
    cal.add_component(event)

    with open("interview.ics", "wb") as f:
        f.write(cal.to_ical())

def send_calendar_invite(candidate_email, interview_time):
    """
    Send the .ics file as a calendar invite via email.
    """
    create_ics_file(candidate_email, interview_time)

    # Email setup
    sender_email = "meetmessi90@gmail.com"
    sender_password = "anoi jwzw sfen kigr"
    subject = "Interview Invitation"

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = candidate_email
    msg["Subject"] = subject

    # Attach the .ics file
    with open("interview.ics", "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename=interview.ics",
    )
    msg.attach(part)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, candidate_email, msg.as_string())

def schedule_interview(candidate_email, interview_time):
    """
    Schedule an interview and send a calendar invite.
    """
    try:
        send_calendar_invite(candidate_email, interview_time)
        return f"Calendar invite sent to {candidate_email}!"
    except Exception as e:
        return f"Error scheduling interview: {str(e)}"