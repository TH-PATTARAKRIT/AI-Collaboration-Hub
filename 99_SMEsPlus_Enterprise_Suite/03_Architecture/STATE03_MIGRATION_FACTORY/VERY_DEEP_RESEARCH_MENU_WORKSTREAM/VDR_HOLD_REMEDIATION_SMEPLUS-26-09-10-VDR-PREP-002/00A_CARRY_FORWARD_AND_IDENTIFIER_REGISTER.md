# 00A_CARRY_FORWARD_AND_IDENTIFIER_REGISTER.md
# Session carry-forward, and every identifier this package uses

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. Why this file exists

This session is a **controlled continuation**, so most identifiers it cites were **defined in the
prior package** and are inherited, not redefined. A package-scoped identifier sweep reports every one
of those as *cited but never defined*, which is correct for its unit and wrong as a conclusion.

**This register is the join.** It declares which identifiers are inherited, from where, and which are
new here — so that "cited but not defined in this package" can be distinguished from "undefined".

## 2. Evidence baseline inherited

| Attribute | Value |
|-----------|-------|
| Prior package | `VDR_PREPARATION_FRAMEWORK_SMEPLUS-26-09-10-VDR-PREP-001-CORR1/` |
| Prior commit | `5b3550c257c5d2eec41b430fe2730f11f0305914` |
| Prior manifest | 63 entries, 0 mismatches |
| Prior disposition | **HOLD** — 0 of 15 Critical Areas at 100% |
| Prior certification | **NONE — invalidated by `GOV-01`** |

**Prior findings are inherited as evidence. No prior finding is inherited as certified.**

## 3. Identifiers inherited from the prior package

| Family | Range | Defined in |
|--------|-------|-----------|
| `MM-F-nn` · `CD-F-nn` · `FT-F-nn` · `FN-F-nn` · `OD-F-nn` · `XM-F-nn` · `SS-F-nn` · `HA-F-nn` | all | the nine registers of the prior package |
| `EB-01` · `EB-02` | both | prior `00A_EVIDENCE_BASE_AND_PATH_SET.md` |
| `SR-01` … `SR-10` | all | prior `INVENTORY_PILOT_SOURCE_RESOLUTION_REPORT.md` |
| `CORR-F-01` … `CORR-F-30` | all | prior `VDR_FRAMEWORK_PILOT_CORRECTION_REGISTER.md` |
| `GAP-INV-01` … `GAP-INV-16` · `CRITICAL-GAP-01` … `-05` · `BOSS-DEC-01` … `-13` | all | prior `09_SMEPLUS_FIT_GAP_DECISION_REGISTER.md` |
| `GOV-01` | — | prior `INVENTORY_PILOT_CHALLENGE_REPORT.md` §2 |

### Inherited identifiers cited individually in this package

Cited by name here, defined in the prior package. Listed individually so that an identifier sweep
whose unit is *this* package can distinguish **inherited** from **undefined**.

| ID | What it is | Defined in |
|----|-----------|-----------|
| `CRITICAL-GAP-01` | the valuation object was replaced between generations | prior register 09 |
| `GAP-INV-09` | runtime evidence not established | prior register 09 |
| `GAP-INV-16` | eligibility: binding object is not functional ownership | prior register 09 |
| `SR-09` | reversibility of the write-off and teardown documents | prior source-resolution report |
| `SR-10` | census of menus that mutate data when opened | prior source-resolution report |
| `CORR-F-30` | the ownership rule was circular as sequenced | prior correction register |

## 4. Identifiers **defined by this session**

### Framework / instrument corrections

