# P09_ANALYTIC_SEMANTIC_MODEL

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.
**Scope basis:** `SMEPLUS-26-09-04-ACC-REV2-CORR1` — every object below carries a declared owning scope.

---

## 1. WHAT ONE MANAGEMENT RECORD ASSERTS

The central semantic question of P09 is: **what business fact does one management record assert?**

In the reference pattern the answer is *not one thing*. The same record type, with the same fields and the same amount column, is written by at least three families of producer asserting three different facts:

| Family | The assertion | Financial event exists? | Evidence |
|---|---|---|---|
| **A — Allocation of a posted amount** | "this much of a posted ledger amount belongs to this dimension" | yes, and it is linked | EV-P09-103 |
| **B — Costed operational measurement** | "this much labour or machine time was consumed here, valued at a rate" | **no** | EV-P09-110, EV-P09-111 |
| **C — Estimated or valuation-derived cost** | "this much cost is expected or has been valued here" | sometimes — and the link is discarded when it exists | COR-P09-05 |

Family B is the sharpest case: an operational time entry **is** a management record in the reference pattern — there is no separate operational object — and it is valued at an hourly rate with no journal entry anywhere (EV-P09-110). A single hour of machine time can produce up to three management records, from three different modules, and zero journal items (EV-P09-111).

**SM-01 — Semantic determination.** SMEsPlus shall not merge these three assertions into one record type. The record shall declare its assertion class, and the class shall be immutable and part of the record's identity, not a mutable classification field.

**SM-02.** A record of family B is **Operational Measurement Truth (T3)**, not Management Dimension Truth (T2). It shall not aggregate with family A in any figure that is presented as accounting information without an explicit, per-figure marker.

## 2. THE IDENTITY OF A MANAGEMENT RECORD

The reference pattern's management record has **no business identity**: no document number, no event reference, no provenance carrier, no immutability, and no versioning. It is created, destroyed and re-created as a by-product of other objects' state changes:

- posting an entry creates the family-A records; resetting it to draft **destroys them** (EV-P09-104);
- changing the allocation on a posted entry **destroys and re-creates them** (EV-P09-103);
- cancelling a work order destroys the family-B records (EV-P09-111);
- changing a dimension value's axis **rewrites** them by direct statement (EV-P09-014);
- deleting an axis **removes the dimension entirely** from every historical record (EV-P09-011).

**SM-03 — Identity.** A management record shall carry an immutable identity and an immutable provenance reference. Correction shall be by a new, signed record, never by destruction and re-creation of the original.

**SM-04 — History.** Management history shall be append-only. No master-data operation — retiring an axis, re-parenting a value, correcting a name — shall alter a historical management record.

## 3. THE SEMANTIC TRACE, STEP BY STEP

The constitution's trace is evaluated below with the carrier that would hold each step in SMEsPlus, and the corresponding reference-pattern carrier where one exists.

| Step | The question it answers | SMEsPlus carrier (proposed) | Owning scope | Reference-pattern carrier | Status |
|---|---|---|---|---|---|
| 1 Business Source | which real-world act happened | source document identity, mandatory | COMPANY | producing-module fields, non-uniform | partial |
| 2 Financial Event | what the ledger recorded, as one identified event | accounting event identity | COMPANY | **none** | absent |
| 3 Dimension | which axes classify it | axis + value, tenant-owned data | TENANT (axis), TENANT/COMPANY (value) | axis as physical schema | present but mis-scoped |
| 4 Allocation | in what proportion | allocation record with referential integrity and a named residual | COMPANY | schemaless percentage payload | present, not integral |
| 5 Cost Object | what accountable thing bears it | first-class cost object | TENANT or COMPANY | **none** — inferred per module | absent |
| 6 Budget | what was intended | budget with declared scope and position | TENANT or COMPANY | budget header + line, no position | partial |
| 7 Actual | what occurred | stored, dated, scope-declared actual | COMPANY | recomputed at read time | present, unstable |
| 8 Management Report | what it means | report over T2 with provenance markers | declared per report | ledger-table shadowing | present, boundary-crossing |

