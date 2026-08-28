import datetime as dt
from typing import Annotated, TypedDict

from .annotation import GitHubField, Relation
from .references import (
    AgentTaskReference,
    BranchReference,
    PullRequestReference,
    UserReference,
)

class AgentSessionUsage(TypedDict):
    type: Annotated[str, GitHubField("type")]
    amount: Annotated[float | None, GitHubField("amount")]
    credits: Annotated[float | None, GitHubField("credits")]

class AgentSessionEvent(TypedDict):
    type: Annotated[str | None, GitHubField("event_type")]
    url: Annotated[str | None, GitHubField("event_url")]
    ids: Annotated[list[str] | None, GitHubField("event_identifiers")]
    content: Annotated[str | None, GitHubField("event_content")]

class AgentSession(TypedDict):
    id: Annotated[str, GitHubField("id")]

    task: Annotated[AgentTaskReference, Relation()]
    log_found: bool

    user: Annotated[
        UserReference,
        GitHubField("user", leaves={"id": "id", "login": "login"}),
    ]

    name: Annotated[str, GitHubField("name")]
    model: Annotated[str | None, GitHubField("model")]
    prompt: Annotated[str | None, GitHubField("prompt")]
    state: Annotated[str, GitHubField("state")]
    usage: Annotated[AgentSessionUsage | None, GitHubField("usage")]
    premium_requests: Annotated[float, GitHubField("premium_requests")]
    error: Annotated[str | None, GitHubField("error.message")]
    remote_steerable: Annotated[bool | None, GitHubField("remote_steerable")]
    workflow_run_id: Annotated[int | None, GitHubField("workflow_run_id")]

    event: AgentSessionEvent
    pull_request: PullRequestReference | None
    branch: BranchReference | None

    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    completed_at: Annotated[dt.datetime | None, GitHubField("completed_at")]
