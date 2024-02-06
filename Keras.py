# 21/01/2024: Looking at some of the features of the Keras library. 

# Backend for using Kears library will be Google JAX. Below are a list of it's 4 main functions:
# grad: automatic differentiation
# jit: compilation
# vmap: auto-vectorization
# pmap: SPMD programming

import numpy as np
import os

os.environ["KERAS_BACKEND"] = "jax"

# Note that Keras should only be imported after the backend
# has been configured. The backend cannot be changed once the
# package is imported.
import keras

# Next, we will look at what is known as an MNIST convnet, MNIST is just a collection of, in our case, handwritten digits to use as our classifier set. 

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# Print results
print("x_train shape:", x_train.shape)
print("y_train shape:", y_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# Now that we have our data set, we now setup our convnet model. Here we are using the Sequential model in Keras. 

# Model parameters
num_classes = 10
input_shape = (28, 28, 1)

model = keras.Sequential(
    [
        keras.layers.Input(shape=input_shape), # class InputLayer: Layer to be used as an entry point into a Network (a graph of layers).
                                               # class InputSpec: Specifies the rank, dtype and shape of every input to a layer.
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),    # class Conv2D: 2D convolution layer (e.g. spatial convolution over images).
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),    # class MaxPooling2D: Max pooling operation for 2D spatial data.
        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
        keras.layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
        keras.layers.GlobalAveragePooling2D(),    # class GlobalAveragePooling2D: Global average pooling operation for spatial data. 
        keras.layers.Dropout(0.5),    # class Dropout: Applies Dropout to the input.
        keras.layers.Dense(num_classes, activation="softmax"),    # class Dense: Just your regular densely-connected NN layer.
    ]
)
# Output model summary
model.summary()

# Compiling model using compile() method

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),    # Computes the crossentropy loss between the labels and predictions. See Information Theory definition. 
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    metrics=[
        keras.metrics.SparseCategoricalAccuracy(name="acc"),
    ],
)

# Training and evaluating the model

batch_size = 128
epochs = 20

callbacks = [
    keras.callbacks.ModelCheckpoint(filepath="model_at_epoch_{epoch}.keras"),
    keras.callbacks.EarlyStopping(monitor="val_loss", patience=2),
]

model.fit(
    x_train,
    y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.15, # 15% validation split
    callbacks=callbacks,
)
score = model.evaluate(x_test, y_test, verbose=0)

model.save("final_model.keras")                        # Save model
model = keras.saving.load_model("final_model.keras")   # Load model
predictions = model.predict(x_test)                    # Query model predictions

# Will now use Keras, subclassing the model class as oppossed to using the sequential class. 

class MyModel(keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = keras.layers.Dense(32, activation="relu")
        self.dense2 = keras.layers.Dense(5, activation="softmax")

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)

model = MyModel()
