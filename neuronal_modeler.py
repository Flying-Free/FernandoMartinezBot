import tensorflow
import tflearn

class NeuronalModeler:

    def modeling(self, training, output):
        global model
        tensorflow.reset_default_graph()
        # Input layer
        net = tflearn.input_data(shape=[None, len(training[0])])
        # Hidden layers
        net = tflearn.fully_connected(net, 7)
        net = tflearn.fully_connected(net, 7)
        # Output layer, with activation function softmax
        # that will give a probability to each neuron
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        # Type of neuronal network DNN
        model = tflearn.DNN(net)