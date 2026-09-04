# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 06 — Product Identity Conformance Specification

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `MTI-11 AND DEPENDENTS RE-SPECIFIED TO A COMPANY ANCHOR — THE TENANT-LEVEL SHARED SURFACE IS ELIMINATED IN FULL — THE REPLACEMENT CONTROL REMAINS UNSPECIFIED`

---

## 1. The Specification, Stated Once

**A product is a company-owned business object.** Its definitional identity is anchored to `company` within `tenant`. Every operational and financial attachment is anchored to the same `company`. A variant follows its parent product.

**Two records in two companies that share a code, a name, a barcode, a unit of measure, a category, a route or a description are two different business objects.** The similarity never creates shared identity, and treating them as one is prohibited.

**Duplication is not a defect.** It is the expected and correct consequence of operational and legal separation per company. No design output, register, report, control, remediation or data-quality process in this programme may describe cross-tenant or cross-company product duplication as a defect, an anomaly, a data-quality issue, or something to be cleaned up.

---

## 2. Why — `L1`

Boss's stated reason governs interpretation and is recorded because a downstream reader who has only the rule will eventually apply it wrongly.

Two companies may perform what is described by the same words and mean two different things. The worked example in the ruling: Company A does transport business subject to a 1% withholding condition; Company B states it is hired transport service with no such condition. **The service description is nearly identical and the treatment is not.**

AAS+ advice `25` §2 enumerates the dimensions that may differ behind identical-looking names: tax treatment, withholding practice, product or service meaning, accounting mapping, approval path, route and rule policy, reporting requirement, and migration provenance.

**The operative principle: similarity of label is not evidence of identity of object.** Any rule in this file that could be read as collapsing two objects because they look alike is being read wrongly.

**No Thai statutory claim is made here.** The withholding example is recorded as Boss's stated business reason for a scope ruling, not as a statement of Thai tax law. Every `TH-HOLD-*` item remains held and routed to the Accounting-Tax track.

---

## 3. The Six Binding Identity Rules

Carried from the consolidation's `06` §3 unchanged, and each is now attached to the invariant that carries it in the conformed set.

| # | Rule | Source | Carried By |
|---:|---|---|---|
| `P-01` | Product definitional identity is anchored to `company` within `tenant` | `MTI-D-01` §1, rule 1 | `MTI-11` R2 |
| `P-02` | Code, name, barcode, UoM, category, route or description similarity **never** creates shared identity across tenants or companies | `MTI-D-01` rule 2; advice `25` §3.4 | `MTI-11` R2, `CF-I-06` |
| `P-03` | Cross-tenant deduplication is **not a requirement**. Cross-company deduplication is **not a default requirement** | `MTI-D-01` rules 3, 4 | `MTI-11` R2 |
| `P-04` | Cross-company or group-level comparison requires an **explicit controlled mapping / provenance layer** | `MTI-D-01` rule 5 | `CF-I-06`, `CF-XCR-GAP-01` |
| `P-05` | Every consuming module resolves product identity **through** tenant/company context, never by inference | `MTI-D-01` rule 6 | `MTI-45` R2, `07` |
| `P-06` | Migration **may preserve** duplicate products where that reflects source business reality; reporting aggregates **only after** an authorized mapping exists | `MTI-D-01` rules 7, 8 | `MTI-42`, `L10-04` R2 |

---

## 4. The Tenant-Level Shared Surface Is Eliminated In Full — `CF-F-01`

### 4.1 The enumeration, with its boundary

**Population:** the 35 numbered rows of `04_CONTEXT_OWNERSHIP_AND_VISIBILITY_MATRIX.md` at `dcb9227`.
**Pattern:** the `Anchor` column containing the token `tenant`.
**Path set:** that single file, on this branch, whose digest matches the package manifest.
**Unit:** one matrix row.

The file's own §4.1 states the same population independently — *"Entries 5, 7, 16 and 17 place definitional data at tenant level"* — which is the author's enumeration and it agrees with the mechanical one. Row 6 follows row 5 by construction, and row 2 (`Company`) is anchored to `tenant` by definition and is the boundary itself, not a shared surface.

| Row | Object | Published anchor | R2 anchor | Moved by |
|---:|---|---|---|---|
| 5 | Product (`CN-11`) | `tenant (definition) / company (attachment)` | **`company`** | `MTI-D-01` — `CD-04` |
| 6 | Product variant (`CN-12`) | its parent product | its parent product, now company-anchored | `MTI-D-01` — `CD-05` |
| 7 | Product category (`CN-08`) | `tenant (structure) / company (costing facet)` | **`company`**, both facets | `MTI-D-03` — `CD-12` |
| 16 | Barcode nomenclature (`CN-16`) | `tenant` | **`company`** | `MTI-D-03` — `CD-13` |
| 17 | Unit group and unit (`CN-14`) | `tenant` | **`company`**, subject to `CF-D-01` | `MTI-D-03` — `CD-14` |

