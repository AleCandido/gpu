import argparse
import logging
import subprocess

import cupyx.profiler

from . import profiler
from .. import meta

_logger = logging.getLogger(__name__)


def extract(output: str):
    return profiler.ProfilerOutput(out=output)


def start_bench(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    command = [
        *"nsys profile".split(),
        *"-c cudaProfilerApi".split(),
        *"poetry run dispatch".split(),
        benchmark.name,
        *(f.name for f in frameworks),
    ]

    _logger.info(
        "Running command:\n\t[magenta]" + " ".join(command) + "[/]",
        extra=dict(markup=True),
    )

    sp = subprocess.run(command, capture_output=True)
    prof_out = extract(sp.stdout.decode())
    prof_out.err = sp.stderr.decode()

    return prof_out


def parse() -> tuple[meta.Benchmark, meta.BenchSubject]:
    parser = argparse.ArgumentParser()

    parser.add_argument("benchmark", type=meta.Benchmark.__getitem__)
    parser.add_argument("framework", type=meta.Framework.__getitem__, nargs="+")

    args = parser.parse_args()

    return args.benchmark, args.framework


def launch(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    names = tuple(f.name for f in frameworks)
    modules = tuple(f.value for f in frameworks)

    _logger.info(f"Running {benchmark.name}" + str(names))
    benchmark.value.f(*modules)


def run():
    """Dispatch individual benchmark."""
    with cupyx.profiler.profile():
        launch(*parse())
