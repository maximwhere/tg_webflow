# Описание

Это приложение слушает входящие POST запросы на /webhook, получает json и отправляет сообщение в чат телеграмм.

# Установка и запуск

1. Клонируйте репозиторий: `git clone https://github.com/maximwhere/tg_webflow.git`
2. Перейдите в папку проекта: `cd tg_webflow`
3. Установите необходимые зависимости: `pip install -r requirements.txt`
4. Создайте файл `.env` и укажите в нем следующие переменные окружения:

    ```
    TELEGRAM_BOT_TOKEN=your_bot_token
    TELEGRAM_CHAT_ID=your_chat_id
    ```
    
5. Запустите приложение: `python main.py`

# Переменные окружения

- `TELEGRAM_BOT_TOKEN` - токен бота телеграмм (можно получить у @BotFather).
- `TELEGRAM_CHAT_ID` - ID чата, в который будут приходить уведомления. Чтобы узнать ID чата, напишите в чат боту @userinfobot.
