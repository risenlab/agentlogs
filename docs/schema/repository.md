# Repository

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>GitHub repository.</td></tr>
<tr><th align="left">Parquet table</th><td><code>repositories</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/repository.py#L17"><code>agentlogs/schema/types/repository.py</code></a></td></tr>
</table>

## Data sources

- **Repository**: SEART GHS CSV export ([seart-ghs.si.usi.ch](https://seart-ghs.si.usi.ch), [seart-group/ghs](https://github.com/seart-group/ghs))

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>agent_tasks</code> (list) | [Agent Task](agent_task.md) | <code>repository</code> |  |
| <code>owner</code> | [User](user.md) | <code>repositories</code> | Login is the first segment of `full_name`. |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>full_name</code> | `str` |  |  |
| <code>agent_tasks</code> | `list[]` | <code>tasks[]</code> | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>tasks[]</code><br><code>.id</code> |  |
| <code>owner</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) | <code>id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;login</code> | `str` (optional) | <code>login</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;graphql_id</code> | `str` (optional) | <code>node_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) | <code>type</code> |  |
| <code>archived</code> | `bool` | <code>isArchived</code> |  |
| <code>disabled</code> | `bool` | <code>isDisabled</code> |  |
| <code>locked</code> | `bool` | <code>isLocked</code> |  |
| <code>fork</code> | `bool` | <code>isFork</code> |  |
| <code>homepage</code> | `str` (optional) | <code>homepageUrl</code> |  |
| <code>has_wiki</code> | `bool` | <code>hasWikiEnabled</code> |  |
| <code>license</code> | `str` (optional) | <code>licenseInfo</code><br><code>.name</code> |  |
| <code>main_language</code> | `str` |  |  |
| <code>default_branch</code> | `str` (optional) | <code>defaultBranchRef</code><br><code>.name</code> |  |
| <code>size</code> | `int` | <code>diskUsage</code> |  |
| <code>created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>pushed_at</code> | `datetime` | <code>pushed_at</code> |  |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>last_commit_at</code> | `datetime` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.committedDate</code> |  |
| <code>last_commit_SHA</code> | `str` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.oid</code> |  |
| <code>forks_count</code> | `int` | <code>forkCount</code> |  |
| <code>stargazers_count</code> | `int` | <code>stargazers</code><br><code>.totalCount</code> |  |
| <code>watchers_count</code> | `int` (optional) | <code>watchers</code><br><code>.totalCount</code> |  |
| <code>commits_count</code> | `int` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.history</code><br><code>.totalCount</code> |  |
| <code>branches_count</code> | `int` (optional) | <code>refs</code><br><code>.totalCount</code> |  |
| <code>releases_count</code> | `int` (optional) | <code>releases</code><br><code>.totalCount</code> |  |
| <code>contributors_count</code> | `int` (optional) |  |  |
| <code>total_issues_count</code> | `int` (optional) | <code>issues</code><br><code>.totalCount</code> |  |
| <code>open_issues_count</code> | `int` (optional) | <code>issues(states: OPEN)</code><br><code>.totalCount</code> |  |
| <code>total_pull_requests_count</code> | `int` (optional) | <code>pullRequests</code><br><code>.totalCount</code> |  |
| <code>open_pull_requests_count</code> | `int` (optional) | <code>pullRequests(states: OPEN)</code><br><code>.totalCount</code> |  |
| <code>labels</code> | `list[str]` | <code>labels</code><br><code>.nodes[]</code><br><code>.name</code> |  |
| <code>topics</code> | `list[str]` | <code>repositoryTopics</code><br><code>.nodes[]</code><br><code>.topic</code><br><code>.name</code> |  |
| <code>languages</code> | `list[]` |  | Number of bytes of code in each language ([GitHub REST API documentation](https://docs.github.com/en/rest/repos/repos#list-repository-languages)). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;language</code> | `str` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;bytes</code> | `int` |  |  |
| <code>blank_lines</code> | `int` (optional) |  | Total blank lines ([cloc](https://github.com/AlDanial/cloc)). |
| <code>code_lines</code> | `int` (optional) |  | Total code lines ([cloc](https://github.com/AlDanial/cloc)). |
| <code>comment_lines</code> | `int` (optional) |  | Total comment lines ([cloc](https://github.com/AlDanial/cloc)). |
| <code>metrics</code> | `list[]` |  | Line counts in each language ([cloc](https://github.com/AlDanial/cloc)). Language names do not match the `languages` field. |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;language</code> | `str` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;blank_lines</code> | `int` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;code_lines</code> | `int` |  |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;comment_lines</code> | `int` |  |  |
