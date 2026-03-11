import pandas as pd
from email_utils import send_email
from whatsapp_utils import send_whatsapp
from config import (
    WINBACK_DAYS,
    FEEDBACK_LINK
)



df = pd.read_csv("Mock_guest.csv")


df["Check Out Date"] = pd.to_datetime(df["Check Out Date"], errors="coerce")

today = pd.Timestamp.today().normalize()
df["days_since_checkout"] = (today - df["Check Out Date"]).dt.days

def normalize_phone(phone):
    phone = str(phone).strip()

    if phone.startswith("+"):
        return phone
    else:
        return "+91" + phone





def feedback_message(name):
    return f"""
Dear {name},

We hope you had a pleasant and relaxing stay with us at Ritumbhara Resort.

Your feedback is extremely valuable to us and helps us improve our services.
We would appreciate it if you could take a moment to share your experience.

Feedback link:
{FEEDBACK_LINK}

Warm regards,
Team Ritumbhara Resort
"""


def winback_message(name):
    return f"""
Dear {name},

We hope you are doing well.

It has been a while since your visit to Ritumbhara Resort, and we truly miss hosting you.
As a valued guest, we are pleased to offer you an exclusive 10% discount on your next stay with us.

We look forward to welcoming you back soon.

Warm regards,
Team Ritumbhara Resort
"""



# MAIN AUTOMATION LOOP
emails_sent = 0

for _, row in df.iterrows():

    if pd.isna(row["days_since_checkout"]):
        continue

    name = row["First Name"]
    email = row["Email"]
    days = row["days_since_checkout"]
    raw_phone = row.get("Phone number")
    phone = normalize_phone(raw_phone)


    if days <= 1:
        subject = "Thank you for staying with us – we’d love your feedback"
        message = feedback_message(name)

        send_email(email, subject, message)
        print(f" Feedback email sent to {email}")

        try:
            send_whatsapp(phone, message)
            print(f" Feedback WhatsApp sent to {phone}")
        except Exception as e:
            print(f" WhatsApp failed for {phone}: {e}")

        emails_sent += 1

    elif days >= WINBACK_DAYS:
        subject = "We’re missing you at Ritumbhara Resort"
        message = winback_message(name)

        send_email(email, subject, message)
        print(f" Win-back email sent to {email}")

        try:
            send_whatsapp(phone, message)
            print(f"Win-back WhatsApp sent to {phone}")
        except Exception as e:
            print(f"WhatsApp failed for {phone}: {e}")

        emails_sent += 1

print(f"\n Total emails sent in this run: {emails_sent}")
