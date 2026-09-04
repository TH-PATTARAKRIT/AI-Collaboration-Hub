# P09_MANAGEMENT_ACCOUNTING_MODEL

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers `EV-P09-nnn` / `COR-P09-nn` resolve in the Layer 2 quarantine.

---

## 1. SCOPE OF THE MODEL

Management accounting in SMEsPlus is the layer that answers *where did the money go and who is accountable*, over a financial ledger that answers *what happened and what is owed*. This document states the model at the level of objects and their obligations; the semantics of a single management record are in `P09_ANALYTIC_SEMANTIC_MODEL`, and the boundary rules are in `P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY`.

## 2. THE OBJECT SET

| # | Object | Purpose | Reference-pattern equivalent found? | Key evidence |
|---|---|---|---|---|
| O1 | **Dimension type** (analytic plan) | declares an axis of management analysis, e.g. cost centre, project, branch | yes — but as **database schema**, not data | EV-P09-010 |
| O2 | **Dimension value** (analytic account) | one member of an axis | yes | EV-P09-027 |
| O3 | **Assignment rule** (distribution model) | pre-fills an allocation from master data | yes | EV-P09-021..024 |
| O4 | **Obligation rule** (applicability) | declares whether an axis is optional / mandatory / unavailable, per company and business domain | yes — resolved by a floating-point score | EV-P09-033..036 |
| O5 | **Allocation** (distribution) | the percentage map attached to a costed row | yes — as a schemaless JSON payload | EV-P09-016 |
| O6 | **Management record** (analytic line) | one costed assertion against one set of dimension values | yes | EV-P09-025 |
| O7 | **Cost object** | the accountable thing a cost lands on | **no first-class object** — see `P09_COST_OBJECT_MODEL` | COR-P09-04 |
| O8 | **Budget** | an intended amount per dimension and period | yes | EV-P09-060 |
| O9 | **Budgetary position** | the account grouping a budget is stated against | **not found** — class B | EV-P09-060 |
| O10 | **Budget control** | a gate that refuses commitment or posting beyond budget | **not found in the budget modules** — class A within that scope | EV-P09-065 |
| O11 | **Allocation-to-ledger mechanism** (automatic transfer) | periodic reallocation that posts | yes — and it posts | EV-P09-040 |
| O12 | **Management report surface** | the presentation of O6 aggregates | yes — implemented by shadowing the ledger table | EV-P09-050 |

**Two of the twelve objects the process needs do not exist in the reference pattern (O7, O9) and one exists only as display (O10).** These are the three places where SMEsPlus has no precedent to learn from and must design.

## 3. THE MODEL'S LOAD-BEARING DEFECT IN THE REFERENCE PATTERN

**The dimension type (O1) is schema, not data.**

Creating a dimension type performs data-definition work on a shared table: a column and an index are created for it. Deleting a dimension type removes that column, and every historical value recorded in that dimension goes with it. Moving a dimension value between types rewrites history by a direct statement outside the ordinary write path, with no log, no tracking and no confirmation beyond a collision check (EV-P09-010, EV-P09-011, EV-P09-014, EV-P09-015).

All of this is reachable from a **single, hidden, undifferentiated permission group** that carries create and delete on every analytic object (EV-P09-012).

Four consequences follow directly:

1. **The dimension set is not tenant data.** In a multi-tenant deployment the axis structure is a property of the database, shared by every tenant. One tenant's decision to add a cost-centre axis is a schema change for all.
2. **Management history is destructible by an ordinary administrative act.** Deleting an axis is a delete of a configuration record in the user interface and a data loss in the database.
3. **Management history is silently mutable.** Re-parenting an axis moves prior-period values with no audit record.
4. **There is no separation of duties.** The right to read management data is the right to destroy its structure.

**SMEsPlus position MA-01:** the dimension type shall be tenant-scoped data, not schema. Adding, renaming, re-parenting or retiring an axis shall be a versioned data operation with an audit record, and shall never alter the physical shape of a shared table.

**SMEsPlus position MA-02:** the analytic surface shall have at least three permission tiers — read, assign, and administer — and axis lifecycle operations shall sit in the third tier alone.

**SMEsPlus position MA-03:** an axis shall be retirable but not deletable once any record references it. Retirement shall preserve every historical value.

## 4. THE OBLIGATION MODEL

