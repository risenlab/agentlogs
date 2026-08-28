from __future__ import annotations

import datetime as dt
from typing import Annotated, TypedDict

from .annotation import GitHubField, Note, Relation
from .references import AgentSessionReference

class AgentSessionLogEntry(TypedDict):
    session: Annotated[AgentSessionReference, Relation()]
    entry_index: int

    parsed: bool
    raw: Annotated[
        str | None,
        Note("Not set when `parsed` is true"),
    ]
    data: Annotated[
        AgentSessionLogEntryData | None,
        GitHubField(""),
        Note("Not set when `parsed` is false. Refer to `raw` instead"),
    ]

class AgentSessionLogEntryData(TypedDict):
    id: Annotated[str | None, GitHubField("id")]
    agentId: Annotated[str | None, GitHubField("agentId")]
    arguments: ToolArguments | None
    callId: Annotated[str | None, GitHubField("callId")]
    choices: list[Choice] | None
    content: list[ContentPart] | None
    copilotBillingMetadata: CopilotBillingMetadata | None
    copilot_info_messages: Annotated[list[CopilotInfoMessage] | None, GitHubField("copilot_info_messages")]
    copilot_model_warning_message: Annotated[str | None, GitHubField("copilot_model_warning_message")]
    copilot_usage: CopilotUsage | None
    copilot_warning_messages: Annotated[list[CopilotWarningMessage] | None, GitHubField("copilot_warning_messages")]
    created: Annotated[dt.datetime | None, GitHubField("created")]
    data: EventData | None
    ephemeral: Annotated[bool | None, GitHubField("ephemeral")]
    error: ErrorInfo | None
    kind: Annotated[str | None, GitHubField("kind")]
    model: Annotated[str | None, GitHubField("model")]
    modelCall_error: Annotated[str | None, GitHubField("modelCall.error")]
    modelCallDurationMs: Annotated[int | None, GitHubField("modelCallDurationMs")]
    object: Annotated[str | None, GitHubField("object")]
    output: Annotated[str | None, GitHubField("output")]
    parentId: Annotated[str | None, GitHubField("parentId")]
    performedBy: Annotated[str | None, GitHubField("performedBy")]
    prompt_filter_results: list[PromptFilterResult] | None
    role: Annotated[str | None, GitHubField("role")]
    source: Annotated[str | None, GitHubField("source")]
    system_fingerprint: Annotated[str | None, GitHubField("system_fingerprint")]
    timestamp: Annotated[str | None, GitHubField("timestamp")]
    toolCallId: Annotated[str | None, GitHubField("toolCallId")]
    toolName: Annotated[str | None, GitHubField("toolName")]
    tool_call_id: Annotated[str | None, GitHubField("tool_call_id")]
    truncateResult: TruncateResult | None
    turn: Annotated[int | None, GitHubField("turn")]
    type: Annotated[str | None, GitHubField("type")]
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

class IPCitation(TypedDict):
    citation_type: str | None
    ip_type: str
    license: str
    snippet: str
    url: str

class IPCitationEntry(TypedDict):
    citations: IPCitation
    end_offset: int
    id: int
    start_offset: int | None

class CopilotAnnotations(TypedDict):
    IPCodeCitations: list[IPCitationEntry] | None
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


class ToolArguments(TypedDict):
    canOfferSessionApproval: bool | None
    command: str | None
    description: str | None
    diff: str | None
    filePath: str | None
    kind: str | None
    toolName: str | None

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

class EventData(TypedDict):
    actions: list[str] | None
    alreadyInUse: bool | None
    approved: bool | None
    autoApproveEdits: bool | None
    eventCount: int | None
    eventsFileSizeBytes: int | None
    feedback: str | None
    intent: str | None
    newMode: str | None
    planContent: str | None
    previousMode: str | None
    reason: str | None
    reasoningEffort: str | None
    recommendedAction: str | None
    remoteSteerable: bool | None
    requestId: str | None
    selectedAction: str | None
    selectedModel: str | None
    summary: str | None
    toolCallId: str | None
    turnId: str | None

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

class TruncateResult(TypedDict):
    messagesRemovedDuringTruncation: int
    postTruncationMessagesLength: int
    postTruncationTokensInMessages: int
    preTruncationMessagesLength: int
    preTruncationTokensInMessages: int
    tokenLimit: int
    tokensRemovedDuringTruncation: int