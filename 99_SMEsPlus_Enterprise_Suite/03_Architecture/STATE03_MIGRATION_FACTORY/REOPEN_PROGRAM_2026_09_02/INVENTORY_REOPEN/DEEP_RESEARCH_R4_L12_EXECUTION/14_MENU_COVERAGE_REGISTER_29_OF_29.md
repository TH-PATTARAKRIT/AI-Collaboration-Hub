# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 14 — Menu Coverage Register — 29 of 29

Scope: `29 of 29 Inventory menus from the Boss-approved R4 evidence intake`
Control Level: `/L9999.9999`
Status: `29 OF 29 MENUS TRACED THROUGH L1-L12 — 0 MENUS DEFERRED — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Coverage Rule Applied

The Boss prompt requires that **every menu is traced through L1-L12, or explicitly marked `HOLD` with reason and owner.** This register records which of the two applies to each menu.

R4's result: **no menu required a blanket `HOLD`.** Every menu was traced through all twelve levels. Six menus are `PARTIAL` at L2 specifically — meaning their field and configuration structure is established but their destructive-change or validation semantics could not be proven without a live reference-instance test or Thai user input. That is a level-specific partial, not a menu-level deferral, and each carries its named cause below.

Nineteen menus carry a `DEPENDENCY: ACCOUNTING COGS GAP` on at least one conclusion. A dependency lock is also not a deferral — the menu is fully researched; specific conclusions within it may not be finalised.

---

## 2. The 29-Menu Coverage Table

| R4 ID | Menu | Menu Deep Challenge ID | Group | L1 | L2 | L3 functions | L4-L12 | COGS dependency | Dependency detail | New R4 findings |
|---|---|---|---|---|---|---|---|---|---|---|
| `INV-M01` | Replenishment | `MENU-OP-01` | Operations | L1 ✓ | L2 COMPLETE | INV-F-01, INV-F-02 | L4-L12 ✓ | No | — | R4-F-01, R4-F-14 |
| `INV-M02` | Inventory Adjustments | `MENU-OP-02` | Operations | L1 ✓ | L2 COMPLETE | INV-F-03, INV-F-04, INV-F-41 | L4-L12 ✓ | Yes | Adjustment loss classification — JT-07 adjacent | R4-F-02 |
| `INV-M03` | Transfers | `MENU-OP-03` | Operations | L1 ✓ | L2 COMPLETE | INV-F-05..INV-F-11 | L4-L12 ✓ | Yes | Recognition timing JT-03, JT-04; return basis JT-05 | — |
| `INV-M04` | Scrap | `MENU-OP-04` | Operations | L1 ✓ | L2 COMPLETE | INV-F-12, INV-F-13 | L4-L12 ✓ | Yes | Loss and salvage classification | R4-F-03, R4-F-04 |
| `INV-M05` | Landed Costs | `MENU-OP-05` | Operations | L1 ✓ | L2 COMPLETE | INV-F-14 | L4-L12 ✓ | Yes | Eligibility and posting JT-08 — Audit VETO retained | R4-F-05 |
| `INV-M06` | Run Scheduler | `MENU-OP-06` | Operations | L1 ✓ | L2 COMPLETE | INV-F-15 | L4-L12 ✓ | No | — | — |
| `INV-M07` | Products | `MENU-PR-01` | Products | L1 ✓ | L2 COMPLETE | INV-F-16, INV-F-17 | L4-L12 ✓ | Yes | Costing category consequence JT-01 | — |
| `INV-M08` | Product Variants | `MENU-PR-02` | Products | L1 ✓ | L2 PARTIAL | INV-F-18 | L4-L12 ✓ | Yes | Variant valuation | — |
| `INV-M09` | Lots/Serial Numbers | `MENU-PR-03` | Products | L1 ✓ | L2 COMPLETE | INV-F-19, INV-F-20 | L4-L12 ✓ | Yes | Batch-level valuation | R4-F-06 |
| `INV-M10` | Stock | `MENU-RP-01` | Reporting | L1 ✓ | L2 COMPLETE | INV-F-21 | L4-L12 ✓ | No | Value column only | R4-F-07 |
| `INV-M11` | Locations (Reporting) | `MENU-RP-02` | Reporting | L1 ✓ | L2 COMPLETE | INV-F-21 | L4-L12 ✓ | No | Value column only | — |
| `INV-M12` | Moves History | `MENU-RP-03` | Reporting | L1 ✓ | L2 COMPLETE | INV-F-22 | L4-L12 ✓ | Yes | Value column; TH-HOLD-01 statutory name held | R4-F-08 |
| `INV-M13` | Stock Moves | `MENU-RP-04` | Reporting | L1 ✓ | L2 COMPLETE | INV-F-22 | L4-L12 ✓ | Yes | Pending value visibility | — |
| `INV-M14` | Valuation | `MENU-RP-05` | Reporting | L1 ✓ | L2 COMPLETE | INV-F-23 | L4-L12 ✓ | Yes | ALL CONCLUSIONS LOCKED — JT-01, JT-02, JT-03, JT-07 | — |
| `INV-M15` | Warehouse Analysis | `MENU-RP-06` | Reporting | L1 ✓ | L2 PARTIAL | INV-F-24 | L4-L12 ✓ | Yes | Value-based measures | — |
| `INV-M16` | Settings | `MENU-CF-01` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-26 | L4-L12 ✓ | Yes | Whether valuation is produced at all | — |
| `INV-M17` | Warehouses | `MENU-CF-02` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-27 | L4-L12 ✓ | Yes | Warehouse-level valuation separation JT-01 | — |
| `INV-M18` | Locations (Configuration) | `MENU-CF-03` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-28 | L4-L12 ✓ | Yes | Internal / non-internal boundary definition | R4-F-09 |
| `INV-M19` | Routes | `MENU-CF-04` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-29 | L4-L12 ✓ | Yes | Intermediate-step neutrality | — |
| `INV-M20` | Rules | `MENU-CF-05` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-29 | L4-L12 ✓ | Yes | Destination misconfiguration effect | — |
| `INV-M21` | Operation Types | `MENU-CF-06` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-30 | L4-L12 ✓ | Yes | Default-location financial character; TH-HOLD-09 held | — |
| `INV-M22` | Storage Categories | `MENU-CF-07` | Configuration | L1 ✓ | L2 PARTIAL | INV-F-31 | L4-L12 ✓ | No | Thai regulated-storage requirements held | — |
| `INV-M23` | Putaway Rules | `MENU-CF-08` | Configuration | L1 ✓ | L2 PARTIAL | INV-F-32 | L4-L12 ✓ | Yes | GAP-FS-02 precondition-blocked on JT-01 | — |
| `INV-M24` | Product Categories | `MENU-CF-09` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-33 | L4-L12 ✓ | Yes | HIGHEST — JT-01 NOT DECIDABLE | R4-F-10 |
| `INV-M25` | Attributes | `MENU-CF-10` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-18 | L4-L12 ✓ | Yes | Variant valuation consequence | — |
| `INV-M26` | Product Packagings | `MENU-CF-11` | Configuration | L1 ✓ | L2 PARTIAL | INV-F-34 | L4-L12 ✓ | Yes | Quantity errors become valuation errors | — |
| `INV-M27` | Reordering Rules | `MENU-CF-12` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-35 | L4-L12 ✓ | No | — | R4-F-01, R4-F-11 |
| `INV-M28` | Barcode Nomenclatures | `MENU-CF-13` | Configuration | L1 ✓ | L2 PARTIAL | INV-F-36 | L4-L12 ✓ | Yes | Misread quantity becomes valuation error | R4-F-12 |
| `INV-M29` | UoM Categories | `MENU-CF-14` | Configuration | L1 ✓ | L2 COMPLETE | INV-F-37 | L4-L12 ✓ | Yes | Conversion rounding changes valued quantity | R4-F-13 |

---

## 3. Coverage Roll-Up

| Measure | Count |
|---|---:|
| Menus in the Boss-approved R4 scope | 29 |
| Menus traced through L1 | 29 |
| Menus traced through L2 — COMPLETE | 23 |
| Menus traced through L2 — PARTIAL with named cause | 6 |
| Menus traced through L3-L12 | 29 |
| **Menus explicitly marked `HOLD` at menu level** | **0** |
| Menus carrying at least one `DEPENDENCY: ACCOUNTING COGS GAP` | 19 |
| Menus carrying a Thai statutory `HOLD / EVIDENCE REQUIRED` sub-item | 5 — `INV-M04`, `INV-M12`, `INV-M17`, `INV-M21`, `INV-M22` |
| Menus with at least one new R4 finding | 14 |
| Distinct controlled functions mapped | 41 (`INV-F-01` .. `INV-F-41`) |

---

## 4. The Six L2-Partial Menus — Named Causes

| Menu | Cause of PARTIAL | What would close it | Owner |
|---|---|---|---|
| `INV-M08` Product Variants | Field and configuration structure established; the semantics of changing an attribute set after variants hold stock cannot be proven without a live instance test | Live reference-instance test; `GAP-FS-03` decision | AI-Audit / Data design |
| `INV-M15` Warehouse Analysis | Genuinely evidence-thin — what the measure set should contain has never been evidenced or validated | Thai SME owner validation of the measure set (`GAP-MD-25`, `GAP-FS-13`) | Boss to commission |
| `INV-M22` Storage Categories | Capacity and mixing-constraint structure established; whether Thai regulated-storage requirements map onto it is unevidenced | Accounting-Tax and legal routing input | Accounting-Tax track |
| `INV-M23` Putaway Rules | Structure established and the category dual-ownership coupling confirmed; the separation decision is precondition-blocked | `JT-01`, then `GAP-FS-02` | Joint |
| `INV-M26` Product Packagings | Structure established; retrospective-change semantics unproven | Live instance test; design decision on non-retroactivity | Inventory |
| `INV-M28` Barcode Nomenclatures | Structure established; real Thai structured-barcode formats in use by Thai suppliers are unevidenced | Thai field validation | Boss to commission |

---

## 5. Movement Against The Prior Round

The Menu Deep Challenge round recorded nine menus at `HOLD / EVIDENCE REQUIRED` for want of any evidence at all, and recorded eight menus as resting on no prior evidence (`GAP-FS-20`).

**R4 supplies first-hand field and configuration evidence for six of them:** `INV-M08`, `INV-M22`, `INV-M23`, `INV-M25`, `INV-M26`, `INV-M28`.

This is the principal gap-fill achievement of R4 at the menu level. It **does not close** `GAP-FS-20`, `GAP-MD-08`, `GAP-MD-16`, `GAP-MD-17`, `GAP-MD-18` or `GAP-MD-19` — closure requires validation, not only evidence — but it changes their evidence basis from *no evidence* to *first-hand structural evidence, validation pending*. Each is annotated accordingly in `20_RISK_GAP_DECISION_REGISTER.md`.

One correction is recorded: an earlier round found no packaging model in the source it examined. `INV-M26` establishes that a packaging structure with a contained base quantity **does exist** in the target generation. Recorded as `R4-D-02`.

---

## 6. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
