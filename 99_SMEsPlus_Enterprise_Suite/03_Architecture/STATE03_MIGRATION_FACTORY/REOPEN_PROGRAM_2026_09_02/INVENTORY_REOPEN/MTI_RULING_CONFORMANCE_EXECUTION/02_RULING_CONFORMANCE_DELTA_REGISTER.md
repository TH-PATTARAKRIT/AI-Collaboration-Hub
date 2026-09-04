# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 02 — Ruling Conformance Delta Register

Control Level: `/L9999.9999`
Status: `32 DELTAS REGISTERED — 0 ITEMS CLOSED — CONFORMANCE SET IS LARGER THAN THE VETO CONDITION THAT DEMANDS IT`

---

## 1. What A Delta Is Here

A **delta** is a change the published design must undergo to conform to a Boss ruling, stated with the consequence that follows from making it.

A delta is **not**:

- a closure — no finding, proof, gap, capability or dependency is closed by any delta below;
- an amendment to a ruling — where the published design and a ruling disagree, **the design changes and the ruling stands**;
- a decision — where a delta cannot be completed without a decision, the decision is registered at `11` §3 with its options stated and **never chosen**.

### 1.1 Delta vocabulary

| Transition | Meaning |
|---|---|
| **ANCHOR CHANGE** | The object's context anchor moves. The most consequential class, because `MTI-06` makes an anchored spine immutable once a record has participated in a completed act |
| **VOID** | A published clause ceases to have a referent and must be removed rather than reinterpreted |
| **ELIMINATED** | A design construct is voided in full and no longer needs proving. A **reduction** |
| **CONDITIONALITY RESOLVED** | A `SPECIFIED — CONDITIONAL` status loses its condition. The content still needs rewriting; the status alone is not the delta |
| **WIDENED** | An existing obligation acquires more to carry, cover or attest. Moves the target further away |
| **ADDITION** | A carrier, class or control the rulings require and the published design has nowhere to put |
| **RE-SCORE BASIS** | Evidence supplied so that the owning body can re-score its own item. **This session re-scores nothing** |

---

## 2. The Headline, Stated First

`RC-V-01` names the discharge condition as *"until `MTI-11`, `XCR-03`, `04` §4.1 and matrix rows 5-7 are re-specified to a company anchor"*.

Applying **all three rulings together** rather than `MTI-D-01` alone, the conformance set is:

| Measure | `RC-V-01`'s stated condition | Conformance set found by this session |
|---|---:|---:|
| Context-and-visibility matrix rows requiring an anchor change | **3** (rows 5, 6, 7 read as "5-7") | **5** — rows 5, 6, 7, **16**, **17** |
| Invariants requiring a text change | 1 (`MTI-11`) | **14** |
| Cross-context register entries affected | 1 (`XCR-03`) | **3** — `XCR-01`, `XCR-03`, `XCR-04` |
| Handoff context fields requiring addition | 0 | **2** — `HF-CTX-10`, `HF-CTX-11` |
| Enforcement-point classes requiring addition | 0 | **1** — `EP-P` |
| New invariants required | 0 | **8** — `CF-I-01` .. `CF-I-08` |
| Consuming modules | 7 | **8** — Payment added |
| **Total deltas** | — | **32** |

**`RC-V-01`'s discharge condition is necessary and not sufficient.** Executing it exactly as written would leave matrix rows 16 and 17 anchored to `tenant` in a design in which `MTI-D-03` names both object classes tenant-configurable and `MTI-04` forbids a null company on every Inventory record. Recorded as **`CF-F-02`**.

**This session does not amend `RC-V-01`.** Amending or widening a veto is the issuing body's act. The under-inclusiveness is recorded, the evidence is supplied, and the widening is routed to AAS+ and Boss at `12` §5 and `14` §7.

---

## 3. Group A — Deltas Required By `MTI-D-01`

Product identity is anchored to `company` within `tenant`. Similarity of code, name, barcode, UoM, category, route or description never creates shared identity.

