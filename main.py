from random import random

import numpy

from model.neuronal_modeler import NeuronalModeler
from model.processor import Processor
from model.trainer import Trainer

# Process input data
processor = Processor()
training, output = processor.execute()

# TODO: Continue with clean coding, extract general variables
# Developing the model
m = NeuronalModeler()
model = m.modeling(output=output, training=training)
# Load model
"""try:
    model.load("model.tflearn")

except:"""
# Training
Trainer.train(model=model, training=training, output=output)


# Terminal chat simulation
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        # Get some input from the user
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        # Convert it to a bag of word and get a prediction from the model
        results = model.predict([processor.bag_of_words(inp, processor.words)])
        # Find the most probable intent class
        results_index = numpy.argmax(results)
        tag = processor.labels[results_index]
        # Pick a response from that intent class
        for tg in processor.intents["intents"]:
            if tg.tag == tag:
                responses = tg.responses
                print(random.choice(responses))

chat()
