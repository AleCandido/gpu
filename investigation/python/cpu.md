# CPU arrays

Also for CPU arrays there are standards, and interoperability.

Standards are mainly based on NumPy, extending support for its computation
model, or interoperability with its arrays:

- [A common API for array and tensor Python
  libraries](https://data-apis.org/array-api/)
  - its
    [NumPy's implementation](https://numpy.org/doc/stable/reference/array_api.html)
- [NumPy's `__array_interface__`](https://numpy.org/doc/stable/reference/arrays.interface.html#python-side)

NumPy also exposes an interface to define external array that support its
functions, the
[`__array_function__`](https://numpy.org/doc/stable/reference/arrays.classes.html?highlight=__#numpy.class.__array_function__)
interface.

Also [DLPack](https://dmlc.github.io/dlpack/latest/python_spec.html) provides a
CPU array interoperability interface, through the `__dlpack__` method, analogous
to the GPU one that supports (through `__dlpack_device__`, see
[GPU section](./gpu.md)).