Whether a dimension must be filled is decided, in the reference pattern, by scoring candidate rules: half a point for a company match, one point for a business-domain match, minus one for a mismatch; highest strictly-greater score wins; ties keep the incumbent (EV-P09-033). A rule with no company applies to every company (EV-P09-034). The default is stored per company outside the axis record (EV-P09-035). At base level the business-domain vocabulary has exactly one value (EV-P09-036).

**Assessment:** a mandatory-field policy is a control. This control is a heuristic whose outcome depends on rule creation order in tie cases and on a magic constant. It is not explainable to an auditor.

**SMEsPlus position MA-04:** the obligation of a dimension shall be a deterministic function of an explicitly ordered rule set, and the system shall be able to answer, for any given row, *which rule made this dimension mandatory* — as data, not as a recomputation.

## 5. THE ALLOCATION MODEL

The allocation is a percentage map. It is not required to total 100 % except where the axis is mandatory **and** the caller has opted in to validation by execution context; there is no model-level or storage-level constraint (EV-P09-017). Percentages are rounded to a configurable precision, defaulted to two digits (EV-P09-018). A residual is absorbed only when an axis's allocation reaches exactly 100 %; where it never does, the unallocated remainder simply has no management representation (EV-P09-105). Splits that round to zero are dropped while still counting toward the total (EV-P09-106).

**SMEsPlus position MA-05:** an allocation shall be complete or explicitly declared partial. Where partial, the unallocated remainder shall be a **named, visible residual** carried on a reserved dimension value, never an absence.

**SMEsPlus position MA-06:** the sum-to-whole rule shall be enforced by the storage layer for every axis, mandatory or not, and shall not be defeatable by an execution-context flag.

**SMEsPlus position MA-07:** allocation shall be expressed in a form that carries referential integrity. The reference pattern's schemaless payload has no foreign key and expects dangling references as a normal state (EV-P09-016).

## 6. THE SCOPE MODEL

