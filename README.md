# AgentLogs

<a href="https://pypi.org/project/risenlab-agentlogs/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/PyPI-risenlab--agentlogs-blue?logo=pypi&amp;logoColor=whitesmoke" alt="PyPI risenlab-agentlogs"></a>
<a href="https://huggingface.co/datasets/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Hugging%20Face-risenlab%2Fagentlogs-ffd21e?logo=huggingface&amp;logoColor=whitesmoke" alt="Hugging Face risenlab/agentlogs"></a>
<a href="https://arxiv.org/abs/2608.29204" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/arXiv-2608.29204-b31b1b?logo=arxiv&amp;logoColor=whitesmoke" alt="arXiv 2608.29204"></a>

> [!NOTE]
> The latest dataset release is `1.0-20261008`. Schema documentation and example notebooks follow schema `v1.0`
>
> [Dataset releases](#releases) | [Changelog](CHANGELOG.md)

AgentLogs is a dataset of activity on [GitHub's cloud agent platform](https://github.com/features/copilot/agents): repository metadata, agent tasks, sessions, session logs (messages, tool calls, usage details, etc.), and user records. This repository contains schema definitions, example analysis notebooks, and a sample of the dataset.

This dataset is described in:

> 📄 Jonan Richards, Kosei Horikawa, Youmei Fan, Yutaro Kashiwa, and Mairieli Wessel (2026), *AgentLogs: A Dataset for Opening the Black Box of Cloud Agents on GitHub*. arXiv: [2608.29204](https://arxiv.org/abs/2608.29204) (preprint).

## Dataset

| | # Records | Size | Table | Content |
| --- | ---: | ---: | --- | --- |
| **Repositories**<br><small>−&nbsp;2.18% with agent tasks</small> | 1,861,300<br><small>-&nbsp;40,565</small> | 462.7&nbsp;MB | [`repositories`](docs/schema/repository.md) | Public GitHub repositories with over 10 stars (metadata including name, license, language, stars, forks, timestamps, labels, topics). |
| **Agent tasks**<br><small>−&nbsp;97.20% with sessions</small> | 363,624<br><small>-&nbsp;353,432</small> | 83.7&nbsp;MB | [`agent_tasks`](docs/schema/agent_task.md) | Agent assignments on a repository (metadata including name, request, state, creator, timestamps, branch/PR identifiers). |
| **Agent sessions**<br><small>−&nbsp;98.24% with session logs</small> | 635,886<br><small>-&nbsp;624,668</small> | 243.1&nbsp;MB | [`agent_sessions`](docs/schema/agent_session.md) | Executions of an agent on a task (metadata including model, prompt, outcome, usage, workflow run, and branch/PR identifier for that session). |
| **Log entries**<br><small>−&nbsp;>99.99% parsed</small> | 75,631,136<br><small>-&nbsp;75,630,896</small> | 63.0&nbsp;GB | [`agent_session_logs`](docs/schema/agent_session_log_entry.md) | Session log events (including messages, usage details, tool calls for file edits, git, and GitHub issues, PRs, comments, CI). |
| **Users**<br><small>−&nbsp;4.40% with tasks or sessions</small> | 857,428<br><small>-&nbsp;37,714</small> | 211.5&nbsp;MB | [`users`](docs/schema/user.md) | Users, organizations, and bots related to the other tables (GitHub id, login slug, and creation date). |
| **Pull requests**<br><small>−&nbsp;99.82% with timeline events</small> | 317,878<br><small>-&nbsp;317,297</small> | 483.9&nbsp;MB | [`pull_requests`](docs/schema/pull_request.md) | Pull requests worked on in agent tasks and sessions (GitHub id, number, state, and branches). |
| **Pull request timeline events** | 9,070,939 | 327.4&nbsp;MB | [`pull_request_timelines`](docs/schema/pull_request_timeline_event.md) | Timeline events for a pull request (actor, label, commit, and message). |
| **Workflow runs** | 554,496 | 83.3&nbsp;MB | [`workflow_runs`](docs/schema/workflow_run.md) | GitHub Actions workflow runs that executed an agent session (status, head commit, and triggering user/bot). |
| **Total** | **89,292,687** | **64.9&nbsp;GB** | | |

See the [schema reference](docs/schema/README.md) for field-level documentation of each table.

### Releases

The full dataset is published on [Hugging Face](https://huggingface.co/datasets/risenlab/agentlogs). This repository includes a sample of the `1.0-20261008` release under `data/dataset-sample/`.

<table>
<thead><tr><th>Schema version</th><th>Dataset release</th><th>Release date</th><th>Cutoff date</th></tr></thead>
<tbody>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/1.0.0/">v1.0</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/1.0-20261008">1.0-20261008</a></td><td>8 October, 2026</td><td>29 September, 2026</td></tr>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/0.2.0/">v0.2</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/v0.2">0.2</a></td><td>29 August, 2026</td><td>17 July, 2026</td></tr>
</tbody>
</table>

## This repository

| Path | Description |
| --- | --- |
| [`packages/risenlab-agentlogs/`](packages/risenlab-agentlogs/) | TypedDict schema definitions |
| [`packages/risenlab-agentlogs-collector/`](packages/risenlab-agentlogs-collector/) | Collection pipeline (seed, collect, export) |
| [`scripts/collect/`](scripts/collect/) | Seed, collect, and export scripts |
| [`scripts/analysis/`](scripts/analysis/) | Example notebooks for analyzing the dataset |
| [`api_tokens_example.toml`](api_tokens_example.toml) | Token file shape; copy to `api_tokens.toml` |
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

## Collecting data

The scripts in [`scripts/collect/`](scripts/collect/) download a seed repository list and fill a job queue. They then collect from the GitHub and Copilot APIs and export the eight Parquet tables.

### Setup

```bash
pip install -r scripts/collect/requirements.txt
```

Copy [`api_tokens_example.toml`](api_tokens_example.toml) to `api_tokens.toml` and fill in your tokens.

- **GitHub:** classic personal access tokens
- **Copilot:** use `gh auth token` after authenticating with the GitHub CLI (personal access tokens do not work for the Copilot API)

### Running

```bash
# Download the seed repository list (from GitHub Search; see DATA_LICENSE)
python scripts/collect/download_seed.py

# Seed the job queue (creates data/collect/)
python scripts/collect/seed.py --init

# Run data collection (GitHub API + Copilot API, fully resumable)
python scripts/collect/run.py

# Export collected data to Parquet (creates data/dataset/)
python scripts/collect/export.py
```

### How it works

Work is a SQLite job queue. `seed.py` and `run.py` call into the collector package:

- [`state/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/state/): stores the job queue in a SQLite database and resource bodies as compressed files.
- [`api/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/api/): fetches from GitHub and Copilot, respects rate limits, and rotates through multiple tokens.
- [`resources/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/resources/): types for the GitHub and Copilot objects returned by the API and saved in the collection state, until transformed to the final export format.
- [`runtime/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/runtime/): schedules workers and runs the GraphQL/REST lookups.
- [`export/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/export/): transforms collected resources into the eight Parquet tables.
- [`pipeline.py`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/pipeline.py): starts the seed and collect workers.

Each job type lives in [`steps/`](packages/risenlab-agentlogs-collector/src/agentlogs/collector/steps/): one file (`collect_task.py`, and so on) with the job, the code that runs it, and the later jobs it creates. They run in this order:

1. `seed_repositories`: loads the CSV and queues a listing job per repository.
2. `collect_repository_tasks`: lists agent tasks on GitHub REST and queues a `collect_task` per task, plus jobs to look up the owner.
3. `collect_task`: fetches a task and its sessions from Copilot. It writes the sessions, and queues session-log, workflow-run, user, and pull-request jobs.
4. `collect_session_log`: fetches the session transcript from Copilot.
5. `collect_workflow_run`: fetches the GitHub Actions workflow run from GitHub REST and queues user lookups.
6. `collect_user_*`: looks up a user (GraphQL node id, minted id, login, or REST id).
7. `collect_pull_request_*`: looks up a pull request (GraphQL global id, number+repo, minted id, or REST number+repo) and queues a timeline job.
8. `collect_pull_request_timeline`: pages timeline events on GitHub REST, writes the events, and queues user lookups.

Sessions do not have their own collect job, but are written when collecting a task.

The pipeline is fully resumable, re-run `scripts/collect/run.py` to pick up where it left off. Re-run `export.py` to regenerate Parquet from the current state.

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
  title = {{AgentLogs: A Dataset for Opening the Black Box of Cloud Agents on GitHub}},
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
