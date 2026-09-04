# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 03 — Inventory Multi-Tenant Invariant Set — Canonical

Control Level: `/L9999.9999`
Status: `50 INVARIANTS SPECIFIED — 0 PROVEN — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. What This File Is

This is the artifact `RISK-U03` / `GAP-FS-10` records as non-existent: a canonical, identified, owned set of multi-tenant invariants for SMEsPlus Inventory.

**An invariant here is a property that must hold at all times, expressed so that a violation is detectable.** It is not a feature, not a requirement statement, and not a design of how it is achieved. Each is written so that a later verification pass can attempt to break it.

**This is a conceptual and architectural specification. It is not a data model, not a schema, and not approved design.** No implementation approach is prescribed, and none is implied by the enforcement-layer column.

---

## 2. Vocabulary Used Throughout The Package

### 2.1 The Context Tuple

`CTX = (tenant, company, warehouse?, location?)`

- `tenant` — the SaaS subscriber. The outermost boundary. Always present.
- `company` — the legal entity within a tenant. Always present on every Inventory record.
- `warehouse` — present where the record is physically situated or operationally owned by a site.
- `location` — present where the record identifies a storage place.

`tenant` and `company` are together the **context spine**. `warehouse` and `location` are the **situational axes**. The spine is never optional. The situational axes are present or absent by the object's nature, never by configuration.

### 2.2 Enforcement layers

| Layer | Meaning |
|---|---|
| `STORE` | Enforced beneath application code, such that **no application code path — including privileged, system, background and administrative paths — can produce a violating record**. The mechanism is not prescribed here |
| `PLATFORM` | Enforced by the SaaS foundation runtime that resolves and carries context |
| `DOMAIN` | Enforced by Inventory domain logic at a named function boundary |
| `CONTROL` | A continuous or periodic check that asserts the property and raises on breach. A control **detects**; it never substitutes for `STORE` |
| `GOVERNANCE` | Enforced by an approved, evidenced human act |

`STORE` is named deliberately. Prior evidence records company scoping enforced at the application layer with **no database-layer backstop** and an unfinished privileged-bypass audit (`10` §3). An invariant enforced only at `DOMAIN` is, on that evidence, an assertion rather than a guarantee.

### 2.3 Status vocabulary

| Status | Meaning |
|---|---|
| `SPECIFIED` | Statement and acceptance criteria complete; nothing upstream blocks the specification |
| `SPECIFIED — CONDITIONAL` | Statement complete, but its scope or content is conditioned on a named ruling or input, which is cited |
| `SPECIFIED — VALUE HELD` | The context half is complete; the valuation half carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `SPECIFIED — RANK 2/3 DEPENDENT` | Complete as to context, but cannot be fully exercised until the movement attempt identity (`RISK-C02`) or the provenance reference (`GAP-FS-08`) exists. Neither is designed here |

**No invariant in this file carries a status of proven, verified, satisfied or accepted, and none may be recorded as such on the basis of this file.**

---

## 3. Family A — Context Spine (`MTI-01` .. `MTI-06`)

The six invariants everything else rests on.

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-01` | Every Inventory record, computed value, event, job and emitted fact resolves to exactly one `CTX`, in which `tenant` and `company` are present | SaaS Foundation + Inventory | `STORE` | `SPECIFIED` |
| `MTI-02` | No Inventory record, computation, event, job, report, export or handoff may read, write, reference, aggregate or be influenced by anything resolving to a different `tenant`, under any code path | SaaS Foundation | `STORE` | `SPECIFIED` |
| `MTI-03` | `company` is a closed boundary within a tenant. Cross-company effect occurs only through a Cross-Context Relationship declared in the register at `MTI-22`, and never implicitly | Inventory + SaaS Foundation | `STORE` + `DOMAIN` | `SPECIFIED` |
| `MTI-04` | **No null context.** `tenant` and `company` are non-optional on every Inventory record without exception. A record whose company cannot be resolved is not created; the act fails | Inventory + SaaS Foundation | `STORE` | `SPECIFIED` |
| `MTI-05` | Each object type declares exactly one **context anchor** — the single authoritative ancestor from which its company is derived. The derived value is stored on the record, and a `CONTROL` continuously asserts stored equals derived | Inventory | `STORE` + `CONTROL` | `SPECIFIED` |
| `MTI-06` | A record's `tenant` and `company` are **immutable** once the record has participated in any completed movement, valuation, handoff or report. Reassignment is prohibited. The only permitted path is an approved, evidenced migration act creating new records with provenance linkage | Inventory | `STORE` + `GOVERNANCE` | `SPECIFIED — RANK 3 DEPENDENT` |

