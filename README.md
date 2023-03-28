# Telegram Bot для получения уведомлений о новых заявках в Webflow

Этот Telegram бот используется для получения уведомлений о новых заявках, отправленных через форму на вашем сайте, построенном на платформе Webflow. Бот получает информацию о заявках через Webflow API и отправляет уведомление в чат Telegram с помощью Telegram API.

## Установка и запуск

Для запуска бота необходимо выполнить следующие шаги:

### Склонировать репозиторий:
```
git clone https://github.com/maximwhere/tg_webflow.git
```
### Установить зависимости с помощью утилиты pip:
```
pip install -r requirements.txt
```
### Задать необходимые переменные окружения в файле .env:
```
WEBFLOW_API_TOKEN=<your Webflow API token>
TELEGRAM_BOT_TOKEN=<your Telegram bot token>
TELEGRAM_CHAT_ID=<your Telegram chat ID>
WEBHOOK_URL=<your webhook URL>
WEBFLOW_SITE_ID=<your Webflow site ID>
WEBFLOW_FORM_ID=<your Webflow form ID>
```
### Запустить бот с помощью команды:
``` 
python main.py
```
## Использование

Как только бот будет запущен, он начнет получать уведомления о новых заявках, отправленных через форму на вашем сайте, построенном на платформе Webflow. Бот будет отправлять уведомление в чат Telegram, который вы указали в качестве TELEGRAM_CHAT_ID в файле .env.
