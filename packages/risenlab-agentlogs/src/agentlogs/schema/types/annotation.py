from dataclasses import dataclass

@dataclass(frozen=True)
class Description:
    text: str

@dataclass(frozen=True)
class Note:
    text: str

@dataclass(frozen=True)
class Relation:
    pass

@dataclass(frozen=True)
class GitHubField:
    field: str
    leaves: dict[str, str] | None = None
