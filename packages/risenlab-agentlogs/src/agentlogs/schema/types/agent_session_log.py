from __future__ import annotations

import datetime as dt
from typing import Annotated, TypedDict

from .annotation import Description, GitHubField, Relation, Source, Table
from .references import AgentSessionReference

@Table(
    name="agent_session_logs",
    sources=[
        Source(
            name="Log",
            text="Copilot API `GET https://api.githubcopilot.com/agents/sessions/{id}/logs` (no public documentation)",
        ),
    ],
    explanation="The response is a [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) stream (`Accept: text/event-stream`); each event's `data` field is one log entry.",
)
class AgentSessionLogEntry(TypedDict):
    """Copilot cloud agent session log event."""

    session: Annotated[
        AgentSessionReference,
        Relation(),
        Description(
            "Each log entry points at its `session`; sessions do not list log entries (see [Agent Session](./agent_session.md))."
        ),
    ]
    entry_index: Annotated[
        int,
        Description("Position of the log entry within the session log."),
    ]

    parsed: bool

    raw: Annotated[
        str | None,
        Description("Not set when `parsed` is true"),
    ]
    data: Annotated[
        AgentSessionLogEntryData | None,
        GitHubField(""),
        Description("Not set when `parsed` is false. Refer to `raw` instead"),
    ]

class AgentSessionLogEntryData(TypedDict):
    id: Annotated[str | None, GitHubField("id")]
    agentId: Annotated[str | None, GitHubField("agentId")]
    callId: Annotated[str | None, GitHubField("callId")]
    choices: list[Choice] | None
    content: list[ContentPart] | None
    copilotBillingMetadata: CopilotBillingMetadata | None
    copilot_info_messages: Annotated[list[CopilotInfoMessage] | None, GitHubField("copilot_info_messages")]
    copilot_model_warning_message: Annotated[str | None, GitHubField("copilot_model_warning_message")]
    copilot_usage: CopilotUsage | None
    copilot_warning_messages: Annotated[list[CopilotWarningMessage] | None, GitHubField("copilot_warning_messages")]
    created: Annotated[dt.datetime | None, GitHubField("created")]
    error: ErrorInfo | None
    kind: Annotated[str | None, GitHubField("kind")]
    model: Annotated[str | None, GitHubField("model")]
    modelCall_error: Annotated[str | None, GitHubField("modelCall.error")]
    modelCallDurationMs: Annotated[int | None, GitHubField("modelCallDurationMs")]
    object: Annotated[str | None, GitHubField("object")]
    performedBy: Annotated[str | None, GitHubField("performedBy")]
    prompt_filter_results: list[PromptFilterResult] | None
    role: Annotated[str | None, GitHubField("role")]
    source: Annotated[str | None, GitHubField("source")]
    system_fingerprint: Annotated[str | None, GitHubField("system_fingerprint")]
    tool_call_id: Annotated[str | None, GitHubField("tool_call_id")]
    toolTelemetry: ToolTelemetry | None
    truncateResult: TruncateResult | None
    turn: Annotated[int | None, GitHubField("turn")]
    usage: Usage | None

class ContentFilterCategory(TypedDict):
    filtered: bool
    severity: str

class ContentFilterResults(TypedDict):
    hate: ContentFilterCategory | None
    self_harm: ContentFilterCategory | None
    sexual: ContentFilterCategory | None
    violence: ContentFilterCategory | None

class PromptFilterResult(TypedDict):
    prompt_index: int
    content_filter_results: ContentFilterResults

class Citation(TypedDict):
    ip_type: str | None
    license: str | None
    snippet: str | None
    url: str | None

class CitationEntry(TypedDict):
    citations: Citation | None
    end_offset: int | None
    id: int | None
    start_offset: int | None

class CopilotAnnotations(TypedDict):
    IPCodeCitations: list[CitationEntry] | None
    citations: list[CitationEntry] | None
    raw: str | None

