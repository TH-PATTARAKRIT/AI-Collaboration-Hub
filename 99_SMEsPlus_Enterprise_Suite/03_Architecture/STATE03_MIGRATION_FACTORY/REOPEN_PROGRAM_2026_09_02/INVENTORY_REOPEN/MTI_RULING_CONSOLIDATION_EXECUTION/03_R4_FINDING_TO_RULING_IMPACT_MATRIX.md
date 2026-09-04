# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 03 — R4 Finding To Ruling Impact Matrix

Control Level: `/L9999.9999`
Status: `IMPACT ASSESSED — 0 FINDINGS CLOSED BY RULING — 1 DIRECT CONTRADICTION FOUND — 2 NEW CAPABILITIES CREATED`

---

## 1. The Rule This File Applies

Authorization §9.3: **"Do not mark any blocker closed merely because a ruling exists."**

A ruling changes what a finding is *waiting for*. It does not change whether the finding is *true*. This matrix therefore records, for every affected item, the **transition** — not a closure.

Transition vocabulary used throughout:

| Transition | Meaning |
|---|---|
| **RESOLVED AS DECISION** | The item was a question for Boss. Boss answered it. Nothing was built or proven |
| **NARROWED** | The item survives, but its open surface is smaller and the residual is named |
| **RE-SPECIFICATION REQUIRED** | The ruling contradicts a published design statement. The design must change; the finding does not close |
| **UNCHANGED** | The rulings touch it in no way |
| **NEWLY CREATED** | The item did not exist before the rulings and exists because of them |
| **ELIMINATED** | A design construct is voided by the ruling and no longer needs proving |

---

## 2. The Headline, Stated First Because It Is The Result

| Measure | Before Rulings | After Rulings |
|---|---:|---:|
| Decision blockers `MTI-D-01` .. `MTI-D-03` outstanding | **3** | **0** |
| `MTI-D-04` .. `MTI-D-06` outstanding | 3 | **3** |
| L9 isolation proofs achieved | **0 of 8** | **0 of 8** |
| Boss-approved cross-proof scenarios verified | **0 of 22** | **0 of 22** |
| Material Inventory-to-Accounting handoffs contract-compliant | **0 of 10** | **0 of 10** |
| Joint decisions ready | **0 of 12** | **0 of 12** |
| Thai validations obtained | **0 of 78** | **0 of 78** |
| `R4-F-*` findings closed | — | **0** |
| `MTI-F-*` findings closed | — | **0** |
| `REV-F-*` findings closed | — | **0** |
| AAS+ vetoes discharged | — | **0** |
| Capabilities built | — | **0** |
| **Canonical invariants now contradicting a governing ruling** | **0** | **1** — `MTI-11` |
| **Capabilities required by a ruling with no published design** | **0** | **2** |

**Every count that measures proof is unchanged. The only counts that moved are the count of open shape decisions, which fell to zero, and two counts that moved in the wrong direction.**

---

## 3. The Direct Contradiction — `MTI-11` Versus `MTI-D-01`

This is the single most consequential finding of the consolidation, and it is a contradiction the authorization's §9.2 exception permits recording.

### 3.1 What each document says

| Source | Statement |
|---|---|
| `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md`, `MTI-11` | *"**Definitional identity anchored to `tenant`;** every operational and financial attachment anchored to `company`."* Status: `SPECIFIED — CONDITIONAL (MTI-D-01)` |
| `03` §4.2 | *"The position taken is **A**."* — tenant-level definitional identity with company-level attachment |
| Boss ruling `MTI-D-01` | **`OPTION B`** — company-owned product master, tenant/company-scoped product identity |

**The canonical invariant set took Option A. Boss ruled Option B. The invariant set is now out of conformance with the ruling that governs it.**

### 3.2 How the contradiction is resolved

