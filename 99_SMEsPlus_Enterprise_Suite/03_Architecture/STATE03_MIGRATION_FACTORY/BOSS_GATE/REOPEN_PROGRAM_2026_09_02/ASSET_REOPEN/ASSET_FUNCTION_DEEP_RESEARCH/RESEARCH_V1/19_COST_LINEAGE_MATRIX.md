# 19 — Cost Lineage Matrix

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `CONSOLIDATED MATRIX — TWO PARALLEL LINEAGES, ONE EVIDENCED WEAKLY, ONE PURELY CANDIDATE`

---

Per governing brief: Asset→Equipment→Work Center→Operation→MO→Product→WIP→FG→COGS, worked for both (A) financial depreciation and (B) post-depreciation internal residual usage.

## Lineage A — Financial (Statutory) Depreciation

| Stage | Link evidenced? | Classification |
|---|---|---|
| Asset (depreciation schedule exists and posts) | Yes | `FACT VERIFIED` |
| Asset → Equipment | No native link located | `UNRESOLVED / EVIDENCE REQUIRED`, leaning `NOT PRESENT NATIVELY` |
| Equipment → Work Center | Field exists, cardinality unconfirmed | `SUPPORTED INTERPRETATION` |
| Work Center → Operation (cost per hour × duration) | Yes, documented | `FACT VERIFIED` |
| Operation → Manufacturing Order cost | Yes, documented generally | `SUPPORTED INTERPRETATION` (carried context) |
| MO → Product (WIP/FG valuation) | Yes, documented generally (not re-verified fresh this session) | `SUPPORTED INTERPRETATION` (carried context) |
| Product (FG) → COGS | Yes, documented generally (not re-verified fresh this session) | `SUPPORTED INTERPRETATION` (carried context) |
| **Does depreciation itself enter this chain anywhere?** | **No confirmed entry point.** The chain from Work Center onward is evidenced for labor/machine-time cost, but nothing in the evidence shows a depreciation figure being added to the Work Center's cost-per-hour or otherwise injected into this lineage. | `CONTRADICTED` (of the assumption depreciation flows through this lineage today) |

**Reading**: Lineage A exists and is well-evidenced for ordinary manufacturing cost (labor/machine-time), but **depreciation is not shown to participate in it at all** under current reference-ERP evidence. The break is at the very first link (Asset→Equipment) and is never bridged downstream either. This is the single clearest, most load-bearing negative finding in this whole package for evaluating Hypothesis A.

## Lineage B — Post-Depreciation Internal Residual Usage

| Stage | Status |
|---|---|
| Asset reaches full depreciation | `FACT VERIFIED` mechanism exists (file `07`, `09`) |
| Post-depreciation formula computes an internal usage figure | `DESIGN CANDIDATE` only (file `13`) — no reference-ERP or standards precedent |
| Figure attributed to Equipment | Requires the same unconfirmed Asset→Equipment link as Lineage A | `UNRESOLVED / EVIDENCE REQUIRED` (dependency) |
| Figure attributed to Work Center | Requires the same unconfirmed Equipment→Work-Center-cost-integration as Lineage A | `UNRESOLVED / EVIDENCE REQUIRED` (dependency) |
| Figure posted Off-Balance (Dr Internal Usage Cost / Cr Internal Usage Offset) | `DESIGN CANDIDATE` (file `14`) — no reference-ERP precedent confirmed either way with full confidence |
| Figure influences Operation/MO/Product/WIP/FG/COGS cost | **Explicitly should not**, if the Off-Balance control design (file `14`) is followed correctly — the entire point of the Off-Balance mechanism is to keep this lineage's downstream stages statutorily unaffected. This is a *design requirement*, not evidence of current behavior. | `DESIGN CANDIDATE` (constraint) |

**Reading**: Lineage B is entirely candidate/design work from its second stage onward. It shares Lineage A's foundational gap (no confirmed Asset→Equipment→Work-Center chain) and adds its own gap (no confirmed off-balance-mechanism precedent). Both lineages converge on the same root blocker: **the Asset↔Equipment link is the single most consequential missing evidence point in this entire research package** — it is a prerequisite for both the statutory question (Hypothesis A) and the management-costing question (Hypotheses B/C, the post-depreciation formula).

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
