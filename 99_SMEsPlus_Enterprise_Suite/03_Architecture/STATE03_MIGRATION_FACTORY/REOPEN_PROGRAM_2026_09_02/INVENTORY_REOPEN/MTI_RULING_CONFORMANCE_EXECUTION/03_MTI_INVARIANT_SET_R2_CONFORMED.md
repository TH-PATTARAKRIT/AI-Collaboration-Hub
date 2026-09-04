# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 03 — Inventory MTI Invariant Set R2 — Conformed To `MTI-D-01` / `MTI-D-02` / `MTI-D-03`

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `50 CARRIED + 8 ADDED = 58 INVARIANTS SPECIFIED — 0 PROVEN — 14 RE-SPECIFIED — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. What This File Is And Is Not

**Is:** the Inventory multi-tenant invariant set brought into conformance with the three Boss rulings. It is a **new document in a new folder**. `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md` on `design/inventory-multitenant-invariant-set-2026-09-04-001` @ `dcb9227` is **not edited**, and this session created, modified or deleted **no file outside this output folder**.

**Is not:** a proof, an implementation, a schema, a data model, a minimised set, or a claim that anything conforms to it. **No invariant here carries a status of proven, verified, satisfied or accepted, and none may be recorded as such on the basis of this file.**

### 1.1 The transcription rule this file follows

**Invariants whose text is unchanged are carried by reference and are deliberately not restated.**

The published text at `dcb9227` remains authoritative for all 36 unchanged invariants. Restating 50 invariants in a second document would create a second text that can drift from the first, and the programme has repeatedly found that a restatement is where a correction gets lost. This file therefore states:

- for **every** one of the 50 invariants, its R2 status and whether it changed;
- **in full**, only the 14 invariants whose text the rulings change, and the 8 the rulings require to be added.

Where this file and the published set disagree on a changed invariant, **this file governs**, because it is derived from Boss rulings and the published set predates them. Where they agree, the published set is the text.

### 1.2 Topology scope — `CF-I-08` applied to this whole file

**Every invariant below is scoped to the `SHARED SaaS POOL` topology.** None may be asserted to hold, transfer or fail inside a Private Company operating model. `RC-F-07` records that all 50 invariants, 35 matrix rows, 8 L9 proofs and 30 `MTP-*` scenarios were written for one topology and that none states what changes inside a second. **Stating the scope does not supply the delta and does not reduce `RC-F-07`.** It prevents the more damaging failure: a property established in the pool being cited as evidence about a topology it was never established in.

---

## 2. Vocabulary — R2

### 2.1 The two tuples

```
CTX  = (tenant, company, warehouse?, location?)          the record context — WHERE A FACT BELONGS
AUTH = (tenant, company, warehouse, operation type)      the authorization context — WHAT AN ACTOR MAY DO
```

`tenant` and `company` are the **context spine** and are never optional. `warehouse` and `location` are `CTX`'s **situational axes**, present or absent by the object's nature and never by configuration. `warehouse` and `operation type` are `AUTH`'s **operational axes** and are mandatory wherever the acted-on object carries them.

The two tuples are different shapes, neither substitutes for the other, and **both must be evidenced separately**. Full model, including the six relationship rules and the deferred-execution semantics, at `04`.

### 2.2 Enforcement layers

`STORE` · `PLATFORM` · `DOMAIN` · `CONTROL` · `GOVERNANCE` — carried unchanged from `03` §2.2 at `dcb9227`. `STORE` continues to mean *enforced beneath application code, such that no application code path — including privileged, system, background, administrative and migration paths — can produce a violating record*, with the mechanism unprescribed.

### 2.3 Status vocabulary — R2

| Status | Meaning |
|---|---|
| `SPECIFIED` | Statement and acceptance criteria complete; nothing upstream blocks the specification |
| `SPECIFIED — CONDITIONAL` | Complete in form; scope or content conditioned on a named ruling or input, cited |
| `SPECIFIED — VALUE HELD` | Context half complete; valuation half carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `SPECIFIED — RANK 2 / RANK 3 DEPENDENT` | Complete as to context; not exercisable until the movement attempt identity (`RISK-C02`) or the provenance reference (`GAP-FS-08`) exists. Neither is designed here |

### 2.4 R2 change vocabulary

| Marker | Meaning |
|---|---|
| **`R2-CHANGED`** | The invariant's text changes. Full re-specified text given below |
| **`R2-RESOLVED`** | Status only: a named conditionality is discharged by a ruling. The text is unchanged |
| **`R2-CARRIED`** | Unchanged in text and status. Carried by reference to `dcb9227` |
| **`R2-REINFORCED`** | Unchanged in text; a ruling states the same principle from another direction. **Not a strengthening of evidence** |

---

## 3. Family A — Context Spine (`MTI-01` .. `MTI-06`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-01` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Every record resolves to exactly one `CTX` with `tenant` and `company` present |
| `MTI-02` | `R2-CARRIED` | `SPECIFIED` | Unchanged. The tenant boundary is untouched by every ruling |
| `MTI-03` | `R2-CARRIED` | `SPECIFIED` | Unchanged in text. Its register — `MTI-22` — falls to three entries, `CD-06` |
| `MTI-04` | `R2-REINFORCED` | `SPECIFIED` | Unchanged. **`MTI-D-03` makes it load-bearing in a new place**: every tenant-configurable record is an Inventory record, so `MTI-04` admits no company-less configuration record either. That composition is `CD-16` and is stated explicitly at `CF-I-07` |
| `MTI-05` | `R2-CARRIED` | `SPECIFIED` | Unchanged. `CD-04` and `CD-12` remove the only two matrix rows that declared a two-part anchor, which were in tension with *"exactly one context anchor"*. **Recorded as an observation, not a finding** — the two-part notation described a definitional half and a company half, and the ambiguity is removed as a side effect of conformance rather than corrected as a defect |
| `MTI-06` | `R2-CARRIED` | `SPECIFIED — RANK 3 DEPENDENT` | Unchanged, and it is the reason the anchor changes at `CD-01`, `CD-04`, `CD-12`, `CD-13` and `CD-14` must land before any build. A spine is immutable once a record has participated in a completed act; building to the wrong anchor is not correctable afterwards by any act short of migration, and migration needs `GAP-FS-08`, which does not exist |

