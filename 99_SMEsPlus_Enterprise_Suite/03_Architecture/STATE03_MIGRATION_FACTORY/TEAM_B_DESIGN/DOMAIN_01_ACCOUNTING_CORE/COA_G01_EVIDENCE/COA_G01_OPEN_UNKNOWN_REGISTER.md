# COA-G01 — Open Unknown Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Consolidate every open unknown/evidence gap relevant to COA-G01 from all reconciled sources | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT` folder | 2026-08-30 22:27 +0700 (historical — see CORR3 current-state line below) | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED (historical, Round 1 snapshot) | None of these items are closed by this session *(historical, Round 1 statement — no longer current, see below)*; closing any of them requires new evidence, not reclassification |

**CORR3 current-state correction (2026-08-31, finding `AUD2-03`):** the header row above is preserved as the accurate Round 1 (2026-08-30) snapshot — it is **not** current. As of CORR2 (2026-08-31, commit `a4cebfc`), **N-03 is `RESOLVED`**; **N-01, N-02, N-04, N-05 remain `OPEN`** — open N-series count was **4** at CORR3. **Superseded by CORR4 (see the CORR4 section below): N-01 and N-02 are now also `RESOLVED`; current open N-series count = 2 (N-04, N-05).**

Rule enforced throughout: **Do not convert UNKNOWN into FACT.**

## ROUND 2 UPDATE (2026-08-31): 11-vs-20 scope reconciliation (closes `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-04)

Two distinct, correctly-scoped registers exist, not one contradictory count:

| Register | File | Scope | Count | Composition |
|---|---|---|---|---|
| Program-level Unknown/Gap register | `TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md` | Whole-project (module restore, dump freshness, rights/ownership) — NOT Domain-01-specific | **11** | `Q-01`–`Q-04`, `G-05`–`G-11` |
| Domain-01 residual unknown register (deep synthesis) | `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/11_RESIDUAL_UNKNOWN_REGISTER.md` | Domain-01 Accounting Core only, after the Sonnet deep-synthesis pass | **20** | 9 carried forward + 11 new (`GAP-D01-14..24`) − 3 partially resolved − 1 permanently uncloseable (stated verbatim: `"TOTAL OPEN AFTER THIS ROUND = 20"`) |

Neither figure is wrong; they measure different populations. Of the 11 program-level items, only `G-06` (WHT multi-deduction dependency) is COA-relevant, per the table below. Of the 20 Domain-01 items, the COA-relevant subset is smaller still — most (e.g. `GAP-D01-15` hard-lock-date reversal, `GAP-D01-21` concurrency control) concern posting-engine/ledger mechanics rather than Chart-of-Accounts structure. This register does not re-enumerate all 20 here (they belong to the Domain-01 research pack, cited by reference); it records that the scope question is closed.

## From the actual Team A residual-unknowns register (`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md`, 11 items total — program-wide scope, see Round 2 update above and `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-04)

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

## Round 2 status of N-01..N-05 (2026-08-31)

All five reconfirmed **OPEN** at the close of Round 2 — none closed by Round 2, each requires a Boss decision or new primary evidence this session cannot manufacture: N-01 (workbook file itself unrecoverable — independently reconfirmed by whole-volume search, see `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md`), N-02 (local-evidence porting scope/method), N-03 (clean-room coverage extension method — at Round 2 close, described as "more urgent" because the coverage gap had temporarily grown to 4 documents; corrected below), N-04 (which route closes Class F), N-05 (cause of the `STEP0303R2` self-contradiction, C-02 — unresolved).

## CORR2 status of N-03 (2026-08-31)

**RESOLVED.** The "grew from 3 to 4" description above is stale: the 4th document (`c530138`) was deleted by the repository owner's commit `58ab36d`, confirmed independently — current `COA_STANDARD/` count is 3 (see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07, `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` CORR2 section). N-03's actual question — "should B14 be extended, or should a new, separate clean-room check artifact be created" — is answered by this session's own conduct: **option (b)** was taken. `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` is that dedicated artifact, now providing document-level coverage for all 3 current documents. B14 itself was explicitly not modified. This resolves the *decision* (which path); it does not claim B14-level completeness or independent verification — those remain open per `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` CORR2 part 6. N-01, N-02, N-04, N-05 remain **OPEN**, unchanged by CORR2.

## CORR4 status of N-01, N-02, N-04, N-05 (2026-08-31)

- **N-01 = `RESOLVED`.** The Boss-approved `Odoo18` workbook file was recovered by direct Google Drive file ID, downloaded, independently SHA-256 hashed (exact match), and its content independently parsed and cross-checked row-by-row against the existing GitHub extraction — zero discrepancies. See `COA_G01_PRIMARY_SOURCE_RECOVERY_REGISTER_R4.md` §1. The raw binary itself is intentionally not committed to GitHub, per Boss's own N-01 disposition (access-controlled Drive only) — this is not a residual gap, it is the ruled disposition.
- **N-02 = `RESOLVED`.** All 63 files across S1–S11, T1–T9, and `STEP0303R2`–`R5` (plus their two parent evidence packs) were security-scanned, ported byte-for-byte, and independently re-hashed with zero mismatches. See `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`.
- **N-04 = `OPEN`, reclassified `ACCESS_DENIED`.** Boss provided a specific Drive file ID for the Thai financial-statement example; both `get_file_metadata` and `read_file_content` returned "not found" on the connected account. Not classified as nonexistent; no substitute evidence fabricated. See `COA_G01_THAI_FINANCIAL_STATEMENT_PRESENTATION_SOURCE_R4.md`.
- **N-05 = `OPEN`.** The `STEP0303R2` chronology is now fully reconstructed from primary timestamps (see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-02, `COA_G01_STEP0303R2_CONTRADICTION_RECONCILIATION_R4.md`) — existence is settled, but **the cause of the original search miss remains genuinely `UNKNOWN`** and is not converted to fact.

**Current open N-series count = 2 (N-04, N-05).** N-01, N-02, N-03 are `RESOLVED`.

**CORR5 current-state disposition (2026-08-31, finding `AUD4-01`):** raw fact status above is unchanged — N-04 and N-05 remain `OPEN`. For Gate-blocker-set purposes, `COA_G01_CURRENT_BLOCKER_AND_DISPOSITION_MATRIX_R5.md` records the canonical current classification: **N-04 = `CURRENT COA-G01 BLOCKER`**; **N-05 = `ACCEPTED RESIDUAL UNKNOWN — BOSS DECISION REQUIRED`** (existence resolved per C-02 above; cause remains genuinely `UNKNOWN` and is not converted to fact by this reclassification — only its Gate-disposition label changes, from being listed alongside N-04 as an undifferentiated blocker to being explicitly routed to Boss decision).

## Items explicitly NOT re-opened by this session

- The 19 active Account Types Boss ruling — treated as settled target design, not reopened.
- The `~32` Base Kernel working expectation — treated as a working expectation, not reopened or re-estimated.
- SI-01 through SI-10 themselves — treated as settled Boss-approved control invariants; this session evaluates *compliance evidence against them* (see `COA_G01_SAAS_INVARIANT_COMPLIANCE.md`), it does not renegotiate the invariants.
