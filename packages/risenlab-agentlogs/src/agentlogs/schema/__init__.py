__version__ = "0.2"

from pathlib import Path

from .types.agent_session import (
    AgentSession,
    AgentSessionUsage,
    AgentSessionEvent,
)
from .types.agent_task import (
    AgentArtifactReference,
    AgentTask,
    AgentTaskData,
    CustomAgentReference,
)
from .types.repository import (
    Repository,
    RepositoryMetric,
)
from .types.user import (
    User,
)
from .types.references import (
    AgentSessionReference,
    AgentTaskReference,
    RepositoryReference,
    UserReference,
    AgentReference,
    PullRequestIDReference,
    PullRequestReference,
    BranchReference,
)
from .types.agent_session_log import (
    AgentSessionLogEntry,
    AgentSessionLogEntryData,
)
from .cast import cast_record


class DatasetVersionError(ValueError):
    pass


def assert_version(version: str) -> None:
    version = version.removeprefix("v")
    if version != __version__:
        raise DatasetVersionError(
            f"Dataset version {version} does not match schema {__version__}. "
            f"Install risenlab-agentlogs {version} or snapshot revision v{__version__}."
        )


def assert_dataset_version(dataset_path: str | Path) -> None:
    assert_version(Path(dataset_path).joinpath("VERSION").read_text().strip())


__all__ = [
    "AgentSession",
    "AgentSessionUsage",
    "AgentSessionEvent",

    "AgentSessionLogEntry",
    "AgentSessionLogEntryData",

    "AgentArtifactReference",
    "PullRequestReference",
    "BranchReference",
    "AgentTask",
    "AgentTaskData",
    "CustomAgentReference",
    "PullRequestIDReference",
    "PullRequestReference",
    "BranchReference",
    
    "Repository",
    "RepositoryMetric",

    "User",

    "AgentSessionReference",
    "AgentTaskReference",
    "RepositoryReference",
    "UserReference",
    "AgentReference",

    "cast_record",
    "DatasetVersionError",
    "assert_dataset_version",
    "assert_version",
    "__version__",
]