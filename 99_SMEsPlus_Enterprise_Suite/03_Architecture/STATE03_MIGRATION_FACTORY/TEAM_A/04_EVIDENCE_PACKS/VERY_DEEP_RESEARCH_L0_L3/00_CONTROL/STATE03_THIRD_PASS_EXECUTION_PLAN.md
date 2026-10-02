# STATE03 VDR — Third-Pass Execution Plan
## DIAGNOSTIC ARTIFACT — NOT GATE PASS — NOT BOSS APPROVAL
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

**Produced by:** Main controller session
**Date:** 2026-10-02
**Basis:** START_STATE03_THIRD_PASS_RESEARCH directive; updated per MANDATORY_NEXT_PLAN_REPORTING_EFFECTIVE_NOW (2026-10-02)
**Scope:** U100–U119+ targeting Partial/Not-Proven/C1 gaps from gap register and second-pass residuals

**Reporting format (mandatory from U105 onwards):** Every unit completion report must include: (1) Current Status, (2) Next Plan, (3) Queue Visibility (next 5 units), (4) Blockers. Continue automatically after gate pass — stop only for real blocker or explicit Boss instruction.

---

## Selection Criteria

Units selected per directive:
1. Candidate Modules/Functions marked Partial, Not Proven, or lacking C1/Source/Configuration trace
2. Priority: Thai Tax, multi-company, security, accounting, inventory, sales, purchase, manufacturing, POS
3. Do NOT alter U01–U99; do NOT create new denominator/formal coverage claim

---

## Live Status Table — U100–U119

> Last updated by: Claude session (continuous third-pass execution)

| Unit | Module / Capability Scope | Priority | C1 Impact | Source Gap | Research Focus | Status |
|------|--------------------------|----------|-----------|------------|----------------|--------|
| U100 | l10n_th + l10n_th_withholding_tax — Thai VAT + WHT | P0 | Yes (TH) | NOT_STUDIED | Thai VAT 7%, WHT rates, tax report, ภ.ง.ด. form types | Done 7303819e |
| U101 | account — cash basis accounting (GAP-023) | P0 | Yes | NOT_PROVEN | tax_cash_basis_journal_id, _get_cash_basis_lines, cash basis move creation | Done 66d12714 |
| U102 | Migration scripts — hook patterns across modules (GAP-033) | P0 | Yes | NOT_STUDIED | migrations/ folders, pre/post migrate hooks, field rename/merge patterns | Done 5e594e8e |
| U103 | account — multi-currency revaluation + forex gain/loss | P1 | Yes | NOT_PROVEN | currency_id on account.move.line, _get_adjustment_entry, unrealized FX | Done 6f2d1594 |
| U104 | account_peppol_response — response handling (GAP-040) | P1 | No | NOT_STUDIED | PEPPOL response XML parsing, document status update, error handling | Done f70431ca |
| U105 | pos_restaurant — table/floor management deep (GAP-038) | P1 | No | PARTIAL | floor.plan, restaurant.table, split order, course ordering | Done 82aa031a |
| U106 | stock — replenishment (orderpoint, procurement rule, make-to-order) | P1 | No | NOT_PROVEN | stock.warehouse.orderpoint, _run_scheduler, route MTO vs reorder | Done 55bc06c5 |
| U107 | account — fiscal position Thai edge cases (GAP-043) | P1 | Yes (TH) | NOT_PROVEN | map_tax for Thai VAT 0%/7%, fiscal.position.template, intra-company | Done 075eed50 |
| U108 | auth_passkey — WebAuthn registration/auth flow L2/L3 (GAP-020) | P1 | No | PARTIAL | WebAuthn controllers, passkey CRUD, security group gate | Done e903ae5b |
| U109 | account.analytic.plan — multi-plan hierarchy deep | P1 | No | NOT_PROVEN | analytic.plan tree, mandatory % validation, cross-module distribution | Done 2d57e3c6 |
| U110 | stock — lot/serial traceability + account impact | P1 | No | NOT_PROVEN | stock.lot FIFO/AVCO interaction, lot-level valuation, removal strategy | Done 74d7ffa5 |
| U111 | account_budget — budget control (if Community) | P2 | No | NOT_STUDIED | crossovered.budget, budget.line, account.budget.post | Done 1d439378 (ABSENT — Enterprise-only) |
| U112 | product.template → product.product — attribute/variant explosion | P2 | No | NOT_PROVEN | product.template.attribute.value, _create_variant_ids, price extra | Done 2e66928b |
| U113 | mail — chatter + mail.activity deep (notification/reminder chain) | P2 | No | NOT_PROVEN | mail.activity lifecycle, mail.thread.mix, scheduled actions | Done 4967378c |
| U114 | account — journal locking + sequence integrity | P2 | Yes | NOT_PROVEN | Journal sequence.mixin, _get_last_sequence, SEQUENCE GAP detection | Done b5816952 |
| U115 | stock_account — WIP account entries from mrp_account close | P1 | Yes | NOT_PROVEN | mrp_account WIP journal, _get_production_account, finished goods posting | Done f8c004b2 |
| U116 | purchase_requisition — if present in Community | P2 | No | NOT_STUDIED | purchase.requisition model, tender workflow, PO from requisition | Done ac2cc851 (PRESENT — blanket_order + purchase_template) |
| U117 | digest — KPI digest cron + ir.actions.server pattern | P2 | No | NOT_STUDIED | digest.digest, _compute_kpis, mail cron | Done e7560a48 |
| U118 | account — deferred revenue/expense (account_deferred) | P1 | No | NOT_STUDIED | account.deferred model, amortization schedule, account.move generation | Done 3d054777 (ABSENT — Enterprise-only) |
| U119 | l10n_th_pnd — Thai personal income tax / PND if present | P0 | Yes (TH) | NOT_STUDIED | PND withholding, ภ.ง.ด.1/3/53, vendor WHT deduction at payment | Done c809cc4b (l10n_th_pnd+l10n_th_withholding_tax ABSENT; 12 WHT templates in l10n_th, PND3/PND53 reports, 5 gaps documented) |

