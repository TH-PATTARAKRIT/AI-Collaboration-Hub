# 17 — Function Matrix

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `CONSOLIDATED MATRIX — MANY CELLS UNRESOLVED BY DESIGN, SEE FILE 24`

---

Columns per governing brief: Domain | Function | Source UI | Code | DB | GL | Accounting Rule | Thai Rule | Classification | Gap. `Code` and `DB` columns are `N/A — NO SOURCE ACCESS` throughout, per governing rule #3 (no code/DB access exists for this session) — this is stated once here rather than repeated as a hedge in every row; the column is retained per the required schema but its content is structurally fixed.

| Domain | Function | Source UI (reference-ERP doc) | Code | DB | GL | Accounting Rule | Thai Rule | Classification | Gap |
|---|---|---|---|---|---|---|---|---|---|
| Asset Model | Straight-line / declining / declining-then-straight-line method | Documented (file `03`) | N/A | N/A | Depreciation Expense / Accumulated Depreciation (documented, account defaults unconfirmed) | IAS 16 systematic allocation | HOLD (file `16`) | `FACT VERIFIED` (mechanism) | Account-default fallback unconfirmed |
| Asset Model | Prorata: no-prorata / constant-periods / based-on-days-per-period | Documented (file `07`) | N/A | N/A | n/a | IAS 16 (no day-count mandate) / Thai daily claim `SUPPORTED INTERPRETATION` (file `08`) | HOLD | `FACT VERIFIED` (existence) | Day-count convention unconfirmed |
| Asset Model | Not-Depreciable Value / residual exclusion | Documented (file `09`) | N/A | N/A | n/a | IAS 16 depreciable amount = cost − residual | n/a | `FACT VERIFIED` | none material |
| Asset | Depreciation board generation, modify-depreciation action | Documented (file `07`) | N/A | N/A | Journal per asset model (documented field, default unconfirmed) | IAS 16 change-in-estimate (prospective) | HOLD | `FACT VERIFIED` (mechanism) / `UNRESOLVED` (annual-review linkage) | Whether Modify fulfills annual-review requirement |
| Asset | Disposal, gain/loss | Documented generally (file `09`) | N/A | N/A | Gain/loss account (unconfirmed default) | IAS 16 proceeds − carrying value | HOLD (deductibility, gain treatment) | `SUPPORTED INTERPRETATION` | Exact posting mechanics unconfirmed |
| Equipment | Identity, category, company, used-by | Documented (file `04`) | N/A | N/A | n/a | n/a | n/a | `FACT VERIFIED` | none material |
| Equipment | Work Center link | Documented (file `04`) | N/A | N/A | n/a | n/a | n/a | `FACT VERIFIED` (existence) / `UNRESOLVED` (cardinality) | Enforced cardinality unconfirmed |
| Equipment | Asset (fixed-asset) link | Not documented natively (file `04`) | N/A | N/A | n/a | n/a | n/a | `CONTRADICTED` (of native-link assumption) | No native mechanism; SMEsPlus must build |
| Equipment | Product link | Not documented natively (file `04`/`05`) | N/A | N/A | n/a | n/a | n/a | `UNRESOLVED / EVIDENCE REQUIRED` | Leaning not-present |
| Equipment | Status/state enum | Not documented as single field (file `04`) | N/A | N/A | n/a | n/a | n/a | `UNRESOLVED / EVIDENCE REQUIRED` | No confirmed 7-state enum |
| Equipment | Usage/meter/runtime | Not documented (file `04`) | N/A | N/A | n/a | n/a | n/a | `UNRESOLVED / EVIDENCE REQUIRED` | — |
| Maintenance | Maintenance Request lifecycle, team assignment | Documented (file `04`, `06`) | N/A | N/A | n/a | n/a | n/a | `FACT VERIFIED` | — |
| Maintenance | Cost field on Maintenance Request | Not documented (file `06`) | N/A | N/A | n/a | n/a | n/a | `CONTRADICTED` (of assumption it exists) | Build new if required |
| Maintenance→Cost | Maintenance cost → Equipment/Work Center/WIP/MO/Product cost | Not documented (file `06`) | N/A | N/A | n/a | n/a | n/a | `CONTRADICTED` (of integration assumption) | Independent tracking only; no integration precedent |
| Work Center | Cost per hour (per-workcenter, per-employee, employee override, precedence) | Documented (file `12`) | N/A | N/A | n/a | IAS 2 overhead-absorption analogy (`SUPPORTED INTERPRETATION`, file `15`) | n/a | `FACT VERIFIED` | — |
| Work Center | Equipment cardinality | Not confirmed (file `04`/`11`) | N/A | N/A | n/a | n/a | n/a | `SUPPORTED INTERPRETATION` | Enforced constraint unconfirmed |
| Asset↔Equipment↔Work Center | Depreciation flow into Work Center cost | Not documented (file `11`) | N/A | N/A | n/a | IAS 2 normal-capacity constraint if adopted (file `15`) | n/a | `CONTRADICTED` (of the assumption a flow-through mechanism exists) | Original design required (Hypothesis A) |
| Product↔Equipment↔Asset | Automatic lineage from purchase/receipt | Not documented as single pipeline (file `05`) | N/A | N/A | Product/Bill→Asset path documented; Equipment path manual, separate | n/a | n/a | `CONTRADICTED` (of single-pipeline assumption) | Two disconnected paths; bridge is new design |
| Manufacturing Cost | Raw material, labor, work-center-rate absorption | Documented (partly carried from adjacent evidence, file `12`) | N/A | N/A | WIP/valuation accounts (documented generally, not re-verified fresh) | IAS 2 | HOLD | `SUPPORTED INTERPRETATION` | — |
| Manufacturing Cost | Depreciation-as-overhead, maintenance-as-overhead | Not documented (file `12`) | N/A | N/A | n/a | IAS 2 normal-capacity constraint (file `15`) | n/a | `CONTRADICTED` (of integration assumption) | Original design required |
| Off-Balance Costing | Non-GL internal usage ledger | Not confirmed present or absent with full confidence (file `14`) | N/A | N/A | Off-Balance account type (candidate) | Outside statutory scope by design (file `15`) | n/a | `UNRESOLVED / EVIDENCE REQUIRED` (reference-ERP precedent) / `DESIGN CANDIDATE` (SMEsPlus mechanism) | Precedent search incomplete; flagged, not closed |
| Post-Depreciation Usage | Residual Book Value × Original Rate ÷ Base formula | No precedent (file `13`) | N/A | N/A | Off-Balance (candidate) | No standards basis (by design, file `15`) | n/a | `DESIGN CANDIDATE` | Base choice (5 options) undecided |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
