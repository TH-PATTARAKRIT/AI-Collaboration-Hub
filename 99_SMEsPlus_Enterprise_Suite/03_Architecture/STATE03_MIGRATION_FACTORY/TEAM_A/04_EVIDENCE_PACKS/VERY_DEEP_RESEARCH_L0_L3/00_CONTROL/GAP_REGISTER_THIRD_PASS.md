# STATE03 Gap Register — Third-Pass Update
## DEEPSEEK-REPORTED / DIAGNOSTIC ONLY
## Date: 2026-10-02
## Base: STATE03_SECOND_PASS_GAP_REGISTER.tsv (45 gaps)
## Update: Third-pass closure review against U100–U114

> **DISCLAIMER:** Gap status, closure evidence, and risk assessments are DEEPSEEK-REPORTED/DIAGNOSTIC.
> No formal gate pass, V-level assignment, or Boss approval is asserted.
> "CLOSED" means a third-pass unit produced DEEPSEEK-REPORTED/MECHANICAL-GATE evidence for the gap.
> Runtime gaps remain OPEN until AWT provisioning.

---

## Summary

| Status | Count |
|--------|-------|
| CLOSED by U70–U114 | 20 |
| OPEN — runtime required | 6 |
| OPEN — governance decision | 4 |
| OPEN — evidence gap remaining | 5 |
| OPEN — partially addressed | 10 |
| **Total** | **45** |

---

## Gap Register

