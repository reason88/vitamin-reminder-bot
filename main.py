from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'YOUR_BOT_TOKEN'
WEBHOOK_SECRET = 'your_webhook_secret'
CHAT_ID = -4828774361

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

def send_vitamin_reminder(child_name):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(f"✅ Multivitamins", callback_data=f"{child_name}:Multivitamins"),
        InlineKeyboardButton(f"✅ D3 + K2", callback_data=f"{child_name}:D3K2"),
        InlineKeyboardButton(f"✅ Iron", callback_data=f"{child_name}:Iron")
    )
    bot.send_message(CHAT_ID, f"🕗 {child_name} — vitamins for today:
• 🟢 Multivitamins
• 🌞 D3 + K2
• 🔴 Iron

Tap each when given ⬇️", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    name, vitamin = call.data.split(":")
    user = call.from_user.first_name
    bot.answer_callback_query(call.id, f"{vitamin} marked for {name} by {user}")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

@app.route(f"/{WEBHOOK_SECRET}", methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    return 'Bot is running!', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
