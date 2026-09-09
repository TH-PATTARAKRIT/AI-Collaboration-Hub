# CONTEXT OWNERSHIP AND VISIBILITY MATRIX — ANCHOR COLUMN — CORR5 CONTROLLED PATCH

> **CONTROLLED PATCH NOTICE.** This file is the Phase SA controlled reading of the `Anchor` column of
> `MULTI_TENANT_INVARIANT_SET_EXECUTION/04_CONTEXT_OWNERSHIP_AND_VISIBILITY_MATRIX.md` (Inventory-owned,
> branch `design/inventory-mti-ruling-conformance-2026-09-05-001`), as amended by the R2 delta register
> (`CD-04`, `CD-12`, `CD-13`, `CD-14`). **The Inventory file is not modified.** This patch is the
> parallel-copy form the programme uses for another party's artefact; it governs Phase SA reading and
> is offered to the Inventory owner as the mechanical patch. Basis: `SA_CORR5_07` §1 (`M05-A1`),
> corrected by internal self-challenge `CHC-03`. Only rows whose anchor cell changes, is compound, or is
> empty are listed; the remaining 26 rows are unchanged single anchors.

**Legend rule (added):** *company is stored on every record (`MTI-05`); the `Anchor` column names the
single ancestor from which it derives, or `company` where it is assigned directly at creation.*

| Row | Object | R1 anchor cell | **Declared single anchor** | Basis |
|---:|---|---|---|---|
| 1 | Tenant | — | **root — legitimately anchorless** | `INV-PR-07` |
| 5 | Product | `tenant (definition) / company (attachment)` | **`company`** | `CD-04` |
| 7 | Product category | `tenant (structure) / company (costing facet)` | **`company`** (costing facet value `HOLD — COGS residual`) | `CD-12` |
| 8 | Lot / Serial | `company + product` | **`company`** — assigned at creation (`L8-10`/`-11`: *"Creation"*); R1 §4.1 itself states *"the anchor moves to `company` (entries 5, 7, 8)"*; `product` is an identity component, not the ancestor | R1 §4.1; `MTI-12` |
| 13 | Reordering rule | `company + location` | **`location`** (→ warehouse → company, `MTI-08`) | `MTI-08` |
| 14 | Put-away rule | `company + location` | **`location`** | `MTI-08` |
| 16 | Barcode nomenclature | `tenant` | **`company`** | `CD-13` |
| 17 | Unit group and unit | `tenant` | **`company` — CONDITIONAL on `CF-D-01`** (Boss: whether `MTI-D-03`'s *"Unit of Measure Category"* is this object). Until ruled the row has two possible anchors and `MTI-05` is **conditional on this row only** | `CD-14`; `CF-D-01` unruled |
| 21 | Inter-company transfer | — | **not an object — an `MTI-22` relationship (`XCR-01`)** between two single-context facts, each anchored to its own movement document (row 18) | R1 row 21; `MTI-44` |
| 22 | Count session (`CN-27`) · Inventory adjustment (`CN-28`) | `company + location` | **two objects, one ancestor each:** count session → **`warehouse`** (a session may span that warehouse's locations); adjustment (the application) → **`location`** | `L8-13`; `MTI-08` |
| 23 | Scrap | `company + location` | **`source location`** | `L8-14` |

**Result:** 35 rows; **34 carry exactly one declared anchor or a stated reason for none; 1 (row 17) is
conditional on Boss ruling `CF-D-01`.** `MTI-05` status: `SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED —
CONDITIONAL (CF-D-01, row 17)`.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
