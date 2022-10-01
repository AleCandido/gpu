# Test array exchange protocols

- [DLPack](https://dmlc.github.io/dlpack/latest/index.html)
- [`__cuda_array_interface__`](https://numba.readthedocs.io/en/stable/cuda/cuda_array_interface.html)

## Original source

First found through CuPy dedicated guide about
["Interoperability"](https://docs.cupy.dev/en/stable/user_guide/interoperability.html).

## Dependencies

The dependencies are divided in groups:

- top level dependencies: are needed to run everything
- `cuda`: the dependencies in this group are used to test on Nvidia hardware
  - `cupy`: needs dedicated package for different hardware
  - `tensorflow`: by default is built
    [without support for ROCm](https://www.tensorflow.org/api_docs/python/tf/test/is_built_with_rocm)
  - `pytorch`: default package for CUDA, but an old version (so let's use an
    alternative repository https://pytorch.org/get-started/locally/)
  - `numba`:
    [only supports CUDA](https://numba.readthedocs.io/en/stable/cuda/index.html)
- `rocm`: the dependencies in this group are used to test on AMD hardware
  - `cupy`: needs dedicated package for different hardware
  - `tensorflow-rocm`: the tf ROCm package
  - `pytorch`: custom Python repository (PyPI alternative) available also for
    ROCm