> **Revalidated under `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction).** This section previously asserted a blanket tenant-and-company requirement. That assertion was over-constrained and is superseded here. The underlying evidence is unchanged; the interpretation is re-derived from scope semantics. The full revalidation record is in `P09_REVISION_LOG` §R1 and the object-by-object determination is in `P09_SCOPE_OWNERSHIP_MATRIX`.

Every analytic object is first assigned an **owning scope** — PLATFORM, TENANT or COMPANY — and only then is a context requirement derived from it. Context is not added by default.

| Object | Company field in the reference pattern | Evidence | SMEsPlus owning scope (proposed) | Context required |
|---|---|---|---|---|
| Dimension type (O1) | **none — the object has no company field at all** | COR-P09-03 | **TENANT** — an analysis axis is a tenant's own management policy, carries no financial effect and is not a legal artefact | tenant mandatory, company not required |
| Dimension value (O2) | optional; empty means visible to every company | EV-P09-027, EV-P09-028 | **TENANT by default, COMPANY where the value denotes a legal-entity-specific object** | tenant mandatory; company mandatory only for the COMPANY-scoped subset |
| Management record (O6) | required, immutable, strictly scoped | EV-P09-027, EV-P09-028 | **COMPANY** — it carries an amount attributable to a legal entity | tenant + company mandatory |
| Assignment rule (O3) | optional; empty matches every company, and every other selector treats empty as a wildcard | EV-P09-021, EV-P09-115 | **TENANT**, with an optional company restriction as a *selector*, not as ownership | tenant mandatory; company optional and explicit |
| Obligation rule (O4) | optional; empty applies to every company | EV-P09-034 | **TENANT**, company-qualified where the obligation is a legal-entity policy | tenant mandatory; company optional and explicit |
| Budget (O8) | optional; empty visible to every company | EV-P09-070 | **TENANT or COMPANY — determined by whether the budget governs a legal entity's result**; a group-level management budget is TENANT, a statutory-entity budget is COMPANY | determined per budget, declared on the record |
| Allocation-to-ledger mechanism (O11) | company derived from the destination journal | EV-P09-049 | **COMPANY** — it produces a financial effect | tenant + company mandatory |

**What the evidence does and does not show.** The reference pattern's empty-company values are *not*, by themselves, evidence of a boundary defect: an empty company on a dimension type or an assignment rule is consistent with a legitimately non-company-scoped object. What the evidence does show is that the reference pattern **has no scope declaration at all** — there is no field, flag or model distinction that says which scope owns an object. Emptiness is used to mean "applies to all", and the same emptiness is used on objects of genuinely different scope. The defect is the **absence of an explicit scope**, not the presence of a null company.

Two consequences survive the correction unchanged, because neither depends on the superseded assumption:

1. **The dimension type is not scoped to anything at all** (COR-P09-03). It has no company field *and* no tenant concept, and it materialises as shared physical schema (§3). Under the corrected model this is not "missing company context" — it is an object whose owning scope cannot be determined from the system, in a design where the object is physically global. `OWNERSHIP ≠ AVAILABILITY` cannot be expressed here because ownership is not represented.
2. **The company-consistency check between a costed row and its dimension values is enforced on exactly one axis** (EV-P09-029, EV-P09-114). This is a COMPANY-scope finding about a COMPANY-scoped object (the management record, O6) and is therefore fully in force. It is not affected by the correction.

**SMEsPlus position MA-08 (revised).** Every analytic object shall carry an **explicit, declared owning scope** (PLATFORM / TENANT / COMPANY) as first-class data. Context requirements shall be **derived from the declared scope**, not applied uniformly:
- PLATFORM-scoped objects require neither tenant nor company context;
- TENANT-scoped objects require tenant context; company context is required only for a company-scoped operation upon them;
- COMPANY-scoped objects require both.
A missing required scope, or an ownership that cannot be proven, shall **deny**. An empty scope field shall not be used to mean "applies to all"; availability shall be expressed by an explicit availability rule that is separate from ownership.

**SMEsPlus position MA-09 (revised).** Where an object is COMPANY-scoped, the company-consistency check between it and every object it references shall be enforced uniformly across all axes, at the storage layer, and shall be provable by a single query. Where an object is TENANT-scoped, the equivalent check is the **tenant**-consistency check, and it is subject to the same uniformity and provability requirement. The reference pattern satisfies neither uniformly.

**SMEsPlus position MA-10 (new, arising from the correction).** A COMPANY-scoped object shall never be reachable from a TENANT-scoped object by an implicit widening. Specifically: a management record (COMPANY) may reference a dimension value of wider scope, but the reverse — a wider-scoped object deriving a figure by summing across companies — shall be an explicit, named, cross-company aggregation with its own authorisation, never a side effect of an empty scope field. The reference pattern's dimension balance does exactly this implicitly, by admitting company-empty records into every company's total (EV-P09-031).

**Peer dependency.** The authoritative tenant/company scope semantics for the Account domain are being determined across P01–P11 concurrently. The determinations in this section are **P09's own scope analysis** and are marked `PEER DEPENDENCY OPEN — P11 SCOPE RECONCILIATION`. P09 does not stop for them and does not adjudicate against another process's determination.

## 7. THE SEVEN CONSTITUTIONAL TRACE POINTS

The constitution requires the trace *Business Source → Financial Event → Analytic/Management Dimension → Allocation → Cost Object → Budget → Actual → Management Report*. Assessed against the reference pattern:

| Trace step | Present? | Carrier | Assessment |
|---|---|---|---|
| Business Source | partial | producing document fields on the management record | present for some producers, absent for others; no uniform source identity |
| Financial Event | **absent as an identity** | — | the prior Core Ledger study found no accounting-event identity and no provenance carrier; this study confirms the management layer inherits that absence |
| Analytic / Management Dimension | present | axis + value | but the axis is schema (§3) |
| Allocation | present | percentage payload | not integral, not complete, not audited (§5) |
| Cost Object | **absent as an object** | inferred from whichever field the producing module chose | see `P09_COST_OBJECT_MODEL` |
| Budget | present | budget header + line | no position object, no control (§2 O9/O10) |
| Actual | present | recomputed at read time from management records | never stored; three different time bases (`P09_ACTUAL_VS_BUDGET_TRACE`) |
| Management Report | present | ledger-table shadowing | crosses the boundary (`P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` §2.5) |

**Two of eight trace steps have no carrier at all.** The trace cannot be completed in the reference pattern, and therefore cannot be inherited. SMEsPlus must author the Financial Event identity and the Cost Object.

## 8. TERMINAL STATE

**FINDINGS AND DESIGN POSITIONS ISSUED — NO GATE MOVED, NO IMPLEMENTATION AUTHORISED.**
Positions MA-01 … MA-09 are proposals to Boss. None is approved by this document.
