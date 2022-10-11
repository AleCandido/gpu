import dataclasses
from collections.abc import Sequence
from typing import Optional


@dataclasses.dataclass
class ProfilerOutput:
    out: str
    err: Optional[str] = None
    cpu_times: Optional[Sequence[float]] = None
    gpu_times: Optional[Sequence[float]] = None
