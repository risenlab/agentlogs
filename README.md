# AgentLogs

<a href="https://pypi.org/project/risenlab-agentlogs/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/PyPI-risenlab--agentlogs-blue?logo=pypi&amp;logoColor=whitesmoke" alt="PyPI risenlab-agentlogs"></a>
<a href="https://huggingface.co/datasets/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Hugging%20Face-risenlab%2Fagentlogs-ffd21e?logo=huggingface&amp;logoColor=whitesmoke" alt="Hugging Face risenlab/agentlogs"></a>
<a href="https://arxiv.org/abs/2608.29204" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/arXiv-2608.29204-b31b1b?logo=arxiv&amp;logoColor=whitesmoke" alt="arXiv 2608.29204"></a>

> [!NOTE]
> The latest dataset release is `1.0-20261008`. Schema documentation and example notebooks follow schema `v1.0`
>
> [Dataset releases](#releases) | [Changelog](CHANGELOG.md)

AgentLogs is a dataset of activity related to the [GitHub agents functionality](https://github.com/features/copilot/agents): repository metadata, agent tasks, sessions, session logs (messages, tool calls, usage details, etc.), and user records. This repository contains schema definitions, example analysis notebooks, and a sample of the dataset.

This dataset is described in:

> 📄 Jonan Richards, Kosei Horikawa, Youmei Fan, Yutaro Kashiwa, and Mairieli Wessel (2026), *AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent*. arXiv: [2608.29204](https://arxiv.org/abs/2608.29204) (preprint).

## Dataset

| | # Records | Size | Table | Content |
| --- | ---: | ---: | --- | --- |
| **Repositories**<br><small>−&nbsp;2.18% with agent tasks</small> | 1,861,300<br><small>-&nbsp;40,565</small> | 462.7&nbsp;MB | [`repositories`](docs/schema/repository.md) | Public GitHub repositories with over 10 stars (metadata including name, license, language, stars, forks, timestamps, labels, topics). |
| **Agent tasks**<br><small>−&nbsp;97.20% with sessions</small> | 363,624<br><small>-&nbsp;353,432</small> | 83.7&nbsp;MB | [`agent_tasks`](docs/schema/agent_task.md) | Agent assignment on a repository (metadata including name, request, state, creator, timestamps, branch/PR identifiers). |
| **Agent sessions**<br><small>−&nbsp;98.24% with session logs</small> | 635,886<br><small>-&nbsp;624,668</small> | 243.1&nbsp;MB | [`agent_sessions`](docs/schema/agent_session.md) | Agent runs within a task (metadata including model, prompt, outcome, usage, and branch/PR identifier for that session). |
| **Log entries**<br><small>−&nbsp;>99.99% parsed</small> | 75,631,136<br><small>-&nbsp;75,630,896</small> | 63.0&nbsp;GB | [`agent_session_logs`](docs/schema/agent_session_log_entry.md) | Session log events (including messages, usage details, tool calls for file edits, git, and GitHub issues, PRs, comments, CI). |
| **Users**<br><small>−&nbsp;4.40% with tasks or sessions</small> | 857,428<br><small>-&nbsp;37,714</small> | 211.5&nbsp;MB | [`users`](docs/schema/user.md) | Users, organizations, and bots related to the other tables (GitHub id, login slug, and creation date). |
| **Pull requests**<br><small>−&nbsp;99.82% with timeline events</small> | 317,878<br><small>-&nbsp;317,297</small> | 483.9&nbsp;MB | [`pull_requests`](docs/schema/pull_request.md) | Pull requests created by agent tasks and sessions (GitHub id, number, state, and branches). |
| **Pull request timeline events** | 9,070,939 | 327.4&nbsp;MB | [`pull_request_timelines`](docs/schema/pull_request_timeline_event.md) | Timeline events for collected pull requests (actor, label, commit, and message). |
| **Workflow runs** | 554,496 | 83.3&nbsp;MB | [`workflow_runs`](docs/schema/workflow_run.md) | GitHub Actions runs that executed agent sessions (status, head commit, and triggering user/bot). |
| **Total** | **89,292,687** | **64.9&nbsp;GB** | | |

See the [schema reference](docs/schema/README.md) for field-level documentation of each table.

### Releases

The full dataset is published on [Hugging Face](https://huggingface.co/datasets/risenlab/agentlogs). This repository includes a sample of the `1.0-20261008` release under `data/dataset-sample/`.

<table>
<thead><tr><th>Schema version</th><th>Dataset release</th><th>Release date</th><th>Cutoff date</th></tr></thead>
<tbody>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/1.0.0/">v1.0</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/1.0-20261008">1.0-20261008</a></td><td>8 October, 2026</td><td>30 August, 2026</td></tr>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/0.2.0/">v0.2</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/v0.2">0.2</a></td><td>29 August, 2026</td><td>17 July, 2026</td></tr>
</tbody>
</table>

## This repository

| Path | Description |
| --- | --- |
| [`packages/risenlab-agentlogs/`](packages/risenlab-agentlogs/) | TypedDict schema definitions |
| [`scripts/analysis/`](scripts/analysis/) | Example notebooks for analyzing the dataset |
| [`data/dataset-sample/`](data/dataset-sample/) | Sample of the dataset for demonstration purposes |
| [`docs/schema/`](docs/schema/) | Field-level schema documentation |
| [`CHANGELOG.md`](CHANGELOG.md) | Schema and repository changelog |
| [`LICENSE`](LICENSE) | MIT license for code in this repository |
| [`DATA_LICENSE`](DATA_LICENSE) | CC BY 4.0 license for the AgentLogs dataset (includes GHS MIT notice) |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install risenlab-agentlogs
# or from this repository: pip install -e packages/risenlab-agentlogs
```

Import types in your own code:

```python
from agentlogs.schema import AgentSessionLogEntry, Repository, AgentTask, ...
```

## Analysis examples

The notebooks in [`scripts/analysis/`](scripts/analysis/) show different ways to work with the dataset. DuckDB, Polars, and streaming read parquet from disk: use the bundled sample under `data/dataset-sample/`, or download a Hub snapshot into `data/dataset/`. Which approach to take depends on the kind of analysis you are doing and what tools you are familiar with.

### [`examples_duckdb.ipynb`](scripts/analysis/examples_duckdb.ipynb): DuckDB, SQL querying over Parquet

Query the dataset with SQL similar to a database. DuckDB can read Parquet directly from disk, so you can aggregate without loading the entire dataset into memory.

**Good for:**

- Accessing the dataset using SQL (`COUNT`, `GROUP BY`, joins across tables).
- Exploring the dataset quickly.
- Computing summary statistics over full tables.

**Not ideal for:**

- Writing a reusable Python analysis pipeline instead of single-use queries (see Polars).
- Complex logic on individual rows with IDE autocompletion (see streaming).

### [`examples_polars.ipynb`](scripts/analysis/examples_polars.ipynb): Polars, lazy-loaded DataFrames

Load and transform the data using Polars, a DataFrame library similar to pandas. However, it can handle datasets larger than the available memory by scanning files lazily.

**Good for:**

- Building multi-step pipelines within Python.
- Balancing memory usage and time to run.
- Aggregating over nested fields.

**Not ideal for:**

- Analysis that can be written as a single query instead of a pipeline (see DuckDB).
- Complex logic on individual rows with IDE autocompletion (see streaming).

### [`examples_streaming.ipynb`](scripts/analysis/examples_streaming.ipynb): Streaming, iterating row-by-row with type support

Read local Parquet tables in small batches and iterate over individual records. Each record is typed, so you get autocomplete and type checking (also for nested fields)!

**Good for:**

- Inspecting individual records and nested fields.
- Running custom Python logic per row (e.g. regex parsing, sequence analysis).
- Low memory usage, by processing one batch at a time.

**Not ideal for:**

- Computing counts or distributions over the full dataset and/or for single columns (see DuckDB and Polars).

## Citation

If you use AgentLogs in an academic publication, please cite this preprint:

```bibtex
@misc{richards2026AgentLogsDatasetOpening,
  title = {{AgentLogs: A Dataset for Opening the Black Box of GitHub's Cloud Agent}},
  author = {Richards, Jonan and Horikawa, Kosei and Fan, Youmei and Kashiwa, Yutaro and Wessel, Mairieli},
  year = 2026,
  month = aug,
  eprint = {2608.29204},
  primaryclass = {cs.SE},
  doi = {10.48550/arXiv.2608.29204},
  archiveprefix = {arXiv},
  url = {https://arxiv.org/abs/2608.29204}
}
```

## License

This repository contains both **code** and **data**, under different licenses:

- **Code** (packages, scripts, notebooks): [MIT](LICENSE)
- **Dataset** (sample under `data/dataset-sample/` and the Hugging Face release): [CC BY 4.0](DATA_LICENSE)

Repository sampling for AgentLogs uses [GitHub Search](https://seart-ghs.si.usi.ch/)
([GitHub](https://github.com/seart-group/ghs), [Zenodo](https://doi.org/10.5281/zenodo.4588464))
&copy; SEART Research Group and Contributors, used under the
[MIT License](https://github.com/seart-group/ghs/blob/master/LICENSE).

The GitHub Search seed CSV is downloaded at collection time and is not distributed with this repository. The `repositories` table is built from that CSV.
