# 00_SOURCE_LEARNING_MASTER_LIST.md
# Source Learning Master List — Governing Standard (Preparation Control 01)

Session: `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
Owner: **LESA — Lead ERP Solution Architect**
Layer: **LAYER 1 — CLEAN-ROOM.** This file defines the standard. The *populated* Inventory Pilot
population is reference-ERP research and lives under `LAYER2_AUDIT_QUARANTINE/`.
Status: **FROZEN v1.0** (Pilot corrections incorporated)

---

## 1. Constitutional Rule

> **No VDR coverage percentage may be calculated without this population.**

A Research Register may not create an independent research population. If a register needs to record
something, that thing must first exist here with a **Learning ID**. **Zero orphan research evidence.**

---

## 2. Learning Item Schema

Every Learning Item carries the following. Fields marked **M** are mandatory at creation; the rest are
filled as the item advances through the research states in `VDR_COVERAGE_RULE.md` §4.

| # | Field | M | Notes |
|---|-------|---|-------|
| 1 | `Learning ID` | M | `LI-<DOMAIN>-<CLASS>-<nnnn>`; immutable; never reused |
| 2 | `Application` | M | |
| 3 | `Module / Domain` | M | |
| 4 | `Ownership Class` | M | **`OWNED` / `SHARED-CONSUMED` / `SHARED-EXTENDED` / `EXTERNAL`** — added by the Pilot (CORR-F-03) |
| 5 | `Top Menu` | | |
| 6 | `Menu Group` | | |
| 7 | `Menu` | | |
| 8 | `Submenu` | | |
| 9 | `Action` | | including the **resolution hops** needed to reach the target (CORR-F-04) |
| 10 | `View` | | |
| 11 | `Button` | | |
| 12 | `Smart Button` | | |
| 13 | `Context Action` | | |
| 14 | `Field` | | |
| 15 | `Configuration` | | |
| 16 | `Feature Toggle` | | with its **toggle class** (§6) |
| 17 | `Business Function` | | |
| 18 | `Business Rule` | | |
| 19 | `Workflow` | | |
| 20 | `State Transition` | | |
| 21 | `Automation` | | |
| 22 | `Scheduler` | | |
| 23 | `Model / Object` | | |
| 24 | `Data Relationship` | | |
| 25 | `Constraint` | | |
| 26 | `Security` | | |
| 27 | `Record Rule` | | |
| 28 | `Approval` | | |
| 29 | `Accounting Impact` | | |
| 30 | `Inventory Impact` | | |
| 31 | `Cross-Module Handoff` | | |
| 32 | `Tenant Impact` | | |
| 33 | `Company Impact` | | |
| 34 | `Failure Path` | | |
| 35 | `Cancel Path` | | |
| 36 | `Reverse Path` | | |
| 37 | `Return Path` | | |
| 38 | `Audit Requirement` | | |
| 39 | `Source Location` | M | |
| 40 | `Evidence Pointer` | M | reproducible: root + path + line, plus the generation it was read at |
| 41 | `Generation Basis` | M | **added by the Pilot (CORR-F-05)** — content-verified, never path-name-derived |
| 42 | `Criticality` | M | `CRITICAL` / `STANDARD`, per `VDR_COVERAGE_RULE.md` §6 |
| 43 | `Research Status` | M | S0..S9 |
| 44 | `Register Coverage` | | which of the nine registers hold a record for this item |
| 45 | `Open Question` | | |
| 46 | `Material Delta` | | |
| 47 | `Last Verified Evidence` | | |
| 48 | `Reachability` | | **added by the Pilot (CORR-F-06)** — latent vs live; source analysis alone cannot establish whether a behaviour can fire |

---

## 3. Decomposition Rule

The following are **never acceptable as a single Learning Item** when independent functions exist
underneath them:

`Inventory` · `Receipt` · `Delivery` · `Replenishment` · `Manufacturing` · `Accounting` ·
`Purchase` · `Sales`

Each must be decomposed to its **actual functional population**. The unit of decomposition is the
smallest independently addressable functional element: one menu node, one action, one view, one
control, one field, one configuration toggle, one automation, one rule, one access grant, one
constraint, one behavioural override.

---

## 4. Population Derivation Contract

The population is produced by a **rule executed over a declared evidence base**, never by an author
listing what they can think of. The derivation must publish, in this order:

1. **Evidence base** — every root swept, every exclusion with its reason, the generation of each root
   established by a **content-based** discriminator.
2. **Anchor** — the starting set, and the rule that produced it.
3. **Closure** — how the anchor was extended, and **where the closure was stopped and why**.
4. **Ownership split** — `OWNED` vs boundary, because a closure that includes universally-extended
   shared objects degenerates to the whole system (Pilot evidence: §7).
5. **Complement** — what the boundary excludes, published as a set, not described in prose.
6. **Instrument controls** — I1–I4 of `VDR_COVERAGE_RULE.md` §3, with outputs.

---

## 5. Learning Item Classes

| Class | Unit |
|-------|------|
| `MENU` | one menu node inside the domain's root menu subtree |
| `MENUX` | one menu node contributed by a domain module but hanging **outside** the domain root |
| `ACTION` | one action record targeting a domain object |
| `VIEW` | one view record on a domain object |
| `BUTTON` | one control inside a view arch |
| `FIELD` | one declared field on a domain object |
| `SETTING` | one configuration-settings field declared by a domain module |
| `AUTOMATION` | one scheduled job / automated behaviour |
| `BEHAVIOUR` | one behavioural override, validation, onchange, lifecycle hook or UI method |
| `CONSTRAINT` | one database or model constraint |
| `RULE` | one record-level access rule |
| `ACL` | one model-level access grant |
| `GROUP` | one security group |
| `SEQUENCE` | one sequence allocator |
| `SYSPARAM` | one system parameter |

`MENUX` exists because a domain's modules add menus to **other** applications' menus; omitting them
loses cross-module surface. In the Inventory Pilot `MENUX` is **134 items — 2.2x the size of the
domain's own menu spine (62)**.

---

## 6. Feature Toggle Classes

A configuration switch is not one kind of thing. Five classes were observed; a register that models
only the first is incomplete.

| Class | Mechanism | Pilot count |
|-------|-----------|-------------|
| `A` MODULE INSTALLER | the feature is a separate installable unit; turning it on installs code | 41 |
| `B` GROUP TOGGLE | activates a security group, which gates UI and rules | 21 |
| `C` SYSTEM PARAMETER | writes a system parameter read at runtime | 7 |
| `D` PASS-THROUGH | stores onto another object (company / warehouse / product) | 138 |
| `E` PLAIN / COMPUTED | held on the settings object itself, or derived | 30 |
| | **TOTAL** | **237** |

**Class D is the largest class and the least visible**, because the durable state lives on a different
object from the screen that sets it.

---

## 7. Why the boundary must be declared, not derived — measured evidence

A relational-closure definition of a domain was executed to fixpoint over the Pilot's evidence base.
It degenerates:

| Iteration | Family size before | Module set | Candidates | Added |
|-----------|-------------------:|-----------:|-----------:|------:|
| 1 | 54 | 99 | 144 | 48 |
| 2 | 102 | 669 | 1,502 | 736 |
| 3 | 838 | 1,037 | 1,166 | 558 |
| 4 | 1,396 | 1,068 | 618 | 109 |
| 5 | 1,505 | 1,071 | 670 | 35 |
| 6 | 1,540 | 1,071 | 635 | 15 |
| 7 | 1,555 | 1,071 | 620 | 4 |
| **fixpoint** | **1,559** | **1,071** | — | 0 |

The whole system. **A domain has no natural relational boundary.** Therefore:

> **The domain boundary is a decision, taken by a named authority, published as a set together with
> its complement. It is not a derivation, and it is not prose.**

The Pilot's adopted rule — anchor + inheritance closure + menu-reachable + **one hop, stopped** +
ownership split — is this session's **candidate standard**. Whether it becomes the universal standard
is `BOSS-DEC-10` and is **open**. Independent challenge also established that the rule as first
published was **circular in its sequencing** — the ownership test refers to the module cluster, which
is derived from ownership. It is evaluable only as a fixpoint, and is now written that way
(`CORR-F-30`).

---

## 8. Governing rules for this file

1. A Learning ID is created **before** any register records evidence about it.
2. A Learning Item's `Ownership Class` determines whether it expands the module set. **Only `OWNED`
   items do.** Including a universally-extended shared object in the owned set degenerates the
   population (Pilot: the module set jumped 100 → 445 the moment shared objects were treated as owned).
3. Every negative recorded here carries its scope. `NOT FOUND IN <declared set>` is a finding;
   `DOES NOT EXIST` is not, unless the set is the whole evidence base and that has been swept.
4. Material discoveries update this list first, and the registers second.
5. This list is re-derived — not edited — when the evidence base or the generation changes.

---

## 9. Inventory Pilot instance

The populated instance is:

- `LAYER2_AUDIT_QUARANTINE/00B_INVENTORY_SOURCE_LEARNING_POPULATION.md` — derivation, counts, boundary
- `LAYER2_AUDIT_QUARANTINE/MACHINE_REGISTERS/LEARNING_POPULATION.csv` — **4,339 Learning Items**, one row per item

**Population v2, rebuilt after the independent challenge: 5,074 rows over 4,699 distinct identities.**
Both figures are published because they are different measurements: a row is a **declaration site**,
an identity is a **thing**. The v1 population (4,339) understated the surface and its rows carried no
research state, no ownership class, no generation basis and no reachability — see
`INVENTORY_PILOT_CHALLENGE_REPORT.md` §4.

Class distribution (rows / distinct): `FIELD` 1,846/1,809 · `BEHAVIOUR` 614/502 · `GATEDELEM` 525/371 ·
`VIEW` 493/493 · `BUTTON` 431/383 · `SETTING` 237/232 · `ACTION` 201/200 · `ACL` 180/178 ·
`MENUX` 134/134 · `OBJECT` 96/96 · `HANDOFF` 90/90 · `MENU` 62/62 · `RULE` 46/46 · `GROUP` 44/34 ·
`CONSTRAINT` 32/32 · `AUTOMATION` 26/26 · `SEQUENCE` 12/12 · `SYSPARAM` 5/5.
**Critical: 2,461.**
