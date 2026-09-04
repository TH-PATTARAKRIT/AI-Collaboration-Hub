# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 04 — The `CTX` / `AUTH` Relationship And Axis Model

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `RC-F-05 SPECIFIED — 9TH ENFORCEMENT POINT CLASS ADDED — 41 OF 41 FUNCTIONS GIVEN AN AUTH AXIS SET — 0 VERIFIED`

---

## 1. The Question This File Answers

`RC-F-05`, stated by the consolidation at `04` §2.1 and `09` §4.1:

> *"The execution family carries no operation-type axis. `MTI-29` and `MTI-30` specify single-`CTX` execution and authority carriage, but `CTX = (tenant, company, warehouse?, location?)` — **operation type is not in the tuple**. The context tuple predates the ruling. `AUTH` and `CTX` are now different shapes, and the relationship between them is unspecified."*

This file specifies the relationship, states where the operation-type axis attaches, and states what happens across a deferral boundary. It supplies **no implementation and no proof.**

---

## 2. The Two Tuples

```
CTX  = (tenant, company, warehouse?, location?)
       WHERE A FACT BELONGS.
       Anchors every record, derived value, event, job and payload.
       Source: 03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md §2.1 at dcb9227.

AUTH = (tenant, company, warehouse, operation type)
       WHAT AN ACTOR MAY DO.
       Governs every permission evaluation.
       Source: Boss ruling MTI-D-02, 26_BOSS_RULING_...-001.md at 13b3e63.
```

They share two members and differ in two. That is the whole of the difficulty, and it is why the relationship must be stated rather than assumed.

| | `tenant` | `company` | `warehouse` | `location` | `operation type` |
|---|:---:|:---:|:---:|:---:|:---:|
| **`CTX`** | mandatory | mandatory | situational | situational | **absent** |
| **`AUTH`** | mandatory | mandatory | mandatory where the object carries it | **not ruled** — `RC-D-01` | **mandatory where the act is performed through one** |

---

## 3. The Six Relationship Rules

Rules 1 and 2 are carried unchanged from `04` §7 of the published matrix and from `04` §2.1 of the consolidation. Rules 3 to 6 are stated here for the first time.

| # | Rule | Basis |
|---:|---|---|
| **R-01** | **`AUTH` is always a subset of a single `CTX` spine.** Never a superset, never a union across companies. Multi-company access is several `AUTH` entries, never one broadened entry | Carried unchanged. `MTI-D-02` rules 5, 6; `CF-I-01` |
| **R-02** | **Neither substitutes for the other, and both must be evidenced separately.** A correct `CTX` on a record proves nothing about whether the actor was permitted to create it; a valid `AUTH` proves nothing about whether the resulting record was anchored correctly | Carried from consolidation `04` §2.1 rule 4 |
| **R-03** | **`AUTH` is resolved at the act; `CTX` is resolved at the record.** They are resolved by different mechanisms at different moments, and a system that derives one from the other has done neither. In particular, **an actor's `AUTH` is not a source from which a record's `CTX` may be inferred**, and a record's `CTX` is not evidence of the `AUTH` that produced it | `MTI-20`, `MTI-42`, `MTI-05`; `R-02` |
| **R-04** | **The operation-type axis is a property of the act, never of the record.** A movement fact records the operation type it was executed through, as history. It does not thereby acquire an operation-type context, and no record's `CTX` gains a fifth member | `MTI-01`, `MTI-09`; `CD-21` |
| **R-05** | **Across a deferral boundary, `CTX` is carried and `AUTH` is carried *and revalidated*.** `CTX` is immutable once resolved (`MTI-06`, `MTI-41`) and is therefore carried unchanged from scheduling to release. `AUTH` is a grant, grants expire and are revoked, and a grant valid at scheduling is not evidence of a grant valid at release. **The two travel together and are treated differently on arrival** | `MTI-30` R2; `CF-I-02`; `L13-MT-01` |
| **R-06** | **A refusal is an act.** An act refused for want of `AUTH` emits an event carrying the `CTX` it was attempted in and the `AUTH` that was found insufficient. **A refusal that leaves no trace cannot be distinguished from an attempt that never happened**, and the negative access tests at `09` depend entirely on refusals being observable | `MTI-38` R2; `N-02` at consolidation `07` §8 |