### 3.1 Why `MTI-04` is stated as an absolute

`MTI-04` is the direct answer to `R4-F-09` and `R4-F-06`. Both findings describe the same shape: a record type whose company scope **may legitimately be absent**, with the resulting collisions handled reactively. R4's assessment — that these are structural and cannot be closed by configuring correctly — is adopted.

The design position is that optionality of the context spine is not a configuration choice that SMEsPlus may offer. It is the property whose absence makes handoff element 10 unsuppliable. `MTI-04` therefore admits **no** exception, including for platform-provided template content, which is handled instead by `MTI-34` and `MTI-35` as a separate object class rather than as a company-less Inventory record.

**This does not close `R4-F-09` or `R4-F-06`.** It states the required divergence. Both findings remain open, and closure requires implementation and independent verification.

### 3.2 Why `MTI-05` requires storage rather than read-time derivation

If a location's company is computed from its warehouse at read time, then a query that does not traverse to the warehouse — an export, an aggregate, a background job, a report — evaluates without the boundary. Storing the derived value puts the boundary on the record itself; the `CONTROL` is what stops the stored value drifting from the anchor. Both halves are required; neither alone is sufficient.

---

## 4. Family B — Object Anchors (`MTI-07` .. `MTI-16`)

`MTI-05` requires each object type to declare its anchor. This family declares them. The object identifiers `CN-*` are carried unchanged from the v1.0 concept model via `15_OBJECT_IMPACT_MATRIX.md`.

| ID | Object | Context Anchor And Rule | Owner | Layer | Status |
|---|---|---|---|---|---|
| `MTI-07` | Warehouse (`CN-02`) | Anchored to `company`. Company immutable after the first completed movement in the warehouse. A warehouse is **never** equated with a Thai tax branch | Inventory | `STORE` | `SPECIFIED` — statutory branch treatment `TH-HOLD-06` held |
| `MTI-08` | Location / storage place (`CN-03`) | Anchored to its **warehouse**; company derived from it and mandatory. A location's parent must resolve to the same company. Location *kind* carries financial meaning and is versioned; a kind change is an approved act and never re-interprets completed movements | Inventory | `STORE` + `GOVERNANCE` | `SPECIFIED` — closes the shape of `R4-F-09`, does not close the finding |
| `MTI-09` | Operation type (`CN-04`) | Anchored to warehouse, therefore to company. Document numbering sequences are per `(company, operation type)`, continuous and never reused across contexts | Inventory | `STORE` | `SPECIFIED` — numbering convention `TH-HOLD-09` held |
| `MTI-10` | Route and rule (`CN-05`) | Anchored to `company`. **Route-to-rule company consistency is adopted as an invariant** — a rule may not belong to a company other than its route's. Extended here to route *version*: a generated operation resolves to the route version in force at generation time | Inventory | `STORE` | `SPECIFIED` — positive transfer, see §4.1 |
| `MTI-11` | Product and variant (`CN-11`, `CN-12`) | **Definitional identity anchored to `tenant`; every operational and financial attachment anchored to `company`.** A company may transact a product only where an explicit company enablement exists. Costing and valuation attachment is company-scoped | Inventory + Boss | `STORE` + `GOVERNANCE` | `SPECIFIED — CONDITIONAL (`MTI-D-01`)` — see §4.2 |
| `MTI-12` | Lot and serial (`CN-17`, `CN-18`) | Identity tuple is `(tenant, company, product, value)`. **Company-less traceable identity is prohibited.** Uniqueness enforced per company. Identical values in two companies are legitimate distinct identities and must **never** be presented, exported or handed off as a bare value — always as the resolved tuple | Inventory + SaaS Foundation | `STORE` | `SPECIFIED` — see §4.3 |
| `MTI-13` | Package / handling unit (`CN-19`) | Anchored to `company`. A handling unit may never contain goods resolving to more than one company. Historical content snapshots carry the `CTX` in force at the time of the snapshot | Inventory | `STORE` | `SPECIFIED` — migration disposition `GAP-FS-05` open |
| `MTI-14` | Reordering rule (`CN-20`) | Anchored to `company` and to the location it acts on, which must resolve to the same company. A rule may propose supply only within its own `CTX` | Inventory | `STORE` + `DOMAIN` | `SPECIFIED` — does not resolve `R4-F-11`, see §4.4 |
| `MTI-15` | Movement document (`CN-24`) and movement fact (`CN-25`) | Anchored to `company` via operation type. A single movement fact resolves to exactly one company. Source and destination locations must resolve to the same company; a movement between companies is not one fact — see `MTI-44` | Inventory | `STORE` | `SPECIFIED — RANK 2 DEPENDENT` — the attempt component of the fact's identity is `RISK-C02`, not designed here |
| `MTI-16` | Balance (`CN-26`), reservation (`CN-23`), valuation fact (`CN-31`), and every other derived state | Anchored to the `CTX` of the facts they derive from, which must be a single `CTX`. **The owner dimension on a balance is orthogonal to `company` and must never be conflated with it** | Inventory | `STORE` + `CONTROL` | `SPECIFIED — VALUE HELD` — see §4.5 |