| U120 | account — multi-company intercompany journal + shared COA (GAP-002/GAP-018) | P0 | Yes | NOT_PROVEN | shared_chart_of_accounts, company_id domain, intercompany automation | Done e24b9f94 (GAP-002 OPEN: account_inter_company_rules ABSENT; GAP-018 PARTIAL: company_ids M2M sharing) |
| U121 | stock — warehouse-company binding + inventory isolation (GAP-003) | P0 | Yes | NOT_PROVEN | warehouse.company_id ir.rule, cross-company stock move prevention | Done 3f5e52ab (GAP-003 PARTIAL: binding+14 ir.rules proven; inter-company PO/SO automation ABSENT) |
| U122 | account — credit note return immutability (GAP-028) | P1 | Yes | NOT_PROVEN | _reverse_move, credit note partial reconciliation, return stock accounting | Done 65065ebc (GAP-028 CLOSED) |
| U123 | account — year-end FX adjustment close (GAP-048) | P1 | Yes | NOT_PROVEN | _get_adjustment_entry at fiscal year close, unrealized FX balance | Done 862ab1fe (GAP-048 PARTIAL: exchange diff at reconcile proven; unrealized FX wizard ABSENT) |
| U124 | account — tax report period lock (GAP-027) | P1 | Yes | NOT_PROVEN | account.tax.report lock_date logic, tax_lock_date enforcement | Done 7323dbc4 (GAP-027 PARTIAL: tax_lock_date ORM enforcement C1; auto-advance on closing post ABSENT — Enterprise-only) |
| U125 | sale_subscription — Community presence check (GAP-049/Rank-12) | P2 | No | NOT_STUDIED | sale.subscription model, recurring invoice generation, contract renewal if present | Done fca31a3d (ABSENT — Enterprise-only; zero recurring billing in Community) |
| U126 | account — bank reconciliation statement backend (GAP-021/Rank-13) | P1 | Yes | PARTIAL | account.bank.statement.line auto-match Python backend, manual reconciliation wizard | Done eaa6652d (GAP-021 PARTIAL: Python backend C1; JS auto-match widget excluded; import ABSENT) |
| U127 | payment — provider webhook chain source-only (GAP-015/GAP-041/Rank-14) | P2 | No | PARTIAL | payment provider webhook chain, Stripe/Mollie source, _process_notification | Done 72dea18e (GAP-015 PARTIAL: 26 modules/18+ providers C1; GAP-041 PARTIAL: SO confirm+auto-invoice chain C1; AWT for live webhook) |
| U128 | mrp_plm / mrp_workcenter — ECO presence check (Rank-15) | P2 | No | NOT_STUDIED | ECO model, workcenter capacity, BOM versioning if present | Done 4f60911c (mrp_plm ABSENT — Enterprise-only; workcenter capacity/OEE/scheduling C1) |
## Continuous Manifest Queue — Batch 1 (U129–U138)
> Operating mode: 10 concurrent workers. Coordinator integrates sequentially. Applied 2026-10-02. Continuous manifest queue active from U139 onward — no batch-stop behavior.

