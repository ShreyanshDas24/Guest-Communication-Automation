# Hotel Guest Communication Automation

This project automates guest communication for hotels using Python.

The system sends personalized messages to guests after checkout, including feedback requests and win-back offers, using Email (SMTP) and WhatsApp (Twilio API).


## Features
- Automated feedback request after guest checkout.
- Automated win-back campaign after inactivity
- Unicast messaging (one message per guest)
- CSV-based guest data processing
- CSV-based guest data processing
- Event-based automation logic

## Technologies
- Python
- Pandas
- Twilio API
- SMTP (Gmail)

## How the System Works

1. Load guest data from CSV
2. Calculate days since checkout
3. Trigger messages:
   - Feedback request: sent on checkout day
   - Win-back offer: sent in after inactivity period
4. Send via Email and WhatsApp.


