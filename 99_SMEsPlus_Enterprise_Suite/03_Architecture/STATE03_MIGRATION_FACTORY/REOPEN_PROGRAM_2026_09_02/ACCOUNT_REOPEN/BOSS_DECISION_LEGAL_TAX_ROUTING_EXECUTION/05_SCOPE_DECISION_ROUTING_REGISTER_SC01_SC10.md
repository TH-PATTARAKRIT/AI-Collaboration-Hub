# 05 — SCOPE DECISION ROUTING REGISTER (SC-01..SC-10)

| Field | Value |
|---|---|
| Source | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §B |
| Decision IDs | `ACC-DEC-004` through `ACC-DEC-013` |
| Rule | Per governing-prompt §7 and Charter §9: this session **cannot add scope**. Each row below only routes an existing scope question already surfaced in the source package to Boss; it does not resolve, expand, or narrow any item. |

| Decision ID | SC ID | Item present in benchmark / implied by menus but not scoped | Source | Owner | Gate Impact | Status | Scope options for Boss | Recommended next action |
|---|---|---|---|---|---|---|---|---|
| `ACC-DEC-004` | SC-01 | Fixed assets, depreciation, disposal (Boss lists them; no COA gate covers them) | 12 UK-02 | Boss | No gate defined | `BOSS DECISION REQUIRED` | IN (assign a gate) / OUT (explicitly deferred) / DEFERRED to a later phase | If IN, feed into `10` §AR/AP + Fixed Asset research pass |
| `ACC-DEC-005` | SC-02 | Deferred revenues/expenses and recognition schedules (models absent in instance) | 12 UK-04 | Boss | No gate defined | `BOSS DECISION REQUIRED` | IN / OUT / DEFERRED | If IN, feed into `10` §AR/AP + Fixed Asset research pass |
| `ACC-DEC-006` | SC-03 | Budgets / budgetary positions / budget analysis (module not installed in instance) | 13 UK-03 | Boss | No gate defined | `BOSS DECISION REQUIRED` | IN / OUT / DEFERRED | If IN, assign a Team A/B research owner (currently none) |
| `ACC-DEC-007` | SC-04 | Treasury / Cash & Bank (bank journals, statements, reconciliation rules, cheques, PromptPay, bank feeds) — neighbour never designed | 02 M-BNK-*; 18 ST-03 | Boss (assign owner) | No gate defined | `GAP OWNER ROUTING REQUIRED` | Assign named owner (Treasury role, currently UNASSIGNED) | See `10` §Treasury / Cash & Bank routing |
| `ACC-DEC-008` | SC-05 | Employee expenses (HR→Accounting), Tax Returns closing menu, Cash Roundings, WT Certificates menu, manufacturing valuation, price difference, inventory write-down (113900) | A1 §C.4; 08 objections 5–6; 04 HO-31 | Boss | No gate defined / Joint | `BOSS DECISION REQUIRED` | Split ruling likely needed: manufacturing valuation / price difference / write-down route to Joint Session 3 (`07`); HR-expense, Tax Returns, Cash Roundings, WT Certificates route to Boss scope ruling | Boss rules per sub-item; Joint-relevant sub-items also appear in `07` |
| `ACC-DEC-009` | SC-06 | VAT and CIT ownership (Accounting Core vs separate Tax domain) — undecided since prior session; PND1/PND54/PP36 in chart but not in scope | 10 objections 7, 9; prior VC-06 | Boss | `COA-G06` | `BOSS DECISION REQUIRED` | Accounting Core owns VAT/CIT / a separate Tax domain owns VAT/CIT / split by form | Feeds `06_LEGAL_TAX_REVIEW_BRIEF.md` — the review brief covers all forms regardless of eventual ownership split |
| `ACC-DEC-010` | SC-07 | Approval-before-posting workflow (`ACC-004` draft) — in or out | 14 OBJN-07 | Boss | `CO-02` | `BOSS DECISION REQUIRED` | IN / OUT | If IN, Team B designs at `CO-02` once unblocked |
| `ACC-DEC-011` | SC-08 | Analytic / dimension model ownership (no Team B neighbour named); branch (สาขา) as dimension vs statutory attribute | 13 objections 2, 4 | Boss / Legal-Tax | `COA-G07` | `GAP OWNER ROUTING REQUIRED` + `LEGAL_TAX_REVIEW_REQUIRED` | Assign owner; branch statutory-status question routes to legal-tax review | See `06` §Branch (สาขา) statutory status |
| `ACC-DEC-012` | SC-09 | Financial Reporting design owner (statement production is OUT neighbour, not designed) | 09 RU-08 | Boss | `COA-G05` | `GAP OWNER ROUTING REQUIRED` | Assign named Team B owner | See `10` §Financial Statement Taxonomy dependency routing |
| `ACC-DEC-013` | SC-10 | Standard COA template mechanics (`B13 DT-03`) — still unapproved | 17 VC-05 | Boss | `COA-G04S` | `BOSS DECISION REQUIRED` | APPROVE / REJECT / MODIFY | Boss rules; carries forward from a prior round, not new to this session |

## Notes

- These are the same 10 items recorded in source `20` §B, unchanged in substance. This register only adds a stable Decision ID, an explicit options list, and a routing pointer into this package's other briefs.
- No item above is resolved by this session. "Recommended next action" describes *routing*, not a scope conclusion.
- Items with a Joint Session 3 dimension (part of SC-05) are cross-referenced in `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` — they are not closed from either side per governing-prompt §7.
