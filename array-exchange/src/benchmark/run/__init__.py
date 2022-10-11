import logging
import subprocess

from . import log, dispatch
from .extract import ProfilerOutput
from .. import meta

_logger = logging.getLogger(__name__)


def launch(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    command = [
        *"nsys profile".split(),
        *"-c cudaProfilerApi".split(),
        #  "ncu",
        #  *"-o timeline".split(),
        #  *"--target-processes all".split(),
        *"poetry run dispatch".split(),
        benchmark.name,
        *(f.name for f in frameworks),
    ]

    _logger.info(
        "Running command:\n\t[magenta]" + " ".join(command) + "[/]",
        extra=dict(markup=True),
    )

    if benchmark.value.npars != len(frameworks):
        raise ValueError(
            f"Exactly {benchmark.value.npars} frameworks required, "
            f"{len(frameworks)} provided"
        )

    sp = subprocess.run(command, capture_output=True)
    prof_out = ProfilerOutput.extract(sp.stdout.decode())
    __import__("rich").print(prof_out.full)
    __import__("rich").print(sp.stderr.decode())


def run():
    """Validate arguments, prepend profiler, analyze result.

    Reuse parser from dispatch, since for the time being there is no extra
    option for the profiler and analyzer.

    """
    try:
        launch(*dispatch.parse())
    except Exception as e:
        _logger.exception(e)
