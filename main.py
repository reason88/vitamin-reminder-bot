import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import schedule
import time
import threading
from datetime import datetime

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = YOUR_CHAT_ID

bot = telebot.TeleBot(TOKEN)

def send_vitamin_reminder(child_name):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("✅ Multivitamins", callback_data=f"{child_name}:Multivitamins"),
        InlineKeyboardButton("✅ D3 + K2", callback_data=f"{child_name}:D3K2"),
        InlineKeyboardButton("✅ Iron", callback_data=f"{child_name}:Iron")
    )
    bot.send_message(
        CHAT_ID,
        f"🕗 {child_name} — vitamins for today:\n• 🟢 Multivitamins\n• 🌞 D3 + K2\n• 🔴 Iron\n\nTap each when given ⬇️",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    name, vitamin = call.data.split(":")
    user = call.from_user.first_name
    response = f"✅ {name} — {vitamin} given (marked by: {user})"
    bot.send_message(CHAT_ID, response)

def job():
    send_vitamin_reminder("Martin")
    send_vitamin_reminder("Nicole")

schedule.every().day.at("09:00").do(job)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule).start()
print("Bot is running...")
bot.infinity_polling()