| Gap-ID | Module(s) | G Group | Description | Priority | C1-material-risk | Proof-layer-missing | Evidence-unit | Status |
|--------|-----------|---------|-------------|----------|-----------------|--------------------|--------------|----|
| GAP-001 | account | G01 | Lock date enforcement — ValidationError on locked period write not proven | P0 | Yes — fiscal compliance | P1/P3 | U70 | **CLOSED by U70** — `_check_fiscalyear_lock_date()` ValidationError confirmed; group_account_manager bypass documented |
| GAP-002 | account | G01 | MCT-F02 intercompany journal generation — cross-company automation not runtime verified | P0 | Yes — multi-entity books | P1/P4 | U71 | PARTIAL — U71 confirmed `account_payment_interco` present Community 19; source studied; L9 runtime not proven |
| GAP-003 | stock | G06 | MCT-F05 warehouse-company binding — ir.rule enforcement not runtime proven | P0 | Yes — inventory isolation | P1/P3 | U71,U99 | PARTIAL — U71 confirmed domain patterns; U99 confirmed sudo() bypasses all ir.rules; runtime P2 NOT_PROVEN |
| GAP-004 | account | G01 | RCN-F02 backdating audit trail — immutability of posted entry under date change | P0 | Yes — audit integrity | P1/P3 | U73 | **CLOSED by U73** — SHA-256 hash chain `$4$<sha256hex>` confirmed; `button_draft()` blocked if hash set |
| GAP-005 | stock_account | G06 | GRV-F04 perpetual inventory valuation at receipt — SVL creation under perpetual=True | P0 | Yes — inventory valuation | P1/P3 | U72,U80 | **CLOSED by U72/U80** — perpetual path traced; SVL→account.move creation path confirmed; note: `product.value` model replaces old SVL in Odoo 19 |
| GAP-006 | account | G01 | PCO-F03 month-end stock closing — accrued-orders wizard full flow | P0 | Yes — period accounting | P1/P3 | U75 | **CLOSED by U75** — accrued_orders_wizard.py full flow traced; period accounting entries confirmed |
| GAP-007 | purchase | G08 | GRV-F06 three-way match — bill control enforcement | P0 | Partial — Community soft only | P1/P3 | U74 | **CLOSED by U74** — FINDING: hard 3-way match (`module_account_3way_match`) is ENTERPRISE-ONLY; Community has soft `qty_invoiced` check only; documented as Community limitation |
| GAP-008 | account,sale,stock | G01/G05/G06 | O2C closed-loop reconciliation — receivable account reconciliation end-to-end | P1 | Yes — revenue completeness | P1/L11 | U76 | **CLOSED by U76** — full O2C chain traced at L5/L11; receivable reconciliation confirmed |
| GAP-009 | account,purchase,stock | G01/G08/G06 | P2P closed-loop reconciliation — AP reconciliation and inventory asset closing | P1 | Yes — payables completeness | P1/L11 | U77 | **CLOSED by U77** — full P2P chain traced at L5/L11; payable reconciliation confirmed |
| GAP-010 | mrp,stock,account | G07/G06/G01 | MRP full lifecycle — BOM to MO to consumption to FG to account close | P1 | Yes — cost of goods | P1/L5 | U78 | **CLOSED by U78** — mrp.production action_produce + mrp_account close entries confirmed |
| GAP-011 | stock_account | G06/G01 | RCN-F03 SVL origin tracking — AVCO recomputation on return immutability | P1 | Yes — valuation integrity | P1/P3 | U80 | **CLOSED by U80** — SVL create/recompute path confirmed; account link field traced |
| GAP-012 | account_edi_ubl_cii | G04 | UBL/CII format mapping depth — field-by-field XML mapping not studied at L3 | P1 | Yes — e-invoice compliance | L3 | U82 | **CLOSED by U82** — invoice line mapper methods studied; full send/receive flow confirmed |
| GAP-013 | account_tax_python | G01/G02 | Python formula tax eval() — security validation not proven | P1 | Yes — tax calculation integrity | L7/L12 | U98 | **CLOSED by U98** — 3 independent RCE blocks confirmed: AST whitelist + safe_eval blacklist + no env/ORM context |
| GAP-014 | point_of_sale | G11 | POS session close → account.move generation — L4 cross-module not proven | P1 | Yes — POS reconciliation | P1/L4 | U85 | **CLOSED by U85** — pos_session.action_pos_session_closing_control → account.move traced; reconciliation confirmed |
| GAP-015 | account_payment | G03 | Payment webhook delivery — webhook→account.move posting runtime NOT_PROVEN | P1 | Yes — payment completeness | P2/runtime | U94 | PARTIAL — U94 studied source; runtime webhook delivery still NOT_PROVEN (P2 gap remains) |
| GAP-016 | account_peppol | G04 | account_peppol — full PEPPOL registration/credential/send/receive at L3 | P1 | No | L3 | U82 | **CLOSED by U82** — PEPPOL models studied; proxy communication flow confirmed |
| GAP-017 | mrp_subcontracting | G07 | Subcontracting cross-module chain — purchase→stock→mrp not proven at L4 | P1 | Yes — outsourced manufacturing | P1/L4 | U83 | **CLOSED by U83** — subcontracting flow traced; MO auto-created at PO confirmation (not receipt) documented |
| GAP-018 | account | G01 | MCT-F03 shared vs per-company COA isolation — runtime proof not proven | P1 | Yes — chart of accounts | P1/P2 | U71 | PARTIAL — U71 studied `company_id` domain; `parent_of` operator for config records confirmed; runtime isolation P2 NOT_PROVEN |
| GAP-019 | (unknown) | G05 | U55 evidence completely missing — zero claims coverage hole | P0 | Yes — coverage integrity | All | U95 | **CLOSED by U95** — 8 sale bridge modules covered: sale_crm, sale_loyalty, sale_management, sale_margin, sale_mrp, sale_product_matrix, sale_project, sale_stock |
| GAP-020 | auth_passkey | G15 | Auth passkey WebAuthn — full registration/authentication UI flow at L2/L3 | P2 | No | L2/L3 | U108 | **CLOSED by U108** — WebAuthn controllers, passkey CRUD, security group gate confirmed at L2/L3 |
| GAP-021 | account | G01 | Bank reconciliation widget — account/static/src/js logic JS runtime NOT_PROVEN | P1 | Yes — bank reconciliation | P2/runtime | U81 | OPEN — U81 studied Python backend; JS reconciliation widget remains P2 NOT_PROVEN (AWT required) |
| GAP-022 | stock_landed_costs | G06 | Landed cost allocation — GRV-F05 split methods and SVL adjustment cross-module | P1 | Yes — cost allocation | P1/L4 | U96 | **CLOSED by U96** — `_check_landed_cost + action_validate` traced; split methods and account.move confirmed |
| GAP-023 | account | G01 | Cash basis accounting — `tax_cash_basis_journal_id` path not proven | P1 | Yes — cash basis compliance | L3/config | U101 | **CLOSED by U101** — `_get_cash_basis_lines`, cash basis move creation traced; journal_id config path confirmed |
| GAP-024 | multiple | All | U01–U46 MECHANICAL_ONLY — ~18,000 claims without semantic review | P1 | Moderate — fabrication risk | Semantic | All second-pass | OPEN — systematic semantic review not performed; risk accepted as DIAGNOSTIC limitation |
| GAP-025 | hr_expense | G09 | Expense chain — hr.expense → hr.expense.sheet → account.move → analytic | P2 | No | P1/L4 | U91 | **CLOSED by U91** — expense chain traced; note: hr.expense.sheet REMOVED in Odoo 19 Community (flat model confirmed) |
| GAP-026 | website_sale | G12 | Website sale checkout→payment→sale.order cross-module chain | P2 | No | P1/L4 | U89 | **CLOSED by U89** — website_sale checkout flow traced; payment integration confirmed |
| GAP-027 | account | G01 | Tax report locking — lock prevents re-export or re-compute not proven | P2 | No | L7 | U31 second pass | OPEN — tax report period lock logic not proven at L7; proposed for U-prop in third-pass plan |
| GAP-028 | account | G01 | SDV-F07 Return after invoicing via credit note — immutability chain | P1 | Yes — credit note integrity | P1/L8 | U81 | PARTIAL — U81 studied `_reverse_move`; credit note-to-return-stock-move account link studied but L8 immutability not fully proven |
| GAP-029 | sale_stock | G05/G06 | SDV-F05 COGS timing — exact moment of COGS account.move relative to delivery | P1 | Yes — revenue recognition | P1/L8 | U84 | **CLOSED by U84** — COGS timing at delivery validation confirmed; SVL-to-move sequence proven |
| GAP-030 | stock | G06 | Multi-step routing 3-step runtime behavior — execution NOT_PROVEN | P2 | No | P2/runtime | RT Backlog | OPEN — source logic studied by U08/U106; runtime sequence NOT_PROVEN (AWT required) |
| GAP-031 | account_edi | G04 | account.edi.document state machine — NEW→TO_SEND→SENT/ERROR cross-module | P2 | No | P1/L4 | U82 | **CLOSED by U82** — state machine `_process_documents` traced; proxy client link confirmed |
| GAP-032 | account_tax_python | G01/G02 | Python tax formula adversarial — L12 red team not run | P1 | Yes — RCE risk assessment | L12 | U98 | **CLOSED by U98** — 3-layer defense confirmed; residual governance risk (authorized user can write wrong formula) documented |
| GAP-033 | all modules | G15 | Migration scripts — ir.module.module.migrate() paths not studied | P1 | Yes — upgrade integrity | L10 | U102 | **CLOSED by U102** — pre/post migration hook patterns across modules confirmed; field rename/merge patterns documented |
| GAP-034 | multiple | G10–G16 | U47–U68 Function-ID unmapped — capability coverage for G10–G16 unknown | P2 | No | F-ID | All P2 units | OPEN — second-pass units added coverage but comprehensive F-ID mapping not completed |
| GAP-035 | l10n_* (all non-Thai) | G16 | 226+ l10n_* modules have no canonical G-group assignment | P2 | No | Governance | Governance decision | OPEN — governance: l10n_* assigned G16 in MODULE_G_CROSSWALK.tsv; formal decision pending |
| GAP-036 | test_* | G16 | 41 test_* modules in 692 denominator — no business function | P3 | No | Governance | Governance decision | OPEN — governance: test_* assigned G16; denominator freeze decision pending |
| GAP-037 | theme_* | G16 | 30 theme_* modules in 692 denominator — website themes | P3 | No | Governance | Governance decision | OPEN — governance: theme_* assigned G16; denominator freeze decision pending |
| GAP-038 | pos_restaurant | G11 | pos_restaurant floor plan/split order — L3 depth insufficient | P2 | No | L3 | U105 | **CLOSED by U105** — floor.plan, restaurant.table, split order, course ordering fully studied at L3 |
| GAP-039 | mail | G13 | Mail gateway incoming email — alias routing runtime NOT_PROVEN | P2 | No | P2/runtime | RT Backlog | OPEN — U113 studied mail.thread/activity; gateway runtime delivery P2 NOT_PROVEN (AWT required) |
| GAP-040 | account_peppol_response | G04 | account_peppol_response — 0 claims, completely unstudied | P2 | No | L3 | U104 | **CLOSED by U104** — PEPPOL response XML parsing, document status update, error handling fully studied |
| GAP-041 | payment (all providers) | G15/G03 | Payment provider integration — webhook/callback runtime NOT_PROVEN for all 22+ providers | P1 | Yes — eCommerce deployment | P2/runtime | U94 | PARTIAL — U94 studied Stripe/PayPal source; runtime webhook still NOT_PROVEN; other providers not studied at L3 |
| GAP-042 | stock_picking_batch | G06 | Batch picking cross-module chain at L4 — action_done | P2 | No | P1/L4 | U93 | **CLOSED by U93** — `stock.picking.batch.action_done` cross-module chain confirmed |
| GAP-043 | account | G01 | Fiscal position mapping — tax/account mapping edge cases not proven | P2 | Yes (TH) — Thai VAT 0%/7% | L3/config | U107 | **CLOSED by U107** — Thai fiscal position `map_tax` confirmed for 0%/7%; intra-company fiscal position studied |
| GAP-044 | hr_work_entry | G09 | hr.work_entry → payroll cross-module — Community payroll boundary | P2 | No | P1/L4 | U88 | **CLOSED by U88** — Community payroll ABSENT confirmed; hr_work_entry→payslip link exists in Enterprise only; boundary documented |
| GAP-045 | multiple | All | U47–U68 GATE_PASS_ONLY — 22 units × ~130 claims with zero semantic review | P1 | Moderate — fabrication risk | Semantic | All P2 second-pass | OPEN — systematic semantic review not performed; same as GAP-024 scope extension |

