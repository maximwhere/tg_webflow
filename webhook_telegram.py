import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def set_telegram_webhook():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook"
    payload = {
        'url': f"{WEBHOOK_URL}telegram_updates"
    }
    logger.debug(f"Setting webhook: {url}, {payload}")
    response = requests.post(url, json=payload)
    logger.debug(f"Webhook response: {response.status_code}, {response.text}")
    response.raise_for_status()

set_telegram_webhook()
