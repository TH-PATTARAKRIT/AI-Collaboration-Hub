# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 08 — Proof Requirement Register — All Thirteen Mandated Themes

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `60 PROOF REQUIREMENTS — 48 CARRIED, 12 ADDED — 0 OF 60 EXECUTABLE TODAY — 0 PROOFS PRODUCED — 7 STILL NOT DEFINABLE`

---

## 1. The Rule This File Applies

**A proof requirement is a proposition plus an acceptance criterion. It is not a proof.**

A proof needs three things: a proposition, an implementation, and a test of the implementation against the proposition. This chain supplies the first and the third. **No implementation exists, and no session in this chain has produced one.** Therefore:

> **No theme in this file is recorded as proven, verified or satisfied, and none may be recorded as such on the basis of this file.**

AAS+ advice `27` §6 states the governing condition and it is unchanged: *"If a downstream package cannot produce proof for this control, AAS+ must keep the relevant item in `HOLD`. This ruling specifies the required control model; it does not verify that the model has been built."*

### 1.1 Proof-state vocabulary — carried unchanged

| State | Meaning |
|---|---|
| `DEFINABLE` | Proposition and acceptance criterion complete. Executable the moment an implementation exists |
| `DEFINABLE — CONDITIONAL` | Definable once a named ruling or input arrives; the dependency is cited |
| `NOT DEFINABLE` | The proposition itself cannot yet be stated, because the capability it would test is unspecified |
| `HELD` | Definable as to context; its content carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

### 1.2 Identifier discipline

`RC-P-01` .. `RC-P-48` are **carried unchanged** — not renumbered, not retired, not merged, not restated in full. Their propositions and acceptance criteria at `07` and `08` of the consolidation remain authoritative. This file states, for each, its **R2 state**, whether that state **moved**, and its blocker.

New requirements take `CF-P-01` .. `CF-P-12` and extend the series rather than replacing any part of it.

---

## 2. Theme Summary — The Answer To The Authorization's Question 3

Every theme is stated with its overall definability and its governing blocker. **No theme is `PROVEN`.**

| # | Theme | Baseline | New | Overall State | Governing Blocker |
|---:|---|---|---|---|---|
| 1 | Tenant/company product isolation | `RC-P-01`..`-04` | `CF-P-01` | **`DEFINABLE`** | Implementation; independent check of this re-specification (`RC-V-01`) |
| 2 | Duplicate names/codes/barcodes without identity collision | `RC-P-05`..`-08` | `CF-P-02` | **`DEFINABLE` except one** | `RC-P-08` **`NOT DEFINABLE`** — privileged-bypass path enumeration |
| 3 | Warehouse-specific authorization | `RC-P-09`..`-12` | — | **`DEFINABLE`** | Implementation |
| 4 | Operation-Type-specific authorization | `RC-P-13`..`-16` | `CF-P-03`, `CF-P-04` | **`DEFINABLE` except two** | `RC-P-16` now **doubly** conditional — Lane C **and** `CF-D-02`; `CF-P-03` conditional on `CF-D-02` |
| 5 | Cross-company report prevention by default | `RC-P-17`..`-19` | — | **`DEFINABLE`** | Implementation |
| 6 | Controlled mapping / provenance for group reporting | `RC-P-20`..`-22` | `CF-P-10` | **2 `NOT DEFINABLE`, 1 `HELD`, 1 `DEFINABLE`** | `RC-F-03` mapping layer unspecified; `MTI-D-04` unruled; `AAS-V-03` |
| 7 | SaaS pool configuration boundary | `RC-P-35`..`-44` | `CF-P-12` | **`DEFINABLE — CONDITIONAL`** | `RC-F-06` open-ended list; `RC-D-02` unruled |
| 8 | Private Company escalation criteria | `RC-P-45`..`-48` | `CF-P-11` | **3 `NOT DEFINABLE`, 1 split, 1 `DEFINABLE`** | `RC-D-03` no criteria; `RC-F-07` no invariants for the topology |
| 9 | Scheduler / background job context carriage | `RC-P-23`..`-25` | `CF-P-05` | **`DEFINABLE` except one** | `RC-P-25` partial only — `RISK-C02` |
| 10 | API / import / export context carriage | `RC-P-26`..`-28` | — | **`DEFINABLE` except one** | `RC-P-28` conditional — `MTI-D-04` unruled |
| 11 | Immutable audit trail context | `RC-P-29`..`-31` | `CF-P-06`, `CF-P-07` | **`DEFINABLE`, one not exercisable** | `RC-P-31` would be satisfied by a broken system — `RISK-C02` |
| 12 | Negative access tests | structural | `CF-P-08` | **`DEFINABLE` as a specification** | Full specification at `09` |
| 13 | Cross-module handoff context — eight modules | `RC-P-32`..`-34` | `CF-P-09` | **`DEFINABLE` except two halves** | `RC-P-34` value half `HELD`; `CF-P-09` conditional on `CF-D-04` |

