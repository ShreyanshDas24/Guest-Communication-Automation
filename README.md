# Hotel Guest Communication Automation

This project automates guest communication for hotels using Python.

It sends:
- Feedback requests after checkout
- Win-back offers after inactivity

Messages are sent via:
- Email (SMTP)
- WhatsApp (Twilio API)

## Features
- Unicast guest messaging
- CSV-based guest data processing
- WhatsApp sandbox integration
- Event-based automation logic

## Technologies
- Python
- Pandas
- Twilio API
- SMTP (Gmail)

## How it works

1. Load guest data from CSV
2. Calculate days since checkout
3. Trigger messages:
   - Feedback request
   - Win-back offer
4. Send via Email and WhatsApp


Credentials are not included in this repository.