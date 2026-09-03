# 27 — MRP / ASSET COSTING EXTENSION RESEARCH
**LAYER 2 — AUDIT QUARANTINE**

§44–§49 and §52. This is where the SMEsPlus differentiator lives, so the deliverable
separates **what exists**, **what is verifiably absent**, and **what would have to be
designed** — and does not blur them.

## 1. What exists — the production cost chain, in full

Traced end to end in primary source. Reproduced from `08` §6 with the mechanism
detail:

| # | Link | Mechanism | Status |
|---|---|---|---|
| 1 | Work Center → hourly rate | `costs_hour`, a **manually entered float, default 0.00** | Exists |
| 2 | Rate → Work Order cost | `duration ÷ 60 × rate`. The rate is **snapshotted onto the work order at creation** | Exists |
| 3 | Work Order → analytic | Analytic lines from the **work centre's** distribution, hours as unit amount, category *manufacturing order*, rewritten whenever duration changes | Exists |
| 4 | Work Order → FG valuation | `Σ work-order costs + extra unit cost − Σ consumed material value` → the finished move's unit price → stock valuation layer. By-products take their configured cost share first | Exists |
| 5 | Work-centre cost → GL | On completion: credit the **work centre's expense account** (falling back to the product's), debit the stock source account. **Only when the product is real-time valued** | Exists, conditional |
| 6 | FG → COGS | Ordinary stock valuation | Exists |

**Links 2–6 are complete, implemented and reusable.** This is the correction that
most changes the size of the SMEsPlus build.

`FACT VERIFIED`

## 2. What is verifiably absent

| ID | Gap | Evidence |
|---|---|---|
| `GAP-01` | **Depreciation → the hourly rate.** Nothing derives, suggests or validates the rate | Exhaustive search: zero references to the asset model from any manufacturing module |
| `GAP-02` | **Equipment → cost, anywhere.** The equipment record carries one inert float | `20` §1 |
| `GAP-03` | **Operation → Equipment.** An operation names a work centre and has no equipment field | `08` §3 |
| `GAP-04` | **Maintenance → cost.** No monetary field on a maintenance request at all | `08` §5 |
| `GAP-05` | **Absorption variance.** Nothing computes, reports or posts absorbed-versus-actual | Raised by Expert 3 at Level 4, accepted |
| `GAP-06` | **Idle / downtime cost.** Not recorded | `12` §4 |

All six are `VERIFIED SOURCE GAP` — established by exhausting the search space, not
by failing to find something. Per §85, the search stops here: the mechanism is
proven absent and continuing to look for it is waste.

## 3. The toll-gate concern — §45, adjudicated

The Boss's concept: *whoever uses the machine receives that machine's cost; whoever
does not, must not.*

**The concern is structurally correct.** The model is:

```
Operation ──► Work Center ◄── Equipment (many)
```

There is no edge from a job to a machine. Any allocation over this model **must**
average across every machine in the work centre. The Boss's objection is an accurate
reading of a real limitation, not a misunderstanding.

`VERIFIED SOURCE GAP` — and `Operation → Equipment` is a legitimate SMEsPlus
extension candidate.

**Translated out of the analogy, as §45 requires**, the requirement is:

> A cost object must absorb a machine's cost pool **only in proportion to that
> machine's measured usage on that cost object**, and must absorb nothing from
> machines it did not use.

That is a **traceable direct cost** requirement, not an allocation requirement — and
that distinction is the reason the reference model cannot satisfy it. The reference
model treats machine cost as a work-centre **overhead rate**. The Boss is asking for
it to be a **traced cost**. These are different cost-accounting constructs, and no
amount of configuration converts one into the other.

## 4. Where the allocation configuration belongs — §46

The Boss's position: allocation configuration belongs to a **production equipment
context**, not to the generic equipment master and not to the asset model.

**The evidence supports this**, for three independent reasons:

1. **The asset model does not govern anything after creation** (`14` §5), and on
   this deployment governs nothing at all — 280 assets, zero model links. Putting
   allocation policy there would put it somewhere the system demonstrably ignores.
2. **The equipment master is shared with non-production equipment.** The runtime
   population is visibly full of air-conditioners. Production allocation
   configuration on every office air-conditioner is noise.
3. **The reference product already places production costing configuration on the
   work centre** — rate, analytic distribution, expense account. There is an
   existing, correct home for production cost policy, and it is the production
   context.

`SUPPORTED INTERPRETATION` — a design judgement, evidence-consistent.

