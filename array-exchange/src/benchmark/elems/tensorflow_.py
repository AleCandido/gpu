import tensorflow as tf

from .utils import prod


def arange(shape):
    return tf.reshape(tf.range(prod(shape)), shape)


def random(shape):
    return tf.random.uniform(shape=shape)


def saxpy(x, y, a):
    return a * x + y
