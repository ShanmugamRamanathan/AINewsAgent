import os
import requests

def send_telegram_message(message):
    bot_token = os.environ.get('bot_token')
    chat_id = os.environ.get('chat_id')
    max_length = 4096
    message_parts = [message[i:i+max_length] for i in range(0, len(message), max_length)]

    for part in message_parts:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": part
        }
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
        else:
            print(f"Sent message part: {part[:50]}...")
