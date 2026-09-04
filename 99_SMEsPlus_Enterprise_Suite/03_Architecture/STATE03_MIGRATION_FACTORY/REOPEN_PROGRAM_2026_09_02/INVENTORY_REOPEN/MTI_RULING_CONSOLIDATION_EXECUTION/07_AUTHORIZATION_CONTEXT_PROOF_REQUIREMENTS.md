# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 07 — Authorization Context Proof Requirements

Control Level: `/L9999.9999`
Status: `PROOF REQUIREMENTS SPECIFIED — 0 OF 34 EXECUTABLE TODAY — NO PROOF PRODUCED BY THIS SESSION`

---

## 1. The Distinction This File Turns On

A proof needs three things: **a proposition**, **an implementation**, and **a test**. This file supplies the first and the third. **It does not supply the second, and no session in this chain has.**

Every requirement below is therefore a **proof requirement**, not a proof. AAS+ advice `27` §6 states the governing condition directly: *"If a downstream package cannot produce proof for this control, AAS+ must keep the relevant item in HOLD. This ruling specifies the required control model; it does not verify that the model has been built."*

### 1.1 Proof-state vocabulary

| State | Meaning |
|---|---|
| `DEFINABLE` | Proposition and acceptance criterion are complete. Executable the moment an implementation exists |
| `DEFINABLE — CONDITIONAL` | Definable once a named ruling or input arrives; the dependency is cited |
| `NOT DEFINABLE` | The proposition itself cannot yet be stated, because the capability it would test is unspecified |
| `HELD` | Definable as to context, but its content carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

**No requirement in this file carries a state of proven, verified, satisfied or passed, and none may be recorded as such on the basis of this file.**

---

## 2. Coverage Of The Mandated Proof Themes

The authorization at §10 mandates thirteen themes. Eleven are covered here; themes 7 and 8 are the configuration boundary and are covered at `08`.

| # | Mandated Theme | Requirements | Section |
|---:|---|---|---|
| 1 | Tenant/company product isolation | `RC-P-01` .. `RC-P-04` | §3 |
| 2 | Duplicate names/codes/barcodes without identity collision | `RC-P-05` .. `RC-P-08` | §3 |
| 3 | Warehouse-specific authorization | `RC-P-09` .. `RC-P-12` | §4 |
| 4 | Operation-Type-specific authorization | `RC-P-13` .. `RC-P-16` | §4 |
| 5 | Cross-company report prevention by default | `RC-P-17` .. `RC-P-19` | §5 |
| 6 | Controlled mapping / provenance for group reporting | `RC-P-20` .. `RC-P-22` | §5 |
| 7 | SaaS pool configuration boundary | → `08` | `08` §3 |
| 8 | Private Company escalation criteria | → `08` | `08` §4 |
| 9 | Scheduler / background job context carriage | `RC-P-23` .. `RC-P-25` | §6 |
| 10 | API / import / export context carriage | `RC-P-26` .. `RC-P-28` | §6 |
| 11 | Immutable audit trail context | `RC-P-29` .. `RC-P-31` | §7 |
| 12 | Negative access tests | Structural — see §8 | §8 |
| 13 | Cross-module handoff context | `RC-P-32` .. `RC-P-34` | §9 |

**Theme 12 is not a separate block of requirements. It is a structural rule applied to every one of the other twelve**, and §8 states why.

---

## 3. Themes 1 And 2 — Product Isolation And Non-Colliding Duplication

