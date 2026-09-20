# Security and Evidence Controls

## Current preflight boundary

The current workflow is intentionally non-authoritative. It performs structural and deny-pattern checks only and has read-only repository permission. Passing preflight cannot create, claim, accept, reject, continue or hold a canonical batch.

## Activation rules

- Treat Issue bodies, comments, PR text, dispatch payloads and agent output as untrusted input.
- Validate an event before using it for routing or state changes.
- Never interpolate agent content into executable commands.
- Never use `pull_request_target` for this pipeline.
- Never put restricted evidence in Actions logs, caches or artifacts.
- A timeout, interrupted run or partial artifact is not success.
- The private controller must reject duplicate event/idempotency keys, stale or absent parents, manifest-chain mismatches, non-monotonic attempts, corpus/module drift and unauthenticated role claims.
- The private controller must bind role authority to the authenticated GitHub App/environment; payload role fields are never identity proof.
- Public Issue forms and unvalidated comments must not be used as pipeline ingress.
- A systemic corpus or provenance failure sets `GLOBAL_HOLD`; existing evidence is retained.

## Required controls before activation

| Control | Current state |
|---|---|
| Default-branch protection with independent review | `NOT CONFIGURED` |
| Dedicated orchestrator GitHub App | `NOT CONFIGURED` |
| Role-specific protected environments | `NOT CONFIGURED` |
| Separate A1/A2/A3/MASTER credentials | `NOT CONFIGURED` |
| Isolated self-hosted ROOM A runners | `NOT CONFIGURED` |
| Persistent event/idempotency uniqueness | `NOT CONFIGURED` |
| Parent, hash-chain and frozen-corpus lookup | `NOT CONFIGURED` |
| Authenticated actor-to-role binding | `NOT CONFIGURED` |
| Public-metadata leakage preflight | `STRUCTURAL VALIDATOR ONLY` |

The pipeline must remain metadata-only until every required control is independently verified.
