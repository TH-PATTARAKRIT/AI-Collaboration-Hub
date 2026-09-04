# 12 — MANUFACTURING COST CLASSIFICATION MATRIX (LEVEL 14)

**LAYER 2 — AUDIT QUARANTINE.**

The prompt's instruction is explicit: *do not treat these as the same taxonomy.* This
report establishes that there are **three** independent taxonomies in play, that
conflating any two of them is the source of a specific class of error, and that the
reference product itself already separates two of them and merges the third.

---

## 1. Three axes, not one

| Axis | Values | Governs | Where it lives |
|---|---|---|---|
| **A — Traceability** | Direct / Indirect | Whether a cost attaches to a unit without allocation | Management accounting |
| **B — Cost behaviour** | Fixed / Variable | **The allocation basis required by TAS 2 ¶13** | Accounting standard |
| **C — Item nature** | Goods / Service, and separately Storable / Not storable | Whether a thing is inventoried at all | Product master |

**These are orthogonal.** Machine depreciation is *indirect* (A), *fixed* (B), and is
not an item at all (C). Direct materials are *direct*, *variable*, and *storable*.
Subcontract service is *direct*, *variable*, and a *service* that is nonetheless
capitalised into inventory.

### The error each conflation produces

| Conflation | Error |
|---|---|
| A with B | Treating "indirect" as a synonym for "overhead to be spread", and spreading it on actual output — **exactly the TAS 2 ¶13 breach in `09` §2** |
| B with C | Assuming only storable items enter inventory value. Services and depreciation both enter conversion cost |
| A with C | Assuming direct cost means material. Direct labour and subcontracting are direct and are not goods |

## 2. What the reference product actually models

A correction to a common assumption, verified from source this session:

**"Storable / Consumable / Service" is not a single three-way choice in this platform
generation.** The product master carries:

- a **type** of *Goods*, *Service*, or *Combo*, and
- a separate **storability** boolean.

So *consumable* is not a type — it is *Goods* that is not storable. The taxonomy is
two-dimensional. Any design that models a three-valued enumeration will fail to
represent a real configuration.

Valuation is a third, independent axis, held on the product **category**: a costing
method (standard / FIFO / average) and a valuation mode (manual/periodic or real-time).
`08` §3 shows both of these gate whether machine cost reaches inventory at all.

**What the product does not model at all is axis B.** There is no fixed/variable
distinction anywhere in the manufacturing cost chain. The single work-centre hourly rate
merges both classes into one number (`07` §6). This is the specific reason the reference
product cannot comply with TAS 2 ¶13, and it is a modelling gap, not a configuration gap.

## 3. The classification matrix

For each cost element: its position on all three axes, its destination, and its
statutory basis.

