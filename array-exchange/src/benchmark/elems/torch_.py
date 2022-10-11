import torch
import torch.random

from .utils import prod

cuda = torch.device("cuda")


def arange(shape):
    return torch.arange(prod(shape), device=cuda).reshape(shape)


def random(shape):
    return torch.rand(prod(shape), device=cuda).reshape(shape)


def saxpy(x, y, a):
    return a * x + y