### 4.2 The finding

**After conformance, no Inventory object class in the 35-row matrix remains anchored to `tenant` alone**, other than the `company` axis itself, which is anchored to `tenant` by definition. Subject to `CF-D-01`.

This is materially larger than `RC-F-02` states. `RC-F-02` records the elimination of one register entry and the voiding of `04` §4.1 *"for product and variant"*. The full position is that **`04` §4.1's subject — the class of tenant-level definitional data within Inventory — has no members left.**

Class **`A` within the boundary declared at §4.1**. Class **`B`** for the wider design corpus: this session enumerated the published context matrix, not every artifact in the programme, and other documents may anchor other objects to `tenant`.

### 4.3 The consequence, which is favourable and easy to under-claim

`04` §4.1 records that the tenant-level split *"creates a shared surface within a tenant that `MTI-02` protects across tenants but that nothing protects within a tenant — because within a tenant, sharing is the point."*

**That surface, and the proof obligation over it, cease to exist.** Concretely:

| Item | Effect |
|---|---|
| `04` §4.1's shared-surface proof obligation | **VOID in full** — `CD-15` |
| `XCR-03` | **ELIMINATED** — `CD-06`, `05` §3 |
| `L9-02` company isolation | **Simplified.** One whole class of legitimate cross-company reference disappears, so the proof has less to exclude. **Still `0 of 8` and still unproven** |
| `MTA-17` — *"a tenant-level master change hits every company at once"* | **Mechanism has no object left to act on.** `RE-SCORE BASIS` supplied at `CD-10`. **Not re-scored and not closed by this session** |
| `INV-F-17` — change stock-control classification while stock exists | Its published failure mode — *"applied tenant-wide while only one company's stock was considered"* — **ceases to be expressible.** The function's own destructive, one-directional character is unchanged |
| `INV-F-16` — create or amend a product | Its published failure mode — *"this writes tenant-level definitional data and company-level attachment in one act; the two halves need different barriers"* — **ceases to be expressible.** One object, one barrier |
| `R4-F-12` barcode misparse, `R4-F-13` conversion rounding | **Surfaces grow, not shrink.** Both classes become **per-company configurable**, so each behaviour must be proven per configured instance rather than once. Recorded, **not re-scored** |

**Two effects run in opposite directions and both are stated.** The isolation proof burden falls; the configuration proof burden rises. Reporting only the first would be a softening.

---

## 5. `MTI-11` And Its Dependents — The Complete Dependent Set

| Artifact | Published | R2 | Delta |
|---|---|---|---|
| `MTI-11` anchor | definitional identity anchored to `tenant` | **`company` within `tenant`** | `CD-01` |
| `MTI-11` enablement clause | *"a company may transact a product only where an explicit company enablement exists"* | **VOID** — ownership is the enablement | `CD-02` |
| `MTI-11` status / owner | `SPECIFIED — CONDITIONAL (MTI-D-01)`; `Inventory + Boss` | `SPECIFIED`; `Inventory` | `CD-03` |
| `04` row 5 | two anchors | **`company`** | `CD-04` |
| `04` row 6 | conditional on `MTI-D-01` and `GAP-FS-03` | conditional on **`GAP-FS-03` only** | `CD-05` |
| `04` row 7 | `tenant (structure) / company (costing facet)` | **`company`**, both facets; costing facet **HELD** | `CD-12` |
| `04` §4.1 | live proof obligation over a shared surface | **VOID in full** | `CD-07`, `CD-15` |
| `XCR-03` | register entry, conditional | **ELIMINATED**; register 4 → 3 | `CD-06` |
| `L8-01` Product identity | `tenant` for definition, `company` on attachment; immutable from creation **and** first enablement | **`company`**, single component; immutable **from creation** | `CD-08` |
| `L8-02` Variant identity | follows parent | follows parent, now company-anchored | `CD-08` |
| `L10-04` Product identity continuity | *"resolves to exactly one product; company enablements assigned explicitly"*; conditional | **resolves to exactly one product in exactly one company; deliberate duplication must be evidenced** | `CD-09` |
| `MTA-17` | `RESIDUAL: MATERIAL`, scored against Option A | `RE-SCORE BASIS` supplied | `CD-10` |
| `XCR-01` correlation | corroborated by a shared definitional identity | **carried entirely by the relationship**; never reconstructed from product attributes | `CD-11` |
| Handoff element 8 | *"suppliable but not unique"*, strengthened to a resolved tuple | **simplified** — the product half is company-resolved by construction | `CD-32` |
| `MTI-40` anchor-change list | includes *"a product's company enablement"* | that member **removed**; configuration anchors added | `CD-02`, `CD-12`-`CD-14` |
| `MTI-16` costing attachment | company-scoped | **unchanged.** Already correct under either option | — |
| `MTI-12` traceable identity tuple | `(tenant, company, product, value)` | **unchanged**, and now over-determined rather than under-determined | — |

