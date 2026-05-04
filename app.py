from flask import Flask, render_template, request
import requests
app = Flask(__name__)
TOKEN, CHAT_ID = '8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE', '8691740167'
@app.route('/')
def index(): return render_template('index.html')
@app.route('/order', methods=['POST'])
def order():
    uid, pack, method, trx = request.form.get('player_id'), request.form.get('package'), request.form.get('payment_method'), request.form.get('trx_id')
    text = f'🔔 *NEW ORDER*\n👤 UID: `{uid}`\n💎 Pack: {pack}\n💳 Method: {method}\n🔑 TrxID: `{trx}`'
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'Markdown'})
    return '<body style="text-align:center;padding-top:100px;font-family:sans-serif;background:#f5f7fa;"><h1>Success!</h1><a href="/">Home</a></body>'
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
