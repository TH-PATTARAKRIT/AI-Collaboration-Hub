# 04 — SHA-256 Manifest Verification (State 02 · Step 09 · EV-03)

Candidate Commit: `4da8cc8423ff9f6964112b2c5b780020cb8e40fa`
Prepared By: Claude Code · Prepared At: 2026-07-14 (UTC)
Reviewer: PENDING INDEPENDENT REVIEW · Verifier: PENDING INDEPENDENT VERIFICATION

This document records (a) the producer verification of the **State 02 Finalization package** internal
manifest at the candidate commit, and (b) the method and producer recompute for **this Step 09 package**
manifest.

---

## 1. Finalization package manifest (verification subject, @ candidate)

File: `STATE02_FINALIZATION/PACKAGE_MANIFEST_SHA256.txt` (blob `df974c12`)

```bash
$ cd .../State_02_Governance/STATE02_FINALIZATION
$ sha256sum -c PACKAGE_MANIFEST_SHA256.txt
```
Result: **17 of 17 files OK** (00–16 + no self-hash). Producer recompute matched every entry.

| Control | Result |
|---|---|
| Files covered | 17 (docs 00–16) |
| Manifest excludes itself | YES |
| Producer recompute | **17/17 matched** |
| Manifest identifies verification target | YES — header names "PR #24 head" + baseline `8570187` |
| Manifest identifies UTC generation | YES — "Generated: 2026-07-14 (UTC)" |

**Manifest target/recompute control (EV-D09) — re-inspected, not closed by prior claim:** The
finalization manifest header names the verification target descriptively as "PR #24 head" and gives the
baseline commit `8570187`, but does **not** pin the 40-character head SHA (`4da8cc8`) in the manifest body.
This is a traceability weakness (the target commit must be read from the live PR, not the artifact).
Recorded as EV-D09 (P2, non-blocking) in doc 07. Producer recompute itself: PASS (17/17).

---

## 2. This Step 09 package manifest (method)

Manifest rules applied:

| Rule | Applied |
|---|---|
| Algorithm | SHA-256 (`sha256sum`) |
| Encoding | UTF-8 |
| Line endings | LF (Unix), recorded |
| Identifies STEP09_CANDIDATE_COMMIT | YES — `4da8cc8...` in manifest header |
| Identifies UTC generation timestamp | YES — in manifest header |
| Covers files 00 through 10 | YES — 11 deliverables |
| Excludes itself | YES — `PACKAGE_MANIFEST_SHA256.txt` not hashed |

Generation command (exact):
```bash
cd .../State_02_Governance/Step_09_Evidence_Verification
sha256sum \
  00_STEP09_EXECUTIVE_SUMMARY.md \
  01_EVIDENCE_SCOPE_REGISTER.md \
  02_REPOSITORY_FILE_VERIFICATION.md \
  03_COMMIT_AND_DIFF_VERIFICATION.md \
  04_SHA256_MANIFEST_VERIFICATION.md \
  05_AUTHORITY_AND_RACI_VERIFICATION.md \
  06_GATE_AND_CLASSIFICATION_VERIFICATION.md \
  07_DEFECT_AND_EXCEPTION_REGISTER.md \
  08_STEP09_VERIFICATION_RESULT.md \
  09_STEP09_BOSS_APPROVAL_QUEUE.md \
  10_STEP09_COMPLETION_CHECKLIST.md \
  > PACKAGE_MANIFEST_SHA256.txt
```

Producer recompute command (independent-reproducible):
```bash
sha256sum -c <(grep -v '^#' PACKAGE_MANIFEST_SHA256.txt)
```

Producer result (recorded at commit time, see commit + PR comment):
```text
MANIFEST CHECK COMPLETED
Producer Recompute: 11/11 matched
```

Claude Code does **not** state INDEPENDENTLY VERIFIED. Independent recompute is reserved for the
appointed Independent Evidence Verifier (see doc 08 handoff).

Verification Status: **PENDING INDEPENDENT VERIFICATION.**
