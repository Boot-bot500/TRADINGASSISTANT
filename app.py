from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from quiz_service import cargar_preguntas

app = Flask(__name__)
preguntas = cargar_preguntas()
indice_usuario = {}

@app.route("/message", methods=["POST"])
def message():
    from_number = request.values.get('From', 'desconocido')
    incoming_msg = request.values.get('Body', '').strip()

    print(f"Mensaje recibido de {from_number}: {incoming_msg}")

    resp = MessagingResponse()
    resp.message("Hola, gracias por tu mensaje.")
    return str(resp)
@app.route('/')
def index():
    return '¡Trading Assistant está corriendo!'
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
