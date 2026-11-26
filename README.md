# AgentLogs

<a href="https://risenlab.com/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Website-risenlab.com%2Fagentlogs-7a61dd" alt="Website https://risenlab.com/agentlogs"></a>
<a href="https://pypi.org/project/risenlab-agentlogs/" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/PyPI-risenlab--agentlogs-blue?logo=pypi&amp;logoColor=whitesmoke" alt="PyPI risenlab-agentlogs"></a>
<a href="https://huggingface.co/datasets/risenlab/agentlogs" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Hugging%20Face-risenlab%2Fagentlogs-ffd21e?logo=huggingface&amp;logoColor=whitesmoke" alt="Hugging Face risenlab/agentlogs"></a>
<a href="https://arxiv.org/abs/2608.29204" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/arXiv-2608.29204-b31b1b?logo=arxiv&amp;logoColor=whitesmoke" alt="arXiv 2608.29204"></a>

AgentLogs is a large-scale dataset of real-world AI coding agent activity on GitHub. It shows how agents work and how developers steer them, not just the pull requests they produce.

**Highlights**

- **Scale**: 636K agent sessions in 364K tasks across 40.6K public repositories, with 75.6M log entries and 28.5M tool calls, in the latest release (`1.0-20261008`)
- **Multi-turn tasks**: tasks are conversations with one session per developer request, including follow-ups given in pull request comments and reviews
- **Execution traces**: every step of a session, with prompts, reasoning, tool calls and their results, and token usage
- **Complete code changes**: every tool call keeps its full arguments, so each file edit records the exact text replaced and inserted, and each new file its full content
- **Outcomes**: the linked pull requests, their timelines, and the workflow runs that executed each session
- **Unfiltered**: sessions with any outcome, including errors and pull requests that were never merged
- **Research uses**: agent behavior and failure modes, multi-turn developer–agent collaboration, tool use, efficiency and cost, and agent adoption across repositories
- **Open**: the full dataset, under CC BY 4.0

