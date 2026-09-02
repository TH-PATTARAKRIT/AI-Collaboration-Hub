# 18 — AI AUDIT SMEsPlus: 9 SPECIAL TEAM CHALLENGE

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / L999.999` |
| Document status | `PROCESS REFERENCE ONLY` — challenge record; not a Gate PASS, not a Final Solution, not development/production authorization |
| Ai Audit structure | `Ai Audit SMEsPlus = 9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Roles Overlay` — three separate layers, kept in files 17 / 18 / 19 |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` `Open ERP / Odoo = Process Benchmark Only.` `SMEsPlus = New Thai Business Process Design Candidate, not final solution.`

## 0. Activation and rule

Special Teams investigate only the material delta (Charter §3, §7). Each team below re-performed the load-bearing evidence behind one Council concern (file 17) against the three mandatory files (02/03/04) and the relevant deep-dive file; duplicate historical questions (G01 baseline exists, Boss sole approver, clean-room absolute, no scope expansion by challenge) are suppressed. Findings return to Council/Boss; no team votes itself into execution authority.

## ST-01 — Audit / Evidence: internal consistency of 02 / 03 / 04 (mirrors VC-01)

**Re-performance:** counted rows and checked cross-references by script — 98 menu rows (02) = 98 Part B rows (03); 53 object rows (03 Part A); 31 handoffs (04); every `Handoff to next process` in 02/03 resolves to an `HO-nn` or `M-xxx`; no blank cell; statuses identical across 02/03 by construction; one factual defect found and corrected before publication (tax template count 17 -> 18).
**Finding:** Internally consistent; consistency is by generation, not by independent check. Nine deep-dive files add sub-IDs (SC-, RC-, TP-, UK-, OBJN-, RU-) that are not back-referenced from 02/03/04 — traceability is one-directional (deep file -> core file).
**Classification:** `CARRY FORWARD — WITH PRECISION NOTE`. **Gate impact:** none. **Next:** independent re-count by ChatGPT audit role; optional back-reference index in a later revision.

## ST-02 — Thailand reality: authoritative-source audit (mirrors VC-02)

**Re-performance:** searched every deliverable for authoritative Thai citations (Revenue Code sections, RD notifications, DBD rules, TFAC/TFRS texts). Result: **zero primary citations**; all Thai statutory statements carry `LEGAL_TAX_REVIEW_REQUIRED`; the only Thai-language sources are the LGPL `l10n_th` template names, the benchmark's installed translations, and the STATE04 draft ACC-001. Inventory reopen file 12 relays TFAC/TAS 2 and tax-adviser web sources for consumables/WHT, which file 08 reuses **as relayed**, not verified.
**Finding:** The Thai process reference is Thai in language and structure, not yet in statutory anchoring. The naming register's audience labels (accountant / owner / tax filer) are this session's assumption.
**Classification:** `CONFIRMED GAP`. **Gate impact:** COA-G05/G06 HOLD. **Next:** file 22 items 3 and 5.

## ST-03 — Process ownership audit: ownerless handoffs (mirrors VC-03)

**Re-performance:** for each of the 31 handoffs, checked whether a Team B deliverable, Boss ruling, or named team owns the receiving side.

| Handoff family | Owner found? | Evidence | Disposition |
|---|---|---|---|
| HO-01..HO-06 configuration/posting | Accounting Core (B02) | B02/B03 | owned |
| HO-07..HO-10, HO-13 GL/reconciliation/TB | Accounting Core; reconciliation UI black-box | PR-05; MP-12 | owned (principle), behaviour HOLD |
| HO-11, HO-12 bank | **none** (Treasury "not designed", B03 §3) | file 02 M-BNK-* | `GAP OWNER ROUTING REQUIRED` |
| HO-14, HO-15, HO-18, HO-23 inventory | Joint Session 3 (ERPPLUS-140) | INV-20 | routed, not owned by Account |
| HO-16, HO-17 assets/deferrals | **none** (no gate) | file 12 UK-02 | `BOSS SCOPE DECISION` |
| HO-19..HO-22 close/FY/RE | Accounting Core (CAP-04/09) | B02/B07 | owned |
| HO-24..HO-28 tax | Accounting/Tax (WHT branch) — VAT/CIT ownership **undecided** | VC-06 prior | partly ownerless |
| HO-29 analytic | **none** (B03 does not name analytic as neighbour) | file 13 objection 4 | `GAP OWNER ROUTING REQUIRED` |
| HO-30 audit trail | Accounting Core (CAP-08) | B02 | owned |
| HO-31 HR expense | **none** (not in Boss scope) | A1/A2 | `BOSS SCOPE DECISION` |
| Posting-architecture fork | "Accounting-owned" per Inventory; no Account deliverable | INV-20 §6 | `GAP OWNER ROUTING REQUIRED` |

