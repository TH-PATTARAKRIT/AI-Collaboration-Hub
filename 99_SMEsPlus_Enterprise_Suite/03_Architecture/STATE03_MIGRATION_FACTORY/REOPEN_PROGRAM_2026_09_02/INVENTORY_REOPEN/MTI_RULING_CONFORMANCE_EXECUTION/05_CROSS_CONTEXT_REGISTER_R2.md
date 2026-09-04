# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 05 — Cross-Context Relationship Register R2

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `REGISTER FALLS FROM 4 ENTRIES TO 3 — 1 INCOMPLETE, 2 CONDITIONAL, 0 UNCONDITIONALLY SETTLED — 1 REQUIRED RELATIONSHIP CLASS UNSPECIFIED — COMPLETENESS NOT CERTIFIABLE`

---

## 1. Why This Register Is The Isolation Claim

`MTI-22` makes this register **the only permitted means** by which anything in one company may reference or affect anything in another. Everything else in the invariant set states a prohibition; this register states the exhaustive list of exceptions.

**An isolation design fails in practice not because the wall is weak but because the doors are undocumented.** The value of `MTI-22` is that the isolation claim becomes a claim about a finite, inspectable list — and a claim about a list is only as good as the list's completeness.

That is why `XCR-03`'s elimination has to be recorded rather than left implicit. **A completeness claim over a register must be corrected when an entry ceases to exist**, or the claim is being made over a list that no longer describes the system.

---

## 2. What Changed

| | Published at `dcb9227` | R2 |
|---|---:|---:|
| Entries | **4** | **3** |
| Entries `INCOMPLETE` | 1 | **1** |
| Entries `SPECIFIED — CONDITIONAL` | 3 | **2** |
| Entries unconditionally settled | **0** | **0** |
| Entries carrying an `AUTH` statement | **0** | **3** |
| Required relationship classes with no entry | 0 | **1** — `CF-XCR-GAP-01` |

`XCR-03` — *tenant-level definitional master reference* — is **eliminated** by `CD-06`. Under `MTI-D-01` there is no tenant-level definitional master for a company-scoped record to reference, so the relationship it described has no referent.

**Every surviving entry additionally acquires an `AUTH` statement**, because `MTI-D-02` makes traversal an authorization question and not only a context question: a door that is documented but whose key-holders are not is a door in an unstated state.

---

## 3. The Register — R2

### `XCR-01` — Inter-company transfer

| Field | Content |
|---|---|
| **Relationship** | Inter-company transfer (`HO-22`) |
| **Direction** | Company A → Company B, **paired** |
| **Permitted effect** | **Two single-context facts, one per company, correlated by a shared relationship identity. Never one fact spanning two companies** (`MTI-15`, `MTI-44`) |
| **`AUTH` required to traverse** | **Two separate `AUTH` entries, one per side.** An actor authorized in Company A's despatching warehouse and operation type is **not** thereby authorized in Company B's receiving warehouse or operation type. `CF-I-01` forbids a single broadened entry spanning both |
| **Evidence obligation** | Both facts carry `HF-CTX-07` naming this entry and the correlation identity; both carry `HF-CTX-10` and `HF-CTX-11`; the correlation is carried **only** by the relationship |
| **`MTI-D-01` consequence — `CD-11`** | Under a tenant-level master the two sides would have shared a definitional identity, giving the pairing a natural corroboration. **Under Option B they are two unrelated product identities.** The correlation is therefore load-bearing where it was previously corroborated, and it may **never** be reconstructed by matching product code, name, barcode, UoM or description — `MTI-D-01` rule 2 prohibits exactly that |
| **Status** | **`INCOMPLETE`** — `JT-10` open; path recorded as **never traced end to end** (`GAP-FS-07`) |
| **Valuation** | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.** No treatment, basis or recognition statement is made here |

### `XCR-02` — Cross-Context Report Grant

| Field | Content |
|---|---|
| **Relationship** | Cross-Context Report Grant (`MTI-25`) |
| **Direction** | **Read only, within one tenant.** Never crosses a tenant boundary under any circumstance |
| **Permitted effect** | Aggregate read across an enumerated company set. **No write. No valuation content while the COGS Gap stands** |
| **`AUTH` required to traverse** | The grant is itself an `AUTH` entry over an enumerated company set, and **it does not widen the warehouse or operation-type axes of any company it names.** A grant that let a warehouse-scoped actor read a whole company would substitute one axis for another, which `CF-I-01` forbids |
| **Evidence obligation** | Grant identity, granting authority, scope, expiry, and a log entry per use |
| **Status** | **`SPECIFIED — CONDITIONAL (MTI-D-04)`** — unchanged and **still unruled** |
| **Residual** | `MTA-11`: **every grant mechanism degrades toward permanence.** No governance review cadence is designed here or anywhere |
| **Veto** | **`AAS-V-03` in force.** No grant may carry valuation content while the Accounting COGS Gap stands. `JT-01` **NOT DECIDABLE**; `GAP-FS-07` path never traced |

### `XCR-04` — Platform template instantiation

