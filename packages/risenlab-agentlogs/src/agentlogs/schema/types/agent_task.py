import datetime as dt
from typing import Annotated, TypedDict

from .annotation import Description, GitHubField, Relation, Source, Table
from .references import (
    COLLECTED_MAY_MISS,
    AgentReference,
    AgentTaskReference,
    BranchReference,
    PullRequestReference,
    RepositoryReference,
    UserReference,
)

class AgentTaskSessionReference(TypedDict):
    id: Annotated[str, GitHubField("id")]
    session_index: Annotated[
        int,
        Description("Position of the session within the task."),
    ]


class CustomAgentReference(TypedDict):
    id: Annotated[str | None, GitHubField("id")]
    name: Annotated[str | None, GitHubField("name")]
    is_automation: Annotated[bool | None, GitHubField("is_automation")]


class BranchArtifactData(TypedDict):
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


@Table(
    name="agent_tasks",
    sources=[
        Source(
            name="Task list",
            text="GitHub REST `GET /agents/repos/{owner}/{repo}/tasks` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks))",
        ),
        Source(
            name="Task",
            text="Copilot API `GET https://api.githubcopilot.com/agents/tasks/{id}` (no public documentation)",
        ),
    ],
    explanation=(
        "Fields and values on the Copilot API differ slightly from GitHub REST "
        "`GET /agents/tasks/{id}` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks#get-a-task-by-id)). "
        + COLLECTED_MAY_MISS
    ),
    reference=AgentTaskReference,
)
class AgentTask(TypedDict):
    """Copilot cloud agent task."""

    id: Annotated[str, GitHubField("id")]

    repository: Annotated[RepositoryReference, Relation("agent_tasks")]
    sessions: Annotated[
        list[AgentTaskSessionReference],
        Relation("task"),
        GitHubField("sessions[]"),
    ]
    creator: Annotated[
        UserReference,
        Relation("tasks"),
        GitHubField("creator", leaves={"id": "id", "login": "login", "graphql_id": "node_id"}),
    ]
    pull_request_artifacts: Annotated[
        list[PullRequestReference],
        Relation("created_by_tasks"),
        GitHubField("artifacts[]", leaves={"id": "data.id", "graphql_id": "data.global_id"}),
        Description(
            "Pull requests created by this task (REST `artifacts[]` of type `pull`). "
            "May include pull requests that are not on any listed session, "
            "possibly because a session was deleted "
            "(see [Agent Session](./agent_session.md) `pull_request_artifact`). "
        ),
    ]

    name: Annotated[str | None, GitHubField("name")]
    state: Annotated[str, GitHubField("state")]
    archived: bool
    remote_steerable: Annotated[bool, GitHubField("remote_steerable")]
    sharing_status: Annotated[str, GitHubField("sharing_status")]

    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    archived_at: Annotated[dt.datetime | None, GitHubField("archived_at")]

    custom_agent: Annotated[CustomAgentReference | None, GitHubField("custom_agent")]
    automation_id: Annotated[str | None, GitHubField("automation_id")]
    agent_collaborators: Annotated[list[AgentReference], GitHubField("agent_collaborators[]")]
    branch_artifacts: Annotated[
        list[BranchArtifactData],
        GitHubField("artifacts[]"),
        Description(
            "Branches worked on and/or pushed to by this task (REST `artifacts[]` of type `branch`). "
            "May include branches that are not on any listed session, "
            "possibly because a session was deleted "
            "(see [Agent Session](./agent_session.md) `base` and `head`)."
        ),
    ]
