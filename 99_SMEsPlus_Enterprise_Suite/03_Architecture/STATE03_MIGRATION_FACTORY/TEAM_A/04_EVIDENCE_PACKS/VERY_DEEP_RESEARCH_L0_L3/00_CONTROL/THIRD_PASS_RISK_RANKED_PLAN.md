# STATE03 Third-Pass Risk-Ranked Research Plan
## DEEPSEEK-REPORTED — PENDING BOSS APPROVAL
## Date: 2026-10-02
## Status: PENDING — do not execute until Boss approves

> **CRITICAL:** This plan is DIAGNOSTIC ONLY. No unit may execute until Boss gives explicit
> approval command. All proposed units are risk-ranked from existing gap register analysis.
> U01–U114 already complete — do NOT re-run those units.
> Runtime gaps (P2) cannot be closed without AWT provisioning — they are listed but flagged.

**Basis:** GAP_REGISTER_THIRD_PASS.md open gaps + residual MODULE_G_CROSSWALK coverage analysis
**Already planned (from THIRD_PASS_EXECUTION_PLAN.md):** U115–U119 — included at risk rank

---

## Proposed Units — Risk Ranked (Cap: 20)

| Rank | Proposed-Unit-ID | Module(s) | G Group | Gap-ID | Proof-layer-missing | C1-material-risk-reason | Expected-evidence | Expected-gate |
|------|-----------------|-----------|---------|--------|--------------------|-----------------------|------------------|---------------|
| 1 | U115-prop | mrp_account, stock_account | G07/G06 | GAP-047 | P1/L4 | WIP journal entries — inventory valuation at MRP production close; C1-adjacent for manufacturing cost | 30+ claims on `_get_production_account`, WIP account routing, mrp_account journal entries | GATE-PASS |
| 2 | U116-prop | l10n_th_withholding_tax, l10n_th | G02 | GAP-046 | L3/P3 | Thai statutory WHT — PND-1/3/53 form generation; Thai deployment P0 | 30+ claims on PND form logic, WHT certificate generation, vendor WHT deduction at payment | GATE-PASS |
| 3 | U117-prop | purchase_requisition (if present) | G08 | — | L3 | Purchase requisition workflow not studied; Community vs Enterprise boundary unknown | 20+ claims on purchase.requisition model, tender workflow, PO from requisition | GATE-PASS |
| 4 | U118-prop | account (tax report lock GAP-027) | G01 | GAP-027 | L7 | Tax period lock — regulatory compliance; prevents re-export risk | 20+ claims on `account.tax.report.py` lock_date logic, period freeze enforcement | GATE-PASS |
| 5 | U119-prop | l10n_th_pnd (if present) | G02 | GAP-046 | L3/P3 | Thai PND personal income tax / ภ.ง.ด. — statutory filing forms; P0 Thai deployment | 30+ claims on PND-1/3/53 form types, vendor WHT deduction at payment, PND reconciliation | GATE-PASS |
| 6 | U120-prop | digest | G14 | GAP-049 | L3 | KPI digest cron — `_compute_kpis` and mail cron; governance/reporting concern | 20+ claims on digest.digest model, KPI computation, scheduled cron trigger | GATE-PASS |
| 7 | U121-prop | account (deferred revenue/expense) | G01 | GAP-050 | L3 | Deferred revenue amortization — revenue recognition timing; IFRS-adjacent | 20+ claims on account.deferred model, amortization schedule, account.move generation | GATE-PASS |
| 8 | U122-prop | account (multi-currency FX year-end) | G01 | GAP-048 | L3 | Year-end FX adjustment — balance sheet accuracy for multi-currency books | 20+ claims on `_get_adjustment_entry`, unrealized FX at fiscal year close | GATE-PASS |
| 9 | U123-prop | account_payment, account (GAP-028) | G03/G01 | GAP-028 | P1/L8 | Credit note return immutability — SDV-F07; C1-rated return/invoice chain | 20+ claims on `_reverse_move`, credit note partial reconciliation, return stock move accounting | GATE-PASS |
| 10 | U124-prop | account (GAP-002/GAP-018 multi-company COA) | G01 | GAP-002,GAP-018 | P1/L9 | MCT-F02/MCT-F03 shared COA and intercompany journal — multi-entity books | 25+ claims on shared_chart_of_accounts config, `company_id` domain enforcement, intercompany automation | GATE-PASS |
| 11 | U125-prop | stock, stock_account (GAP-003 warehouse-company) | G06 | GAP-003 | P1/L9 | MCT-F05 warehouse-company binding — inventory isolation between entities | 20+ claims on warehouse.company_id ir.rule domain, cross-company stock move prevention | GATE-PASS |
| 12 | U126-prop | sale_subscription (if present in Community) | G05 | — | L3 | Recurring subscription invoicing — not studied; potential C1-adjacent for SaaS clients | 20+ claims on subscription model, recurring invoice generation, contract renewal | GATE-PASS |
| 13 | U127-prop | account (GAP-021 bank reconciliation widget backend) | G01 | GAP-021 | P1/L7 | Bank statement auto-matching Python backend (excludes JS runtime) — partial closure | 20+ claims on `account.bank.statement.line`, auto-match Python logic, manual reconciliation wizard | GATE-PASS |
| 14 | U128-prop | account_move, stock (GAP-015/GAP-041 payment runtime) | G03/G15 | GAP-015,GAP-041 | P2/runtime | Payment provider webhook chain — eCommerce deployment critical; 22+ providers unstudied | NOTE: Runtime required — cannot fully close without AWT; source study only for Stripe/Mollie | PARTIAL |
| 15 | U129-prop | mrp_plm, mrp_workcenter (if present) | G07 | — | L3 | Engineering Change Orders (ECO) and work centre capacity — manufacturing planning depth | 20+ claims on ECO model, workcenter capacity, BOM versioning | GATE-PASS |
| 16 | U130-prop | website_sale, payment (GAP-026 residual) | G12/G15 | GAP-026 | P1/L4 | eCommerce payment confirmation residual — website_sale_wishlist, website_sale_loyalty cross-module | 20+ claims on wishlist→cart→payment→SO confirmation chain | GATE-PASS |
| 17 | U131-prop | hr_expense, analytic (GAP-024 semantic spot-check) | G09/G14 | GAP-024,GAP-045 | Semantic | MECHANICAL_ONLY semantic risk — spot-check 5 random claims per unit for U01–U46 high-priority | 5 random claims from each of U11, U05, U07, U08, U09 verified against source line references | SEMANTIC-PASS |
| 18 | U132-prop | account_move (GAP-034 Function-ID mapping) | All | GAP-034 | F-ID | Function-ID coverage gap for G10–G16 — U47–U68 unmapped; blocks traceability report | Map each U47–U68 capability to existing Function-IDs or propose new ones | F-ID-MAPPED |
| 19 | U133-prop | stock (GAP-030 multi-step routing P2 preparation) | G06 | GAP-030 | P2/runtime | Multi-step 3-step routing — AWT preparation unit; document test plan for future runtime run | 15+ claims documenting 3-step INT→OUT route creation, picking_type_id logic; RT test plan | AWT-READY |
| 20 | U134-prop | mail (GAP-039 mail gateway P2 preparation) | G13 | GAP-039 | P2/runtime | Mail gateway incoming email — AWT preparation; document test plan for mail.alias routing | 15+ claims documenting alias routing, message_process; RT test plan for mail gateway | AWT-READY |

