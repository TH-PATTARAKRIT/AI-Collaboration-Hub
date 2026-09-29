> Domain: SHARED_MASTER_DATA_PILOT | Domain Index | Documentation-Tier | **STATUS: IN PROGRESS — first pass only, not complete**

# 00 — DOMAIN INDEX

Module: `M3` — Shared Business Master (Wave 1, per `STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.md`). Selected as the **top priority** next module per Boss's "STATE03 M1 Close Then Core Module Priority" instruction (2026-09-29): "Shared Master Data required by transactions (Partner, Product, UoM, Company/Role boundaries as applicable)" — priority #1, ahead of Sales/Purchase/Inventory/Accounting/O2C-P2P/Manufacturing.

## Readiness evidence (why this module is `READY`, not `HOLD`)

- Priority-matrix gate: `ML-W1-G1` + "Shared Domain Freeze" (`STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.csv`, Wave 1 rows) — a **design**-freeze dependency, not a research-blocking gate; documentation-tier reference research may run ahead of it (the same standing rule already applied to every prior Gx/M1/M2 pilot).
- No Boss Gate Queue item blocks documentation-tier research on this module.
- No duplicate-framework risk: confirmed by direct search that **no existing pilot in this repository already covers Party/Contact, Product Template/Variant, UoM conversion, or Access-Rights/Groups** under this Deep Study's own documentation-tier taxonomy.

## Scope-collision check (mandatory — "no duplicate framework/register/universe/denominator")

Two **separate, pre-existing, differently-authorized** research tracks were found and must **not** be touched, restarted, or duplicated by this session:

1. `DOMAIN_01_ACCOUNTING_CORE/` — session `SMEPLUS-26-08-29-MIG-A-D01-CORR-001`, Team A with live source/DB access, terminal status `CORRECTIVE ROUND EXECUTED ... READY FOR CHATGPT RE-AUDIT`, explicit stop directive: *"Team A stops here. Not proceeding to Sonnet. Not proceeding to Team B. Not starting another domain."* This is a different program, different branch context, different access model (source+DB) than this session's own WebSearch-documentation-tier method. **Not resumed here.**
2. `GROUP_01_SALES_INVENTORY_PURCHASE/` — session series `SMEPLUS-26-08-3x-MIG-A-GRPA-SIP-*`, Team A with live `iTEST02` dump access, on branch `claude/group-a-sales-inventory-purchase-dr002` (not this session's `claude/new-session-l8f19r`), terminal status `TEAM A EVIDENCE GATE CANDIDATE — READY FOR INDEPENDENT REVIEW`. **Not resumed here** — this session has no dump/source access and is not that program's authorized executor.

**Conclusion**: this Deep Study's own Lane C Gx pilots (`Gx1` Goods Receipt, `Gx2` Sales Delivery, `Gx4` Inventory Adjustment, `Gx6` Period Cutoff, `Gx9` Multi-company) already provide *cross-proof reference-behavior scenarios* touching Purchase/Sales/Inventory/Accounting/Company-scope, but they are not dedicated per-module Shared-Master-Data registers. This pilot fills exactly that gap — Party/Contact, Product Template/Variant, UoM — without re-opening or duplicating either separate track above. **Company boundary** is cross-referenced to `MULTICOMPANY_ISOLATION_PILOT` (`Gx9`, already researched — not re-done here); **Role boundary** (Access Rights/Groups) is genuinely new, not covered anywhere in this Deep Study before now.

## Scope (this pass)

4 functions drafted (see `04_FUNCTION_REGISTER.md`): Partner/Contact model (Party), Product Template/Variant, UoM Category/Conversion, Access Rights/Groups (Role boundary). **Not yet researched**: Pricing/Pricelist, Tax Master, Payment Terms, Fiscal Calendar, Currency/Exchange Rate, Dimension/Analytic Structure, Shared Reference/Sequence — remaining Wave 1 items, candidates for a bounded follow-up only if a material gap surfaces, per Boss's "stop adding scope after the present slice reaches its checkpoint" discipline (applied here by analogy from the M1 instruction).

## Status

`IN PROGRESS` — documentation-tier first pass. Not added to any population total until its own row-level reconciliation, per the same discipline as `M1`/`M2`. Not a Gate PASS, not Team B design input, not STATE03 completion.
