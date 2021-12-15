from tensorflow.keras.callbacks import ModelCheckpoint


def create_checkpoint(checkpoint_path="my_model/model",
                      monitor="val_accuracy",
                      mode="max"):

    return ModelCheckpoint(
        checkpoint_path,
        monitor=monitor,
        verbose=1,
        save_best_only=True,
        save_weights_only=True,
        mode=mode)
