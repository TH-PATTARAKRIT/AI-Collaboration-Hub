# 03 — Asset Model Function Forensic

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION`

---

## 1. Scope

Forensic review of the reference ERP's asset-model-equivalent (the template/policy record that an individual Asset instance is created from), per governing brief research object 04. Layer A = reference-ERP public documentation. Layer B = Thai statutory (routed to files `08`/`16`). Layer C = SMEsPlus candidate semantics.

---

## 2. Field-by-Field Forensic

| Field (business term) | Reference-ERP evidence | Classification |
|---|---|---|
| Depreciation method: Straight Line | Documented: divides Depreciable Value by number of depreciations planned; equal-amount entries. | `FACT VERIFIED` |
| Depreciation method: Declining | Documented: multiplies Depreciable Value by a Declining Factor each entry; final entry is a balancing amount, not factor-based. | `FACT VERIFIED` |
| Depreciation method: Declining Then Straight Line | Documented: applies Declining Method with a floor equal to what Straight Line would produce, so it switches to straight-line once that floor is reached. | `FACT VERIFIED` |
| Computation method: No Prorata | Documented as an option distinct from prorata computation. Exact behavior (whole-period-from-policy-start vs. whole-period-from-acquisition) not independently quoted in this session's retrieval. | `SUPPORTED INTERPRETATION` |
| Computation method: Constant Periods | Documented as a prorata sub-option. | `FACT VERIFIED` (existence) / `UNRESOLVED / EVIDENCE REQUIRED` (exact day-weighting formula) |
| Computation method: Based on Days per Period | Documented as a prorata sub-option — first depreciation entry computed from the actual acquisition date rather than the first of the fiscal year/policy start, implying day-level granularity exists as a documented option. This is directly relevant to file `08`'s Thai daily-depreciation question: the reference ERP demonstrably supports day-based prorata as one of several configurable options, not as the sole or default method. | `FACT VERIFIED` (existence and general shape) / `UNRESOLVED / EVIDENCE REQUIRED` (exact day-count convention — 30/360, actual/365, actual/actual) |
| Not-Depreciable Value (residual/salvage) | Documented: Depreciable Value = Original Value − Not Depreciable Value; this carve-out is excluded from the depreciation schedule entirely, i.e., it is never depreciated. | `FACT VERIFIED` |
| Fixed Asset account / Accumulated Depreciation account / Depreciation Expense account | Documented as configurable fields on the asset-model-equivalent record (naming per official documentation: an asset account, a depreciation account, an expense account are each separately configurable). Exact three-way default/fallback behavior when left blank not retrieved. | `SUPPORTED INTERPRETATION` (existence) / `UNRESOLVED / EVIDENCE REQUIRED` (blank-field fallback) |
| Journal | Documented as a configurable field for where depreciation entries post. | `SUPPORTED INTERPRETATION` |
| Analytic distribution | Not independently confirmed in this session's asset-specific retrieval (analytic/cost-center distribution is a documented reference-ERP concept generally, but its specific presence on the asset-model-equivalent record was not directly quoted). | `UNRESOLVED / EVIDENCE REQUIRED` |
| Company (multi-company scoping) | Not independently re-confirmed for the asset-model-equivalent record in this session (multi-company scoping is a documented pattern elsewhere in the reference ERP, e.g. Chart of Accounts, but its specific application to asset-model records was not directly quoted here). | `UNRESOLVED / EVIDENCE REQUIRED` |

---

## 3. Inheritance to Asset Instance

`SUPPORTED INTERPRETATION`: the reference-ERP pattern (well-established across its other template/instance relationships, e.g. Product Category → Product) is that an asset-model-equivalent record supplies defaults that an Asset instance inherits and may override at creation time. This specific inheritance-and-override behavior was not independently re-quoted for the asset module in this session's retrieval; it is inferred by structural analogy to the reference ERP's general design pattern, not directly evidenced for this module. Marked `UNRESOLVED / EVIDENCE REQUIRED` as a standalone claim, `SUPPORTED INTERPRETATION` only as an analogy-based expectation.

## 4. Effective-Dating and Multi-Company Constraints

`UNRESOLVED / EVIDENCE REQUIRED` on both counts. No documentation page retrieved in this session states whether an asset-model-equivalent record supports effective-dated policy versions (e.g., "this depreciation method applies to assets created after date X") or whether an existing Asset re-reads its Asset Model's current field values versus freezing them at creation time. This is a materially important question for SMEsPlus (a policy change should not silently retroactively alter an in-flight Asset's schedule) and is flagged to file `24` as a priority unresolved item.

## 5. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`: SMEsPlus should treat the Asset Model as a template that Asset instances copy field values from at creation time (not a live reference), consistent with the reference ERP's general template/instance pattern elsewhere, so that a later Asset Model edit does not retroactively alter an existing Asset's depreciation schedule. This candidate is explicitly not confirmed as the reference ERP's actual behavior for this specific module (§4) — it is offered as a control-conscious default pending confirmation, and must be independently decided by SMEsPlus, not copied blind.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
