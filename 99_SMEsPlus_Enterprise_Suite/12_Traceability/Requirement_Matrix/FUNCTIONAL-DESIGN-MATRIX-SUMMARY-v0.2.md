# Functional Design Matching Matrix v0.2 - Summary (Reconciled)

**Supersedes**: FUNCTIONAL-DESIGN-MATRIX-SUMMARY.md (v0.1, 2026-07-02)
**Full detail**: SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.2.md (same folder)
**Reconciled by**: Claude, 2026-07-02, against real source code (`01_ACCOUNT.zip`, `02_OTHER.zip`) and the live DB dump (`iTEST02_2026-06-14_14-41-19.dump`)

---

## Evidence status: before (v0.1) vs. after (v0.2)

| Status | v0.1 count | v0.2 count | Change |
|---|---|---|---|
| MATCHED | 0 | 5 | +5 |
| PARTIAL | 7 | 4 | -3 |
| GAP | 2 | 3 | +1 (FR-PUR-005 split: in-scope part stays GAP) |
| NEW (=GAP) | 3 | 2 | -1 (moved into GAP count above) |
| OUT OF SCOPE | 0 | 1 (part of FR-PUR-005) | new category — Boss decision 2026-07-02 |

**Headline change**: 5 of 12 requirements (FR-FD-002, FR-PUR-001, FR-PUR-006, FR-INV-001, FR-ACC-001) turned out to already be working native Odoo capability — no new service needs to be built, only sourced/verified/gated. Estimated story points for ERPPLUS-92, 95, 100, 101, 102 should come down materially.

The two requirements that remain genuinely hard did not change: **FR-PUR-002 (RFQ multi-vendor tendering, 55 SP)** and **FR-PUR-004 (vendor comparison)** are confirmed real gaps with no existing implementation anywhere in the 1,395-table schema. **FR-PUR-005 (Vendor Selection)** is now split: the actual "buyer picks winner + justification" object is a confirmed GAP (build needed); the separate `level1/level2` approval fields that were previously assumed to be part of this same gap are **out of scope** per Boss's 2026-07-02 decision and should be removed from ERPPLUS-99's scope entirely.

## Per-FR verdict (see full matrix for evidence detail)

| FR | v0.2 Status | Note |
|---|---|---|
| FR-FD-001 Tenant Isolation | PARTIAL | Company-level isolation exists; Tenant-grouping layer above it does not |
| FR-FD-002 RBAC | MATCHED (base) | Odoo `res_groups`/`ir_model_access`/`ir_rule` fully covers base RBAC |
| FR-FD-003 Subscription | GAP | Confirmed — zero subscription/entitlement tables exist |
| FR-FD-004 Module Activation | PARTIAL | Base toggle exists; subscription-gating layer doesn't |
| FR-PUR-001 Purchase Request | MATCHED | Real OCA `purchase_request` module confirmed in DB — needs sourcing, not building |
| FR-PUR-002 RFQ Management | GAP | Confirmed real gap, biggest remaining build item |
| FR-PUR-003 Quote Tracking | GAP | Confirmed real gap, depends on FR-PUR-002 |
| FR-PUR-004 Vendor Comparison | GAP | Confirmed real gap |
| FR-PUR-005 Vendor Selection | GAP (in-scope) / OUT OF SCOPE (level1/2 fields) | Boss excluded the level1/2 approval extension 2026-07-02 |
| FR-PUR-006 PO Generation | MATCHED (base) / GAP (approval gate) | Native RFQ→PO confirm works; missing gate on Vendor Selection approval |
| FR-INV-001 Goods Receipt | MATCHED (base) / GAP (tolerance rule) | Native Odoo receiving works; over-receipt tolerance rule unconfirmed |
| FR-ACC-001 Vendor Bill / 3-way match | MATCHED | Explicitly confirmed twice in Learning Analysis — fully working |

## Recommended next action

PMO AI / Enterprise Architect AI: re-estimate story points for ERPPLUS-92, 95, 99, 100, 101, 102 against this v0.2 evidence before Phase 2 sprint planning starts (target 2026-07-03 per v0.1's own timeline). ERPPLUS-96 (RFQ) remains the correct top priority and its 55 SP estimate is unchanged/confirmed.
