# 11 — Asset ↔ Equipment ↔ Work Center Lineage

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — MECHANISM CHALLENGE`

---

## 1. Scope

Per governing brief research object 09: cardinalities across Asset↔Equipment↔Work Center, and whether depreciation currently flows into Work Center cost in the reference ERP — prove the mechanism if yes, prove its absence and nearest existing mechanism if no.

## 2. Cardinality Consolidation (from files 04, 07)

| Pair | Cardinality evidence | Classification |
|---|---|---|
| Asset ↔ Equipment | No native link located (file `04` §2). Cardinality is moot without a link. | `UNRESOLVED / EVIDENCE REQUIRED`, leaning `NOT PRESENT NATIVELY` |
| Equipment ↔ Work Center | Documented field exists; exact enforced cardinality not confirmed; many-Equipment-to-one-Work-Center is the more plausible real-world reading (file `04` §3). | `SUPPORTED INTERPRETATION` |
| Asset ↔ Work Center | No direct link of any kind located — this would necessarily route through Equipment (Asset→Equipment→Work Center), and the first leg of that chain is unconfirmed. | `UNRESOLVED / EVIDENCE REQUIRED` |

## 3. Does Depreciation Flow Into Work Center Cost?

**Direct challenge, answer: no confirmed mechanism, and the negative case is reasonably well evidenced.**

- Work Center cost is documented as composed of two rate inputs: a per-workcenter hourly rate and a per-employee hourly rate (with individual employee override), feeding an operation's calculated cost as rate × duration. Both inputs are **labor/machine-time-rate** concepts, manually set by a user filling in a number — not derived from, or connected to, any Asset's depreciation schedule.
- No documentation page located describes a work center's cost-per-hour field being computed from, linked to, or automatically updated by an Asset's depreciation entries.
- Given the Asset↔Equipment link itself is unconfirmed to exist (§2), a depreciation→Work-Center-cost flow would require **two** unconfirmed links to chain together (Asset→Equipment, and Equipment→Work-Center-cost-integration), making the absence finding more, not less, confident by compounding.

**Finding: `CONTRADICTED (of the assumption that depreciation flows into Work Center cost in the reference ERP)`.** This is the single most consequential negative finding for Hypothesis A (file `21`) — the reference ERP provides no adaptable precedent for the mechanism Hypothesis A envisions.

## 4. Nearest Existing Mechanism (What SMEsPlus Would Be Extending, Not Adopting)

The nearest existing mechanism is the Work Center's manually-set Cost per Hour field itself. If SMEsPlus wants depreciation to influence work center cost, the closest analogy is: treat a derived "depreciation-per-hour" figure the same way the reference ERP treats a manually-entered labor rate — i.e., as an additional input to the same per-hour cost calculation — but this is a **structural extension SMEsPlus would have to design and build**, not a pattern being adapted from observed reference-ERP behavior, because no such input exists there today.

## 5. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`, `EXTEND` classification in file `23`'s terms: SMEsPlus should build an explicit Asset↔Equipment↔Work Center chain (all three links, since none is confirmed to exist end-to-end in the reference ERP) as new design work, informed by — but not copied from — the reference ERP's Work Center cost-per-hour pattern as the closest structural analogy for where a depreciation-derived rate could plug in.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
