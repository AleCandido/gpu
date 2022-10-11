"""Profiler relying on ``cupyx.profiler.benchmark``.

Basic profiler, but working also for the other frameworks.

Limited to performances (only CPU and GPU overall time, no more fine-grained),
no memory information is retrieved.

See `cupyx.profiler.benchmark <https://docs.cupy.dev/en/stable/reference/generated/cupyx.profiler.benchmark.html>`_.

More Info
~~~~~~~~~

To extract more information is possible to use the `Low-level CUDA support
<https://docs.cupy.dev/en/stable/reference/cuda.html>`_ within CuPy.

In particular, it should be possible to get some information about memory usage
by accessing `cupy.cuda.Device.mem_info
<https://docs.cupy.dev/en/stable/reference/generated/cupy.cuda.Device.html#cupy.cuda.Device.mem_info>`_
(even though it won't be granular at all).

Other attributes and other parts of low-level API might provide some additional
information, but it is definitely not worth (with respect to ``nsys``/``ncu``).

"""

import logging

import cupyx.profiler
import cupyx.profiler._time

from . import profiler
from .. import meta

_logger = logging.getLogger(__name__)


def extract(output: cupyx.profiler._time._PerfCaseResult):
    return profiler.ProfilerOutput(
        out=output.to_str(), cpu_times=output.cpu_times, gpu_times=output.gpu_times
    )


def start_bench(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    _logger.info(
        "Running with [underline]cupyx.profiler.benchmark[/]",
        extra=dict(markup=True),
    )

    out = cupyx.profiler.benchmark(
        benchmark.value.f, tuple(f.value for f in frameworks), n_repeat=1000
    )

    prof_out = extract(out)

    return prof_out
