# 11 — SC-10 STANDARD COA TEMPLATE MECHANICS EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-10` |
| Decision ID | `ACC-DEC-013` |
| Topic | Standard COA template mechanics (`B13 DT-03`) — still unapproved |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` row `VC-05` (deep-study, lines 65–69, 105, 128) |
| Evidence pointer result | Verified |
| Owner status | Boss |
| Gate impact | `COA-G04S` |
| GL impact known? | Yes — the chart-of-accounts template underlies every GL posting; this is structurally certain even though the approval decision itself is pending |
| TB impact known? | Yes — same reasoning; TB is a direct roll-up of GL accounts defined by the template |
| BS / PL / Cash Flow / Tax Report impact known? | Yes for BS/PL (chart structure determines statement-line mapping, per the `COA-G05` dependency chain in `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §C); Cash Flow/Tax Report: Unknown |
| Subledger or interface impact | N/A directly, though `VC-05`'s own evidence-inspected list touches `M-BNK` (bank/cash) and `OBJ-53`, i.e. the template question has downstream subledger dependents |
| Thai menu/report communication issue | Unknown — not addressed by the `VC-05` fragment read |
| AI Audit SMEsPlus objection | This item "carries forward from a prior round, not new to this session," per both required registers — it is the oldest unresolved item among the ten `SC` rows; an objection worth surfacing to Boss is simply that of the ten items, this is the one with the least excuse for remaining open, since it does not depend on any other unresolved gate the way `SC-09` or `SC-06` do |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` |
| Next action | Boss rules APPROVE / REJECT / MODIFY on `B13 DT-03` in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` |

## Detail

Both required registers cite "source `05` row `ACC-DEC-013`; source `17` VC-05." "Source `17` VC-05" resolves outside the required perimeter to `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md`:

> `## VC-05` — EXPERT IESA / ERP & SaaS System Integrity
> **Evidence inspected:** `02` M-CFG-06/11/12, M-JRN-07, M-BNK-04; `03` OBJ-53; `14` §1 CTL-10, §6; `B09` CO-09/CO-10; prior AI Audit `VC-05`/`ST-08`.
>
> (summary table) `VC-05` | `HOLD / EVIDENCE REQUIRED` | template mechanics, branch, reporting owner

The summary-table row's own gloss — "template mechanics, branch, reporting owner" — lines up directly with this row's topic ("Standard COA template mechanics") and, incidentally, cross-references the same two neighboring open items this cross-check found for `SC-08` (branch) and `SC-09` (reporting owner), suggesting the deep-study package itself treated these three as a related cluster. This session's targeted fetch captured the `VC-05` header, its evidence-inspected list, and its summary-table verdict, but not a full prose body for `VC-05` (the file is organized as VETO-seat headers `VC-01`..`VC-09` followed by a consolidated table) — the verdict row itself, however, is the operative citation and was read in full. **Verified.**

No discrepancy found between the two required registers and this anchor.