| ID | Proposition | Acceptance Criterion — A Rejection, Not A Demonstration | State | Blocked By |
|---|---|---|---|---|
| `RC-P-01` | A product record resolves to exactly one company within one tenant | Every product row's company anchor is mandatory and derived from a declared anchor path; a write attempting a company-less product is **rejected at `STORE`** | `DEFINABLE` | Implementation. Requires `RC-F-01` re-specification first |
| `RC-P-02` | No actor in Company A can read, search, select, report on or reference a product of Company B | Each of the thirteen enforcement surfaces at `04` §5 is exercised for a cross-company product read and **produces nothing**, not an empty-filtered result derived from a wider set | `DEFINABLE` | Implementation |
| `RC-P-03` | No module infers product identity from anything other than resolved context | Sale, Purchase, Manufacturing, Accounting, Reporting, Approval, Document and Payment each reject a product reference that does not resolve within the caller's `CTX` | `DEFINABLE` | Implementation |
| `RC-P-04` | Product isolation holds on **derived** surfaces, not only stored records | The derived surfaces named at `R4-F-22` — `INV-M10`, `INV-M11`, `INV-M14`, `INV-M15` — each fail to produce a cross-company aggregate | `DEFINABLE` | Implementation. `R4-F-22` open |
| `RC-P-05` | Two companies may hold products with **identical** code, name, barcode and UoM, and both are legitimate | Creating the identical set in both companies **succeeds in both**, and neither creation raises a duplicate condition, a warning, a merge suggestion or a data-quality flag | `DEFINABLE` | Implementation. **This is the proof that Option B was actually implemented rather than tolerated** |
| `RC-P-06` | Identical values never collide into one identity | Every read, report, export, scan and handoff of the identical pair returns **two distinct resolved identities**, never one; the bare value is never presented as the identity | `DEFINABLE` | Implementation. `MTI-F-01` |
| `RC-P-07` | Absence does not leak existence across the duplication boundary | An actor in Company A entering a code, barcode, lot or serial value in use in Company B receives a response **indistinguishable** from the value being unused. Tested on uniqueness feedback, autocomplete, barcode resolution, error text, collision messages, import validation and export scoping | `DEFINABLE` | Implementation. `MTI-F-03`, **widened by `D-01`** |
| `RC-P-08` | No process merges, links or correlates products by attribute similarity | No scheduled, administrative, migration or maintenance path exists that proposes or performs a similarity-based merge. **The path set is enumerated and the enumeration is certified complete** | **`NOT DEFINABLE`** | The path enumeration is the **privileged-bypass path audit**, started and never completed. Same blocker as `L9-01` |

---

## 4. Themes 3 And 4 — Warehouse And Operation-Type Authorization

Adopting AAS+ advice `27` §5 and extending it. Advice `27` names eight proof requirements; the four negative-access ones are `RC-P-10`, `RC-P-11`, `RC-P-14` and `RC-P-15`.

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-09` | Every warehouse-sensitive action resolves warehouse context **before** execution | Permission is evaluated before search, selection, confirmation, posting handoff, report generation, export, import, scheduler execution and API execution — **not applied as a filter afterwards** | `DEFINABLE` | Implementation |
| `RC-P-10` | **Negative — other company.** An actor with no authority in Company B cannot act in Company B | Attempt rejected at every one of the thirteen surfaces; rejection recorded | `DEFINABLE` | Implementation |
| `RC-P-11` | **Negative — other warehouse, same company.** An actor authorized for Warehouse 1 cannot read or write in Warehouse 2 of the same company | Attempt rejected; rejection recorded. **This is the proof `D-02` rule 2 exists to force** | `DEFINABLE` — conditionality removed by the ruling | Implementation |
| `RC-P-12` | Warehouse authority is never widened by company authority | An actor with company-level authority and no warehouse grant cannot act in any warehouse. `AUTH` is a **subset** of a `CTX`, never a superset | `DEFINABLE` | Implementation |
| `RC-P-13` | Every operation-sensitive action resolves operation-type context before execution | As `RC-P-09`, for the operation-type axis | `DEFINABLE` | Implementation |
| `RC-P-14` | **Negative — other operation type, same warehouse.** An actor authorized for Receipt cannot perform Delivery, Internal Transfer, Adjustment, Scrap, Replenishment or Landed Cost action in the same warehouse | Attempt rejected per operation type; rejection recorded. **The operation-type list is open (`D-02` §5 says "including, but not limited to"), so the test set must be derived from the implemented set, not from the ruling's examples** | `DEFINABLE` | Implementation |
| `RC-P-15` | **Negative — no axis substitutes for another.** Operation type does not confer warehouse; warehouse does not confer company; company does not confer tenant | Four directed attempts, each rejected | `DEFINABLE` | Implementation |
| `RC-P-16` | Segregation of duties is expressible and degrades rather than breaks | A segregation rule can be stated over the four `AUTH` axes; where no second qualifying actor exists **within the same company**, the compensating control engages and **approval does not route across a company boundary** | **`DEFINABLE — CONDITIONAL (Lane C)`** | The compensating-control **content** requires Thai user input. `MTI-F-05`, `R4-F-21`, `0 of 78` |

---

## 5. Themes 5 And 6 — Cross-Company Report Prevention, And Controlled Mapping

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-17` | **Cross-company aggregation is impossible by default.** Not merely absent — impossible | No sum, count, average, forecast, ranking, alert or derived measure spans more than one company unless an authorized grant is present. Attempted without a grant, the computation **does not execute** | `DEFINABLE` | Implementation. `MTI-24` |
| `RC-P-18` | Every report states the `CTX` scope it was produced under, as part of its identity | Two reports over different scopes are **different reports** and the system refuses to present them as comparable | `DEFINABLE` | Implementation. `MTI-28` |
| `RC-P-19` | Scope is applied **before** evaluation, never as a post-filter | A report over a wider set filtered down is distinguishable from a report scoped before evaluation, and only the latter is produced. **Row counts, aggregates and pagination totals must not reveal the wider set** | `DEFINABLE` | Implementation |
| `RC-P-20` | A group-level cross-company view exists **only** through an explicit authorized mapping | No aggregation across companies occurs without a mapping; the mapping is named, authorized, versioned and logged per use | **`NOT DEFINABLE`** | **`RC-F-03`** — the mapping layer is unspecified. A proposition cannot be written against an object that does not exist |
| `RC-P-21` | A mapping asserts correspondence and never merges identity | After mapping, both products remain separately addressable, separately reportable and separately auditable in their own companies | **`NOT DEFINABLE`** | `RC-F-03` |
| `RC-P-22` | No cross-company view carries valuation content | Any mapped or granted cross-company output is quantity-and-context only | **`HELD`** | **`AAS-V-03` in force.** `JT-01` **NOT DECIDABLE**; `GAP-FS-07` path never traced. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

