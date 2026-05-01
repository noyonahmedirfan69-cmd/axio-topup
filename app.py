from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Telegram Configuration
# Replace these with your actual Bot Token and Chat ID
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    player_id = request.form.get('player_id')
    package = request.form.get('package')
    payment_method = request.form.get('payment_method')
    trx_id = request.form.get('trx_id')
    phone_number = request.form.get('phone_number')

    # Telegram Message Format
    message = (
        f"🔔 **New Order Received**\n\n"
        f"🎮 Player ID: {player_id}\n"
        f"📦 Package: {package}\n"
        f"💳 Method: {payment_method}\n"
        f"🔢 TrxID: {trx_id}\n"
        f"📞 Sender Phone: {phone_number}\n"
        f"✅ Status: Pending"
    )
    
    # Sending to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}&parse_mode=Markdown"
    
    try:
        requests.get(url)
        return render_template('success.html', player_id=player_id)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
