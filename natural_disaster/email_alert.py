import smtplib
import os
from email.mime.text import MIMEText
import re
# sauz xooq bdte cmnq
# Load credentials from environment variables for security
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "ayush975600@gmail.com")  # Your Gmail
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "sauz xooq bdte cmnq")  # Use an App Password (DO NOT HARD CODE!)
RECIPIENT_EMAILS = os.getenv("RECIPIENT_EMAILS", "sistlaanupam@gmail.com").split(",")  # Comma-separated emails



# Function to validate email format
def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email)

def send_email_alert(subject, message):
    # Check if environment variables are set
    if not SENDER_EMAIL or not SENDER_PASSWORD or not RECIPIENT_EMAILS:
        print("❌ ERROR: Missing email credentials. Ensure environment variables are set.")
        return

    # Validate recipient emails
    valid_recipients = [email for email in RECIPIENT_EMAILS if is_valid_email(email)]
    if not valid_recipients:
        print("❌ ERROR: No valid recipient emails found!")
        return

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(valid_recipients)  # Support multiple recipients

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, valid_recipients, msg.as_string())
        print(f"✅ Email Alert Sent Successfully to {', '.join(valid_recipients)}!")
    except smtplib.SMTPAuthenticationError:
        print("❌ ERROR: Authentication failed. Check your Google App Password.")
    except smtplib.SMTPRecipientsRefused:
        print("❌ ERROR: Recipient email addresses were refused.")
    except smtplib.SMTPException as e:
        print(f"❌ ERROR: Failed to send email - {e}")

# 🚀 Automatically send a test email when this script runs
if __name__ == "__main__":
    print("🔄 Sending test email...")
    send_email_alert("🚨 TEST ALERT: Disaster Prediction System", "This is a test email to verify the system is working.")
