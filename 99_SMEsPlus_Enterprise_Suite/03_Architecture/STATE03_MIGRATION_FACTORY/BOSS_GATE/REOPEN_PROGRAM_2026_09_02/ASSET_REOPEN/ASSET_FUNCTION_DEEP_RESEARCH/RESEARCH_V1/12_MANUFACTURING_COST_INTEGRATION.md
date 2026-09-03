# 12 — Manufacturing Cost Integration

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION`

---

## 1. Scope

Per governing brief research object 10: the full manufacturing cost stack (raw material + labor + work center + equipment + service + overhead + depreciation + maintenance → WIP → FG → COGS), each component classified as directly-supported / manually-configured / automatic / allocated / absorbed / variance / not-supported in the reference ERP.

## 2. Cost Component Classification

| Component | Reference-ERP evidence | Classification | Fact Status |
|---|---|---|---|
| Raw material cost | Documented: consumed component cost flows into manufacturing order cost via the components list, valued per the product's costing method (well-evidenced generally in the sibling COGS research; not re-litigated here). | Directly-supported / automatic | `SUPPORTED INTERPRETATION` (carried from adjacent evidence base, not re-verified fresh this session) |
| Direct labor | Documented via employee hourly-cost field feeding work-center per-employee rate. | Directly-supported / manually-configured (a rate a user enters) | `FACT VERIFIED` |
| Work center operating cost | Documented per-workcenter hourly rate, precedence over per-employee rate. | Directly-supported / manually-configured | `FACT VERIFIED` |
| Equipment-specific cost (distinct from work center cost) | No distinct documented field found — Equipment does not appear to carry its own cost-per-hour separate from its Work Center's rate. | Not-supported (as a distinct line item) | `UNRESOLVED / EVIDENCE REQUIRED`, leaning not-present |
| Service/subcontracting cost | Not independently investigated in this session beyond general reference-ERP familiarity that subcontracted operations are a documented manufacturing concept elsewhere; not re-confirmed here. | Manually-configured (plausible) | `UNRESOLVED / EVIDENCE REQUIRED` |
| Manufacturing overhead (general) | Work center cost-per-hour functions as the primary documented overhead-absorption vehicle (labor+machine rate blended); no separate overhead-allocation-rate feature beyond that was located. | Absorbed via work-center rate | `SUPPORTED INTERPRETATION` |
| Depreciation-as-overhead | No documented mechanism connects Asset depreciation to work center or product cost (file `11` §3). | Not-supported | `CONTRADICTED (of the assumption it is supported)` |
| Maintenance cost | No documented mechanism connects Maintenance Request cost to product/work-center/WIP cost (file `06`). | Not-supported (tracked independently, if at all) | `CONTRADICTED (of the assumption it is supported)` |
| WIP | Documented generally elsewhere (production-location-based clearing, per the sibling COGS package's independent finding — not re-verified fresh in this session, cited for consistency only). | Directly-supported | `SUPPORTED INTERPRETATION` (not fresh evidence this session) |
| Finished-goods valuation / COGS | Same caveat — out of this session's fresh-evidence scope; the asset/equipment/maintenance components (the actual assignment) are the fresh contribution of this file. | n/a to this session's scope | n/a |
| Variance (standard-cost manufacturing variance) | Prior COGS research (cited, not re-verified) found no documented production-variance-posting mechanism for standard-cost manufacturing in the reference ERP. Consistent finding carried forward as context, not re-proven here. | Not-supported (per prior finding) | `SUPPORTED INTERPRETATION` (carried, not fresh) |

## 3. Headline Reading

Of the eight cost-stack components in the governing brief's list (raw material, labor, work center, equipment, service, overhead, depreciation, maintenance), this session's fresh evidence covers **labor, work center, equipment, depreciation, and maintenance** directly, and the finding is stark: **the two components most central to this research session's purpose — depreciation and maintenance — are the two with no documented integration mechanism at all**, while the pre-existing, already-evidenced components (raw material, labor, work center rate) are well-supported. This is not a coincidence to be smoothed over: it means the Asset Model/Equipment/Maintenance domain sits structurally outside the reference ERP's documented manufacturing-cost machinery, and any SMEsPlus integration is new design work by evidence, not adaptation.

## 4. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`: depreciation-as-overhead and maintenance-cost-as-overhead should both be modeled as **explicit, separately-added inputs** to the work-center cost-per-hour calculation (or an equivalent allocation mechanism), analogous in shape to the existing per-workcenter/per-employee rate inputs, but understood from the outset as original construction, not reference-ERP adaptation.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
