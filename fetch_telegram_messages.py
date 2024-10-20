import datetime
from telegram import Bot

def fetch_messages_last_week(bot_token, chat_id):
    bot = Bot(token=bot_token)
    current_time = datetime.datetime.now()
    one_week_ago = current_time - datetime.timedelta(days=7)
    messages = []

    updates = bot.get_updates()
    for update in updates:
        if update.message and update.message.date > one_week_ago:
            messages.append(update.message)

    return messages

if __name__ == "__main__":
    bot_token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    messages = fetch_messages_last_week(bot_token, chat_id)
    for message in messages:
        print(f"From: {message.from_user.username}, Date: {message.date}, Text: {message.text}")