| ID | Defect | Effect if unrepaired | Where raised |
|----|--------|----------------------|--------------|
| **`CORR-F-31`** | Primary ownership of an object was first resolved by **alphabetical order** of its declaring modules | attributed the product object to a documents module and the unit-of-measure object to a point-of-sale module — **wrong owners for the two most-consumed shared objects** | `00B` §2 |
| **`CORR-F-32`** | A database extraction was truncated by a pipe that closed early; **584 rows returned of 34,164** | produced **0 of 62 menus present** — a clean, uniform, catastrophic false negative. Caught by a coverage assertion, not by inspection. **Third occurrence of this defect class in this programme.** | `00C` §2 |
| **`CORR-F-33`** | The Learning Item schema assumes every item has a **data object** | one Inventory menu is a device-management action with **no object at all** — invisible to the object-impact, ownership and data-impact registers by construction | `VDR_TARGETED_DELTA_RESEARCH_REPORT.md` `DR-F-09` |
| **`CORR-F-34`** | The clean-room scrub matched dotted identifier prefixes as bare substrings | reported a leak on the English sentence *"…real stock."* — the same false-positive class as matching a stem inside a longer ordinary word. Dotted prefixes now require a following identifier character | `PMO_FINAL_VERIFICATION_REPORT.md` §3 |

### Gaps

| ID | Gap | Size | Status |
|----|-----|------|--------|
| **`GAP-INV-09B`** | **WITHDRAWN** — it asserted that no target-generation deployment carries stock. One does. Replaced by `GAP-INV-09C` | — | **WITHDRAWN** |
| **`GAP-INV-17`** | The database artefact census was run **after** the deployments were chosen; 3 of 6 identities unexamined and a newer copy exists of both that were used | 3 of 6 identities; cloud storage unswept | **OPEN** |
| **`GAP-INV-18`** | A reference object binds Inventory documents to point-of-sale, purchase and sales documents, has no controls, no validations and no behaviours, and is hidden behind a technical-only group | 1 object | **OPEN — Identity is a Critical Area** |
| **`GAP-INV-19`** | The optional-function dimension is absent for the **32** menus that prior research covered | 32 menus | **OPEN — sized, not closed** |

### Findings

| Family | Range | Defined in |
|--------|-------|-----------|
| `FO-F-01` … `FO-F-07` | 7 | `00B_FUNCTIONAL_OWNERSHIP_MATRIX.md` |
| `RR-F-01` … `RR-F-09` | 9 | `00C_RUNTIME_REACHABILITY_MATRIX.md` |
| `RC-F-01` … `RC-F-03` | 3 | `00D_PRIOR_RESEARCH_RECONCILIATION_MATRIX.md` |
| `DR-F-01` … `DR-F-09` | 9 | `VDR_TARGETED_DELTA_RESEARCH_REPORT.md` |

### Instrument corrections added by the re-challenge round

| ID | Defect |
|----|--------|
| **`CORR-F-35`** | reachability and **use** were conflated; a fourth class `REACHABLE BUT UNUSED` is required — 40% of the object surface differs between them |
| **`CORR-F-36`** | a many-to-many relation lives in a **join table**; a column check on the parent cannot see it and returns a false zero |
| **`CORR-F-37`** | **a positive control drawn from the same vocabulary as the search term tests nothing.** It must be drawn from the corpus being searched. This single defect produced the round's largest retraction |
| **`CORR-F-38`** | the population register carries **one ordinal status per row** and cannot represent three independent dimensions; any three-dimension count over it is zero by construction |
| **`CORR-F-39`** | a **zero on one dimension beside a non-zero on another** is a contradiction, and no control was positioned to see it |
| **`CORR-F-40`** | a proxy validated at one granularity is **not** validated at a finer one — the module-installation inference holds for menus and fails for fields |
| **`CORR-F-41`** | a derived axis must publish **its token set and its scope**; executing the published wording literally disagreed on 11 of 96 rows |
| **`CORR-F-42`** | a flag derived from a set-membership test must **name the set** — a research boundary is not a deployment |
| **`CORR-F-43`** | an action comparison that reads only the domain cannot see **view overrides** |

### Gaps added by the re-challenge round

