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
| **`GAP-INV-09B`** | **Transactional** reachability in the target generation | affects every behavioural finding | **OPEN** — no target-generation deployment carries stock |
| **`GAP-INV-17`** | The database artefact census was run **after** the deployments were chosen; 3 of 6 identities unexamined and a newer copy exists of both that were used | 3 of 6 identities; cloud storage unswept | **OPEN** |
| **`GAP-INV-18`** | A reference object binds Inventory documents to point-of-sale, purchase and sales documents, has no controls, no validations and no behaviours, and is hidden behind a technical-only group | 1 object | **OPEN — Identity is a Critical Area** |
| **`GAP-INV-19`** | The optional-function dimension is absent for the **32** menus that prior research covered | 32 menus | **OPEN — sized, not closed** |

### Findings

| Family | Range | Defined in |
|--------|-------|-----------|
| `FO-F-01` … `FO-F-06` | 6 | `00B_FUNCTIONAL_OWNERSHIP_MATRIX.md` |
| `RR-F-01` … `RR-F-06` | 6 | `00C_RUNTIME_REACHABILITY_MATRIX.md` |
| `RC-F-01` … `RC-F-03` | 3 | `00D_PRIOR_RESEARCH_RECONCILIATION_MATRIX.md` |
| `DR-F-01` … `DR-F-09` | 9 | `VDR_TARGETED_DELTA_RESEARCH_REPORT.md` |

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