**One challenge to record** (Expert 4, Level 4): the reference product puts the rate
on the work **centre**, not on the equipment. A per-machine rate is a **new grain**.
Whether that grain belongs on the equipment record, on a new production-equipment
mapping object, or on the work-centre–equipment pair is an open design decision —
`UNR-24`.

## 5. Cost pool versus allocation driver — §47, §48

The Boss's insistence on separating these two steps is **vindicated by the
evidence**, and the reason is now concrete:

> The reference product's single hourly rate **conflates** the cost pool and the
> driver into one number. That conflation is precisely why the system cannot answer
> "which machine" — the pool has already been dissolved into a rate before any
> driver is applied.

`FACT VERIFIED` as a reading of the mechanism.

### Step A — determine the cost pool

Candidate, from the Boss's §49 hypothesis: **the depreciation actually recognised in
the period** forms the eligible pool for that machine.

| Component | Status |
|---|---|
| A per-period depreciation figure exists | `FACT VERIFIED` — the posted entry |
| It can be attributed to a machine | **Requires the Asset↔Equipment link to be reliable — it is not** (`19`) |
| It should be the whole pool | **Boss decision.** Maintenance cost, energy, and operator cost are all arguably in the pool and none of them is captured (`GAP-04`, `GAP-06`) |

### Step B — allocate the pool

The Boss's design admits exactly **one driver per applicable production equipment
mapping**, chosen from machine hour, work-centre hour, or production quantity.

Against the evidence:

| Driver | Is the measurement available? |
|---|---|
| **Machine hour** | **Not directly.** Work-order duration is recorded against the **work centre**, not the machine. Available only once `GAP-03` is closed |
| **Work centre hour** | **Yes** — this is exactly what the reference chain already uses |
| **Production quantity** | **Yes** — from the manufacturing order |

So of the three candidate drivers, **the one the Boss most wants is the one whose
measurement does not yet exist.** That is not an argument against it; it is the
build order.

`FACT VERIFIED` for the availability assessment.

## 6. The financial depreciation cost pool — §49

The Boss's caution — *depreciation cost pool ≠ automatically FG cost* — is correct
and the evidence sharpens it in two ways.

**First, timing.** `FAIL-P09`: the reference chain recognises work-centre cost when
the **order completes**, not when the machine ran. A monthly depreciation-derived
pool fed into that chain lands in the completion period. For orders spanning a month
end, the cost is in the wrong month.

**Second, snapshotting.** `08` §6 link 2: the rate is copied onto the work order at
creation. A rate derived at month end does not apply to work orders already open.

**Both are inherited defects, not new ones**, and both must be designed around
explicitly. Neither is in the Boss's hypothesis today.

**Unabsorbed depreciation.** When usage is below capacity, part of the pool is not
absorbed. Nothing in the reference system decides where it goes — because nothing in
the reference system has a pool. Under normal cost-accounting treatment it is a
period expense, not an inventoriable cost. **This is a Boss policy decision**, not a
research finding — `UNR-18`.

## 7. Cost lineage classification — §52

See `36_COST_LINEAGE_MATRIX.md` for the full table.

## 8. The verified-gap declaration required by §85

> **Verified source gap:** the reference ERP contains **no mechanism** connecting
> asset depreciation to equipment usage, operations, manufacturing orders, WIP or
> finished-goods cost. Established by exhaustive search of 797 modules.
>
> **SMEsPlus differentiating design candidate:** derive a per-machine cost pool from
> the asset sub-ledger, give the operation an equipment dimension, and allocate the
> pool by measured usage — reusing the existing absorption chain from the work-order
> cost onward.

Per §85, the search for an existing mechanism **stops here**.

## 9. The recommended sequence — and why

From `10` §3.1, restated with reasons:

| # | Step | Why it must come first |
|---|---|---|
| 1 | **Repair the Asset↔Equipment association** | Everything keys on it, and today it is manual, unconstrained, and three-quarters inert (`19`). A duplicate double-counts a machine's pool |
| 2 | **Add the equipment dimension to the operation** | Without it the machine-hour driver has no measurement (§5 step B) |
| 3 | **Derive the pool from the sub-ledger** | Only meaningful once 1 and 2 hold |
| 4 | **Design absorption variance and the unabsorbed policy** | `GAP-05`, `UNR-18` |
| 5 | **Design the timing and snapshotting behaviour** | `FAIL-P09`, `UNR-24` |

Steps 1 and 2 are unglamorous and are the whole foundation. A costing design built
before them will be built on an association that is optional, duplicable and
populated by hand.