| U129 | website_sale — deeper cross-module chain (GAP-026 depth/wishlist/loyalty) | P1 | No | PARTIAL | wishlist→loyalty→gift_card→cart→payment→SO confirm cross-module | Done 1eccfc7b (28 claims) |
| U130 | Semantic spot-check — U01–U46 + U47–U68 claim verification (GAP-024/GAP-045) | P1 | Moderate | Semantic | 10 random C1 claims per 5 high-risk units verified against source line refs | Done 886f3582 (evidence) + 4cd5d27c (neutral, packet); spot-check, 25 claim checks (5 groups × 5) |
| U131 | F-ID mapping — G10–G16 capability-to-Function-ID (GAP-034) | P2 | No | F-ID | Map each U47–U68 capability to existing Function-IDs or propose new ones | Done 4cd5d27c (evidence, neutral) + 1eccfc7b (packet) (30 claims) |
| U132 | stock — 3-step routing AWT-prep source study (GAP-030) | P2 | No | AWT-prep | INT→OUT route creation, picking_type_id chain, AWT test plan document | Done c864cc16 (evidence) + b9353bd6 (neutral, packet) (19 claims) |
| U133 | mail — gateway incoming email AWT-prep (GAP-039) | P2 | No | AWT-prep | mail.alias routing, message_process source, AWT test plan document | Done 7bc2b70e (22 claims) |
| U134 | l10n_th WHT PND form L3 deep (GAP-046 P0 TH) | P0 | Yes (TH) | NOT_PROVEN | PND-1/3/53 form generation wizard, WHT certificate, vendor deduction at payment | Done 886f3582 (30 claims) |
| U135 | account_payment_interco — intercompany journal L3 deep (GAP-002 extension) | P0 | Yes | PARTIAL | account_payment_interco module models, intercompany journal entry creation chain | Done 3c513351 (26 claims) |
| U136 | account_reconcile_model — rule engine deep (GAP-021 Python extension) | P1 | Yes | PARTIAL | account.reconcile.model rule types, _apply_rules, writeoff/invoice-match logic | Done 4cd5d27c (25 claims) |
| U137 | payment_xendit — Thai payment provider deep (source evidence U127, TH-adjacent) | P2 | Yes (TH) | NOT_STUDIED | Xendit FPX webhook, x-callback-token verification, THB decimal handling | Done a8655629 (26 claims) |
| U138 | account_tax_group / tax repartition — Thai WHT/VAT computation (GAP-046 sub) | P0 | Yes (TH) | PARTIAL | account.tax.group, account.tax.repartition.line, WHT deduction mechanics | Done b9353bd6 (30 claims) |

> Coordinator register catch-up (2026-10-02, origin tip d5e4d91e): U129–U138 above moved from Running to Done, and U139–U230 are recorded below. Commit SHAs are the git first-add commits of each unit's evidence (E), neutral (N) and packet (P) files, read from git history — not from the packet `sha` field, which is worker-written and may hold a source-file hash prefix or PENDING_COMMIT (e.g., U228, U229). Claim counts are the worker-reported counts in each unit's packet. Mixed commits (several units in one commit) are preserved as made, not rewritten. All commits listed are on origin/claude/local-odoo-source-research (REMOTE EVIDENCE READY). This register records presence and provenance only — NOT a verification result, NOT Gate PASS, NOT Formal Coverage, NOT Module Complete.

## Continuous Manifest Queue — Completed Units U139–U230
> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. No evidence files for U172–U179 were found in the three evidence sub-folders at origin tip. "with Uxxx" = the unit shares the commit with that unit. "absent per packet" = the unit's own packet reports the module as not present in the Community source tree.