### 3.1 Why `R-04` matters more than it looks

The tempting alternative is to add operation type to `CTX` and have one tuple. It is wrong, and the reason is `MTI-06`.

`CTX` is **immutable once a record has participated in a completed act**. If operation type were a `CTX` member, then an operation type could never be reorganised, retired or reclassified for any product that had ever moved through it — and `MTI-D-03` makes operation type **tenant-configurable**, so tenants would be creating immutable context members by ordinary administrative action. The two rulings would collide.

Keeping operation type in `AUTH` and out of `CTX` keeps `MTI-D-02` and `MTI-D-03` consistent. The movement fact still records which operation type it was executed through — as an attribute of history under `MTI-38`, which is immutable for a different and correct reason: **an event is immutable because it happened**, not because it anchors anything.

---

## 4. Where The Operation-Type Axis Attaches

Three attachment points, and they are different in kind.

| # | Attachment | What Attaches | Governing |
|---:|---|---|---|
| **1** | **The act** | Every act performed through an operation type resolves that operation type before execution and evaluates `AUTH` against it | `MTI-D-02` rules 3, 4; `EP-P` at §5 |
| **2** | **The deferred act** | Every scheduled, queued or background run carries an explicit operation-type context from scheduling to release, and re-resolves the grant at release | `MTI-D-02` rule 8; `MTI-29` R2, `MTI-30` R2, `CF-I-02` |
| **3** | **The emitted fact** | Every handoff payload and every audit event carries the operation-type identity of the act, and the attestation of the control that asserted the authorization property | `HF-CTX-10`, `HF-CTX-11`; `MTI-38` R2, `MTI-43` R2 |

**It attaches nowhere else.** It is not a member of `CTX` (`R-04`), not an anchor for any object other than a movement document (`MTI-09`, unchanged), and not a dimension of any derived value.

### 4.1 The axis ranges over a tenant-owned enumeration — `CF-F-04`

`MTI-D-02` §5 names eight operation types *"including, but not limited to"* — Receipt · Delivery · Internal Transfer · Inventory Adjustment · Scrap · Replenishment · Landed Cost review/action · Scheduler-controlled replenishment or reservation actions. `MTI-D-03` §3 names **Operation Type** among the records a tenant/company may configure.

The two compose to a gap: **a platform-level control cannot be expressed over an enumeration each tenant defines for itself**, because the platform has no stable term to bind to. *"Scrap requires a second approver"* and *"Landed Cost review is segregated from Landed Cost action"* are both unstatable as platform rules if `Scrap` and `Landed Cost` are tenant labels.

`CF-I-05` supplies the shape of the remedy, and the shape is already in the set: `MTI-33` requires the **reason** classification for adjustment, count, scrap, return, transfer and landed-cost to be *"defined independently of context, so that the same reason means the same thing in every company"*. `CF-I-05` applies exactly that pattern to operation types — every tenant-configured operation type declares one platform-owned class, and platform controls bind to the class.

**The closure of the platform class enumeration is a Boss decision.** It is `CF-D-02`, and it is stated at `11` §3 with its options and **never chosen**. Until it is ruled, `CF-I-05` is `SPECIFIED — CONDITIONAL`, and every proof requirement that quantifies over operation types must derive its test set from the **implemented** set rather than from `MTI-D-02` §5's illustration — which the consolidation already states at `RC-P-14`.

---

## 5. The Ninth Enforcement-Point Class — `EP-P`

### 5.1 The gap, with its search boundary

**Boundary `B-03`** — population: the enforcement-point class table at `05_FUNCTION_ENFORCEMENT_POINT_MATRIX.md` §2 at `dcb9227`; pattern: rows matching `^\| \`EP-`; path set: that single file; unit: one class.

Result: **eight classes.** `EP-R` Resolve · `EP-W` Write barrier · `EP-Q` Query scope · `EP-A` Aggregate barrier · `EP-X` Execution binding · `EP-E` Event emission · `EP-H` Handoff carriage · `EP-G` Governance gate.

