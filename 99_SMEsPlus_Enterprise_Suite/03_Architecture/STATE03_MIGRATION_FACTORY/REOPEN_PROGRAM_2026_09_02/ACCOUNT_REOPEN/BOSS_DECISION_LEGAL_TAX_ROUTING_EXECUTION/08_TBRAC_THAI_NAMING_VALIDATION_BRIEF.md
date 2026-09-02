# 08 — TBRAC THAI NAMING VALIDATION BRIEF

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-015` |
| Source | source file `15_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` (151 candidates — used as candidate vocabulary only, not reproduced verbatim here); `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` OB-15; `22_NEXT_PROMPT_RECOMMENDATION.md` §2 item 5 |
| Owner | TBRAC (UNASSIGNED) / Boss (accept/reject working draft) |
| Status | `ROUTING REQUIRED` (panel recruitment) + `BOSS DECISION REQUIRED` (working-draft acceptance) |
| Gate Impact | None directly (no COA gate); feeds UI vocabulary for a future FDS (Functional Design Spec) |

`No Thai name is approved by this brief. Every name remains candidate / UNVALIDATED until TBRAC returns real-user evidence.`

## What source 15 is and is not

Source `15` is a **151-item candidate vocabulary register**, produced by this study as working material — not an approved naming standard. Per session clean-room rules, Thai names are always "candidate / UNVALIDATED." Source `20` OB-15 additionally flags that:

- Two seed names were refined **without explicit Boss instruction** during the source study and must be re-confirmed, not assumed correct.
- The term **กระทบยอด was reserved by this session for "bank reconciliation"** — a scoping choice made without Boss instruction that TBRAC/Boss should explicitly confirm or override before it becomes load-bearing vocabulary.
- Source `21` §2 item 8 separately records that the benchmark's own Thai menu labels are **partly mistranslated** — i.e., the benchmark cannot be used as a naming authority even as a starting point without scrutiny.

## Required TBRAC validation activities

| # | Activity | Required evidence | Status |
|---|---|---|---|
| 1 | Thai accountant review of each candidate name against real bookkeeping/accounting vocabulary | Named reviewer(s), credential, per-item verdict | `ROUTING REQUIRED` |
| 2 | Thai SME owner/user review — does a non-accountant business owner understand the menu name in context? | Named reviewer(s) (should not be the same people as #1 — different fluency profile), per-item verdict | `ROUTING REQUIRED` |
| 3 | Evidence that names are understandable in actual Thai business usage (not just linguistically correct) | Session notes, think-aloud transcripts, or equivalent real-user evidence — analogy or assumption is not sufficient | `ROUTING REQUIRED` |
| 4 | Explicit rejection pass for mistranslated benchmark labels | A list of candidate names the panel flags as inherited-and-wrong, with corrected alternatives | `ROUTING REQUIRED` |
| 5 | Separate mapping: internal technical object name (English, stable, used in code/data model) vs. Thai menu/report display name (user-facing, may change without a data migration) | A two-column mapping table, one row per object | `ROUTING REQUIRED` |

## Two items TBRAC must explicitly rule on (carried from OB-15)

1. The two seed names refined without Boss instruction — confirm or reject the refinement.
2. The กระทบยอด = "bank reconciliation" reservation — confirm or reassign this term.

## What this brief does not do

- It does not approve any name.
- It does not recruit the TBRAC panel — that is a Boss/PMO action (`ACC-DEC-015`, working-draft acceptance decision, is a prerequisite: Boss must first accept source 15 as the *working* vocabulary to hand to TBRAC).
- It does not touch statutory Thai report titles that are legally mandated (DBD-5 in `06_LEGAL_TAX_REVIEW_BRIEF.md`) — that is a separate legal-tax question, not a usability question, even where the same word might appear in both tracks.

## Recruitment checklist for Boss / PMO

- [ ] Name at least 2 Thai accountant reviewers
- [ ] Name at least 2 Thai SME owner/user reviewers (non-accountants)
- [ ] Confirm panel has no conflict of interest with the benchmark vendor
- [ ] Set a review format (workshop, individual survey, or structured interview) that can produce the "real Thai business usage" evidence required by activity #3
- [ ] Schedule TBRAC output to land before any Team B FDS session references Thai menu vocabulary as final
