"""Profiler relying on PyTorch tools.

It is possible to profile benchmarks also using `PyTorch benchmark support
<https://pytorch.org/tutorials/recipes/recipes/benchmark.html#benchmarking-with-torch-utils-benchmark-timer>`_.

In particular, leveraging tools inside `torch.utils.benchmark
<https://pytorch.org/docs/stable/benchmark_utils.html>`_.

"""

from .. import meta


def start_bench(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    raise NotImplementedError
