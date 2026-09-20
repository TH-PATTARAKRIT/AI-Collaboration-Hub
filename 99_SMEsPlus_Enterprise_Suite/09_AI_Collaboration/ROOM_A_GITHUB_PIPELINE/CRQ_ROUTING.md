# Controlled CRQ Routing

Status: `STRUCTURAL PREFLIGHT ONLY / CONTROLLER NOT CONFIGURED`

## A2 asks A1

| Step | Event | Sender | Receiver | Meaning |
|---:|---|---|---|---|
| 1 | `A2_CRQ_OPENED` | A2 | A1 | A2 found a bounded question; affected CFC/edges remain blocked. |
| 2 | `A1_CRQ_RESPONSE_READY` | A1 | A2 | A1 supplied a restricted answer artifact; the CRQ is not closed. |
| 3a | `A2_CRQ_OPENED` | A2 | A1 | A2 rejects or needs a revised answer; attempt and parent advance. |
| 3b | `A2_REVIEW_READY` | A2 | A3 | A2 verified the answer and no Critical/High CRQ or blocking dependency remains. |
| 3c | `HOLD` | Controller | Controller | The bounded or systemic stop condition is recorded without deleting evidence. |

## Public control record

Allowed:

- `crq_ids`;
- CRQ counts by severity;
- `cfc_revisions` and blocked dependency IDs;
- opaque handoff/payload artifact IDs;
- manifests and SHA-256 values;
- event parent, attempt and state.

Prohibited:

- question or answer prose derived from source;
- source excerpts, file paths, `path:line`, symbols or private APIs;
- customer, database or personal data;
- credentials;
- ROOM B design material.

## Controller invariants before activation

- authenticate the sender role independently of payload fields;
- compare-and-set the canonical batch state atomically;
- enforce unique event and idempotency keys;
- verify parent existence, attempt monotonicity and manifest hash chain;
- verify every CRQ ID against the private CRQ register;
- lock affected CFC/edges while Critical/High CRQs are open;
- prevent A1 from closing, verifying or deleting its own CRQ response;
- resume A2 only after the response artifact is immutable and its hash is verified;
- preserve rejected and superseded responses in the audit trail.
