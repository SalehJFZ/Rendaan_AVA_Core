import requests
import logging
from config import WHATSAPP,TELEGRAM

WA_API_URL = "https://messenger-api.com/send"
TG_API_URL = "https://messenger-api2.com/send"

def send_response_to_client(media,media_id, reply_to, text):
    if (media == WHATSAPP):
        MESSENGER_API_URL = WA_API_URL
    else:
        MESSENGER_API_URL = TG_API_URL
    try:
        payload = {"media_id": media_id, "reply_to": reply_to, "text": text}
        response = requests.post(MESSENGER_API_URL, json=payload)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"Failed to send response: {e}")
        return False
