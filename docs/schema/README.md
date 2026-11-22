# Schema reference

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

This reference documents every table of the [AgentLogs dataset](https://huggingface.co/datasets/risenlab/agentlogs) of real-world AI coding agent activity on GitHub. For an overview of the dataset and how it was collected, see the [README](../../README.md).

Each table is a set of Parquet files. Its page lists the fields and their types, how the table links to other tables, and which GitHub or Copilot API each field comes from. The execution traces are in [Agent Session Log Entry](agent_session_log_entry.md).

| Table | Parquet table | Description |
| --- | --- | --- |
| [Repository](repository.md) | `repositories` | GitHub repository. |
| [Agent Task](agent_task.md) | `agent_tasks` | Agent assignment on a repository. |
| [Agent Session](agent_session.md) | `agent_sessions` | Execution of an agent on a task. |
| [Agent Session Log Entry](agent_session_log_entry.md) | `agent_session_logs` | One entry in the log of a session. |
| [User](user.md) | `users` | GitHub user, organization, or bot. |
| [Pull Request](pull_request.md) | `pull_requests` | GitHub pull request collected from a task or session. |
| [Pull Request Timeline Event](pull_request_timeline_event.md) | `pull_request_timelines` | One event from a pull request timeline. |
| [Workflow Run](workflow_run.md) | `workflow_runs` | GitHub Actions workflow run. |

Generated from [schema definitions](../../packages/risenlab-agentlogs/src/agentlogs/schema).
