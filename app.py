from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from quiz_service import cargar_preguntas

app = Flask(__name__)
preguntas = cargar_preguntas()
indice_usuario = {}

@app.route("/message", methods=["POST"])
def message():
    numero = request.values.get('From', 'default')
    msg_in = request.values.get('Body', '').strip()

    if numero not in indice_usuario:
        indice_usuario[numero] = 0

    i = indice_usuario[numero]
    if i < len(preguntas):
        pregunta = preguntas[i]["Pregunta"]
        indice_usuario[numero] += 1
    else:
        pregunta = "¡Gracias por completar el cuestionario!"

    resp = MessagingResponse()
    resp.message(pregunta)
    return str(resp)
@app.route('/')
def index():
    return '¡Trading Assistant está corriendo!'
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
