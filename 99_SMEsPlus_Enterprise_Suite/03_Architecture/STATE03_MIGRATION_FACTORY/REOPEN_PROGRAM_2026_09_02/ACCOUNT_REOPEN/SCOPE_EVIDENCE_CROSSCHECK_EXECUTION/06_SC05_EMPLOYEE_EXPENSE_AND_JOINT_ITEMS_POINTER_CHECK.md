# 06 — SC-05 EMPLOYEE EXPENSE / TAX RETURNS / CASH ROUNDINGS / WT CERTIFICATES / JOINT ITEMS POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-05` |
| Decision ID | `ACC-DEC-008` |
| Topic | Employee expenses (HR→Accounting), Tax Returns closing menu, Cash Roundings, WT Certificates menu, manufacturing valuation, price difference, inventory write-down (`113900`) |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` (required, source pack); `A1_BENCHMARK_MENU_TREE_EVIDENCE_iTEST02.md` §C item 4 (deep-study); `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md` "Unresolved objections," items 5–6 (deep-study, file numbering local to that package — not this session's file `08`); `04_ACCOUNT_PROCESS_HANDOFF_MAP.md` row `HO-31` (deep-study) |
| Evidence pointer result | Verified |
| Owner status | Boss (HR-expense/Tax Returns/Cash Roundings/WT Certificates sub-items); Joint / UNASSIGNED (manufacturing valuation/price difference/write-down sub-items) |
| Gate impact | No gate defined / Joint (split, as both required registers state) |
| GL impact known? | Partial — `HO-31` confirms employee-expense postings exist conceptually ("expense + employee payable... Approval; VAT/WHT where applicable") but marks the handoff `UNVERIFIED (this session reading only)`; the manufacturing/price-difference/write-down sub-items are documented as GL-impacting valuation events in the Inventory-side map (`M-STK-06`/`M-STK-08` in the deep-study `08_STOCK_COGS_ACCOUNT_BOUNDARY_MATRIX.md`) but not yet Account-side designed |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | PL: Yes for manufacturing/price-difference/write-down (COGS and variance lines); Tax Report: Yes for Tax Returns / WT Certificates sub-items (these are literally tax-filing-adjacent menus); BS: Unknown; Cash Flow: No |
| Subledger or interface impact | Inventory (manufacturing valuation, price difference, write-down); N/A for HR-expense/Tax Returns/Cash Roundings/WT Certificates (Accounting Core, not a subledger) |
| Thai menu/report communication issue | Yes — `A1` §C item 5 separately notes "`WT Certificates` and `Withholding Tax` and `WT Income Tax Report` have **no Thai translation** in the instance although they are the Thailand-specific menus — a UX-fitness finding for TBRAC," directly touching this row's WT Certificates sub-item |
| AI Audit SMEsPlus objection | This row bundles seven distinct sub-items behind one Decision ID with two different owner tracks (Boss scope vs. Joint Session 3); a single IN/OUT/DEFERRED ruling cannot resolve it — Boss must rule per sub-item, which both required registers already state ("Boss rules per sub-item") but which is easy to misread as one ruling if this row is skimmed |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` (HR-expense, Tax Returns, Cash Roundings, WT Certificates sub-items) and `READY AFTER JOINT_SESSION` (manufacturing valuation, price difference, write-down sub-items) — **split**, not a single classification |
| Next action | Boss rules on the four Boss-track sub-items directly; the three Joint-track sub-items are simultaneously carried in `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` agenda items 6–7 and cannot close from the Account side alone |

## Detail

Both required registers cite "source `05` row `ACC-DEC-008`; source `A1` §C.4; source `08` objections 5–6; source `04` HO-31." All four sub-pointers were checked:

- **`A1` §C.4** — resolves outside the required perimeter to `A1_BENCHMARK_MENU_TREE_EVIDENCE_iTEST02.md` §C item 4, which lists benchmark-tree extras "NOT in Boss list," explicitly including "**Tax Returns**... **Cash Roundings**... **Employee Expenses, WT Certificates**." This is a precise, on-point match to four of this row's named sub-items. **Verified.**
- **`08` objections 5–6** — resolves to `08_STOCK_COGS_ACCOUNT_BOUNDARY_MATRIX.md`'s "Unresolved objections noticed" list (numbering local to that file, not this session's own file `08`): objection 5 is "SC-20 (inventory write-down / allowance `113900`) has a Thai template account but no benchmark process and no owner in any Inventory register — a scope hole"; objection 6 is "Manufacturing (SC-09) is installed in the benchmark and named an `ACCOUNTING_INTERFACE_REQUIREMENT` by Inventory, but is absent from Boss Section 6 — scope decision required." Both are precise, on-point matches to this row's write-down and manufacturing sub-items, including the exact chart account `113900` cited in this row's own topic description. **Verified.**
- **`04` HO-31** — resolves to `04_ACCOUNT_PROCESS_HANDOFF_MAP.md` row `HO-31`: "Employee expense report -> expense + employee payable (HR -> Accounting)... Owner `UNASSIGNED`... Status `SCOPE QUESTION — BOSS DECISION`... `HOLD`," with a closing note "**HO-31 (HR expense)** — surfaced from the benchmark instance; not in Boss Section 6; scope question only." A precise, on-point match. **Verified.**

All four sub-pointers resolve and topically support the row. The row-level result is **Verified**, with the caveat (shared with every SC row) that the deepest citation layer sits outside this session's required source perimeter — see `01_SOURCE_PACKAGE_VERIFICATION_REGISTER.md` §B.

`07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` (a required input) independently corroborates the split-ownership structure: agenda item 6 ("Manufacturing") and item 7 ("Price difference") are both cross-referenced "also surfaced in `05` (`ACC-DEC-008` / SC-05)," and the brief explicitly states it "does not close SC-05 sub-items (manufacturing, price difference, write-down) from the Account side — those remain routed to both `05` (Boss scope ruling) and this Joint agenda simultaneously, since ownership itself is one of the Joint questions." No discrepancy found between the required inputs on this point.
