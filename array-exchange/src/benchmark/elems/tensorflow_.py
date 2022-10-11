"""Standardize TensorFlow interface.

Tensorflow by default run on GPU, no need to explicitly select the device.
Decorator available to temporarily switch.

See `GPU guide <https://www.tensorflow.org/guide/gpu>`_.

"""

import tensorflow as tf

from .utils import prod


def arange(shape):
    return tf.reshape(tf.range(prod(shape)), shape)


def random(shape):
    return tf.random.uniform(shape=shape)


def saxpy(x, y, a):
    return a * x + y
