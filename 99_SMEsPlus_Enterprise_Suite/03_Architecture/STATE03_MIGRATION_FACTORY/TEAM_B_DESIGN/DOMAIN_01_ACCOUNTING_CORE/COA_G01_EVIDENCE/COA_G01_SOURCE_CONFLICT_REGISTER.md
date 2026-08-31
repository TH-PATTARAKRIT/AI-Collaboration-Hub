# COA-G01 — Source Conflict Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Register every conflict found between evidence sources during COA-G01 remediation | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | GitHub `SMEsPlus` branch; local `ACCOUNT` folder | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED — unresolved conflicts below | Blocks PROPOSED PASS until each conflict is adjudicated or explicitly accepted as a known residual |

None of the conflicts below have been resolved by this session. Resolution requires Boss adjudication or a dedicated evidence-gathering step; they are registered, not closed.

## C-01 — GitHub and local evidence bases have diverged (CONFLICTING EVIDENCE / MAJOR)

The GitHub `SMEsPlus` branch's `BOSS_GATE`, `TEAM_A`, and `TEAM_B_DESIGN` evidence makes no mention of the local `STATE03` architecture findings (S1–S11), the Thai localization toolchain findings (T1–T9), or the `STEP0303R2` through `STEP0303R5` Boss toolchain rulings — all of which exist, dated and evidenced, in the local `SMEsPlus ENTERPRISE SUITE/ACCOUNT` working folder outside this repository. Per session control, "GitHub is the project Source of Record," yet substantive frozen evidence currently exists **only** locally and has never been committed.

- Impact: Findings directly relevant to SI-01/SI-02 (S5: Tenant → Company → Tax Branch model) and SI-10 (S1/S4: Thai statutory logic must live in versioned data/localization layer, not hard-coded core) are not visible to anyone reviewing only the GitHub record.
- Status: **HOLD / EVIDENCE REQUIRED.** This register does not port the local findings into GitHub beyond citing them (see `COA_G01_THAI_RELEVANCE_REGISTER.md` and the AQ ruling, §4) — a full port/reconciliation is a distinct remediation task requiring Boss authorization on how much local material becomes committed evidence.

## C-02 — `STEP0303R2` existence is self-contradicted in local records

Local file `STATE03_DETAILED_FOLLOWUP/STATE03_BOSS_REVIEW_SUMMARY.md` and three sibling registers state: *"No STEP0303R2 execution artifact was found locally or in the current GitHub evidence search."* However, a fully populated local folder `01 ACCOUNT/STEP0303R2_BOSS_TOOLCHAIN_RULING_SELECTION_GATE/` exists with 11 files, including a recorded Boss ruling (`BOSS_TOOLCHAIN_RULING_RECORD.md`, dated 2026-08-24) — and its filesystem timestamps (22:23–22:25) **predate** the follow-up registers that claim it is missing (22:29–22:40, same day).

- Status: **CONFLICTING EVIDENCE — unresolved anomaly.** This session does not adjudicate why the follow-up registers missed an artifact that already existed in the same parent directory. Flagged for Boss/PMO review; not silently resolved in either direction.

## C-03 — S1 (Thai statutory report specification) status conflict

`STATE03_DETAILED_FOLLOWUP` (dated 2026-08-24) records S1 as `BOSS_DECISION_REQUIRED` / open. A later local artifact, `STEP0303R5_PLANNING_BASELINE_CLOSURE/STEP0303R5_FINAL_STATUS.md` (dated 2026-08-24, but part of a sequence continuing through 2026-08-28), records: *"S1 = CLOSED — BOSS AUTHORIZED PLANNING BASELINE... Approved route: ROUTE (b) — black-box observation... Scope: PLANNING BASELINE AUTHORISATION ONLY."*

- Both are local-only (see C-01) and neither has been committed to GitHub.
- Even under the later "closed" status, route (b) (black-box observation) is authorized only at the planning level and has **not been executed** — the one database dump checked (`iTEST02`) contained 6 journal entries and zero withholding-tax certificates, insufficient to serve as real financial-statement evidence.
- Status: **HOLD / EVIDENCE REQUIRED.** Treat S1 as "planning-baseline authorized, evidence not yet produced" rather than either "open" or "resolved" — neither local label alone is accurate for a Gate-level record.

## C-04 — Residual unknown count mismatch ("20" vs. actual register of 11) — **RESOLVED IN ROUND 2 (2026-08-31)**

Multiple GitHub governance documents (`AH_BOSS_FINAL_GATE_RULING.md`, PMO/ChatGPT audit docs) cite a "Team A residual unknowns" figure, and `AH_BOSS_FINAL_GATE_RULING.md` itself already flags this figure as requiring reconciliation: *"the residual register currently contains a declared summary total that requires reconciliation against the individually enumerated open/partially-open IDs... RESIDUAL UNKNOWN COUNT = RECONCILIATION REQUIRED."* Direct inspection of the actual register (`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md`) finds **11** enumerated items (`Q-01`–`Q-04`, `G-05`–`G-11`), not 20, and the number "20" does not appear anywhere in that file.

- **Round 1 status (superseded):** CONFLICTING EVIDENCE — flagged but not traced to source.
- **Round 2 resolution:** Traced. The "20" figure originates from a *different, Domain-01-specific* document: `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/11_RESIDUAL_UNKNOWN_REGISTER.md`, which states verbatim: `"TOTAL OPEN AFTER THIS ROUND = 20"` (9 items carried forward from Part 1 + 11 new items `GAP-D01-14..24`, after 3 partial resolutions and 1 permanently-uncloseable item). The **11**-item register (`09_OPEN_QUESTIONS/`) is **program-wide** (module restore, dump freshness, rights/ownership — not Domain-01-specific). The **20**-item register is **Domain-01 Accounting-Core-specific**, produced by a later, deeper research pass than the 11-item register. These are two genuinely different documents at two different scopes, not one register miscounted.
- Status: **RESOLVED — different scopes confirmed, not a contradiction.** Both figures are individually correct for what they each measure. Downstream Gates citing "Team A residual unknowns" should specify which register they mean going forward. Full detail: `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md` Q-03.

