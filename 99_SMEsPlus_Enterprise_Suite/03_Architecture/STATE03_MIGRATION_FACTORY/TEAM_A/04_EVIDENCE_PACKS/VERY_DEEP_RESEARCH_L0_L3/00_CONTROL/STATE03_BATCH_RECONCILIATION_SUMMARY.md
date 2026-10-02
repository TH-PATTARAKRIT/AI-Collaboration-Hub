# STATE03 VDR — Batch Reconciliation Summary
## DIAGNOSTIC ARTIFACT — NOT GATE PASS — NOT BOSS APPROVAL

**Produced by:** Main controller session (claude/local-odoo-source-research)
**Date:** 2026-10-02
**Scope:** U70–U99 second-pass batch completion summary
**Status:** ALL 30 UNITS GATE-PASS — BATCH COMPLETE

---

## Batch Completion Status

| Unit | SHA | Claims | Priority | Key Capability |
|------|-----|--------|----------|----------------|
| U70 | ec7f3cee | — | P0 | Account lock date enforcement (PCO-F01) |
| U71 | 0865e1b8 | — | P0 | Multi-company isolation ir.rule domains |
| U72 | 14678b80 | — | P0 | Stock valuation perpetual AVCO/FIFO |
| U73 | 1128925f | — | P0 | Audit trail immutability hash chain |
| U74 | bd6edd19 | — | P0 | Three-way match / bill control (GRV-F06) |
| U75 | bdc59706 | — | P0 | Period cutoff / accrued orders wizard |
| U76 | bf927a87 | — | P1 | Full O2C chain (L5/L11) |
| U77 | 975500d1 | — | P1 | Full P2P chain (L5/L11) |
| U78 | b9c44b0b | 45 | P1 | MRP MO full lifecycle |
| U79 | b6486c83 | 52 | P1 | Account entry full lifecycle |
| U80 | bdf8d16f | 41 | P1 | Stock valuation AVCO/FIFO deep |
| U81 | 7cb2a5f2 | 60 | P1 | Payment + bank reconciliation |
| U82 | cfde150b | 50 | P1 | EDI/UBL/PEPPOL full flow |
| U83 | ff7def70 | 45 | P1 | MRP subcontracting + purchase |
| U84 | d4cb63c1 | 21 | P1 | COGS timing at delivery |
| U85 | 8c17f79b | 66 | P1 | POS session lifecycle |
| U86 | a976e473 | 51 | P2 | CRM lead full pipeline |
| U87 | 14282d11 | 53 | P2 | Project + timesheet + analytic chain |
| U88 | 4225babd | 56 | P2 | HR leave + work entry + payroll prep |
| U89 | 3ec55574 | 63 | P2 | Website eCommerce full flow |
| U90 | 9eeab40f | 35 | P2 | Marketing automation chain |
| U91 | e77e84a5 | 35 | P2 | HR expense → invoice chain |
| U92 | db650e65 | 36 | P2 | Website content platform (blog/forum/slides) |
| U93 | fcc1891c | 32 | P2 | Batch picking workflow |
| U94 | 6ac54bb1 | 35 | P2 | Payment provider webhooks (Stripe/PayPal) |
| U95 | dc599bed | 49 | P0 | U55 RECOVERY — sale bridge modules |
| U96 | 6089fa95 | 45 | P1 | Landed costs (GRV-F05) |
| U97 | ebea52b2 | 32 | P2 | Survey + CRM integration |
| U98 | 4cfa68df | 27 | P1 | Python formula tax (L12 adversarial) |
| U99 | 71d8c299 | 35 | P0 | Multi-company record rule audit |

**All 30 units: GATE-PASS (claim-checks=0, neutral-leak-tokens=0 per unit)**

---

## P0 Critical Findings Summary

### U70 — Lock Date Enforcement
- `_check_fiscalyear_lock_date()` raises ValidationError for write to locked period
- Lock date bypass requires `account.group_account_manager` AND advisory lock override
- `posted_before` permanent latch; `action_post()` auto-advances past lock date (no hard error in Community)

### U71 — Multi-Company Isolation
- Two ir.rule domain patterns: strict `in` (transactions) vs `parent_of` (config records)
- `allowed_company_ids` set per RPC by web client; `env.companies` reads from context
- `sudo()` **completely bypasses all ir.rules** including company isolation (documented behavior)

### U73 — Audit Trail Immutability
- SHA-256 hash chain: format `$4$<sha256hex>`; `MAX_HASH_VERSION=4`
- Only journals with `restrict_mode_hash_table=True` are auto-hashed
- `button_draft()` blocked if hash already set; `write()` guards on posted fields

### U74 — Three-Way Match
- Hard three-way match (`module_account_3way_match`) is ENTERPRISE-ONLY in Odoo 19
- Community has soft bill-control via `purchase_order_line.qty_invoiced` check only
- GRV-F06 partially met in Community; hard block absent

### U95 — U55 Recovery
- Gap identified: 8 sale bridge modules (sale_crm, sale_loyalty, sale_management, sale_margin, sale_mrp, sale_product_matrix, sale_project, sale_stock)
- U55 evidence gap now closed; all 692 CANDIDATE modules have first-pass coverage

### U98 — Python Tax (L12 Adversarial)
- RCE blocked by 3 independent layers: AST whitelist (save-time) + safe_eval opcode blacklist (runtime) + no env/ORM in eval context
- Residual risk: authorized Account Manager can write formula returning incorrect tax amounts (governance concern, not sandbox failure)

### U99 — Multi-Company Record Rule Audit
- `sudo()` in `_get_rules()` returns empty browse set — total bypass of all ir.rules
- `account_payment_interco` IS present in Community 19; uses `moves.sudo()._interco_filter_moves()` intentionally
- `parent_of` operator used for config records (journal, account, tax) — parent company config visible to child company users

---

## Architecture Discoveries (Session-Level)

1. `stock.valuation.layer` replaced by `product.value` model in Odoo 19 (no `quantity` field)
2. `_account_entry_move()` renamed to `_create_account_move()`
3. `account_bank_statement_import` ABSENT from Community 19
4. `hr.expense.sheet` model REMOVED in Odoo 19 Community
5. `hr_payroll` ABSENT from Community 19 (Enterprise-only)
6. `account.payment` states: draft/in_process/paid/canceled/rejected (no 'posted')
7. Community `_get_invoice_in_payment_state()` always returns 'paid' (no 'in_payment' state)
8. MRP subcontracting MO auto-created at PO confirmation, not receipt validation
9. Hard 3-way match (`module_account_3way_match`) is Enterprise-only
10. Both `payment_stripe` and `payment_paypal` present in Community 19
11. `account_payment_interco` present in Community 19

---

## P2 Runtime Reachability

**P2 (Runtime Reachability) remains NOT_PROVEN across ALL units.**
No Odoo runtime was executed during this research phase. All evidence is source-level (P1) and config/rule-level (P3). Runtime proof requires AWT (Automated Workflow Test) environment provisioning.

---

## Batch Statistics

- Total second-pass units completed: 30 (U70–U99)
- Total claims produced (U78–U99 tracked): 886+
- All units: GATE-PASS on first attempt (this session: U78–U99 zero gate failures)
- Workers total (all sessions): 83

---

*DIAGNOSTIC ARTIFACT — Not Gate PASS — Not Boss Approval — Not Formal Coverage — Not STATE03 Complete*
*Canonical denominator 692 = CANDIDATE MODULE UNIVERSE — NOT FROZEN*