| Unit | Topic (evidence file name) | Claims | Commit | Notes |
|------|----------------------------|--------|--------|-------|
| U139 | tax_lock_depth | 23 | E+N 08bf2b95; P 1cc9747a | with U140 |
| U140 | hr_leave | 25 | E+N 08bf2b95; P 1cc9747a | with U139 |
| U141 | semantic_spot_check_u47_u68 | spot-check: 5 groups × 5 claims verified | 549dbe0d | with U149 |
| U142 | project | 28 | c874839b | |
| U143 | crm | 27 | 6f9a8c37 | |
| U144 | account_asset | 5 | 9f1a7be7 | absent per packet |
| U145 | hr_attendance | 32 | 313df880 | |
| U146 | hr_core | 22 | b58bd08c | with U148 |
| U147 | hr_timesheet | 25 | 771547bc | |
| U148 | account_reports | 25 | b58bd08c | with U146 |
| U149 | account_coa_isolation | 22 | 549dbe0d | with U141 |
| U150 | purchase_stock_p2p | 25 | ac002e88 | with U156, U160 |
| U151 | sale_timesheet_billing | 24 | 681585dc | |
| U152 | account_followup | 7 | 39b6119b | absent per packet (7 of 7 claims absent) |
| U153 | maintenance | 22 | 4138cdbf | |
| U154 | stock_scrap | 22 | 0ed782eb | |
| U155 | mrp_workorder | 22 | 12dc98f0 | |
| U156 | fleet | 20 | ac002e88 | with U150, U160 |
| U157 | bank_stmt_import | 21 | 1bdf9c2b | |
| U158 | quality_control | 15 | 59b610d9 | absent per packet (15 of 15 claims absent) |
| U159 | account_cash_rounding | 20 | aee0f35b | |
| U160 | helpdesk | 7 | ac002e88 | absent per packet; with U150, U156 |
| U161 | stock_dropshipping | 25 | 80f7cbae | with U162, U163 |
| U162 | purchase_mrp | 25 | 80f7cbae | with U161, U163 |
| U163 | account_move_send | 22 | 80f7cbae | with U161, U162 |
| U164 | sale_purchase | 18 | 93bbbafe | |
| U165 | product_expiry | 20 | 00d4f1ca | |
| U166 | website | 22 | fe9af8e4 | with U170 |
| U167 | base_vat | 20 | 9de3f5f4 | |
| U168 | hr_recruitment | 22 | bd0e910a | |
| U169 | stock_inventory | 22 | fe8aeeed | |
| U170 | stock_putaway | 18 | fe9af8e4 | with U166 |
| U171 | product_pricelist | 22 | c80b3318 | |
| U180 | im_livechat | 20 | 146dda8b | with U183 |
| U181 | event | 11 | 83391b5d | |
| U182 | lunch | 20 | E 4dc5274a; N 61e21dbf; P 80aefa7d | evidence file is in the commit shared with U184 |
| U183 | note | 15 | 146dda8b | absent per packet; with U180 |
| U184 | mail_bot | 15 | 4dc5274a | commit also holds the U182 evidence file |
| U185 | website_sale_loyalty | 24 | 8ec0685a | |
| U186 | stock_picking_wave | 19 | d4221e3a | commit also holds the U187 evidence file |
| U187 | utm | 9 | E d4221e3a; N+P 11444d10 | evidence file is in the commit shared with U186; neutral and packet with U190, U191 |
| U188 | repair | 21 | c7effb35 | |
| U189 | account_payment | 22 | e3b77651 | |
| U190 | res_partner_bank | 19 | 11444d10 | with U187 (neutral, packet), U191 |
| U191 | gamification | 15 | 11444d10 | with U187 (neutral, packet), U190 |
| U192 | product_category_accounts | 22 | d77d9374 | |
| U193 | stock_barcode | 22 | ec9f452d | |
| U194 | website_slides | 18 | cc7a9532 | |
| U195 | account_journal | 22 | 822b8ada | with U196 |
| U196 | crm | 25 | 822b8ada | with U195 |
| U197 | hr_holidays | 23 | d8a0915a | |
| U198 | hr_timesheet | 21 | ef4c023b | packet SHA follow-up caea4585 |
| U199 | fleet | 20 | ccfea033 | packet SHA follow-up 9d4fe08e |
| U200 | base_automation | 22 | d3155f17 | packet SHA follow-up cce96a4d |
| U201 | sale_margin | 20 | 6dacbd78 | packet SHA follow-up 0766ce5a |
| U202 | hr_employee | 25 | f0cf5e10 | packet SHA follow-up c803a6b9 |
| U203 | stock_rule_route | 25 | b549f8f3 | |
| U204 | account_move_line | 26 | 3b2232e1 | packet SHA follow-up e30099cf |
| U205 | res_partner | 22 | 812d6978 | packet SHA follow-up ef23702d |
| U206 | hr_attendance | 20 | 75333077 | packet SHA follow-up 8a72d192 |
| U207 | calendar | 20 | e2a54616 | |
| U208 | mail_template | 20 | 022f4718 | |
| U209 | stock_scrap | 19 | 49f5b669 | |
| U210 | product_supplierinfo | 21 | 2a0de681 | packet SHA follow-up 10569041 |
| U211 | mrp_workcenter | 22 | 498b7871 | |
| U212 | account_payment_term | 22 | 230d69b1 | |
| U213 | stock_warehouse | 25 | 555efc66 | |
| U214 | ir_rule | 20 | 5b704d4d | |
| U215 | purchase_order_line | 22 | 97593ab6 | |
| U216 | mrp_production | 24 | 3d6e5c04 | |
| U217 | stock_location | 20 | d36063ef | |
| U218 | account_account | 22 | 498c4ba3 | |
| U219 | stock_move_line | 20 | d7ae34c1 | |
| U220 | res_company | 22 | 6db2deb6 | packet SHA follow-up 8479517f |
| U221 | sale_order | 22 | c49abbf4 | |
| U222 | ir_model_access | 20 | c7c03956 | with U223 |
| U223 | product_pricelist | 24 | c7c03956 | with U222 |
| U224 | account_tax | 25 | 0c2d35ab | with U225, U229 |
| U225 | purchase_order | 22 | 0c2d35ab | with U224, U229 |
| U226 | stock_picking | 24 | fa29c417 | |
| U227 | account_analytic | 25 | 210ba2e6 | |
| U228 | stock_quant | 22 | d82093b5 | |
| U229 | res_currency | 20 | 0c2d35ab | with U224, U225 |
| U230 | hr_version | 23 | d5e4d91e | |

