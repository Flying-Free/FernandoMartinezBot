from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import nltk
nltk.download('punkt')
import tensorflow
import random
import json
import pickle

# Load data to train the model
with open('intents.json') as file:
    data = json.load(file)
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    # Extract data
    words = []
    labels = []
    docs_x = []
    docs_y = []
    # Stammer, take each word in our pattern and bring it down to the root word
    # to reduce the vocabulary of our model and attempt to find the more general
    # meaning behind sentences.
    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)# return a list of words
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    # Lower words
    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    # Sort words
    words = sorted(list(set(words)))
    # Sort labels
    labels = sorted(labels)


    # Preprocessing data, creating a bag of words
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    # Transform input to numpy
    training = numpy.array(training)
    output = numpy.array(output)

    # Save preprocessing
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# Developing the model
tensorflow.reset_default_graph()
# Input layer
net = tflearn.input_data(shape=[None, len(training[0])])
# Hidden layers
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
# Output layer, with activation function softmax
# that will give a probability to each neuron
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
# Type of neuronal network DNN
model = tflearn.DNN(net)
# Load model
"""try:
    model.load("model.tflearn")

except:"""
# Training model, nepoch=the amount of times that the model
# will see the same information while training
model.fit(training, output, n_epoch=3000, batch_size=8, show_metric=True)
model.save("model.tflearn")


# Generate a bag of words as numpy array from a provided string
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


# Terminal chat simulation
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        # Get some input from the user
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        # Convert it to a bag of word and get a prediction from the model
        results = model.predict([bag_of_words(inp, words)])
        # Find the most probable intent class
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        # Pick a response from that intent class
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
                print(random.choice(responses))

        if(responses==""):
            print("Sorry, but i don't undestand you")



chat()