---

## 4. Family B — Object Anchors (`MTI-07` .. `MTI-16`)

| ID | Object | R2 Marker | R2 Status | Note |
|---|---|---|---|---|
| `MTI-07` | Warehouse (`CN-02`) | `R2-CARRIED` | `SPECIFIED` — `TH-HOLD-06` held | Unchanged. **A warehouse is never equated with a Thai tax branch, and `MTI-D-02` does not disturb that**: an authorization axis is an operational concept; a tax branch is a statutory one. No Thai statutory claim is made |
| `MTI-08` | Location (`CN-03`) | `R2-CARRIED` | `SPECIFIED` | Unchanged. Whether `location` is *also* an authorization axis is `RC-D-01`, **unruled**. Design proceeds on the three ruled dimensions; the residual is registered, not assumed away in either direction |
| `MTI-09` | Operation type (`CN-04`) | **`R2-CHANGED`** | `SPECIFIED` — numbering convention `TH-HOLD-09` held | Becomes an authorization axis as well as an anchor. Text at §12.1 |
| `MTI-10` | Route and rule (`CN-05`) | `R2-CARRIED` | `SPECIFIED` | Unchanged. Remains the one place in the set where a reference behaviour is the target rather than the divergence, and it is carried as an existing invariant, not newly adopted |
| `MTI-11` | Product and variant (`CN-11`, `CN-12`) | **`R2-CHANGED`** | `SPECIFIED` | Anchor moves to `company`; the enablement clause is void. Text at §12.2. Full treatment at `06` |
| `MTI-12` | Lot and serial (`CN-17`, `CN-18`) | `R2-REINFORCED` | `SPECIFIED` | Unchanged. `MTI-D-01` rule 2 states for product code, name, barcode and UoM the same principle `MTI-F-01` states for traceable values: **the bare value is never the identity**. The two now share one governing rationale. `R4-F-06` remains open |
| `MTI-13` | Package / handling unit (`CN-19`) | `R2-CARRIED` | `SPECIFIED` | Unchanged. `MTI-D-06` — whether a handling unit may ever carry two companies' goods — is a Thai panel question and **no AI may answer it**. `GAP-FS-05` migration disposition open |
| `MTI-14` | Reordering rule (`CN-20`) | `R2-CARRIED` | `SPECIFIED` | Unchanged, and **it still does not resolve `R4-F-11`**. The within-company nested overlap is untouched by every ruling. Stated here because it is the most likely misreading in the set and the published package states it four times for that reason |
| `MTI-15` | Movement document and fact (`CN-24`, `CN-25`) | `R2-CARRIED` | `SPECIFIED — RANK 2 DEPENDENT` | Unchanged. The attempt component of the fact's identity is `RISK-C02` and is not designed here |
| `MTI-16` | Balance, reservation, valuation fact and every derived state | `R2-CARRIED` | `SPECIFIED — VALUE HELD` | Unchanged, **and correct under either option** — costing and valuation attachment was already company-scoped. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`. The owner dimension remains orthogonal to company (`MTI-F-02`, `GAP-MD-09` open) |

---

## 5. Family C — Enforcement (`MTI-17` .. `MTI-22`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-17` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Whether `STORE` enforcement is achievable in a chosen technology is `MTI-CH-01`, **a Team B question not approached by any session in this chain, including this one** |
| `MTI-18` | `R2-CARRIED` | `SPECIFIED` | Unchanged, and **still unverifiable**: the privileged-bypass path audit was started and never completed, so the path set is not enumerated. `RC-P-08` is `NOT DEFINABLE` for the same reason |
| `MTI-19` | `R2-CHANGED` | `SPECIFIED` | Text unchanged; **an explicit scope statement is added** so that it is not read as covering authorization. It is the *context* conformance control. The authorization analogue is `CF-I-03`. Text at §12.3 |
| `MTI-20` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Fail closed; context never defaulted, inferred or inherited from a session fallback |
| `MTI-21` | **`R2-CHANGED`** | `SPECIFIED` | The scoping set becomes the four-axis `AUTH` set. Text at §12.4 |
| `MTI-22` | **`R2-CHANGED`** | `SPECIFIED — CONDITIONAL (JT-10, GAP-FS-07)` | The register falls from four entries to **three**, and each surviving entry acquires an `AUTH` statement. Text at §12.5; register at `05` |

