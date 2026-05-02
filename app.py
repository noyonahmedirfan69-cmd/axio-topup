from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOKEN = "8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE"
CHAT_ID = "8691740167"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    uid = request.form.get('player_id') or request.form.get('uid')
    pack = request.form.get('package') or request.form.get('pack')
    method = request.form.get('payment_method') or request.form.get('method')
    trx = request.form.get('trx_id') or request.form.get('trx')
    
    text = (
        "🔔 *NEW TOP-UP ORDER*\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Player ID:* `{uid}`\n"
        f"💎 *Package:* {pack}\n"
        f"💳 *Method:* {method}\n"
        f"🔑 *TrxID:* `{trx}`\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "✅ *Check payment!*"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, data=payload)
    except:
        pass

    return """
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; background: #eef2f3; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; max-width: 400px; width: 90%; }
            h1 { color: #2c3e50; }
            p { color: #7f8c8d; }
            .btn { display: inline-block; margin-top: 20px; padding: 12px 30px; background: #27ae60; color: white; text-decoration: none; border-radius: 50px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1 style="color:#f39c12;">Order Pending!</h1>
            <p>Your diamonds will be added within 5-10 minutes.</p>
            <a href="/" class="btn">Back to Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
