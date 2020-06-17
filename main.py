from backend.neuronal_modeler import NeuronalModeler
from backend.processor import Processor
from backend.trainer import Trainer
# from frontend.ui import chat
from frontend.ui import telegram_chat

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
    #chat(processor, model)

    # Telegram Chat Bot
    telegram_chat(processor, model)


if __name__ == "__main__":
    main()