---

## 3. Themes 1 And 2 — Product Isolation And Non-Colliding Duplication

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-01` — a product resolves to exactly one company | `DEFINABLE` | **Yes, in blocker.** Its published blocker was *"Implementation. Requires `RC-F-01` re-specification first."* **The re-specification now exists** at `03` and `06` | Implementation, **and an independent check of this re-specification.** `RC-V-01` is discharged by the check, not by the document |
| `RC-P-02` — no cross-company product read on any of the thirteen surfaces | `DEFINABLE` | No | Implementation |
| `RC-P-03` — no module infers product identity | `DEFINABLE` | **Yes, in scope.** The module set is now **eight**, Payment included — `MTI-45` R2 | Implementation; the Payment half additionally `CF-D-04` |
| `RC-P-04` — isolation holds on derived surfaces | `DEFINABLE` | No | Implementation. `R4-F-22` open |
| `RC-P-05` — identical code/name/barcode/UoM in two companies both succeed, with no duplicate condition raised | `DEFINABLE` | No. **This remains the proof that Option B was implemented rather than tolerated** | Implementation |
| `RC-P-06` — identical values never collide into one identity | `DEFINABLE` | No | Implementation. `MTI-F-01` |
| `RC-P-07` — absence does not leak existence across the duplication boundary | `DEFINABLE` | **Yes, in scope.** The channel list grows to eight — `06` §7 — because categories, nomenclatures and unit groups become company-owned | Implementation. `MTI-F-03`, widened twice and **not re-scored** |
| `RC-P-08` — no process merges or correlates products by attribute similarity | **`NOT DEFINABLE`** | No | **The privileged, system, background, administrative and migration path enumeration.** The bypass-path audit was started and never completed. Same blocker as `L9-01`. Root cause at `10` §2 |

| ID | New requirement | Acceptance criterion — a rejection, not a demonstration | State | Blocker |
|---|---|---|---|---|
| **`CF-P-01`** | A company's configuration records — category, barcode nomenclature, unit group, storage category, route, rule, operation type, putaway rule, reordering rule — are not visible, selectable, referenceable or reportable outside their owning company | Each of the thirteen enforcement surfaces is exercised for a cross-company **configuration** read and **produces nothing**, not an empty-filtered result derived from a wider set | `DEFINABLE` | Implementation. Created by `CD-12` .. `CD-14`; without it the anchor change is asserted and never tested |
| **`CF-P-02`** | Two companies may hold configuration records with **identical** names, codes and structures, and both are legitimate | Creating the identical set in both companies **succeeds in both**, and neither creation raises a duplicate condition, a warning, a merge suggestion or a data-quality flag | `DEFINABLE` | Implementation. `RC-P-05` for configuration; AAS+ advice `29` §3 |

---

## 4. Themes 3 And 4 — Warehouse And Operation-Type Authorization

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-09` — warehouse context resolved before execution | `DEFINABLE` | No | Implementation. Attaches at `EP-P` — `04` §5 |
| `RC-P-10` — **negative, other company** | `DEFINABLE` | No | Implementation |
| `RC-P-11` — **negative, other warehouse, same company** | `DEFINABLE` | No. **The proof `MTI-D-02` rule 2 exists to force** | Implementation |
| `RC-P-12` — warehouse authority never widened by company authority | `DEFINABLE` | No | Implementation. `CF-I-01` |
| `RC-P-13` — operation-type context resolved before execution | `DEFINABLE` | No | Implementation. `EP-P` |
| `RC-P-14` — **negative, other operation type, same warehouse** | `DEFINABLE` | **Yes, in test-set derivation.** The set must derive from the **implemented** operation types **and their platform classes** (`CF-I-05`), not from `MTI-D-02` §5's illustration, which is explicitly open | Implementation; class enumeration `CF-D-02` for the platform half |
| `RC-P-15` — **negative, no axis substitutes for another** | `DEFINABLE` | No. Four directed attempts, each rejected | Implementation. `CF-I-01` |
| `RC-P-16` — segregation of duties is expressible and degrades rather than breaks | **`DEFINABLE — CONDITIONAL` on Lane C *and* `CF-D-02`** | **Yes — a regression.** It carried one condition and now carries two | **The compensating-control content requires Thai user input** (`MTI-F-05`, `R4-F-21`, `0 of 78`); **and a platform-level segregation rule cannot bind to a tenant-defined operation-type label** (`CF-F-04`). Reported as a regression rather than smoothed over |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-03`** | Every tenant-configured operation type declares exactly one platform-owned operation class, and platform-level controls bind to the class | Creating an operation type without a class is **rejected**; a platform control expressed over a class binds to every tenant type of that class in every company; changing a type's class after any completed movement through it is **rejected** | **`DEFINABLE — CONDITIONAL (CF-D-02)`** | The platform class enumeration is unruled. `CF-F-04`, `CF-I-05` |
| **`CF-P-04`** | Defining a configuration object confers no authority to act through it | An actor who creates an operation type, warehouse, route or rule and holds no grant over it is **refused** on every act through it; the refusal is recorded | `DEFINABLE` | Implementation. `CF-I-04`; `RC-P-40`'s criterion promoted |

---

## 5. Themes 5 And 6 — Cross-Company Report Prevention, And Controlled Mapping

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-17` — cross-company aggregation is **impossible** by default, not merely absent | `DEFINABLE` | No | Implementation. `MTI-24` |
| `RC-P-18` — a report states the scope it was produced under, as part of its identity | `DEFINABLE` | **Yes, in content.** The identity now includes the **`AUTH` set** as well as the `CTX` scope — `07` §3 row 7 | Implementation. `MTI-28` |
| `RC-P-19` — scope applied **before** evaluation, never as a post-filter | `DEFINABLE` | No. Row counts, aggregates and pagination totals must not reveal the wider set | Implementation |
| `RC-P-20` — a group-level cross-company view exists **only** through an explicit authorized mapping | **`NOT DEFINABLE`** | No | **`RC-F-03`.** A proposition cannot be written against an object that does not exist. Root cause at `10` §3 |
| `RC-P-21` — a mapping asserts correspondence and never merges identity | **`NOT DEFINABLE`** | No | `RC-F-03` |
| `RC-P-22` — no cross-company view carries valuation content | **`HELD`** | No | **`AAS-V-03` in force.** `JT-01` **NOT DECIDABLE**; `GAP-FS-07` path never traced. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-10`** | **In the absence of an authorized mapping, no cross-company correspondence exists** and none may be created, asserted, inferred or relied upon | No scheduled, administrative, reporting, export, migration or maintenance path produces, stores or presents a correspondence between products, categories, nomenclatures or unit groups in different companies. **Attempting to record one is refused, and the refusal is an event** | `DEFINABLE` | Implementation. `CF-I-06` |

### 5.1 Theme 6's honest position

The authorization directs this session to *"say so or close them"* on the two `NOT DEFINABLE` requirements in theme 6.

**They are said, not closed.** `RC-P-20` and `RC-P-21` remain `NOT DEFINABLE` and this session cannot make them otherwise: the object they would test is unspecified (`RC-F-03`), its specification is gated on `MTI-D-04` (`RC-F-04`, unruled), and its commissioning is `RC-D-04` (unruled). Specifying it here would design a door before Boss has decided whether there is one.

**What this session can add, and does, is `CF-P-10`.** The *prohibition* that holds in the object's absence is testable even though the object is not. Theme 6 therefore moves from *three requirements, none of which can be executed and two of which cannot be stated* to *four requirements, one of which can be stated and would be executable against an implementation.* **That is a change in definability of one requirement. It is not progress toward the mapping layer, and it does not reduce `RC-F-03`.**

---

## 6. Theme 7 — SaaS Pool Configuration Boundary

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-35` — the platform-owned record set is enumerated, published and complete | `DEFINABLE — CONDITIONAL` | No | **`RC-F-06`** — `MTI-D-03` §3 ends with *"other approved…"*. An open-ended list cannot satisfy *complete* |
| `RC-P-36` — the tenant-configurable set is enumerated and every instance carries a `CTX` | `DEFINABLE — CONDITIONAL` | **Yes, in status elsewhere.** Its acceptance criterion is now also an invariant — `CF-I-07` — so the requirement and the design agree where before only the requirement stated it | `RC-F-06` |
| `RC-P-37` — the six prohibitions hold absolutely in the pool | `DEFINABLE — CONDITIONAL` | No | Prohibitions 1, 2, 3, 6 have a defined escalation route; **4 and 5 do not** — `RC-D-03` |
| `RC-P-38` — configuration is configuration-led | `DEFINABLE` | No | Implementation. `MTI-CH-01` — whether `STORE` enforcement is achievable is a Team B question, not approached |
| `RC-P-39` — configuration never weakens `MTI-D-01` | `DEFINABLE`, **`HELD` on the costing facet** | **Yes, in scope.** Now tested on **three** configurable classes touching product semantics — Product Category, UoM Category **and Barcode Nomenclature** — because `CD-13` makes the third company-owned and it resolves product identity | `RC-F-08`; costing facet **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| `RC-P-40` — configuration never weakens `MTI-D-02` | `DEFINABLE` | No | Implementation. Its criterion is promoted to `CF-I-04` and separately tested at `CF-P-04` |
| `RC-P-41` — configuration versioned with effective dates, never regenerated in place | `DEFINABLE` | No | Implementation. `MTI-35`, `MTI-36`, `IV-15` |
| `RC-P-42` — reconfiguration never re-derives a record without its company | `DEFINABLE` | No. **Still the highest-value configuration proof in the chain** — the `R4-F-09` condition produced in bulk by an ordinary administrative action | Implementation. `SAAS-04` regeneration, untouched by any ruling |
| `RC-P-43` — every configuration change is an auditable act | `DEFINABLE` | **Yes, in content.** The act must now carry the four-axis `AUTH`, not the actor and authority alone — `MTI-38` R2 | Implementation |
| `RC-P-44` — reversibility is version supersession, never in-place mutation | `DEFINABLE` | No. **Reversion is a forward act** | Implementation |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-12`** | A change to a configuration record's **company anchor** is an evented, approved act carrying before and after values — and for a record that has participated in a completed act, is **refused** | Attempting to re-anchor a category, nomenclature or unit group to another company after any completed movement resolved to it is **refused**; the refusal is an event; the only permitted path is an evidenced migration act | `DEFINABLE` | Implementation. `MTI-06`, `MTI-40` R2, `CD-12` .. `CD-14`. **The migration path itself needs `GAP-FS-08`, which does not exist** |

---

## 7. Theme 8 — Private Company Escalation Criteria

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-45` — every requirement is classifiable as pool-safe or Private-Company-required | **`NOT DEFINABLE`** | No | **`RC-D-03`** — no criteria exist. `05` §4 of the consolidation shows the classification failing on **4 of 7** live requirement classes |
| `RC-P-46` — a Private Company preserves every control rule the pool preserves, or names each one it changes | **`NOT DEFINABLE`** | No | **`RC-F-07`** — no invariant, matrix row, proof or scenario is written for the topology |
| `RC-P-47` — separation occurs only through an explicit Gate record with evidence and a Boss ruling | **`DEFINABLE` in its prohibition half; `NOT DEFINABLE` in its positive half** | No | The Gate record's required **content** is unspecified. **The prohibition is enforceable today** and is the one usable requirement in this theme |
| `RC-P-48` — movement between pool and Private Company preserves immutable history | **`NOT DEFINABLE`** | No | `MTI-06` makes the context spine immutable; `GAP-FS-08` does not exist. **Neither path is specified** |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-11`** | Every invariant, proof, scenario and attack states the isolation topology it was established in, and no result is cited as evidence about another topology | Each artifact carries a topology scope statement; a citation of a pool-established result in a Private Company context is **refused at review**, not at runtime | `DEFINABLE` **as a governance control** | None for the control itself. **It supplies no Private Company content and reduces `RC-F-07` by nothing** — `CF-I-08` |

### 7.1 Theme 8's honest position

The authorization records that **three** of these are `NOT DEFINABLE`. That is confirmed, and the fourth is split rather than whole. **Nothing this session can do makes them definable**, because the missing input is a Boss ruling (`RC-D-03`) and not an analysis.

`CF-P-11` is added not to improve the count but to stop the specific harm `RC-F-07` warns of: a proof produced in the pool being read later as evidence about a topology it was never run in. **It is a labelling control. Recording it as progress toward theme 8 would be a softening, and it is not recorded that way.**

---

## 8. Themes 9 And 10 — Scheduler, Background, API, Import, Export

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-23` — every scheduled or background run resolves exactly one `CTX` **and an explicit operation-type context** | **`DEFINABLE`** | **Yes — from `DEFINABLE — CONDITIONAL`.** Its condition was `RC-F-05`, *"the relationship between `CTX` and `AUTH` for deferred execution is unspecified"*. **`04` §7 specifies it** and `CF-I-02` states it as an invariant | Implementation, **and an independent check of that specification**. `RC-F-05` is **not closed** |
| `RC-P-24` — a deferred run whose authority has lapsed does not execute | `DEFINABLE` | **Yes, in content.** *"Lapsed"* now means any of four axes lapsed, narrowed or revoked — `MTI-30` R2 | Implementation. `L13-MT-01` |
| `RC-P-25` — two runs with the same identity do not execute concurrently | **`DEFINABLE` — partial only** | No | `MTI-31` supplies run scoping, **not idempotency identity**. `RISK-C02` open; a retried run remains indistinguishable from a second genuine run. **`C-02` severity is a Boss ruling and is not classified here** |
| `RC-P-26` — API execution carries `AUTH` explicitly on every call | `DEFINABLE` | **Yes, in content.** `AUTH` is four-axis; an endpoint accepting company alone is non-compliant | Implementation |
| `RC-P-27` — import supplies context explicitly and never infers it from file content | `DEFINABLE` | **Yes, in content.** A file naming a warehouse or an operation type is not thereby authorized for either | Implementation. `MTI-42` applied to import |
| `RC-P-28` — export is scoped by `AUTH` and cannot become the unsanctioned cross-company read | `DEFINABLE — CONDITIONAL (MTI-D-04)` | No. **Under Option B the pressure on this requirement is higher, not lower** — a group maintains several catalogues, so the group-view need is larger and export is where it goes (`MTA-09`) | `MTI-D-04` **unruled** |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-05`** | A deferred run carries the full four-axis `AUTH` from scheduling and **revalidates it in full at release**, while carrying `CTX` unchanged and never re-resolving it from current configuration | Revoke or narrow **each** axis in turn — company deactivated, warehouse grant withdrawn, operation-type grant withdrawn, actor access removed — release the queued run, and in **each** case it does not execute and the non-execution is an event naming the axis that failed. Separately, change configuration between scheduling and release and confirm the run's `CTX` is **not** re-resolved | `DEFINABLE` | Implementation. `CF-I-02`, `MTI-30` R2, `MTI-41`, `R-05` at `04` §3 |

---

## 9. Theme 11 — Immutable Audit Trail Context

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-29` — every context-bearing act emits an immutable event carrying the full context, authority, both dates and the evidence reference | `DEFINABLE` — **widened** | **Yes, in content.** The event carries the **full four-axis `AUTH` as a resolved tuple** — `MTI-38` R2, `CD-26` | Implementation |
| `RC-P-30` — the audit trail is subject to the same isolation as the records it describes | `DEFINABLE` | **Yes, in content.** *"The same isolation"* is now four-axis; an actor may not read audit entries outside their `AUTH` set | Implementation |
| `RC-P-31` — replay reproduces context deterministically | `DEFINABLE` — **not exercisable** | No | `MTI-41` states the property; **`RISK-C02` means the test would be satisfied by a broken system.** Replayed duplicates are individually context-correct and collectively wrong, and `MTI-19` would report no breach |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-06`** | An **authorization conformance control** exists, runs continuously, raises on breach and never silently repairs; its runs are retained, context-scoped and inspectable | Introduce, by direct manipulation, a recorded act whose `AUTH` was not within any grant in force at the time of the act; the control **raises**. Introduce a recorded act with an absent axis where the object carries that axis; the control **raises**. Introduce a grant spanning two companies; the control **raises**. In every case the control's own run is retained and readable by an auditor | `DEFINABLE` | Implementation. **`CF-I-03` — the control does not exist.** `CF-F-05`, `L13-CF-01` |
| **`CF-P-07`** | Every emitted fact carries `HF-CTX-10` and `HF-CTX-11`, and a consumer **rejects** a fact whose authorization attestation is absent, stale or failing | Emit a fact with `HF-CTX-11` absent — the consumer rejects. Emit one whose referenced control run reports a breach — the consumer rejects. Emit one whose referenced control run predates the act — the consumer rejects | `DEFINABLE` | Implementation, **and `CF-I-03`, since `HF-CTX-11` presently references a control that does not exist**. `MTI-43` R2, `MTI-45` R2 |

### 9.1 The distinction theme 11 now rests on

`09` §3.2 of the invariant set establishes that **context conformance and duplicate freedom are independent properties, and neither implies the other.** Conformance adds a third and a fourth:

| Property | Asserted by | Exists? |
|---|---|:---:|
| Context conformance | `MTI-19` | Specified, not built |
| Duplicate freedom | nothing — `RISK-C02` | **No** |
| **Authorization conformance** | **`CF-I-03`** | **Specified here, not built** |
| Attestation freshness | `HF-CTX-06`, `HF-CTX-11` + `MTI-50` | Specified, not built |

**None implies another.** A system can be context-conformant, authorization-conformant, and still produce duplicate facts; and it can be duplicate-free and still record acts nobody was authorized to perform.

---

## 10. Theme 12 — Negative Access Tests

Structural. **Every acceptance criterion in this file is written as a rejection that must occur, never as an operation that must succeed.** The expected result is a refusal; a successful operation is a **failed proof**.

`N-01`, `N-02` and `N-03` are carried unchanged from the consolidation's `07` §8 and are extended at `09` of this package, which is theme 12's full specification.

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-08`** | **A refusal is an act and emits an event.** An act refused for want of `AUTH` emits an event carrying the `CTX` it was attempted in, the `AUTH` found insufficient, and which axis failed | For each of the four axes, on each of the thirteen enforcement surfaces, a refused act produces an event; the event is itself context-scoped; and **the event's existence is not disclosed to an actor outside the target's `AUTH` set** | `DEFINABLE` | Implementation. `R-06` at `04` §3; `N-02`, `N-03` |

