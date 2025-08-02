import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт! Я нагадаю дати вітаміни дитині 💊")

@bot.message_handler(commands=['remind'])
def remind_message(message):
    bot.send_message(message.chat.id, "Нагадування встановлено! 🕒 (демо)")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