**Classification:** `CONFIRMED GAP` (6 ownerless families). **Gate impact:** none moved; routing required. **Next:** Boss decision batch (file 22 item 1).

## ST-04 — Identity / reconciliation: subledger and opening-balance re-performance (mirrors VC-04)

**Re-performance:** traced OBJ-44 (opening balance) and OBJ-15/16/26/27/32 (AR/AP/WHT/asset subledgers) through 07 and 09 RC-13: the tie-out target is now stated as Raw Cumulative TB (G1) as of cutover; for subledgers, no mechanism, no research, no rehearsal exists (G-B5, GAP-D01-11). The Thai template `999999` current-year-earnings placeholder has no counterpart in the derived-RE model (B07 §1e); MG-C15 requires exactly one designated RE account — the template offers `321200 กำไรสะสม` and `999999` simultaneously.
**Finding:** Migration reconciliation can be specified at GL/TB level only; subledger identity is unspecified; the 999999/321200 designation is a concrete COA-G03 / MG-C15 decision waiting to be made.
**Classification:** `CONFIRMED GAP`. **Gate impact:** MG-C11 unsatisfiable today; Joint G-5 open. **Next:** file 22 item 6; Boss decision on RE designation at COA-G03.

## ST-05 — Period close / retained earnings: does the process map contradict Rounds 2–7? (mirrors VC-06 close items)

**Re-performance:** compared 04 HO-19..HO-23 and 14 §2 checklist against B02 CAP-04/CAP-09, B07 §1d/§1e, B10 MG-C03/C16. No contradiction: monthly close = posting lock only; FY close posts no entry; RE derived at elapsed boundary; opening balances as ordinary entries; implicit carry-forward. Two additions introduced by this package are candidates, not contradictions: (a) an inventory-valuation close step sequenced with the accounting close (from CORR-007B 08), (b) a hard/irreversible lock after statutory filing (file 14 OBJN-06), which Team B has not designed.
**Classification:** `CARRY FORWARD — VERIFIED` with two candidate extensions `HOLD`. **Gate impact:** CAP-09/COA-G08 unchanged. **Next:** Joint Session 3 (a); Team B decision (b).

## ST-06 — Account x Inventory boundary scenarios (mirrors VC-03/VC-04 inventory items)

**Re-performance:** checked that file 08's 23 scenarios and 11 Joint-only items match Inventory reopen files 14/20 and CORR-007B 08/09 verbatim in ownership; confirmed no Account-side row closes an Inventory or Joint item; confirmed the return-valuation basis is `CONFLICTING` inside Inventory (C-03) and is not adjudicated here. New Account-side facts contributed: `TH-INV-03` was deferred to COA-G06, but COA-G06 as defined by Boss AK does not cover costing methods (file 08 objection 4); inventory write-down account 113900 has a template account but no process owner in either domain (objection 5); manufacturing and price difference are live in the instance but absent from Boss Section 6 (objection 6).
**Classification:** `CARRY FORWARD — WITH PRECISION NOTE`; three new scope holes `GAP OWNER ROUTING REQUIRED`. **Gate impact:** Joint backbone publication blocked (unchanged). **Next:** Joint Session 3 agenda (file 22 item 4) to include the three holes.

## ST-07 — WHT / VAT / CIT re-performance (mirrors VC-06 tax items)