class DeltaToolCall(TypedDict):
    function_name: str | None
    function_arguments: str | None
    custom_name: str | None
    custom_input: str | None
    id: str | None
    index: int | None
    type: str | None

class MessageToolCall(TypedDict):
    function_name: str | None
    function_arguments: str | None
    id: str | None
    type: str | None

class Delta(TypedDict):
    content: str | None
    copilot_annotations: CopilotAnnotations | None
    encrypted_content: str | None
    padding: str | None
    phase: str | None
    reasoning_opaque: str | None
    reasoning_text: str | None
    role: str | None
    tool_calls: list[DeltaToolCall] | None

class Message(TypedDict):
    content: str | None
    role: str | None
    tool_calls: list[MessageToolCall] | None

class Choice(TypedDict):
    content_filter_results: ContentFilterResults | None
    delta: Delta
    finish_reason: str | None
    index: int | None
    message: Message | None


class ContentPart(TypedDict):
    type: str
    text: str | None
    image_url: str | None

class CopilotBillingMetadata(TypedDict):
    billable: bool

class CopilotInfoMessage(TypedDict):
    code: Annotated[str, GitHubField("code")]
    message: Annotated[str, GitHubField("message")]

class CopilotWarningMessage(TypedDict):
    code: Annotated[str, GitHubField("code")]
    message: Annotated[str, GitHubField("message")]

class TokenDetail(TypedDict):
    batch_size: int
    cost_per_batch: int
    token_count: int
    token_type: str

class CopilotUsage(TypedDict):
    token_details: list[TokenDetail]
    total_nano_aiu: int

class ErrorInfo(TypedDict):
    code: str
    message: str

class CompletionTokensDetails(TypedDict):
    accepted_prediction_tokens: int | None
    reasoning_tokens: int | None
    rejected_prediction_tokens: int | None

class PromptTokensDetails(TypedDict):
    cache_creation_tokens: int | None
    cached_tokens: int
    input_tokens: int | None
    output_tokens: int | None

class UsageCopilotUsage(TypedDict):
    token_details: list[TokenDetail]
    total_nano_aiu: int

class Usage(TypedDict):
    completion_tokens: int
    completion_tokens_details: CompletionTokensDetails | None
    copilot_usage: UsageCopilotUsage | None
    prompt_tokens: int
    prompt_tokens_details: PromptTokensDetails | None
    reasoning_tokens: int | None
    time_in_ms: int | None
    total_tokens: int

class ToolTelemetryMetrics(TypedDict):
    agent_count: int | None
    callCount: int | None
    cancelled_count: int | None
    cloudRowsReturned: int | None
    codeql_alertCount: Annotated[int | None, GitHubField("codeql.alertCount")]
    codeql_duration_ms: Annotated[int | None, GitHubField("codeql.duration.ms")]
    codeql_languages_count: Annotated[int | None, GitHubField("codeql.languages.count")]
    codeql_languages_skipped_count: Annotated[int | None, GitHubField("codeql.languages.skipped_count")]
    codeql_total_alerts: Annotated[int | None, GitHubField("codeql.total.alerts")]
    codeReview_alertCount: Annotated[int | None, GitHubField("codeReview.alertCount")]
    codeReview_durationMs: Annotated[int | None, GitHubField("codeReview.durationMs")]
    commandTimeout: int | None
    commentsExcluded: int | None
    commentsGenerated: int | None
    compacted_saved_chars: int | None
    completed_count: int | None
    completedStatements: int | None
    definitionCount: int | None
    delivered_count: int | None
    duration_seconds: int | None
    elapsed_seconds: int | None
    exit_code: int | None
    failed_count: int | None
    file_count: int | None
    hasContent: int | None
    idle_count: int | None
    linesAdded: int | None
    linesRemoved: int | None
    localRowsReturned: int | None
    mcp_result_content_bytes: int | None
    mcp_structured_content_bytes: int | None
    mcp_task_count: int | None
    message_length: int | None
    numberOfToolCallsMadeByAgent: int | None
    originalContentLength: int | None
    queue_depth: int | None
    redirectCount: int | None
    requested_recipient_count: int | None
    resolved_recipient_count: int | None
    response_length: int | None
    responseTokenLimit: int | None
    result_length: int | None
    result_length_original: int | None
    resultForLlmLength: int | None
    resultLength: int | None
    returnedContentLength: int | None
    reviewedFiles: int | None
    rowsAffected: int | None
    rowsReturned: int | None
    running_count: int | None
    skillContentLength: int | None
    skipped_count: int | None
    startIndex: int | None
    statementCount: int | None
    symbolCount: int | None
    timeout_seconds: int | None
    total_turns: int | None
    tracked_shutdown_count: int | None
    validation_budgetSeconds: Annotated[int | None, GitHubField("validation.budgetSeconds")]
    validation_codeQLDurationMs: Annotated[int | None, GitHubField("validation.codeQLDurationMs")]
    validation_codeReviewDurationMs: Annotated[int | None, GitHubField("validation.codeReviewDurationMs")]
    validation_iteration: Annotated[int | None, GitHubField("validation.iteration")]
    validation_remainingBudgetMs: Annotated[int | None, GitHubField("validation.remainingBudgetMs")]
    validation_totalDurationMs: Annotated[int | None, GitHubField("validation.totalDurationMs")]