**Seventeen dependents. Fourteen change. Two are unchanged and are recorded as unchanged so that a reader does not assume a change that did not occur. One — `MTA-17` — receives a re-score basis and is not re-scored.**

---

## 6. The Control That Replaced Deduplication — And Has Not Been Supplied

### 6.1 The cost the ruling knowingly accepts

The invariant set's own statement of Option B's cost is exact and is not softened here:

> *"the same physical item exists as several unrelated identities within one tenant; inter-company transfer loses its natural correlation; Thai SME groups that operate several companies over one catalogue would maintain duplicate masters, **which the L8 evidence names as a live source of identity failure**."*

Boss ruled with that cost visible and the ruling is authoritative. **This session does not re-argue it.**

### 6.2 The control consequence, restated at design level

**Deduplication is no longer available as a control against identity failure, because deduplication is now prohibited as a default. The identity-failure mode does not disappear because the remedy was ruled out.**

The failure mode is operational, not structural: an actor in Company A selects the wrong product because two company catalogues that were once one have drifted; a group-level report is assembled by hand from two catalogues that no longer correspond; a migration produces two products where the source had one, or one where the source had two, and nothing afterwards can tell which.

`MTI-D-01` rules 5 and 8 name the replacement — an **explicit controlled mapping / provenance layer**. **That object is not specified in any of the four packages this session read** — R4 at `fc0b168`, the review at `e218e5b`, the invariant set at `dcb9227`, the consolidation at `a57bd55`; carried as `RC-F-03`, which states the same for the first three. Class **`A` within that path set**; class **`B`** for the wider programme, it is gated on `MTI-D-04` which is unruled (`RC-F-04`), and its ownership and commissioning are `RC-D-04`, also unruled.

### 6.3 What is therefore true today

| Statement | Position |
|---|---|
| Is duplication prohibited? | **No.** It is legitimate and expected |
| Is deduplication available as a control? | **No.** Prohibited as a default by `MTI-D-01` rules 3, 4 |
| Does a replacement control exist? | **No.** `RC-F-03` |
| May one be specified now? | **No.** Gated on `MTI-D-04` — `RC-F-04`, Lane R3 `NOT AVAILABLE` |
| What holds in the meantime? | **`CF-I-06`** — a prohibition. No correspondence exists, and none may be created, asserted, inferred or relied upon |
| Is the identity-failure exposure thereby controlled? | **No.** A prohibition prevents an unauthorized correspondence; it does not prevent an operator picking the wrong product. **The exposure is uncontrolled and is stated as uncontrolled** |
| Whose decision is the remedy? | **Boss.** Options at `11` §3, `CF-D-03`. **Stated, never chosen** |

### 6.4 The ten required properties, carried unchanged

`M-01` .. `M-10` at the consolidation's `06` §5.3 are carried **verbatim in effect and not restated**, for the transcription reason at `03` §1.1. They are requirements, not a design. **Treating the mapping layer as designed because its properties are enumerated is prohibited** — the consolidation's own prohibition 8, carried.

`M-08` is load-bearing here: **the layer carries no valuation content while the COGS Gap stands** — `AAS-V-03`, in force.

---

## 7. The Disclosure Channel Under Option B

`MTI-27` requires that **absence must not leak existence**. `MTI-F-03` raised it because `MTI-12` made traceable-identity uniqueness per-company. **`MTI-D-01` extends the same condition to products, categories, nomenclatures and unit groups** — every class `CD-04` .. `CD-14` moves to a company anchor.

The channels, carried and extended:

| # | Channel | Under Option B |
|---:|---|---|
| 1 | Uniqueness feedback on create or amend | A user in Company A entering a product code in use in Company B must receive a response **indistinguishable** from the value being unused |
| 2 | Autocomplete and suggestion | Zero results, indistinguishable from non-existence |
| 3 | Barcode resolution | Resolves nothing outside the caller's `AUTH` set |
| 4 | Error text, code, timing and shape | **Identical** whether the target exists elsewhere or does not exist at all — `N-03` |
| 5 | Identifier-collision messages | As channel 1 |
| 6 | Import validation responses | Row-level rejection that discloses nothing about another company's data |
| 7 | Export scoping | As `MTI-26` R2 |
| 8 | **Category, nomenclature and unit-group naming** — **new under `CD-12` .. `CD-14`** | The same three classes become per-company, so each acquires the same disclosure channel a product code has |

