from __future__ import annotations

import datetime as dt
from typing import Any, Mapping, TypeVar, cast

from .types.agent_session import AgentSession
from .types.agent_session_log import AgentSessionLogEntry
from .types.agent_task import AgentTask
from .types.repository import Repository
from .types.user import User

T = TypeVar("T", bound=Mapping[str, Any])

TABLE_TYPES = frozenset(
    {
        Repository,
        AgentTask,
        AgentSession,
        AgentSessionLogEntry,
        User,
    }
)

def cast_record(cls: type[T], row: Mapping[str, Any]) -> T:
    if cls not in TABLE_TYPES:
        raise TypeError("cast_record only supports Repository, AgentTask, AgentSession, AgentSessionLogEntry, and User")

    record = cast(dict[str, Any], row)

    if cls is Repository:
        for key in ("created_at", "pushed_at", "updated_at", "last_commit_at"):
            value = record.get(key)
            if isinstance(value, dt.datetime) and value.tzinfo is None:
                record[key] = value.replace(tzinfo=dt.timezone.utc)

        languages = record.get("languages")
        if isinstance(languages, list):
            if not languages:
                record["languages"] = {}
            elif isinstance(languages[0], dict):
                record["languages"] = {entry["key"]: entry["value"] for entry in languages}
            else:
                record["languages"] = dict(languages)

    elif cls is AgentTask:
        data = record.get("data")
        if isinstance(data, dict):
            for key in ("created_at", "updated_at", "archived_at"):
                value = data.get(key)
                if isinstance(value, dt.datetime) and value.tzinfo is None:
                    data[key] = value.replace(tzinfo=dt.timezone.utc)

    elif cls is AgentSession:
        for key in ("created_at", "updated_at", "completed_at"):
            value = record.get(key)
            if isinstance(value, dt.datetime) and value.tzinfo is None:
                record[key] = value.replace(tzinfo=dt.timezone.utc)

    elif cls is AgentSessionLogEntry:
        data = record.get("data")
        if isinstance(data, dict):
            created = data.get("created")
            if isinstance(created, dt.datetime) and created.tzinfo is None:
                data["created"] = created.replace(tzinfo=dt.timezone.utc)

    return cast(T, record)
