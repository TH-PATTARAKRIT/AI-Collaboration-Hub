# STATE02_STEP03_INDEPENDENT_VERIFICATION_REQUEST_v1.0.md

Session: SMEPLUS-26-07-14-STEP03-CORR
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Execution Branch: claude/canonical-raci-evidence-xgk851
Draft PR: #20
Related Issue: #5
Requested By: Claude Code (Responsible role only — requests verification, does not perform it)
Requested At: 2026-07-14 (UTC)
Verifier Role Required: Independent Evidence Verifier (EV — must be separate from the
preparer; per Canonical RACI §2, may be ChatGPT L99 only where evidence is
system-generated and independently inspectable; must never rely only on Claude AI
self-report)
Document Status: VERIFICATION REQUESTED — NOT YET VERIFIED

## 1. Instruction to Verifier

Claude Code has prepared, but not independently verified, the items below. Direct,
independent inspection of the repository is required — do not accept any hash, path, or
commit SHA in this request as verified without re-computing or re-checking it yourself.
Record your result only in the "Verifier Result" column using one of the four permitted
values.

Permitted Verification results: `VERIFIED`, `PARTIALLY VERIFIED`, `NOT VERIFIED`,
`EVIDENCE MISMATCH`.

## 2. Verification Scope

| # | Inspection Item | What to Check | Evidence Path | Verifier Result |
|---|---|---|---|---|
| 1 | Repository paths | Every file path referenced in the evidence register actually exists at the stated path on `claude/canonical-raci-evidence-xgk851` | `STATE02_STEP03_EVIDENCE_REGISTER_v1.0.md` | |
| 2 | Commit SHAs | `ff6cb12` (RACI correction record + RC-001..RC-010 edits + glossary), `2bb40da` (RC execution/before-after/rollback records), `2ed3925` (SHA256 recalculation + evidence register update) each contain exactly the files claimed | `git show --stat <sha>` against each commit | |
| 3 | Changed-file count | 6 files in `ff6cb12`, 3 files in `2bb40da`, 4 files in `2ed3925` — no more, no fewer | `git show --stat` per commit | |
| 4 | Before/After evidence | Blob SHA before matches the pre-correction blob for each of `APPROVAL_AUTHORITY_MATRIX.md`, `AI_ROLE_AND_RESPONSIBILITY.md`, `ARCHITECTURE_GOVERNANCE_STANDARD.md`, `FOLDER_REGISTRY.yaml`; before/after text matches actual diff | `STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md`; `git diff <before>..<after> -- <file>` | |
| 5 | Actual SHA256 values | Independently re-run `sha256sum` on every file listed in the manifest and compare to the recorded value | `STATE02_STEP03_SHA256_MANIFEST_v1.1.txt` | |
| 6 | Manifest completeness | Every file in the Step 03 package directory and every RC-modified source file appears in the manifest; no silent omission | `STATE02_STEP03_SHA256_MANIFEST_v1.1.txt`; directory listing of `Step_03_Canonical_RACI/` | |
| 7 | Source-correction scope | `git diff` for `ff6cb12` touches only the 10 lines identified in `STATE02_SOURCE_GOVERNANCE_CONFLICT_REGISTER_v1.0.md` across the 4 files, plus the new additive glossary — no other line changed | `git diff ff6cb12^..ff6cb12` | |
| 8 | Role separation | Confirm Claude Code (preparer) did not fill any Reviewer Decision or Verifier Result field in the review/verification requests, and did not record any PASS/APPROVED/CLOSED/FINAL status anywhere in this package | `STATE02_STEP03_INDEPENDENT_REVIEW_REQUEST_v1.0.md`; this file; full grep of package for prohibited terms | |
| 9 | Boss approval evidence | `STATE02_STEP03_BOSS_APPROVAL_RECORD_v1.0.md` accurately transcribes the actual Boss comment on PR #20 (cross-check against the live GitHub PR, not just the transcription) | PR #20 review comments vs. `STATE02_STEP03_BOSS_APPROVAL_RECORD_v1.0.md` | |
| 10 | Unauthorized modification absence | No source code, application code, infrastructure, database, or production configuration file appears in any commit in this correction set | `git show --stat` for `ff6cb12`, `2bb40da`, `2ed3925` | |

## 3. Explicit Non-Requests

Claude Code does not ask the Verifier to declare STEP 03 PASS, CLOSED, COMPLETE, FINAL,
or APPROVED, and does not ask the Verifier to record `FULLY VERIFIED` on behalf of Claude
Code — only the Verifier's own direct inspection may produce that result.

## 4. Control Statement

This request package is prepared, not verified. Verifier Result cells are intentionally
blank; Claude Code does not fill them. Gate remains HOLD pending verification. Boss
remains Sole Final Approver.
