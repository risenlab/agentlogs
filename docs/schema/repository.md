# Repository

Parquet table: `repositories`

Defined in [`agentlogs/schema/types/repository.py`](../../packages/risenlab-agentlogs/src/agentlogs/schema/types/repository.py#L13).

| Property | Type | GitHub field |
| --- | --- | --- |
| <code>full_name</code> | `str` |  |
| <code>agent_tasks</code> | `list[]` | <code>tasks[]</code> |
| <code>agent_tasks[]</code><br><code>.id</code> | `str` | <code>tasks[]</code><br><code>.id</code> |
| <code>archived</code> | `bool` | <code>isArchived</code> |
| <code>disabled</code> | `bool` | <code>isDisabled</code> |
| <code>locked</code> | `bool` | <code>isLocked</code> |
| <code>fork</code> | `bool` | <code>isFork</code> |
| <code>homepage</code> | `str` (optional) | <code>homepageUrl</code> |
| <code>has_wiki</code> | `bool` | <code>hasWikiEnabled</code> |
| <code>license</code> | `str` (optional) | <code>licenseInfo</code><br><code>.name</code> |
| <code>main_language</code> | `str` |  |
| <code>default_branch</code> | `str` (optional) | <code>defaultBranchRef</code><br><code>.name</code> |
| <code>size</code> | `int` | <code>diskUsage</code> |
| <code>created_at</code> | `datetime` | <code>created_at</code> |
| <code>pushed_at</code> | `datetime` | <code>pushed_at</code> |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |
| <code>last_commit_at</code> | `datetime` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.committedDate</code> |
| <code>last_commit_SHA</code> | `str` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.oid</code> |
| <code>forks_count</code> | `int` | <code>forkCount</code> |
| <code>stargazers_count</code> | `int` | <code>stargazers</code><br><code>.totalCount</code> |
| <code>watchers_count</code> | `int` (optional) | <code>watchers</code><br><code>.totalCount</code> |
| <code>commits_count</code> | `int` (optional) | <code>defaultBranchRef</code><br><code>.target</code><br><code>.history</code><br><code>.totalCount</code> |
| <code>branches_count</code> | `int` (optional) | <code>refs</code><br><code>.totalCount</code> |
| <code>releases_count</code> | `int` (optional) | <code>releases</code><br><code>.totalCount</code> |
| <code>contributors_count</code> | `int` (optional) |  |
| <code>total_issues_count</code> | `int` (optional) | <code>issues</code><br><code>.totalCount</code> |
| <code>open_issues_count</code> | `int` (optional) | <code>issues(states: OPEN)</code><br><code>.totalCount</code> |
| <code>total_pull_requests_count</code> | `int` (optional) | <code>pullRequests</code><br><code>.totalCount</code> |
| <code>open_pull_requests_count</code> | `int` (optional) | <code>pullRequests(states: OPEN)</code><br><code>.totalCount</code> |
| <code>labels</code> | `list[str]` | <code>labels</code><br><code>.nodes[]</code><br><code>.name</code> |
| <code>topics</code> | `list[str]` | <code>repositoryTopics</code><br><code>.nodes[]</code><br><code>.topic</code><br><code>.name</code> |
| <code>languages</code> | `dict[str, int]` | <code>languages</code> |
| <code>blank_lines</code> | `int` (optional) |  |
| <code>code_lines</code> | `int` (optional) |  |
| <code>comment_lines</code> | `int` (optional) |  |
| <code>metrics</code> | `list[]` |  |
| <code>metrics[]</code><br><code>.language</code> | `str` |  |
| <code>metrics[]</code><br><code>.blank_lines</code> | `int` |  |
| <code>metrics[]</code><br><code>.code_lines</code> | `int` |  |
| <code>metrics[]</code><br><code>.comment_lines</code> | `int` |  |
