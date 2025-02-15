#!/usr/bin/env pyhton3

import requests
import json

# Configuración
ACCESS_TOKEN = "TU_ACCESS_TOKEN"
ITEM_ID = "ID_DE_LA_PUBLICACION"
MESSAGE_TEXT = "Hola, estoy interesado en este producto. ¿Sigue disponible?"

# URL de la API de MercadoLibre para enviar mensajes
url = f"https://api.mercadolibre.com/messages/packs/{ITEM_ID}/sellers/{ACCESS_TOKEN}"

def send_message(url):
    """enviar mensaje"""
    # Encabezados
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Cuerpo del mensaje
    payload = {
        "from": {"user_id": "TU_USER_ID"},
        "to": {"user_id": "ID_DEL_VENDEDOR"},
        "text": MESSAGE_TEXT
    }

    # Enviar la solicitud
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Verificar respuesta
    if response.status_code == 201:
        print("Mensaje enviado con éxito.")
    else:
        print("Error al enviar el mensaje:", response.json())

if __name__ == "__main__":
    send_message()