---

## Already-Planned Units from Third-Pass Execution Plan (U115–U119)

These were queued in `STATE03_THIRD_PASS_EXECUTION_PLAN.md` and map to this plan's risk ranks:

| Execution-Plan Unit | Risk Rank Equivalent | Notes |
|--------------------|---------------------|-------|
| U115 (stock_account + mrp_account WIP) | Rank 1 (U115-prop) | Exact match |
| U116 (purchase_requisition) | Rank 3 (U117-prop) | Execution plan uses U116; this plan uses U117-prop to avoid confusion with risk rank IDs |
| U117 (digest cron) | Rank 6 (U120-prop) | |
| U118 (account deferred revenue) | Rank 7 (U121-prop) | |
| U119 (l10n_th PND Thai WHT) | Rank 5 (U119-prop) | P0 — should run before purchase_requisition |

**Recommended execution order if Boss approves:** U115 → U119 → U116/U117-prop → U118-prop → U120-prop → remainder ranked 1–20

---

## Exclusions

The following gap types are EXCLUDED from proposed units:
- **Runtime-only gaps (P2)**: GAP-021 JS widget, GAP-030 3-step routing, GAP-039 mail gateway, GAP-041 payment webhooks — AWT environment required; no source-only unit can close these
- **Governance-only gaps**: GAP-035, GAP-036, GAP-037 — require Boss/Project Manager decision on denominator scope, not research units
- **Semantic review gaps**: GAP-024, GAP-045 — addressed by U131-prop as spot-check; comprehensive re-review not feasible without dedicated semantic verification pipeline

---

## Coverage Impact Assessment

If all 20 proposed units execute and GATE-PASS:

| G Group | Current Open Gaps | Gaps Addressed by Plan | Estimated Residual |
|---------|------------------|----------------------|-------------------|
| G01 | 5 open/partial | 6 proposed (U121,U122,U123,U124,U127,U132) | 1 (GAP-027 partial) |
| G02 | 2 open | 2 proposed (U116-prop, U119-prop) | 0 |
| G03 | 2 open/partial | 2 proposed (U123,U127) | 1 (runtime only) |
| G04 | 0 open | 0 | 0 |
| G05 | 1 open | 1 proposed (U130-prop) | 0 |
| G06 | 3 open/partial | 2 proposed (U125,U133-AWT-prep) | 1 (runtime) |
| G07 | 1 open | 2 proposed (U115,U129) | 0 |
| G08 | 0 open | 1 proposed (U117) | 0 |
| G09 | 0 open | 0 | 0 |
| G10 | 0 open | 0 | 0 |
| G11 | 0 open | 0 | 0 |
| G12 | 0 open | 1 proposed (U130) | 0 |
| G13 | 1 open (runtime) | 1 proposed (U134-AWT-prep) | 1 (runtime) |
| G14 | 1 open | 1 proposed (U120) | 0 |
| G15 | 3 open | 1 proposed (U131 semantic) | 2 |
| G16 | 3 governance | 0 (governance) | 3 (governance) |

---

## Blockers

1. **AWT not provisioned** — 5 gaps (GAP-021, GAP-030, GAP-039, GAP-041, partial GAP-015) cannot be closed without runtime Odoo instance. AWT-prep units (U133-prop, U134-prop) document test plans only.
2. **Governance decisions pending** — GAP-035/036/037 require Boss to confirm test_*/theme_* denominator scope.
3. **Boss approval required** — This entire plan is PENDING. No unit executes until explicit Boss command.

---

*DEEPSEEK-REPORTED — PENDING BOSS APPROVAL*
*Not Gate PASS — Not Boss Approval — Not Formal Coverage — Not STATE03 Complete*
*Canonical denominator 692 = CANDIDATE MODULE UNIVERSE — NOT FROZEN*
