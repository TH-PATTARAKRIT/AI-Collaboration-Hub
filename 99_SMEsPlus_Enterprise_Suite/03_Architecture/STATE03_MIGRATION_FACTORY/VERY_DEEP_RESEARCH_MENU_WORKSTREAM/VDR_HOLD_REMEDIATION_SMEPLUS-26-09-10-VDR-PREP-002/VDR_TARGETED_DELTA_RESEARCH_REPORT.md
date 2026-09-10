# VDR_TARGETED_DELTA_RESEARCH_REPORT.md
# Targeted Delta VDR — the ten live functions prior research never covered

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Generation basis: series-19 source, corroborated on two series-19 deployments.

---

## 1. Selection rule — delta only, and only where justified

Targeted VDR was run **only** on items classified `MISSING` by `00D` **and** `RUNTIME REACHABLE` by
`00C`. That is **10 of 62 menus**. The **29** `PARTIAL` items were **not re-researched**: their process,
configuration **and optional-function** dimensions are covered by prior work.

> **The justification is stronger than first published.** This section originally claimed prior work
> covered process and configuration but **not** optional function. **That was wrong** — `RC-F-01` is
> withdrawn — and the prior corpus covers all three. The decision not to re-research them stands on
> better ground than the reasoning first given for it. The 6 `MISSING` items that are installed nowhere observed were **not researched**
either — they are optional-module dependent and out of the applicable baseline.

Each of the 10 was studied across the required chain:
`INPUT → PROCESS → CONFIGURATION → OPTIONAL FUNCTION → OUTPUT → CROSS-MODULE HANDOFF`.

---

## 2. Findings

### DR-F-01 — CORRECTED — Batch and wave transfers are **one object with two projections** (**MATERIAL**)
Both menus resolve to the **same object**. The published claim that they differ *"only by a boolean
filter"* is **wrong**: verified independently, they differ by the domain boolean **plus a dedicated
list and kanban view set plus a distinct action path** — three differences, not one. The instrument
could not have seen the view overrides because it captured only the action's domain. `CORR-F-43`.
**The design conclusion — two projections of one function — survives.** They share:
one lifecycle (`draft · in progress · done · cancelled`), 58 fields, **28 controls**, 28 behaviours,
one set of 10 gated elements.

**Consequence for SMEsPlus design:** these are **one function with two projections**. Designing them as
two features would duplicate a lifecycle; designing them as one without the projection would lose a
real operational distinction. Neither is derivable from the menu list, which shows two peers.

### DR-F-02 — Batch/wave transfers pull **fleet management** into the Inventory surface (**MATERIAL**)
The batch object carries vehicle, vehicle-category, driver and dock references — a **fleet** cluster
dependency, plus a country e-transport document object. **Neither cluster is in the Inventory
ownership boundary and neither appears anywhere in prior research.** A batch transfer is therefore a
cross-domain object whose scheduling attributes are owned elsewhere.

### DR-F-03 — The operation-type Overview is the richest configuration surface in the domain, and only its *configuration* twin was researched (**CRITICAL**)
The Overview object declares **129 fields — 13 of them required**, **12 stored computed values**,
**5 validation constraints**, **4 persistence interceptions**, and **48 gated elements across 10
distinct security groups** (published as 11; a group and its negation were counted twice) — the highest gating density measured anywhere in the Pilot.
It reaches **61 distinct external objects**.

Prior research covered the *Operation Types configuration menu* (`INV-M21`) as `L2 COMPLETE`. It did
**not** cover the **Overview dashboard**, which is the application's default operational landing
surface and is driven by the same object.

> **The same object was researched through its configuration screen and not through the screen users
> actually work in.** A configuration-screen study answers *what can be set*; it does not answer *what
> the operator sees, in what order, filtered how, and with which controls enabled*.

### DR-F-04 — CORRECTED AND STRENGTHENED — the reference object is the order-to-cash traceability spine (**CRITICAL — Identity**)

**Two corrections.** It binds **four** domains, not three — the fourth being **manufacturing**, the
very object `FO-F-03` names as the sole co-owner. And it was described from source declarations only;
**measured in data on the transacted deployment it is far more important than the text implied**:

| Link | Rows | Against | Density |
|---|---:|---:|---|
| reference ↔ **stock movement** | **13,163** | 14,441 movements | **91.1%** |
| reference ↔ **sales order** | **6,661** | 6,665 sales orders | **99.94%** |
| reference ↔ purchase order | 11 | 31 | 35.5% |
| reference ↔ point-of-sale · production order | **0** | — | declared, unused |
| the object itself | **11,852 rows** | — | **2nd most populated object in the domain** |

**In data this object is the join between stock movements and sales orders** — essentially every sales
order and nine in ten movements carry one. It is that deployment's order-to-cash traceability spine,
and it has **no controls, no validations, no behaviours and no record rule**, reachable only through a
menu gated to a **technical-only** group. **`GAP-INV-18` is promoted to `CRITICAL-GAP-06`.**

**Method note:** the links are many-to-many and live in **join tables**. A first check looked for a
reference column on the parent documents, found none, and would have recorded *"0% populated"*.
**The relation type determines where the evidence lives.** `CORR-F-36`.

The original text follows.

#### (as published)
A small object — 7 fields, **no controls, no behaviours, no constraints** — carries references to
**point-of-sale orders, purchase orders and sales orders**. Its menu is gated to a **technical-only
group**, so no ordinary user, and no menu-driven research, would ever see it.

