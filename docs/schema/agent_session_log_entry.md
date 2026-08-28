# Agent Session Log Entry

Parquet table: `agent_session_logs`

Defined in [`agentlogs/schema/types/agent_session_log.py`](../../packages/risenlab-agentlogs/src/agentlogs/schema/types/agent_session_log.py#L9).

| Property | Type | GitHub field | Notes |
| --- | --- | --- | --- |
| <code>session</code> | `struct{}` |  |  |
| <code>session</code><br><code>.id</code> | `str` |  |  |
| <code>entry_index</code> | `int` |  |  |
| <code>parsed</code> | `bool` |  |  |
| <code>raw</code> | `str` (optional) |  | Not set when `parsed` is true |
| <code>data</code> | `struct{}` (optional) |  | Not set when `parsed` is false. Refer to `raw` instead |
| <code>data</code><br><code>.id</code> | `str` (optional) | <code>id</code> |  |
| <code>data</code><br><code>.agentId</code> | `str` (optional) | <code>agentId</code> |  |
| <code>data</code><br><code>.arguments</code> | `struct{}` (optional) | <code>arguments</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.canOfferSessionApproval</code> | `bool` (optional) | <code>arguments</code><br><code>.canOfferSessionApproval</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.command</code> | `str` (optional) | <code>arguments</code><br><code>.command</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.description</code> | `str` (optional) | <code>arguments</code><br><code>.description</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.diff</code> | `str` (optional) | <code>arguments</code><br><code>.diff</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.filePath</code> | `str` (optional) | <code>arguments</code><br><code>.filePath</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.kind</code> | `str` (optional) | <code>arguments</code><br><code>.kind</code> |  |
| <code>data</code><br><code>.arguments</code><br><code>.toolName</code> | `str` (optional) | <code>arguments</code><br><code>.toolName</code> |  |
| <code>data</code><br><code>.callId</code> | `str` (optional) | <code>callId</code> |  |
| <code>data</code><br><code>.choices</code> | `list[]` (optional) | <code>choices</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.content_filter_results</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.filtered</code> | `bool` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.severity</code> | `str` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.filtered</code> | `bool` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.severity</code> | `str` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.filtered</code> | `bool` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.severity</code> | `str` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.filtered</code> | `bool` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.severity</code> | `str` | <code>choices[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code> | `struct{}` | <code>choices[]</code><br><code>.delta</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.content</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.content</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations</code> | `list[]` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code> | `struct{}` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.citation_type</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.citation_type</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.ip_type</code> | `str` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.ip_type</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.license</code> | `str` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.license</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.snippet</code> | `str` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.snippet</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.url</code> | `str` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.citations</code><br><code>.url</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.end_offset</code> | `int` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.end_offset</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.id</code> | `int` | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.id</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.start_offset</code> | `int` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.IPCodeCitations[]</code><br><code>.start_offset</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.raw</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.copilot_annotations</code><br><code>.raw</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.encrypted_content</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.encrypted_content</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.padding</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.padding</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.phase</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.phase</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.reasoning_opaque</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.reasoning_opaque</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.reasoning_text</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.reasoning_text</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.role</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.role</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls</code> | `list[]` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.function_name</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.function_name</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.function_arguments</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.function_arguments</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.custom_name</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.custom_name</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.custom_input</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.custom_input</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.id</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.id</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.index</code> | `int` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.index</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.type</code> | `str` (optional) | <code>choices[]</code><br><code>.delta</code><br><code>.tool_calls[]</code><br><code>.type</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.finish_reason</code> | `str` (optional) | <code>choices[]</code><br><code>.finish_reason</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.index</code> | `int` (optional) | <code>choices[]</code><br><code>.index</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code> | `struct{}` (optional) | <code>choices[]</code><br><code>.message</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.content</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.content</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.role</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.role</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.tool_calls</code> | `list[]` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.tool_calls</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.function_name</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.function_name</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.function_arguments</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.function_arguments</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.id</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.id</code> |  |
| <code>data</code><br><code>.choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.type</code> | `str` (optional) | <code>choices[]</code><br><code>.message</code><br><code>.tool_calls[]</code><br><code>.type</code> |  |
| <code>data</code><br><code>.content</code> | `list[]` (optional) | <code>content</code> |  |
| <code>data</code><br><code>.content[]</code><br><code>.type</code> | `str` | <code>content[]</code><br><code>.type</code> |  |
| <code>data</code><br><code>.content[]</code><br><code>.text</code> | `str` (optional) | <code>content[]</code><br><code>.text</code> |  |
| <code>data</code><br><code>.content[]</code><br><code>.image_url</code> | `str` (optional) | <code>content[]</code><br><code>.image_url</code> |  |
| <code>data</code><br><code>.copilotBillingMetadata</code> | `struct{}` (optional) | <code>copilotBillingMetadata</code> |  |
| <code>data</code><br><code>.copilotBillingMetadata</code><br><code>.billable</code> | `bool` | <code>copilotBillingMetadata</code><br><code>.billable</code> |  |
| <code>data</code><br><code>.copilot_info_messages</code> | `list[]` (optional) | <code>copilot_info_messages</code> |  |
| <code>data</code><br><code>.copilot_info_messages[]</code><br><code>.code</code> | `str` | <code>copilot_info_messages[]</code><br><code>.code</code> |  |
| <code>data</code><br><code>.copilot_info_messages[]</code><br><code>.message</code> | `str` | <code>copilot_info_messages[]</code><br><code>.message</code> |  |
| <code>data</code><br><code>.copilot_model_warning_message</code> | `str` (optional) | <code>copilot_model_warning_message</code> |  |
| <code>data</code><br><code>.copilot_usage</code> | `struct{}` (optional) | <code>copilot_usage</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.token_details</code> | `list[]` | <code>copilot_usage</code><br><code>.token_details</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.batch_size</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.batch_size</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.cost_per_batch</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.cost_per_batch</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_count</code> | `int` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.token_count</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_type</code> | `str` | <code>copilot_usage</code><br><code>.token_details[]</code><br><code>.token_type</code> |  |
| <code>data</code><br><code>.copilot_usage</code><br><code>.total_nano_aiu</code> | `int` | <code>copilot_usage</code><br><code>.total_nano_aiu</code> |  |
| <code>data</code><br><code>.copilot_warning_messages</code> | `list[]` (optional) | <code>copilot_warning_messages</code> |  |
| <code>data</code><br><code>.copilot_warning_messages[]</code><br><code>.code</code> | `str` | <code>copilot_warning_messages[]</code><br><code>.code</code> |  |
| <code>data</code><br><code>.copilot_warning_messages[]</code><br><code>.message</code> | `str` | <code>copilot_warning_messages[]</code><br><code>.message</code> |  |
| <code>data</code><br><code>.created</code> | `datetime` (optional) | <code>created</code> |  |
| <code>data</code><br><code>.data</code> | `struct{}` (optional) | <code>data</code> |  |
| <code>data</code><br><code>.data</code><br><code>.actions</code> | `list[str]` (optional) | <code>data</code><br><code>.actions</code> |  |
| <code>data</code><br><code>.data</code><br><code>.alreadyInUse</code> | `bool` (optional) | <code>data</code><br><code>.alreadyInUse</code> |  |
| <code>data</code><br><code>.data</code><br><code>.approved</code> | `bool` (optional) | <code>data</code><br><code>.approved</code> |  |
| <code>data</code><br><code>.data</code><br><code>.autoApproveEdits</code> | `bool` (optional) | <code>data</code><br><code>.autoApproveEdits</code> |  |
| <code>data</code><br><code>.data</code><br><code>.eventCount</code> | `int` (optional) | <code>data</code><br><code>.eventCount</code> |  |
| <code>data</code><br><code>.data</code><br><code>.eventsFileSizeBytes</code> | `int` (optional) | <code>data</code><br><code>.eventsFileSizeBytes</code> |  |
| <code>data</code><br><code>.data</code><br><code>.feedback</code> | `str` (optional) | <code>data</code><br><code>.feedback</code> |  |
| <code>data</code><br><code>.data</code><br><code>.intent</code> | `str` (optional) | <code>data</code><br><code>.intent</code> |  |
| <code>data</code><br><code>.data</code><br><code>.newMode</code> | `str` (optional) | <code>data</code><br><code>.newMode</code> |  |
| <code>data</code><br><code>.data</code><br><code>.planContent</code> | `str` (optional) | <code>data</code><br><code>.planContent</code> |  |
| <code>data</code><br><code>.data</code><br><code>.previousMode</code> | `str` (optional) | <code>data</code><br><code>.previousMode</code> |  |
| <code>data</code><br><code>.data</code><br><code>.reason</code> | `str` (optional) | <code>data</code><br><code>.reason</code> |  |
| <code>data</code><br><code>.data</code><br><code>.reasoningEffort</code> | `str` (optional) | <code>data</code><br><code>.reasoningEffort</code> |  |
| <code>data</code><br><code>.data</code><br><code>.recommendedAction</code> | `str` (optional) | <code>data</code><br><code>.recommendedAction</code> |  |
| <code>data</code><br><code>.data</code><br><code>.remoteSteerable</code> | `bool` (optional) | <code>data</code><br><code>.remoteSteerable</code> |  |
| <code>data</code><br><code>.data</code><br><code>.requestId</code> | `str` (optional) | <code>data</code><br><code>.requestId</code> |  |
| <code>data</code><br><code>.data</code><br><code>.selectedAction</code> | `str` (optional) | <code>data</code><br><code>.selectedAction</code> |  |
| <code>data</code><br><code>.data</code><br><code>.selectedModel</code> | `str` (optional) | <code>data</code><br><code>.selectedModel</code> |  |
| <code>data</code><br><code>.data</code><br><code>.summary</code> | `str` (optional) | <code>data</code><br><code>.summary</code> |  |
| <code>data</code><br><code>.data</code><br><code>.toolCallId</code> | `str` (optional) | <code>data</code><br><code>.toolCallId</code> |  |
| <code>data</code><br><code>.data</code><br><code>.turnId</code> | `str` (optional) | <code>data</code><br><code>.turnId</code> |  |
| <code>data</code><br><code>.ephemeral</code> | `bool` (optional) | <code>ephemeral</code> |  |
| <code>data</code><br><code>.error</code> | `struct{}` (optional) | <code>error</code> |  |
| <code>data</code><br><code>.error</code><br><code>.code</code> | `str` | <code>error</code><br><code>.code</code> |  |
| <code>data</code><br><code>.error</code><br><code>.message</code> | `str` | <code>error</code><br><code>.message</code> |  |
| <code>data</code><br><code>.kind</code> | `str` (optional) | <code>kind</code> |  |
| <code>data</code><br><code>.model</code> | `str` (optional) | <code>model</code> |  |
| <code>data</code><br><code>.modelCall_error</code> | `str` (optional) | <code>modelCall</code><br><code>.error</code> |  |
| <code>data</code><br><code>.modelCallDurationMs</code> | `int` (optional) | <code>modelCallDurationMs</code> |  |
| <code>data</code><br><code>.object</code> | `str` (optional) | <code>object</code> |  |
| <code>data</code><br><code>.output</code> | `str` (optional) | <code>output</code> |  |
| <code>data</code><br><code>.parentId</code> | `str` (optional) | <code>parentId</code> |  |
| <code>data</code><br><code>.performedBy</code> | `str` (optional) | <code>performedBy</code> |  |
| <code>data</code><br><code>.prompt_filter_results</code> | `list[]` (optional) | <code>prompt_filter_results</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.prompt_index</code> | `int` | <code>prompt_filter_results[]</code><br><code>.prompt_index</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code> | `struct{}` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code> | `struct{}` (optional) | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.filtered</code> | `bool` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.severity</code> | `str` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.hate</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code> | `struct{}` (optional) | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.filtered</code> | `bool` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.severity</code> | `str` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.self_harm</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code> | `struct{}` (optional) | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.filtered</code> | `bool` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.severity</code> | `str` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.sexual</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code> | `struct{}` (optional) | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.filtered</code> | `bool` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.filtered</code> |  |
| <code>data</code><br><code>.prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.severity</code> | `str` | <code>prompt_filter_results[]</code><br><code>.content_filter_results</code><br><code>.violence</code><br><code>.severity</code> |  |
| <code>data</code><br><code>.role</code> | `str` (optional) | <code>role</code> |  |
| <code>data</code><br><code>.source</code> | `str` (optional) | <code>source</code> |  |
| <code>data</code><br><code>.system_fingerprint</code> | `str` (optional) | <code>system_fingerprint</code> |  |
| <code>data</code><br><code>.timestamp</code> | `str` (optional) | <code>timestamp</code> |  |
| <code>data</code><br><code>.toolCallId</code> | `str` (optional) | <code>toolCallId</code> |  |
| <code>data</code><br><code>.toolName</code> | `str` (optional) | <code>toolName</code> |  |
| <code>data</code><br><code>.tool_call_id</code> | `str` (optional) | <code>tool_call_id</code> |  |
| <code>data</code><br><code>.truncateResult</code> | `struct{}` (optional) | <code>truncateResult</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.messagesRemovedDuringTruncation</code> | `int` | <code>truncateResult</code><br><code>.messagesRemovedDuringTruncation</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.postTruncationMessagesLength</code> | `int` | <code>truncateResult</code><br><code>.postTruncationMessagesLength</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.postTruncationTokensInMessages</code> | `int` | <code>truncateResult</code><br><code>.postTruncationTokensInMessages</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.preTruncationMessagesLength</code> | `int` | <code>truncateResult</code><br><code>.preTruncationMessagesLength</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.preTruncationTokensInMessages</code> | `int` | <code>truncateResult</code><br><code>.preTruncationTokensInMessages</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.tokenLimit</code> | `int` | <code>truncateResult</code><br><code>.tokenLimit</code> |  |
| <code>data</code><br><code>.truncateResult</code><br><code>.tokensRemovedDuringTruncation</code> | `int` | <code>truncateResult</code><br><code>.tokensRemovedDuringTruncation</code> |  |
| <code>data</code><br><code>.turn</code> | `int` (optional) | <code>turn</code> |  |
| <code>data</code><br><code>.type</code> | `str` (optional) | <code>type</code> |  |
| <code>data</code><br><code>.usage</code> | `struct{}` (optional) | <code>usage</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.completion_tokens</code> | `int` | <code>usage</code><br><code>.completion_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.completion_tokens_details</code> | `struct{}` (optional) | <code>usage</code><br><code>.completion_tokens_details</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.completion_tokens_details</code><br><code>.accepted_prediction_tokens</code> | `int` (optional) | <code>usage</code><br><code>.completion_tokens_details</code><br><code>.accepted_prediction_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.completion_tokens_details</code><br><code>.reasoning_tokens</code> | `int` (optional) | <code>usage</code><br><code>.completion_tokens_details</code><br><code>.reasoning_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.completion_tokens_details</code><br><code>.rejected_prediction_tokens</code> | `int` (optional) | <code>usage</code><br><code>.completion_tokens_details</code><br><code>.rejected_prediction_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code> | `struct{}` (optional) | <code>usage</code><br><code>.copilot_usage</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.token_details</code> | `list[]` | <code>usage</code><br><code>.copilot_usage</code><br><code>.token_details</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.batch_size</code> | `int` | <code>usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.batch_size</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.cost_per_batch</code> | `int` | <code>usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.cost_per_batch</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_count</code> | `int` | <code>usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_count</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_type</code> | `str` | <code>usage</code><br><code>.copilot_usage</code><br><code>.token_details[]</code><br><code>.token_type</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.copilot_usage</code><br><code>.total_nano_aiu</code> | `int` | <code>usage</code><br><code>.copilot_usage</code><br><code>.total_nano_aiu</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens</code> | `int` | <code>usage</code><br><code>.prompt_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens_details</code> | `struct{}` (optional) | <code>usage</code><br><code>.prompt_tokens_details</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens_details</code><br><code>.cache_creation_tokens</code> | `int` (optional) | <code>usage</code><br><code>.prompt_tokens_details</code><br><code>.cache_creation_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens_details</code><br><code>.cached_tokens</code> | `int` | <code>usage</code><br><code>.prompt_tokens_details</code><br><code>.cached_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens_details</code><br><code>.input_tokens</code> | `int` (optional) | <code>usage</code><br><code>.prompt_tokens_details</code><br><code>.input_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.prompt_tokens_details</code><br><code>.output_tokens</code> | `int` (optional) | <code>usage</code><br><code>.prompt_tokens_details</code><br><code>.output_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.reasoning_tokens</code> | `int` (optional) | <code>usage</code><br><code>.reasoning_tokens</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.time_in_ms</code> | `int` (optional) | <code>usage</code><br><code>.time_in_ms</code> |  |
| <code>data</code><br><code>.usage</code><br><code>.total_tokens</code> | `int` | <code>usage</code><br><code>.total_tokens</code> |  |
