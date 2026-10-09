from dataclasses import dataclass, field


@dataclass(frozen=True)
class Description:
    text: str


@dataclass(frozen=True)
class Relation:
    field: str | None = None
    collected: bool = True


@dataclass(frozen=True)
class GitHubField:
    field: str
    leaves: dict[str, str] | None = None


@dataclass(frozen=True)
class FoundUsing:
    name: str
    text: str


@dataclass(frozen=True)
class Source:
    name: str
    text: str | None = None
    found_using: list[FoundUsing] = field(default_factory=list)


@dataclass(frozen=True)
class Table:
    name: str
    sources: list[Source] = field(default_factory=list)
    explanation: str | None = None
    reference: type | tuple[type, ...] | None = None

    def __call__(self, cls: type) -> type:
        setattr(cls, "__schema_table__", self)
        return cls


def table_reference_types(info: Table) -> tuple[type, ...]:
    if info.reference is None:
        return ()
    if isinstance(info.reference, tuple):
        return info.reference
    return (info.reference,)


def table_info(cls: type) -> Table:
    info = getattr(cls, "__schema_table__", None)
    if not isinstance(info, Table):
        raise TypeError(f"{cls.__name__} is not annotated with @Table")
    return info


def table_slug(cls: type) -> str:
    name = cls.__name__
    chars: list[str] = []
    for index, char in enumerate(name):
        if char.isupper() and index > 0 and (
            name[index - 1].islower()
            or (index + 1 < len(name) and name[index + 1].islower())
        ):
            chars.append("_")
        chars.append(char.lower())
    return "".join(chars)


def table_title(cls: type) -> str:
    return table_slug(cls).replace("_", " ").title()
