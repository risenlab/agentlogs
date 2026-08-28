import datetime as dt
from typing import Annotated, TypedDict

from .annotation import GitHubField, Note, Relation
from .references import (
    AgentReference,
    AgentSessionReference,
    BranchReference,
    PullRequestIDReference,
    RepositoryReference,
    UserReference,
)

class CustomAgentReference(TypedDict):
    id: Annotated[str | None, GitHubField("id")]
    name: Annotated[str | None, GitHubField("name")]
    is_automation: Annotated[bool | None, GitHubField("is_automation")]

class AgentArtifactReference(TypedDict):
    type: str
    pull_request: Annotated[PullRequestIDReference | None, GitHubField("data")]
    branch: Annotated[BranchReference | None, GitHubField("data")]

class AgentTaskData(TypedDict):
    name: Annotated[str | None, GitHubField("name")]
    state: Annotated[str, GitHubField("state")]
    archived: bool
    remote_steerable: Annotated[bool, GitHubField("remote_steerable")]
    sharing_status: Annotated[str, GitHubField("sharing_status")]

    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    archived_at: Annotated[dt.datetime | None, GitHubField("archived_at")]

    custom_agent: Annotated[CustomAgentReference | None, GitHubField("custom_agent")]
    agent_collaborators: Annotated[list[AgentReference], GitHubField("agent_collaborators[]")]
    artifacts: Annotated[list[AgentArtifactReference], GitHubField("artifacts[]")]

class AgentTask(TypedDict):
    id: Annotated[str, GitHubField("id")]

    repository: Annotated[RepositoryReference, Relation()]
    sessions: Annotated[list[AgentSessionReference], GitHubField("sessions[]")]

    creator: Annotated[
        UserReference | None,
        GitHubField("creator", leaves={"id": "id", "login": "login"}),
        Note("Not set when `found` is false"),
    ]
    collaborators: Annotated[
        list[UserReference] | None,
        GitHubField("user_collaborators[]", leaves={"id": ""}),
        Note("Not set when `found` is false"),
    ]

    found: bool
    data: Annotated[
        AgentTaskData | None,
        Note("Not set when `found` is false"),
    ]
