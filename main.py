from neuronal_modeler import NeuronalModeler
from processor import Processor
from trainer import Trainer

# Process input data
Processor.execute()

# TODO: Continue with clean coding, extract general variables
# Developing the model
NeuronalModeler.modeling(training=training, output=output)
# Load model
"""try:
    model.load("model.tflearn")

except:"""
# Training
Trainer.train(model=model, training= training, output=output)


chat()

