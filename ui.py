from random import choice

import numpy


# Terminal chat simulation
def chat(processor, model):
    print("Start talking with the bot (type quit to stop)!")
    while True:
        # Get some input from the user
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        # Convert it to a bag of word and get a prediction from the model
        results = model.predict([processor.bag_of_words(inp, processor.pre_processed_words)])
        # Find the most probable intent class
        results_index = numpy.argmax(results)
        tag = processor.labels[results_index]
        # Pick a response from that intent class
        for tg in processor.intents:
            if tg.tag == tag:
                responses = tg.responses
                print(choice(responses))
