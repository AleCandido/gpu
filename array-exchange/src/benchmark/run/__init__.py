import argparse
import logging

from .. import meta
from . import dispatch as dispatchm, cupybench, log

_logger = logging.getLogger(__name__)


def validate(args):
    if args.benchmark.value.npars != len(args.framework):
        raise ValueError(
            f"Exactly {args.benchmark.value.npars} frameworks required, "
            f"{len(args.framework)} provided"
        )


def parse() -> tuple[meta.Benchmark, meta.BenchSubject, bool]:
    parser = argparse.ArgumentParser()

    parser.add_argument("benchmark", type=meta.Benchmark.__getitem__)
    parser.add_argument("framework", type=meta.Framework.__getitem__, nargs="+")
    parser.add_argument("-d", "--dispatch", action="store_true")

    args = parser.parse_args()
    validate(args)

    return args.benchmark, args.framework, args.dispatch


def launch(benchmark: meta.Benchmark, frameworks: meta.BenchSubject, dispatch: bool):
    if dispatch:
        start = dispatchm.start_bench
    else:
        start = cupybench.start_bench

    pout = start(benchmark, frameworks)

    __import__("rich").print(
        "\n------------------\n Standard Output:\n------------------"
    )
    __import__("rich").print(pout.out)
    __import__("rich").print("\n-----------------\n Standard Error:\n-----------------")
    __import__("rich").print(pout.err)


def run():
    """Validate arguments, prepend profiler, analyze result.

    Reuse parser from dispatch, since for the time being there is no extra
    option for the profiler and analyzer.

    """
    try:
        launch(*parse())
    except Exception as e:
        _logger.exception(e)