---

## 6. Family D — Visibility And Derivation (`MTI-23` .. `MTI-28`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-23` | `R2-CARRIED` | `SPECIFIED — VALUE HELD` | Unchanged. Derived values carry the `CTX` of their inputs |
| `MTI-24` | `R2-REINFORCED` | `SPECIFIED` | Unchanged. `MTI-D-02` rule 7 restates the requirement for reports, valuation views, replenishment views and movement history. `R4-F-22` remains open — **only implementation and verification close it** |
| `MTI-25` | `R2-CARRIED` | `SPECIFIED — CONDITIONAL (MTI-D-04)` | Unchanged and **still conditional**. `MTI-D-04` is unruled, and `RC-F-04` records that `MTI-D-01` rules 5 and 8 presuppose exactly this mechanism. **`AAS-V-03` in force: no grant may carry valuation content while the COGS Gap stands** |
| `MTI-26` | **`R2-CHANGED`** | `SPECIFIED` | *"The same scope as the record store"* is made explicit as the four-axis `AUTH` set, for the same reason as `MTI-21`. Text at §12.6 |
| `MTI-27` | `R2-CARRIED` | `SPECIFIED` | Unchanged in text. **`MTI-F-03`'s surface is larger than when it was raised**: per-company uniqueness is now the ruled norm for products as well as traceable identities. **Not re-scored here** — that is the owning body's act. Channel list at `06` §7 |
| `MTI-28` | `R2-CARRIED` | `SPECIFIED` | Unchanged. A report's `CTX` scope is part of its identity. `CF-I-08` adds that the **topology** is part of a proof's scope, which is the same principle applied one level up |

---

## 7. Family E — Execution Boundary (`MTI-29` .. `MTI-33`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-29` | **`R2-CHANGED`** | `SPECIFIED` | Single-context execution extended to resolve an explicit operation-type context. Text at §12.7. This is half of `RC-F-05` |
| `MTI-30` | **`R2-CHANGED`** | `SPECIFIED` | A deferred run revalidates the **full four-axis `AUTH`** at release, not only the scheduling authority's existence. Text at §12.8. This is the other half of `RC-F-05`, and it is the invariant `L13-MT-01` was opened against |
| `MTI-31` | `R2-CARRIED` | `SPECIFIED — RANK 2 DEPENDENT` | Unchanged. Supplies run scoping and mutual exclusion, **not idempotency identity**. `RISK-C02` open; a retried run remains indistinguishable from a second genuine run |
| `MTI-32` | `R2-CARRIED` | `SPECIFIED` | Unchanged. The input snapshot requirement that `R4-F-14` needs is already stated |
| `MTI-33` | `R2-CHANGED` | `SPECIFIED — VALUE HELD` | Text unchanged; **scope made explicit** — the context-independence requirement it places on reason classification is the governing precedent for `CF-I-05`, which places the same requirement on operation-type classification. Text at §12.9. Reason taxonomy is `R4-Q-01`, Thai panel, **unanswered** |

---

