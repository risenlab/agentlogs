# Agent Task

Parquet table: `agent_tasks`

Defined in [`agentlogs/schema/types/agent_task.py`](../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_task.py#L39).

| Property | Type | GitHub field | Notes |
| --- | --- | --- | --- |
| <code>id</code> | `str` | <code>id</code> |  |
| <code>repository</code> | `struct{}` |  |  |
| <code>repository</code><br><code>.full_name</code> | `str` |  |  |
| <code>sessions</code> | `list[]` | <code>sessions[]</code> |  |
| <code>sessions[]</code><br><code>.id</code> | `str` | <code>sessions[]</code><br><code>.id</code> |  |
| <code>creator</code> | `struct{}` (optional) | <code>creator</code> | Not set when `found` is false |
| <code>creator</code><br><code>.id</code> | `int` | <code>creator</code><br><code>.id</code> |  |
| <code>creator</code><br><code>.login</code> | `str` (optional) | <code>creator</code><br><code>.login</code> |  |
| <code>collaborators</code> | `list[]` (optional) | <code>user_collaborators[]</code> | Not set when `found` is false |
| <code>collaborators[]</code><br><code>.id</code> | `int` | <code>user_collaborators[]</code> |  |
| <code>collaborators[]</code><br><code>.login</code> | `str` (optional) |  |  |
| <code>found</code> | `bool` |  |  |
| <code>data</code> | `struct{}` (optional) |  | Not set when `found` is false |
| <code>data</code><br><code>.name</code> | `str` (optional) | <code>name</code> |  |
| <code>data</code><br><code>.state</code> | `str` | <code>state</code> |  |
| <code>data</code><br><code>.archived</code> | `bool` |  |  |
| <code>data</code><br><code>.remote_steerable</code> | `bool` | <code>remote_steerable</code> |  |
| <code>data</code><br><code>.sharing_status</code> | `str` | <code>sharing_status</code> |  |
| <code>data</code><br><code>.created_at</code> | `datetime` | <code>created_at</code> |  |
| <code>data</code><br><code>.updated_at</code> | `datetime` | <code>updated_at</code> |  |
| <code>data</code><br><code>.archived_at</code> | `datetime` (optional) | <code>archived_at</code> |  |
| <code>data</code><br><code>.custom_agent</code> | `struct{}` (optional) | <code>custom_agent</code> |  |
| <code>data</code><br><code>.custom_agent</code><br><code>.id</code> | `str` (optional) | <code>custom_agent</code><br><code>.id</code> |  |
| <code>data</code><br><code>.custom_agent</code><br><code>.name</code> | `str` (optional) | <code>custom_agent</code><br><code>.name</code> |  |
| <code>data</code><br><code>.custom_agent</code><br><code>.is_automation</code> | `bool` (optional) | <code>custom_agent</code><br><code>.is_automation</code> |  |
| <code>data</code><br><code>.agent_collaborators</code> | `list[]` | <code>agent_collaborators[]</code> |  |
| <code>data</code><br><code>.agent_collaborators[]</code><br><code>.id</code> | `int` | <code>agent_collaborators[]</code><br><code>.agent_id</code> |  |
| <code>data</code><br><code>.agent_collaborators[]</code><br><code>.slug</code> | `str` | <code>agent_collaborators[]</code><br><code>.slug</code> |  |
| <code>data</code><br><code>.agent_collaborators[]</code><br><code>.task_id</code> | `str` (optional) | <code>agent_collaborators[]</code><br><code>.agent_task_id</code> |  |
| <code>data</code><br><code>.agent_collaborators[]</code><br><code>.type</code> | `str` (optional) | <code>agent_collaborators[]</code><br><code>.agent_type</code> |  |
| <code>data</code><br><code>.artifacts</code> | `list[]` | <code>artifacts[]</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.type</code> | `str` |  |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.pull_request</code> | `struct{}` (optional) | <code>artifacts[]</code><br><code>.data</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.pull_request</code><br><code>.id</code> | `int` (optional) | <code>artifacts[]</code><br><code>.data</code><br><code>.id</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.pull_request</code><br><code>.global_id</code> | `str` (optional) | <code>artifacts[]</code><br><code>.data</code><br><code>.global_id</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.branch</code> | `struct{}` (optional) | <code>artifacts[]</code><br><code>.data</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.branch</code><br><code>.base_ref</code> | `str` | <code>artifacts[]</code><br><code>.data</code><br><code>.base_ref</code> |  |
| <code>data</code><br><code>.artifacts[]</code><br><code>.branch</code><br><code>.head_ref</code> | `str` (optional) | <code>artifacts[]</code><br><code>.data</code><br><code>.head_ref</code> |  |