Of the eight, **exactly one references `AUTH`** — `EP-Q`, *"every read is scoped to the caller's `AUTH` set before evaluation"*. `EP-R` resolves `CTX`. The remaining six make no authorization statement.

AAS+ advice `27` §4.4 requires permission checks *"before search, selection, confirmation, posting handoff, report generation, export, import, scheduler execution, and API execution"*. **Six of those nine are not reads.** There is therefore no function-boundary attachment point for the central control `MTI-D-02` establishes.

Class **`A` within boundary `B-03`**. Class **`B`** for the wider design corpus, which this session did not re-derive.

### 5.2 The class

| Class | Name | What Must Happen | Governing |
|---|---|---|---|
| **`EP-P`** | **Permission evaluation** | The caller's `AUTH` is resolved and evaluated **before** the act — before search, selection, confirmation, write, posting handoff, report generation, export, import, scheduler release and API execution. Evaluation is against all applicable axes, not against company alone. **A failed evaluation refuses the act and emits a refusal event; it never degrades to a filter, an empty result or a silent no-op** | `MTI-D-02` rules 1-8; advice `27` §4.4; `CF-I-01`, `CF-I-04`; `R-06` |

`EP-P` does not replace `EP-Q`. `EP-Q` states *what a read may see*; `EP-P` states *whether the act may proceed at all*. On a read both apply, and `EP-P` runs first — which is the difference between a refused search and a search that returns nothing, and `N-01` and `N-03` at `09` turn on exactly that difference.

### 5.3 `EP-P` versus the published `EP-R`

| | `EP-R` Resolve | `EP-P` Permission evaluation |
|---|---|---|
| Resolves | `CTX` from the declared anchor | `AUTH` from the caller |
| Fails when | Context cannot be resolved | Authority is absent, expired, revoked, or narrower than the act |
| Failure is | The act fails, recorded as a failure | The act is **refused**, recorded as a refusal |
| Evidences | `HF-CTX-05` anchor path | `HF-CTX-11` authorization attestation |
| Asserted by | `MTI-19` context conformance control | **`CF-I-03`** authorization conformance control — **which does not exist** |

The last row is `CF-F-05` and is the subject of §9.

---

## 6. The `AUTH` Axis Set Of Every Controlled Function

All 41 controlled functions `INV-F-01` .. `INV-F-41` across 29 menus, carried unchanged from `05_FUNCTION_ENFORCEMENT_POINT_MATRIX.md`. **No function is renumbered and none is added.**

Legend: **T** tenant · **C** company · **W** warehouse · **O** operation type. `EP-P` attaches to all 41 without exception; the published enforcement points of each function are unchanged and are not restated.

### 6.1 Operations functions

| Function | Menu | `AUTH` axes | Note |
|---|---|---|---|
| `INV-F-01` Compute replenishment shortfall | `M01`, `M06` | T C W **O** | The shortfall walk crosses a location hierarchy; the walk must be bounded by the caller's warehouse set, not only its company |
| `INV-F-02` Convert a proposal into a supply action | `M01` | T C W **O** | |
| `INV-F-03` Record a physical count | `M02` | T C W **O** | The count sheet's contents are an `EP-P` question before they are an `EP-Q` question |
| `INV-F-04` Approve and apply an adjustment | `M02` | T C W **O** | **Approval and application are separate `AUTH` evaluations.** `R4-F-02` records that no approval state exists at all in the reference pattern; the axis now exists for one to bind to |
| `INV-F-05` Create a stock operation | `M03` | T C W **O** | `O` is the operation's own type |
| `INV-F-06` Reserve stock against an operation | `M03` | T C W **O** | Reservation is held on the balance, so the balance's context is the only protection on the `CTX` side; `EP-P` is the protection on the `AUTH` side |
| `INV-F-07` Validate a stock operation | `M03` | T C W **O** | **The single most consequential point in the matrix.** Where a movement fact becomes done, and where element 10 is either supplied with both attestations or is not |
| `INV-F-08` Handle a shortfall — backorder or close | `M03` | T C W **O** | |
| `INV-F-09` Handle over-delivery or over-receipt | `M03` | T C W **O** | Tolerance threshold and approver are per company — `GAP-FS-16`, a business policy decision, open |
| `INV-F-10` Cancel before execution | `M03` | T C W **O** | `C-01` cancellation-cascade symmetry is an unarbitrated conflict and is **not** arbitrated here |
| `INV-F-11` Return goods after execution | `M03` | T C W **O** | The return resolves to the original's company. Cost basis is `JT-05`, **NOT DECIDABLE** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `INV-F-12` Scrap goods | `M04` | T C W **O** | `R4-F-04` — scrap has no approval path. The axis exists; the control does not |
| `INV-F-13` Recover salvage value | `M04` | T C W **O — indeterminate** | `R4-F-03` — **the concept has no object at all.** The axis set is stated for when it is originated; the operation type it would execute through does not exist to be named. `HOLD` on the value half |
| `INV-F-14` Allocate a landed cost | `M05` | T C W? **O** | Warehouse situational. `JT-08` **Audit VETO retained**; `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` on the posting half |
| `INV-F-15` Run the planning engine on demand | `M06` | T C W? **O** | A manual run and a scheduled run must resolve the **same** four axes. `L6-10` records that nothing prevents overlap; `MTI-31` scopes and does not identify |

