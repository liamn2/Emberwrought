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
