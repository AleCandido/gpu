import enum
import dataclasses
import inspect
from collections.abc import Callable

from .elems import cupy_, numba_, tensorflow_, torch_
from . import benchmarks as bs


class Framework(enum.Enum):
    cupy = cupy_
    tensorflow = tensorflow_
    torch = torch_
    numba = numba_


BenchSubject = tuple[Framework] | tuple[(Framework,) * 2]


@dataclasses.dataclass
class DefBench:
    f: Callable
    npars: int

    @classmethod
    def fromfunc(cls, func: Callable):
        return cls(f=func, npars=len(inspect.signature(func).parameters))


class Benchmark(enum.Enum):
    arange = DefBench.fromfunc(bs.arange)
    saxpy = DefBench.fromfunc(bs.saxpy)


shapes = {
    k: (int(x) for x in v)
    for k, v in dict(s=(1e3, 1e3), m=(1e6, 1e6), l=(1e9, 1e9), rect=(1e3, 1e9)).items()
}
