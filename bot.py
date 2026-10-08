import os
import urllib.parse
import urllib.request
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = os.environ["BOT_TOKEN"]

def telegram(method, data):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    encoded = urllib.parse.urlencode(data).encode()
    with urllib.request.urlopen(url, data=encoded) as response:
        return json.loads(response.read())


class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            update = json.loads(body)

            message = update.get("message", {})
            chat = message.get("chat", {})
            text = message.get("text", "")

            if text:
                chat_id = chat["id"]

                telegram("sendMessage", {
                    "chat_id": chat_id,
                    "text": f"Получено: {text}"
                })

        except Exception as e:
            print("Ошибка:", e)

        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Riadovoy GPT is alive")


port = int(os.environ.get("PORT", 10000))

server = HTTPServer(("0.0.0.0", port), Handler)

print("Рядовой ЖПТ запущен")

server.serve_forever()
