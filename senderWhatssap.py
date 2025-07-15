import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def sendWhatssap(body: str, mediaURL: str = None) -> str:
    client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    messageContent = {
        'body': body,
        'from_': os.getenv('TWILIO_WHATSAPP_FROM'),
        'to':   os.getenv('TWILIO_WHATSAPP_TO')
    }
    if mediaURL:
        messageContent['mediaURL'] = [mediaURL]
    return client.messages.create(**messageContent).sid