### 4.1 `MTI-10` is a positive transfer, recorded as such

`L2-OBS` records that route-to-rule company consistency **is** genuinely enforced in the reference pattern — a route belonging to one company with a rule belonging to another is rejected. R4 and the review both record this as a real strength worth transferring. It is adopted here as an invariant rather than re-derived, and it is the only place in this set where the reference behaviour is the target rather than the divergence. Versioning, by contrast, is **not** a reference behaviour and remains a required divergence (`IV-15`).

### 4.2 `MTI-11` carries a design position that Boss must confirm — `MTI-D-01`

The tenant-level definitional identity with company-level attachment is a **design position taken by this session**, not a carried decision. It is stated because the authorization requires product and variant visibility to be defined, and because the alternative — a company-owned product master — has a material consequence.

| Option | Consequence |
|---|---|
| **A — tenant-level definitional identity, company-level attachment** (position taken) | One product means one thing across a tenant's companies; inter-company transfer and group reporting are expressible; costing method remains company-scoped, which the reference evidence confirms is the correct shape. Cost: the tenant-level master becomes a shared surface that must itself be isolation-proven, and template-versus-tenant questions apply to it |
| **B — company-owned product master** | Maximum isolation, and no shared surface to prove. Cost: the same physical item exists as several unrelated identities within one tenant; inter-company transfer loses its natural correlation; Thai SME groups that operate several companies over one catalogue would maintain duplicate masters, which the L8 evidence names as a live source of identity failure |

The position taken is A. **It is recorded as decision blocker `MTI-D-01` and requires Boss confirmation before it is relied upon.** This session does not treat it as settled. The dual ownership of the product category (`R4-F-10` — reporting, put-away and costing facets in one concept) means the category's costing facet must be company-scoped whichever option is chosen; the split of the category itself is `GAP-FS-02`, precondition-blocked on `JT-01`, which is **NOT DECIDABLE**, and is not touched here.

### 4.3 `MTI-12` replaces detection with prevention, and adds non-confusability

`R4-F-06` records reactive cross-company duplicate detection. `MTI-12` requires prevention of the company-less case, which removes the class of collision that detection existed to catch.

It then adds a requirement no prior round states: **identical batch values across two companies are legitimate**, because two companies may buy from the same supplier who reuses batch codes. Prohibiting that would be wrong. What must be prohibited is *presenting or transmitting the bare value as if it were the identity* — in a report, an export, a scan result, or a handoff payload. The identity is the tuple; the value is an attribute of it. This is the same principle the L8 governing rule applies to product codes and names, applied to traceable identities.