class ToolTelemetryProperties(TypedDict):
    agent_id: str | None
    agent_name: str | None
    agent_name_hash: str | None
    agent_type: str | None
    asyncOnlyShell: str | None
    backend: str | None
    character: str | None
    codeBlocks: str | None
    codeReviewFileExtensions: str | None
    codeReviewModel: str | None
    codeReviewResult: str | None
    codeReviewTimedOut: str | None
    codeReview_engine: Annotated[str | None, GitHubField("codeReview.engine")]
    codeReview_skipReason: Annotated[str | None, GitHubField("codeReview.skipReason")]
    codeql_aborted: Annotated[str | None, GitHubField("codeql.aborted")]
    codeql_analysisRuleIds: Annotated[str | None, GitHubField("codeql.analysisRuleIds")]
    codeql_languages: Annotated[str | None, GitHubField("codeql.languages")]
    codeql_languagesAttempted: Annotated[str | None, GitHubField("codeql.languagesAttempted")]
    codeql_skipReason: Annotated[str | None, GitHubField("codeql.skipReason")]
    codeql_version: Annotated[str | None, GitHubField("codeql.version")]
    command: str | None
    commentQueryNames: str | None
    current_value: str | None
    customTimeout: str | None
    database: str | None
    delivery_status: str | None
    detached: str | None
    error: str | None
    execution_mode: str | None
    executionMode: str | None
    failedStatementType: str | None
    file_hash: str | None
    file_type: str | None
    fileExtension: str | None
    files_found: str | None
    found: str | None
    hashedUrl: str | None
    inputs: str | None
    is_timeout: str | None
    language_server: str | None
    languageId: str | None
    languages: str | None
    large_output: str | None
    largeOutputAvoided: str | None
    largeOutputHandled: str | None
    largeOutputJsonFormatted: str | None
    largeOutputOriginalSizeBytes: str | None
    largeOutputWrittenToFile: str | None
    limit_type: str | None
    limit_value: str | None
    line: str | None
    matches_found: str | None
    mimeType: str | None
    model: str | None
    operation: str | None
    options: str | None
    output_mode: str | None
    outputTruncated: str | None
    prompt_length: str | None
    queryType: str | None
    raw: str | None
    read_target_original_mode: str | None
    read_target_state: str | None
    readError: str | None
    resolved_model: str | None
    resolvedPathAgainstCwd: str | None
    response_length: str | None
    sandboxApplied: str | None
    sandboxOptOutRequested: str | None
    scope: str | None
    selection_kind: str | None
    shell_error_category: str | None
    shell_operation: str | None
    shell_status: str | None
    skillNameHash: str | None
    skillSource: str | None
    statementTypes: str | None
    status: str | None
    timed_out: str | None
    trivialChange_alertCount: Annotated[str | None, GitHubField("trivialChange.alertCount")]
    trivialChange_codeQL_durationMs: Annotated[str | None, GitHubField("trivialChange.codeQL.durationMs")]
    trivialChange_codeQL_isTrivial: Annotated[str | None, GitHubField("trivialChange.codeQL.isTrivial")]
    trivialChange_disagreement: Annotated[str | None, GitHubField("trivialChange.disagreement")]
    trivialChange_isTrivial: Annotated[str | None, GitHubField("trivialChange.isTrivial")]
    validation_budgetResetEnabled: Annotated[str | None, GitHubField("validation.budgetResetEnabled")]
    validation_codeQL_skipReason: Annotated[str | None, GitHubField("validation.codeQL.skipReason")]
    validation_codeQLEnabled: Annotated[str | None, GitHubField("validation.codeQLEnabled")]
    validation_codeQLSuccess: Annotated[str | None, GitHubField("validation.codeQLSuccess")]
    validation_codeQLTimedOut: Annotated[str | None, GitHubField("validation.codeQLTimedOut")]
    validation_codeReview_skipReason: Annotated[str | None, GitHubField("validation.codeReview.skipReason")]
    validation_codeReviewEnabled: Annotated[str | None, GitHubField("validation.codeReviewEnabled")]
    validation_codeReviewSuccess: Annotated[str | None, GitHubField("validation.codeReviewSuccess")]
    validation_codeReviewTimedOut: Annotated[str | None, GitHubField("validation.codeReviewTimedOut")]
    validation_consecutiveTimeouts: Annotated[str | None, GitHubField("validation.consecutiveTimeouts")]
    validation_invalidInput: Annotated[str | None, GitHubField("validation.invalidInput")]
    validation_jobStarted: Annotated[str | None, GitHubField("validation.jobStarted")]
    validation_languages: Annotated[str | None, GitHubField("validation.languages")]
    validation_retryGuidance: Annotated[str | None, GitHubField("validation.retryGuidance")]
    validation_skipReason: Annotated[str | None, GitHubField("validation.skipReason")]
    validation_skipped: Annotated[str | None, GitHubField("validation.skipped")]
    viewType: str | None
    wasSyntaxError: str | None

