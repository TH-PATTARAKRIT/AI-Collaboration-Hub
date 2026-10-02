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
| U111 | account_budget — budget control (if Community) | P2 | No | NOT_STUDIED | crossovered.budget, budget.line, account.budget.post | Running |
| U112 | product.template → product.product — attribute/variant explosion | P2 | No | NOT_PROVEN | product.template.attribute.value, _create_variant_ids, price extra | Queued |
| U113 | mail — chatter + mail.activity deep (notification/reminder chain) | P2 | No | NOT_PROVEN | mail.activity lifecycle, mail.thread.mix, scheduled actions | Queued |
| U114 | account — journal locking + sequence integrity | P2 | Yes | NOT_PROVEN | Journal sequence.mixin, _get_last_sequence, SEQUENCE GAP detection | Queued |
| U115 | stock_account — WIP account entries from mrp_account close | P1 | Yes | NOT_PROVEN | mrp_account WIP journal, _get_production_account, finished goods posting | Queued |
| U116 | purchase_requisition — if present in Community | P2 | No | NOT_STUDIED | purchase.requisition model, tender workflow, PO from requisition | Queued |
| U117 | digest — KPI digest cron + ir.actions.server pattern | P2 | No | NOT_STUDIED | digest.digest, _compute_kpis, mail cron | Queued |
| U118 | account — deferred revenue/expense (account_deferred) | P1 | No | NOT_STUDIED | account.deferred model, amortization schedule, account.move generation | Queued |
| U119 | l10n_th_pnd — Thai personal income tax / PND if present | P0 | Yes (TH) | NOT_STUDIED | PND withholding, ภ.ง.ด.1/3/53, vendor WHT deduction at payment | Queued |

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
