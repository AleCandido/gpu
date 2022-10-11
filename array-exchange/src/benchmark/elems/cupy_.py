"""Standardize CuPy interface.

CuPy by default run on GPU (otherwise you would have used NumPy), no need to
explicitly select the device.
It will use the "Current Device". Decorator available to temporarily switch.

See `Basics of CuPy <https://docs.cupy.dev/en/stable/user_guide/basic.html>`_.


"""

import cupy as cp

from .utils import prod


def arange(shape):
    return cp.arange(prod(shape)).reshape(shape)


def random(shape):
    return cp.random.rand(prod(shape)).reshape(shape)


def saxpy(x, y, a):
    return a * x + y