## Continuous Manifest Queue — Running (as of this update)
> Dispatched 2026-10-02 by the coordinator; 10 concurrent workers; each worker writes only its own three U-specific files. Not yet committed or registered.

| Unit | Scope (dispatch label) | Status |
|------|------------------------|--------|
| U231 | product.template — type / is_storable / tracking | Running |
| U232 | stock_account — valuation / product.value | Running |
| U233 | sale.order.line — quantities / invoicing | Running |
| U234 | stock.move — state / reservation | Running |
| U235 | res.users / res.groups — privilege | Running |
| U236 | uom.uom / packaging | Running |
| U237 | mrp.bom — bom_line / byproduct | Running |
| U238 | account.move — header / fields / post | Running |
| U239 | partial / full reconcile engine | Running |
| U240 | module / data lifecycle — xmlid | Running |

---

## Execution Notes

1. **U100 starts immediately** after this plan is committed
2. **Thai Tax units (U100, U107, U119) are P0** — SMEsPlus is Thailand-deployment; TH-flagged gaps are highest priority
3. **Cash basis (U101)** is GAP-023 — C1-adjacent, PCO-F01 scope extension
4. **Migration (U102)** covers GAP-033 — migration scripts not studied in any prior unit
5. **Runtime items** (bank recon JS, mail gateway, multi-step routing) remain in AWT backlog — no runtime available
6. **All outputs**: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
7. **Do not post START_STATE03_BATCH_VERIFICATION** — awaiting Boss instruction
8. **Do not declare Formal Coverage or STATE03 Complete**

---

*DIAGNOSTIC ARTIFACT — Not Gate PASS — Not Boss Approval — Not Formal Coverage — Not STATE03 Complete*
*Canonical denominator 692 = CANDIDATE MODULE UNIVERSE — NOT FROZEN*
