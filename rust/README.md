# Rust

## Collections

- nice but outdated [blog post](https://bheisler.github.io/post/state-of-gpgpu-in-rust/)
- [discussion](https://users.rust-lang.org/t/best-way-to-start-programming-for-gpu-in-rust/29768/5)
  on Rust users forum

## Crates

The unmaintained and not so big crates are not even listed.

- [`ocl`](https://github.com/cogciprocate/ocl), bindings to OpenCL
  - OpenCL kernels are written in OpenCL C, i.e. yet another language, compiled
    at runtime on the GPU **violates 1.**
- [`arrayfire-rust`](https://github.com/arrayfire/arrayfire-rust), bindings to
  ArrayFire
  - quite Rusty, I've seen no trace of 1.
- [`Rust-CUDA`](https://github.com/Rust-GPU/Rust-CUDA), essentially CUDA
  bindings, so it **violates 4.**

[`wgpu`](https://github.com/gfx-rs/wgpu),
[`vulkano`](https://github.com/vulkano-rs/vulkano), and
[`rust-gpu`](https://github.com/EmbarkStudios/rust-gpu) are reasonable but they
are graphics, so **violate 3.**

## Misc

There is also a native Tier 2 target of `rustc` (`no_std`) for CUDA only
https://doc.rust-lang.org/stable/rustc/platform-support/nvptx64-nvidia-cuda.html
