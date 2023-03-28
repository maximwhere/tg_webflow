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

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
app = Flask(__name__)

def send_message_to_chat(message, chat_id):
    time.sleep(1)  # Добавляем задержку в 1 секунду между запросами, а то ебучая телега блочит меня
    bot.send_message(chat_id, text=message)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    form_data = data['data']
    name = form_data['Name 2']
    email = form_data['Email 2']

    message = f"У нас новый лид\n\nФорма: {form_data['formName']}\nИмя: {name}\nEmail: {email}"
    send_message_to_chat(message, TELEGRAM_CHAT_ID)

    return 'OK'

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv('WEBHOOK_URL'))
    app.run(debug=True, host='0.0.0.0', port=5000)
