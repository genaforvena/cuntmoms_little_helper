import datetime
import asyncio
from telegram import Bot
from telegram.error import InvalidToken
import os
import datetime
import asyncio
from telegram import Bot
from telegram.error import InvalidToken

async def fetch_messages_last_week(bot_token, chat_id):
    bot = Bot(token=bot_token)
    current_time = datetime.datetime.now()
    one_week_ago = current_time - datetime.timedelta(days=7)
    messages = []

    try:
        updates = await bot.get_updates()
        for update in updates:
            if update.message and update.message.date > one_week_ago:
                messages.append(update.message)
    except InvalidToken as e:
        print(f"Error: {e}. Please check your bot token.")
        return []

    return messages

if __name__ == "__main__":
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not bot_token:
        bot_token = input("Please enter your bot token: ")
    chat_id = "YOUR_CHAT_ID"
    loop = asyncio.get_event_loop()
    messages = loop.run_until_complete(fetch_messages_last_week(bot_token, chat_id))
    for message in messages:
        print(f"From: {message.from_user.username}, Date: {message.date}, Text: {message.text}")