**`CF-P-08` carries an internal tension that is stated rather than resolved:** `N-02` requires every refusal to be recorded, and `N-03` requires a refusal to disclose nothing. Recording a refusal in a context-scoped audit trail satisfies both only if the trail is scoped to the **target's** context and not the **attempting actor's**. That is a design consequence, it is stated here, and it is one of the reasons `09` exists as a separate specification.

---

## 11. Theme 13 — Cross-Module Handoff Context, Eight Modules

| ID | R2 State | Moved? | Blocker |
|---|---|---|---|
| `RC-P-32` — every handoff payload carries the context field group **and the evidence of it** | `DEFINABLE` — **widened twice** | **Yes, in content.** The field group is now eleven fields and the evidence is **two** attestations | Implementation, **and `CF-I-03`**. **`AAS-V-01` in force — element 10 is `specified, not built, not verified`** |
| `RC-P-33` — no consuming module infers, defaults or reconstructs context | `DEFINABLE` | **Yes, in scope.** Eight modules, Payment included | Implementation; Payment half `CF-D-04` |
| `RC-P-34` — context is **conserved** across the handoff boundary | **`DEFINABLE` for the count half; `HELD` for the value half** | **Yes, in content.** The conserved quantity is a **four-part** context — `MTI-F-06` widened | `RC-11`. **Value half `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |

| ID | New requirement | Acceptance criterion | State | Blocker |
|---|---|---|---|---|
| **`CF-P-09`** | Payment consumes any Inventory-originated fact under `PAY-01` .. `PAY-05` — never inferring company from a payment instrument, bank account, vendor, customer, currency or settlement route | A settlement referencing an Inventory-originated fact whose company differs from the instrument's is resolved to the **fact's** company; a settlement act spanning companies is **refused**, there being no `MTI-22` register entry for it | **`DEFINABLE — CONDITIONAL (CF-D-04)`** | Whether Payment is a direct consumer is unruled. **No Inventory-to-Payment handoff is published within boundary `B-01`** — `07` §4 |

---

## 12. Roll-Up

### 12.1 By state

| State | Count | IDs |
|---|---:|---|
| `DEFINABLE` | **38** | `RC-P-01`..`-07`, `-09`..`-15`, `-17`..`-19`, `-24`, `-26`, `-27`, `-29`, `-30`, `-32`, `-33`, `-38`, `-40`..`-44`, `RC-P-23`, and `CF-P-01`, `-02`, `-04`, `-05`, `-06`, `-07`, `-08`, `-10`, `-11`, `-12` |
| `DEFINABLE — CONDITIONAL` | **9** | `RC-P-16` (two conditions), `-28`, `-35`, `-36`, `-37`, `-39` non-costing half, `CF-P-03`, `CF-P-09`, and `RC-P-31` definable-but-not-exercisable |
| `DEFINABLE` — partial only | **1** | `RC-P-25` |
| **`NOT DEFINABLE`** | **7** | `RC-P-08`, `-20`, `-21`, `-45`, `-46`, `-48`, and the positive half of `RC-P-47` |
| `HELD` under the COGS Gap | **3** | `RC-P-22`, the value half of `RC-P-34`, the costing facet of `RC-P-39` |
| **Total requirements** | **60** | 48 carried unchanged + 12 added |
| **Executable today** | **0** | **No implementation exists** |
| **Proofs produced by this session** | **0** | |

Requirements split across two states are counted in each half and the halves are named, so the state counts sum above 60 by design; the **total requirement count is 60 and is exact**.

### 12.2 Definability movement

| Movement | Count | Detail |
|---|---:|---|
| `DEFINABLE — CONDITIONAL` → `DEFINABLE` | **1** | `RC-P-23` — its condition was `RC-F-05`, whose specification half is supplied at `04` |
| Blocker narrowed, state unchanged | **1** | `RC-P-01` — the re-specification its blocker named now exists |
| `DEFINABLE` → **more** conditional | **1** | `RC-P-16` — gains `CF-D-02` alongside Lane C. **A regression, reported as one** |
| `NOT DEFINABLE` → any better state | **0** | **All seven remain `NOT DEFINABLE`** |
| New requirements added | **12** | `CF-P-01` .. `CF-P-12` |
| **Requirements proven** | **0** | |

**One requirement became definable and one became more conditional. Seven that could not be stated still cannot be stated. No requirement became true.**

### 12.3 The counts that measure proof — unchanged

`0 of 8` L9 proofs · `0 of 22` cross-proof scenarios · `0 of 10` material handoffs contract-compliant · `0 of 12` Joint decisions ready · `0 of 78` Thai validations · `0 of 13` enforcement surfaces verified · `0 of 41` functions verified against any axis · `0 of 60` proof requirements executable · **`0` findings closed, `0` capabilities built, `0` vetoes discharged.**

---

## 13. The `HOLD` Condition, Restated

AAS+ advice `27` §6 and advice `29` §7 both make an unprovable or unclassifiable item a `HOLD`.

**No package in this chain has produced proof for this control. Every item governed by it therefore remains `HOLD`.** This file makes sixty proofs writable. **It does not make any of them true.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
