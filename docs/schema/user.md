# User

Parquet table: `users`

Defined in [`agentlogs/schema/types/user.py`](../../packages/risenlab-agentlogs/src/agentlogs/schema/types/user.py#L6).

| Property | Type | GitHub field | Notes |
| --- | --- | --- | --- |
| <code>id</code> | `int` |  |  |
| <code>found</code> | `bool` |  |  |
| <code>found_using</code> | `str` (optional) |  | `'id' \| 'login'`. Not set when `found` is false |
| <code>login</code> | `str` (optional) |  | Not set when `found` is false |
| <code>created_tasks</code> | `list[]` |  |  |
| <code>created_tasks[]</code><br><code>.id</code> | `str` |  |  |
| <code>collaborated_tasks</code> | `list[]` |  | Taken from GitHub's API and may not be complete. Use together with created_tasks and sessions. |
| <code>collaborated_tasks[]</code><br><code>.id</code> | `str` |  |  |
| <code>sessions</code> | `list[]` |  |  |
| <code>sessions[]</code><br><code>.id</code> | `str` |  |  |
