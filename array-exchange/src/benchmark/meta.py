import enum

from .elems import cupy_, tensorflow_, torch_, numba_


class Framework(enum.Enum):
    cupy = cupy_
    tensorflow = tensorflow_
    torch = torch_
    numba = numba_


shapes = {
    k: (int(x) for x in v)
    for k, v in dict(s=(1e3, 1e3), m=(1e6, 1e6), l=(1e9, 1e9), rect=(1e3, 1e9))
}
