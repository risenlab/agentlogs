import datetime as dt
from typing import Annotated, TypedDict

from .annotation import Description, GitHubField, Relation, Source, Table
from .references import (
    COLLECTED_MAY_MISS,
    AgentSessionReference,
    CheckSuiteReference,
    CommitReference,
    RepositoryReference,
    UserReference,
    WorkflowRunReference,
)


@Table(
    name="workflow_runs",
    sources=[
        Source(
            name="Workflow run",
            text="GitHub REST `GET /repos/{owner}/{repo}/actions/runs/{id}` "
            "([documentation](https://docs.github.com/en/rest/actions/workflow-runs#get-a-workflow-run))",
        ),
    ],
    explanation=COLLECTED_MAY_MISS,
    reference=WorkflowRunReference,
)
class WorkflowRun(TypedDict):
    """GitHub Actions workflow run."""

    id: Annotated[int, GitHubField("id")]
    repository: Annotated[RepositoryReference, Relation()]
    head_repository: Annotated[
        RepositoryReference,
        Relation(collected=False),
        GitHubField("head_repository"),
        Description(
            "Not collected. May be absent from [repositories](./repository.md) "
            "(fork or not the task repository)."
        ),
    ]
    actor: Annotated[
        UserReference | None,
        Relation("workflow_runs"),
        GitHubField("actor"),
    ]
    triggering_actor: Annotated[
        UserReference | None,
        Relation("triggered_workflow_runs"),
        GitHubField("triggering_actor"),
    ]
    session: Annotated[AgentSessionReference, Relation("workflow_run")]

    name: Annotated[str | None, GitHubField("name")]
    graphql_id: Annotated[str, GitHubField("node_id")]
    check_suite: Annotated[
        CheckSuiteReference | None,
        GitHubField(
            "",
            leaves={"id": "check_suite_id", "graphql_id": "check_suite_node_id"},
        ),
    ]
    head: Annotated[
        CommitReference,
        GitHubField("", leaves={"ref": "head_branch", "sha": "head_sha"}),
    ]
    path: Annotated[str, GitHubField("path")]
    run_number: Annotated[int, GitHubField("run_number")]
    run_attempt: Annotated[int | None, GitHubField("run_attempt")]
    event: Annotated[str, GitHubField("event")]
    status: Annotated[str | None, GitHubField("status")]
    conclusion: Annotated[str | None, GitHubField("conclusion")]
    workflow_id: Annotated[int, GitHubField("workflow_id")]
    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    run_started_at: Annotated[dt.datetime | None, GitHubField("run_started_at")]
    display_title: Annotated[str, GitHubField("display_title")]