| ID | Object | Published State | Required State | Transition | Consequence |
|---|---|---|---|---|---|
| `CD-01` | `MTI-11` anchor | *"Definitional identity anchored to `tenant`; every operational and financial attachment anchored to `company`."* | **Definitional identity anchored to `company` within `tenant`.** The product is a company-owned business object; there is one anchor, not two | **ANCHOR CHANGE** | The spine of every product-derived record moves. Because `MTI-06` makes a spine immutable after a completed act, this is the delta that must land **before** any build, which is the whole basis of `RC-V-01` |
| `CD-02` | `MTI-11` enablement clause | *"A company may transact a product only where an explicit company enablement exists."* | **VOID as written.** Under Option B a product belongs to exactly one company; ownership *is* the enablement | **VOID** | Retaining the clause would imply a shared master that no longer exists, and would reintroduce the tenant-level surface `CD-07` removes. An enablement gate over a company-owned object is a second, contradictory anchor |
| `CD-03` | `MTI-11` status and owner | `SPECIFIED — CONDITIONAL (MTI-D-01)`; owner `Inventory + Boss` | `SPECIFIED`; owner `Inventory`. Layer `STORE` + `GOVERNANCE` unchanged | **CONDITIONALITY RESOLVED** | The condition is discharged by a Boss act, not by this session. **The invariant is not thereby proven** — `MTI-11` remains `SPECIFIED, NOT BUILT, NOT VERIFIED` |
| `CD-04` | `04` matrix row 5 — Product (`CN-11`) | Anchor `tenant (definition) / company (attachment)`; *"Definitional identity readable tenant-wide; transactable only in a company that has an explicit enablement"* | Anchor **`company`**. Visibility: readable, selectable, referenceable and reportable **only within its owning company**. Costing and valuation attachment company-scoped, unchanged | **ANCHOR CHANGE** | Row 5 was the only row in the matrix declaring two anchors for one object, which sat awkwardly against `MTI-05`'s *"exactly one context anchor"*. The conformance change removes the ambiguity as a side effect |
| `CD-05` | `04` matrix row 6 — Product variant (`CN-12`) | Anchor `its parent product`; status `SPECIFIED — CONDITIONAL (MTI-D-01, GAP-FS-03)` | Anchor unchanged (**follows its parent**, which is now company-anchored). Status `SPECIFIED — CONDITIONAL (GAP-FS-03)` | **CONDITIONALITY RESOLVED**, partly | The `MTI-D-01` half of the conditionality is discharged. **`GAP-FS-03` is untouched and remains open** — attribute change after variants hold stock is unaffected by any ruling |
| `CD-06` | `XCR-03` — tenant-level definitional master reference | One of four `MTI-22` register entries, `SPECIFIED — CONDITIONAL (MTI-D-01)` | **ELIMINATED.** There is no tenant-level definitional master for a company-scoped record to reference | **ELIMINATED** | The `MTI-22` register falls from **4 entries to 3**. A register whose *completeness* is the isolation claim must be corrected when an entry ceases to exist, or the claim is made over a list that no longer describes the system. Register re-specified at `05` |
| `CD-07` | `04` §4.1, product and variant half | *"Tenant-level definitional data is a shared surface, and shared surfaces must be proven too"*, applied to entries 5 and 6 | **VOID for entries 5 and 6.** No shared product surface exists within a tenant, so there is nothing to isolation-prove | **VOID — favourable** | A genuine **reduction** in proof burden. Carried from `RC-F-02`. See `CD-15`, which extends the void to the rest of §4.1 for a different reason |
| `CD-08` | `L8-01` Product, `L8-02` Variant — context component of canonical identity | `L8-01`: *"`tenant` for the definitional identity; `company` on every attachment"*; immutable from *"Creation (tenant); first enablement (company)"* | `L8-01`: **`company` within `tenant`**, single component; immutable **from creation**. `L8-02` follows its parent | **ANCHOR CHANGE** | Removes a two-part immutability trigger. Under Option B there is no "first enablement" event, so an immutability rule keyed to it would never fire. The identity becomes immutable at one moment instead of two |
| `CD-09` | `L10-04` Product identity continuity | *"A legacy product resolves to exactly one product, and its company enablements are assigned explicitly"*; `SPECIFIED — CONDITIONAL (MTI-D-01)` | **A legacy product resolves to exactly one product in exactly one company. Where the source business reality is that two companies operated the same catalogue item, migration produces two products and must evidence that the duplication was deliberate** | **CONDITIONALITY RESOLVED** + **WIDENED** | `MTI-D-01` rule 7 turns duplicate preservation from a tolerance into a requirement, and a requirement must be evidenced. The evidence is provenance, and provenance is `GAP-FS-08`, which does not exist. **`GAP-FS-08` is unchanged in status and larger in scope** — carried from `RC-F-01`'s consequence chain, restated here because `L10-04` is where a migration executor would read it |
| `CD-10` | `MTA-17` — *"a tenant-level master change hits every company at once"* | `RESIDUAL: MATERIAL`, with the stated basis *"this is the cost of `MTI-D-01` option A and it is why the decision is a Boss item"* | **RE-SCORE BASIS supplied.** Boss ruled Option B, so the stated cost is not incurred. After `CD-01`, `CD-12`, `CD-13` and `CD-14` the attack's mechanism — a change to a tenant-anchored master propagating to every company — has **no tenant-anchored Inventory object class left to act on**, subject to `CF-D-01` | **RE-SCORE BASIS** | **This session does not re-score `MTA-17` and does not close it.** Re-scoring another session's registered attack is that session's act or AAS+'s. What is supplied is the basis: the attack was scored against a design position Boss did not take |
| `CD-11` | `XCR-01` — inter-company transfer | Two single-context facts *"correlated by a shared relationship identity"* | Unchanged in structure. **Made explicit:** the correlation is carried **entirely** by `HF-CTX-07` and the `MTI-22` register entry, and may **never** be reconstructed by matching product code, name, barcode, UoM or description | **WIDENED** | Under Option A the pairing had a natural corroboration through a shared definitional identity. Under Option B it has none, so the relationship identity becomes load-bearing where it was previously corroborated. `JT-10` is unchanged in status and harder in content. **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** on every treatment and valuation consequence |