| Field | Content |
|---|---|
| **Relationship** | Platform template instantiation (`MTI-35`) |
| **Direction** | Platform → tenant, **at provisioning only** |
| **Permitted effect** | Copy, recording the template version. **Never a live link; a later template change never propagates** |
| **`AUTH` required to traverse** | A provisioning authority, which is a platform authority and not any tenant's `AUTH`. **No tenant `AUTH` traverses this relationship in either direction**, and a tenant may not invoke instantiation for itself |
| **Evidence obligation** | The instantiated record names the template version copied |
| **`MTI-D-03` consequence — `CD-17`** | The **mechanism** conditionality is discharged: `MTI-D-03` supplies the boundary. The **content** is not: §3 of the ruling ends with *"other approved Inventory configuration/master records"*, so the set of classes this relationship instantiates is open-ended — `RC-F-06` |
| **Status** | **`SPECIFIED`, bounded by `RC-F-06`.** `L9-04`'s boundary half stays `PARTIALLY DEFINABLE`; `RC-D-02` stays unruled |

### `XCR-03` — **ELIMINATED**

| Field | Content |
|---|---|
| **Was** | Tenant-level definitional master reference (`MTI-11`), read only within one tenant. *"A company-scoped record may reference tenant-level definitional data. Carries no quantity, value, policy attachment or history"* |
| **Eliminated by** | `MTI-D-01` — Option B. There is no tenant-level definitional master |
| **Consequence** | **Favourable.** The relationship needed an isolation proof of its own and no longer does. `04` §4.1's shared-surface proof obligation is void with it — and void **in full**, not only for product, once `CD-12` .. `CD-14` are applied. See `06` §4 |
| **Recorded as** | `RC-F-02`, extended by `CF-F-01` |
| **Retained here** | As a **struck entry with its reason**, not as an entry. A register that silently drops a member cannot be audited against its own history |

---

## 4. The Relationship Class With No Entry — `CF-XCR-GAP-01`

**This is deliberately not numbered `XCR-05`.** Giving it an entry number would place an unspecified object in a register whose completeness is the isolation claim, and a register with an entry that does not describe anything is worse than a register with three.

| Field | Content |
|---|---|
| **Required relationship** | Controlled product mapping / provenance correspondence between companies |
| **Required by** | `MTI-D-01` rule 5 — *"any cross-company or group-level comparison must use an explicit controlled mapping layer"* — and rule 8 — *"reporting may aggregate only after an explicit authorized mapping exists"* |
| **Specified by** | **Nothing.** `RC-F-03`: no published design in R4, the review, the invariant set or the consolidation specifies such an object. The nearest published construct was `XCR-03`, **which this ruling eliminates**, and which served the opposite purpose: `XCR-03` let a company-scoped record *reference* a shared definition; a mapping layer asserts a *correspondence* between records that remain separate |
| **Gated on** | `MTI-D-04`, **unruled**. `RC-F-04`: properties `M-04`, `M-08` and `M-09` of the required object are the properties of `XCR-02`, whose existence is `MTI-D-04`'s subject. Specifying the mechanism before the authorization would design the door before deciding whether there is one |
| **Ownership and commissioning** | `RC-D-04`, **unruled** |
| **Present effect** | **`CF-I-06`.** Until the object is specified and authorized, **no cross-company correspondence exists**, and no process, report, export, migration or maintenance path may create, assert, infer or rely on one. This is a prohibition in the object's absence. **It is not a specification of the object and must not be read as one** |
| **Proof consequence** | `RC-P-20` and `RC-P-21` remain **`NOT DEFINABLE`** — the only two requirements in the chain that cannot be stated as propositions at all. See `10` §3 |
| **Register consequence** | **The register cannot be certified complete.** A relationship the governing ruling requires has no entry, so a completeness claim over three entries would be a claim that the system has three doors when the ruling requires a fourth to exist |

---

## 5. Completeness Position

| Question | Answer |
|---|---|
| Is the register complete as a list of relationships that **exist**? | **Yes, as far as this session's boundary reaches.** Three entries, one struck with its reason |
| Is the register complete as a list of relationships the rulings **require**? | **No.** `CF-XCR-GAP-01` |
| May the register be certified complete today? | **No** |
| What would make it certifiable? | Either `MTI-D-04` ruled and the mapping layer specified and entered, **or** a Boss ruling that no cross-company product correspondence exists — in which case `CF-I-06`'s prohibition becomes permanent and the register is complete at three |
| Is any entry proven? | **No. `0 of 3`.** No implementation exists |
| Is any entry unconditionally settled? | **No.** `XCR-01` `INCOMPLETE`; `XCR-02` conditional on `MTI-D-04`; `XCR-04` bounded by `RC-F-06` |

**Ruling `MTI-D-04` "no such grant exists" is a perfectly good ruling and would settle two of the three conditionalities at once.** Leaving it unruled is not neutral: `MTA-09` records that the group-view need is then met by **export**, and under Option B a Thai SME group maintains several catalogues instead of one, so the need is **larger**, not smaller.

---

## 6. What This Register Does Not Do

| Not done | Why |
|---|---|
| It does not specify the mapping / provenance layer | `RC-F-03`, gated on `MTI-D-04`. `CF-I-06` is a prohibition, not a design |
| It does not rule `MTI-D-04`, `RC-D-04` or `CF-D-01` | Boss decisions. Options at `11` §3, **never chosen** |
| It does not state any inter-company transfer treatment, basis or recognition | `JT-10` open; `GAP-FS-07` path never traced; `JT-01` **NOT DECIDABLE**. **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| It does not design a grant review cadence | `MTA-11` residual `MATERIAL`, carried unchanged |
| It does not state what any relationship does inside a Private Company | `RC-F-07`; `CF-I-08` scopes the whole register to the shared pool |
| It does not close `RC-F-02`, `RC-F-03` or `RC-F-04` | A correction to a register is not a closure of the finding that required it |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
