# Pull Request

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>GitHub pull request collected from a task or session.</td></tr>
<tr><th align="left">Parquet table</th><td><code>pull_requests</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/pull_request.py#L74"><code>agentlogs/schema/types/pull_request.py</code></a></td></tr>
</table>

## Data sources

- Pull request (see [`found_using`](#fields)):
    - `graphql_global_id`: GitHub GraphQL `node(id:)` ([documentation](https://docs.github.com/en/graphql/reference/queries#node))
    - `graphql_number_repo`: GitHub GraphQL `repository.pullRequest(number:)` ([documentation](https://docs.github.com/en/graphql/reference/objects#repository))
    - `graphql_mint_global_id`: GitHub GraphQL `node(id:)` with a minted `global_id` from the base64-encoded `011:PullRequest{id}` ([documentation](https://docs.github.com/en/graphql/reference/queries#node))
    - `rest_number_repo`: GitHub REST `GET /repos/{owner}/{repo}/pulls/{pull_number}` ([documentation](https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request))

Only successful GitHub API responses are stored. Other tables may contain references to this table with no matching row.

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>repository</code> | [Repository](repository.md) |  |  |
| <code>created_by_tasks</code> (list) | [Agent Task](agent_task.md) | <code>pull_request_artifacts</code> | Tasks that created this pull request as an artifact (see [Agent Task](./agent_task.md) `pull_request_artifacts`). |
| <code>created_by_sessions</code> (list) | [Agent Session](agent_session.md) | <code>pull_request_artifact</code> | Sessions that created this pull request (see [Agent Session](./agent_session.md) `pull_request_artifact`). |
| <code>user</code> (optional) | [User](user.md) | <code>pull_requests</code> |  |
| <code>assignees</code> (list) | [User](user.md) | <code>assigned_pull_requests</code> |  |
| <code>requested_reviewers</code> (list) | [User](user.md) | <code>review_requested_pull_requests</code> | Users only. Review requests to teams are not collected: GitHub GraphQL `Team` fields on review requests require org scopes this collection does not use. Only the first 20 are fetched. |
| <code>merged_by</code> (optional) | [User](user.md) | <code>merged_pull_requests</code> |  |
| <code>auto_merge.enabled_by</code> (optional) | [User](user.md) | <code>auto_merge_enabled_pull_requests</code> |  |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>id</code> | `int` (optional) | <code>id</code> |  |
| <code>graphql_id</code> | `str` | <code>node_id</code> |  |
| <code>number</code> | `int` | <code>number</code> |  |
| <code>found_using</code> | `str` |  | `graphql_global_id`, `graphql_number_repo`, `graphql_mint_global_id`, or `rest_number_repo`. See [Data sources](#data-sources) |
| <code>timeline_found</code> | `bool` |  |  |
| <code>repository</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;full_name</code> | `str` |  |  |
| <code>created_by_tasks</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>created_by_sessions</code> | `list[]` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>user</code> | `struct{}` (optional) | <code>user</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>user</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>user</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>user</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>user</code><br><code>.type</code> |  |
| <code>assignees</code> | `list[]` | <code>assignees</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>assignees[]</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>assignees[]</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>assignees[]</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>assignees[]</code><br><code>.type</code> |  |
| <code>requested_reviewers</code> | `list[]` | <code>requested_reviewers</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>requested_reviewers[]</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>requested_reviewers[]</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>requested_reviewers[]</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>requested_reviewers[]</code><br><code>.type</code> |  |
| <code>merged_by</code> | `struct{}` (optional) | <code>merged_by</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>merged_by</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>merged_by</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>merged_by</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>merged_by</code><br><code>.type</code> |  |
| <code>title</code> | `str` | <code>title</code> |  |
| <code>body</code> | `str` (optional) | <code>body</code> |  |
| <code>state</code> | `str` | <code>state</code> |  |
| <code>locked</code> | `bool` | <code>locked</code> |  |
| <code>draft</code> | `bool` | <code>draft</code> |  |
| <code>labels</code> | `list[str]` | <code>labels[]</code><br><code>.name</code> | Only the first 20 are fetched. |
| <code>active_lock_reason</code> | `str` (optional) | <code>active_lock_reason</code> |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>closed_at</code> | `datetime` (optional) | <code>closed_at</code> |  |
| <code>merged_at</code> | `datetime` (optional) | <code>merged_at</code> |  |
| <code>head</code> | `struct{}` | <code>head</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>head</code><br><code>.ref</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sha</code> | `str` | <code>head</code><br><code>.sha</code> |  |
| <code>base</code> | `struct{}` | <code>base</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;ref</code> | `str` | <code>base</code><br><code>.ref</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sha</code> | `str` | <code>base</code><br><code>.sha</code> |  |
| <code>author_association</code> | `str` | <code>author_association</code> |  |
| <code>auto_merge</code> | `struct{}` (optional) |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;enabled_by</code> | `struct{}` (optional) | <code>enabled_by</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>enabled_by</code><br><code>.id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>enabled_by</code><br><code>.login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>enabled_by</code><br><code>.node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>enabled_by</code><br><code>.type</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;merge_method</code> | `str` | <code>merge_method</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commit_title</code> | `str` (optional) | <code>commit_title</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commit_message</code> | `str` (optional) | <code>commit_message</code> |  |
| <code>merged</code> | `bool` | <code>merged</code> |  |
| <code>mergeable</code> | `bool` (optional) | <code>mergeable</code> |  |
| <code>mergeable_state</code> | `str` | <code>mergeable_state</code> |  |
| <code>maintainer_can_modify</code> | `bool` | <code>maintainer_can_modify</code> |  |
| <code>additions_count</code> | `int` | <code>additions</code> |  |
| <code>deletions_count</code> | `int` | <code>deletions</code> |  |
| <code>changed_files_count</code> | `int` | <code>changed_files</code> |  |
