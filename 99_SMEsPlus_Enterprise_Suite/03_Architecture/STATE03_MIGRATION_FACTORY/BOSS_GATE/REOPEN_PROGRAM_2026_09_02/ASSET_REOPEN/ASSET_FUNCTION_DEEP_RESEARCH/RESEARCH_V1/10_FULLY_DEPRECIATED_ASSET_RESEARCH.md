# 10 — Fully Depreciated, Still-Productive Asset Research

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — HYPOTHESIS C EVALUATION`

---

## 1. Scope

Per governing brief research object 08 and Boss Hypothesis C (P04): a fully depreciated but still-productive piece of equipment may still carry non-zero internal economic usage cost. This file covers the accounting-principle side (normal capacity / idle capacity / useful-life review under IAS/TAS 16) and evaluates Hypothesis C against it. The mechanism-design side (the formula itself) is deferred to file `13`; this file is the principle-research foundation for that evaluation.

## 2. Accounting Principle Research

| Principle | Source | Finding | Classification |
|---|---|---|---|
| Once an asset is fully depreciated (book value = residual value), **no further depreciation expense is recognized**, regardless of continued use, under both the reference-ERP mechanism (file `07`/`09`) and IAS 16 (depreciation stops when the asset is fully depreciated or derecognized, whichever is earlier). | IAS 16 (direct); reference-ERP documented formula (direct) | Convergent, standards-level and system-level | `FACT VERIFIED` |
| Useful life must be reviewed at least annually; if an asset is still productive well past its originally estimated useful life, that is itself a signal the original useful-life estimate may need revision (prospectively), per IAS 16's change-in-estimate mechanism. | IAS 16 (direct) | This is the standards-level *response* to a fully-depreciated-but-still-productive asset: revise the estimate, don't invent a new expense category. | `FACT VERIFIED` (standards-level) |
| Normal capacity / idle capacity: IAS 2 (inventory) allocates *production overhead* based on normal capacity, treating unabsorbed overhead from below-normal (idle) production as a period expense rather than capitalizing it into inventory cost. This is the closest standards-level analogue to "should a fully depreciated machine's continued operation carry an internal cost," but it addresses **overhead absorption during production**, not a **post-depreciation internal usage charge** on an individually zero-book-value asset. | IAS 2 (general professional knowledge; not independently re-fetched with a URL in this session — flagged) | The concepts are adjacent, not identical | `SUPPORTED INTERPRETATION` |

## 3. Hypothesis C Evaluation

Boss Hypothesis C, restated: a fully depreciated machine may still have non-zero internal economic usage cost.

- **As a management/cost-accounting concept** (i.e., "this machine still consumes real economic value — wear, opportunity cost, energy, capacity — even though its statutory book value is zero, and management wants visibility into that"), Hypothesis C is **directionally consistent** with well-established managerial-accounting practice (opportunity cost, economic depreciation vs. accounting depreciation are long-recognized as distinct concepts in general accounting theory), though this file did not locate a citation naming this exact practice under any authoritative standard-setter source. `SUPPORTED INTERPRETATION`.
- **As a statutory/financial accounting concept**, Hypothesis C has **no support** — IAS 16 is explicit that depreciation stops at full depreciation, and there is no standards-level mechanism to recognize a *new* expense for continued use of a fully depreciated, already-recognized asset. Any implementation of Hypothesis C must, per IAS 16, stay entirely outside the statutory P&L/balance sheet — which is precisely why the Boss's own Off-Balance accounting model pairs with this hypothesis (file `14`). This convergence (Hypothesis C requires an off-balance mechanism, and the Boss independently proposed one) is evidence the two hypotheses are coherently linked, not that either is independently verified as correct design.
- **Reference-ERP precedent**: none located. No documentation page describes any "shadow cost" or "internal usage cost" feature for fully depreciated assets. This is expected — it is a non-statutory management concept unlikely to appear in a fixed-asset module whose entire documented purpose is statutory-adjacent depreciation scheduling.

## 4. Classification

`DESIGN CANDIDATE`. Hypothesis C is not a verified accounting fact and is not contradicted by any authoritative source located — it occupies a legitimate but currently ungoverned management-accounting space that IAS/TAS 16 deliberately does not address (because IAS/TAS 16 is a statutory-reporting standard, not a management-costing standard). Its accounting soundness depends entirely on execution discipline: it must never touch statutory accounts (file `14`'s Off-Balance requirement is doing real work here, not decoration).

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
