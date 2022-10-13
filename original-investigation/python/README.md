# Python

It is by far the richest language as of:

- machine learning frameworks
- user-friendly libraries
- feature complete libraries
- libraries interoperability

Unfortunately, we have to rely on whatever it is implemented, and possibly run
everything from Python, without the chance of passing control to C++ libraries.

## CuPy

[CuPy](https://cupy.dev/) is a notable example in this is sense, since it is:

- user-friendly, with a NumPy-like (and SciPy-like) library
  - including easy installation with `pip` (plus of course CUDA dependencies)
- complete: it already has
  [plenty of functions](https://docs.cupy.dev/en/stable/reference/comparison.html)
- Python
  [interoperable](https://docs.cupy.dev/en/stable/user_guide/interoperability.html),
  supporting a (CUDA) standard interface (so not so standard at the end of the
  day - but makes possible to talk with quite a good number of )
- [extendable](https://docs.cupy.dev/en/stable/user_guide/kernel.html), so we
  don't have to rely only on available primitives, if needed, we can add our own

It seems to be still mainly
[limited to CUDA](https://docs.cupy.dev/en/stable/install.html#requirements),
but
[on its way for AMD](https://docs.cupy.dev/en/stable/install.html#using-cupy-on-amd-gpu-experimental).

Unfortunately, it is **Python interoperable**, but not with C++. This means that
there is no easy documented way to pass control over arrays to a C++ library.

My best option at the moment is to copy them in memory, pass through memory, and
copy back to GPU in the C++ library. Quite a poor interface...

But still need to
[investigate deeper](https://stackoverflow.com/questions/66989716/passing-cupy-cuda-device-pointer-to-pybind11).

## OpenCL

Another interesting project is
[PyOpenCL](https://dmlc.github.io/dlpack/latest/c_api.html), since it provides
access to the OpenCL primitives, allowing fine-tuning of implementation details,
but directly from Python itself.

Essentially, the project consist in bindings for a generic OpenCL
implementation, to be
[installed separately](https://documen.tician.de/pyopencl/misc.html#installation).

The project essentially consist in bindings, and it is available on
[GitHub](https://github.com/inducer/pyopencl).