## 8. Family F — Configuration And Template (`MTI-34` .. `MTI-37`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-34` | **`R2-CHANGED`** | `SPECIFIED` | The company anchor on tenant configuration is made explicit rather than left to compose from `MTI-04` eleven rows away. Text at §12.10 |
| `MTI-35` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Copy at provisioning; a template change never mutates instantiated configuration. **The `SAAS-04` regeneration half of `GAP-MD-14` is untouched by every ruling** |
| `MTI-36` | `R2-CARRIED` | `SPECIFIED` | Unchanged, and it is what bounds `MTI-D-03` rule 5's *"reversible where applicable"*. **Reversion is a forward act**: a new version whose content matches an older one, never the older one restored |
| `MTI-37` | `R2-RESOLVED` | `SPECIFIED — CONDITIONAL (GAP-MD-14)` | The `MTI-D-03` half of the conditionality is discharged. **`GAP-MD-14`'s switch-off-guard and versioning halves are not** |

---

## 9. Family G — Identity, Event, Audit And Replay (`MTI-38` .. `MTI-42`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-38` | **`R2-CHANGED`** | `SPECIFIED` | The event carries the full four-axis `AUTH` as a resolved tuple, not an authority reference alone. Text at §12.11 |
| `MTI-39` | `R2-CARRIED` | `SPECIFIED` | Unchanged. An event's `CTX` is immutable; a correction is a new linked event |
| `MTI-40` | `R2-CHANGED` | `SPECIFIED` | The enumerated anchor changes lose *"a product's company enablement"*, which `CD-02` voids, and gain the configuration anchors `CD-12` .. `CD-14` create. Text at §12.12 |
| `MTI-41` | `R2-CARRIED` | `SPECIFIED — RANK 2 DEPENDENT` | Unchanged, and **still a property that would be satisfied by a broken system**: a replay without an attempt identity produces duplicates whose context is individually correct and collectively wrong, and `MTI-19` would report no breach. `RC-P-31` states this exactly |
| `MTI-42` | `R2-CARRIED` | `SPECIFIED — RANK 3 DEPENDENT` | Unchanged, **and now carrying more**: `CD-09` makes deliberate duplicate preservation a migration requirement, and `MTI-42` prohibits the wrong act without being able to evidence the right one. That evidence is `GAP-FS-08`, which does not exist |

`MTI-40` is counted among the 14 changed invariants because its enumerated list of anchor changes is normative, not illustrative.

---

## 10. Family H — Handoff And Reporting Carriage (`MTI-43` .. `MTI-46`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-43` | **`R2-CHANGED`** | `SPECIFIED` | The attestation covers **both** tuples. Text at §12.13. **`AAS-V-01` in force — element 10 is `specified, not built, not verified`** |
| `MTI-44` | `R2-CARRIED` | `SPECIFIED — CONDITIONAL (JT-10, GAP-FS-07)` | Unchanged in text, **harder in content** under `CD-11`: the correlation is carried entirely by the relationship and may never be reconstructed from product attributes |
| `MTI-45` | **`R2-CHANGED`** | `SPECIFIED` | **Eight** consuming modules, Payment added. Text at §12.14. Obligations at `07` |
| `MTI-46` | `R2-CARRIED` | `SPECIFIED — VALUE HELD` | Unchanged. Context conservation across handoffs; `RC-11`. **The conserved quantity is now a four-part context** — `MTI-F-06` widened, not re-scored |

---

## 11. Family I — Lifecycle (`MTI-47` .. `MTI-50`)

| ID | R2 Marker | R2 Status | Note |
|---|---|---|---|
| `MTI-47` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Zero inherited operational data at provisioning |
| `MTI-48` | `R2-CARRIED` | `SPECIFIED` | Unchanged. Company deactivation freezes and does not delete |
| `MTI-49` | `R2-CARRIED` | `SPECIFIED — CONDITIONAL (MTI-D-05, GAP-MD-29)` | Unchanged, and **still empty in content**. `GAP-MD-29` has zero coverage anywhere in the evidence chain. **No AI may supply a legal scope, and none is supplied here** |
| `MTI-50` | `R2-CARRIED` | `SPECIFIED` | Unchanged, and it is the invariant `HF-CTX-06` and the new `HF-CTX-11` both reference. A control-run reference is only evidence if the control's own runs are retained and inspectable |

---

## 12. The Fourteen Re-Specified Invariants — Full Text

Each is stated in full so that a downstream reader works from one text and not from a diff.

### 12.1 `MTI-09` — Operation type (`CN-04`)

> Operation type is anchored to warehouse, therefore to company. Document numbering sequences are per `(company, operation type)`, continuous and never reused across contexts. **Operation type is additionally an axis of `AUTH`: an actor authorized for one operation type within a warehouse is not thereby authorized for any other operation type within that warehouse. Visibility of an operation type, and authority to act through it, are separate and are separately granted.**