Recorded as a new finding: `MTI-F-01`.

### 4.4 `MTI-14` is necessary and not sufficient — stated explicitly

`R4-F-11` records that two reordering rules on nested locations are both permitted and both active, so each can raise supply for the same shortfall. `MTI-14` closes only the cross-company half of that: a rule may not act on a location in another company.

**Within a single company the overlap remains, and `MTI-14` does not address it.** Hierarchy-aware uniqueness within a context is an Inventory design item carried at `R4-F-11`, Lane A, and is out of this authorization's scope. This is recorded here so that a downstream reader does not read `MTI-14` as closing `R4-F-11`. It does not.

### 4.5 `MTI-16` — the owner dimension is not the company dimension

`L5-07` records two orthogonal questions: *where* goods are, and *whose* they are. Consignment stock sits at our location but is not ours; goods at a customer site on approval may be ours but not at our location. The v1.0 concept model already carries an owner dimension on the balance (`CN-26`).

The failure mode is bidirectional and easy to create: treating `owner` as if it were `company` makes consignment stock look like another company's stock and hides it from the company that is accountable for it; treating `company` as if it were `owner` makes third-party goods look like a company asset. `MTI-16` prohibits the conflation. **What may be valued as whose asset is `GAP-MD-09`, open, and its valuation consequence carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.** This session states the separation and decides no policy.

Recorded as a new finding: `MTI-F-02`.

---

## 5. Family C — Enforcement (`MTI-17` .. `MTI-22`)

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-17` | Every Family A and Family B invariant is enforced at `STORE`, such that no application code path — privileged, system, background, administrative or migration — can produce a violating record. `DOMAIN` enforcement is additional, never substitutional | SaaS Foundation | `STORE` | `SPECIFIED` |
| `MTI-18` | **No unaudited privileged bypass exists.** Where elevation across a context boundary is legitimate, it is a named grant carrying grantor, grantee, reason, scope, expiry and a permanent record. A global, unscoped, unlogged bypass is prohibited | Boss + SaaS Foundation | `STORE` + `GOVERNANCE` | `SPECIFIED` — see §5.1 |
| `MTI-19` | A continuous **context conformance control** asserts, for every object type, that stored context equals derived context, that no spine value is absent, and that no relationship crosses a boundary outside the `MTI-22` register. Breach raises; it does not silently repair | Inventory + SaaS Foundation | `CONTROL` | `SPECIFIED` |
| `MTI-20` | **Fail closed.** Where context cannot be resolved, the act fails and is recorded as a failure. Context is never defaulted, never inferred from a name or code, and never inherited from a session fallback | SaaS Foundation | `STORE` + `PLATFORM` | `SPECIFIED` |
| `MTI-21` | **Deny by default on read.** Every read, search, list, export, aggregate and API projection is scoped to the caller's authorized `CTX` set before evaluation, not filtered after it | SaaS Foundation | `PLATFORM` | `SPECIFIED` |
| `MTI-22` | A closed, enumerated **Cross-Context Relationship register** is the only permitted means by which anything in one company may reference or affect anything in another. Each entry names the two contexts, the correlation identity, the direction, the permitted effect and the evidence obligation | Inventory + Boss | `STORE` + `GOVERNANCE` | `SPECIFIED — CONDITIONAL (`JT-10`, `GAP-FS-07`)` — see §5.2 |

### 5.1 `MTI-18` and the audit that was never completed

`L9-01` records an audit of privileged bypass paths that was **started and never finished**. `MTI-18` states the target property. It does not supply the audit, and the audit is not in this authorization's scope.

The consequence must be stated plainly: **`MTI-18` is unverifiable until that audit is completed**, because the set of privileged paths is not enumerated. This is carried as a dependency at `11`, not as a defect of the invariant.

The prohibition on a global unaudited bypass is not new reasoning. The v1.0 design already rejected exactly such a bypass for the period guard, on the ground that it is unauditable (`L6-15`, `G-2`). `MTI-18` applies the same settled position to the context boundary.

### 5.2 `MTI-22` is the only door, and it is currently empty

Isolation designs fail in practice not because the wall is weak but because the doors are undocumented. `MTI-22` requires that every legitimate cross-company path be enumerated in one register, so that the isolation claim is a claim about a finite, inspectable list rather than about the absence of paths.

The register's **content** cannot be completed by this session. The principal entry it would carry — inter-company transfer treated as a paired sale and purchase (`HO-22`) — sits on a path that `GAP-FS-07` records as **never traced end to end**, and whose treatment is `JT-10`, open. The register is therefore specified as a structure and instantiated with the entries this session can justify, with `JT-10` named. See `06` §5.

---

## 6. Family D — Visibility And Derivation (`MTI-23` .. `MTI-28`)

This family exists because of `R4-F-22`, and it is the part of the invariant set that no earlier round stated.

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-23` | Every derived value — balance, availability, forecast, valuation position, analytic measure — carries the `CTX` of the facts it derives from, and that `CTX` is part of the derived value's identity | Inventory | `DOMAIN` + `CONTROL` | `SPECIFIED — VALUE HELD` |
| `MTI-24` | **No computation may aggregate across a context boundary** except under a Cross-Context Report Grant (`MTI-25`). This applies to sums, counts, averages, forecasts, rankings, alerts and any measure derived from more than one record | Inventory + SaaS Foundation | `DOMAIN` + `CONTROL` | `SPECIFIED` |
| `MTI-25` | A Cross-Context Report Grant is named, granted by an identified authority, scoped to an enumerated company set within **one tenant**, time-bounded, logged on every use, and **never** crosses a tenant boundary under any circumstance | Boss + SaaS Foundation | `PLATFORM` + `GOVERNANCE` | `SPECIFIED — CONDITIONAL (`MTI-D-04`)` |
| `MTI-26` | Search, autocomplete, barcode resolution, export, print and every API listing obey the same scope as the record store. A surface that resolves an identifier must not resolve one outside the caller's `CTX` set | SaaS Foundation | `PLATFORM` | `SPECIFIED` |
| `MTI-27` | **Absence must not leak existence.** A caller outside a record's `CTX` receives the same response as for a record that does not exist. Uniqueness feedback, suggestion, error text and identifier-collision messages must not disclose that a value is in use in another context | SaaS Foundation | `PLATFORM` | `SPECIFIED` — see §6.1 |
| `MTI-28` | Every report states the `CTX` scope it was produced under, and that scope is part of the report's identity. Two reports over different scopes are different reports and must not be compared as one | Inventory | `DOMAIN` | `SPECIFIED` |

