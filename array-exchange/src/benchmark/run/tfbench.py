"""Profiler relying on TensorFlow tools.

It is possible to profile benchmarks also using `TensorFlow benchmark support
<https://www.tensorflow.org/api_docs/python/tf/test/Benchmark>`_.

"""

from .. import meta


def start_bench(benchmark: meta.Benchmark, frameworks: meta.BenchSubject):
    raise NotImplementedError