Owner `Inventory` · Layer `STORE` + `PLATFORM` · `SPECIFIED` · `TH-HOLD-09` held · `CD-21`

### 12.2 `MTI-11` — Product and variant (`CN-11`, `CN-12`)

> **A product is a company-owned business object. Its definitional identity is anchored to `company` within `tenant`, and every operational and financial attachment is anchored to the same `company`.** A variant follows its parent product. **Two records in two companies sharing a code, a name, a barcode, a unit of measure, a category, a route or a description are two different business objects; the similarity never creates shared identity and is never a defect, an anomaly or a cleanup candidate.** Costing and valuation attachment is company-scoped.

Owner `Inventory` · Layer `STORE` + `GOVERNANCE` · `SPECIFIED` · `CD-01`, `CD-02`, `CD-03`

**The company-enablement clause of the published `MTI-11` is void.** Under a company-owned master, ownership is the enablement; an enablement gate would imply a shared master that does not exist.

### 12.3 `MTI-19` — Context conformance control

> A continuous **context** conformance control asserts, for every object type, that stored context equals derived context, that no spine value is absent, and that no relationship crosses a boundary outside the `MTI-22` register. Breach raises; it does not silently repair. **This control asserts properties of `CTX` only. It asserts nothing about `AUTH`, and no report of its result may be read as evidence that any authorization property held.** The authorization analogue is `CF-I-03`.

Owner `Inventory` + `SaaS Foundation` · Layer `CONTROL` · `SPECIFIED` · `CD-28`

### 12.4 `MTI-21` — Deny by default on read

> Every read, search, list, export, aggregate and API projection is scoped to the caller's authorized **`AUTH` set** before evaluation, not filtered after it. **The `AUTH` set is four-axis. A read scoped by company alone returns every warehouse and every operation type within that company and is therefore a leak inside a company, not a compliant read.**

Owner `SaaS Foundation` · Layer `PLATFORM` · `SPECIFIED` · `CD-23`

### 12.5 `MTI-22` — Cross-Context Relationship register

> A closed, enumerated Cross-Context Relationship register is the only permitted means by which anything in one company may reference or affect anything in another. Each entry names the two contexts, the correlation identity, the direction, the permitted effect, the evidence obligation, **and the `AUTH` required to traverse it.** **The register holds three entries: `XCR-01`, `XCR-02`, `XCR-04`. `XCR-03` is eliminated.** A completeness claim over this register is a claim about these three entries and nothing else.

Owner `Inventory` + `Boss` · Layer `STORE` + `GOVERNANCE` · `SPECIFIED — CONDITIONAL (JT-10, GAP-FS-07)` · `CD-06`

### 12.6 `MTI-26` — Identifier-resolving surfaces

> Search, autocomplete, barcode resolution, export, print and every API listing obey the same scope as the record store, **which is the caller's four-axis `AUTH` set**. A surface that resolves an identifier must not resolve one outside that set.

Owner `SaaS Foundation` · Layer `PLATFORM` · `SPECIFIED` · `CD-23`

### 12.7 `MTI-29` — Single-context execution

> Every run, job, scheduler execution and background task resolves exactly one `CTX` **and exactly one operation-type context**, and may read and write only within them. A run that must cover several companies is an enumerated set of single-context executions, each with its own identity and its own result. **Context and operation type are resolved explicitly at scheduling and again at release; neither is defaulted, inherited implicitly, or inferred from the run's own payload.**

Owner `Inventory` + `SaaS Foundation` · Layer `PLATFORM` · `SPECIFIED` · `CD-22`

### 12.8 `MTI-30` — Deferred execution authority

> A deferred or queued execution carries both the `CTX` and the **full four-axis `AUTH`** under which it was scheduled. **At release, the `AUTH` is revalidated in full.** If any axis of it has lapsed, been revoked, narrowed, or its grant expired — the scheduling actor's access removed, the company deactivated, the warehouse grant withdrawn, or the operation-type grant withdrawn — the run does not execute, and the non-execution is recorded as an event.

Owner `SaaS Foundation` · Layer `PLATFORM` + `CONTROL` · `SPECIFIED` · `CD-22` · `L13-MT-01`

### 12.9 `MTI-33` — Single-context acts and context-independent classification

> Adjustment, count, scrap, return, transfer and landed-cost allocation each execute within exactly one `CTX`, and each carries a reason classification that is defined independently of context, so that the same reason means the same thing in every company. **The same context-independence requirement applies to the operation-type classification the act is executed under — see `CF-I-05`.**

