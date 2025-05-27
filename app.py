from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from quiz_service import cargar_preguntas

app = Flask(__name__)
preguntas = cargar_preguntas()
indice_usuario = {}

@app.route("/message", methods=["POST"])
def message():
    from_number = request.values.get("From", "desconocido")
    incoming_msg = request.values.get("Body", "").strip()

    print(f"Mensaje recibido de {from_number}: {incoming_msg}")

    # Si el usuario es nuevo, iniciar su índice
    if from_number not in indice_usuario:
        indice_usuario[from_number] = 0

    index = indice_usuario[from_number]

    if index < len(preguntas):
        respuesta = preguntas[index]
        indice_usuario[from_number] += 1
    else:
        respuesta = "Gracias, ya has respondido todas las preguntas."
        del indice_usuario[from_number]  # Reiniciar usuario

    resp = MessagingResponse()
    resp.message(respuesta)
    return str(resp)
@app.route('/')
def index():
    return '¡Trading Assistant está corriendo!'
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
