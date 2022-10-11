"""Profiler based on `nsys
<https://docs.nvidia.com/nsight-systems/UserGuide/index.html>`_.

NVIDIA deprecated ``nvprof`` and *Visual Profiler* in favor of new tools:

    - `NVIDIA Nsight Systems <https://developer.nvidia.com/nsight-systems>`_,
      corresponding to ``nsys`` CLI
    - `NVIDIA Nsight Compute <https://developer.nvidia.com/nsight-compute>`_,
      corresponding to ``ncu`` CLI

A comparison between the two and the old ones can be found on the old Profiler
guide, in the `Migrating section
<https://docs.nvidia.com/cuda/profiler-users-guide/index.html#migrating-to-nsight-tools>`_
(together with a concise description of the two, difficult to find elsewhere).

"""

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
