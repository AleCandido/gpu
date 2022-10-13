# GPU arrays interoperability

There two rather popular interfaces in Python to exchange tensors between
different frameworks.

## Interfaces

### CUDA Array Interface

Defined by the Numba package,
[specs in Numba docs](https://numba.readthedocs.io/en/stable/cuda/cuda_array_interface.html).

Supported by:

- Numba
- CuPy
- PyTorch
- JAX
- [and more...](https://numba.readthedocs.io/en/stable/cuda/cuda_array_interface.html#interoperability)

Pay attention to JAX: despite being an experimental framework is very good on
its own, but it is also built on top of XLA, i.e. the same Accelerated Linear
Algebra library backing TensorFlow (that is not explicitly listed as supporting
CUDA Array Interface).

### DLPack

This is a [standalone specification](https://dmlc.github.io/dlpack/latest/), for
both [CPU](./cpu-interop) and GPU.

Supported (on GPU) by:

- CuPy
- TensorFlow
- PyTorch
- [and more...](https://dmlc.github.io/dlpack/latest/#purpose)

Designed for cross hardware.

The full specification consist of a
[Python](https://dmlc.github.io/dlpack/latest/python_spec.html) and a
[C](https://dmlc.github.io/dlpack/latest/c_api.html) part. The main API is
defined in C, but it also specifies how Python frameworks should exchange the
information required by the underlying C implementation.

## Guides

CuPy has a pretty good
[guide about interoperability](https://docs.cupy.dev/en/stable/user_guide/interoperability.html),
for both CUDA Array Interface and DLPack, with examples for the different
frameworks (and useful notes).
