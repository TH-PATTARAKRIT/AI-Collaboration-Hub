# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 02 — `RISK-U03` / `GAP-FS-10` Problem Statement And Evidence Boundary

Control Level: `/L9999.9999`
Status: `PROBLEM DEFINED — SCOPE BOUNDED — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. The Item, Stated Exactly

`RISK-U03` / `GAP-FS-10` / `U-03`:

> **The Inventory-side multi-tenant invariant set does not exist.**

R4 records that a cross-gate SaaS invariant set is defined elsewhere in the programme, and that **whether and how it extends to Inventory has never been established** (`10_L9...` §1). That is the gap. It is not that isolation is known to be broken; it is that there is no stated set of properties against which isolation could be asserted, tested, or disproved.

This is why R4 reports `0 of 8` L9 proofs. The proofs were never achievable, because a proof requires a proposition.

---

## 2. Why This Item, And Why Now

The AAS+ / PMO review ranked this **Rank 1** of the three structural capabilities, on grounds re-derived from the Boss controls themselves rather than from R4's description (`04` §3, §4):

| Property | Basis |
|---|---|
| **Unconditional** | Handoff element 10 — *"mandatory company and tenant context"* — carries **no qualifier** in the Minimum Handoff Data Contract §3 (`d9e845e`), and **no qualifier** in the 22-Scenario Cross-Proof Baseline §3 (`296b495`). Elements 14 and 15 are each qualified; element 10 is not |
| **Sufficient on its own to produce the `0 of 22` result** | Contract §4 forbids declaring a scenario verified where it is *"missing company/tenant isolation context"*. That condition is met on all ten material handoffs (`16` §3). The `0 of 22` conclusion follows from element 10 **alone**, independently of elements 14 and 15 |
| **Not COGS-gated** | `RISK-U03` appears nowhere in the COGS dependency chain and is none of the twelve Joint decisions (`04` §5). Verified by the review |
| **Requires no prior Boss ruling to begin** | Which is why it is the only one of the three that could be commissioned without a ruling first |
| **Precondition for eight further proofs** | All eight L9 isolation proofs, currently `0 of 8`, and `L14-01` traceability |

---

## 3. What The Gap Concretely Consists Of

R4's L9 and L8 work makes the gap specific rather than general. Four components, each independently evidenced:

### 3.1 Two structural mechanisms by which company context can legitimately be absent

| Finding | Mechanism | Consequence |
|---|---|---|
| `R4-F-09` | A storage location's company assignment is **optional** in the reference pattern; company-scoped behaviour is guarded so it applies only where a company is present | A location with no company falls outside company scoping entirely. Handoff element 9 (`WHICH Warehouse / Location`) and semantic `L5-08` (internal-movement neutrality) both assume a location carries company context |
| `R4-F-06` | Traceable identity uniqueness is scoped to (identifier, product, company) and **company-less identities are possible**; the reference implementation reconciles collisions with a **reactive** cross-company duplicate check | A reactive check is a report, not an isolation guarantee. Handoff element 8 and the entire traceability semantic `L5-06` rest on identity uniqueness |

R4's own characterisation is adopted without softening: these are **structural, not configurational**. They cannot be closed by configuring the system correctly.

### 3.2 Enforcement sits in a layer that can be bypassed

Prior evidence records company scoping enforced at the application layer across the core stock concepts with **no database-layer backstop**, and an audit of privileged bypass paths that was **started and never completed** (`10` §3, `L9-01`). Isolation is therefore asserted as a property of the system but enforced by a layer whose bypass surface has never been enumerated.

### 3.3 The most-used numbers in the module are derived, and derivation was never in scope

`R4-F-22`: isolation must be proven on the **derived** surfaces — balances, forecasts, valuation positions, analytics — not only on stored records, because design principle `P-03` makes on-hand a derived value by design. A computation can aggregate across a boundary even where every underlying record is scoped correctly. No prior round stated this requirement explicitly.

### 3.4 Two isolation properties were never researched at all

`L9-03` (branch and location isolation) rests on `RISK-U01` / `U-01`, recorded in prior evidence as *"not merely undesigned — unevidenced either way"*. `L9-04` (shared template versus tenant-owned customization) has no decided boundary, and `L2-OBS` confirms the underlying hazard: reconfiguring a warehouse causes its operation types, locations and routes to be **re-derived** rather than versioned.

---

## 4. What This Session Is, And What It Is Not

| This session **is** | This session **is not** |
|---|---|
| A design and specification act: it authors the invariant set that `RISK-U03` says does not exist | A proof. No isolation property is proven here |
| A statement of what would have to be true, with acceptance criteria precise enough to be tested later | An implementation. No code, schema, migration or API is produced |
| A definition of the enforcement obligation and the surfaces it must cover | A verification that the obligation is satisfiable in a chosen technology. That is a Team B question and is not approached |
| An honest account of what remains blocked after the design exists | A closure of `RISK-U03`, `GAP-FS-10`, `R4-F-06`, `R4-F-09` or `R4-F-22`. **Items closed by this session: 0** |

**The distinction that governs the whole package.** A proof of isolation requires three things: a proposition, an implementation, and a test of the implementation against the proposition. This session supplies the first. It cannot supply the second or third, and does not claim to.

---

## 5. Scope Boundary Applied

### 5.1 In scope, and treated

All fifteen areas named in the authorization: tenant, company, warehouse and location isolation; product and variant visibility; lot and serial traceability; package isolation; route and rule ownership; operation type ownership; move and transfer ownership; replenishment and scheduler execution boundary; the context boundary for adjustment, scrap, return and landed cost; the context boundary for stock and valuation reporting; event, audit trail and immutable identity requirements; and the cross-module handoff contract fields required by Accounting, Purchase, Sale, Manufacturing, Approval, Document and Reporting.

### 5.2 Out of scope, and not decided

COGS policy; period-close policy; valuation posting policy; landed-cost accounting posting; return cost basis; any Thai statutory position; source code; database schema; API implementation; UI implementation; Team B and Team C work; production; release.

Where an invariant touches a valuation surface, the **context** half is specified and the **value** half carries:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

### 5.3 The two adjacent structural capabilities are deliberately not designed here

Ranks 2 and 3 of `04` §4 — the deterministic movement attempt identity (`RISK-C02`, element 15) and the migration or replay provenance reference (`GAP-FS-08`, element 14) — are **not** in this authorization and are not designed. Where an invariant here needs one of them, it states the dependency and stops. It does not design around them, and it does not treat the context half as a substitute for either.

---

## 6. The Question This Package Must Answer Honestly

The authorization's own framing is that this work unblocks the most while depending on the least. The package must therefore be explicit about what it does **not** unblock, or it will be misread as progress it is not.

| Question | Answer, stated here and evidenced at `07` and `14` |
|---|---|
| Does this design make any of the 8 L9 proofs achieved? | **No.** `0 of 8` stands |
| Does it make any of them **definable and testable** for the first time? | **Yes — 8 of 8 become definable**, 4 unconditionally and 4 conditioned on named rulings or inputs |
| Does it move the `0 of 22` cross-proof result? | **No.** `0 of 22` stands |
| Does it change anything about the `0 of 22`? | **Yes — the reason for element 10 changes.** From *"the capability does not exist"* to *"the capability is specified, not built, and not verified."* That is a real change in position and a small one in effect |
| Is Inventory Final Solution v2.0 closer to ready? | Not materially. `0 of 12` Joint decisions ready and 3 NOT DECIDABLE are untouched by this session |

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