| ID | Gap | Status |
|----|-----|--------|
| **`GAP-INV-09C`** | transactional reachability in the target generation is **small-N** — one deployment, one configuration, no application server | OPEN |
| **`GAP-INV-20`** | the accounting-link column moves 77.2% → 0.0% between two *earlier* generations and is governed by configuration; **not interpreted** | OPEN |
| **`GAP-INV-21`** | the movement → accounting-entry link is **unobservable** in the target generation because every located deployment runs periodic valuation | OPEN |
| **`GAP-INV-22`** | *"no prior conclusion is contradicted"* was a **floor over an unstated set**; no population, pattern or unit was declared for that sweep | OPEN |
| **`CRITICAL-GAP-06`** | the reference object — **2nd most populated in the domain**, joining 91% of movements and 99.9% of sales orders, with no controls, no validations, no behaviours and no record rule, hidden behind a technical-only group, covered by no prior research | **OPEN — Identity is a Critical Area** |
| **`BOSS-DEC-14`** | is the quantity axis scoped to the **owning module** or **cross-module**? The answer decides whether the product master is a co-owned Inventory subject or an upstream one | **OPEN — Boss** |

### Individually-cited identifiers from other corpora

Cited by name in this package, defined elsewhere. Listed individually so an identifier sweep whose
unit is *this* package can tell **inherited** from **undefined**.

| ID | What it is | Defined in |
|----|-----------|-----------|
| `INV-M21` | prior menu study — operation types | prior deep-research corpus |
| `INV-M29` | prior menu study — the unit-of-measure **category** master, an object that does not exist in the target generation | " |
| `INV-F-26` | the capability-switch function — the evidence that refuted this session's `RC-F-01` | " |
| `INV-F-41` | the last function in the prior scope | " |
| `GAP-MD-14` | the prior corpus's own open gap on switch-off guards and versioning | " |
| `JT-12` | the last of the twelve joint accounting decisions | " |
| `IV-05` | immutability of a completed movement fact | " |
| `P-02` | corrections are new reversing facts, never edits | " |
| `P-07` | Inventory emits facts; Accounting decides postings | " |
| `MM-F-08` | a third-party module rewrites Inventory menu gates on install | prior VDR package |
| `OD-F-07` | the valuation figure is a writable column whose audit log is deletable | " |
| `RR-F-06` | retracted jointly with `RR-F-05` under a combined heading in `00C` | **this package** |

### Identifier families inherited from the prior **deep-research** corpus

The first version of this register declared inherited families from the prior *VDR* package only.
Re-challenge found four further families cited here and declared nowhere. They come from a **third**
corpus — the prior Inventory deep research — and are declared now:

| Family | Range | Corpus |
|--------|-------|--------|
| `INV-M01` … `INV-M29` | 29 menus | prior deep-research corpus |
| `INV-F-01` … `INV-F-41` | 41 functions | " |
| `JT-01` … `JT-12` | 12 joint decisions | " |
| `P-02`, `P-07`, `IV-05` | standing principles | " |

The package's own identifier sweep was **blind to these prefixes** and could not have reported them —
corrected in the sweep instrument.

## 5. Boss decisions this session supplies evidence for

| ID | Status after this session |
|----|---------------------------|
| `BOSS-DEC-01` — are prior valuation/COGS conclusions superseded; is series-19 the target? | **evidence now row-level and cross-generation** — see `00C` `RR-F-06`. Still **OPEN**. |
| `BOSS-DEC-02` — does the Inventory subject include the adjacent clusters? | **recommendation supplied with evidence** — `VDR_FUNCTIONAL_OWNERSHIP_RECONCILIATION_REPORT.md` §4. Still **OPEN**. |
| `BOSS-DEC-12` — binding object or functional ownership as the eligibility rule? | **live counter-example supplied** — the valuation-closing job. Still **OPEN**. |
| `BOSS-DEC-13` — must the Pilot be re-challenged from a clean freeze? | **partially addressed**: this session's own work is re-challenged from a clean freeze; the prior package is not. Still **OPEN**. |

## 6. Provisional status of the two candidate universal rules (§16)

| Rule | Status |
|------|--------|
| **STOP-AT-ONE-HOP** | **PROVISIONAL RESEARCH CONTROL.** Not frozen as a universal architecture rule. Evidence from one domain only. |
| **FUNCTIONAL-OWNERSHIP ELIGIBILITY** | **PROVISIONAL RESEARCH CONTROL.** Not frozen. This session supplies the first cross-cluster evidence for it — and a live counter-example against the alternative — but that is one domain, not the cross-module evidence §16 requires. |

Neither is proposed for universal adoption by this session.