**`RC-P-20` and `RC-P-21` are the two requirements this session cannot even state as testable propositions.** That is the practical cost of `RC-F-03`, and it is why the mapping layer is `BLOCKING` for group-level reporting rather than merely missing.

---

## 6. Themes 9 And 10 — Scheduler, Background, API, Import, Export

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-23` | Every scheduled or background run resolves **exactly one** `CTX` and carries an explicit operation-type context | A run covering several companies is an enumerated set of single-context executions, each with its own identity and result. A run with defaulted, inherited or inferred context **does not execute** | **`DEFINABLE — CONDITIONAL`** | **`RC-F-05`** — operation type is not in the `CTX` tuple. The relationship between `CTX` and `AUTH` for deferred execution is unspecified |
| `RC-P-24` | A deferred run whose scheduling authority has lapsed **does not execute**, and the non-execution is recorded | Revoke the scheduling actor's access, deactivate the company, or expire the grant, then release the queued run: it does not run, and the refusal is an event | `DEFINABLE` | Implementation. `MTI-30`, `L13-MT-01` |
| `RC-P-25` | Two runs with the same identity do not execute concurrently within a `CTX` | Concurrent release is serialised or refused | **`DEFINABLE` — partial only** | `MTI-31` supplies run scoping, **not idempotency identity**. `RISK-C02` open; a retried run is still indistinguishable from a second genuine run |
| `RC-P-26` | API execution carries `AUTH` explicitly on every call | No endpoint accepts an action whose tenant, company, warehouse or operation-type context is absent, defaulted or derived from the payload's own content | `DEFINABLE` | Implementation |
| `RC-P-27` | Import supplies context explicitly and never infers it from file content | An import file naming a company, warehouse or product is **not** thereby authorized for it; context comes from the authenticated caller's `AUTH`, and rows outside it are rejected individually with the rejection recorded | `DEFINABLE` | Implementation. `MTI-42`'s prohibition on inference, applied to import |
| `RC-P-28` | Export is scoped by `AUTH` and cannot become the unsanctioned cross-company read | No export spans companies without a grant; every export records its scope, its authority and its content boundary | **`DEFINABLE — CONDITIONAL (`MTI-D-04`)`** | `MTA-09` records export as the path the unsanctioned need takes. Until `MTI-D-04` is ruled, the sanctioned alternative does not exist |

---

## 7. Theme 11 — Immutable Audit Trail Context

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-29` | Every context-bearing act emits an **immutable** event carrying the full `CTX`, the full `AUTH` relied on, the actor, the physical event date and entry date as **two distinct values**, and the evidence reference | The event is not amendable; a correction is a new event linked to the original; the audit trail answers *who did what, in which tenant, company, warehouse and operation type* | **`DEFINABLE` — widened** | Implementation. `MTI-38`; **`D-02` widens the required content beyond what `MTI-38` states** |
| `RC-P-30` | The audit trail is subject to the **same** isolation as the records it describes | An actor cannot read audit entries outside their `AUTH`; and the audit surface does not leak existence (`RC-P-07` applied to the trail itself) | `DEFINABLE` | Implementation |
| `RC-P-31` | Replay of the event stream reproduces context **deterministically** | Replaying produces identical context assignments; and the replay is distinguishable from original execution | **`DEFINABLE` — not exercisable** | `MTI-41` states the property; **`RISK-C02` means a replay's duplicates would be individually context-correct and collectively wrong, and the `MTI-19` conformance control would report no breach.** `GAP-FS-08` provenance absent |

`RC-P-31` is the sharpest example in this file of why specification is not proof: the property is stated, the test is writable, and the test would **pass on a broken system**.

---

