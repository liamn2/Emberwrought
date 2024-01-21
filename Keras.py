# 21/01/2024: Looking a tsome of the features of the Keras library. 

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
