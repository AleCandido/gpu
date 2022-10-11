import argparse
import logging
from sys import modules

from . import log, dispatch
from .. import meta

_logger = logging.getLogger(__name__)


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
    launch(*parse())