### 6.1 `MTI-27` — the leak that survives a correct record store

`MTI-27` is included because `MTI-12` creates the condition for it. Once traceable identity uniqueness is enforced per company, a user in company A who enters a batch value already used in company B must receive a response that does not reveal it. A naive uniqueness message discloses the existence, and often the identity, of a record in another company — from a screen where every stored record is correctly scoped.

The same class applies to product codes, location barcodes, document numbers and serial values. Recorded as a new finding: `MTI-F-03`.

---

## 7. Family E — Execution Boundary (`MTI-29` .. `MTI-33`)

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-29` | **Single-context execution.** Every run, job, scheduler execution and background task resolves exactly one `CTX` and may read and write only within it. A run that must cover several companies is an enumerated set of single-context executions, each with its own identity and its own result | Inventory + SaaS Foundation | `PLATFORM` | `SPECIFIED` |
| `MTI-30` | A deferred or queued execution carries both the `CTX` and the **authority** under which it was scheduled. If that authority has lapsed, been revoked, or its grant expired before the run executes, the run does not execute and the non-execution is recorded | SaaS Foundation | `PLATFORM` + `CONTROL` | `SPECIFIED` — see §7.1 |
| `MTI-31` | A run has an identity scoped to its `CTX`, and two runs with the same identity may not execute concurrently within that `CTX` | Inventory | `PLATFORM` | `SPECIFIED — RANK 2 DEPENDENT` — see §7.2 |
| `MTI-32` | Replenishment and scheduling read only facts within their own `CTX`, and a proposal they emit carries that `CTX` and the input snapshot the run evaluated | Inventory | `DOMAIN` | `SPECIFIED` |
| `MTI-33` | Adjustment, count, scrap, return, transfer and landed-cost allocation each execute within exactly one `CTX`, and each carries a reason classification that is defined independently of context, so that the same reason means the same thing in every company | Inventory | `DOMAIN` + `GOVERNANCE` | `SPECIFIED — VALUE HELD` — reason taxonomy is `R4-Q-01`, Thai panel |

### 7.1 `MTI-30` — an execution boundary that L1-L12 does not reach

The enforcement points at L3 are synchronous function boundaries with a caller present. A queued run has no synchronous caller: it executes later, potentially after the scheduling user's access to that company has been removed, after the company has been deactivated, or after a `MTI-18` grant has expired. Nothing in the published evidence addresses this case.

`MTI-30` states the property. It is one of the triggers for the L13+ escalation recorded at `12` §6.

### 7.2 `MTI-31` is the context half of a two-part problem, and only the context half

`L6-10` records that nothing prevents an overlapping scheduler run, that there is no run-level mutual exclusion, and that there is no idempotency identity on what a run produces. `MTI-31` supplies the scoping and the mutual-exclusion requirement.

**It does not supply the idempotency identity.** That is `RISK-C02` / `IV-06`, rank 2 of `04` §4, whose severity is a live Boss ruling (`C-02`) and which is **not in this authorization**. Without it, a run that is interrupted and retried still cannot be distinguished from a second genuine run. `MTI-31` narrows the exposure; it does not remove it, and must not be reported as doing so.

---

## 8. Family F — Configuration And Template (`MTI-34` .. `MTI-37`)

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-34` | Platform-provided template content and tenant-owned configuration are **distinct object classes**. Template content is versioned, tenant-neutral and never directly transacted against; tenant configuration always carries a `CTX` | SaaS Foundation | `STORE` | `SPECIFIED` |
| `MTI-35` | Tenant configuration is created by **copy at provisioning time**, recording the template version copied. A later change to the template **never** mutates configuration already instantiated in a tenant | SaaS Foundation | `STORE` + `GOVERNANCE` | `SPECIFIED` — see §8.1 |
| `MTI-36` | Configuration is **versioned with effective dates and never regenerated in place**. Every generated operation, movement and proposal resolves to the configuration version in force at the time it was generated | Inventory | `STORE` | `SPECIFIED` — carries `IV-15` |
| `MTI-37` | A capability or feature switch change is scoped to one `CTX`, is an approved act, is versioned, and is never retroactive in effect | Inventory + Boss | `GOVERNANCE` | `SPECIFIED — CONDITIONAL (`MTI-D-03`, `GAP-MD-14`)` |