class ToolTelemetryRestrictedProperties(TypedDict):
    addedPaths: str | None
    agent_id: str | None
    agent_name: str | None
    cloudError: str | None
    codeql_error: Annotated[str | None, GitHubField("codeql.error")]
    codeql_stack: Annotated[str | None, GitHubField("codeql.stack")]
    codeReviewError: str | None
    deletedPaths: str | None
    domParsingError: str | None
    error: str | None
    error_detail: str | None
    errorMessage: str | None
    file: str | None
    filePaths: str | None
    filesReviewed: str | None
    finalUrl: str | None
    large_output_file: str | None
    largeOutputFilePath: str | None
    path: str | None
    pattern: str | None
    pluginName: str | None
    prTitle: str | None
    query: str | None
    shell_id: str | None
    skillName: str | None
    trivialChange_codeQL_reason: Annotated[str | None, GitHubField("trivialChange.codeQL.reason")]
    trivialChange_reason: Annotated[str | None, GitHubField("trivialChange.reason")]
    url: str | None
    validation_error: Annotated[str | None, GitHubField("validation.error")]

class ToolTelemetry(TypedDict):
    event: str | None
    metrics: ToolTelemetryMetrics | None
    properties: ToolTelemetryProperties | None
    restrictedProperties: ToolTelemetryRestrictedProperties | None

class TruncateResult(TypedDict):
    messagesRemovedDuringTruncation: int
    postTruncationMessagesLength: int
    postTruncationTokensInMessages: int
    preTruncationMessagesLength: int
    preTruncationTokensInMessages: int
    tokenLimit: int
    tokensRemovedDuringTruncation: int