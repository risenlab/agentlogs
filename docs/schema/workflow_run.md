# Workflow Run

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>GitHub Actions workflow run.</td></tr>
<tr><th align="left">Parquet table</th><td><code>workflow_runs</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/workflow_run.py#L16"><code>agentlogs/schema/types/workflow_run.py</code></a></td></tr>
</table>

## Data sources

- **Workflow run**: GitHub REST `GET /repos/{owner}/{repo}/actions/runs/{id}` ([documentation](https://docs.github.com/en/rest/actions/workflow-runs#get-a-workflow-run))

Only successful GitHub API responses are stored. Other tables may contain references to this table with no matching row.

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>repository</code> | [Repository](repository.md) |  |  |
| <code>head_repository</code> (uncollected) | [Repository](repository.md) |  | Not collected. May be absent from [repositories](./repository.md) (fork or not the task repository). |
| <code>actor</code> (optional) | [User](user.md) | <code>workflow_runs</code> |  |
| <code>triggering_actor</code> (optional) | [User](user.md) | <code>triggered_workflow_runs</code> |  |
| <code>session</code> | [Agent Session](agent_session.md) | <code>workflow_run</code> |  |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>id</code> | `int` | <code>id</code> |  |
| <code>repository</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>head_repository</code> | `struct{}` | <code>head_repository</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>actor</code> | `struct{}` (optional) | <code>actor</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>actor</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>actor</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>actor</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>actor</code><br><code>.type</code> |  |
| <code>triggering_actor</code> | `struct{}` (optional) | <code>triggering_actor</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>triggering_actor</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>triggering_actor</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>triggering_actor</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>triggering_actor</code><br><code>.type</code> |  |
| <code>session</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>name</code> | `str` (optional) | <code>name</code> |  |
| <code>graphql_id</code> | `str` | <code>node_id</code> |  |
| <code>check_suite</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>check_suite_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>check_suite_node_id</code> |  |
| <code>head</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sha</code> | `str` | <code>head_sha</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` (optional) | <code>head_branch</code> |  |
| <code>path</code> | `str` | <code>path</code> |  |
| <code>run_number</code> | `int` | <code>run_number</code> |  |
| <code>run_attempt</code> | `int` (optional) | <code>run_attempt</code> |  |
| <code>event</code> | `str` | <code>event</code> |  |
| <code>status</code> | `str` (optional) | <code>status</code> |  |
| <code>conclusion</code> | `str` (optional) | <code>conclusion</code> |  |
| <code>workflow_id</code> | `int` | <code>workflow_id</code> |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>run_started_at</code> | `datetime` (optional) | <code>run_started_at</code> |  |
| <code>display_title</code> | `str` | <code>display_title</code> |  |
