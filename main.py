import requests
from datetime import datetime

# Твій токен і chat_id (вставлені напряму в код)
TOKEN = "7994163357:AAEJ4xyXcaX1EY19jebXulCAnystxCbsscE"
CHAT_ID = -4828774361

# Повідомлення
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
text = f"🕘 {now}\nНагадування: дайте дітям вітаміни!"

# Надсилання повідомлення
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": text
}

response = requests.post(url, data=payload)

# Лог
if response.status_code == 200:
    print("✅ Повідомлення надіслано")
else:
    print(f"❌ Помилка: {response.status_code} - {response.text}")