Owner `Inventory` · Layer `DOMAIN` + `GOVERNANCE` · `SPECIFIED — VALUE HELD` · reason taxonomy `R4-Q-01`, Thai panel · `CD-31`

### 12.10 `MTI-34` — Template content versus tenant configuration

> Platform-provided template content and tenant-owned configuration are distinct object classes. Template content is versioned, tenant-neutral and never directly transacted against. **Tenant configuration always carries a `CTX`, in which `company` is mandatory and derived from a declared anchor. A company-less configuration record is not created; the act fails.** Every record class named tenant-configurable by `MTI-D-03` §3 belongs to this second class, and duplication of configuration across companies is a legitimate and expected state.

Owner `SaaS Foundation` · Layer `STORE` · `SPECIFIED` · `CD-16` · see `CF-I-07`

### 12.11 `MTI-38` — Event completeness

> Every context-bearing act emits an immutable event carrying the full `CTX`, **the full four-axis `AUTH` relied on as a resolved tuple**, the actor, the authority relied on including any `MTI-18` grant, the **physical event date and the entry date as two distinct values**, and the evidence reference. **The audit trail must answer: who performed what action, in which tenant, in which company, in which warehouse, and under which operation type.**

Owner `Inventory` · Layer `STORE` · `SPECIFIED` · `CD-26`

### 12.12 `MTI-40` — Anchor change auditability

> Any change to a context anchor — a warehouse's company, a location's parent or kind, a route's company, **a product category's company, a barcode nomenclature's company, a unit group's company** — is itself an evented, approved act carrying before and after values. **The published enumeration's reference to a product's company enablement is removed: under `MTI-D-01` no such object exists.**

Owner `Inventory` · Layer `GOVERNANCE` + `STORE` · `SPECIFIED` · `CD-02`, `CD-12`, `CD-13`, `CD-14`

**A product's own company is not in this list, and must not be added to it.** `MTI-06` prohibits reassignment outright; the only permitted path is an approved, evidenced migration act creating new records with provenance linkage, and that provenance is `GAP-FS-08`, which does not exist.

### 12.13 `MTI-43` — Handoff carriage and attestation

> Every emitted handoff fact carries the resolved `CTX`, **the resolved `AUTH`**, and **two attestations** — one naming which invariants guaranteed the context and which control run last asserted them (`HF-CTX-05`, `HF-CTX-06`), and one naming which control run last asserted the authorization conformance property (`HF-CTX-11`). **Element 10 is satisfied by the tuples plus both attestations, never by a tuple alone and never by one attestation alone.**

Owner `Inventory` · Layer `DOMAIN` · `SPECIFIED` · `CD-25`, `CD-27` · `MTI-F-04`

**`AAS-V-01` in force.** Element 10's status is `specified, not built, not verified`, and this invariant does not change it. `HF-CTX-11` references a control that `CF-I-03` requires and that **is not stated by any of the 50 published invariants** — `CF-F-05`, boundary `B-02` at `01` §8, class `A` in that scope and `B` wider — so the attestation is presently a reference to nothing — which is the honest position and is why the status does not move.

### 12.14 `MTI-45` — Consuming module obligation

> **Every consuming module — Accounting, Sale, Purchase, Manufacturing, Approval, Document, Reporting and Payment — receives `CTX` and `AUTH` as mandatory, non-inferable inputs.** A consumer may not derive, default or reconstruct either. A consumer rejects a fact whose context attestation or authorization attestation is absent or failing.

Owner `Inventory` + consuming domains · Layer `DOMAIN` · `SPECIFIED` · `CD-27` · `RC-F-09` · obligations at `07`

---

## 13. The Eight Invariants The Rulings Require To Be Added

`CF-I-*` are **additions to the `MTI-*` family, never replacements**. They are not numbered `MTI-51`+ because folding them into that sequence is a consolidation act belonging to AAS+ and Boss.

