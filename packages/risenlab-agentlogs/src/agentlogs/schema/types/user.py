import datetime as dt
from typing import Annotated, TypedDict

from .annotation import Description, FoundUsing, GitHubField, Relation, Source, Table
from .pull_request import PullRequestTimelineReference
from .references import (
    COLLECTED_MAY_MISS,
    AgentSessionReference,
    AgentTaskReference,
    PullRequestReference,
    RepositoryReference,
    UserReference,
    WorkflowRunReference,
)


@Table(
    name="users",
    sources=[
        Source(
            name="User",
            found_using=[
                FoundUsing(
                    name="graphql_node_id",
                    text="GitHub GraphQL `node(id:)` with a stored node id "
                    "([documentation](https://docs.github.com/en/graphql/reference/queries#node))",
                ),
                FoundUsing(
                    name="rest_id",
                    text="GitHub REST `GET /user/{id}` "
                    "([documentation](https://docs.github.com/en/rest/users/users#get-a-user-using-their-id))",
                ),
                FoundUsing(
                    name="graphql_mint_global_id",
                    text="GitHub GraphQL `node(id:)` with a minted `global_id` from the "
                    "base64-encoded `04:User{id}` "
                    "([documentation](https://docs.github.com/en/graphql/reference/queries#node))",
                ),
                FoundUsing(
                    name="graphql_login",
                    text="GitHub GraphQL `repositoryOwner(login:)` "
                    "([documentation](https://docs.github.com/en/graphql/reference/queries#repositoryowner))",
                ),
            ],
        ),
    ],
    explanation=COLLECTED_MAY_MISS,
    reference=UserReference,
)
class User(TypedDict):
    """GitHub user, organization, or bot."""

    id: Annotated[int, GitHubField("id")]
    login: Annotated[str, GitHubField("login")]
    graphql_id: Annotated[str, GitHubField("node_id")]
    type: Annotated[
        str,
        GitHubField("type"),
        Description("`user`, `organization`, or `bot`."),
    ]

    found_using: Annotated[
        str,
        Description(
            "`graphql_node_id`, `graphql_login`, `graphql_mint_global_id`, or `rest_id`. "
            "See [Data sources](#data-sources)"
        ),
    ]

    tasks: Annotated[list[AgentTaskReference], Relation("creator")]
    sessions: Annotated[list[AgentSessionReference], Relation("user")]
    repositories: Annotated[
        list[RepositoryReference],
        Relation("owner"),
        Description(
            "User's repositories that appear in the seed (see [repository schema](./repository.md)). Does not include public repositories not in this seed or any private repositories."
        ),
    ]
    pull_requests: Annotated[list[PullRequestReference], Relation("user")]
    assigned_pull_requests: Annotated[list[PullRequestReference], Relation("assignees")]
    review_requested_pull_requests: Annotated[
        list[PullRequestReference],
        Relation("requested_reviewers"),
    ]
    merged_pull_requests: Annotated[list[PullRequestReference], Relation("merged_by")]
    auto_merge_enabled_pull_requests: Annotated[
        list[PullRequestReference],
        Relation("auto_merge.enabled_by"),
    ]
    timeline_events: Annotated[list[PullRequestTimelineReference], Relation("actor")]
    assigned_timeline_events: Annotated[
        list[PullRequestTimelineReference],
        Relation("assignee"),
    ]
    workflow_runs: Annotated[list[WorkflowRunReference], Relation("actor")]
    triggered_workflow_runs: Annotated[
        list[WorkflowRunReference],
        Relation("triggering_actor"),
    ]
    created_at: Annotated[dt.datetime, GitHubField("created_at")]