**Three of eight steps have no carrier in the reference pattern (2, 5) or no stable one (7).** The semantic trace cannot be inherited; it must be authored.

## 4. THE DIMENSION SEMANTICS

### 4.1 An axis is a question, not a folder
An axis (cost centre, project, branch, product line) is a **question asked of every cost**. Its semantics are therefore: *is this question applicable here, and if so must it be answered?* The reference pattern expresses applicability and obligation through a scored rule set (EV-P09-033) whose outcome in tie cases depends on rule creation order.

**SM-05.** Applicability and obligation shall be deterministic, explainable per row, and answerable as data: for any management record, the system shall be able to state which rule made each axis mandatory or optional.

### 4.2 An axis value may be scoped more widely than the records that use it
Under the corrected constitution this is legitimate. A tenant-level cost-centre tree may be referenced by management records of several companies. What must never happen is the reverse inference — treating a widely-scoped **value** as licence to aggregate **records** across scopes implicitly (`P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` B-09).

**SM-06.** `OWNERSHIP ≠ AVAILABILITY` shall be represented explicitly: an axis value carries an owning scope **and** a separate availability rule. The reference pattern conflates the two into a single nullable field (§`P09_SCOPE_OWNERSHIP_MATRIX`).

### 4.3 The dimension set is finite and named at design time in the reference pattern
Because an axis is a physical column, the practical number of axes is bounded by schema tolerance rather than by business need, and adding one is a migration event (EV-P09-010).

**SM-07.** The number of axes shall be a tenant configuration decision with no schema consequence, and shall be bounded by an explicit, stated limit rather than by an implicit physical one.

## 5. THE AMOUNT SEMANTICS

| Property | Reference pattern | Evidence | SMEsPlus determination |
|---|---|---|---|
| currency | company currency only, derived, no transaction currency, no rate | EV-P09-026 | **SM-08** — carry transaction currency, rate and rate date, or declare single-currency explicitly |
| sign | inverse of the ledger; cost negative | EV-P09-031, EV-P09-053 | **SM-09** — declare the convention once at model level; every published equation states it |
| quantity | a separate untyped quantity with a unit of measure | — | **SM-10** — quantity and its unit shall be mandatory together or absent together |
| rounding | percentage rounded to a configurable precision, defaulted to two digits; amount is a rounded percentage of a rounded base | EV-P09-018 | **SM-11** — allocate by exact rational shares with a named residual, not by rounded percentages |
| zero splits | a split rounding to zero is silently dropped while still counting toward the total | EV-P09-106 | **SM-12** — a zero-valued allocation shall be recorded, not dropped, or the total shall be adjusted; silence is not permitted |
| residual | absorbed only when an axis reaches exactly 100 %; otherwise unrepresented | EV-P09-105 | **SM-13** — an unallocated remainder shall be a visible residual on a reserved value (see MA-05) |

## 6. THE SEMANTICS OF CHANGE

**SM-14 — The four change classes.** Management data changes for four distinct reasons and the reference pattern treats all four identically (destroy and re-create). SMEsPlus shall distinguish them:

| Class | Cause | Permitted treatment |
|---|---|---|
| K1 Correction of allocation | the original allocation was wrong | new signed reallocation record; original retained |
| K2 Correction of source | the financial event itself was wrong | driven by the financial correction; management record follows as a derived event |
| K3 Reclassification | the dimension structure changed | mapping record with an effective date; **historical records are not rewritten** |
| K4 Reversal | the event did not happen | reversal record; original retained |

**SM-15.** No change class shall be implemented as a delete. The reference pattern implements K1 as delete-and-recreate on a posted entry with no audit trace whatsoever (EV-P09-100, EV-P09-101, EV-P09-102, EV-P09-103) — see `P09_EDGE_CASE_MATRIX` EC-01.

## 7. TERMINAL STATE

**SEMANTIC DETERMINATIONS SM-01 … SM-15 ISSUED AS PROPOSALS — NO GATE MOVED.**
