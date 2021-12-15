from keras.applications import VGG16


def create_model(img_width, img_height):
    conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(
        img_width, img_height, 3))  # 3 = number of channels in RGB pictures

    return conv_base


def compile_model(model):

    model.compile(optimizer=optimizers.Adam(),
                  loss='binary_crossentropy',
                  metrics=['acc'])


def train_model(model, X):

    model.fit()
