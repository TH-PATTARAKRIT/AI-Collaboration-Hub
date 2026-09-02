# 18 — Migration, Data Quality and Reconciliation Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — MIGRATION IMPLICATIONS PER MENU — NOT A MIGRATION PLAN, NOT AUTHORIZATION`
Clean-room boundary: migration is defined as `Migrate Business Facts + Business Semantics Only`. Nothing here describes legacy schema, extraction code, or vendor structures. Reference facts are cited from reopen deliverables `06`, `11`, `12`.

Standing facts (carry-forward): zero migration/ETL code exists; the migration plan document is an unauthored placeholder; the reference source carries no external-ID/provenance field on stock records; no unified idempotency mechanism exists; empirical invariant-violation incidence in real data is blocked (`N-DB-01`); the studied dataset had 989 product rows violating the type invariant and 6.6% of products in a "lot-tracked but not fully ledgered" tier.

---

## 1. Migration Data Register by Menu

| Menu ID | Data that must be preserved (business facts) | Data that must NOT be migrated (architecture) | Reconciliation identity | Quality risks observed / expected | Status |
|---|---|---|---|---|---|
| MENU-CF-14 UoM | Unit groups, units, factors with effective dates, rounding policy | Vendor unit tree structure | unit code | Factor edits non-retroactive in source → historical quantities may not reproduce; rounding default up | CARRY_FORWARD |
| MENU-CF-09 Categories | Category tree; per-category valuation policy and history (Accounting) | Vendor account fields | category path | Only 3/3,980 categories overrode policy in studied data — most inherit; policy history may be absent | CARRY_FORWARD (Joint) |
| MENU-PR-01 Products | Code, names (Thai/English), barcode, kind (both axes), UoM, category, tracking, active, external ID | Vendor field model | product code + external ID | 989 rows kind-invariant violation; duplicates; archived rows with stock | CARRY_FORWARD (`GAP-MD-10` tie-break) |
| MENU-PR-02 / CF-10 Variants, Attributes | Attribute codes/values; variant ↔ legacy SKU map | Variant generation mode | attribute-value codes | No evidence (`GAP-MD-08`) | HOLD |
| MENU-PR-03 Lots/Serials | Lot/serial values, expiry dates, per-lot balances, supplier refs, history | Vendor lot model | product + lot/serial | Duplicate serials possible in source (reactive detection only); expiry fields present in dump schema | CARRY_FORWARD (`GAP-MD-11`) |
| MENU-CF-11 Packagings | Pack definitions (qty in base, barcode) | Unit-based representation | product + pack code | Packaging represented via units in source — mapping needed | HOLD (`GAP-MD-18`) |
| MENU-CF-13 Barcodes | Barcode values per product/pack/lot | Nomenclature rules | barcode | Overlapping formats | HOLD (`GAP-MD-19`) |
| MENU-CF-02 Warehouses | Code, name, address, company; branch attribute separately | Step-policy configuration objects | warehouse code | Warehouse ≠ tax branch (`GRPA-H8`) | CARRY_FORWARD |
| MENU-CF-03 Locations | Full path, type, warehouse, archive state | View-node internals | location path | Stock in view/virtual locations; orphan bins | CARRY_FORWARD |
| MENU-CF-06 Operation types | Document series, prefixes, last numbers | Picking-type object model | series code | Shared sequences across warehouses | CARRY_FORWARD |
| MENU-CF-04/05 Routes, Rules | Business policy statement per warehouse/product ("2-step receipt from date X") | Rule/route objects | policy id | Regenerated per tenant, never copied (`SAAS-04`) | CARRY_FORWARD |
| MENU-CF-07/08 Storage, Putaway | Optional: storage classes; putaway policy statements | Rule objects | class code | No evidence | HOLD |
| MENU-CF-12 Reordering | Min/max/route per product-location as policy | Reorder-rule objects | product + location | Rules on archived products / wrong UoM | CARRY_FORWARD |
| MENU-CF-01 Settings | Feature-switch set as tenant policy | Config parameters | company + version | Global bypass toggle state must not be migrated as "on" | CARRY_FORWARD |
| MENU-OP-03 Transfers | Done movements (history) or certified opening + history from cutover; open documents regenerated from orders; transit balances | Document/state model | source line + attempt (idempotency key) | Non-1:1 cardinality (source merges moves); orphaned lines (`ON DELETE SET NULL` class risk); duplicates on replay | CARRY_FORWARD (`C-02`) |
| MENU-OP-02 Adjustments | Historical adjustments with reason/approver; **opening balance at cutover as certified adjustment** | Conflict wizard state | adjustment number | `G-5`: no source mechanism for first opening balance — highest AI-fabrication risk | HOLD (Joint certification) |
| MENU-OP-04 Scrap | Scrap history with reasons; loss-location balances should be zero | Scrap document model | scrap number | Loss location holding balances | CARRY_FORWARD |
| MENU-OP-05 Landed cost | Cost history only (Accounting) | Allocation objects | receipt line | Not re-created | CARRY_FORWARD (Accounting) |
| MENU-OP-01/06 Replenishment, Scheduler | Nothing (regenerate) | Job state | — | Duplicate proposals if run before rules verified | N/A |
| MENU-RP-* Reports | Nothing (derived); **but** as-of-date snapshots at cutover for proof | Report definitions | period | Valuation report export defect in source (`G-7`) — export snapshots manually | CARRY_FORWARD |
| MENU-RP-05 Valuation | Closing quantity and value per product at cutover; costing method used; cost layers if FIFO (Accounting) | Valuation layer representation | product + period | Cross-proof to opening trial balance (`G-5`) | HOLD (Joint) |