### 8.1 `MTI-35` against the regeneration hazard

`L2-OBS` records that reconfiguring a warehouse causes its operation types, locations and routes to be **re-derived**. R4 records this as the `SAAS-04` regeneration risk and confirms `IV-15` as the required divergence.

Regeneration is a multi-tenant invariant concern and not only a versioning concern, because re-derivation is precisely the moment at which a derived record can be recreated **without** its company — the condition `R4-F-09` describes, produced in bulk by an ordinary administrative action. `MTI-35` and `MTI-04` together are what prevent that.

**What a tenant may change, and what remains platform-owned, is not decided here.** It is `GAP-MD-14` / `SAAS-04`, open, and is recorded as decision blocker `MTI-D-03`.

---

## 9. Family G — Identity, Event, Audit And Replay (`MTI-38` .. `MTI-42`)

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-38` | Every context-bearing act emits an immutable event carrying the full `CTX`, the actor, the authority relied on, the **physical event date and the entry date as two distinct values**, and the evidence reference | Inventory | `STORE` | `SPECIFIED` |
| `MTI-39` | An event's `CTX` is immutable. A correction is a new, linked event that references the original; an event is never edited and never deleted | Inventory | `STORE` | `SPECIFIED` — carries `P-02`, `IV-05`, `INV-F-40` |
| `MTI-40` | Any change to a context anchor — a warehouse's company, a location's parent or kind, a route's company, a product's company enablement — is itself an evented, approved act carrying before and after values | Inventory | `GOVERNANCE` + `STORE` | `SPECIFIED` |
| `MTI-41` | A replay of any sequence of events reproduces the identical `CTX` on every resulting record. `CTX` is never re-resolved from current configuration during a replay | Inventory + Migration | `DOMAIN` | `SPECIFIED — RANK 2 DEPENDENT` — see §9.1 |
| `MTI-42` | A record created by bulk load or migration has its `CTX` **explicitly assigned and evidenced**, never defaulted, never inferred from a legacy name, code or text match | Migration + Inventory | `STORE` + `GOVERNANCE` | `SPECIFIED — RANK 3 DEPENDENT` — see §9.2 |

### 9.1 `MTI-41` states a property that cannot yet be exercised

Replay determinism for `CTX` is specifiable. Replay **safety** is not, because a replay that cannot distinguish a retry from a second genuine event will produce duplicate records whose `CTX` is individually correct and collectively wrong. That is `RISK-C02`, rank 2, not designed here. `MTI-41` is specified and explicitly marked as not exercisable alone.

### 9.2 `MTI-42` against the two migration findings

`R4-F-23` records that migrating legacy batch identities without resolving company scope imports the cross-company collision surface in bulk. `R4-F-24` records that assigning location kinds by name-matching silently mis-states the financial meaning of historical movements. Both describe the same failure: a bulk act that resolves a semantically load-bearing attribute by inference.

`MTI-42` prohibits inference for `CTX`. It does **not** address the location-kind half of `R4-F-24`, which is a financial-meaning attribute rather than a context attribute and is carried at `11` as a Migration item. And the provenance reference that would make a migrated record's origin inspectable is `GAP-FS-08`, rank 3, not designed here.

---

## 10. Family H — Handoff And Reporting Carriage (`MTI-43` .. `MTI-46`)

This family is what makes handoff element 10 specifiable. Detail at `06`.

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-43` | Every emitted handoff fact carries the resolved `CTX` **and an attestation** naming which invariants guaranteed it and which control last asserted them. Element 10 is satisfied by the tuple **plus** the attestation, never by the tuple alone | Inventory | `DOMAIN` | `SPECIFIED` — see §10.1 |
| `MTI-44` | **No handoff fact spans contexts.** An inter-company movement emits two single-context facts linked by a Cross-Context Relationship identity from the `MTI-22` register | Inventory | `DOMAIN` | `SPECIFIED — CONDITIONAL (`JT-10`, `GAP-FS-07`)` |
| `MTI-45` | Every consuming module — Accounting, Sale, Purchase, Manufacturing, Approval, Document, Reporting — receives `CTX` as a **mandatory, non-inferable** input. A consumer may not derive, default or reconstruct it | Inventory + consuming domains | `DOMAIN` | `SPECIFIED` |
| `MTI-46` | A continuous reconciliation asserts **context conservation** across handoffs: every fact emitted in a context is received in that context, and the emitted and received populations agree | Inventory + Accounting | `CONTROL` | `SPECIFIED — VALUE HELD` |