---

## Third-Pass New Gaps (Identified During U100–U114)

| Gap-ID | Module(s) | G Group | Description | Priority | C1-material-risk | Proof-layer-missing | Evidence-unit | Status |
|--------|-----------|---------|-------------|----------|-----------------|--------------------|--------------|----|
| GAP-046 | l10n_th_withholding_tax | G02 | Thai WHT (ภ.ง.ด.) PND form generation — PND-1/3/53 form production not proven at L3 depth beyond U100 breadth scan | P0 | Yes — Thai statutory WHT | L3/P3 | U100 | OPEN — U100 confirmed module present; full PND form generation logic not at L3 |
| GAP-047 | stock_account, mrp_account | G06/G07 | WIP journal entries from MRP close — `_get_production_account` and WIP account routing | P1 | Yes — manufacturing cost | P1/L4 | U115-prop | OPEN — No unit studied mrp_account WIP accounting; queued as U115 |
| GAP-048 | account | G01 | Multi-currency unrealized FX on year-end — `_get_adjustment_entry` for open balances at fiscal year close | P1 | Yes — balance sheet accuracy | P1/L3 | U103 | PARTIAL — U103 studied multi-currency; year-end FX adjustment entry at fiscal close specifically not traced |
| GAP-049 | digest | G14 | KPI digest cron + ir.actions.server pattern — `digest.digest._compute_kpis` and mail cron trigger | P2 | No | L3 | U117-prop | OPEN — digest studied superficially in U01; full cron chain not studied |
| GAP-050 | account_deferred (if present) | G01 | Deferred revenue/expense — amortization schedule and account.move generation | P2 | No | L3 | U118-prop | OPEN — module not studied; deferred revenue accounting not in existing evidence |

---

*DIAGNOSTIC ARTIFACT — Not Gate PASS — Not Boss Approval — Not Formal Coverage — Not STATE03 Complete*
*All gap status: DEEPSEEK-REPORTED / MECHANICAL-GATE-ONLY*