**`MTI-F-03`'s scope is larger than when it was raised, and it was raised as `MATERIAL`. It is not re-scored here** — severity classification of another session's finding is not this session's act. The widening is recorded so that whoever re-scores it does so with this in hand.

---

## 8. Migration And Historical Continuity Under Option B — `L10`

| Requirement | Consequence |
|---|---|
| `MTI-D-01` rule 7 — migration **may preserve** duplicate products where that reflects source business reality | Migration must be able to produce duplicates **deliberately**, and must be able to **evidence** that the duplication was deliberate rather than a fault. That evidence is provenance, and provenance is `GAP-FS-08`, **which does not exist** |
| `L10-04` R2 | A legacy product resolves to exactly one product in exactly one company. Where the source reality is one catalogue item operated by two companies, migration produces **two** products and records that it did so on purpose |
| `MTI-42` — context is never **inferred** at migration | A migration assigning company by name-matching a product across source systems would violate `MTI-42` **and** `P-02` at once. `R4-F-24` records exactly this failure mode for location kinds, and it is unaddressed for the kind half |
| `R4-F-23` — migrating legacy batch identities without company scope | **Narrowed in target state, unchanged as a finding.** `MTI-12` plus `P-01` make the target unambiguous. Only implementation and verification close it |
| Handoff element 14 | **Obligation widened.** The provenance reference must now evidence deliberate duplication, not only batch membership. `REV-F-02` still governs its **conditionality**: element 14 is contractually required on migration, replay and recovery handoffs, not on all ten |
| `L10-07` cutover reconciliation | **Naturally per company under Option B**, which is what `R4-F-25` and `09` §6.1 of the invariant set already extended it to. Quantity half certifiable now; **value half held** |

**Net effect on `GAP-FS-08`: unchanged in status, larger in scope.** It was `BLOCKING`; it remains `BLOCKING` and now has more to evidence.

---

## 9. Prohibitions

Carried from the consolidation's `06` §9 and extended by this session's two additions, because the most likely failure mode of this policy is a well-intentioned optimisation.

| # | Prohibited | Why |
|---:|---|---|
| 1 | Merging, linking or correlating products by code, name, barcode, UoM, category or description similarity | `P-02`. The ruling's central prohibition |
| 2 | Reporting duplicate products across companies as a data-quality defect, anomaly or cleanup candidate | `MTI-D-01` §1, rule 3, and the required carry-forward wording |
| 3 | Building a de facto shared master under another name — a *golden record*, a *canonical product*, a *master mapping table* everything routes through | `M-10`; `MTI-D-01` §1 |
| 4 | Aggregating across companies before an authorized mapping exists | `MTI-D-01` rule 8; `MTI-24` |
| 5 | Carrying valuation content across a mapping while the COGS Gap stands | `AAS-V-03` |
| 6 | Inferring company from product at any point in any module | `P-05`, `MTI-42`, `R-03` at `04` §3 |
| 7 | Recording `MTI-11` as satisfied, or product isolation as proven, on the basis of this file | Nothing here is built or verified |
| 8 | Treating the mapping layer as designed because its properties are enumerated | `RC-F-03`. Requirements are not a design |
| **9** | **Extending the same treatment to categories, nomenclatures or unit groups — that is, deduplicating *configuration* across companies** | **New.** `CD-12` .. `CD-14` make these company-owned; AAS+ advice `29` §3 states directly that duplicated configuration across companies is not a defect. The prohibition that protects products protects these too |
| **10** | **Reading `CF-I-06` as a specification of the mapping layer, or as a decision that no mapping layer will exist** | **New.** It is a prohibition in the object's absence. `MTI-D-04` and `RC-D-04` are unruled, and both readings would pre-empt Boss |

---

## 10. Specification Status

| Dimension | Status |
|---|---|
| Ruled by Boss | **Yes** — `MTI-D-01`, Option B |
| `MTI-11` and dependents re-specified | **Yes** — 17 dependents assessed, 14 changed |
| The tenant-level shared surface | **Eliminated in full**, subject to `CF-D-01` — `CF-F-01` |
| Published design now conforms | **This document is the conformance. Whether it is correct is not established by this document** — `RC-V-01` is discharged by an independent check, not by the re-specification |
| Replacement control for identity failure | **Not designed** — `RC-F-03`, gated on `MTI-D-04` |
| Replacement control operable once designed | **Not yet** — `RC-F-04` |
| Migration able to evidence deliberate duplication | **No** — `GAP-FS-08` |
| Any product isolation property proven | **No** — `L9-02` `DEFINABLE`, `0 of 8` |
| Thai-validated | **No** — `0 of 78` |
| Valuation consequences stated | **No** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

`DECIDED BY BOSS — RE-SPECIFIED, NOT BUILT, NOT VERIFIED — REPLACEMENT CONTROL UNSPECIFIED`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
