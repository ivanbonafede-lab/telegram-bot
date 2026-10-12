# Telegram Client Request Bot

A Python Telegram bot designed to collect customer contact details and service requests for an electrical installation and renewable energy business.

## Features

- Welcomes customers and guides them through a conversational flow.
- Collects the customer's name and phone number.
- Offers service categories such as electrical installations, photovoltaic systems, quotations, and technical support.
- Uses Telegram reply keyboards to simplify interaction.
- Configures the bot token through an environment variable instead of storing it directly in the source code.

## Technologies

- Python
- python-telegram-bot
- Telegram Bot API
- Environment variables for configuration

## Project structure

- `bot.py` — bot logic and conversation handlers.
- `requirements.txt` — Python dependencies.

## Setup

1. Install Python 3.
2. Clone this repository.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the `TELEGRAM_BOT_TOKEN` environment variable using the token obtained from Telegram's BotFather.
5. Run the bot:

   ```bash
   python bot.py
   ```

## Security

Never commit bot tokens, passwords, or other secrets to version control. Configure credentials through environment variables.

## Status

Portfolio project. Further testing and documentation may be required before production use.