| ID | Invariant | Owner | Layer | Status | Source |
|---|---|---|---|---|---|
| **`CF-I-01`** | **`AUTH` is a four-axis tuple `(tenant, company, warehouse, operation type)`, and every `AUTH` is a subset of a single `CTX` spine — never a superset, never a union across companies. Multi-company access is several `AUTH` entries, never one broadened entry. No axis substitutes for a wider one: operation type ⊄ warehouse ⊄ company ⊄ tenant** | SaaS Foundation + Inventory | `PLATFORM` + `STORE` | `SPECIFIED` | `MTI-D-02` rules 4, 5, 6; `04` §7 rule 1 of the published matrix, carried unchanged |
| **`CF-I-02`** | **Every deferred, queued, scheduled or background execution resolves an explicit operation-type context, carried from scheduling to release, and re-resolved against the grant in force at release. An execution whose operation-type context is absent, defaulted or inferred does not execute, and the non-execution is recorded** | Inventory + SaaS Foundation | `PLATFORM` | `SPECIFIED` | `MTI-D-02` rule 8; `RC-F-05`; extends `MTI-29`, `MTI-30` |
| **`CF-I-03`** | **A continuous authorization conformance control asserts, for every recorded act, that the `AUTH` it records was within a grant in force at the time of the act; that no act is recorded with an absent axis where the acted-on object carries that axis; and that no grant spans more than one company. Breach raises; it does not silently repair. Its runs are retained, context-scoped and inspectable, and are what `HF-CTX-11` references** | SaaS Foundation + Inventory | `CONTROL` | `SPECIFIED` | `CF-F-05`; `CD-28`; the `AUTH` analogue of `MTI-19`; `MTI-50` supplies the retention obligation |
| **`CF-I-04`** | **Defining a configuration object and being authorized to act through it are separate grants. Creating an operation type, a warehouse, a route, a rule or any other configurable record confers no authority to act through it, and no authority to act is inferred from the ability to create** | Inventory + SaaS Foundation | `PLATFORM` + `DOMAIN` | `SPECIFIED` | `MTI-D-02` rules 2, 3; `MTI-D-03` rule 4; `RC-P-40`'s acceptance criterion promoted to an invariant |
| **`CF-I-05`** | **Every tenant-configured operation type declares exactly one platform-owned operation class. Platform-level controls, segregation rules and proof scenarios bind to the class and never to the tenant's own label. The class of an operation type is immutable once any completed movement has been executed through it** | Boss + Inventory | `STORE` + `GOVERNANCE` | **`SPECIFIED — CONDITIONAL (CF-D-02)`** | `CF-F-04`; `CD-29`; the `MTI-33` pattern applied to operation types. **The class enumeration's closure is a Boss decision and is stated, never chosen** |
| **`CF-I-06`** | **No correspondence between products, categories, nomenclatures or unit groups in different companies is created, asserted, inferred or relied upon by any process, report, export, migration or maintenance path. Until a controlled mapping / provenance object is specified and authorized, no cross-company correspondence exists, and no surface may present one** | Inventory + Boss | `STORE` + `DOMAIN` | `SPECIFIED` | `MTI-D-01` rules 2, 5, 8; `RC-F-03`. **This is a prohibition in the absence of the object. It is not a specification of the object, and it must not be read as one** |
| **`CF-I-07`** | **Every instance of every tenant-configurable record class carries a mandatory `company`, derived from a declared anchor under `MTI-05` and stored on the record. A company-less configuration record is rejected at `STORE`. Duplicate configuration records across companies within a tenant are a legitimate state and are never reported, flagged or remediated as a defect** | SaaS Foundation + Inventory | `STORE` | `SPECIFIED — CONDITIONAL (RC-D-02)` | `MTI-D-03` §3 with `MTI-04` and `MTI-34`; AAS+ advice `29` §3; `RC-P-36`. **Conditional because the class list is open-ended — `RC-F-06`** |
| **`CF-I-08`** | **Every invariant, matrix row, enforcement point, proof, proof scenario and attack in the Inventory multi-tenant set states the isolation topology it is scoped to. A property established in one topology is not evidence about another. No property established in the shared SaaS pool may be asserted to hold, transfer or fail inside a Private Company operating model** | AAS+ + Inventory | `GOVERNANCE` | `SPECIFIED` | `MTI-D-03` §4; `RC-F-07`; AAS+ advice `29` §7. **This is a scope rule. It supplies no Private Company content and reduces `RC-F-07` by nothing** |

---

## 14. Internal Consistency Of The Conformed Set — `L5`

Tested directly, because a set changed at fourteen points and extended at eight is exactly where a new contradiction would hide.

