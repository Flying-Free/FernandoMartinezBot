from nltk.stem.lancaster import LancasterStemmer

from model.intent import Intent

stemmer = LancasterStemmer()
import numpy
import nltk

nltk.download('punkt')
import json
import pickle


class Processor:
    intents = []
    pre_processed_words = []
    labels = []
    docs_x = []
    docs_y = []

    def __init__(self):
        # Load data to train the model
        with open('input/intents.json') as file:
            data = json.load(file)
        # Stammer, take each word in our pattern and bring it down to the root word
        # to reduce the vocabulary of our model and attempt to find the more general
        # meaning behind sentences.
        for i in data['intents']:
            intent = Intent(i)
            self.intents.append(intent)
            for pattern in intent.patterns:
                post_processed_words = nltk.word_tokenize(pattern)  # return a list of words
                self.pre_processed_words.extend(post_processed_words)
                self.docs_x.append(post_processed_words)
                self.docs_y.append(intent.tag)
            if intent.tag not in self.labels:
                self.labels.append(intent.tag)

    def execute(self):
        self.__extract_data()

        try:
            with open("../input/data.pickle", "rb") as f:
                self.pre_processed_words, self.labels, training, output = pickle.load(f)
            return training, output
        except:
            training, output = self.__process_input()
            # Save pre-processing
            with open("../input/data.pickle", "wb") as f:
                pickle.dump((self.pre_processed_words, self.labels, training, output), f)
            return training, output

    # Generate a bag of words as numpy array from a provided string
    def bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

    def __extract_data(self):
        # Lower words
        self.pre_processed_words = [stemmer.stem(w.lower()) for w in self.pre_processed_words if w != "?"]
        # Sort words
        self.pre_processed_words = sorted(list(set(self.pre_processed_words)))
        # Sort labels
        self.labels = sorted(self.labels)

    def __process_input(self):
        training = []
        output = []
        out_empty = [0 for _ in range(len(self.labels))]
        for x, doc in enumerate(self.docs_x):
            bag = []
            post_processed_words = [stemmer.stem(w.lower()) for w in doc]
            for w in self.pre_processed_words:
                if w in post_processed_words:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[self.labels.index(self.docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)

        # Transform input to numpy
        return numpy.array(training), numpy.array(output)
