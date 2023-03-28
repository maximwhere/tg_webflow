import os
import requests
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telebot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_message_to_chat(message, chat_id):
    bot.send_message(chat_id, text=message)

if __name__ == '__main__':
    data = requests.post('http://localhost:5000/webhook', json={"data": {"Name 2": "John", "Email 2": "john@example.com", "formName": "Lead Form"}}).json()
    message = f"У нас новый лид\n\nФорма: {data['form_name']}\nИмя: {data['name']}\nEmail: {data['email']}"
    send_message_to_chat(message, TELEGRAM_CHAT_ID)
