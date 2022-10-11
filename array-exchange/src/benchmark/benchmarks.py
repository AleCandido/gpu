from types import ModuleType


def arange(mod: ModuleType):
    mod.arange(100)


def saxpy(mod: ModuleType):
    mod.saxpy(mod.arange(100), mod.arange(100), 3)
