import os
import json
import telebot
import requests
from metrics import Metrics

API_URL = os.environ.get(key="API_URL")
BOT_TOKEN = os.environ.get(key="BOT_TOKEN")
bot = telebot.TeleBot(token=BOT_TOKEN)
metricsdb = Metrics()


def chat(message: str) -> str:

    payload = json.dumps({
        "message": message
    })
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request(method="POST", url=API_URL, headers=headers, data=payload)
    response.raise_for_status()

    return response.text


@bot.message_handler(func=lambda m: True)
def reply_to_message(message):

    print(f"username: {message.from_user.username}, unix_date: {message.date}, text: {message.text}")

    try:
        if message.text.lower().startswith("/hello"):
            response = chat(message=message.text)
            bot.reply_to(message, response)
    except Exception as ex:
       bot.reply_to(message, f"Error: {ex}")

    metric = {
        "username": message.from_user.username,
        "submission_unix_date": message.date
    }

    metricsdb.save_metric(collection="telegram", document=metric)


if __name__ == "__main__":

    bot.infinity_polling()