**In the ruling's favour, without qualification.** Boss is the sole Final Approver; a Boss ruling is authoritative over a design position an executor took while waiting for it. The invariant set's own status field anticipated exactly this — `SPECIFIED — CONDITIONAL (MTI-D-01)` means *"this changes when the ruling arrives"*, and the ruling has arrived and changed it.

The design session recorded the position honestly, disclosed it as a decision belonging to Boss, upheld the attack on it in its own adversarial challenge (`12` §2, attack 4), and set out both options with their costs so the ruling could be taken on its merits. **That is the process working, not failing.** The consequence is nonetheless a document that must be revised before anything is built against it.

### 3.3 What must change in the invariant set

| Item | Current State | Required State Under `MTI-D-01` |
|---|---|---|
| `MTI-11` | Definitional identity anchored to `tenant` | **Definitional identity anchored to `company`.** The product is a company-owned business object |
| `MTI-11` clause *"a company may transact a product only where an explicit company enablement exists"* | An enablement gate over a shared tenant-level master | **Void as written.** Under Option B a product belongs to exactly one company; enablement is inherent in ownership, not a separate grant. Retaining the clause would imply a shared master that no longer exists |
| `XCR-03` — *"Tenant-level definitional master reference"* | `SPECIFIED — CONDITIONAL (MTI-D-01)`; one of four cross-context register entries | **ELIMINATED.** Under Option B there is no tenant-level definitional master to reference. The `MTI-22` register falls from 4 entries to **3** |
| `04` §4.1 — *"Tenant-level definitional data is a shared surface, and shared surfaces must be proven too"* | A proof obligation over the product master | **Void for product and variant.** The shared surface does not exist, so there is nothing to isolation-prove. This is a genuine **reduction** in proof burden |
| Matrix rows 5, 6, 7 (`04`) | `SPECIFIED — CONDITIONAL` | Conditionality **resolved**; content must be rewritten to a company anchor |
| `L10-04` | Conditional on `MTI-D-01` | Conditionality resolved; migration must **preserve** duplicates per ruling rule 7 |
| `MTA-17` | Conditional on `MTI-D-01` | Conditionality resolved; the attack must be re-scored against a company-anchored master |
| `MTI-16` costing/valuation attachment | Company-scoped | **Unchanged.** Option B does not disturb it; the invariant set already had costing company-scoped under either option |

### 3.4 Consequence for reliance

**No design work may be built against `03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md` as published.** A build conforming to `MTI-11` as written would violate `MTI-D-01`. This is an **independent bar on implementation start**, additional to and separate from `AAS-V-02`. See `11` §5.

Recorded as `RC-F-01`.

---

## 4. Impact On The Three Decision Blockers Ruled

| ID | Before | Transition | After | Residual |
|---|---|---|---|---|
| `MTI-D-01` | `OPEN — BOSS RULING REQUIRED` | **RESOLVED AS DECISION** | `DECIDED BY BOSS — OPTION B` | `RC-F-01` re-specification; `RC-F-03` mapping layer; `RC-F-04` `MTI-D-04` dependency |
| `MTI-D-02` | `OPEN — BOSS RULING REQUIRED` | **RESOLVED AS DECISION** | `DECIDED BY BOSS — Company + Warehouse + Operation-Type` | `RC-D-01` location axis; `RC-F-05` execution-family axis gap |
| `MTI-D-03` | `OPEN — BOSS RULING REQUIRED` | **RESOLVED AS DECISION** | `DECIDED BY BOSS — Platform Core + Tenant Config Overlay` | `RC-F-06` open-ended list; `RC-F-07` Private Company undefined; `RC-D-02`, `RC-D-03` |

---

## 5. Impact On The Eight L9 Isolation Proofs

The rulings change what each proof is **waiting for**. None changes a proof from unachieved to achieved.

