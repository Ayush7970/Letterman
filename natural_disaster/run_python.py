import smtplib

SENDER_EMAIL = "ayush975600@gmail.com"
SENDER_PASSWORD = "sauz xooq bdte cmnq"

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Login Successful!")
except Exception as e:
    print(f"❌ ERROR: {e}")