### 6.2 Product and master-data functions

| Function | Menu | `AUTH` axes | Note |
|---|---|---|---|
| `INV-F-16` Create or amend a product | `M07` | T C | **Simplified by `MTI-D-01`.** The published note records that this function wrote tenant-level definitional data and company-level attachment in one act, needing different barriers. Under Option B it writes one company-owned object |
| `INV-F-17` Change stock-control classification while stock exists | `M07` | T C | The published failure mode — *"applied tenant-wide while only one company's stock was considered"* — **ceases to be expressible** under `CD-01`. `RE-SCORE BASIS` only; the function's own destructive one-directional character is unchanged |
| `INV-F-18` Generate or amend variants | `M08`, `M25` | T C | `GAP-FS-03` unresolved and untouched by any ruling |
| `INV-F-19` Create a batch or serial identity | `M09` | T C W? **O?** | **Path-dependent.** Created within an operation, it inherits that operation's `AUTH`; created standalone in `M09`, the axes are `(T, C)`. Both paths must evaluate `EP-P`. This is the `R4-F-06` point |
| `INV-F-20` Amend or merge a batch identity | `M09` | T C | A merge spanning companies is prohibited outright by `MTI-12`, not merely unauthorized |
| `INV-F-33` Assign or change a product category | `M24` | T C | Listed here rather than under configuration because `CD-12` makes the category a company-owned configuration object. **Costing facet `HOLD` — `GAP-FS-02` precondition-blocked on `JT-01`, NOT DECIDABLE** |

### 6.3 Reporting functions

For reporting, the `AUTH` set is the caller's; the report's scope is the **intersection** of the caller's `AUTH` set with the requested scope, computed **before** evaluation.

