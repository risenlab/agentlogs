import datetime as dt
from typing import Annotated, TypedDict

from .annotation import GitHubField, Relation
from .references import AgentTaskReference

class RepositoryMetric(TypedDict):
    language: str
    blank_lines: int
    code_lines: int
    comment_lines: int

class Repository(TypedDict):
    full_name: str

    agent_tasks: Annotated[list[AgentTaskReference], GitHubField("tasks[]")]

    archived: Annotated[bool, GitHubField("isArchived")]
    disabled: Annotated[bool, GitHubField("isDisabled")]
    locked: Annotated[bool, GitHubField("isLocked")]
    fork: Annotated[bool, GitHubField("isFork")]

    homepage: Annotated[str | None, GitHubField("homepageUrl")]
    has_wiki: Annotated[bool, GitHubField("hasWikiEnabled")]
    license: Annotated[str | None, GitHubField("licenseInfo.name")]
    main_language: str
    default_branch: Annotated[str | None, GitHubField("defaultBranchRef.name")]
    size: Annotated[int, GitHubField("diskUsage")]

    created_at: Annotated[dt.datetime, GitHubField("created_at")]
    pushed_at: Annotated[dt.datetime, GitHubField("pushed_at")]
    updated_at: Annotated[dt.datetime, GitHubField("updated_at")]
    last_commit_at: Annotated[dt.datetime | None, GitHubField("defaultBranchRef.target.committedDate")]
    last_commit_SHA: Annotated[str | None, GitHubField("defaultBranchRef.target.oid")]

    forks_count: Annotated[int, GitHubField("forkCount")]
    stargazers_count: Annotated[int, GitHubField("stargazers.totalCount")]
    watchers_count: Annotated[int | None, GitHubField("watchers.totalCount")]
    commits_count: Annotated[int | None, GitHubField("defaultBranchRef.target.history.totalCount")]
    branches_count: Annotated[int | None, GitHubField("refs.totalCount")]
    releases_count: Annotated[int | None, GitHubField("releases.totalCount")]
    contributors_count: int | None
    total_issues_count: Annotated[int | None, GitHubField("issues.totalCount")]
    open_issues_count: Annotated[int | None, GitHubField("issues(states: OPEN).totalCount")]
    total_pull_requests_count: Annotated[int | None, GitHubField("pullRequests.totalCount")]
    open_pull_requests_count: Annotated[int | None, GitHubField("pullRequests(states: OPEN).totalCount")]

    labels: Annotated[list[str], GitHubField("labels.nodes[].name")]
    topics: Annotated[list[str], GitHubField("repositoryTopics.nodes[].topic.name")]
    languages: Annotated[dict[str, int], GitHubField("languages")]

    blank_lines: int | None
    code_lines: int | None
    comment_lines: int | None
    metrics: list[RepositoryMetric]
