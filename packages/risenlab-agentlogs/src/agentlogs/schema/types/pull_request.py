import datetime as dt
from typing import Annotated, TypedDict

from .annotation import Description, FoundUsing, GitHubField, Relation, Source, Table
from .references import (
    COLLECTED_MAY_MISS,
    AgentSessionReference,
    AgentTaskReference,
    BranchCommitReference,
    PullRequestReference,
    RepositoryReference,
    UserReference,
)


class PullRequestTimelineReference(TypedDict):
    pull_request: PullRequestReference
    event_index: int


class PullRequestAutoMergeData(TypedDict):
    enabled_by: Annotated[
        UserReference | None,
        Relation("auto_merge_enabled_pull_requests"),
        GitHubField("enabled_by"),
    ]
    merge_method: Annotated[str, GitHubField("merge_method")]
    commit_title: Annotated[str | None, GitHubField("commit_title")]
    commit_message: Annotated[str | None, GitHubField("commit_message")]


@Table(
    name="pull_request_timelines",
    sources=[
        Source(
            name="Pull request timeline",
            text="GitHub REST `GET /repos/{owner}/{repo}/issues/{issue_number}/timeline` "
            "([documentation](https://docs.github.com/en/rest/issues/timeline#list-timeline-events-for-an-issue))",
        ),
    ],
    reference=PullRequestTimelineReference,
)
class PullRequestTimelineEvent(TypedDict):
    """One event from a collected pull request timeline."""

    pull_request: Annotated[
        PullRequestReference,
        Relation(),
        Description(
            "Each timeline event points at its pull request; pull requests do not list timeline events (see [Pull Request](./pull_request.md))."
        ),
    ]
    event_index: Annotated[
        int,
        Description("Position of the event within the pull request timeline."),
    ]
    event: Annotated[str, GitHubField("event")]
    created_at: Annotated[dt.datetime | None, GitHubField("created_at | submitted_at | author.date")]
    actor: Annotated[
        UserReference | None,
        Relation("timeline_events"),
        GitHubField("actor | user"),
    ]
    assignee: Annotated[
        UserReference | None,
        Relation("assigned_timeline_events"),
        GitHubField("assignee"),
    ]
    label: Annotated[str | None, GitHubField("label.name")]
    commit_id: Annotated[str | None, GitHubField("commit_id | sha")]
    message: Annotated[str | None, GitHubField("message")]


@Table(
    name="pull_requests",
    sources=[
        Source(
            name="Pull request",
            found_using=[
                FoundUsing(
                    name="graphql_global_id",
                    text="GitHub GraphQL `node(id:)` "
                    "([documentation](https://docs.github.com/en/graphql/reference/queries#node))",
                ),
                FoundUsing(
                    name="graphql_number_repo",
                    text="GitHub GraphQL `repository.pullRequest(number:)` "
                    "([documentation](https://docs.github.com/en/graphql/reference/objects#repository))",
                ),
                FoundUsing(
                    name="graphql_mint_global_id",
                    text="GitHub GraphQL `node(id:)` with a minted `global_id` from the "
                    "base64-encoded `011:PullRequest{id}` "
                    "([documentation](https://docs.github.com/en/graphql/reference/queries#node))",
                ),
                FoundUsing(
                    name="rest_number_repo",
                    text="GitHub REST `GET /repos/{owner}/{repo}/pulls/{pull_number}` "
                    "([documentation](https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request))",
                ),
            ],
        ),
    ],
    explanation=COLLECTED_MAY_MISS,
    reference=PullRequestReference,
)
class PullRequest(TypedDict):
    """GitHub pull request collected from a task or session."""

    id: Annotated[int | None, GitHubField("id")]
    graphql_id: Annotated[str, GitHubField("node_id")]
    number: Annotated[int, GitHubField("number")]

    found_using: Annotated[
        str,
        Description(
            "`graphql_global_id`, `graphql_number_repo`, `graphql_mint_global_id`, "
            "or `rest_number_repo`. See [Data sources](#data-sources)"
        ),
    ]
    timeline_found: bool

    repository: Annotated[
        RepositoryReference,
        Relation(),
    ]
    created_by_tasks: Annotated[
        list[AgentTaskReference],
        Relation("pull_request_artifacts"),
        Description(
            "Tasks that created this pull request as an artifact "
            "(see [Agent Task](./agent_task.md) `pull_request_artifacts`)."
        ),
    ]
    created_by_sessions: Annotated[
        list[AgentSessionReference],
        Relation("pull_request_artifact"),
        Description(
            "Sessions that created this pull request "
            "(see [Agent Session](./agent_session.md) `pull_request_artifact`)."
        ),
    ]
    user: Annotated[
        UserReference | None,
        Relation("pull_requests"),
        GitHubField("user"),
    ]
    assignees: Annotated[
        list[UserReference],
        Relation("assigned_pull_requests"),
        GitHubField("assignees"),
    ]
    requested_reviewers: Annotated[
        list[UserReference],
        Relation("review_requested_pull_requests"),
        GitHubField("requested_reviewers"),
        Description(
            "Users only. Review requests to teams are not collected: "
            "GitHub GraphQL `Team` fields on review requests require org scopes "
            "this collection does not use."
        ),
        Description("Only the first 20 are fetched."),
    ]
    merged_by: Annotated[
        UserReference | None,
        Relation("merged_pull_requests"),
        GitHubField("merged_by"),
    ]

    title: Annotated[str, GitHubField("title")]
    body: Annotated[str | None, GitHubField("body")]
    state: Annotated[str, GitHubField("state")]
    locked: Annotated[bool, GitHubField("locked")]
    draft: Annotated[bool, GitHubField("draft")]
    labels: Annotated[
        list[str],
        GitHubField("labels[].name"),
        Description("Only the first 20 are fetched."),
    ]
    active_lock_reason: Annotated[str | None, GitHubField("active_lock_reason")]
    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    closed_at: Annotated[dt.datetime | None, GitHubField("closed_at")]
    merged_at: Annotated[dt.datetime | None, GitHubField("merged_at")]
    head: Annotated[BranchCommitReference, GitHubField("head")]
    base: Annotated[BranchCommitReference, GitHubField("base")]
    author_association: Annotated[str, GitHubField("author_association")]
    auto_merge: PullRequestAutoMergeData | None
    merged: Annotated[bool, GitHubField("merged")]
    mergeable: Annotated[bool | None, GitHubField("mergeable")]
    mergeable_state: Annotated[str, GitHubField("mergeable_state")]
    maintainer_can_modify: Annotated[bool, GitHubField("maintainer_can_modify")]
    additions_count: Annotated[int, GitHubField("additions")]
    deletions_count: Annotated[int, GitHubField("deletions")]
    changed_files_count: Annotated[int, GitHubField("changed_files")]