| Proof | State Before | Ruling Effect | State After | Still Blocked By |
|---|---|---|---|---|
| `L9-01` Tenant isolation | `DEFINABLE` | None | `DEFINABLE` | Privileged-bypass path audit — started, never completed. Plus implementation |
| `L9-02` Company isolation | `DEFINABLE` | **`D-01` strengthens the proposition** — with no tenant-level product master, one whole class of cross-company reference disappears | `DEFINABLE` — **narrowed and simplified** | Implementation and independent verification. `R4-F-06`, `R4-F-09` open |
| `L9-03` Branch and location isolation | `DEFINABLE — CONDITIONAL (MTI-D-02 / U-01)` | **`D-02` resolves the conditionality.** The proof is **non-vacuous** — warehouse and operation-type scoping are now required, so there is a real property to test | **`DEFINABLE`** — conditionality removed | Implementation. `RC-D-01` affects only the location axis, not the warehouse or operation-type axes |
| `L9-04` Template versus tenant-owned boundary | `PARTIALLY DEFINABLE` — mechanism definable, boundary conditional | **`D-03` substantially supplies the boundary half** — eleven record classes named, six prohibitions named | **`PARTIALLY DEFINABLE`** — materially narrowed, **not** closed | The acceptance criterion requires the enumeration to be *"published and **complete**"*. `"Other approved Inventory configuration/master records"` is open-ended — `RC-F-06` |
| `L9-05` No cross-tenant stock visibility | `DEFINABLE` | None directly; `D-02` rule 7 reinforces report/export scope | `DEFINABLE` | Implementation. `R4-F-22` derived surfaces |
| `L9-06` No cross-company cost leakage | `PARTIALLY DEFINABLE` — context half definable, value half `HOLD` | **Context half narrowed by `D-01`**; value half untouched | `PARTIALLY DEFINABLE` | Value half: `JT-01` **NOT DECIDABLE**, `JT-10`, `GAP-FS-07`, `R4-F-20`. **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| `L9-07` No hard-coded Thailand-only logic | `DEFINABLE — CONDITIONAL (Lane C)` | None | `DEFINABLE — CONDITIONAL` | The Thai requirement classification inventory does not exist. `TH-HOLD-01` .. `-09`, `0 of 78` |
| `L9-08` Controlled localization extension points | `DEFINABLE — CONDITIONAL` on `L9-07` | None | `DEFINABLE — CONDITIONAL` | `L9-07` |

**`0 of 8` proofs achieved, before and after. Two proofs improved in definability — `L9-03` from conditional to definable, `L9-04` from thinly to substantially specified. Neither is a proof.**

---

## 6. Impact On The Sixteen Handoff Contract Elements

| Element | Position Before | Ruling Effect | Position After |
|---:|---|---|---|
| 1, 3, 5, 6, 11 | Suppliable | None | Suppliable — unchanged |
| 2 `WHO owns the fact` | Suppliable | `D-02` strengthens the authority reference — `HF-CTX-08` must now carry warehouse and operation-type authority, not company authority alone | Suppliable — **obligation widened** |
| 4 `WHEN financial recognition occurs` | **Not suppliable** | None | **Not suppliable** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| 7 `WHAT valuation / cost basis` | **Not suppliable** | None | **Not suppliable** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| 8 `WHICH Product / Lot / Serial` | Strengthened; identity is the resolved tuple | **`D-01` simplifies it.** With a company-owned master the product half of the tuple is company-resolved by construction | Suppliable subject to implementation — **simplified** |
| 9 `WHICH Warehouse / Location` | Strengthened | `D-02` makes warehouse an **authorization** axis as well as a situational one | Suppliable subject to implementation |
| **10** `WHICH Company / Tenant` | **`specified, not built, not verified`** | **None. A ruling does not build or verify.** `AAS-V-01` remains in force and its wording may not be substituted | **`specified, not built, not verified`** — **UNCHANGED** |
| 12, 13 | Partial — rank 2 dependent | None | Partial — rank 2 dependent |
| **14** `WHICH Migration / Replay Batch` | **Not suppliable** — `GAP-FS-08` | **Obligation widened.** `D-01` rule 7 makes duplicate preservation across companies a migration requirement, which the provenance reference must now evidence | **Not suppliable** — `GAP-FS-08`, **scope grown** |
| **15** `WHICH Idempotency Identity` | **Not suppliable** — `RISK-C02` | None | **Not suppliable** — `RISK-C02` |
| 16 `WHAT Evidence proves it` | Partial | `D-02` widens what the attestation must cover | Partial — **obligation widened** |

