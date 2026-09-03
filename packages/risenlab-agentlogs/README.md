# AgentLogs

<a href="https://pypi.org/project/risenlab-agentlogs/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Version-v0.2-blue?logo=pypi&amp;logoColor=whitesmoke" alt="Version"></a>
<a href="https://huggingface.co/datasets/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Dataset-v0.2-ffd21e?logo=huggingface&amp;logoColor=whitesmoke" alt="Dataset"></a>
<a href="https://github.com/risenlab/agentlogs/tree/main" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Code-v0.2-181717?logo=github&amp;logoColor=whitesmoke" alt="Code"></a>
<a href="https://arxiv.org/abs/2608.29204" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Preprint-2608.29204-b31b1b.svg?logo=arxiv&amp;logoColor=whitesmoke" alt="Preprint"></a>

TypedDict schema and helpers for the [AgentLogs](https://huggingface.co/datasets/risenlab/agentlogs) dataset. Field-level documentation: [schema reference](https://github.com/risenlab/agentlogs/tree/main/docs/schema).

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
