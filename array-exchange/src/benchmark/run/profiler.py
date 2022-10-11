import dataclasses
import enum
from collections.abc import Sequence
from typing import Optional

from . import nsys, cupybench, tfbench, torchbench


class Profiler(enum.Enum):
    nsys = nsys
    cupy = cupybench
    tensorflow = tfbench
    torch = torchbench


@dataclasses.dataclass
class ProfilerOutput:
    out: str
    err: Optional[str] = None
    cpu_times: Optional[Sequence[float]] = None
    gpu_times: Optional[Sequence[float]] = None