**Zero of the ten material Inventory-to-Accounting handoffs is contract-compliant. Unchanged. Three elements had their obligations widened by the rulings, which moves the target further away, not closer.**

---

## 7. Impact On Every R4 Finding

`R4-F-01` .. `R4-F-25`, assessed individually. **No finding is closed.**

| ID | Subject | Transition | Post-Ruling Status |
|---|---|---|---|
| `R4-F-01` | Inverted min/max silently accepted | UNCHANGED | Open — Lane A |
| `R4-F-02` | Count is an attribute, not a document with lifecycle | UNCHANGED | Open — Lane A |
| `R4-F-03` | Scrap has no salvage concept | UNCHANGED | Open — Lane A / B for value |
| `R4-F-04` | Scrap has no approval path | **NARROWED.** `D-02` makes Scrap a named operation type with its own authorization axis, so an approval control now has a context to attach to | Open — Lane A. Approval **designable**, not designed |
| `R4-F-05` | Weight/volume landed-cost distortion | UNCHANGED | Open — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` on the posting half |
| `R4-F-06` | Company-less traceable identity possible | **NARROWED.** `D-01` removes the shared-master route to cross-company identity confusion; `MTI-12` already required prevention | **Open.** Only implementation and verification can close it |
| `R4-F-07` | Available quantity display-clamped at zero | UNCHANGED | Open — Lane A, display contract |
| `R4-F-08` | Running balance ordering ambiguity | UNCHANGED | Open — Lane A, one of the seven available items |
| `R4-F-09` | Location company assignment optional | UNCHANGED by ruling; `MTI-08` already anchors it | **Open.** Implementation and verification |
| `R4-F-10` | Product category owns reporting, put-away **and costing** | **COMPLICATED, not narrowed.** `D-03` names Product Category as tenant-configurable while its costing facet is `GAP-FS-02`, precondition-blocked on `JT-01` (**NOT DECIDABLE**). A tenant-configurable object with a COGS-blocked facet is a new tension | **Open** — and see `RC-F-08` |
| `R4-F-11` | Nested reordering rule overlap **within** a company | UNCHANGED. `MTI-14` closed only the cross-company half; the rulings touch neither half | Open — Lane A |
| `R4-F-12` | Misparsed barcode yields wrong quantity | UNCHANGED. `D-03` names Barcode Nomenclature tenant-configurable, which **widens** the surface | Open — Lane A |
| `R4-F-13` | Upward conversion rounding inflates quantity | UNCHANGED. `D-03` names UoM Category tenant-configurable | Open — Lane A |
| `R4-F-14` | Planning run not reproducible without input snapshot | UNCHANGED. `MTI-32` already requires the snapshot | Open — Lane A |
| `R4-F-15` | Approval infrastructure is original design work | **NARROWED.** `D-02`'s operation-type axis gives approval a context to bind to; `L7-09` segregation becomes designable | Open — Lane A + C |
| `R4-F-16` | **Three handoff elements unsuppliable, none for COGS reasons** | **UNCHANGED — the finding stands in full.** Element 10 status unchanged; elements 14 and 15 unchanged; element 14's obligation widened | **Open. The programme critical path is still where `R4-F-16` put it** |
| `R4-F-17` | On-hand / reserved / incoming all depend on movement identity | UNCHANGED | Open — `RISK-C02`, severity ruling outstanding |
| `R4-F-18` | Internal-movement neutrality has no independent check | UNCHANGED | Open — one of the seven available items |
| `R4-F-19` | Every semantic reaches the user as an unvalidated Thai label | UNCHANGED. **The rulings introduce further unvalidated labels** — every configurable record class named in `D-03`, and every operation type named in `D-02` | Open — Lane C, `0 of 78` |
| `R4-F-20` | Retroactive compensation sequenced by creation order | UNCHANGED | Open — `L13-01`, value half `HOLD` |
| `R4-F-21` | Segregation model that cannot degrade will be bypassed | **NARROWED in shape, unchanged in substance.** `D-02` makes the model designable; it does not supply the degradation design, which needs Thai input | Open — Lane A + C, `MTI-F-05` |
| `R4-F-22` | Isolation must be proven on **derived** surfaces | UNCHANGED. `D-02` rule 7 restates the requirement for reports and views; Family D already specified it | Open — implementation |
| `R4-F-23` | Migrating legacy batch identities without company scope | **NARROWED.** `MTI-12` plus `D-01` make the target state unambiguous | Open — `GAP-FS-08` |
| `R4-F-24` | Location kind assigned by name-matching at migration | UNCHANGED. `MTI-42` covers context, not the financial-meaning attribute | Open — Lane A |
| `R4-F-25` | Quantity-side cutover certifiable independently of value — **opportunity** | **EXTENDED.** Under `D-01` the certification is naturally per company, which is what the invariant-set package already extended it to | **Available now** — Lane A |

**25 findings. 0 closed. 6 narrowed. 1 complicated. 18 unchanged.**

---

## 8. Impact On The Six `MTI-F-*` Findings

| ID | Subject | Transition | Post-Ruling Status |
|---|---|---|---|
| `MTI-F-01` | A traceable identity's bare value is not its identity | **REINFORCED.** `D-01` rule 2 states the same principle for product code, name, barcode and UoM. The two now share one governing rationale | Open — specification complete, verification needs implementation |
| `MTI-F-02` | Owner dimension is orthogonal to company | UNCHANGED | Open — value half `HOLD`, `GAP-MD-09` |
| `MTI-F-03` | Absence must not leak existence | **WIDENED.** Under `D-01`, per-company uniqueness is now the ruled norm for products as well as traceable identities, so the disclosure channel `MTI-27` guards against exists across a **larger** surface | Open — **larger scope than when raised** |
| `MTI-F-04` | Element 10 requires carriage **plus attestation** | **WIDENED.** `D-02` means the attestation must now cover warehouse and operation-type context, not company alone | Open — `AAS-V-01` in force |
| `MTI-F-05` | Approval routing may not cross a company boundary | **NARROWED in shape.** `D-02` supplies the operation-type axis the compensating control needs. The control content still needs Thai input | Open — Lane A + C |
| `MTI-F-06` | Context conservation across handoffs is unchecked | **WIDENED.** The conserved quantity is now a four-part context, not a two-part one | Open — count half specifiable, value half `HOLD` |

**6 findings. 0 closed. 2 narrowed. 3 widened. 1 unchanged.** Three findings got **larger** as a direct result of the rulings, because a wider control model has a wider surface to conserve, attest and not leak.

---

## 9. Items Newly Created By The Rulings

These did not exist before 2026-09-04 and exist because of the rulings. Each is a real obligation with no published design.

| ID | Item | Created By | Severity | Owner | Why It Is Not Covered By Any Existing Design |
|---|---|---|---|---|---|
| `RC-F-01` | **`MTI-11` contradicts `MTI-D-01`.** The canonical invariant set is out of conformance with its governing ruling | `D-01` | **BLOCKING for reliance on file `03`** | Inventory | The invariant set was published before the ruling. Its own status field anticipated revision; the revision has not been performed |
| `RC-F-02` | **`XCR-03` is eliminated.** The cross-context relationship register falls from 4 entries to 3, and `04` §4.1's shared-surface proof obligation for product is voided | `D-01` | MATERIAL — **favourable** | Inventory | A register whose completeness is the isolation claim must be corrected when an entry ceases to exist. This is a reduction in scope and is recorded so it is taken, not missed |
| `RC-F-03` | **The controlled mapping / provenance layer does not exist.** `D-01` rules 5 and 8 require an *"explicit controlled mapping layer"* before any cross-company or group-level product comparison or aggregation. **No published design in R4, the review or the invariant set specifies such an object** | `D-01` | **BLOCKING** for any group-level reporting | Inventory + Boss | The invariant set's nearest construct, `XCR-03`, was the tenant-level master reference — **and `D-01` eliminates it**. The mapping layer is a different object serving a different purpose, and it is unspecified |
| `RC-F-04` | **`D-01` is not fully operable until `MTI-D-04` is ruled.** Rules 5 and 8 presuppose an authorized aggregation mechanism; `MTI-D-04` (whether a sanctioned cross-company read exists) is exactly that mechanism, and is **unruled** | `D-01` | MATERIAL | Boss | `MTI-D-04` was ranked 6th in the invariant-set PMO recommendation and 8th in its Boss list. `D-01` promotes it into its own dependency chain |
| `RC-F-05` | **The execution family carries no operation-type axis.** `D-02` rule 8 requires background jobs and automation to carry explicit operation-type context. `MTI-29` and `MTI-30` specify single-`CTX` execution and authority carriage, but `CTX = (tenant, company, warehouse?, location?)` — **operation type is not in the tuple** | `D-02` | MATERIAL | Inventory + SaaS Foundation | The context tuple predates the ruling. `AUTH` and `CTX` are now different shapes, and the relationship between them is unspecified |
| `RC-F-06` | **The tenant-configurable enumeration is open-ended.** `D-03` names eleven record classes plus *"other approved Inventory configuration/master records"*. `L9-04`'s boundary-half acceptance criterion requires the enumeration to be *"published and **complete**"* | `D-03` | MATERIAL | Boss / product scope | An open-ended list cannot satisfy a completeness criterion. `L9-04` therefore stays `PARTIALLY DEFINABLE` |
| `RC-F-07` | **Private Company is a second isolation topology with no invariants.** All 50 invariants, all 35 matrix rows, all 8 L9 proofs and all 30 proof scenarios are written for the shared pool. **None states what changes, or does not change, inside a Private Company** | `D-03` | MATERIAL, trending BLOCKING | Boss + Inventory | The construct is introduced by the ruling and appears in no prior design document |
| `RC-F-08` | **Product Category is tenant-configurable and COGS-blocked at the same time.** `D-03` names it configurable; `R4-F-10` records that it owns reporting, put-away **and costing** in one concept; the costing split is `GAP-FS-02`, precondition-blocked on `JT-01`, which is **NOT DECIDABLE** | `D-03` × `R4-F-10` | MATERIAL | Inventory + Joint | Allowing tenant configuration of an object one of whose facets is COGS-blocked risks tenants configuring a facet no domain currently owns |

**8 new findings. All are consequences of the rulings, none is a challenge to them.**

---

## 10. Impact On Inherited Dependencies

| Dependency | Transition | Post-Ruling Status |
|---|---|---|
| `RISK-U03` / `GAP-FS-10` — the multi-tenant invariant capability | UNCHANGED | **OPEN.** The item is the capability. Rulings do not build |
| `RISK-U01` / `U-01` — warehouse/operation authorization scope | **RESOLVED AS DECISION** by `D-02` | Decision half **closed**. Build half open |
| `GAP-MD-14` / `SAAS-04` — provisioning template regeneration, switch-off guards, versioning | **PARTIALLY NARROWED** by `D-03` | Boundary half substantially supplied; **regeneration, switch-off and versioning mechanics unchanged** (`MTI-35`, `MTI-36` specify, nothing verifies) |
| `RISK-C02` / `IV-06` — movement attempt identity | UNCHANGED | **BLOCKING.** Severity ruling outstanding |
| `GAP-FS-08` / `CN-36` — migration and replay provenance reference | **SCOPE WIDENED** by `D-01` rule 7 | **BLOCKING**, and now larger |
| Privileged-bypass path audit | UNCHANGED | **BLOCKING** for `L9-01` |
| `JT-01` valuation policy owner — **NOT DECIDABLE** | UNCHANGED | **BLOCKING** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `JT-04`, `JT-05` — **NOT DECIDABLE** | UNCHANGED | **BLOCKING** |
| `JT-10` inter-company transfer treatment | **COMPLICATED by `D-01`.** Under Option B the two sides of an inter-company transfer are unrelated product identities, so the correlation `XCR-01` requires must be carried by the relationship, never inferred from product | **BLOCKING**, and harder |
| `GAP-FS-07` — cross-company transfer path never traced end to end | UNCHANGED | **BLOCKING** |
| `GAP-MD-09` — consignment and ownership policy | UNCHANGED | MATERIAL — value half `HOLD` |
| `GAP-MD-29` — PDPA scope, **zero coverage anywhere** | UNCHANGED | MATERIAL trending BLOCKING — `MTI-D-05` unruled |
| `GAP-FS-11` / `GAP-MD-30` — Thai validation `0 of 78` | **SURFACE WIDENED.** Every record class and operation type named in the rulings is a further unvalidated label | **BLOCKING** for user-facing design |
| `TH-HOLD-01` .. `TH-HOLD-09` | UNCHANGED. **`MTI-07`'s prohibition on equating a warehouse with a Thai tax branch survives `D-02` intact** — `D-02` makes warehouse an authorization axis, which is an operational concept, not a statutory one | `HOLD / EVIDENCE REQUIRED` |
| `C-05` clean-room containment — exposure confirmed live | UNCHANGED | **BLOCKING** for downstream reliance. This package inherits the lock |
| `U-07` two competing Council charters | UNCHANGED | **BLOCKING** for challenge finality. This package inherits the conditionality |
| `REV-F-01` depth shortfall; `REV-F-02` element 14 conditionality; `REV-F-03` lane collision; `REV-F-04` roll-up not reconstructable | UNCHANGED | All open |
| `C-04` / `N-CONC-01`, `N-A13-01` — two reachable leads | UNCHANGED | Open. **Not read by this session either** |
| `MTI-CH-01` `STORE` satisfiability; `MTI-CH-02` set not minimised; `MTI-CH-03` three scenarios unrunnable | UNCHANGED | Open |
| `MTI-D-04`, `MTI-D-05`, `MTI-D-06` | `MTI-D-04` **promoted** by `RC-F-04`; other two unchanged | All three **unruled** |

---

## 11. Roll-Up

| Measure | Result |
|---|---:|
| Decision blockers resolved as decisions | **3** |
| Upstream decisions discharged | **1** — `U-01` decision half |
| `R4-F-*` findings closed | **0** |
| `MTI-F-*` findings closed | **0** |
| `REV-F-*` findings closed | **0** |
| Inherited dependencies discharged | **0** |
| Findings narrowed | **8** |
| Findings widened by a ruling | **5** |
| Design constructs eliminated | **1** — `XCR-03` |
| Direct contradictions found | **1** — `RC-F-01` |
| New findings created by the rulings | **8** — `RC-F-01` .. `RC-F-08` |
| New decision items created | **4** — `RC-D-01` .. `RC-D-04`, at `09` |
| L9 proofs achieved | **0 of 8**, unchanged |
| Cross-proof scenarios verified | **0 of 22**, unchanged |
| Handoffs contract-compliant | **0 of 10**, unchanged |

**No open-item roll-up total is asserted by this session.** `REV-F-04` records that the 92 figure is not independently reconstructable and that no open-item crosswalk exists. The invariant-set session declined to assert a total for the same reason; this session declines on the same grounds. The twelve new items within this file's scope are enumerated exactly; the full set of fifteen, including `RC-F-09` and the two evidence notes, is at `09` §11.

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
