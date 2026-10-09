# Agent Task

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>Copilot cloud agent task.</td></tr>
<tr><th align="left">Parquet table</th><td><code>agent_tasks</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_task.py#L44"><code>agentlogs/schema/types/agent_task.py</code></a></td></tr>
</table>

## Data sources

- **Task list**: GitHub REST `GET /agents/repos/{owner}/{repo}/tasks` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks))
- **Task**: Copilot API `GET https://api.githubcopilot.com/agents/tasks/{id}` (no public documentation)

Fields and values on the Copilot API differ slightly from GitHub REST `GET /agents/tasks/{id}` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks#get-a-task-by-id)). Only successful GitHub API responses are stored. Other tables may contain references to this table with no matching row.

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>repository</code> | [Repository](repository.md) | <code>agent_tasks</code> |  |
| <code>sessions</code> (list) | [Agent Session](agent_session.md) | <code>task</code> |  |
| <code>creator</code> | [User](user.md) | <code>tasks</code> |  |
| <code>pull_request_artifacts</code> (list) | [Pull Request](pull_request.md) | <code>created_by_tasks</code> | Pull requests created by this task (REST `artifacts[]` of type `pull`). May include pull requests that are not on any listed session, possibly because a session was deleted (see [Agent Session](./agent_session.md) `pull_request_artifact`).  |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>id</code> | `str` | <code>id</code> |  |
| <code>repository</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>sessions</code> | `list[]` | <code>sessions[]</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>sessions[]</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;session_index</code> | `int` |  | Position of the session within the task. |
| <code>creator</code> | `struct{}` | <code>creator</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>creator</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>creator</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>creator</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) |  |  |
| <code>pull_request_artifacts</code> | `list[]` | <code>artifacts[]</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>artifacts[]</code><br><code>.data</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>artifacts[]</code><br><code>.data</code><br><code>.global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>name</code> | `str` (optional) | <code>name</code> |  |
| <code>state</code> | `str` | <code>state</code> |  |
| <code>archived</code> | `bool` |  |  |
| <code>remote_steerable</code> | `bool` | <code>remote_steerable</code> |  |
| <code>sharing_status</code> | `str` | <code>sharing_status</code> |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>archived_at</code> | `datetime` (optional) | <code>archived_at</code> |  |
| <code>custom_agent</code> | `struct{}` (optional) | <code>custom_agent</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` (optional) | <code>custom_agent</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;name</code> | `str` (optional) | <code>custom_agent</code><br><code>.name</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;is_automation</code> | `bool` (optional) | <code>custom_agent</code><br><code>.is_automation</code> |  |
| <code>automation_id</code> | `str` (optional) | <code>automation_id</code> |  |
| <code>agent_collaborators</code> | `list[]` | <code>agent_collaborators[]</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` | <code>agent_collaborators[]</code><br><code>.agent_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;slug</code> | `str` | <code>agent_collaborators[]</code><br><code>.slug</code> | `copilot-developer` or `copilot-pr-reviews`. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;task_id</code> | `str` (optional) | <code>agent_collaborators[]</code><br><code>.agent_task_id</code> | Usually `ownerId-repoId-uuid`, a bare UUID, or `owner:{id}:repo:{id}:pull:{id}`. Currently unknown what the UUID refers to. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>agent_collaborators[]</code><br><code>.agent_type</code> | `Integration`, `UserToServerToken`, `IntegrationInstallation`, or `OauthApplication`. |
| <code>branch_artifacts</code> | `list[]` | <code>artifacts[]</code> | Branches worked on and/or pushed to by this task (REST `artifacts[]` of type `branch`). May include branches that are not on any listed session, possibly because a session was deleted (see [Agent Session](./agent_session.md) `base` and `head`). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;base</code> | `struct{}` (optional) | <code>artifacts[]</code> | Branch the agent started from. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>artifacts[]</code><br><code>.base_ref</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;head</code> | `struct{}` (optional) | <code>artifacts[]</code> | Branch the agent created and/or pushed to. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>artifacts[]</code><br><code>.head_ref</code> |  |