### 3.1 What Group A does not change

`MTI-16`'s company-scoped costing and valuation attachment is **unchanged** — the invariant set already had costing company-scoped under either option. `MTI-12`'s traceable-identity tuple `(tenant, company, product, value)` is **unchanged**, and is now reinforced rather than qualified: `MTI-D-01` rule 2 states the same non-confusability principle for product attributes that `MTI-F-01` states for lot and serial values.

---

## 4. Group B — Deltas Required By `MTI-D-03`

Platform-owned core plus tenant configuration overlay. The eleven named record classes are **tenant-configurable**, and AAS+ advice `29` §3 states directly that *"the design should not assume that duplicated configuration across companies is a defect."*

### 4.1 The derivation, stated because Group B is the part `RC-V-01` does not name

Three published statements compose, and their composition is what forces `CD-12` .. `CD-14`:

1. **`MTI-D-03` §3** names Product Category, Unit of Measure Category and Barcode Nomenclature among the records a tenant/company may configure.
2. **`MTI-34`** distinguishes two object classes and states that *"tenant configuration always carries a `CTX`"*. Platform-provided template content is the other class, and `MTI-D-03` places these three in the first.
3. **`MTI-04`** admits no exception: `tenant` and `company` are non-optional on every Inventory record, and a record whose company cannot be resolved is not created.

The consolidation already stated the acceptance criterion this composition produces — `RC-P-36`: *"every configuration record has a mandatory company anchor; a company-less configuration record is rejected at `STORE`."* **The published matrix has not been brought into line with it.**

