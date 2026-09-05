# 56 — LATENT DOUBLE-COUNTING RISK

**LAYER 2 — AUDIT QUARANTINE.**

**No source defect is withdrawn because a deployment has not activated it.** §11 of the
directive is explicit, and it is the correct instruction: a latent defect is a defect with
a precondition, not a defect that has been fixed.

---

## 1. Per-defect risk analysis

| ID | Code path exists | Config required | Configs can coexist | Mutual exclusion | Runtime guard | Financial duplication | Management duplication | Active | **Class** |
|---|---|---|---|---|---|---|---|---|---|
| `DC-01` | **yes** | ≥2 overlapping time logs on one work order | **yes — observed** | **none** | none | **yes**, machine component | no | precondition met, effect 0 | **LATENT REACHABLE** |
| `DC-02` | yes | work-centre rate **and** employee rate | yes | **none** | none | yes | no | no | **LATENT CONFIGURATION-DEPENDENT** |
| `DC-03` | yes | a human types `extra_cost` | yes | n/a | none | residue, not duplication | no | no | **LATENT CONFIGURATION-DEPENDENT** |
| `DC-04` | yes | standard cost **+** real-time valuation | yes | **none — no cost-method guard on the relief side** | none | residue both signs | no | unknown | **LATENT REACHABLE** |
| `DC-05` | yes | work-centre `analytic_distribution` | yes | none | none | no | **yes** | no | **LATENT CONFIGURATION-DEPENDENT** |
| `DC-14` | yes | project bridge **+** project on order **+** two distributions resolving to one account | **yes — modules installed in `iTEST02`** | **none, no collision check** | none | **no — 0 financial** | **yes** | no | **LATENT REACHABLE** |
| `DC-15` | yes | any second call site | — | **none** | **call-site state filter only** | **yes, if a second call site is added** | no | **guard absent, live** | **LATENT REACHABLE** |

## 2. The finding that matters most for SMEsPlus

> **`P03R-F-06`. Across all seven duplication-class defects, not one mutual exclusion, one
> configuration validation, or one collision check exists.** Every one is prevented today
> only by a configuration field being left empty.

Measured: 59 of 60 work centres have no rate; 60 of 60 have no expense account; 0 of 60
have an analytic distribution. **The system is safe because it is unconfigured.**

That is the opposite of a control. Filling in the fields the product asks an administrator
to fill in is what activates the defects.

## 3. Reachability now demonstrated for two defects round 3 called impossible

`DC-14` and `DC-10` were recorded in round 3 as blocked by modules *"not installed in any
readable dump"*. `iTEST02` has **both** modules installed. The bound was honest; the
conclusion inside it did not survive.

**Neither defect has fired** — no analytic distributions exist in `iTEST02` either. But they
have moved from *unreachable* to **one configuration field away**.

## 4. Requirement generated — `DESIGN CANDIDATE`

`R-18`: **where two mechanisms can attribute the same economic cost, SMEsPlus must enforce
mutual exclusion structurally** — not leave it to an unset field. Where coexistence is
intended, a collision check must exist and be tested.

Not authorised for implementation.
