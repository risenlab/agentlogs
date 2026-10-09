# Agent Session Log Entry

> [!NOTE]
> This is the documentation for schema `v1.0`
>
> [Changelog](../../CHANGELOG.md#schema-v1_0)

<table>
<tr><th align="left">Description</th><td>Copilot cloud agent session log event.</td></tr>
<tr><th align="left">Parquet table</th><td><code>agent_session_logs</code></td></tr>
<tr><th align="left">Schema definition</th><td><a href="../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_session_log.py#L9"><code>agentlogs/schema/types/agent_session_log.py</code></a></td></tr>
</table>

## Data sources

- **Log**: Copilot API `GET https://api.githubcopilot.com/agents/sessions/{id}/logs` (no public documentation)

The response is a [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) stream (`Accept: text/event-stream`); each event's `data` field is one log entry.

## Relations

| Property | Related table | Related field | Description |
| --- | --- | --- | --- |
| <code>session</code> | [Agent Session](agent_session.md) |  | Each log entry points at its `session`; sessions do not list log entries (see [Agent Session](./agent_session.md)). |

## Fields

| Property | Type | GitHub field | Description |
| --- | --- | --- | --- |
| <code>session</code> | `struct{}` |  | See [Relations](#relations). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` | <code>id</code> |  |
| <code>entry_index</code> | `int` |  | Position of the log entry within the session log. |
| <code>parsed</code> | `bool` |  |  |
| <code>raw</code> | `str` (optional) |  | Not set when `parsed` is true |
| <code>data</code> | `struct{}` (optional) |  | Not set when `parsed` is false. Refer to `raw` instead |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` (optional) | <code>id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agentId</code> | `str` (optional) | <code>agentId</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;callId</code> | `str` (optional) | <code>callId</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;choices</code> | `list[]` (optional) | <code>choices</code> | See [`data.choices`](#data-choices). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;content</code> | `list[]` (optional) | <code>content</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` | <code>content[]</code><br><code>.type</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;text</code> | `str` (optional) | <code>content[]</code><br><code>.text</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;image_url</code> | `str` (optional) | <code>content[]</code><br><code>.image_url</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilotBillingMetadata</code> | `struct{}` (optional) | <code>copilotBillingMetadata</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;billable</code> | `bool` | <code>copilotBillingMetadata</code><br><code>.billable</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilot_info_messages</code> | `list[]` (optional) | <code>copilot_info_messages</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;code</code> | `str` | <code>copilot_info_messages[]</code><br><code>.code</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message</code> | `str` | <code>copilot_info_messages[]</code><br><code>.message</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilot_model_warning_message</code> | `str` (optional) | <code>copilot_model_warning_message</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilot_usage</code> | `struct{}` (optional) | <code>copilot_usage</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_details</code> | `list[]` | <code>copilot_usage</code><br><code>.token_details</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;batch_size</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.batch_size</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost_per_batch</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.cost_per_batch</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_count</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.token_count</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type</code> | `str` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.token_type</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total_nano_aiu</code> | `int` | <code>copilot_usage</code><br><code>.total_nano_aiu</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilot_warning_messages</code> | `list[]` (optional) | <code>copilot_warning_messages</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;code</code> | `str` | <code>copilot_warning_messages[]</code><br><code>.code</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message</code> | `str` | <code>copilot_warning_messages[]</code><br><code>.message</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;created</code> | `datetime` (optional) | <code>created</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;error</code> | `struct{}` (optional) | <code>error</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;code</code> | `str` | <code>error</code><br><code>.code</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message</code> | `str` | <code>error</code><br><code>.message</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;kind</code> | `str` (optional) | <code>kind</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;model</code> | `str` (optional) | <code>model</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;modelCall_error</code> | `str` (optional) | <code>modelCall</code><br><code>.error</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;modelCallDurationMs</code> | `int` (optional) | <code>modelCallDurationMs</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;object</code> | `str` (optional) | <code>object</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;performedBy</code> | `str` (optional) | <code>performedBy</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;prompt_filter_results</code> | `list[]` (optional) | <code>prompt_filter_results</code> | See [`data.prompt_filter_results`](#data-prompt_filter_results). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;role</code> | `str` (optional) | <code>role</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;source</code> | `str` (optional) | <code>source</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;system_fingerprint</code> | `str` (optional) | <code>system_fingerprint</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;tool_call_id</code> | `str` (optional) | <code>tool_call_id</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;toolTelemetry</code> | `struct{}` (optional) | <code>toolTelemetry</code> | See [`data.toolTelemetry`](#data-toolTelemetry). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;truncateResult</code> | `struct{}` (optional) | <code>truncateResult</code> | See [`data.truncateResult`](#data-truncateResult). |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;turn</code> | `int` (optional) | <code>turn</code> |  |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;usage</code> | `struct{}` (optional) | <code>usage</code> | See [`data.usage`](#data-usage). |

<a id="data-choices"></a>

### `data.choices`

| Property | Type |
| --- | --- |
| <code>content_filter_results</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;hate</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;self_harm</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sexual</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;violence</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>delta</code> | `struct{}` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;content</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;copilot_annotations</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IPCodeCitations</code> | `list[]` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;citations</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_type</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;license</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;snippet</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_offset</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_offset</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;citations</code> | `list[]` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;citations</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_type</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;license</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;snippet</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end_offset</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;start_offset</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;encrypted_content</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;padding</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;phase</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;reasoning_opaque</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;reasoning_text</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;role</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;tool_calls</code> | `list[]` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function_name</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function_arguments</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;custom_name</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;custom_input</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) |
| <code>finish_reason</code> | `str` (optional) |
| <code>index</code> | `int` (optional) |
| <code>message</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;content</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;role</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;tool_calls</code> | `list[]` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function_name</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;function_arguments</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</code> | `str` (optional) |

<a id="data-prompt_filter_results"></a>

### `data.prompt_filter_results`

| Property | Type |
| --- | --- |
| <code>prompt_index</code> | `int` |
| <code>content_filter_results</code> | `struct{}` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;hate</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;self_harm</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sexual</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;violence</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filtered</code> | `bool` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity</code> | `str` |

<a id="data-toolTelemetry"></a>

### `data.toolTelemetry`

| Property | Type |
| --- | --- |
| <code>event</code> | `str` (optional) |
| <code>metrics</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;callCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;cancelled_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;cloudRowsReturned</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_alertCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_duration_ms</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_languages_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_languages_skipped_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_total_alerts</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReview_alertCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReview_durationMs</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commandTimeout</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commentsExcluded</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commentsGenerated</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;compacted_saved_chars</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;completed_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;completedStatements</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;definitionCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;delivered_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;duration_seconds</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;elapsed_seconds</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;exit_code</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;failed_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;file_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;hasContent</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;idle_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;linesAdded</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;linesRemoved</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;localRowsReturned</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;mcp_result_content_bytes</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;mcp_structured_content_bytes</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;mcp_task_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;message_length</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;numberOfToolCallsMadeByAgent</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;originalContentLength</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;queue_depth</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;redirectCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;requested_recipient_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;resolved_recipient_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;response_length</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;responseTokenLimit</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;result_length</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;result_length_original</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;resultForLlmLength</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;resultLength</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;returnedContentLength</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;reviewedFiles</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;rowsAffected</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;rowsReturned</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;running_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;skillContentLength</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;skipped_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;startIndex</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;statementCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;symbolCount</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;timeout_seconds</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;total_turns</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;tracked_shutdown_count</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_budgetSeconds</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeQLDurationMs</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeReviewDurationMs</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_iteration</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_remainingBudgetMs</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_totalDurationMs</code> | `int` (optional) |
| <code>properties</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_id</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_name</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_name_hash</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_type</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;asyncOnlyShell</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;backend</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;character</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeBlocks</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReviewFileExtensions</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReviewModel</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReviewResult</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReviewTimedOut</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReview_engine</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReview_skipReason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_aborted</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_analysisRuleIds</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_languages</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_languagesAttempted</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_skipReason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_version</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;command</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;commentQueryNames</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;current_value</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;customTimeout</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;database</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;delivery_status</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;detached</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;error</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;execution_mode</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;executionMode</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;failedStatementType</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;file_hash</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;file_type</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;fileExtension</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;files_found</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;found</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;hashedUrl</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;inputs</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;is_timeout</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;language_server</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;languageId</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;languages</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;large_output</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputAvoided</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputHandled</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputJsonFormatted</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputOriginalSizeBytes</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputWrittenToFile</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;limit_type</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;limit_value</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;line</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;matches_found</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;mimeType</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;model</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;operation</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;options</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;output_mode</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;outputTruncated</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;prompt_length</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;queryType</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;raw</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;read_target_original_mode</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;read_target_state</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;readError</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;resolved_model</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;resolvedPathAgainstCwd</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;response_length</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sandboxApplied</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;sandboxOptOutRequested</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;scope</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;selection_kind</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;shell_error_category</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;shell_operation</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;shell_status</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;skillNameHash</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;skillSource</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;statementTypes</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;status</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;timed_out</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_alertCount</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_codeQL_durationMs</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_codeQL_isTrivial</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_disagreement</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_isTrivial</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_budgetResetEnabled</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeQL_skipReason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeQLEnabled</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeQLSuccess</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeQLTimedOut</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeReview_skipReason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeReviewEnabled</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeReviewSuccess</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_codeReviewTimedOut</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_consecutiveTimeouts</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_invalidInput</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_jobStarted</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_languages</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_retryGuidance</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_skipReason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_skipped</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;viewType</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;wasSyntaxError</code> | `str` (optional) |
| <code>restrictedProperties</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;addedPaths</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_id</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;agent_name</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;cloudError</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_error</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeql_stack</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;codeReviewError</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;deletedPaths</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;domParsingError</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;error</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;error_detail</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;errorMessage</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;file</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;filePaths</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;filesReviewed</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;finalUrl</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;large_output_file</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;largeOutputFilePath</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;path</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;pattern</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;pluginName</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;prTitle</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;query</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;shell_id</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;skillName</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_codeQL_reason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;trivialChange_reason</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;url</code> | `str` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;validation_error</code> | `str` (optional) |

<a id="data-truncateResult"></a>

### `data.truncateResult`

| Property | Type |
| --- | --- |
| <code>messagesRemovedDuringTruncation</code> | `int` |
| <code>postTruncationMessagesLength</code> | `int` |
| <code>postTruncationTokensInMessages</code> | `int` |
| <code>preTruncationMessagesLength</code> | `int` |
| <code>preTruncationTokensInMessages</code> | `int` |
| <code>tokenLimit</code> | `int` |
| <code>tokensRemovedDuringTruncation</code> | `int` |

<a id="data-usage"></a>

### `data.usage`

| Property | Type |
| --- | --- |
| <code>completion_tokens</code> | `int` |
| <code>completion_tokens_details</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;accepted_prediction_tokens</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;reasoning_tokens</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;rejected_prediction_tokens</code> | `int` (optional) |
| <code>copilot_usage</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;token_details</code> | `list[]` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;batch_size</code> | `int` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost_per_batch</code> | `int` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_count</code> | `int` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;token_type</code> | `str` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;total_nano_aiu</code> | `int` |
| <code>prompt_tokens</code> | `int` |
| <code>prompt_tokens_details</code> | `struct{}` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;cache_creation_tokens</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;cached_tokens</code> | `int` |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;input_tokens</code> | `int` (optional) |
| <code>&nbsp;&nbsp;&nbsp;&nbsp;output_tokens</code> | `int` (optional) |
| <code>reasoning_tokens</code> | `int` (optional) |
| <code>time_in_ms</code> | `int` (optional) |
| <code>total_tokens</code> | `int` |
