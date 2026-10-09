__version__ = "1.0"

from pathlib import Path

from .types.agent_session import (
    AgentSession,
    AgentSessionUsage,
    AgentSessionEvent,
)
from .types.agent_task import (
    AgentTask,
    AgentTaskSessionReference,
    BranchArtifactData,
    CustomAgentReference,
)
from .types.repository import (
    Repository,
    RepositoryLanguage,
    RepositoryMetric,
)
from .types.user import (
    User,
)
from .types.workflow_run import (
    WorkflowRun,
)
from .types.pull_request import (
    PullRequest,
    PullRequestTimelineEvent,
)
from .types.references import (
    AgentSessionReference,
    AgentTaskReference,
    RepositoryReference,
    UserReference,
    AgentReference,
    PullRequestReference,
    WorkflowRunReference,
    BranchReference,
    BranchCommitReference,
    CommitReference,
)
from .types.agent_session_log import (
    AgentSessionLogEntry,
    AgentSessionLogEntryData,
)
from .types.annotation import table_info

TABLES = (
    Repository,
    AgentTask,
    AgentSession,
    AgentSessionLogEntry,
    User,
    PullRequest,
    PullRequestTimelineEvent,
    WorkflowRun,
)

for table in TABLES:
    table_info(table)


class DatasetVersionError(ValueError):
    pass


def assert_version(version: str) -> None:
    version = version.removeprefix("v")
    schema = version.split("-", 1)[0]
    if schema != __version__:
        raise DatasetVersionError(
            f"Dataset schema {schema} does not match installed schema {__version__}."
        )


def assert_dataset_version(dataset_path: str | Path) -> None:
    assert_version(Path(dataset_path).joinpath("VERSION").read_text().strip())


__all__ = [
    "AgentSession",
    "AgentSessionUsage",
    "AgentSessionEvent",

    "AgentSessionLogEntry",
    "AgentSessionLogEntryData",

    "BranchArtifactData",
    "AgentTask",
    "AgentTaskSessionReference",
    "CustomAgentReference",
    "PullRequestReference",
    "WorkflowRunReference",
    "BranchReference",
    "BranchCommitReference",
    "CommitReference",
    
    "Repository",
    "RepositoryLanguage",
    "RepositoryMetric",

    "User",

    "WorkflowRun",
    "PullRequest",
    "PullRequestTimelineEvent",

    "AgentSessionReference",
    "AgentTaskReference",
    "RepositoryReference",
    "UserReference",
    "AgentReference",

    "TABLES",
    "DatasetVersionError",
    "assert_dataset_version",
    "assert_version",
    "__version__",
]