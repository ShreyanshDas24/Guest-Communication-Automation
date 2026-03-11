import urllib.parse
import urllib.request
import base64
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_FROM
)


def send_whatsapp(to_number, message):

    if not to_number or not str(to_number).startswith("+"):
        raise ValueError(f"Invalid phone number: {to_number}")

    to = f"whatsapp:{to_number}"

    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json"

    data = urllib.parse.urlencode({
        "From": TWILIO_WHATSAPP_FROM,
        "To": to,
        "Body": message
    }).encode("utf-8")

    auth = f"{TWILIO_ACCOUNT_SID}:{TWILIO_AUTH_TOKEN}"
    auth_encoded = base64.b64encode(auth.encode("utf-8")).decode("utf-8")

    req = urllib.request.Request(url, data=data)
    req.add_header("Authorization", f"Basic {auth_encoded}")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            print(f"📱 WhatsApp sent to {to_number}")
            return response_body

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        raise RuntimeError(
            f"Twilio WhatsApp failed ({e.code}): {error_body}"
        )
