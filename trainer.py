class Trainer:

    def train(model, training, output):
        # Training model, nepoch=the amount of times that the model
        # will see the same information while training
        model.fit(training, output, n_epoch=5000, batch_size=8, show_metric=True)
        model.save("model/model.tflearn")