**Identity is a Critical Area.** An object that binds inventory documents to three other domains'
documents, with no validation, no controls and no audit behaviour, is an identity surface that
SMEsPlus must design deliberately. Prior research never covered it. Raised as `GAP-INV-18`.

### DR-F-05 — The Packages function is entirely conditional, and it touches accounting (**MATERIAL**)
The Packages menu is gated on a configuration toggle. Its object carries **4 controls**
(unpack · package transfers · put in pack · remove), **2 persistence interceptions**, **11 gated
elements across 5 groups**, and an edge to an **accounting document** through a localisation field.

**A function that does not exist until a toggle is set, and that reaches accounting when it does, is
exactly the optional-function class prior research has zero coverage of** (`00D` `RC-F-01`).

### DR-F-06 — Manufacturing orders inside the Inventory application are a 115-field, 61-control surface (**CRITICAL**)
The production order — the one genuine cross-module co-owner (`00B` `FO-F-03`) — is reachable from
within the Inventory application through a menu gated to the Inventory user and manager groups.
It declares **115 fields, 9 required, 18 stored computed values, 61 controls, 66 behaviours including
9 persistence interceptions**, and **40 gated elements across 17 security groups** (published as 18; a group and its negation were counted twice) — including groups
owned by **accounting, project, purchase and sales**.

**Inventory users can reach and act on a manufacturing document from inside Inventory.** The ownership
question is therefore not academic: `BOSS-DEC-02` must decide whether this surface is inside the
Inventory subject, inside Manufacturing, or jointly owned with a named owner per fact.

### DR-F-07 — The Master Production Schedule is a client-rendered surface, not a record list (**MATERIAL**)
Its action is a **client action** — the screen is rendered by application code, not by a declarative
view. Its object has 17 fields, 3 required, and **2 controls only (save, cancel)**.

**A client-rendered screen cannot be studied from view declarations at all.** Any register whose
population is view records is blind to it. Two of the 62 menus in this domain are client actions.

### DR-F-08 — WITHDRAWN AND REPLACED — the delivery objects were measured at zero by a scoping defect (**MATERIAL**)

> **This finding was published on an object the extractor reported as having 0 fields, 0 required
> fields, 0 controls and 0 behaviours — beside a count of 46 external edges. Nothing flagged the
> contradiction.**

The extractor scoped field collection to the **menu's** module, which only extends the object:

| Object | Published | Actual |
|---|---:|---:|
| delivery carrier | 0 fields | **264 fields across 24 modules**, 17 required |
| delivery postcode prefix | 0 fields | **1 field**, required |

**The ownership conclusion survives** — both are `CONSUMING`, displayed by Inventory, owned by
Delivery, one gated to a technical-only group. **Every quantitative statement about them is
withdrawn.** `CORR-F-39`: *a zero on one dimension beside a non-zero on another is a contradiction,
and no control was positioned to see it.*

### DR-F-09 — One Inventory menu performs a device-management action against **no object at all**
The *Reset Linked Printers* menu is a **client action with no target object**, no fields, no controls
and no behaviours. It is a side-effecting device operation reachable from the Inventory application.

**Every register in this framework is keyed on an object. This item has none.** It is invisible to the
object-impact matrix, the ownership matrix and the data-impact matrix by construction. Recorded as
framework correction `CORR-F-33`: **the Learning Item schema must admit an item whose target is a
device or an external system rather than a data object.**

---

## 3. Optional-function and configuration dimensions — the delta's own contribution

| Menu | Gated by | Optional-module dependent | Configuration surface |
|------|----------|---------------------------|-----------------------|
| Batch transfers · Wave transfers | ungated menu; 10 gated elements inside | **yes** — a module-installer toggle | quality checks, reception report, multi-location, lot tracking |
| Packages | **a configuration toggle** | no | 11 gated elements, 5 groups |
| Overview | ungated | no | **48 gated elements, 11 groups** |
| Manufacturing orders | Inventory user/manager groups | **yes** — manufacturing install | 40 gated elements, 18 groups |
| Master Production Schedule | manufacturing manager group | **yes** — a module-installer toggle | 3 gated elements |
| Stock references | **technical-only group** | no | none |
| Delivery methods | ungated | **yes** — delivery install | none measured |
| Delivery postcode prefixes | **technical-only group** | **yes** | none |
| Reset linked printers | ungated | **yes** — device-integration install | none |

**Six of the ten are optional-module dependent.** They exist only where the tenant installs the
relevant module — and **all six are installed on at least one observed deployment** (published as five; corrected on
recount), so this is not a theoretical branch.

---

## 4. What this delta did **not** cover, stated

| Not covered | Why |
|-------------|-----|
| The 29 `PARTIAL` menus' **runtime** dimension | prior research covers their process, configuration **and optional-function** dimensions; what it cannot cover is runtime reachability, which did not exist as a control when it was written |
| Transactional behaviour of any of the 10 | no deployment carries on-hand quantity (`00C` `RR-F-04`) |
| The 6 `MISSING` menus not installed anywhere | optional-module dependent, outside the applicable baseline |
| The 134 extra-application menus | out of this session's control-area scope |

**No item studied here is claimed `RESEARCH-COMPLETE`.** Each has PROCESS, CONFIGURATION and
OPTIONAL FUNCTION at first-pass depth and **no transactional verification** — which under §11 is
`PARTIAL`, not complete.