**Re-performance:** re-read the 18 tax templates and 5 tax groups; re-checked A2 installed list for `l10n_th_withholding_tax_multi` (absent) and `account_payment_multi_deduction` (present); re-read WHT branch 05 §2/§5/§6. Confirmed: (a) purchase-side WHT process is the only tax process with test-backed benchmark evidence; (b) sales-side WHT has no grid, no certificate tracking, no test; (c) tax-group closing accounts net purchase-side liabilities against sales-side assets (new error finding, file 10 §2.2); (d) exempt input VAT template maps to the "entitled to deduction" grid contrary to its own Thai description; (e) Undue VAT accounts (114100/213100) exist with no tax template and no process; (f) PND1/PND54/PP36 exist in the chart and nowhere in scope; (g) CIT has no benchmark process at all.
**Classification:** `CONFIRMED GAP` (VAT, CIT, sales WHT, tax-group netting, Undue VAT); ACC-WHT-06 `HIGH` unchanged (Boss standing ruling). **Gate impact:** COA-G06 HOLD. **Next:** legal-tax review (file 22 item 3); Boss module-baseline decision; Boss scope ruling on VAT/CIT ownership and on PND1/PND54/PP36.

## ST-08 — SaaS / isolation / reporting-owner (mirrors VC-05)

**Re-performance:** checked whether any deliverable in the Account chain designs Financial Reporting, Treasury, Analytic or Assets: none (B03 §3 lists Reporting, Treasury, Budgeting as OUT/IN neighbours "not designed here"; Assets/Analytic are not named at all). Checked template mechanics: B13 DT-03 still "not approved". Checked branch: `l10n_th_partner` adds a Thai branch code used on PND output (STEP040304 FE5) — branch is already a statutory attribute on WHT filings in the benchmark, supporting file 13's concern that สาขา is not merely a dimension.
**Classification:** `HOLD / EVIDENCE REQUIRED` (template, branch treatment, four undesigned neighbour domains). **Gate impact:** COA-G04S/G07 HOLD. **Next:** Boss assigns owners (file 22 items 1, 7, 8).

## ST-09 — Clean-room / AI reproducibility re-performance (mirrors VC-08/VC-09)

**Re-performance:** (a) grep of the 25 deliverables for forbidden terminal words used as SMEsPlus conclusions — none found outside quoted prior statuses and explicit "not X" statements (see file 24 check log); (b) verified that no file under the OUTPUT folder contains source-code bodies (no `def `, no `class `, no `<record` blocks except the 12-line data snippet quoted from the WHT branch inside file 10, which is itself a relayed register quote of an LGPL data file); (c) verified the scratchpad dump extraction produced only three metadata tables and that the temporary dump copy no longer exists; (d) confirmed files 02/03/04 regenerate byte-identically from the JSON registers; (e) confirmed sub-agent authored files each end with a "Consistency and limits" section (tail check) — partial-write risk from the two rate-limit interruptions not realised.
**Classification:** `CARRY FORWARD — VERIFIED`; one item `HOLD` (Boss acknowledgment of docker-based metadata extraction as within read-only authorization). **Gate impact:** none. **Next:** Boss acknowledgment; ChatGPT independent read of prose files.

## Special Team consolidated return to Council

| Team | Result | Returned to |
|---|---|---|
| ST-01 | consistent by generation; one-directional traceability | VC-01 |
| ST-02 | zero authoritative Thai citations | VC-02 |
| ST-03 | 6 ownerless handoff families | VC-03 |
| ST-04 | subledger identity unspecified; 999999 vs 321200 designation open | VC-04 |
| ST-05 | close/RE model not contradicted; 2 candidate extensions | VC-06 |
| ST-06 | Joint items intact; 3 new scope holes | VC-03/VC-04 |
| ST-07 | 7 tax findings incl. tax-group netting error | VC-06 |
| ST-08 | 4 undesigned neighbour domains; branch is statutory on WHT | VC-05 |
| ST-09 | no leakage; extraction authorization to acknowledge | VC-08/VC-09 |

No Special Team declares any gate movement. All returns are `HOLD / EVIDENCE REQUIRED`, `CONFIRMED GAP` or `CARRY FORWARD` as stated.