### 10.1 Why `MTI-43` requires an attestation and not only a value

The contract's enforcement rule at §4 (`d9e845e`) disqualifies a scenario where an element is *missing, ambiguous, **unsupported by evidence**, contradictory, or dependent on an unapproved assumption*. A `CTX` value printed on a payload satisfies "present". It does not satisfy "supported by evidence".

R4's phrasing of the gap is precise on this point: company and tenant context *"can be carried but not guaranteed"* (`09` §3). Carriage was never the missing thing. **The guarantee is the missing thing**, and a guarantee is only inspectable if the payload says what guaranteed it. `MTI-43` is therefore the invariant that most directly addresses `RISK-U03` as R4 actually states it.

Recorded as a new finding: `MTI-F-04`.

---

## 11. Family I — Lifecycle (`MTI-47` .. `MTI-50`)

| ID | Invariant | Owner | Layer | Status |
|---|---|---|---|---|
| `MTI-47` | A newly provisioned tenant begins with **zero inherited operational data**. Only versioned template content is instantiated, by copy, under `MTI-35` | SaaS Foundation | `PLATFORM` | `SPECIFIED` |
| `MTI-48` | Company deactivation **freezes and does not delete**. Deactivated-company records remain fully context-resolvable, remain visible to audit and reporting under an explicit historical scope, and accept no new facts | Inventory + SaaS Foundation | `PLATFORM` + `GOVERNANCE` | `SPECIFIED` |
| `MTI-49` | Tenant offboarding, data export and data erasure are bounded by `CTX`: an export contains exactly one tenant's data and no other, and an erasure removes exactly that tenant's data and nothing another tenant relies on | SaaS Foundation + Legal | `PLATFORM` + `GOVERNANCE` | `SPECIFIED — CONDITIONAL (`MTI-D-05`, `GAP-MD-29`)` — see §11.1 |
| `MTI-50` | The evidence that each invariant held — control run, timestamp, scope, result — is itself retained, context-scoped and inspectable, and is the evidence reference required by handoff element 16 | Inventory + SaaS Foundation | `CONTROL` | `SPECIFIED` |

