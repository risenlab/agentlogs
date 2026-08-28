# AgentLogs

[![version 0.2](https://img.shields.io/badge/version-0.2-blue)](https://huggingface.co/datasets/risenlab/agentlogs/tree/v0.2)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-dataset-ffd21e?logo=huggingface&logoColor=ffd21e)](https://huggingface.co/datasets/risenlab/agentlogs)
[![GitHub](https://img.shields.io/badge/GitHub-code-black?logo=github)](https://github.com/risenlab/agentlogs)

TypedDict schema and helpers for the [AgentLogs](https://huggingface.co/datasets/risenlab/agentlogs) dataset. Field-level documentation: [schema reference](https://github.com/risenlab/agentlogs/tree/v0.2/docs/schema).

## Installation

```bash
pip install risenlab-agentlogs huggingface_hub pyarrow
```

## Usage

```python
from pathlib import Path

import pyarrow.parquet as pq
from huggingface_hub import snapshot_download
from agentlogs.schema import AgentSession, assert_dataset_version, cast_record

# Full dataset into data/dataset/; existing files are skipped
dataset_path = Path("data") / "dataset"
snapshot_download(
    repo_id="risenlab/agentlogs",
    repo_type="dataset",
    revision="v0.2",
    local_dir=dataset_path,
)
# Fail if the snapshot tag does not match this package version
assert_dataset_version(dataset_path)

# First session row, typed as AgentSession (nested fields included)
session_file = next((dataset_path / "agent_sessions").glob("*.parquet"))
session = cast_record(
    AgentSession,
    pq.read_table(session_file, memory_map=False).slice(0, 1).to_pylist()[0],
)
print(session["id"], session["name"])
```
