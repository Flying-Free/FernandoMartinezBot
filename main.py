from model.neuronal_modeler import NeuronalModeler
from model.processor import Processor
from model.trainer import Trainer
from ui import chat

def main():
    # Process input data
    processor = Processor()
    training, output = processor.execute()

    # Developing the model
    m = NeuronalModeler()
    model = m.modeling(output=output, training=training)

    # Training
    Trainer().train(model=model, training=training, output=output)

    # UI that will be replaced with the Telegram Bot
    chat()


if __name__ == "__main__":
    main()
