# GPU investigation

## Languages

The most powerful for driving GPU is C/C++, no doubt, so this is the basic
choice.

Two ways interoperable:

- Rust, since [ever](https://doc.rust-lang.org/nomicon/ffi.html), and
  [ever](https://docs.rust-embedded.org/book/interoperability/index.html),
  and [ever](https://cxx.rs/)
- Fortran, since
  [2003](https://www.ibm.com/docs/en/xl-fortran-aix/15.1.2?topic=reference-language-interoperability-features#interoperability)
  - small community still

One way (the other is possible, but instantiating the full interpreter, and in
general inefficient/uncomfortable):

- Python, relatively easy to make packages out of C/C++ libraries
- Julia, seems [easy](https://github.com/JuliaInterop/Cxx.jl) [as
  well](https://docs.julialang.org/en/v1/manual/calling-c-and-fortran-code/#Calling-C-and-Fortran-Code)

Other languages are present and popular, but they are mainly relevant for Web
and Interfaces, not so much for scientific computing.

- Bash -> whatever (favorite: file system manipulation), but non-numerical
- Go, PHP, Ruby -> Web Back-end
- JS/TS, HTML, CSS -> Web Front-end
- Java, Kotlin, Swift, Dart, C# -> used for UI
- R -> statistics, not optimal for intensive/performant custom calculation
- MATLAB -> simply not used

### Conclusion

In particular, the best choices are to write directly to C/C++ and Rust
(discarding Fortran for convenience), and get all the others through wrappers
and packages.

Personal experience: Rust

But there is a lack of native tools for GPGPU in Rust, because it is still
somewhat "a niche", and because in Rust there is plenty of things missing or
half-done.

Final Choice: C/C++

## Target

Reuse same array in GPU over and over (passing "pointers").

### Personal principles

1. avoid language in strings/comments -> all language should be encoded in syntax
   - this doesn't rule out eDSL (e.g. SYCL) but rules out CuPy if large buches
     of `RawKernel` are needed
2. support efficient interfaces for all the relevant languages above
   - it does rule out Python or Julia native frameworks, since you need to
     embed an interpreter to run a library in C++ (e.g.)
   - https://docs.julialang.org/en/v1/manual/embedding/
3. avoid graphics first frameworks
   - the majority of frameworks leveraging GPU are for graphics, since it's the
     oldest and most established application
   - graphics has a different logic (shaders, 3D native, ...), so it would
     require relevant effort to fit our concepts (n-dim arrays and generic
     linear algebra) in its language
4. support at least Nvidia and AMD

## Framework choice

### Python (discarded)

- CuPy
  - interesting because it has NumPy API,
  - it would be inefficient to run from MadGraph
- TensorFlow

### Julia (discarded)

There is an entire [site](https://juliagpu.org/) dedicated to GPU computation in
Julia.

### Rust (almost discarded)

See [rust](./README.md)

### C++

#### SYCL

See [SYCL](./sycl/README.md).

#### Kokkos

#### Alpaka

#### ArrayFire

https://github.com/arrayfire/arrayfire

Native support for all relevant languages (+1)

- C++
- Python
- Rust
- Julia
- Nim

In-progress for even more: Fortran, .NET, Java, LUA, JavaScript, R, Ruby.

Ok, Fortran is in the wrong list, but if we have a C++ library or interface it
should be possible to use from Fortran, as written above.

Nice documentation (at first sight, still Doxygen) including Tutorials.

OpenCL interoperability, not SYCL. Native support for all back-ends, through
CUDA and OpenCL layers (built-in) and CUDA and OpenCL interoperability.

In principle support even for Xilinx FPGA, through SDAccel, but they say to
contact [Xilinx sales
representatives](https://arrayfire.com/partner-program/#xilinx).
