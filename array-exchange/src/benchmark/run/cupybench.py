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
        "Running with `cupyx.profiler.benchmark`",
        extra=dict(markup=True),
    )

    out = cupyx.profiler.benchmark(
        benchmark.value.f, tuple(f.value for f in frameworks), n_repeat=1000
    )

    prof_out = extract(out)

    return prof_out