---

## 2. Reconciliation Identities (candidate; human-approved formulas, deterministically computed)

| Rec ID | Identity | Level | Tolerance | Owner |
|---|---|---|---|---|
| REC-01 | Σ source on-hand per product (base UoM) = Σ target on-hand per product | product | 0 | Migration / Inventory |
| REC-02 | Σ per (product, location, lot) source = target | bin | 0 | Migration / Inventory |
| REC-03 | Source movement count (after documented cardinality transform) = target movement count | movement | 0 after transform table | Migration |
| REC-04 | Opening qty + Σ in − Σ out ± adjustments = closing qty (per product, per period) after replay | period | 0 | Inventory |
| REC-05 | Σ target opening value = Accounting opening trial balance inventory account | company | 0 (or explained) | **Joint (`G-5`)** |
| REC-06 | Every target record has exactly one provenance key; every source key maps to at most one target | record | 0 | Migration (`GAP-MD-27`) |
| REC-07 | No target record readable outside its company | record | 0 | Track 07 / SaaS |
| REC-08 | Serial uniqueness per product per company | serial | 0 | Inventory |
| REC-09 | Checksum of migrated batch = checksum of extracted batch | batch | exact | Migration (SHA-256 discipline) |
| REC-10 | UoM conversions of historical lines reproduce source base quantities | line | rounding policy | Inventory |

AI role: narrate already-computed results; never compute, adjust, or assert a reconciliation (reopen `11`).

---

## 3. Data Quality Rules (candidate acceptance for Team A profiling; not authorized here)

| DQ ID | Rule | Source of concern |
|---|---|---|
| DQ-01 | Product kind axes consistent; tie-break documented; violations quarantined not auto-fixed | 989-row violation (reopen `12`) |
| DQ-02 | No duplicate product by (code) or (barcode); near-duplicates by name reviewed by human | Common Thai SME data |
| DQ-03 | No stock in non-internal locations except transit; loss/adjustment locations zero | Location semantics |
| DQ-04 | No negative on-hand without explicit tenant policy | Clamped negatives in source |
| DQ-05 | No duplicate bins; no duplicate serials | No unique index in source |
| DQ-06 | No orphaned movement lines | FK behaviour in source |
| DQ-07 | Every lot-tracked product's on-hand fully allocated to lots | Partial-rigor tier |
| DQ-08 | Expiry date present for expiry-tracked lots | Expiry fields present but workflow unread |
| DQ-09 | UoM factors valid; no cross-group conversions | UoM facts |
| DQ-10 | Live distinct-value check of kind axes per tenant at cutover (not one-time sample) | reopen `12` `GRPA-M14` |

---

## 4. Migration Gaps and Gate Impact

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-27 | Provenance / external-ID map must be originated | Track 04, 09 / S9 | Precondition for any migration authorization |
| GAP-MD-26 | Package migration disposition (live / history / both) | Track 04 / S9 | Team B precondition (conditional) |
| GAP-MD-10 | Kind tie-break rule | Track 03 / S2 | Team B precondition |
| GAP-MD-28 | Cardinality transform table and orphan quarantine rules | Track 04, 09 / S9 | Precondition for migration authorization |
| C-02 | Idempotency key severity/ownership | Boss | Boss decision |
| G-5 / U-04 | Opening balance certification | Joint | Blocks Joint Backbone publication and migration |
| N-DB-01 | Empirical incidence testing | Team A | Bounded verification |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