For an example session, first findings, and a five-minute video introduction, visit the [dataset homepage](https://risenlab.com/agentlogs).

This repository contains the pipeline that collects the dataset, its schema definitions and documentation, example analysis notebooks, and a sample of the data.

This dataset is described in:

> 📄 Jonan Richards, Kosei Horikawa, Youmei Fan, Yutaro Kashiwa, and Mairieli Wessel (2026), *AgentLogs: A Dataset for Opening the Black Box of Cloud Agents on GitHub*. arXiv: [2608.29204](https://arxiv.org/abs/2608.29204) (preprint).

**Contents**

- [Dataset summary](#dataset-summary)
- [Dataset contents](#dataset-contents)
  - [Tables](#tables)
  - [Scope](#scope)
  - [Releases](#releases)
- [Using the dataset](#using-the-dataset)
  - [Quick start](#quick-start)
  - [Analysis examples](#analysis-examples)
- [This repository](#this-repository)
  - [Layout](#layout)
  - [Collecting data](#collecting-data)
- [Citation](#citation)
- [License](#license)

## Dataset summary

On GitHub, developers start a cloud agent on a coding task by assigning it an issue, mentioning it on a pull request (e.g., `@copilot`), writing a prompt on the repository's Agents tab, or through integrations such as Slack and Jira. The agent works on its own branch and opens a pull request. Developers then review its work and steer it with follow-up requests in comments and reviews, until the task is done. Each follow-up starts a new session in the same task.

> [!TIP]
> Other datasets call a conversation with an agent a *session*. In AgentLogs, that conversation is a **task**, and each turn or prompt in it is a **session**.

Nearly all sessions are by the Copilot cloud agent, which ran 44 different models, mostly from the Claude and GPT families. Most of the rest are by third-party agents on the same platform, such as Anthropic's Claude agent and OpenAI's Codex.

On public repositories, GitHub shows every cloud agent task, session, and log on the repository's Agents tab, so AgentLogs collects this activity without developers having to opt in or install anything. Starting from all public repositories with at least 10 stars in [SEART GitHub Search](https://seart-ghs.si.usi.ch/), it lists every task through the GitHub REST API, fetches sessions and logs from the GitHub Copilot API, and links each session to its pull request, timeline, workflow run, and users.

## Dataset contents

### Tables

| | # Records | Size | Table | Content |
| --- | ---: | ---: | --- | --- |
| **Repositories**<br><small>–&nbsp;2.18% with agent tasks</small> | 1,861,300<br><small>–&nbsp;40,565</small> | 462.7&nbsp;MB | [`repositories`](docs/schema/repository.md) | Public GitHub repositories with at least 10 stars (metadata including name, license, language, stars, forks, timestamps, labels, topics). |
| **Agent tasks**<br><small>–&nbsp;97.20% with sessions</small> | 363,624<br><small>–&nbsp;353,432</small> | 83.7&nbsp;MB | [`agent_tasks`](docs/schema/agent_task.md) | Agent assignments on a repository (metadata including name, request, state, creator, timestamps, branch/PR identifiers). |
| **Agent sessions**<br><small>–&nbsp;98.24% with session logs</small> | 635,886<br><small>–&nbsp;624,668</small> | 243.1&nbsp;MB | [`agent_sessions`](docs/schema/agent_session.md) | Executions of an agent on a task (metadata including model, prompt, outcome, usage, workflow run, and branch/PR identifier for that session). |
| **Log entries** | 75,631,136 | 63.0&nbsp;GB | [`agent_session_logs`](docs/schema/agent_session_log_entry.md) | Session log events (including messages, usage details, tool calls for file edits, git, and GitHub issues, PRs, comments, CI). |
| **Users**<br><small>–&nbsp;4.40% with tasks or sessions</small> | 857,428<br><small>–&nbsp;37,714</small> | 211.5&nbsp;MB | [`users`](docs/schema/user.md) | Users, organizations, and bots related to the other tables (GitHub id, login slug, and creation date). |
| **Pull requests** | 317,878 | 483.9&nbsp;MB | [`pull_requests`](docs/schema/pull_request.md) | Pull requests worked on in agent tasks and sessions (GitHub id, number, state, and branches). |
| **Pull request timeline events** | 9,070,939 | 327.4&nbsp;MB | [`pull_request_timelines`](docs/schema/pull_request_timeline_event.md) | Timeline events for a pull request (actor, label, commit, and message). |
| **Workflow runs** | 554,496 | 83.3&nbsp;MB | [`workflow_runs`](docs/schema/workflow_run.md) | GitHub Actions workflow runs that executed an agent session (status, head commit, and triggering user/bot). |
| **Total** | **89,292,687** | **64.9&nbsp;GB** | | |

> [!TIP]
> The [schema reference](docs/schema/README.md) documents every table: its fields and types, how it links to other tables, and which GitHub or Copilot API each field comes from. Click a table name above to open its page.

### Scope

The `1.0-20261008` release covers sessions from May 11, 2025 to the cutoff on September 29, 2026.

| ✅ Included | ❌ Not included |
| --- | --- |
| Sessions with any outcome, including errors and pull requests that were never merged | Sessions run locally, outside GitHub's cloud agent platform |
| Repositories without any tasks | Private repositories |
| Sessions whose log was not found, without log entries | Repositories deleted, renamed, or made private before collection |
| Users' login, GitHub ID, and account creation date | Profile fields such as name, email, or bio |
| Multi-turn conversations: every follow-up request that steered the agent on its pull request | Real-time chat with an agent in an IDE or terminal |

### Releases

The full dataset is published on [Hugging Face](https://huggingface.co/datasets/risenlab/agentlogs). This repository includes a sample of the `1.0-20261008` release under `data/dataset-sample/`.

<table>
<thead><tr><th>Schema version</th><th>Dataset release</th><th>Release date</th><th>Cutoff date</th></tr></thead>
<tbody>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/1.0.0/">v1.0</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/1.0-20261008">1.0-20261008</a></td><td>October 8, 2026</td><td>September 29, 2026</td></tr>
<tr><td rowspan="1"><a href="https://pypi.org/project/risenlab-agentlogs/0.2.0/">v0.2</a></td><td><a href="https://huggingface.co/datasets/risenlab/agentlogs/tree/v0.2">0.2</a></td><td>August 29, 2026</td><td>July 17, 2026</td></tr>
</tbody>
</table>

Each release only works with its schema version, so pin the Python package to match, for example with `~=1.0.0`. The schema documentation and example notebooks in this repository follow schema `v1.0`. See the [changelog](CHANGELOG.md) for what changed between releases.

## Using the dataset

### Quick start

**1. Install the Python package** with the schema types and helpers:

```bash
pip install 'risenlab-agentlogs~=1.0.0' huggingface_hub
```

**2. Download the dataset** from Hugging Face. To try things out first, use the small [sample](https://github.com/risenlab/agentlogs/tree/main/data/dataset-sample) in the GitHub repository instead.

```python
from pathlib import Path
from huggingface_hub import snapshot_download
from agentlogs.schema import assert_dataset_version

dataset_path = Path("data") / "dataset"
snapshot_download(
    repo_id="risenlab/agentlogs",
    repo_type="dataset",
    revision="1.0-20261008",
    local_dir=dataset_path,
    # To download only some tables: allow_patterns=["VERSION", "agent_tasks/*", "agent_sessions/*"]
)
assert_dataset_version(dataset_path)
```

**3. Analyze it** with the tools you know. Each table is a folder of Parquet files that DuckDB, Polars, or pandas can read directly. For typed access to records, import the schema types:

```python
from agentlogs.schema import AgentSessionLogEntry, Repository, AgentTask, ...
```

The [analysis examples](#analysis-examples) below compare querying the dataset with DuckDB, Polars, and typed streaming.

### Analysis examples

The notebooks in [`scripts/analysis/`](scripts/analysis/) show three ways to work with the dataset. Run them on the bundled sample in `data/dataset-sample/`, or on a full snapshot downloaded into `data/dataset/` (see [Quick start](#quick-start)). Pick the one that fits your analysis and the tools you know:

| | DuckDB | Polars | Streaming |
| --- | --- | --- | --- |
| **Notebook** | [`examples_duckdb.ipynb`](scripts/analysis/examples_duckdb.ipynb) | [`examples_polars.ipynb`](scripts/analysis/examples_polars.ipynb) | [`examples_streaming.ipynb`](scripts/analysis/examples_streaming.ipynb) |
| **How it works** | SQL over the Parquet files, like a database, aggregating without loading the dataset into memory | Lazy DataFrames, similar to pandas, that scan files and so handle data larger than memory | Typed records read in small batches, with autocomplete and type checking down to nested fields |
| **✅ Good for** | • SQL (`COUNT`, `GROUP BY`, joins across tables)<br>• Exploring the dataset quickly<br>• Summary statistics over full tables | • Multi-step pipelines in Python<br>• Balancing memory use and run time<br>• Aggregating over nested fields | • Inspecting individual records and nested fields<br>• Custom Python logic per row, such as regex parsing or sequence analysis<br>• Low memory use, one batch at a time |
| **⚠️ Not ideal for** | • Reusable Python pipelines<br>• Complex logic on individual rows | • Analyses that fit in a single query<br>• Complex logic on individual rows | • Counts or distributions over full tables or single columns |

## This repository

### Layout

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

### Collecting data

The scripts in [`scripts/collect/`](scripts/collect/) download a seed repository list and fill a job queue. They then collect from the GitHub and Copilot APIs and export the eight Parquet tables.

#### Requirements

```bash
pip install -r scripts/collect/requirements.txt
```

Copy [`api_tokens_example.toml`](api_tokens_example.toml) to `api_tokens.toml` and fill in your tokens.

- **GitHub:** classic personal access tokens
- **Copilot:** use `gh auth token` after authenticating with the GitHub CLI (personal access tokens do not work for the Copilot API)

#### Running

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

#### How it works

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

The GitHub Search seed CSV is downloaded at collection time and is not distributed with AgentLogs. The `repositories` table is built from that CSV.
