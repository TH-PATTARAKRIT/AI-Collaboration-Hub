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

## C-04 — Residual unknown count mismatch ("20" vs. actual register of 11)

Multiple GitHub governance documents (`AH_BOSS_FINAL_GATE_RULING.md`, PMO/ChatGPT audit docs) cite a "Team A residual unknowns" figure, and `AH_BOSS_FINAL_GATE_RULING.md` itself already flags this figure as requiring reconciliation: *"the residual register currently contains a declared summary total that requires reconciliation against the individually enumerated open/partially-open IDs... RESIDUAL UNKNOWN COUNT = RECONCILIATION REQUIRED."* Direct inspection of the actual register (`TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md`) finds **11** enumerated items (`Q-01`–`Q-04`, `G-05`–`G-11`), not 20, and the number "20" does not appear anywhere in that file.

- Status: **CONFLICTING EVIDENCE — already flagged upstream, now independently confirmed.** This session does not overwrite the "20" figure used elsewhere; it records that the primitive register itself supports only 11 as of this reading. See `COA_G01_OPEN_UNKNOWN_REGISTER.md` for the full list.

## C-05 — Independent Review historical conflict (pre-existing, carried forward)

`STATE03_EVIDENCE_GAP_REGISTER.csv` (GAP-004, local) already records: PR #53 states Independent Review complete; a later PR #58 states it PENDING. The local register notes Boss's `STEP030210` Conditional Pass is treated as controlling regardless of this discrepancy. This session did not independently verify PR #53/#58 against GitHub (out of COA-G01 scope) and simply carries the conflict forward as previously logged, per the instruction not to silently resolve pre-existing conflicts.

- Status: **CARRIED FORWARD, NOT RE-ADJUDICATED.**

## C-06 — Clean-room provenance matrix does not cover the COA_STANDARD documents

`B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` records overall Critical Vendor-Derived Design Risk = 0 and is marked COMPLETE, but its 16-row matrix contains **zero** entries citing any of the three `COA_STANDARD` documents (`DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`, `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`, `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`) or Account Type taxonomy work. Only one row addresses COA at all, and it covers template/instance sharing generally (citation `GAP-D01-05`), not these three documents.

- Status: **HOLD / EVIDENCE REQUIRED.** See `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` for the detailed gap analysis. This is not treated as a clean-room *violation* (no vendor-derived risk was found where B14 did look) — it is treated as a **coverage gap**: the specific COA_STANDARD artifacts have not yet been run through a dedicated clean-room check.
