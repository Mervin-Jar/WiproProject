import gradio as gr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP server details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # For TLS
SENDER_EMAIL = "meetmessi90@gmail.com"  # Replace with your Gmail address
SENDER_PASSWORD = "anoi jwzw sfen kigr"  # Replace with your Gmail password or app password

def send_email(to, subject, body):
    """
    Send an email using Gmail's SMTP server.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS encryption
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the SMTP server
            server.sendmail(SENDER_EMAIL, to, msg.as_string())  # Send the email

        return f"Email sent successfully to {to}!"
    except Exception as e:
        return f"Error sending email: {str(e)}"

def email_automation_ui(to, subject, body):
    send_email(to, subject, body)
    return f"Email sent to {to} with subject: {subject}"