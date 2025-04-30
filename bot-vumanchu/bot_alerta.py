from flask import Flask, request
import requests

app = Flask(__name__)

# Substitua pelo seu token de bot
TELEGRAM_BOT_TOKEN = '8087351438:AAFi8mQyu7VdVQqAXjvZiJln8NheCAYIR6Q'
# Substitua pelo seu chat_id (pode ser seu ID ou ID do grupo)
TELEGRAM_CHAT_ID = '1153866750'

@app.route('/', methods=['POST'])
def alert():
    data = request.json
    # Pega a mensagem que vem do TradingView
    message = data.get('message', 'Alerta recebido do TradingView!')

    # Monta a URL para enviar a mensagem pelo bot
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }

    # Envia o alerta para o Telegram
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return 'Mensagem enviada!', 200
    else:
        return f'Erro ao enviar: {response.text}', 400

@app.route('/', methods=['GET'])
def home():
    return 'Servidor rodando!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
