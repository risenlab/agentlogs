# Changelog

- [v1.0.0](#v1_0_0)
    - [schema v1.0](#schema-v1_0)
- [v0.2.0](#v0_2_0)
    - [schema v0.2](#schema-v0_2)

<a id="v1_0_0"></a>

## [v1.0.0](https://github.com/risenlab/agentlogs/tree/v1.0.0)

- Additional resources collected:
    - Agent task and session pull request artifacts (`pull_requests`) and their timelines (`pull_request_timelines`).
    - Agent session workflow runs (`workflow_runs`).
- Updated schema reference for schema `v1.0`, including `pull_requests`, `pull_request_timelines` and `workflow_runs`.
- Added data source and relation tables to schema documentation.
- Added more field descriptions in schema documentation.
- Changed versioning, separating the schema carried inside the package (e.g. schema `v1.0` in package `v1.0.0`) from the dataset release (e.g. `1.0-12345678`). A later package patch still carries that schema, so dataset `1.0-12345678` can be used with package `v1.0.1`.
- Added a changelog.

<a id="schema-v1_0"></a>

### schema v1.0

- Added tables: `pull_requests`, `pull_request_timelines`, and `workflow_runs`.
- `repositories`:
    - Added `owner`, a relation to the `users` table.
    - Change `languages` to `{language, bytes}[]` instead of the mapping `{language -> bytes}`.
- `agent_tasks`:
    - This table now only contains found tasks. References to this table may not have a corresponding row if the task could not be found.
    - Removed `found`.
    - Removed the wrapper field `data`. Moved all fields under `data` directly under the table.
    - Removed `collaborators`. It was a partial list of the users on the task's sessions.
    - Changed `sessions` to `{id, session_index}` instead of `{id}`.
    - Split `artifacts`:
        - `pull_request_artifacts` (a list of `{id, graphql_id, number, repository}`, relations to the `pull_requests` table).
        - `branch_artifacts` (a list of `{base: {ref}, head: {ref}}`).
    - Added `automation_id`.
    - Made `creator` required, adding `graphql_id` and `type` and making `id` or `login` optional.
- `agent_sessions`:
    - Added `session_index` and `reasoning_effort`.
    - Changed `user`, adding `graphql_id` and `type` and making `id` or `login` optional.
    - Changed `branch` to `{base: {ref}, head: {ref}}`.
    - Changed `pull_request` to `pull_request_artifact` (`{id, graphql_id, number, repository}`), a relation to the `pull_requests` table. Renamed `global_id` to `graphql_id`, removed `state` is gone, and added `repository`.
    - Changed `workflow_run_id` to `workflow_run` (`{id, repository}`), a relation to the `workflow_runs` table.
- `users`:
    - This table now only contains found users. References to this table may not have a corresponding row if the user could not be found.
    - Removed `found` and `collaborated_tasks`.
    - Made `login` and `found_using` required. Changed `found_using` values to `graphql_node_id`, `graphql_login`, `graphql_mint_global_id`, or `rest_id` instead of `'id'` or `'login'`.
    - Renamed `created_tasks` to `tasks`.
    - Added `graphql_id`, `type`, `created_at`, and `repositories`.
    - Added `pull_requests`, `assigned_pull_requests`, `review_requested_pull_requests`, `merged_pull_requests`, and `auto_merge_enabled_pull_requests`, relations to the `pull_requests` table.
    - Added `timeline_events` and `assigned_timeline_events`, relations to the `pull_request_timelines` table.
    - Added `workflow_runs` and `triggered_workflow_runs`, relations to the `workflow_runs` table.
- `agent_session_logs`:
    - Removed `data.data`, `data.ephemeral` and `data.parentId`.
    - Added `data.toolTelemetry` and `copilot_annotations.citations`.
    - Made `ip_type`, `license`, `snippet`, `url`, `citations`, `end_offset`, and `id` optional on  `copilot_annotations.IPCodeCitations`.
- Removed `cast_record`. Cast parquet rows with `typing.cast`.

<a id="v0_2_0"></a>

## [v0.2.0](https://github.com/risenlab/agentlogs/tree/v0.2)

Initial release:
- Added schema package
- Added documentation
- Added dnalysis examples
- Added dataset sample

<a id="schema-v0_2"></a>

### schema v0.2

Initial release: 
- Added tables: `repositories`, `agent_tasks`, `agent_sessions`, `agent_session_logs`, and `users`.
