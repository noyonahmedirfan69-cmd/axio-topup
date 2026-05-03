echo "from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOKEN = '8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE'
CHAT_ID = '8691740167'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    uid = request.form.get('player_id')
    pack = request.form.get('package')
    method = request.form.get('payment_method')
    trx = request.form.get('trx_id')
    
    text = (
        '🔔 *NEW ORDER*\n'
        f'👤 UID: \`{uid}\`\n'
        f'💎 Pack: {pack}\n'
        f'💳 Method: {method}\n'
        f'🔑 TrxID: \`{trx}\`'
    )
    
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'Markdown'})
    
    return '<body style=\"text-align:center;padding-top:100px;font-family:sans-serif;background:#f0f4f8;\"><h1>Order Success!</h1><p>Wait 5-10 mins.</p><a href=\"/\">Back to Home</a></body>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)" > app.py

