# 05 — SC-04 TREASURY / CASH & BANK EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-04` |
| Decision ID | `ACC-DEC-007` |
| Topic | Treasury / Cash & Bank (bank journals, statements, reconciliation, cheques, PromptPay, bank feeds) |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §B (required, source pack); `02_ACCOUNT_MENU_COVERAGE_REGISTER.md` rows `M-BNK-01..08` (deep-study package); `18_AI_AUDIT_SMEPLUS_9_SPECIAL_TEAM_CHALLENGE.md` row `ST-03` (deep-study package) |
| Evidence pointer result | Partial |
| Owner status | Unassigned (Treasury role — Boss to assign) |
| Gate impact | No gate defined |
| GL impact known? | Yes — `M-BNK-05` states explicitly: "Bank/cash movements post to `asset_cash` accounts; outstanding receipts/payments and suspense accounts bridge timing," citing `l10n_th` chart rows `111100`/`111200`/`111201`/`111202` |
| TB impact known? | Unknown — no source explicitly traces bank/cash lines through to a Trial Balance presentation rule |
| BS / PL / Cash Flow / Tax Report impact known? | BS: Yes (Bank and Cash is a Balance Sheet category per `09_FINANCIAL_STATEMENT_REPORTING_MAP.md` row `M-RPT-01`, cross-referenced from `10` §C); PL: No; Cash Flow: Yes (`M-RPT-03` "Bank and Cash category movements... classification is driven by account tags"); Tax Report: N/A |
| Subledger or interface impact | Treasury (this is precisely the gap `10` §B and the Boss decision queue describe: "a neighbour never designed") |
| Thai menu/report communication issue | Unknown — Thai labels exist for each `M-BNK` row (e.g. `เพิ่มบัญชีธนาคาร`, `รายการเดินบัญชีธนาคาร`) but none has gone through TBRAC; not flagged as a distinct objection in `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md` as read |
| AI Audit SMEsPlus objection | The `18` `ST-03` citation ("6 ownerless handoff families," mirrors `VC-03`) is a *general* ownerless-handoffs finding, not a Treasury-specific one on its face — this session located and read the anchor but could not, from the fragment read, independently confirm Treasury is one of the six named families without reading `18` in full; flagged as the reason for the `Partial` verdict below |
| Readiness classification | `READY AFTER OWNER ASSIGNED` |
| Next action | Boss assigns a named Treasury owner in `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §B; once assigned, research scope is already fully specified (bank journals, Thai bank statement formats, reconciliation rules, cheques, PromptPay, bank feeds, and — notably — a PDPA review that `10` §B flags as "a compliance dimension not covered elsewhere in this package and should not be dropped") |

## Detail

Both required registers cite "source `05` row `ACC-DEC-007`; source `02` M-BNK-*; source `18` ST-03" (Batch A phrasing) / "`02` M-BNK-*; `18` ST-03" (source-pack phrasing). "Source `02` M-BNK-*" resolves outside the required perimeter to `02_ACCOUNT_MENU_COVERAGE_REGISTER.md`, which carries eight fully-populated `M-BNK-01`..`M-BNK-08` rows (bank account creation, bank transactions, reconciliation models, online sync, GL impact, AR/AP clearing, reconciliation status, unreconciled aging) — a strong, on-point match; every row is independently marked `UNVERIFIED (this session reading only)` or a HOLD/GAP/PARTIAL status by the deep-study package itself, i.e. it does not overstate its own findings either.

"Source `18` ST-03" resolves to `18_AI_AUDIT_SMEPLUS_9_SPECIAL_TEAM_CHALLENGE.md`, section header "`ST-03` — Process ownership audit: ownerless handoffs (mirrors `VC-03`)" and a summary-table row "`ST-03` | 6 ownerless handoff families | `VC-03`." The anchor **exists**, but this session's targeted fetch did not capture the full `ST-03` section body (only the header and one summary row), so it cannot independently confirm Treasury is explicitly named among the "6 ownerless handoff families" from what was read — hence **Partial**, not **Verified**, for this specific sub-citation. This is disclosed rather than assumed resolved.

This is independently corroborated within the required source pack: `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §B states plainly "Treasury — UNASSIGNED... B03 names Treasury as a neighbour never designed; bank items in this package are HOLD," which matches the `GAP OWNER ROUTING REQUIRED` status carried by both required registers.
