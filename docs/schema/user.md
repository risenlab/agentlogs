# User

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>GitHub user, organization, or bot.</td></tr>
<tr><th align="left">Parquet table</th><td><code>users</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/user.py#L17"><code>agentlogs/schema/types/user.py</code></a></td></tr>
</table>

## Data sources

- User (see [`found_using`](#fields)):
    - `graphql_node_id`: GitHub GraphQL `node(id:)` with a stored node id ([documentation](https://docs.github.com/en/graphql/reference/queries#node))
    - `rest_id`: GitHub REST `GET /user/{id}` ([documentation](https://docs.github.com/en/rest/users/users#get-a-user-using-their-id))
    - `graphql_mint_global_id`: GitHub GraphQL `node(id:)` with a minted `global_id` from the base64-encoded `04:User{id}` ([documentation](https://docs.github.com/en/graphql/reference/queries#node))
    - `graphql_login`: GitHub GraphQL `repositoryOwner(login:)` ([documentation](https://docs.github.com/en/graphql/reference/queries#repositoryowner))

Only successful GitHub API responses are stored. Other tables may contain references to this table with no matching row.

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>tasks</code> (list) | [Agent Task](agent_task.md) | <code>creator</code> |  |
| <code>sessions</code> (list) | [Agent Session](agent_session.md) | <code>user</code> |  |
| <code>repositories</code> (list) | [Repository](repository.md) | <code>owner</code> | User's repositories that appear in the seed (see [repository schema](./repository.md)). Does not include public repositories not in this seed or any private repositories. |
| <code>pull_requests</code> (list) | [Pull Request](pull_request.md) | <code>user</code> |  |
| <code>assigned_pull_requests</code> (list) | [Pull Request](pull_request.md) | <code>assignees</code> |  |
| <code>review_requested_pull_requests</code> (list) | [Pull Request](pull_request.md) | <code>requested_reviewers</code> |  |
| <code>merged_pull_requests</code> (list) | [Pull Request](pull_request.md) | <code>merged_by</code> |  |
| <code>auto_merge_enabled_pull_requests</code> (list) | [Pull Request](pull_request.md) | <code>auto_merge.enabled_by</code> |  |
| <code>timeline_events</code> (list) | [Pull Request Timeline Event](pull_request_timeline_event.md) | <code>actor</code> |  |
| <code>assigned_timeline_events</code> (list) | [Pull Request Timeline Event](pull_request_timeline_event.md) | <code>assignee</code> |  |
| <code>workflow_runs</code> (list) | [Workflow Run](workflow_run.md) | <code>actor</code> |  |
| <code>triggered_workflow_runs</code> (list) | [Workflow Run](workflow_run.md) | <code>triggering_actor</code> |  |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>id</code> | `int` | <code>id</code> |  |
| <code>login</code> | `str` | <code>login</code> |  |
| <code>graphql_id</code> | `str` | <code>node_id</code> |  |
| <code>type</code> | `str` | <code>type</code> | `user`, `organization`, or `bot`. |
| <code>found_using</code> | `str` |  | `graphql_node_id`, `graphql_login`, `graphql_mint_global_id`, or `rest_id`. See [Data sources](#data-sources) |
| <code>tasks</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>sessions</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>repositories</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>pull_requests</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>assigned_pull_requests</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>review_requested_pull_requests</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>merged_pull_requests</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>auto_merge_enabled_pull_requests</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>timeline_events</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;pull_request</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;event_index</code> | `int` |  |  |
| <code>assigned_timeline_events</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;pull_request</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;event_index</code> | `int` |  |  |
| <code>workflow_runs</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` | <code>id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>triggered_workflow_runs</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` | <code>id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
