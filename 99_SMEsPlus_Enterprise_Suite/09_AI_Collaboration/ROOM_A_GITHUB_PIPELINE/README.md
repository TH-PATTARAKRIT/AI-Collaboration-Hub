# ROOM A GitHub Agent Pipeline

Status: `STRUCTURAL PREFLIGHT ONLY / METADATA-ONLY / PREPARED FOR REVIEW`

GitHub is the control plane for the ROOM A chain:

```text
A1 research producer
  -> A2 functional QA
      -> CRQ to A1 -> A1 response -> A2 re-verification
  -> A3 independent challenge
  -> MASTER RED TEAM disposition
  -> next A1 batch or bounded return/HOLD
```

## Current capability

The included workflow checks only the shape and source-neutrality of an event. A successful check means `STRUCTURALLY VALID`; it does **not** mean the producer is authenticated, the referenced parent exists, manifests match stored artifacts, module IDs belong to the frozen corpus, or a canonical state transition is authorized.

The example event is synthetic and non-evidentiary. It must never be imported into the canonical batch ledger.

## Fixed authority boundary

- Automatic continuation is a future controller capability and is not activated by this package.
- No event or workflow in this package grants Boss approval.
- No automatic runtime execution, ROOM B transfer, product-scope selection, merge, release, deployment, RA-01 closure, or RA-02 final approval is permitted.
- The current workflow cannot mutate Issues, labels, branches, pull requests or a canonical batch ledger.
- A future canonical controller may route work only after stateful verification; it may not self-certify independent review.

## Public repository boundary

This repository is public. Only source-neutral control metadata may be committed or dispatched:

- batch/module/CRQ identifiers;
- owner group and stage;
- aggregate counts;
- SHA-256 manifests and revision lineage;
- source-neutral status and gate recommendation.

The following are prohibited:

- source code or excerpts;
- `path:line`, source file paths, class/method/private API/XML IDs;
- implementation-derived pseudocode or schema copies;
- restricted evidence maps;
- credentials, customer data, database data, personal data;
- ROOM B design artifacts.

Public Issues are not an ingress channel. A future private controller must validate and normalize an event before publishing any control record.

## Event contract

Every handoff preflight uses `contracts/batch-event.schema.json` and `config/state-transitions.json`. The validator loads both rather than maintaining a separate transition list. It enforces:

- exact allowed keys;
- producer/consumer transition compatibility;
- 64-character lowercase SHA-256 fields;
- assigned/received/module count equality and unique module IDs;
- CRQ severity totals equal the explicit `open_crq_ids` set;
- valid timestamps;
- a parent event ID field for all events after A1, without claiming that the parent exists;
- rejection of forbidden field names and source-specific content markers;
- a deterministic idempotency-key format with no free text;
- `MASTER_AUTO_CONTINUE` requires zero Critical/High CRQs, no blocking dependency, and distinct source/target batch IDs;
- `A2_CRQ_OPENED` routes an opaque CRQ set to A1 and `A1_CRQ_RESPONSE_READY` returns evidence to A2;
- an A1 response is `ANSWERED_RESTRICTED`, never automatic CRQ closure;
- `A2_REVIEW_READY` requires zero Critical/High CRQs and no blocking dependency;
- `HOLD` requires scope, reason code and finding IDs;
- workflow-dispatch paths stay below the approved event directory.

The validator does not provide durable replay protection, authenticated role binding, frozen-corpus membership, parent/hash-chain verification, attempt monotonicity or atomic compare-and-set. Those are mandatory controller controls before activation.

## A2 to A1 controlled question loop

```text
A2 detects a question
  -> A2_CRQ_OPENED / ACTION_REQUIRED
  -> future Controller authenticates A2 and locks affected edges
  -> A1 studies the restricted evidence
  -> A1_CRQ_RESPONSE_READY / ANSWERED_RESTRICTED
  -> A2 verifies semantics and evidence
  -> reopen CRQ, issue HOLD, or emit A2_REVIEW_READY
```

GitHub receives only CRQ IDs, counts, opaque artifact IDs and hashes. Question text, answer text, source evidence and `path:line` remain in controlled ROOM A storage. A1 cannot mark its own answer `VERIFIED` or `CLOSED`; only A2 may proceed after re-verification, and Critical/High CRQs continue to block `A2_REVIEW_READY`.

## Role isolation

`config/roles.json` declares distinct A1, A2, A3, MASTER and CONTROLLER roles. Role names inside an event are untrusted declarations, not identity proof. All integrations remain `NOT_CONFIGURED`; the validation workflow cannot invoke an AI provider, mutate issues, apply labels, merge PRs, or access ROOM A source.

When activated later, each role requires a separate identity, runner workspace and least-privilege environment. A role must not approve or merge its own output.

## Rollout

1. **Current:** structural and leakage preflight in pull requests/manual dry-runs, including adversarial tests.
2. Create a private controller ledger with unique event/idempotency constraints, parent/hash-chain checks, frozen-corpus membership and atomic state transitions.
3. Install a dedicated GitHub App, bind authenticated installations to roles, create protected environments, and protect the default branch.
4. Register isolated self-hosted ROOM A runners; never run public-PR code on them and never upload restricted source to GitHub-hosted runners.
5. Configure provider credentials per role and pin every production Action to a reviewed commit.
6. Run one shadow batch without canonical state mutation.
7. Enable controller-owned normalized Issue/label views after independent review.

## Local validation

```text
node 99_SMEsPlus_Enterprise_Suite/09_AI_Collaboration/ROOM_A_GITHUB_PIPELINE/scripts/validate-event.mjs \
  99_SMEsPlus_Enterprise_Suite/09_AI_Collaboration/ROOM_A_GITHUB_PIPELINE/events/examples/a1-handoff-ready.json
```

Expected result begins with `VALID ROOM A STRUCTURAL EVENT` and is followed by a non-authoritative warning.
