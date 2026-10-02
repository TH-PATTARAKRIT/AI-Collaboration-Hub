# U97 Neutral Knowledge — Survey CRM Integration
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U97-001 | The platform's survey capability is modelled as a primary entity that participates in threaded messaging and activity tracking. |
| NR-U97-002 | A survey may be classified as one of four operational types: a standard survey, a live interactive session, a scored assessment, or a custom-configured form. |
| NR-U97-003 | Survey access can be set to open (anyone with a public link) or restricted (invited people who have a private token). |
| NR-U97-004 | An additional login requirement can be imposed independently of the access mode, forcing authenticated sign-in even when a valid token is held. |
| NR-U97-005 | Four scoring strategies are available: no scoring, scored with correct answers revealed after each page, scored with answers revealed at the end, and scored without revealing answers at all. |
| NR-U97-006 | A configurable passing threshold (default 80 percent) determines whether a respondent is considered to have succeeded the survey or certification. |
| NR-U97-007 | The database enforces that certification mode can only be enabled when a scoring strategy other than "no scoring" is chosen. |
| NR-U97-008 | Each set of answers submitted by one participant to one survey is tracked as a separate response record that also participates in messaging and activities. |
| NR-U97-009 | A response record moves through three lifecycle states: new (not yet started), in progress (started), and completed. There is no invalidated state in this version. |
| NR-U97-010 | Every response is identified by a unique access token; an invite token groups attempts by the same participant when attempt limits are active. |
| NR-U97-011 | Total score and score percentage for each response are stored redundantly to support efficient reporting queries. |
| NR-U97-012 | A response is marked as passed when its score percentage equals or exceeds the survey's required minimum percentage. |
| NR-U97-013 | When a participant begins answering, the system records the current timestamp as the session start time and moves the response to the in-progress state. |
| NR-U97-014 | When a participant submits their final answers, the system records the end timestamp, moves the response to the completed state, and may trigger additional post-completion actions such as sending a certificate. |
| NR-U97-015 | The transition to the completed state is performed atomically in a single write operation that sets both the end time and the status. |
| NR-U97-016 | Before a new participation token is issued, the platform validates that the survey is active, that the requester meets the access mode requirements, and that attempt limits have not been exhausted. |
| NR-U97-017 | When a survey requires authentication with no public sign-up, external participants without a known partner record are rejected before a token is issued. |
| NR-U97-018 | When a survey is restricted to internal staff, any request from a non-employee participant is rejected at token-issuance time. |
| NR-U97-019 | The CRM integration module extends the survey entity rather than creating a new model; it adds lead-generation fields and a sales-team assignment to the existing survey record. |
| NR-U97-020 | A survey is flagged as lead-generating when its type permits lead creation and at least one of its questions contains an answer choice marked as lead-triggering. |
| NR-U97-021 | Each survey that generates leads maintains a reverse link to all opportunity records it has produced. |
| NR-U97-022 | A survey can be pre-configured with a target sales team; leads produced from the survey will be assigned to that team. |
| NR-U97-023 | Individual answer choices on multiple-select and choice questions can each be independently marked as lead-triggering. |
| NR-U97-024 | A question is considered lead-generating only if it is a choice type (single-choice, multiple-choice, or matrix) and at least one of its answer options is marked as lead-triggering. |
| NR-U97-025 | Each response record is linked to at most one CRM opportunity that was created from it. |
| NR-U97-026 | The transition-to-completed operation is extended by the CRM integration to also evaluate whether new opportunity records should be created; this hook runs for all non-live-session completion paths. |
| NR-U97-027 | Lead creation is limited to surveys of type standard, live session, or custom; the assessment type does not generate leads. |
| NR-U97-028 | A completed response only generates a lead if at least one answer actually chosen by the participant was marked as lead-triggering; browsing without selecting a triggering option produces no lead. |
| NR-U97-029 | Leads are created in bulk with elevated privileges to avoid access-control failures when participants are public or portal users. |
| NR-U97-030 | All automatically-created leads are classified as opportunities rather than raw leads, reflecting the assumption that survey respondents represent qualified prospects. |
| NR-U97-031 | The opportunity record gains a back-reference to the survey that produced it, enabling reporting on lead origin by survey. |
| NR-U97-032 | For live session surveys, lead creation is triggered by the session-end action on the survey rather than by individual response completion, ensuring all session answers are processed together. |