| Cost element | A | B | C | Destination | Basis |
|---|---|---|---|---|---|
| Direct material | Direct | Variable | Storable goods | **WIP → FG** | TAS 2 ¶11 — purchase cost |
| Indirect material / consumables | Indirect | Variable | Goods, not storable | **WIP → FG** | TAS 2 ¶12 — variable overhead |
| Direct labour | Direct | Variable | — | **WIP → FG** | TAS 2 ¶12 — directly related |
| Indirect labour, factory supervision | Indirect | **Fixed** | — | **WIP → FG, on normal capacity** | TAS 2 ¶12 — factory management |
| Utilities — output-driven (power to machines) | Indirect | Variable | — | **WIP → FG, on actual use** | TAS 2 ¶12–13 |
| Utilities — standing (lighting, standing charges) | Indirect | **Fixed** | — | **WIP → FG, on normal capacity** | TAS 2 ¶13 |
| **Machine depreciation — production assets** | Indirect | **Fixed** | — | **WIP → FG, on normal capacity** | **TAS 2 ¶12 — named expressly** |
| Machine depreciation — **non-production** assets | — | Fixed | — | **Period expense** | TAS 16 — outside conversion cost |
| Factory building depreciation | Indirect | **Fixed** | — | **WIP → FG, on normal capacity** | **TAS 2 ¶12 — named expressly** |
| Right-of-use asset depreciation, production | Indirect | **Fixed** | — | **WIP → FG, on normal capacity** | **TAS 2 ¶12 — named expressly** |
| Maintenance — **planned**, production equipment | Indirect | **Fixed** | — | **Absorbed via the rate** (`09` §6) | TAS 2 ¶12–13 |
| Maintenance — **unplanned** / breakdown | Indirect | Fixed | — | **Period expense** | TAS 2 ¶13 — unallocated |
| Subcontract / outside processing | Direct | Variable | Service | **WIP → FG** | TAS 2 ¶15 — other cost to bring to present condition |
| Inbound transport on materials | Direct | Variable | Service | **WIP → FG** | TAS 2 ¶11 — purchase cost |
| Outbound transport / delivery | — | Variable | Service | **Period expense** | Not a cost of bringing inventory to its present condition |
| Franchise / royalty on production | Depends | Depends | Service | **Requires case analysis** — see §4 | TAS 2 ¶15 |
| Franchise / royalty on sales | — | Variable | Service | **Period expense** | Selling cost |
| **Internal equipment usage** (`BD-01`) | Indirect | Fixed | — | **Management ledger only — never WIP, FG or expense** | No statutory basis; original design (`10`) |
| Abnormal waste, abnormal idle capacity | — | — | — | **Period expense** | TAS 2 ¶13 and ¶16 |
| Administrative overhead | — | Fixed | — | **Period expense** | TAS 2 ¶16 — unless it brings inventory to its present condition |
| Selling cost | — | — | — | **Period expense** | TAS 2 ¶16 |

## 4. The two rows that need judgement rather than a rule

**Franchise / royalty on production.** Whether a production-based royalty is a cost of
conversion depends on what it buys. A per-unit licence to manufacture is arguably a cost
of bringing inventory to its present condition; a general trade-mark fee is not. **This
is a case-by-case determination and the design must permit both treatments per contract**
rather than fixing one. Marked `UNRESOLVED — policy per contract`, not blocking.

**Depreciation of assets used partly in production.** TAS 2 ¶12 covers assets *used in
the production process*. A vehicle used half for deliveries and half for plant movements
is neither wholly in nor wholly out. The reference product's asset grouping object
carries **no behaviour** (`05` §2), so there is nowhere to record a production/non-
production classification today. `19` §2 requires SMEsPlus to add one, as a first-class
attribute of the asset, because it is the gate that decides whether an asset enters the
costing model at all.

## 5. Non-productive causes → destination

Completing `09` §4 with the accounting destination of each cause.

| Cause | Destination | Note |
|---|---|---|
| MAINTENANCE — planned | Absorbed through the rate | Not a posting; a denominator reduction |
| MAINTENANCE — unplanned | Period expense | |
| BREAKDOWN | Period expense | |
| SETUP | Productive (candidate) — absorbed | Boss decision pending |
| STOPPAGE | Period expense | |
| NO_DEMAND | Period expense | |
| IDLE | Period expense | Where abnormal, TAS 2 ¶13 requires expensing; where within normal capacity it is already in the denominator |
| OTHER | Period expense, **and reported** | A non-zero balance means evidence is missing |

Account codes are a chart-of-accounts decision. The **classification** is the research
finding; the **coding** is not.

## 6. What SMEsPlus must model that the reference product does not

1. **Axis B — fixed versus variable — as a first-class attribute of every cost element.**
   Without it TAS 2 ¶13 cannot be implemented at all.
2. **A production / non-production classification on the asset**, gating entry to the
   costing model.
3. **A planned / unplanned distinction with a costing consequence** — the data exists
   (`06` §4), the consequence does not.
4. **A normal-capacity register per machine**, dated (`11` §6).
5. **Two rate derivations**, one per cost class, rather than one merged scalar.
