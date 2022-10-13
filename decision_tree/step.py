import dataclasses


@dataclasses.dataclass
class Step:
    text: str
    options: dict[str, "Step"] = dataclasses.field(default_factory=dict)
