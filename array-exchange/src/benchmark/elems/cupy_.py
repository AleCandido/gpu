import cupy as cp

from .utils import prod


def arange(shape):
    return cp.arange(prod(shape)).reshape(shape)


def random(shape):
    return cp.random.rand(prod(shape)).reshape(shape)


def saxpy(x, y, a):
    return a * x + y
