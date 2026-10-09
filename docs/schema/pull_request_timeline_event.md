# Pull Request Timeline Event

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>One event from a collected pull request timeline.</td></tr>
<tr><th align="left">Parquet table</th><td><code>pull_request_timelines</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/pull_request.py#L32"><code>agentlogs/schema/types/pull_request.py</code></a></td></tr>
</table>

## Data sources

- **Pull request timeline**: GitHub REST `GET /repos/{owner}/{repo}/issues/{issue_number}/timeline` ([documentation](https://docs.github.com/en/rest/issues/timeline#list-timeline-events-for-an-issue))

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>pull_request</code> | [Pull Request](pull_request.md) |  | Each timeline event points at its pull request; pull requests do not list timeline events (see [Pull Request](./pull_request.md)). |
| <code>actor</code> (optional) | [User](user.md) | <code>timeline_events</code> |  |
| <code>assignee</code> (optional) | [User](user.md) | <code>assigned_timeline_events</code> |  |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>pull_request</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>resource_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>resource_global_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;number</code> | `int` (optional) | <code>resource_number</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;repository</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>event_index</code> | `int` |  | Position of the event within the pull request timeline. |
| <code>event</code> | `str` | <code>event</code> |  |
| <code>created_at</code> | `datetime` (optional) | <code>created_at</code> \| <code>submitted_at</code> \| <code>author</code><br><code>.date</code> |  |
| <code>actor</code> | `struct{}` (optional) | <code>actor</code> \| <code>user</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>actor</code><br><code>.id</code> \| <code>user</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>actor</code><br><code>.login</code> \| <code>user</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>actor</code><br><code>.node_id</code> \| <code>user</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>actor</code><br><code>.type</code> \| <code>user</code><br><code>.type</code> |  |
| <code>assignee</code> | `struct{}` (optional) | <code>assignee</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>assignee</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>assignee</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>assignee</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>assignee</code><br><code>.type</code> |  |
| <code>label</code> | `str` (optional) | <code>label</code><br><code>.name</code> |  |
| <code>commit_id</code> | `str` (optional) | <code>commit_id</code> \| <code>sha</code> |  |
| <code>message</code> | `str` (optional) | <code>message</code> |  |
