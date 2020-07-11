
# Importar librerias
import json
import requests
import os                                              

class Telegram:
    # Variables para el Token y la URL del chatbot
    TOKEN = os.environ['TelegramToken']  # Cambialo por tu token
    URL = "https://api.telegram.org/bot" + TOKEN + "/"

    def update(self, offset):
        # Llamar al metodo getUpdates del bot, utilizando un offset
        respuesta = requests.get(self.URL + "getUpdates" + "?offset=" + str(offset) + "&timeout=" + str(100))

        # Decodificar la respuesta recibida a formato UTF8
        mensajes_js = respuesta.content.decode("utf8")

        # Convertir el string de JSON a un diccionario de Python
        mensajes_diccionario = json.loads(mensajes_js)

        # Devolver este diccionario
        return mensajes_diccionario

    def info_mensaje(self, mensaje):

        # Comprobar el tipo de mensaje
        if "text" in mensaje["message"]:
            tipo = "texto"
        elif "sticker" in mensaje["message"]:
            tipo = "sticker"
        elif "animation" in mensaje["message"]:
            tipo = "animacion"  # Nota: los GIF cuentan como animaciones
        elif "photo" in mensaje["message"]:
            tipo = "foto"
        else:
            # Para no hacer mas largo este ejemplo, el resto de tipos entran
            # en la categoria "otro"
            tipo = "otro"

        # Recoger la info del mensaje (remitente, id del chat e id del mensaje)
        persona = mensaje["message"]["from"]["first_name"]
        id_chat = mensaje["message"]["chat"]["id"]
        id_update = mensaje["update_id"]

        # Devolver toda la informacion
        return tipo, id_chat, persona, id_update

    def leer_mensaje(self, mensaje):
        # Extraer el texto, nombre de la persona e id del último mensaje recibido
        texto = mensaje["message"]["text"]

        # Devolver las dos id, el nombre y el texto del mensaje
        return texto

    def enviar_mensaje(self, idchat, texto):
        # Llamar el metodo sendMessage del bot, passando el texto y la id del chat
        requests.get(self.URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))