## 8. Theme 12 — Negative Access Tests, As A Structural Rule

Negative testing is not a section of this file. It is the **form** of the file.

Every acceptance criterion above is written as *a rejection that must occur*, never as *an operation that must succeed*. This follows the invariant set's `MTP-*` convention: **the expected result is a rejection; a successful operation is a failed proof.**

The four negative access tests AAS+ advice `27` §5 requires explicitly are `RC-P-10` (other company), `RC-P-11` (other warehouse, same company), `RC-P-14` (other operation type, same warehouse), and `RC-P-15` (no axis substitutes). Beyond those, three structural rules apply to every requirement in this file:

| # | Rule | Reason |
|---:|---|---|
| N-01 | **A negative result must be produced by refusal, not by an empty result set.** An empty list derived from a wider query is a filtered leak, not isolation | `RC-P-19`; `MTI-24` |
| N-02 | **Every refusal is recorded.** A refusal that leaves no trace cannot be distinguished from an attempt that never happened | `MTI-38`; `RC-P-29` |
| N-03 | **A refusal must not itself disclose.** The refusal text, code, timing and shape must be identical whether the target exists in another context or does not exist at all | `MTI-27`; `RC-P-07` |

**N-03 is the rule most likely to be violated by a correct implementation**, because a system that correctly refuses cross-context access will naturally produce a different message from one that finds nothing — and that difference is the disclosure.

---

## 9. Theme 13 — Cross-Module Handoff Context

The authorization names Sale, Purchase, Manufacturing, Accounting, Approval, Payment, Document and Reporting. The invariant set specified seven consuming modules; **Payment is named in this authorization and appears in no prior consuming-module table.**

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-32` | Every handoff payload carries the context field group **and the evidence of it** — value, derivation path, and conformance attestation | `HF-CTX-01`, `-02`, `-05`, `-06`, `-08` present and non-inferable on every material handoff; a consumer **rejects** a fact whose attestation is absent or failing | **`DEFINABLE` — widened** | **`AAS-V-01` in force.** Element 10 is `specified, not built, not verified` and no other wording may be substituted. `D-02` widens the attestation to warehouse and operation type — `MTI-F-04` |
| `RC-P-33` | No consuming module infers, defaults or reconstructs context | Each of the eight modules rejects a fact with absent context rather than supplying one. **Accounting posts within the company the fact resolves to and no other** | `DEFINABLE` | Implementation |
| `RC-P-34` | Context is **conserved** across the handoff boundary | A reconciliation exists that compares context on both sides and detects a fact that crossed a boundary, **which no existing reconciliation does** — both domains can balance internally while a fact has moved | **`DEFINABLE` for the count half; `HELD` for the value half** | `MTI-F-06`, identity `RC-11`. Value half `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

### 9.1 Payment — a module with no published context obligation

Payment is named in this authorization's theme 13 and does not appear in the invariant set's seven-module obligation table (`06` §6: Accounting, Purchase, Sale, Manufacturing, Approval, Document, Reporting).

This session does **not** author Payment's obligation. Doing so would be design work outside a consolidation's authority, and Payment's relationship to Inventory runs through Purchase and Accounting rather than directly. It is recorded as a **coverage gap in the successor prompt's scope**, at `13` §7 theme 13, so that the re-specification pass either states Payment's obligation or records why Payment has none.

Recorded as `RC-F-09`.

---

## 10. Requirement Roll-Up

| State | Count | IDs |
|---|---:|---|
| `DEFINABLE` | **24** | `RC-P-01` .. `-07`, `-09` .. `-15`, `-17` .. `-19`, `-24`, `-26`, `-27`, `-29`, `-30`, `-32`, `-33` |
| `DEFINABLE — CONDITIONAL` | **4** | `RC-P-16` (Lane C), `RC-P-23` (`RC-F-05`), `RC-P-28` (`MTI-D-04`), and `RC-P-31` definable-but-not-exercisable |
| `DEFINABLE` partial only | **1** | `RC-P-25` |
| `NOT DEFINABLE` | **3** | `RC-P-08`, `RC-P-20`, `RC-P-21` |
| `HELD` under the COGS Gap | **2** | `RC-P-22`, and the value half of `RC-P-34` |
| **Total requirements** | **34** | |
| **Executable today** | **0** | **No implementation exists** |
| **Proofs produced by this session** | **0** | |

---

## 11. The `HOLD` Condition, Restated

AAS+ advice `27` §6: *"If a downstream package cannot produce proof for this control, AAS+ must keep the relevant item in HOLD."*

**No package in this chain has produced proof for this control. Every item governed by it therefore remains `HOLD`.** This file makes the proofs writable. It does not make them true.

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
