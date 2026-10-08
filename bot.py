import os
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": text
    }).encode()

    urllib.request.urlopen(url, data=data)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Riadovoy GPT is alive")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()


port = int(os.environ.get("PORT", 10000))

server = HTTPServer(("0.0.0.0", port), Handler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()

send_message("Рядовой ЖПТ снова на связи. Сервер работает.")

while True:
    time.sleep(60)
