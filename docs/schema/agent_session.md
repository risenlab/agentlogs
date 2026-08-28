# Agent Session

Parquet table: `agent_sessions`

Defined in [`agentlogs/schema/types/agent_session.py`](../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_session.py#L23).

| Property | Type | GitHub field |
| --- | --- | --- |
| <code>id</code> | `str` | <code>id</code> |
| <code>task</code> | `struct{}` |  |
| <code>task</code><br><code>.id</code> | `str` |  |
| <code>log_found</code> | `bool` |  |
| <code>user</code> | `struct{}` | <code>user</code> |
| <code>user</code><br><code>.id</code> | `int` | <code>user</code><br><code>.id</code> |
| <code>user</code><br><code>.login</code> | `str` (optional) | <code>user</code><br><code>.login</code> |
| <code>name</code> | `str` | <code>name</code> |
| <code>model</code> | `str` (optional) | <code>model</code> |
| <code>prompt</code> | `str` (optional) | <code>prompt</code> |
| <code>state</code> | `str` | <code>state</code> |
| <code>usage</code> | `struct{}` (optional) | <code>usage</code> |
| <code>usage</code><br><code>.type</code> | `str` | <code>usage</code><br><code>.type</code> |
| <code>usage</code><br><code>.amount</code> | `float` (optional) | <code>usage</code><br><code>.amount</code> |
| <code>usage</code><br><code>.credits</code> | `float` (optional) | <code>usage</code><br><code>.credits</code> |
| <code>premium_requests</code> | `float` | <code>premium_requests</code> |
| <code>error</code> | `str` (optional) | <code>error</code><br><code>.message</code> |
| <code>remote_steerable</code> | `bool` (optional) | <code>remote_steerable</code> |
| <code>workflow_run_id</code> | `int` (optional) | <code>workflow_run_id</code> |
| <code>event</code> | `struct{}` |  |
| <code>event</code><br><code>.type</code> | `str` (optional) | <code>event_type</code> |
| <code>event</code><br><code>.url</code> | `str` (optional) | <code>event_url</code> |
| <code>event</code><br><code>.ids</code> | `list[str]` (optional) | <code>event_identifiers</code> |
| <code>event</code><br><code>.content</code> | `str` (optional) | <code>event_content</code> |
| <code>pull_request</code> | `struct{}` (optional) |  |
| <code>pull_request</code><br><code>.id</code> | `int` (optional) | <code>resource_id</code> |
| <code>pull_request</code><br><code>.global_id</code> | `str` (optional) | <code>resource_global_id</code> |
| <code>pull_request</code><br><code>.number</code> | `int` (optional) | <code>resource_number</code> |
| <code>pull_request</code><br><code>.state</code> | `str` (optional) | <code>resource_state</code> |
| <code>branch</code> | `struct{}` (optional) |  |
| <code>branch</code><br><code>.base_ref</code> | `str` | <code>base_ref</code> |
| <code>branch</code><br><code>.head_ref</code> | `str` (optional) | <code>head_ref</code> |
| <code>created_at</code> | `datetime` | <code>created_at</code> |
| <code>updated_at</code> | `datetime` | <code>updated_at</code> |
| <code>completed_at</code> | `datetime` (optional) | <code>completed_at</code> |