## C-05 — Independent Review historical conflict (pre-existing, carried forward)

`STATE03_EVIDENCE_GAP_REGISTER.csv` (GAP-004, local) already records: PR #53 states Independent Review complete; a later PR #58 states it PENDING. The local register notes Boss's `STEP030210` Conditional Pass is treated as controlling regardless of this discrepancy. This session did not independently verify PR #53/#58 against GitHub (out of COA-G01 scope) and simply carries the conflict forward as previously logged, per the instruction not to silently resolve pre-existing conflicts.

- Status: **CARRIED FORWARD, NOT RE-ADJUDICATED.**

## C-06 — Clean-room provenance matrix does not cover the COA_STANDARD documents

`B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` records overall Critical Vendor-Derived Design Risk = 0 and is marked COMPLETE, but its 16-row matrix contains **zero** entries citing any of the three `COA_STANDARD` documents (`DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`, `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`, `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`) or Account Type taxonomy work. Only one row addresses COA at all, and it covers template/instance sharing generally (citation `GAP-D01-05`), not these three documents.

- Status: **HOLD / EVIDENCE REQUIRED.** See `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` for the detailed gap analysis. This is not treated as a clean-room *violation* (no vendor-derived risk was found where B14 did look) — it is treated as a **coverage gap**: the specific COA_STANDARD artifacts have not yet been run through a dedicated clean-room check.

**CORR2 status update (2026-08-31):** the phrase "three COA_STANDARD documents" above is, and always was, the correct current-branch count (the finding briefly described 4 during the `c530138` window; that file is now deleted — see C-07). All 3 have since been run through a dedicated clean-room check (`COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`, CORR2 section): 2 `VERIFIED CLEAN-ROOM BOUNDARY`, 1 closed this session by adding an explicit source-column disclaimer. **B14 itself remains unmodified and still does not cover any of the 3** — this finding's core claim (B14 non-coverage) is unchanged and still accurate. Status remains **HOLD / EVIDENCE REQUIRED**: the dedicated review is not yet independently re-verified, and B14's own coverage gap is a standing, deliberate-choice condition, not something CORR2 closes.

## C-07 — Commits `c530138`/`8fceca0` self-declare COA-G01 PASS with no independent review trail (new, Round 2, 2026-08-31)

Between the Round 2 remediation prompt being published (commit `157a496`, 00:16:52) and this Round 2 session starting, two commits were pushed by the same author/committer, unsigned, 20 seconds apart: `c530138` (adds `COA_STANDARD/DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md`, asserting inline `"ChatGPT Independent Evidence Review = PASS / VERIFIED FOR COA-G01 SCOPE"`) and `8fceca0` (updates the `AL` evidence index to state `"COA-G01 blocking evidence gaps = 0"`).

Investigation findings (full detail: `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`):
- No separate ChatGPT audit artifact exists anywhere in `CHATGPT_AUDIT/` for this claim (that directory's last COA-G01-relevant activity predates Round 2 by hours).
- No PMO artifact exists in `PMO_VERIFICATION/` for this claim.
- No Jira comment exists on `ERPPLUS-132` for this claim — breaking this project's own established pattern of a matching Jira comment for every prior GitHub evidence push.
- The document does not address any of the AR record's R/E/Q findings by ID, and does not resolve C-01, C-02, or C-06 above.
- It adds a fourth, still-uncovered document to the `COA_STANDARD/` clean-room coverage gap (C-06).
- Its claim of having "directly re-verified" the Odoo18 workbook "in connected Drive" is unaccompanied by any extraction artifact, hash, or log (see `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md` §5).

- Status: **CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT**, per explicit Boss/user control instruction. Both commits are preserved unmodified in this session's own history — not deleted, reverted, or renamed by this session. Neither commit's PASS declaration is used as COA-G01 closure evidence. This is not a claim of bad faith; it is a claim that independent verification for this specific declaration does not exist anywhere in the evidence base.

**CORR1 update (2026-08-31): independently confirmed by the project owner.** Commit `58ab36d6f8cd70843553de01be892e444ea7b784` ("Revert accidental WEBSITE-session write to SMEsPlus," pushed 2026-08-31 08:07:09 +0700, outside this session) deletes the exact file `c530138` added (`COA_STANDARD/DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md`, 266 lines removed). The commit message states plainly that this content was an accidental write from an unrelated "WEBSITE" session onto the `SMEsPlus` branch. This **confirms** (does not merely leave open) that the file's provenance was not a genuine COA-G01 remediation product — it independently corroborates this register's `CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT` classification from the outside, via the repository owner's own action, not this session's inference alone. `8fceca0`'s index-update text (which described that now-deleted file as complete/PASS) is correspondingly stale and was already corrected by this session's Round 2 pass regardless of this external revert. Both `c530138` and `8fceca0` remain in git history (git history is immutable evidence); only the file content they introduced was reverted, by the repository owner, not this session.

**CORR2 current-vs-historical clarification (2026-08-31):** to remove any ambiguity — **historically**, `c530138` added a file, and this register's investigation (above) describes what was found while that file existed. **Currently** (as of this CORR2 pass and confirmed by direct listing), that file does not exist in `COA_STANDARD/`; the classification `CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT` is retained as this register's permanent record of that historical episode, not as a description of any file presently on the branch. `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`'s CORR2 section makes the same distinction explicitly (its parts 1–2).
