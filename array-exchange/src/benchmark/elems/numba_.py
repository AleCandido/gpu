"""Standardize Numba interface.

Numba is definitely the most complicated to use, being closer to OpenCL (thus
more low level).
Moving explicitly arrays from memory to device is required, as well as taking
care of the threads workload distribution.

See `CUDA examples <https://numba.readthedocs.io/en/stable/cuda/examples.html>`_.

"""

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
