# 01_CLASSIFICATION_FRAMEWORK.md

Order: /L99.99 — State 02, Step 08 — Classification Registers
Work Package: WP-08-01 — Classification Framework
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: claude/state-02-classification-registers-7qwwcy
Prepared By: Claude Code (Preparer / Executor — Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD

## 1. Classification Objectives

- Establish exactly one controlling classification for every governance item so that
  authority to control execution is unambiguous.
- Separate five orthogonal dimensions that must never be treated as interchangeable:
  Classification, Execution Status, Verification Status, Gate Status, Approval Status.
- Ensure that no item controls execution unless it is classified, owned, and evidenced.
- Provide an auditable, reproducible basis for the Step 08 registers and matrices.

## 2. Classification Scope

Applies to all State 02 governance items in
`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/` and its `State_02_Governance/`
subtree: documents, requirements and work items, evidence, RAID items, decisions and
exceptions, execution/verification/gate/approval statuses, and confidentiality/access.
Root-scope governance standards are in scope for document classification where they
control State 02 execution.

## 3. Classification Authorities

| Authority | May classify | May approve classification | Constraint |
|---|---|---|---|
| Claude Code (Preparer) | Prepare/assign draft classification | No | Cannot verify or approve own classification |
| Document Control (DC) | Assign document classification | No (executes after approval) | Registry maintenance only |
| ChatGPT L99 (Independent Governance Reviewer) | Review classification | No (recommend only) | Cannot be Final Approver |
| Independent Evidence Verifier | Verify evidence backing a classification | No | Must be non-preparer identity |
| Boss (Final Approver) | — | Yes (sole) | Sole authority to confirm CANONICAL / close |

Draft classification prepared by Claude Code is not a controlling classification until it
is independently reviewed and Boss-confirmed where authority impact exists.

## 4. Document Classification Rules

- Every governance document receives exactly one primary classification from the DOC set
  (see doc 02): CANONICAL, SUPPORTING, WORKING DRAFT, SUPERSEDED, ARCHIVED,
  RETAINED AS EVIDENCE, UNCLASSIFIED.
- Only one controlling CANONICAL document may exist per governance topic. Competing
  canonical documents are recorded as a CONFLICT and are Boss-decision items.
- A SUPERSEDED document must name its replacement (Superseded By).
- An UNCLASSIFIED document cannot control execution.
- Historical evidence is never deleted; superseded material is retained.

## 5. Evidence Classification Rules

Evidence is classified E0–E5 (see doc 05). E4 (claim / unverified status update) does not
count as verified progress. E5 (missing / inaccessible) is classified HOLD, FAIL, or
FROZEN by criticality. A classification that controls execution must be backed by E0–E2
evidence with a location and timestamp.

## 6. Work-Item Classification Rules

Every work item is registered (doc 04) with an Owner, Priority, Status, and Evidence.
A work item with No Owner is FROZEN. A work item without evidence cannot be reported as
verified progress.

## 7. Status Classification Rules

Execution status (doc 09) describes only preparation/execution state. It never implies
verification, gate, or approval. Transitions follow the allowed next-status map in doc 09.

## 8. Gate Classification Rules

Gate status (doc 09) is PASS, PASS WITH CONTROL, HOLD, FAIL, FROZEN, NOT APPLICABLE.
A Gate result is only valid when supported by independent review and verification
evidence. No preparer may declare a Gate PASS.

## 9. Confidentiality Classification Rules

Confidentiality (doc 10) is PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED, or
SECRET/CREDENTIAL — REFERENCE ONLY. Secrets, credentials, tokens, and private keys are
never copied into any register; only a controlled reference to the secret-storage
location is recorded.

## 10. Reclassification Rules

Any change of classification is logged (doc 13) with previous value, new value, reason,
evidence, requester, reviewer, approver, effective date, affected records, rollback
method, and gate impact. Reclassification that changes controlling authority requires
Boss confirmation.

## 11. Archive and Supersession Rules

Superseding a document requires an archive record naming paths, reason, replacement, and
the SHA-256 of both old and new. Archived material remains in the repository. Nothing is
deleted under this order.

## 12. Entry Criteria (to assign a controlling classification)

- Item exists at an inspectable repository path or system location.
- Item has a named Owner.
- Item has at least one evidence reference (E0–E2 for execution-controlling items).
- Classification code is defined in doc 02.

## 13. Exit Criteria (classification changes / retires)

- A superseding item is CANONICAL-confirmed, or the item is archived/retired per rule 11,
  or independent review directs reclassification, recorded in doc 13.

## 14. Exception Handling

Any deviation from these rules (including the branch reconciliation in doc 00) is recorded
as an exception in doc 07 with conditions and expiry, and is a Boss / independent-review
decision item. Exceptions are never self-approved by the preparer.

## 15. Audit Trail Requirements

Every classified record carries: repository path or system location, version, owner,
evidence reference, timestamp, and (where integrity matters) commit SHA / blob SHA /
SHA-256. The Step 08 manifest and validation report provide the reproducible audit basis.

## 16. Non-Interchangeability (mandatory)

```text
Classification        ≠ Execution Status
Execution Status      ≠ Verification Status
Verification Status   ≠ Gate Status
Gate Status           ≠ Approval Status
EXECUTION COMPLETE    ≠ APPROVED
READY                 ≠ PASS
SUBMITTED             ≠ VERIFIED
AVAILABLE             ≠ ACCEPTED
CLAIMED               ≠ VERIFIED
```

These five dimensions are recorded in separate fields and never collapsed into one status
or one percentage.