| Function | Menu | `AUTH` axes | Note |
|---|---|---|---|
| `INV-F-21` Derive the current stock position | `M10`, `M11` | T C W? O? | Display clamping (`R4-F-07`) can mask a cross-context arithmetic break — `MTA-07`, residual `MATERIAL`, display contract open |
| `INV-F-22` Produce movement history | `M12` | T C W? O? | The stock card is the document a Thai auditor asks for. Ordering rule is `R4-F-08`, open |
| `INV-F-23` Produce the valuation position | `M14` | T C W? O? | **All conclusions `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| `INV-F-24` Produce warehouse analytics | `M15` | T C **W** O? | Warehouse mandatory — the measure is per warehouse. Measure set evidence-thin, `GAP-FS-13` |
| `INV-F-25` Export a report | `M12`, `M14`, `M15` | T C W? O? | **The highest-consequence leak surface.** `MTA-09`: nothing in the system controls the file after it leaves. `MTI-D-04` unruled, so the sanctioned cross-company alternative does not exist and the need is met here |

### 6.4 Configuration functions

**`CF-I-04` applies to every row below: defining a configuration object confers no authority to act through it.**

| Function | Menu | `AUTH` axes | Note |
|---|---|---|---|
| `INV-F-26` Change a capability switch | `M16` | T C | Never retroactive; scoped to one `CTX` |
| `INV-F-27` Create or restructure a warehouse | `M17` | T C **W** | **The `SAAS-04` regeneration point.** `RC-P-42` is the highest-value configuration proof and it is unexecutable |
| `INV-F-28` Create or change a location, including its kind | `M18` | T C **W** | **The `R4-F-09` point** |
| `INV-F-29` Change a supply route or rule | `M19`, `M20` | T C W? | Route-to-rule company consistency is `MTI-10`, carried |
| `INV-F-30` Change an operation type, including numbering | `M21` | T C **W** | **This function defines an `AUTH` axis value.** `CF-I-04` and `CF-I-05` both bind here: creating the type confers no authority through it, and the type must declare a platform class. `TH-HOLD-09` held on numbering |
| `INV-F-31` Define storage constraints | `M22` | T C **W** | |
| `INV-F-32` Suggest and override a put-away destination | `M23` | T C **W** **O** | The override occurs inside a receipt or transfer, so it carries that operation's `AUTH`. The override is an evented act |
| `INV-F-34` Define a packaging | `M26` | T C | `MTI-D-06` — whether a handling unit may carry two companies' goods — is a **Thai panel** question. No AI may answer it |
| `INV-F-35` Set or maintain a reordering rule | `M27` | T C **W** | **Within-company nested overlap (`R4-F-11`) is not addressed by any axis here and remains open** |
| `INV-F-36` Define barcode interpretation | `M28` | T C | **Company-anchored under `CD-13`.** `R4-F-12`'s misparse surface is now per-company configurable |
| `INV-F-37` Define or change a unit conversion | `M29` | T C | **Company-anchored under `CD-14`, subject to `CF-D-01`.** `R4-F-13`'s rounding surface is now per-company configurable |

### 6.5 Cross-cutting functions

| Function | Scope | `AUTH` axes | Note |
|---|---|---|---|
| `INV-F-38` Enforce the period guard | All operational menus | T C | The lock date is supplied per company by Accounting. **The exception grant carries `CTX` as well as grantor, reason and expiry**; the global unscoped bypass at `G-2` is rejected, consistent with `MTI-18` |
| `INV-F-39` Emit a fact to Accounting | All value-bearing functions | **carries the originating act's full four-axis `AUTH`** | Where element 10 is supplied with both attestations or is not. Elements 4 and 7 remain `HOLD`; elements 14 and 15 remain unsuppliable |
| `INV-F-40` Correct a completed fact | All operational menus | **the original's `AUTH`, plus a correction grant** | A correction resolves to the same `CTX` as the original. **A correction that changes context is prohibited outright** — it is a migration act |
| `INV-F-41` Establish opening balances at cutover | `M02`, migration | T C **W** · **O — indeterminate** | **The highest-risk point in the matrix.** A cutover is not an operation type in `MTI-D-02` §5's list, and whether it should be one is part of `CF-D-02`. Quantity half Inventory-owned; value half held; provenance is `GAP-FS-08`, which does not exist |

### 6.6 Axis coverage result

| Measure | Result |
|---|---:|
| Controlled functions | **41** |
| Functions given an `AUTH` axis set | **41 of 41** |
| Functions carrying `EP-P` | **41 of 41** |
| Functions with a **mandatory** warehouse axis | **21** |
| Functions with a **situational** warehouse axis (`W?`) | **8** — `INV-F-14`, `-15`, `-19`, `-21`, `-22`, `-23`, `-25`, `-29` |
| Functions with **no** warehouse axis | **11** — `INV-F-16`, `-17`, `-18`, `-20`, `-26`, `-33`, `-34`, `-36`, `-37`, `-38`, `-40` |
| Functions whose warehouse axis is **inherited from the originating act** | **1** — `INV-F-39` |
| Functions with a **determinate** operation-type axis | **15** — `INV-F-01` .. `INV-F-12`, `INV-F-14`, `INV-F-15`, `INV-F-32` |
| Functions whose operation-type axis is **inherited by carriage** | **1** — `INV-F-39` |
| Functions whose operation-type axis is **path-dependent** | **1** — `INV-F-19` |
| Functions whose operation type is **indeterminate because the concept has no object or no class** | **2** — `INV-F-13` (`R4-F-03`, salvage has no object), `INV-F-41` (`CF-D-02`, a cutover is not a ruled operation type) |
| Functions with **no** operation-type axis | **22** |
| Functions whose published failure mode ceases to be expressible under conformance | **1** — `INV-F-17`. **`RE-SCORE BASIS` only; not closed** |
| **Functions verified against any axis** | **0.** No implementation exists |

---

## 7. Deferred Execution — The Full Semantics

`RC-F-05`'s hardest half, and the subject of `L13-MT-01`.

| Moment | `CTX` | `AUTH` | Recorded |
|---|---|---|---|
| **Scheduling** | Resolved from the declared anchor. Immutable thereafter | Resolved in full, four axes. Stored **as a resolved tuple**, not as a reference to the actor | The scheduling act is an event carrying both |
| **In queue** | Carried unchanged | Carried unchanged. **Not re-evaluated while queued** — a queue is not a permission surface | — |
| **Release** | Carried unchanged. **Never re-resolved from current configuration** (`MTI-41`) | **Revalidated in full.** Each axis is checked against the grant in force **now** | The release act, or the refusal, is an event |
| **Refusal at release** | The `CTX` the run would have executed in | The `AUTH` found insufficient, and which axis failed | **The non-execution is an event.** `MTI-30` R2, `R-06` |
| **Execution** | The run's own `CTX`, single | The revalidated `AUTH` | Every resulting fact carries both, plus `HF-CTX-10` and `HF-CTX-11` |

### 7.1 The asymmetry, stated once

**`CTX` is carried; `AUTH` is carried and revalidated.** A context is a fact about where something belongs and does not expire. A grant is a permission and does expire. Treating them the same in either direction produces one of two failures: re-resolving `CTX` at release re-interprets history and violates `MTI-41`; not revalidating `AUTH` at release executes under a permission that no longer exists and violates `MTI-D-02` rule 8.

### 7.2 What this does not fix

**A run with a fully resolved and revalidated four-axis `AUTH` is still indistinguishable from a retry of itself.** `MTI-31` supplies run scoping and mutual exclusion; it supplies no idempotency identity. That is `RISK-C02` / `IV-06`, rank 2, whose severity is an outstanding Boss ruling (`C-02`) which **this session does not classify**, consistent with R4, the review, the invariant set and the consolidation all declining.

`RC-P-25` is therefore `DEFINABLE` in part only, and `RC-P-31` remains a proof that would be satisfied by a broken system.

---

## 8. Segregation Of Duties Over Four Axes — `L7`

`L7-09` and `R4-F-21` record segregation of duties as **undesignable** because the authorization scope was unruled. `MTI-D-02` makes it designable. It does not make it designed, and two things stand between the two.

| Requirement | Position |
|---|---|
| A segregation rule can now be **expressed** | **Yes.** *A different actor holding a different operation type within the same company and warehouse* is statable over `AUTH` |
| A segregation rule can be expressed **at platform level** | **Not yet.** `CF-F-04` — operation type is a tenant-owned label. A platform rule must bind to `CF-I-05`'s platform class, whose enumeration is `CF-D-02`, unruled |
| The context boundary wins over segregation | **Yes, and it is now more firmly grounded.** `MTI-D-01` and `MTI-D-02` rule 1 together mean approval routing may **never** cross a company boundary to satisfy a segregation requirement. Segregation degrades to a compensating control; it is never satisfied by crossing a company |
| The compensating control is designed | **No.** `MTI-F-05`. A Thai micro-SME with two staff may have no second qualifying actor at all (`R4-F-21`), and **the control's content requires Thai user input — Lane C, `0 of 78`.** No AI may supply it |

---

## 9. The Structural Gap This Model Exposes — `CF-F-05`

### 9.1 The finding

**Boundary `B-02`** — population: the 50 rows `MTI-01` .. `MTI-50` at `dcb9227`, read in full including all fourteen commentary sub-sections; pattern: the enforcement-layer column, the invariant text of every row, and every row whose text contains `authorit|authoris|authoriz|permission|role|grant`; path set: that single file; unit: one invariant.

Result: **eight invariants carry the `CONTROL` layer** — `MTI-05`, `MTI-16`, `MTI-19`, `MTI-23`, `MTI-24`, `MTI-30`, `MTI-46`, `MTI-50`.

| Control | Asserts |
|---|---|
| `MTI-05` | stored context equals derived context, per object type |
| `MTI-16` | derived state resolves to a single `CTX` |
| `MTI-19` | context conformance, system-wide |
| `MTI-23` | a derived value carries the `CTX` of its inputs |
| `MTI-24` | no computation aggregates across a context boundary |
| `MTI-30` | a deferred run whose authority has lapsed does not execute |
| `MTI-46` | context is conserved across handoffs |
| `MTI-50` | control evidence is retained and inspectable |

**Seven of the eight assert a property of `CTX`. The eighth, `MTI-50`, asserts retention.** `MTI-30` is the only one that touches authority at all, and it asserts a **runtime precondition on one path** — a lapsed grant blocks one deferred run — not a continuously asserted conformance property over recorded acts.

**No invariant in the published set requires a control that asserts an authorization property.** Class **`A` within boundary `B-02`**. Class **`B`** for the wider system — this session searched the invariant set, not every artifact in the programme, and `NO EVIDENCE FOUND` is not `DOES NOT EXIST`.

### 9.2 Why it is material and not cosmetic

The consolidation's `04` §2.1 rule 4 requires context and authority to be **evidenced separately**. The published fields deliver that asymmetrically:

| Half | Value carried by | Attestation carried by | Control behind the attestation |
|---|---|---|---|
| **Context** | `HF-CTX-01` .. `HF-CTX-05` | **`HF-CTX-06`** | **`MTI-19`** |
| **Authority** | `HF-CTX-08` | **nothing** | **nothing** |

`06` §3.1 of the invariant set states the governing distinction exactly: *"Without them the payload asserts a company. With them it states **how** the company was determined and **when** that determination was last independently checked. That is the difference between carriage and guarantee."*

**The authority half of element 10's widened obligation is currently carriage, not guarantee** — the same defect the whole of element 10's treatment exists to remove, reproduced one level along on the axis `MTI-D-02` has just made mandatory.

`HF-CTX-11` and `CF-I-03` are the remedy. **`HF-CTX-11` presently references a control that does not exist**, which is why `MTI-43` R2's status does not move and why element 10 remains `specified, not built, not verified` under `AAS-V-01`.

### 9.3 What is escalated

`L13-CF-01` — **authorization conformance as a continuously asserted property**. All six fields at `12` §6.

---

## 10. Model Status

| Dimension | Status |
|---|---|
| Is the `CTX` / `AUTH` relationship stated? | **Yes** — two tuples, six rules, three attachment points, full deferral semantics |
| Does it discharge `RC-F-05`? | **The specification half only.** `RC-F-05` records the gap as *"in the specification"*; the specification now exists. **The finding is not closed** — closure requires implementation and independent verification |
| Is every function given an axis set? | **Yes — 41 of 41** |
| Is any axis set verified? | **No. 0 of 41.** No implementation exists |
| Is the enforcement-point set complete? | **No.** `EP-P` is added; whether nine classes are sufficient is untested, and `MTI-CH-02`'s non-minimisation note applies here too |
| Is the operation-type axis usable at platform level? | **No** — `CF-F-04`, `CF-D-02` unruled |
| Does authorization have a conformance control? | **No** — `CF-F-05`, `CF-I-03` specified and not built |
| Is `location` an authorization axis? | **Unruled** — `RC-D-01`. Design proceeds on the three ruled dimensions |
| Is any of it Thai-validated? | **No** — `0 of 78`. Every operation-type label and every class name is unvalidated |
| Does it authorize implementation? | **No.** `RC-V-01`, `AAS-V-02` |

`SPECIFIED, NOT BUILT, NOT VERIFIED`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
