# STATE03 VDR — Third-Pass Execution Plan
## DIAGNOSTIC ARTIFACT — NOT GATE PASS — NOT BOSS APPROVAL
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

**Produced by:** Main controller session
**Date:** 2026-10-02
**Basis:** START_STATE03_THIRD_PASS_RESEARCH directive
**Scope:** U100–U119+ targeting Partial/Not-Proven/C1 gaps from gap register and second-pass residuals

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
| U100 | l10n_th + l10n_th_withholding_tax — Thai VAT + WHT | P0 | Yes (TH) | NOT_STUDIED | Thai VAT 7%, WHT rates, tax report, ภ.ง.ด. form types | Queued |
| U101 | account — cash basis accounting (GAP-023) | P0 | Yes | NOT_PROVEN | tax_cash_basis_journal_id, _get_cash_basis_lines, cash basis move creation | Queued |
| U102 | Migration scripts — hook patterns across modules (GAP-033) | P0 | Yes | NOT_STUDIED | migrations/ folders, pre/post migrate hooks, field rename/merge patterns | Queued |
| U103 | account — multi-currency revaluation + forex gain/loss | P1 | Yes | NOT_PROVEN | currency_id on account.move.line, _get_adjustment_entry, unrealized FX | Queued |
| U104 | account_peppol_response — response handling (GAP-040) | P1 | No | NOT_STUDIED | PEPPOL response XML parsing, document status update, error handling | Queued |
| U105 | pos_restaurant — table/floor management deep (GAP-038) | P1 | No | PARTIAL | floor.plan, restaurant.table, split order, course ordering | Queued |
| U106 | stock — replenishment (orderpoint, procurement rule, make-to-order) | P1 | No | NOT_PROVEN | stock.warehouse.orderpoint, _run_scheduler, route MTO vs reorder | Queued |
| U107 | account — fiscal position Thai edge cases (GAP-043) | P1 | Yes (TH) | NOT_PROVEN | map_tax for Thai VAT 0%/7%, fiscal.position.template, intra-company | Queued |
| U108 | auth_passkey — WebAuthn registration/auth flow L2/L3 (GAP-020) | P1 | No | PARTIAL | WebAuthn controllers, passkey CRUD, security group gate | Queued |
| U109 | account.analytic.plan — multi-plan hierarchy deep | P1 | No | NOT_PROVEN | analytic.plan tree, mandatory % validation, cross-module distribution | Queued |
| U110 | stock — lot/serial traceability + account impact | P1 | No | NOT_PROVEN | stock.lot FIFO/AVCO interaction, lot-level valuation, removal strategy | Queued |
| U111 | account_budget — budget control (if Community) | P2 | No | NOT_STUDIED | crossovered.budget, budget.line, account.budget.post | Queued |
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
