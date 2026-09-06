# P04 — OPERATION → EQUIPMENT CAUSALITY INTERFACE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-07`. **P03 is consumed, not executed.**
P03 input: `bc767a8` (`CQ-P03-06`, `FACT VERIFIED — CLOSED`).

---

## 1. The chain, with each link's owner and evidence

| Link | Exists? | Owner of the evidence |
|---|---|---|
| Routing Operation → **Work Centre** | **YES** | P03, accepted with attribution; not re-derived here |
| Routing Operation → **specific Equipment** | **NO — proven absent** | P03 **and** P04 independently, both in series 18 |
| Equipment → Work Centre | **YES**, via `mrp_maintenance` | P03; `mrp_maintenance` confirmed installed in P04's 361-module set |
| Equipment → **Asset** | **NO in the reference product** | **P04** (`CQ-P04-03` §1, with firing control) |
| Asset → Equipment | **YES, custom only**, one-way, manual, irreversible | **P04** (`CQ-P04-03` §4) |
| Time log → machine | **NO** — every measurement resolves to a work centre | P03 |

> The chain P03 published is `asset ✗ equipment → work centre ← operation`.
> **P04 closes the asset side of it and finds the arrow does exist — but only in a custom
> module, only from asset to equipment, only when a human sets it, and never afterwards
> reversible.** That is a materially different statement from *"no link"*, and it is the half
> P03 could not see from the manufacturing side.

## 2. What actual-used differs from merely-available

| Concept | Represented in the estate? |
|---|---|
| Equipment **available** to an operation | **Indirectly** — via work-centre membership, a configuration fact |
| Equipment **actually used** in a run | **Not represented anywhere.** No event model records a machine |
| Machine cost driver | Human time logs — P03 measured that a machine running unattended generates none, and two operators at one machine generate two |

> **Membership is configuration; usage is an event; the estate has the first and not the
> second.** P04 adds one consequence P03 did not need: because `name_asset` is **many-to-one
> and unconstrained** (`CQ-P04-03` §4), even if usage events existed, **several assets could
> claim the same equipment**, and nothing would apportion between them. **A usage event model
> alone would not be sufficient; it would also need a cardinality rule that does not exist.**

## 3. The SMEsPlus functional contract — DESIGN CANDIDATE, not a finding

Stated as a contract so that P03, Inventory/MRP and P04 can each implement their own side
without either process assuming the other's mechanism:

| Element | Contract |
|---|---|
| **Event** | An *Equipment Usage Event* asserting: this equipment, this operation, this MO, this quantity of a declared driver, this period |
| **Driver** | One of Machine Hour / Work Centre Hour / Production Quantity — **Boss-selected, no default** (carried policy) |
| **Producer** | Manufacturing execution (**P03 / MRP owns this**) |
| **Consumer** | Asset/Equipment cost allocation (**P04 owns this**) |
| **Cardinality rule** | Required, and **currently absent**: which asset's depreciation an equipment's usage draws from, when more than one asset references it |
| **Reconciliation invariant** | Period depreciation of an asset = Σ productive allocations + Σ non-productive attributions, to the period, with no residue |
| **Prohibited** | Deriving usage from work-centre membership; deriving machine hours from human time logs |

> **The last row is the one both packages arrived at from opposite directions**, and it is
> stated as a prohibition rather than a preference because P03 measured what happens without
> it: machine cost that is not causally connected to machine use.

## 4. What P04 does not do here

- **Does not research P03.** Every manufacturing-side claim above is attributed, and none was
  re-derived.
- **Does not decide the denominator.** That is `BLK-07` / `P04-BD-05`, Boss-owned, and P03
  explicitly routed it back to this register. **It is not closed by this run.**
- **Does not build the contract.** §3 is a `DESIGN CANDIDATE` and appears as such in the
  Design Input Pack.

## 5. Disposition

> **`CQ-P04-07` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the causal question:
> Operation → specific Equipment **does not exist**; Equipment → Asset **does not exist in the
> reference product**; Asset → Equipment **exists in one custom module**, with the limits in
> `CQ-P04-03`.
> **The design question is `BOSS DECISION REQUIRED`** — `BLK-07`, `P04-BD-05`, both already
> open, neither closed here.
