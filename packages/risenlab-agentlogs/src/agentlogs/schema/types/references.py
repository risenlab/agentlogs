from typing import Annotated, TypedDict

from .annotation import Description, GitHubField

class AgentSessionReference(TypedDict):
    id: Annotated[str, GitHubField("id")]
    
class AgentTaskReference(TypedDict):
    id: Annotated[str, GitHubField("id")]

class RepositoryReference(TypedDict):
    full_name: str

class WorkflowRunReference(TypedDict):
    id: Annotated[int, GitHubField("id")]
    repository: RepositoryReference

class UserReference(TypedDict):
    id: Annotated[int | None, GitHubField("id")]
    login: Annotated[str | None, GitHubField("login")]
    graphql_id: Annotated[str | None, GitHubField("node_id")]
    type: Annotated[str | None, GitHubField("type")]


COLLECTED_MAY_MISS = (
    "Only successful GitHub API responses are stored. Other tables may contain "
    "references to this table with no matching row."
)

class AgentReference(TypedDict):
    id: Annotated[int, GitHubField("agent_id")]

    slug: Annotated[
        str,
        GitHubField("slug"),
        Description("`copilot-developer` or `copilot-pr-reviews`."),
    ]

    task_id: Annotated[
        str | None,
        GitHubField("agent_task_id"),
        Description(
            "Usually `ownerId-repoId-uuid`, a bare UUID, or `owner:{id}:repo:{id}:pull:{id}`. Currently unknown what the UUID refers to."
        ),
    ]

    type: Annotated[
        str | None,
        GitHubField("agent_type"),
        Description(
            "`Integration`, `UserToServerToken`, `IntegrationInstallation`, or `OauthApplication`."
        ),
    ]

class CheckSuiteReference(TypedDict):
    id: Annotated[int | None, GitHubField("id")]
    graphql_id: Annotated[str | None, GitHubField("node_id")]

class PullRequestReference(TypedDict):
    id: Annotated[int | None, GitHubField("resource_id")]
    graphql_id: Annotated[str | None, GitHubField("resource_global_id")]
    number: Annotated[int | None, GitHubField("resource_number")]
    repository: RepositoryReference | None

class BranchReference(TypedDict):
    ref: Annotated[str, GitHubField("ref")]


class BranchCommitReference(TypedDict):
    ref: Annotated[str, GitHubField("ref")]
    sha: Annotated[str, GitHubField("sha")]


class CommitReference(TypedDict):
    sha: Annotated[str, GitHubField("sha")]
    ref: Annotated[str | None, GitHubField("ref")]
