# 10 — RESEARCH ROUTING: AR/AP + FIXED ASSET, TREASURY, FINANCIAL STATEMENT TAXONOMY

| Field | Value |
|---|---|
| Source | `22_NEXT_PROMPT_RECOMMENDATION.md` §2 items 6, 7, 8; `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` EG-06, EG-07, SC-04, SC-09 |
| Status | `HOLD / EVIDENCE REQUIRED` (all three tracks) |

Three independent research/design tracks are grouped in this single file because they are all **pending routes, not yet started**, and each depends on prior gates rather than on each other — they can be commissioned in parallel once owners are named.

## A. AR/AP + Fixed Asset research pass (Team A style)

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-004` / `ACC-DEC-005` (scope), this section (research routing) |
| Owner | Team A (research) — UNASSIGNED |
| Why now | Source `22` #6: "Menus mapped but behaviour black-box; migration reconciliation cannot be signed off" |
| Unblocks | `MG-C11` subledger tie-out; `P0-10` |
| Prior open item | Source `20` EG-06 notes this ties to a still-open prior item, "G-B5" |

Required research scope (per source `22` #6 and `20` EG-06):

- AR aging semantics (bucket definitions, as-of-date handling)
- AP aging semantics (bucket definitions, as-of-date handling)
- Allowance for doubtful accounts — recognition and release mechanics
- Write-off process — approval chain, GL impact, tax deductibility interaction (cross-reference `06` CIT-2)
- Subledger tie-out at cutover — how AR/AP subledgers reconcile to GL at migration cutover (this is the `MG-C11` dependency)
- Asset register roll-forward — opening balance, additions, disposals, depreciation run, closing balance reconciliation
- Deferral schedules — recognition timing for deferred revenue/expense (cross-reference `05` `ACC-DEC-005` / SC-02 scope ruling — this research should not proceed on deferred-revenue mechanics until SC-02 scope is ruled IN)

**Sequencing note:** the AR/AP aging and write-off research can start immediately (no scope gate blocks it). The deferral-schedule and fixed-asset sub-scopes should wait for `ACC-DEC-004`/`ACC-DEC-005` (SC-01/SC-02) scope rulings, since source `20` records those areas as **not yet scoped at all** ("no COA gate covers them").

## B. Treasury / Cash & Bank process reference

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-007` (owner assignment) |
| Owner | Treasury — UNASSIGNED |
| Why now | Source `22` #7: "B03 names Treasury as a neighbour never designed; bank items in this package are HOLD" |
| Unblocks | `HO-11` / `HO-12` |

Required research scope (per governing-prompt §3 item 7 and source `22` #7):

- Bank journals — structure and posting mechanics
- Statement import formats of Thai banks (which banks, which formats — CSV/MT940/proprietary)
- Reconciliation rules (matching logic, tolerance handling)
- Cheque handling
- PromptPay handling
- Bank-transfer handling
- Bank-feed availability in the Thai market (does any Thai bank offer a live feed API SMEsPlus could integrate with, vs. manual statement import only)
- PDPA (Thailand's Personal Data Protection Act) review of any bank-data handling — this is a compliance dimension not covered elsewhere in this package and should not be dropped

**Note:** this track has no dependency on any other item in this package and can be commissioned immediately once an owner is named.

## C. Financial statement taxonomy dependency routing (`COA-G05`)

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-012` (owner assignment, SC-09) |
| Owner | Team B — but **only once `COA-G01`–`COA-G04` clear** |
| Why now (i.e., why route now even though it can't start now) | Source `22` #8: this item is explicitly **sequenced after** items 2 (`COA-G01` unblock, `09`) and 3 (legal-tax review, `06`) |
| Depends on | `COA-G01` closure (see `09`) **and** DBD statement-format evidence (see `06` §D, items DBD-1/DBD-2) |
| Gate Impact | `COA-G05` |

Scope, once unblocked (per source `22` #8):

- Map the 19 Boss-approved canonical account types to Thai NPAE statement lines
- Resolve the Off-Balance rule (source `20` OB-06: "Off-Balance rule 5 — engine must distinguish active type from included-in-statements — has no design artefact")
- Resolve mode-label handling (referenced in source `22` #8; no further detail available in the reviewed source files — Team B should locate the originating reference before starting)

**This track must not start before `06` (legal-tax review) returns DBD statement-format evidence and `09` (COA-G01 unblock) is resolved.** Starting early risks designing against unverified statutory assumptions, repeating the same defect already found in the benchmark's own contradictory VAT template (`06` VAT-3).

## Cross-track dependency summary

```
COA-G01 unblock (09)  ──┐
                         ├──>  Financial Statement Taxonomy (C, above)  ──> COA-G05
Legal-tax review (06)  ──┘

AR/AP + Fixed Asset research (A, above)  ──>  MG-C11 subledger sign-off  (independent of the above)

Treasury / Cash & Bank (B, above)  ──>  HO-11 / HO-12  (independent of the above)
```
