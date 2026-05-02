from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Telegram Configuration
# Replace these with your actual Bot Token and Chat ID
BOT_TOKEN = "8567544194:AAHbkTbjnkTsN2iNznlN5Ek1TtlN_R0ncTE"
CHAT_ID = "8691740167"

@app.route('/')
def index():
    return render_template('index.html')
    return """
    <div style="text-align:center; margin-top:100px; font-family: sans-serif; background-color: #f4f4f4; padding: 20px;">
        <div style="background: white; display: inline-block; padding: 40px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h1 style="color: #f39c12;">Order Pending!</h1>
            <p style="font-size: 18px; color: #333;">Apnar order ti amra peyechi. Ekhon processing-e ache.</p>
            <p style="color: #666;">Onugroho kore 5-10 minute opekkha korun.</p>
            <br>
            <a href="/" style="background: #27ae60; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Back to Home</a>
        </div>
    </div>
    """

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
