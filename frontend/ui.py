from random import choice

import numpy

from backend.telegram import Telegram

def reply(inp, model, processor):
    # Convert it to a bag of word and get a prediction from the model
    results = model.predict([processor.bag_of_words(inp, processor.pre_processed_words)])
    # Find the most probable intent class
    results_index = numpy.argmax(results)
    tag = processor.labels[results_index]
    # Pick a response from that intent class
    for tg in processor.intents:
        if tg.tag == tag:
            responses = tg.responses
            return choice(responses)


# Terminal chat simulation
def chat(processor, model):
    print("Start talking with the bot (type quit to stop)!")
    print("Fernando Martínez: Hello, I am Fernando Martinez and this is Emotion.\n"
          "When I first come to Vice City I feel all lonely, a man on the outside,\n"
          "a foreigner, then I say Fernando, you like to talk a lot so\n"
          "I get a well paid job on the radio and begin to make my name as a\n"
          "successful DJ.  Now I'm not so lonely, but I never forget my roots,\n"
          "I never forget, so I always have a soft spot for Foreigner,\n"
          "I've been waiting is next.")
    while True:
        # Get some input from the user
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        response=reply(inp, model, processor)
        print("Fernando Martínez: ", response)


# Telegram chat
def telegram_chat(processor, model):
    t = Telegram()
    # Variable para almacenar la ID del ultimo mensaje procesado
    ultima_id = 0

    while (True):
        mensajes_diccionario = t.update(ultima_id)
        for i in mensajes_diccionario["result"]:
            # Guardar la informacion del mensaje
            tipo, idchat, nombre, id_update = t.info_mensaje(i)

            # Generar una respuesta dependiendo del tipo de mensaje
            if tipo == "texto":
                texto = t.leer_mensaje(i)
                response = reply(texto, model, processor)
            elif tipo == "sticker":
                response = "What sticker!"
            elif tipo == "animacion":
                response = "I like that GIF!"
            elif tipo == "foto":
                response = "Nice photo! Or how my people say \"Very guapa\""
            elif tipo == "otro":
                response = "Huh?"

            # Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1
            if id_update > (ultima_id - 1):
                ultima_id = id_update + 1

            # Enviar la respuesta
            t.enviar_mensaje(idchat, response)

