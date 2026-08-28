from typing import Annotated, TypedDict

from .annotation import GitHubField

class AgentSessionReference(TypedDict):
    id: Annotated[str, GitHubField("id")]
    
class AgentTaskReference(TypedDict):
    id: Annotated[str, GitHubField("id")]

class RepositoryReference(TypedDict):
    full_name: str

class UserReference(TypedDict):
    id: Annotated[int, GitHubField("id")]
    login: Annotated[str | None, GitHubField("login")]

class AgentReference(TypedDict):
    id: Annotated[int, GitHubField("agent_id")]

    # "copilot-developer" | "copilot-developer-cli" | "copilot-pr-reviews" | "vscode-chat"
    slug: Annotated[str, GitHubField("slug")]

    # Seems to be combination of the following three IDs:
    #  - Owner ID (internal, not queryable)
    #  - Repository ID (internal, not queryable)
    #  - PR GraphQL ID (queryable) / some uuid (not clear what resource)
    task_id: Annotated[str | None, GitHubField("agent_task_id")]

    # "Integration" | "UserToServerToken" | "OauthApplication" | "IntegrationInstallation" | None
    type: Annotated[str | None, GitHubField("agent_type")]

class PullRequestIDReference(TypedDict):
    id: Annotated[int | None, GitHubField("id")]
    global_id: Annotated[str | None, GitHubField("global_id")]

class PullRequestReference(TypedDict):
    id: Annotated[int | None, GitHubField("resource_id")]
    global_id: Annotated[str | None, GitHubField("resource_global_id")]
    number: Annotated[int | None, GitHubField("resource_number")]
    state: Annotated[str | None, GitHubField("resource_state")]

class BranchReference(TypedDict):
    base_ref: Annotated[str, GitHubField("base_ref")]
    head_ref: Annotated[str | None, GitHubField("head_ref")]
