# Agent Session

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>Copilot cloud agent session.</td></tr>
<tr><th align="left">Parquet table</th><td><code>agent_sessions</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_session.py#L26"><code>agentlogs/schema/types/agent_session.py</code></a></td></tr>
</table>

## Data sources

- **Session**: `sessions[]` on Copilot API `GET https://api.githubcopilot.com/agents/tasks/{id}` (no public documentation)

Fields and values differ slightly from GitHub REST `GET /agents/tasks/{id}` ([documentation](https://docs.github.com/en/rest/agent-tasks/agent-tasks#get-a-task-by-id)).

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>task</code> | [Agent Task](agent_task.md) | <code>sessions</code> |  |
| <code>user</code> | [User](user.md) | <code>sessions</code> |  |
| <code>pull_request_artifact</code> (optional) | [Pull Request](pull_request.md) | <code>created_by_sessions</code> | Pull request created by this session. Often also listed on the parent task ([pull request artifacts](./agent_task.md)). May be missing when the task still lists the pull request. |
| <code>workflow_run</code> (optional) | [Workflow Run](workflow_run.md) | <code>session</code> | Actions run that executed this session. |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>id</code> | `str` | <code>id</code> |  |
| <code>session_index</code> | `int` |  | Position of the session within the task. |
| <code>log_found</code> | `bool` |  |  |
| <code>task</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>user</code> | `struct{}` | <code>user</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>user</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>user</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>user</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) |  |  |
| <code>pull_request_artifact</code> | `struct{}` (optional) |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>workflow_run</code> | `struct{}` (optional) |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` | <code>workflow_run_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>base</code> | `struct{}` (optional) |  | Branch the agent started from. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>base_ref</code> |  |
| <code>head</code> | `struct{}` (optional) |  | Branch the agent created and/or pushed to. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>head_ref</code> |  |
| <code>name</code> | `str` | <code>name</code> |  |
| <code>model</code> | `str` (optional) | <code>model</code> |  |
| <code>prompt</code> | `str` (optional) | <code>prompt</code> |  |
| <code>reasoning_effort</code> | `str` (optional) | <code>reasoning_effort</code> |  |
| <code>state</code> | `str` | <code>state</code> |  |
| <code>usage</code> | `struct{}` (optional) | <code>usage</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` | <code>usage</code><br><code>.type</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;amount</code> | `float` (optional) | <code>usage</code><br><code>.amount</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;credits</code> | `float` (optional) | <code>usage</code><br><code>.credits</code> |  |
| <code>premium_requests</code> | `float` | <code>premium_requests</code> |  |
| <code>error</code> | `str` (optional) | <code>error</code><br><code>.message</code> |  |
| <code>remote_steerable</code> | `bool` (optional) | <code>remote_steerable</code> |  |
| <code>event</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>event_type</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;url</code> | `str` (optional) | <code>event_url</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ids</code> | `list[str]` (optional) | <code>event_identifiers</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;content</code> | `str` (optional) | <code>event_content</code> |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>completed_at</code> | `datetime` (optional) | <code>completed_at</code> |  |
