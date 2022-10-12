# Memory Management

Collection of references and tutorials.

## Reference

The SYCL reference (about SYCL 2020) can be found:
https://registry.khronos.org/SYCL/specs/sycl-2020/pdf/sycl-2020.pdf

Chapter 4.7 is specifically dedicated to "Data access and storage in SYCL".

It might be useful to have also a look at the brief (7 pages) chapter 3.8
"Memory model".

## oneAPI - SYCL

An introduction to the basic stuffs, including Buffers and Accessors, can be
found at:
https://github.com/oneapi-src/oneAPI-samples/blob/master/DirectProgramming/DPC%2B%2B/Jupyter/oneapi-essentials-training/02_DPCPP_Program_Structure/DPCPP_Program_Structure.ipynb

(look in particular for "Buffer Model").

An in-depth tutorial about this alone can be found at:
https://github.com/oneapi-src/oneAPI-samples/blob/master/DirectProgramming/DPC%2B%2B/Jupyter/oneapi-essentials-training/09_DPCPP_Buffers_And_Accessors_Indepth/DPCPP_Buffers_accessors.ipynb

## Alpaka

The documentation about memory management it is almost non-existent:
https://alpaka.readthedocs.io/en/latest/basic/library.html#memory-management

Further details are provided as recipes:
https://alpaka.readthedocs.io/en/latest/basic/cheatsheet.html#memory but it is
not much better...

## Kokkos

Documentation about memory management can be found here:
https://kokkos.github.io/kokkos-core-wiki/ProgrammingGuide/View.html#managing-data-placement

It provides some details, but it is almost completely missing the purpose of the
framework: CUDA and HIP resources have to be managed separately, so there is no
common abstraction (apparently).
