import datetime as dt
from typing import Annotated, TypedDict

from .agent_task import AgentTaskSessionReference
from .annotation import Description, GitHubField, Relation, Source, Table
from .references import (
    AgentSessionReference,
    AgentTaskReference,
    BranchReference,
    PullRequestReference,
    UserReference,
    WorkflowRunReference,
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

@Table(
    name="agent_sessions",
    sources=[
        Source(
            name="Session",
            text="`sessions[]` on Copilot API `GET https://api.githubcopilot.com/agents/tasks/{id}` (no public documentation)",
        ),
    ],
    explanation="Fields and values differ slightly from GitHub REST `GET /agents/tasks/{id}` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks#get-a-task-by-id)).",
    reference=(AgentSessionReference, AgentTaskSessionReference),
)
class AgentSession(TypedDict):
    """Copilot cloud agent session."""

    id: Annotated[str, GitHubField("id")]
    session_index: Annotated[
        int,
        Description("Position of the session within the task."),
    ]

    log_found: bool

    task: Annotated[AgentTaskReference, Relation("sessions")]
    user: Annotated[
        UserReference,
        Relation("sessions"),
        GitHubField("user", leaves={"id": "id", "login": "login", "graphql_id": "node_id"}),
    ]
    pull_request_artifact: Annotated[
        PullRequestReference | None,
        Relation("created_by_sessions"),
        GitHubField(
            "",
            leaves={
                "id": "resource_id",
                "graphql_id": "resource_global_id",
                "number": "resource_number",
            },
        ),
        Description(
            "Pull request created by this session. "
            "Often also listed on the parent task "
            "([pull request artifacts](./agent_task.md)). "
            "May be missing when the task still lists the pull request."
        ),
    ]
    workflow_run: Annotated[
        WorkflowRunReference | None,
        Relation("session"),
        GitHubField("", leaves={"id": "workflow_run_id"}),
        Description("Actions run that executed this session."),
    ]
    base: Annotated[
        BranchReference | None,
        GitHubField("", leaves={"ref": "base_ref"}),
        Description("Branch the agent started from."),
    ]
    head: Annotated[
        BranchReference | None,
        GitHubField("", leaves={"ref": "head_ref"}),
        Description(
            "Branch the agent created and/or pushed to."
        ),
    ]

    name: Annotated[str, GitHubField("name")]
    model: Annotated[str | None, GitHubField("model")]
    prompt: Annotated[str | None, GitHubField("prompt")]
    reasoning_effort: Annotated[str | None, GitHubField("reasoning_effort")]
    state: Annotated[str, GitHubField("state")]
    usage: Annotated[AgentSessionUsage | None, GitHubField("usage")]
    premium_requests: Annotated[float, GitHubField("premium_requests")]
    error: Annotated[str | None, GitHubField("error.message")]
    remote_steerable: Annotated[bool | None, GitHubField("remote_steerable")]

    event: AgentSessionEvent

    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    completed_at: Annotated[dt.datetime | None, GitHubField("completed_at")]
