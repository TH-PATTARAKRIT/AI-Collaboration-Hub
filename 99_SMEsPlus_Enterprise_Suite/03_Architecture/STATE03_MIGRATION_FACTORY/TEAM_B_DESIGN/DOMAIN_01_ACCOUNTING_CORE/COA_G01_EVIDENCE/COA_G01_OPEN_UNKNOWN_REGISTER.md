# COA-G01 — Open Unknown Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Consolidate every open unknown/evidence gap relevant to COA-G01 from all reconciled sources | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT` folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED | None of these items are closed by this session; closing any of them requires new evidence, not reclassification |

Rule enforced throughout: **Do not convert UNKNOWN into FACT.**

## From the actual Team A residual-unknowns register (`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md`, 11 items total — not 20; see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-04)

| ID | Description | COA-G01 relevance | Status |
|---|---|---|---|
| G-06 | `l10n_th_withholding_tax_multi` depends on `account_payment_multi_deduction`, not present anywhere in the tree; WHT multi-deduction behavior unverifiable | Directly relevant — Thai WHT capability partially unobservable, affects `COA_G01_THAI_RELEVANCE_REGISTER.md` and downstream `COA-G06` | OPEN |
| Q-01–Q-04, G-05, G-07–G-11 | Other Team A open items (non-COA, e.g. Docker/database restore, non-Thailand module scope) | Not directly COA-relevant per this session's review | OPEN (carried forward, not re-examined in depth) |

## From local `STATE03` evidence-gap and open-item registers

| ID | Description | Status |
|---|---|---|
| OI-001 / GAP-005 | S1 Thai statutory report specification — route authorization vs. execution status itself in conflict (see C-03) | BOSS_DECISION_REQUIRED / HOLD |
| OI-004 | Generic WHT engine dependency ruling (`l10n_account_withholding_tax`) needed | OPEN |
| OI-005 | 8 residual localization modules require disposition | OPEN |
| OI-006 | PND1 payroll WHT scope needs a ruling | OPEN |
| OI-008 / GAP-002 | Approved DOCX template not found; documentation release blocked | BLOCKED |
| GAP-001 | STEP0303R2 execution artifact — register says missing, filesystem shows it exists (see C-02) | CONFLICTING EVIDENCE |
| GAP-003 | GitHub evidence synchronization — later local STEP artifacts not confirmed present in GitHub search/index | PARTIAL / HOLD |
| GAP-004 | PR #53 vs PR #58 Independent Review status conflict | CONFLICTING EVIDENCE (carried forward, not re-adjudicated) |

## New unknowns surfaced by this session's own reconciliation (not previously registered anywhere)

| ID | Description | Status |
|---|---|---|
| N-01 | Whether the Boss-approved `Odoo18` workbook source file itself (not just its extracted inventory) should be committed to GitHub or the local `ACCOUNT` folder for full traceability — it was not found as a standalone file in either location during this session. | UNKNOWN |
| N-02 | Whether the local S1–S11 / T1–T9 findings and the `STEP0303R2`–`R5` rulings should be ported into the GitHub `SMEsPlus` branch, and if so, in what form (verbatim vs. re-authored under the lettered `BOSS_GATE` convention). | UNKNOWN — requires Boss decision on porting scope and method |
| N-03 | Whether the B14 Clean-Room Provenance Matrix should be extended with a dedicated pass over the three `COA_STANDARD` documents, or whether a new, separate clean-room check artifact should be created for COA-specific work going forward. | UNKNOWN — see `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` |
| N-04 | Whether route (a) (Thai Revenue Department published forms) or a fresh route (b) execution (real black-box observation with populated data) should be pursued to close the Thai financial-statement presentation evidence gap (class F). | UNKNOWN — requires Boss decision on which route to authorize and fund |
| N-05 | Whether the `STEP0303R2` self-contradiction (C-02) reflects a lost/overwritten local file history, a search-tooling error in the prior session, or a genuinely separate artifact that was never indexed — the cause has not been established. | UNKNOWN |

## Items explicitly NOT re-opened by this session

- The 19 active Account Types Boss ruling — treated as settled target design, not reopened.
- The `~32` Base Kernel working expectation — treated as a working expectation, not reopened or re-estimated.
- SI-01 through SI-10 themselves — treated as settled Boss-approved control invariants; this session evaluates *compliance evidence against them* (see `COA_G01_SAAS_INVARIANT_COMPLIANCE.md`), it does not renegotiate the invariants.
