from tensorflow.keras import backend as K
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPool2D, ReLU,\
    Flatten, Dense, Rescaling
from tensorflow.keras.optimizers import SGD

tf.random.set_seed(0)

IMG_SIZE = (299, 299)


def create_model(img_size=IMG_SIZE):
    K.clear_session()

    input_layer = Input(shape=(img_size[0], img_size[1], 1))
    rescaling_layer = Rescaling(scale=1 / 127.5, offset=-1)(input_layer)
    convolutional_1 = Conv2D(
        16,
        kernel_size=3,
        padding="same")(rescaling_layer)
    max_pooling_1 = MaxPool2D(2)(convolutional_1)
    relu_1 = ReLU()(max_pooling_1)
    convolutional_2 = Conv2D(32, kernel_size=3, padding="same")(relu_1)
    max_pooling_2 = MaxPool2D(2)(convolutional_2)
    relu_2 = ReLU()(max_pooling_2)
    convolutional_3 = Conv2D(64, kernel_size=3)(relu_2)
    relu_3 = ReLU()(convolutional_3)
    flatten = Flatten()(relu_3)
    dense = Dense(256, activation="relu")(flatten)
    output_layer = Dense(3, activation="softmax")(dense)

    model = Model(inputs=input_layer, outputs=output_layer)

    return model


def compile_model(model, lr, momentum):

    model.compile(
        optimizer=SGD(
            learning_rate=lr,
            momentum=momentum),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

    return model


def load_weights(model, checkpoint_path):
    model.load_weights(checkpoint_path)


def train_model(model, dataset_train, dataset_val, epochs=5, batch_size=10,
                model_checkpoint=None):

    return model.fit(
        dataset_train,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=dataset_val,
        callbacks=None if model_checkpoint is None else [model_checkpoint])
