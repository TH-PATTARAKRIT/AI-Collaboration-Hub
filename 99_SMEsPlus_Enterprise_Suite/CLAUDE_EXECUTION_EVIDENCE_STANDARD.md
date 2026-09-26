# Claude Execution Evidence Folder Standard

Document ID: SMEPLUS-CLAUDE-EXEC-EVIDENCE-STD-001
Control Level: /L99.99
Status: DRAFT / HOLD (standard proposed; not an approval mechanism)
Updated: 2026-07-14
Owner: PMO Evidence AI / Claude Execution
Independent Reviewer: ChatGPT L99
Approval Authority: Boss
Applies to: `14_Claude_Execution/` and all Claude execution evidence in the suite

## 1. Purpose

Define one controlled folder structure and evidence standard for **Claude execution
evidence**, so that every Claude execution task produces inspectable, non-fabricated,
traceable evidence under the rule **No Evidence = No Progress**. This standard organizes
where Claude execution artifacts live and what fields each must carry. It does not grant any
approval; authoritative gate status remains `CURRENT_GATE_STATUS.md` (HOLD — NEED EXECUTION
EVIDENCE).

## 2. Scope

- In scope: task prompts, execution logs, produced artifacts, evidence registers, manifests,
  and handoff/review records created by Claude execution.
- Out of scope: approving gates, marking VERIFIED, writing application/build code, creating
  credentials.

## 3. Canonical Folder Layout (`14_Claude_Execution/`)

```text
14_Claude_Execution/
  README.md                         # index of execution batches (pointer to this standard)
  Task_Prompts/                     # authorized task prompts / handoff standards (input)
  <BATCH_ID>/                       # one folder per execution batch
    00_TASK/                        # the exact task/order the batch executed
    10_WORK/                        # produced working artifacts (drafts, documents)
    20_EVIDENCE/                    # evidence register + supporting evidence
    30_VALIDATION/                  # automated validation scripts + reports
    40_HANDOFF/                     # independent-review handoff + gap report
    MANIFEST_SHA256_<BATCH_ID>.txt  # SHA-256 manifest for the batch (authoritative)
    EXECUTION_SUMMARY_<BATCH_ID>.md # what was inspected/created/updated + gate impact
```

Batches that must live beside existing domain files (e.g., Accounting FDS under
`02_Functional_Design/`) may keep the artifact in place and record its path in the batch
`20_EVIDENCE/` register and `MANIFEST`, rather than duplicating the file into
`14_Claude_Execution/`. Duplication of authoritative files is prohibited (see §7).

## 4. Naming Rules

- `<BATCH_ID>`: `SMEPLUS-<STATE|MODULE>-<TOPIC>-BATCH<NN>` (uppercase, hyphenated).
- Manifests: `MANIFEST_SHA256_<BATCH_ID>.txt` or the established domain name
  (e.g., `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt`).
- No spaces in new folder names; existing filenames with spaces are referenced verbatim.

## 5. Mandatory Evidence Fields (per artifact, in the batch evidence register)

| Field | Requirement |
|---|---|
| Artifact / WP ID | Identifier |
| GitHub evidence path | Repo-root-relative, must resolve to a committed file |
| Content hash | SHA-256 (and/or git blob SHA) |
| Owner | Named AI/human owner |
| Timestamp | Creation/update time |
| Reviewer | Independent reviewer (not the drafting agent) |
| Verification status | From the controlled legend (§6) |
| Build eligibility | BUILD ELIGIBLE / NOT BUILD ELIGIBLE |
| Gate impact | Which gate(s) affected |
| Dependencies | Upstream/downstream references |
| Open issues | Unresolved items / decisions required |

Chat-only, local-only, or uncommitted content is not accepted as evidence.

## 6. Controlled Verification-Status Legend

`DRAFT CREATED` · `PREPARED FOR REVIEW` · `REVIEW IN PROGRESS` · `VERIFIED` · `REJECTED`
· `HOLD` · `NOT VERIFIED`

- Claude may set any status **except** `VERIFIED`. Only a named independent reviewer sets
  `VERIFIED`. Claude must not mark `APPROVED`, `PASS`, `BUILD READY`, `RELEASE READY`, or
  `PRODUCTION READY`.

## 7. Integrity Rules

1. Every batch has exactly one authoritative manifest; nested duplicate manifests are
   prohibited and, if found, marked `_SUPERSEDED_DO_NOT_USE.md` (never silently deleted).
2. The manifest is regenerated after the final content change of the batch (freeze → rebuild).
3. No evidence path may point to a missing file.
4. Historical documents are preserved; superseded ones are marked, not deleted.
5. Automated validation is evidence, not approval.

## 8. Relationship to Authoritative Gate Status

This standard governs how evidence is organized. It does not move any gate. The single
authoritative gate status is `CURRENT_GATE_STATUS.md` — currently **HOLD — NEED EXECUTION
EVIDENCE**.

## 9. Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | 2026-07-14 | Initial Claude execution evidence folder standard | Claude Code (evidence-only remediation) |

## 10. Approval Status

DRAFT / HOLD — prepared for independent review. No gate approved. Boss decision mandatory.
