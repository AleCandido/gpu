import dataclasses


@dataclasses.dataclass
class ProfilerOutput:
    full: str

    @classmethod
    def extract(cls, output: str):
        return cls(full=output)
