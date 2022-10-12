# GPU Frameworks Inspection

Here are investigated a few properties of the current GPGPU programming
frameworks, and the landscape in general.

## Initial

The [original plan](./original-investigation) was to see if there is any
framework:

1. as platform generic as possible (not NVIDIA specific)
2. with C/C++ API
3. allowing to manage memory manually
   - to support performance critical and non-standard use case
4. if possible, with a Python API out of the box

The outcome is that there is no such a framework, but many options each one with
some limitations.

In particular, there are many good and interoperable Python abstractions:

- CuPy
- TensorFlow
- PyTorch
- Numba
- ...

And a couple of standards for tensor exchange between frameworks (Numba's
`__cuda_array_interface__` and DLPack).

For more details see the
[dedicated note](./original-investigation/python/gpu-interop.md).
