# AgentLogs

<a href="https://github.com/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/GitHub-risenlab%2Fagentlogs-181717?logo=github&amp;logoColor=whitesmoke" alt="GitHub risenlab/agentlogs"></a>
<a href="https://huggingface.co/datasets/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Hugging%20Face-risenlab%2Fagentlogs-ffd21e?logo=huggingface&amp;logoColor=whitesmoke" alt="Hugging Face risenlab/agentlogs"></a>
<a href="https://arxiv.org/abs/2608.29204" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/arXiv-2608.29204-b31b1b?logo=arxiv&amp;logoColor=whitesmoke" alt="arXiv 2608.29204"></a>

> :information_source: **Note:** This package contains the schema `v1.0`, which only works with dataset releases `1.0-xxxxxxxx`
>
> [Dataset releases](https://huggingface.co/datasets/risenlab/agentlogs#releases) | [Changelog](https://github.com/risenlab/agentlogs/blob/main/CHANGELOG.md)

TypedDict schema and helpers for the [AgentLogs](https://huggingface.co/datasets/risenlab/agentlogs) dataset. Field-level documentation: [schema reference](https://github.com/risenlab/agentlogs/tree/main/docs/schema).

## Installation

```bash
pip install risenlab-agentlogs huggingface_hub pyarrow
```

## Usage

```python
from pathlib import Path
from typing import cast

import pyarrow.parquet as pq
from huggingface_hub import snapshot_download
from agentlogs.schema import AgentSession, assert_dataset_version

# Full dataset into data/dataset/; existing files are skipped
dataset_path = Path("data") / "dataset"
snapshot_download(
    repo_id="risenlab/agentlogs",
    repo_type="dataset",
    revision="1.0-xxxxxxxx",
    local_dir=dataset_path,
)
# Fail if the snapshot schema does not match this package
assert_dataset_version(dataset_path)

# First session row, typed as AgentSession (nested fields included)
session_file = next((dataset_path / "agent_sessions").glob("*.parquet"))
session = cast(
    AgentSession,
    pq.read_table(session_file, memory_map=False).slice(0, 1).to_pylist()[0],
)
print(session["id"], session["name"])
```
