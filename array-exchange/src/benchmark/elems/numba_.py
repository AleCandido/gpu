#  import numba as nb
import numpy as np
from numba import cuda

from .utils import prod


def arange(shape):
    return cuda.to_device(np.arange(prod(shape)).reshape(shape))


def random(shape):
    return cuda.to_device(np.random.rand(prod(shape)).reshape(shape))


def saxpy(x, y, a):
    out = cuda.device_array_like(x)
    _saxpy.forall(len(x))(x, y, a, out)
    return out


@cuda.jit
def _saxpy(x, y, a, out):
    i = cuda.grid(1)
    size = len(x)

    if i < size:
        out[i] = a * x[i] + y[i]
