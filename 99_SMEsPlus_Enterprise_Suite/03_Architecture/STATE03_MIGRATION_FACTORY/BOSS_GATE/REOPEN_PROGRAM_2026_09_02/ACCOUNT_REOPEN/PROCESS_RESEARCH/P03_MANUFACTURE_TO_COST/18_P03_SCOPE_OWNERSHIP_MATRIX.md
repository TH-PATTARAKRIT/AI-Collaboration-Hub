# 18 — P03 SCOPE OWNERSHIP MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

Produced under **`SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction**,
received mid-session. This session did **not** reset, restart or discard evidence; only
scope-affected findings were revalidated. The revalidation record is `22` §3.

Canonical rule applied: **SCOPE-AWARE EVERYWHERE.** Permitted scopes `PLATFORM`,
`TENANT`, `COMPANY`. Missing required scope = DENY. Ownership ≠ availability.

---

## 1. The finding that governs this whole matrix

**Enumeration.** POPULATION: `mrp`, `mrp_account`, `mrp_workorder`, `stock_account`.
PATTERN: case-insensitive word `tenant` in `*.py`. UNIT: one file with ≥1 match.
**Result: 0 files.**

> **No tenant boundary exists anywhere in the reference manufacturing source, within this
> scope.** Its only boundary is `company`, and its only sharing mechanism is
> `company_id = False`.

`FACT VERIFIED`, scope declared. Everything below follows from it: the reference product
cannot be read as evidence *for* any tenant-scope decision, only as evidence of what a
company-only model does and does not achieve.

## 2. The `company_id = False` hazard — ownership vs availability

`mrp.bom` and `mrp.workcenter` both permit an empty company
(`mrp/models/mrp_bom.py:64`, `mrp/models/mrp_workcenter.py:497`), and resolution
deliberately includes company-less records:

| Site | Behaviour |
|---|---|
| `mrp/models/mrp_bom.py:351 — _bom_find` | `['|', ('company_id','=',False), ('company_id','=',company_id …)]` |
| `mrp/models/mrp_production.py:137, 1435` | same pattern for BOM selection |
| `mrp/models/product.py:40, 145` | same pattern for kit resolution |
| `mrp/models/mrp_workcenter.py:75` | alternative work centres may be company-less |

The correction's distinction is exactly the right instrument here:

> **`company_id = False` expresses AVAILABILITY, not OWNERSHIP.** A company-less BOM is
> available to every company and owned by none.

In a single-legal-entity deployment that is a convenience. In SMEsPlus — where the
correction defines **TENANT = security/customer boundary** and states that *unrelated
independent companies are separate tenants by default* — an unowned, globally available
BOM is a **record with no security boundary at all**.

`FACT VERIFIED`. Recorded as `SCOPE-01`.

## 3. Scope ownership matrix — P03 objects

Answering, for each material object, the eight questions CORR1 §4 requires. `OWNS` is the
scope that owns the object; `EXEC` the scope that executes operations on it; `MUT` the
scope that may mutate it; `REF` the scope that may reference it; `FIN` whether it creates a
financial effect and which scope owns that effect.

| Object | OWNS | EXEC | MUT | REF | FIN | Basis |
|---|---|---|---|---|---|---|
| Unit of measure, currency | `PLATFORM` candidate | `PLATFORM` | `PLATFORM` | any | No | Platform standard reference |
| Productivity-loss / blocking-reason taxonomy | `PLATFORM` candidate, tenant-extensible | `TENANT` | `PLATFORM` for the base set, `TENANT` for extensions | `TENANT` | No | Reference taxonomy; `07` §1 of the Asset package treats it as structure, not cost |
| **Bill of materials** | **`TENANT`** | `TENANT` | `TENANT` | `COMPANY` | No | Shared engineering definition; a tenant's product design is not a legal-entity fact. **`SCOPE-01` is the defect against this** |
| **Routing / operation** | **`TENANT`** | `TENANT` | `TENANT` | `COMPANY` | No | Travels with the BOM |
| **Work centre — as a resource** | **`TENANT`** | `TENANT` | `TENANT` | `COMPANY` | No | Scheduling resource; `ASSET_DR_CONTINUATION/07` §3 demoted it to resource group |
| **Work-centre hourly rate** | **`COMPANY`** | `COMPANY` | `COMPANY` | `COMPANY` | **Yes — `COMPANY`** | It is a costing parameter that lands in a legal entity's inventory value. **Splitting it from the resource is a P03 scope conclusion — §4** |
| Machine / equipment | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | Yes — `COMPANY` | An asset is owned by a legal entity. Asset track owns this |
| **Manufacturing order** | **`COMPANY`** | `COMPANY` | `COMPANY` | `COMPANY` | **Yes — `COMPANY`** | It consumes and produces a legal entity's inventory |
| Work order | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | Yes — `COMPANY` | Related to the MO's company (`mrp/models/mrp_workorder.py:50`) |
| **Time log** | **`COMPANY`** | `COMPANY` | `COMPANY` | `TENANT` for analytics | **Yes — `COMPANY`** | It is the evidence for a company's conversion cost |
| Employee, and their hourly cost | `TENANT` for identity; **`COMPANY`** for the cost rate | `COMPANY` | `COMPANY` | `COMPANY` | Yes — `COMPANY` | A person may work for several companies of one tenant; the cost rate is a company fact |
| Raw / finished stock move | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | Yes — `COMPANY` | Inventory track owns this |
| Valuation layer | `COMPANY` | `COMPANY` | none — immutable | `COMPANY` | Yes — `COMPANY` | Inventory track |
| **Production cost account, WIP accounts** | **`COMPANY`** | `COMPANY` | `COMPANY` | `COMPANY` | **Yes — `COMPANY`** | Company-dependent by construction. **`DC-11` is a breach of exactly this row** |
| Labour absorption journal entry | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **Yes — `COMPANY`** | A journal entry is the canonical company-scoped financial event |
| WIP accrual entry | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | Yes — `COMPANY` | as above |
| Analytic account / plan | `TENANT` or `COMPANY` | depends | depends | depends | Depends | **`HOLD — SCOPE EVIDENCE REQUIRED`, §5** |
| Subcontractor (partner) | `TENANT` | `COMPANY` | `TENANT` | `COMPANY` | Yes — `COMPANY` | Partner identity is a tenant's relationship; the payable is a company's |

## 4. The scope split this analysis forces — `DESIGN CANDIDATE`

The matrix separates two things the reference product holds in **one** record:

| Concern | Scope | Today |
|---|---|---|
| Work centre as a **scheduling resource** — calendar, capacity, alternatives | `TENANT` | one record |
| Work centre's **hourly cost rate** | `COMPANY` | the same record, one scalar field |

`mrp/models/mrp_workcenter.py:43` puts `costs_hour` directly on the resource, and
`mrp/models/mrp_workcenter.py:497` permits that resource to have **no company at all**.

> **A company-less work centre carries a cost rate that no company owns, and that rate
> reaches inventory value in every company that uses it.**

This is `SCOPE-01` in its most financially direct form, and it is a **new finding produced
by CORR1** — the pre-correction reading of this session recorded the work centre only as a
company-guarded object and did not separate resource scope from rate scope.

`R-15`: **the costing rate must be a `COMPANY`-scoped object distinct from the
`TENANT`-scoped resource it prices.** `DESIGN CANDIDATE`. Not authorised for
implementation; the AAS+ veto stands.

## 5. Unresolved scope questions

| ID | Question | Status |
|---|---|---|
| `SCOPE-Q-01` | Is an analytic plan `TENANT` (management reporting across the group) or `COMPANY` (statutory cost analysis)? Both readings are defensible and the reference product has no tenant to distinguish them | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `SCOPE-Q-02` | Is the productivity-loss taxonomy `PLATFORM` with tenant extension, or `TENANT` outright? Governs whether downtime causes are comparable across tenants | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `SCOPE-Q-03` | May one tenant's BOM reference another tenant's product? Presumed no; not provable from a source with no tenant concept | **HOLD — SCOPE EVIDENCE REQUIRED** |

Per CORR1 §8, none of these is put to Boss for selection, and none stopped the session.
All unaffected work continued.

## 6. Peer dependency

**`PEER DEPENDENCY OPEN — P11`.** CORR1 §7 assigns continuous cross-process scope
reconciliation to P11. P03's matrix is stated from the P03 side only. Rows that P03 marks
`COMPANY` on financial grounds — the MO, the time log, the rate, the entries — are the rows
P03 is confident of. Rows marked `TENANT` on the master-data side (BOM, routing, resource,
partner) are **candidates offered to P11**, not determinations binding on P01–P10.

This session does not wait for P11. `12_P03_CROSS_PROCESS_OWNERSHIP.md` is unchanged in
substance; §1 of that file gains no new contested boundary from this correction.
