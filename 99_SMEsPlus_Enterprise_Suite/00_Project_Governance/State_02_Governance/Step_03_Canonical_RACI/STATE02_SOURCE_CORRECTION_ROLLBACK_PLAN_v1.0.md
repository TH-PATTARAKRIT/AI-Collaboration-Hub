# STATE02_SOURCE_CORRECTION_ROLLBACK_PLAN_v1.0.md

Session: SMEPLUS-26-07-14-STEP03-CORR
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Execution Branch: claude/canonical-raci-evidence-xgk851
Prepared By: Claude Code (Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR REVIEW
Gate Status: HOLD

## 1. Rollback Trigger Conditions

Rollback of RC-001 through RC-010 must be executed if any of the following occur:

```text
1. Independent Governance Review returns REJECT on any RC item.
2. Independent Evidence Verification returns EVIDENCE MISMATCH or NOT VERIFIED.
3. Boss withholds or reverses Decision 2 (Controlled Source Correction Authorization).
4. An unauthorized or out-of-scope change is discovered in the same commit.
5. STEP 03 is placed under Replacement Review per
   STATE02_ESCALATION_AND_REPLACEMENT_RULE_v1.0.md.
```

## 2. Rollback Mechanism

```text
Commit to revert: ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc
Command:          git revert ff6cb128d9e5fc2d832cca1e7be97eef2eb356cc
Effect:           Restores APPROVAL_AUTHORITY_MATRIX.md, AI_ROLE_AND_RESPONSIBILITY.md,
                  ARCHITECTURE_GOVERNANCE_STANDARD.md, and FOLDER_REGISTRY.yaml to the
                  blob SHAs recorded in STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md
                  §2 ("Blob SHA Before" column), and removes CANONICAL_ROLE_GLOSSARY.md.
History impact:   NONE — a new revert commit is created; no force-push, no history
                  rewrite, no rebase. Original commit remains in history as evidence.
Authorization
required to
execute rollback:  Boss, or Boss-delegated Execution Coordinator (Executive Secretary /
                  Liza) acting on a recorded Boss decision.
```

## 3. Per-RC Rollback Verification

After a revert, each file's restored blob SHA must be checked against the "Blob SHA
Before" values in `STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md`:

| File | Blob SHA to Restore On Rollback |
|---|---|
| `AI_ROLE_AND_RESPONSIBILITY.md` | `ed333098c4559b91bfcedf6a05cad80e6219671c` |
| `APPROVAL_AUTHORITY_MATRIX.md` | `66930ae503cc6f672bf66a9c450a67ac6872d839` |
| `ARCHITECTURE_GOVERNANCE_STANDARD.md` | `3a262218c3c5c5fc929680d5a5705cea424254fc` |
| `FOLDER_REGISTRY.yaml` | `f307484a5a2b63b1d91835d66845e1a66ae9a064` |
| `CANONICAL_ROLE_GLOSSARY.md` | Not present before correction — rollback removes the file entirely |

## 4. Non-Rollback Scope

```text
No source code, application code, infrastructure, database, or production configuration
was touched by RC-001..RC-010, so rollback of this correction set has no effect outside
the four governance documents and one additive glossary file listed above.
```

## 5. Control Statement

This plan is prepared for review, not self-executed. Rollback requires Boss or
Boss-delegated authorization. Every correction remains reversible via `git revert` without
rewriting history. Gate remains HOLD. Boss remains Sole Final Approver.