| Pair | Test | Result |
|---|---|---|
| `MTI-11` R2 × `MTI-12` | Does a company-owned product master conflict with the traceable-identity tuple `(tenant, company, product, value)`? | **No.** The tuple already carried `company`; under R2 the `product` member is company-resolved by construction, so the tuple is over-determined rather than under-determined. `CD-32` records the resulting simplification of handoff element 8 |
| `MTI-11` R2 × `CF-I-07` | May a company-owned product belong to a company-owned category? | **Yes, and both are now anchored the same way.** Under the published set a company-owned attachment referenced a tenant-level category, which was the shared surface `CD-15` removes |
| `CF-I-01` × `MTI-08` | Does a four-axis `AUTH` conflict with `location` being a `CTX` axis? | **No, and the difference is deliberate.** `CTX` says where a record lives; `AUTH` says what an actor may do. `location` anchors records and is **not** ruled an authorization axis. `RC-D-01` is registered, unruled, and design proceeds on the axes ruled |
| `CF-I-02` × `MTI-31` | Does resolving an operation-type context give a run an identity? | **No, and it must not be read as doing so.** `MTI-31` supplies run scoping and mutual exclusion; `RISK-C02` supplies neither. A run with a fully resolved four-axis `AUTH` is still indistinguishable from a retry of itself |
| `CF-I-03` × `MTI-19` | Do two conformance controls overlap or contradict? | **Neither.** They assert disjoint properties over the same acts. `MTI-19` asserts that a record's context is right; `CF-I-03` asserts that the act that produced it was permitted. **`09` §3.2 of the invariant set establishes the general form of this: context conformance and duplicate freedom are independent properties. Context conformance and authorization conformance are a third and fourth independent property, and none implies another** |
| `CF-I-05` × `MTI-D-03` | Does a platform-owned operation class fork the platform core, which the pool forbids? | **No.** The tenant configures its operation types freely and declares a class for each. The **class enumeration** is platform-owned, which is precisely what `MTI-D-03` requires of core logic, and the **instances** are tenant-owned, which is what it permits |
| `CF-I-06` × `MTI-D-01` rule 5 | Does prohibiting correspondence contradict a ruling that requires a mapping layer? | **No.** Rule 5 permits comparison *"only after an explicit authorized mapping exists"*. No such object exists, so the permitted case is empty and the prohibition is the whole of the rule's present effect. `CF-I-06` is void of restriction the moment `RC-F-03` is remedied and `MTI-D-04` is ruled |
| `CF-I-08` × every proof | Does a topology scope statement weaken any proof? | **No. It states what the proof was always true of.** A proof whose scope was unstated was not thereby wider |
| All three rulings × the conformed set | Is any invariant now in conflict with any ruling? | **None found.** Search boundary: all 58 invariants in this file, read against the three ruling files and three AAS+ advice records in full. **Class `A` within that boundary; class `B` for the wider design corpus, which this session did not re-derive** |

---

## 15. Roll-Up

| Measure | Result |
|---|---:|
| Invariants carried from `dcb9227` | **50** |
| Invariants re-specified in text | **14** — `MTI-09`, `-11`, `-19`, `-21`, `-22`, `-26`, `-29`, `-30`, `-33`, `-34`, `-38`, `-40`, `-43`, `-45` |
| Invariants with conditionality resolved, text unchanged | **1** — `MTI-37` |
| Invariants reinforced by a ruling, text unchanged | **3** — `MTI-04`, `MTI-12`, `MTI-24` |
| Invariants carried unchanged | **32** |
| Invariants added | **8** — `CF-I-01` .. `CF-I-08` |
| **Total invariants in the conformed set** | **58** |
| Invariants `SPECIFIED` unconditionally | **41** |
| Invariants `SPECIFIED — CONDITIONAL` | **7** — `MTI-22`, `MTI-25`, `MTI-37`, `MTI-44`, `MTI-49`, `CF-I-05`, `CF-I-07` |
| Invariants `SPECIFIED — VALUE HELD` | **5** — `MTI-16`, `MTI-23`, `MTI-33`, `MTI-46`, and the costing facet of the `MTI-11` category attachment |
| Invariants `SPECIFIED — RANK 2 / RANK 3 DEPENDENT` | **5** — `MTI-06`, `MTI-15`, `MTI-31`, `MTI-41`, `MTI-42` |
| **Invariants proven by this session** | **0** |
| **Invariants verified by this session** | **0** |
| Prior items closed | **0** |
| Carried identifiers renumbered, retired or merged | **0** |

**The set is not minimised.** `MTI-CH-02` records that the published 50 were made complete rather than minimal, and adding eight does not improve that. `MTI-CH-02` is carried unchanged and is not discharged.

---

## 16. Non-Authorization Lock

This file does not declare, and this session is not empowered to declare: `PASS`, `APPROVED`, `CLOSED`, `FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, merge approval, or release authorization.

**`RC-V-01` is not discharged by this file.** The veto's remedy is a re-specification that is then **independently checked**; this file is the first half and an independent check is another body's act. `AAS-V-01`, `AAS-V-02` and `AAS-V-03` are in force and unchanged.

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