### 11.1 `MTI-49` sits on a gap with no coverage anywhere

`GAP-MD-29` — the PDPA scope for Inventory documents — is recorded in the R4 dependency map as having **zero coverage anywhere in the evidence chain**. Erasure and export are inherently isolation acts, so the invariant belongs here; but its content depends on a legal scope that has never been established, and no AI may supply it.

`MTI-49` is therefore specified in shape and **conditional in content**, recorded as decision blocker `MTI-D-05`, routed jointly to the Account and Legal tracks. No statutory claim of any kind is made by this session.

---

## 12. Roll-Up

| Measure | Result |
|---|---:|
| Invariants specified | **50** |
| Families | 9 |
| `SPECIFIED` unconditionally | 35 |
| `SPECIFIED — CONDITIONAL` on a named ruling or input | 6 |
| `SPECIFIED — VALUE HELD` under the COGS Gap | 4 |
| `SPECIFIED — RANK 2 / RANK 3 DEPENDENT` | 5 |
| Invariants **proven** by this session | **0** |
| Invariants enforced at `STORE` | 27 |
| Prior items closed by this session | **0** |
| New findings raised | 4 — `MTI-F-01` .. `MTI-F-04` |
| New decision blockers raised | 6 — `MTI-D-01` .. `MTI-D-06` |

**Every carried identifier is preserved unchanged.** `RISK-U03`, `GAP-FS-10`, `U-03`, `R4-F-06`, `R4-F-09`, `R4-F-22`, `IV-01` .. `IV-15`, `CN-01` .. `CN-36` are cited, not renumbered, and none is closed.

---

## 13. Relationship To The `IV-01` .. `IV-15` Candidate Invariants

The v1.0 candidate invariants are **not superseded**. This set is orthogonal to them: `IV-*` states what must be true of stock, quantity, value and identity; `MTI-*` states what must be true of context. Three overlap and are carried explicitly rather than restated:

| Carried | Into | Relationship |
|---|---|---|
| `IV-04` — traceable identity unique per product per company, enforced below the application layer | `MTI-12`, `MTI-17` | `MTI-*` supplies the context tuple and the non-confusability rule `IV-04` does not state |
| `IV-08` — one company per record, guaranteed below the application layer | `MTI-04`, `MTI-05`, `MTI-17` | `MTI-*` is the expansion of `IV-08` from a one-line invariant into an enforceable set with anchors, controls and acceptance criteria |
| `IV-15` — configuration versioned with effective dates, never regenerated in place | `MTI-35`, `MTI-36` | `MTI-*` adds the multi-tenant consequence of regeneration that `IV-15` does not state |

**`IV-08` is the single sentence this entire file expands.** That it existed as a candidate invariant since v1.0, and that `RISK-U03` records the set as non-existent, are both true: a candidate invariant is a proposition; an invariant set is a specification with anchors, layers, controls and acceptance criteria. The gap was the second, and this file addresses the second.

---

## 14. Non-Authorization Lock

This file does not declare, and this session is not empowered to declare: `PASS`, `APPROVED`, `CLOSED`, `FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, merge approval, or release authorization.

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
