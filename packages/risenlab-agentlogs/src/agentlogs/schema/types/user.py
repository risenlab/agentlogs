from typing import Annotated, TypedDict

from .annotation import Note, Relation
from .references import AgentSessionReference, AgentTaskReference

class User(TypedDict):
    """
    A GitHub user or organization
    """

    id: int
    found: bool
    found_using: Annotated[
        str | None,
        Note("`'id' | 'login'`. Not set when `found` is false"),
    ]
    login: Annotated[
        str | None,
        Note("Not set when `found` is false"),
    ]

    created_tasks: Annotated[list[AgentTaskReference], Relation()]
    collaborated_tasks: Annotated[
        list[AgentTaskReference],
        Relation(),
        Note("Taken from GitHub's API and may not be complete. Use together with created_tasks and sessions."),
    ]
    sessions: Annotated[list[AgentSessionReference], Relation()]