| ID | Object | Published State | Required State | Transition | Consequence |
|---|---|---|---|---|---|
| `CD-12` | `04` matrix row 7 — Product category (`CN-08`) | Anchor `tenant (structure) / company (costing facet)`; *"Structure may be tenant-level"* | Anchor **`company`** for both facets. The structure facet is tenant-configurable **per company** under `MTI-D-03`; the costing facet was already company-scoped | **ANCHOR CHANGE** | Two companies holding categories with identical names is a legitimate state, not a data-quality defect. **The costing facet remains `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** — `GAP-FS-02` is precondition-blocked on `JT-01`, which is **NOT DECIDABLE**. `RC-F-08`'s tension is unchanged: tenant configuration of the costing facet must not be permitted while `GAP-FS-02` stands |
| `CD-13` | `04` matrix row 16 — Barcode nomenclature (`CN-16`) | Anchor `tenant`; company axis `S`; *"A nomenclature may be tenant-level"* | Anchor **`company`**; company axis `Y`. Resolution of a scanned value continues to occur within the caller's `CTX`, unchanged | **ANCHOR CHANGE** | **Not named in `RC-V-01`.** `R4-F-12` — a misparsed structured barcode yields a plausible but wrong quantity, silently — now has a **per-company configurable** surface, so the misparse behaviour must be proven per configured nomenclature and not once. `R4-F-12` is not re-scored here; its surface is recorded as larger |
| `CD-14` | `04` matrix row 17 — Unit group and unit (`CN-14`) | Anchor `tenant`; company axis `N`; *"Tenant-level definitional data"* | Anchor **`company`**, **subject to `CF-D-01`** — whether `MTI-D-03`'s *"Unit of Measure Category"* is the same object as the matrix's *"Unit group and unit (`CN-14`)"* is a scope clarification of a Boss ruling, and only Boss may state what a Boss ruling covers | **ANCHOR CHANGE — conditional on `CF-D-01`** | **Not named in `RC-V-01`.** `R4-F-13` — default conversion rounding is upward and repeated conversion inflates quantity monotonically — acquires a per-company configurable surface on the same terms as `CD-13`. **If `CF-D-01` is answered the other way**, row 17 stays tenant-anchored, `CD-15` does not hold in full, and one shared surface survives and must be isolation-proven. Both readings are specified so the clarification can be taken on its merits |
| `CD-15` | `04` §4.1 in full | *"Entries 5, 7, 16 and 17 place definitional data at tenant level… this creates a shared surface within a tenant that `MTI-02` protects across tenants but that nothing protects within a tenant"* | **VOID in full**, subject to `CF-D-01`. After `CD-04`, `CD-05`, `CD-12`, `CD-13` and `CD-14`, **no Inventory object class in the 35-row matrix remains anchored to `tenant` alone** other than the `company` axis itself, which is anchored to `tenant` by definition | **ELIMINATED — favourable** | Recorded as **`CF-F-01`**. The scope of the reduction is larger than `RC-F-02` states: it is not one register entry and one clause, it is the **disappearance of the tenant-level shared-surface class from the Inventory design**. Every proof obligation, attack and disclosure channel written against that class is void with it. Population, pattern and path set for the enumeration are declared at `06` §4 |
| `CD-16` | `MTI-34` | *"Template content is versioned, tenant-neutral and never directly transacted against; tenant configuration always carries a `CTX`"* | Unchanged in wording. **Made explicit as an acceptance criterion:** every instance of every tenant-configurable class carries a mandatory `company`, derived from a declared anchor and rejected at `STORE` when absent — `RC-P-36` promoted from a proof requirement to a stated invariant consequence at `CF-I-07` | **ADDITION** | Without the explicit statement, `MTI-34` reads as a classification rule and a reader may take "carries a `CTX`" as satisfied by a tenant identifier alone. `MTI-04` forbids that, but the two invariants are eleven rows apart and nothing joins them |
| `CD-17` | `XCR-04` — platform template instantiation | `SPECIFIED — CONDITIONAL (MTI-D-03)` | `SPECIFIED`, **bounded by `RC-F-06`**. Copy at provisioning recording the template version; never a live link | **CONDITIONALITY RESOLVED**, bounded | The mechanism half is unblocked. The **content** half is not: `MTI-D-03` §3 ends with *"other approved Inventory configuration/master records"*, so the set of classes `XCR-04` instantiates is open-ended. `L9-04`'s boundary half stays `PARTIALLY DEFINABLE` and `RC-D-02` stays unruled |
| `CD-18` | `MTI-37` — capability and feature switch | `SPECIFIED — CONDITIONAL (MTI-D-03, GAP-MD-14)` | `SPECIFIED — CONDITIONAL (GAP-MD-14)` | **CONDITIONALITY RESOLVED**, partly | The `MTI-D-03` half is discharged. **`GAP-MD-14` / `SAAS-04`'s regeneration and switch-off-guard halves are untouched by any ruling** — `MTI-35`, `MTI-36` and `MTI-37` specify them and nothing verifies them. `RC-P-42` remains the highest-value configuration proof, and it remains unexecutable |
| `CD-19` | Every invariant, matrix row, `L9-*` proof and `MTP-*` scenario | Written for one isolation topology, with no topology stated | **Each carries an explicit topology scope statement: `SHARED SaaS POOL`.** No invariant, proof or scenario may be asserted to transfer to a Private Company topology | **ADDITION** | `RC-F-07` records that all 50 invariants, 35 matrix rows, 8 L9 proofs and 30 `MTP-*` scenarios are written for one topology and none states what changes inside a Private Company. **Stating the scope does not supply the delta and does not reduce `RC-F-07`.** It prevents the more damaging failure: a proof produced in the pool being cited as evidence about a topology it was never run in. Specified as `CF-I-08` |

### 4.2 What Group B does not change

The six pool prohibitions are absolute and are carried unchanged. The five conditions on pool configuration — configuration-led, evidence-backed, reversible where applicable, auditable, and not weakening `MTI-D-01` or `MTI-D-02` — are carried unchanged, including the boundary the consolidation placed on *"reversible where applicable"*: **reversion is a forward act**, a new version whose content matches an older one, never the older one restored.

**Private Company remains an option requiring a Gate record, evidence and a Boss ruling. No customer is in it, no criteria exist to enter it, and nothing in this package treats it as approved or available.**

---

## 5. Group C — Deltas Required By `MTI-D-02`

`AUTH = (tenant, company, warehouse, operation type)`. Full model at `04`.

| ID | Object | Published State | Required State | Transition | Consequence |
|---|---|---|---|---|---|
| `CD-20` | `04` §7 — authorization scope | *"Specified in both shapes, because the ruling is outstanding"*; `AUTH = (tenant, company[, warehouse][, location][, operation class])`; three candidate shapes tabled | **Superseded.** `AUTH = (tenant, company, warehouse, operation type)`, four axes, all mandatory where the acted-on object carries the axis. The three-shape presentation is retained only as lineage | **CONDITIONALITY RESOLVED** | `RISK-U01` / `U-01` is discharged **as a decision**. The build half is untouched. **`RC-D-01` — whether `location` is excluded as an authorization axis or merely not required — is unruled**, and design proceeds on the three ruled dimensions plus tenant. Five matrix rows (4, 14, 19, 22, 23) that `04` §7 assigned to the finest filter stay unsettled and are registered, not assumed away in either direction |
| `CD-21` | `MTI-09` — operation type (`CN-04`) | Anchored to warehouse, therefore to company. Numbering per `(company, operation type)` | Unchanged as an anchor. **Added: operation type is an authorization axis.** Being able to see or select an operation type is not being authorized to act through it | **WIDENED** | An object that was purely structural becomes simultaneously a context anchor and an authorization axis. The two roles must not be conflated: `CF-I-04` states that **defining a configuration object and being authorized to act through it are separate grants**, which is `RC-P-40`'s acceptance criterion promoted to an invariant |
| `CD-22` | `MTI-29`, `MTI-30` — execution boundary | *"Every run, job, scheduler execution and background task resolves exactly one `CTX`"*; a deferred execution carries the `CTX` and the authority | **Extended: every run additionally resolves an explicit operation-type context, and a deferred run revalidates the full four-axis `AUTH` at release, not only the scheduling authority's existence** | **ADDITION** | This is `RC-F-05`. `MTI-D-02` rule 8 requires background jobs and automation to carry **explicit** tenant/company/warehouse/operation-type context; `CTX = (tenant, company, warehouse?, location?)` has no operation-type member, so no published invariant states that a deferred run resolves one. Specified as `CF-I-02`. **`RC-P-23` moves from `DEFINABLE — CONDITIONAL` to `DEFINABLE` as a consequence — a change in definability, not in proof** |
| `CD-23` | `MTI-21`, `EP-Q` | *"Every read… is scoped to the caller's authorized `CTX` set before evaluation"*; `EP-Q` scopes reads *"to the caller's `AUTH` set"* | The scoping set is the **four-axis `AUTH` set**, and the two statements are made to use one term. `MTI-21` currently says `CTX`; `EP-Q` currently says `AUTH`; before the ruling the two were interchangeable and they are not now | **WIDENED** | A read scoped by `CTX` alone would return every warehouse and every operation type within the caller's company. Under `MTI-D-02` rules 2 and 3 that is a leak inside a company. The divergence between `MTI-21`'s wording and `EP-Q`'s is pre-existing and harmless before the ruling; after it, the two words denote different sets |
| `CD-24` | Enforcement-point classes | Eight classes: `EP-R`, `EP-W`, `EP-Q`, `EP-A`, `EP-X`, `EP-E`, `EP-H`, `EP-G`. `EP-R` resolves `CTX`; `EP-Q` scopes **reads** by `AUTH` | **A ninth class, `EP-P` — permission evaluation.** `AUTH` is evaluated before the act, on **every** act, not only on reads | **ADDITION** | Population, pattern and path set at `01` §8 boundary `B-03`; result at `04` §5. Of the eight published classes, exactly one references `AUTH`, and it governs reads. `MTI-D-02` §4.4 of advice `27` requires permission checks *"before search, selection, confirmation, posting handoff, report generation, export, import, scheduler execution, and API execution"* — six of those nine are not reads. **Without `EP-P` there is no function-boundary attachment point for the ruling's central control** |
| `CD-25` | `HF-CTX-01` .. `HF-CTX-09` | Nine context handoff fields. `HF-CTX-03` warehouse; `HF-CTX-08` actor and authority | **Two additions.** `HF-CTX-10` — operation-type identity of the act. `HF-CTX-11` — **authorization attestation**: the identifier of the control run that last asserted the authorization conformance property, with timestamp and result | **ADDITION** | `HF-CTX-10` closes the carriage half: no published field carries the operation type of the act, so `MTI-D-02`'s audit-trail requirement — *"who / what / under which tenant, company, warehouse, operation type"* — has no carrier. `HF-CTX-11` closes the guarantee half and is the direct consequence of `CD-28`. **Both are specified, not built, not verified** |
| `CD-26` | `MTI-38` — event content | Full `CTX`, actor, authority relied on, physical event date and entry date as two distinct values, evidence reference | **Extended: the full four-axis `AUTH` relied on, as a resolved tuple, not as an authority reference alone** | **WIDENED** | `MTI-D-02` §4 and advice `27` §5 both require the audit trail to answer *who performed what action under which tenant, company, warehouse and operation type*. An authority reference identifies the grant; it does not by itself state the four axes the act was performed under. `RC-P-29` is recorded by the consolidation as `DEFINABLE — widened`; this delta is what widens it |
| `CD-27` | `MTI-43`, `MTI-45` | `MTI-43`: element 10 is the tuple **plus** the attestation. `MTI-45`: seven consuming modules | `MTI-43`: the attestation covers **both** tuples — `HF-CTX-05`/`-06` for context, `HF-CTX-11` for authority. `MTI-45`: **eight** consuming modules, Payment added | **WIDENED** + **ADDITION** | `MTI-F-04` widened by `MTI-D-02`; this is its design consequence. Payment is `RC-F-09` and is discharged as a **coverage** obligation at `07`, where it is either given an obligation or recorded as having none, with the search boundary declared. **`AAS-V-01` remains in force: element 10 is `specified, not built, not verified` and no other wording is used anywhere in this package** |

---

## 6. Group D — Cross-Cutting Consequences

These follow from the rulings **in combination** and are not attributable to any one of them. Both `CD-28` and `CD-29` are structural gaps that no prior package states.

| ID | Subject | Published State | Required State | Transition | Consequence |
|---|---|---|---|---|---|
| `CD-28` | **Authorization has no conformance control** | `MTI-19` is the context conformance control: it asserts that stored context equals derived context, that no spine value is absent, and that no relationship crosses a boundary outside the `MTI-22` register. Eight invariants carry the `CONTROL` layer — `MTI-05`, `-16`, `-19`, `-23`, `-24`, `-30`, `-46`, `-50` | **An authorization conformance control is required** — the `AUTH` analogue of `MTI-19`, asserting continuously that every act's recorded `AUTH` was within a grant in force at the time of the act, that no act was recorded with an absent axis, and that no grant spans more than one company. Specified as `CF-I-03` | **ADDITION** | **`CF-F-05`.** Search boundary `B-02` at `01` §8. All eight controls assert a property of **context**; none asserts a property of **authority**. `MTI-30` is the closest and asserts a runtime precondition on one path — a lapsed authority prevents a deferred run — not a continuously asserted conformance property. Class **A within boundary `B-02`**; class **B** for the wider system. The consequence is exact: `04` §2.1 rule 4 of the consolidation requires context and authority to be **evidenced separately**, and `HF-CTX-08` carries the authority **value** while `HF-CTX-06` carries the context **attestation**. There is no attestation for the authority half, and `06` §3.1 of the invariant set is explicit that a value without an attestation is carriage, not guarantee — *the* distinction on which element 10's whole treatment turns |
| `CD-29` | **The operation-type axis ranges over a tenant-owned enumeration** | `MTI-D-02` makes operation type an authorization axis and names eight examples *"including, but not limited to"*. `MTI-D-03` names Operation Type among the records a tenant/company may configure. Nothing maps a tenant-configured operation type to any platform-owned classification | **Every tenant-configured operation type declares exactly one platform-owned operation class. Platform-level controls bind to the class and never to the tenant's label.** Specified as `CF-I-05` | **ADDITION** | **`CF-F-04`.** The two rulings compose to a gap: a platform-level control — *"Scrap requires a second approver"*, *"Landed Cost review is segregated from Landed Cost action"* — cannot be expressed over an enumeration each tenant defines for itself, because the platform has no stable term to bind to. **The remedy shape already exists in the published set**: `MTI-33` requires adjustment, count, scrap, return, transfer and landed-cost reason classification to be *"defined independently of context, so that the same reason means the same thing in every company"*. `CF-I-05` applies exactly that pattern to operation types. **The closure of the platform class enumeration is a Boss decision — `CF-D-02` — and is stated, never chosen** |
| `CD-30` | `L9-03` acceptance criterion; `MTP-15` | `L9-03`'s criterion branches: *"Under a company-only ruling the proof is vacuous… Under a warehouse- or location-level ruling…"*. `MTP-15`'s expected result branches the same way | **De-branched.** `L9-03`: an actor scoped to one warehouse can neither read nor write in another within the same company; **and** an actor scoped to one operation type cannot perform another within the same warehouse. `MTP-15`'s expected result is **rejected**, unconditionally | **CONDITIONALITY RESOLVED** | The proof becomes **non-vacuous** — there is a real property to test. `L9-03` moves from `DEFINABLE — CONDITIONAL` to `DEFINABLE`. **`0 of 8` proofs achieved is unchanged, before and after.** `MTP-16` — that a tax-branch attribute is not derived from warehouse — is **unchanged**: `MTI-07`'s prohibition on equating a warehouse with a Thai tax branch survives `MTI-D-02` intact, because an authorization axis is an operational concept and a tax branch is a statutory one. **No Thai statutory claim is made here; `TH-HOLD-06` is held** |
| `CD-31` | `MTI-33` | *"…each carries a reason classification that is defined independently of context, so that the same reason means the same thing in every company"* | Unchanged in wording. **Recorded as the governing precedent for `CF-I-05`**, and its scope made explicit: the same context-independence requirement now applies to the operation-type axis it is executed under | **RE-SCORE BASIS** | `MTI-33` is `SPECIFIED — VALUE HELD`, and its reason taxonomy is `R4-Q-01`, routed to the Thai panel and unanswered. **The platform operation-class enumeration at `CF-I-05` inherits the same exposure**: it is a set of labels that no Thai user has validated. `0 of 78` |
| `CD-32` | Handoff elements 8, 10, 14 | Element 8 *"suppliable but not unique"* → strengthened; element 10 *"specified, not built, not verified"*; element 14 not suppliable | Element 8 **simplified** — the product half of the resolved tuple is company-resolved by construction. Element 10 **unchanged in status, widened in obligation**. Element 14 **unchanged in status, widened in scope** by `CD-09` | **WIDENED** / **RE-SCORE BASIS** | **Zero of the ten material Inventory-to-Accounting handoffs is contract-compliant, before and after.** Elements 4 and 7 remain `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` on eight of ten; element 15 remains absent on all ten (`RISK-C02`); element 14 remains absent on the handoffs where it is **contractually** applicable, which per `REV-F-02` is the migration, replay and recovery handoffs and not all ten |

---

## 7. Delta Roll-Up

| Group | Ruling | Deltas | Anchor Changes | Voids / Eliminations | Conditionality Resolved | Widened | Additions | Re-Score Basis |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | `MTI-D-01` | 11 | 3 | 3 | 3 | 2 | 0 | 1 |
| **B** | `MTI-D-03` | 8 | 3 | 1 | 2 | 0 | 2 | 0 |
| **C** | `MTI-D-02` | 8 | 0 | 0 | 1 | 4 | 3 | 0 |
| **D** | combination | 5 | 0 | 0 | 1 | 1 | 2 | 2 |
| **Total** | | **32** | **6** | **4** | **7** | **7** | **7** | **3** |

Counted by primary transition; several deltas carry a second, and the second is stated in the row.

| Measure | Result |
|---|---:|
| Deltas registered | **32** |
| Deltas that are **reductions** in work | **4** — `CD-06`, `CD-07`, `CD-15`, and the element-8 half of `CD-32` |
| Deltas blocked on a decision this session may not take | **2** — `CD-14` (`CF-D-01`), `CD-29` (`CF-D-02`) |
| Deltas carrying `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` | **3** — `CD-11`, `CD-12` costing facet, `CD-32` elements 4 and 7 |
| Findings closed by any delta | **0** |
| Proofs achieved | **0 of 8** |
| Cross-proof scenarios verified | **0 of 22** |
| Handoffs contract-compliant | **0 of 10** |
| Joint decisions ready | **0 of 12** |
| Thai validations | **0 of 78** |
| Capabilities built | **0** |
| Vetoes discharged | **0** |
| Carried identifiers renumbered, retired or merged | **0** |

**No open-item roll-up total is asserted by this session.** `REV-F-04` records the 92 figure as not independently reconstructable and no open-item crosswalk exists. The new items are enumerated exactly at `11` §6.

---

## 8. What This Register Does Not Do

| Not done | Why |
|---|---|
| It does not amend, widen or discharge `RC-V-01` | Amending a veto is the issuing body's act. `CF-F-02` supplies the evidence and routes it |
| It does not re-score `MTA-17`, `R4-F-12`, `R4-F-13`, `MTI-F-03` or any other body's registered item | Severity classification of another session's item is not this session's act. `RE-SCORE BASIS` is supplied instead |
| It does not close `RC-F-01`, `RC-F-02`, `RC-F-05`, `RC-F-09` or any `RC-F-*` item | A specification is not a closure. The findings close when an implementation exists and is independently verified |
| It does not decide `CF-D-01`, `CF-D-02`, `RC-D-01` .. `RC-D-04`, `MTI-D-04`, `MTI-D-05` or `MTI-D-06` | Options are stated at `11` §3. **Never chosen** |
| It does not specify the controlled mapping / provenance layer | `RC-F-03`. Gated on `MTI-D-04`, unruled. `CF-I-06` states a **prohibition** in its absence, which is not a specification of it |
| It does not specify anything for the Private Company topology | `RC-D-03`. `CF-I-08` states a **scope rule**, which is not a delta |
| It does not touch valuation, COGS, landed-cost posting, period close, return cost basis or cross-company valuation | `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`. 10 of 10 areas locked |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
