# gptbot84import os
import os
import urllib.parse
import urllib.request

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": text
    }).encode()

    urllib.request.urlopen(url, data=data)


send_message("Рядовой ЖПТ успешно запущен на сервере.")
