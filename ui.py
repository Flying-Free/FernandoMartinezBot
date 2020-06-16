from random import choice

import numpy


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
        # Convert it to a bag of word and get a prediction from the model
        results = model.predict([processor.bag_of_words(inp, processor.pre_processed_words)])
        # Find the most probable intent class
        results_index = numpy.argmax(results)
        tag = processor.labels[results_index]
        # Pick a response from that intent class
        for tg in processor.intents:
            if tg.tag == tag:
                responses = tg.responses
                print("Fernando Martínez: ", choice(responses))
