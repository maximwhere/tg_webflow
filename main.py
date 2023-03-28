import os
import json
import requests
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telebot
from flask import Flask, request
import time

load_dotenv()
WEBFLOW_SITE_ID = os.getenv('WEBFLOW_SITE_ID')
WEBFLOW_FORM_ID = os.getenv('WEBFLOW_FORM_ID')
WEBFLOW_API_KEY = os.getenv('WEBFLOW_API_KEY')

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
app = Flask(__name__)

def get_last_request_from_webflow():
    url = f"https://api.webflow.com/sites/{WEBFLOW_SITE_ID}/forms/{WEBFLOW_FORM_ID}/submissions"
    headers = {
        "Authorization": f"Bearer {WEBFLOW_API_KEY}",
        "accept-version": "1.0.0",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        submissions = response.json()
        if submissions:
            last_submission = submissions[0]  # Последняя заявка
            return {
                "form_name": last_submission["formName"],
                "name": last_submission["data"]["Name 2"],
                "email": last_submission["data"]["Email 2"],
            }
    return None


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    form_data = data['data']
    name = form_data['Name 2']
    email = form_data['Email 2']

    message = f"У нас новый лид\n\nФорма: {form_data['formName']}\nИмя: {name}\nEmail: {email}"
    send_message_to_chat(message, TELEGRAM_CHAT_ID)

    return 'OK'


def send_message_to_chat(message, chat_id):
    time.sleep(1)  # Добавляем задержку в 1 секунду между запросами, а то ебучая телега блочит меня
    bot.send_message(chat_id, text=message)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv('WEBHOOK_URL'))
    app.run(debug=True, host='0.0.0.0', port=12345)
