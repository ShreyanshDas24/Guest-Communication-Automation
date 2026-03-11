import smtplib
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_APP_PASSWORD


def send_email(to_email, subject, body):
    if not to_email or str(to_email).strip() == "":
        raise ValueError("Invalid recipient email")

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        server.send_message(msg)

    print(f"Email sent to {to_email}")

