# 00B_INVENTORY_SOURCE_LEARNING_POPULATION.md
# Inventory Pilot — Source Learning Population: derivation, counts, boundary

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**
Machine register: `MACHINE_REGISTERS/LEARNING_POPULATION.csv` — 4,339 rows.

---

## 1. Derivation, in the order it was executed

```
STEP 0  EVIDENCE BASE      50 reference roots located across every mount and $HOME by content
                           signature; generation of each fixed by a content discriminator
                           -> R1 adopted (series-19, 1,433 modules), R2 (series-18) as comparator
STEP 1  ANCHOR             51 objects declared by the core inventory module
STEP 2  INHERITANCE        + 3 objects created by prototype inheritance   -> FAM-CORE = 54
        CLOSURE
STEP 3  MENU REACH         + 18 objects reachable as the target of an action bound to a menu in the
                             Inventory application root subtree
STEP 4  ONE HOP, STOPPED   + 24 objects declared only by inventory-touching modules and holding a
                             declared relation to FAM-CORE.  CLOSURE STOPPED HERE.  -> ADOPTED = 96
STEP 5  OWNERSHIP SPLIT    OWNED = 86  (declaring modules lie wholly inside the inventory cluster)
                           BOUNDARY = 10  (lifecycle owned by another domain)
STEP 6  MODULE SET         149 modules declare or extend an OWNED object
STEP 7  SURFACE CENSUS     15 element classes extracted over those 149 modules
STEP 8  LEARNING IDS       4,339 Learning Items
```

## 2. Why the closure is stopped at one hop

Running the relational closure to fixpoint was **executed, not assumed**, and it degenerates to
1,559 objects across 1,071 modules — effectively the whole system. The iteration table is in
`00_SOURCE_LEARNING_MASTER_LIST.md` §7.

A second degeneration was measured one level down: treating universally-extended shared objects
(the configuration-settings object, the product objects, the unit-of-measure object) as **owned**
expands the module set from **100 → 445** in a single step. This is why `Ownership Class` is a
mandatory schema field and why only `OWNED` objects expand the module set.

> **A domain boundary is a decision published as a set with its complement. It is not a derivation.**

The boundary set (10 objects) is published in Register 05 §1. The module set (149) is published in
`MACHINE_REGISTERS/inv_modset_final.json`. **The mechanically-derived module set draws in the
manufacturing, quality, point-of-sale, repair, field-service and delivery clusters**; whether the
research subject keeps them is `BOSS-DEC-02` — put to Boss with the derived set attached, rather than
trimmed by an author.

## 3. Population

| Class | Items | Unit |
|-------|------:|------|
| `FIELD` | 1,846 | one declared field on an OWNED object |
| `BEHAVIOUR` | 614 | one override / validation / handler / UI method (dependency declarations excluded and counted separately at 483) |
| `VIEW` | 492 | one view definition on an OWNED object |
| `BUTTON` | 431 | one control inside a view definition |
| `SETTING` | 237 | one configuration-settings field declared by a domain module |
| `ACTION` | 200 | one action record targeting an OWNED object |
| `ACL` | 176 | one object-level access grant |
| `MENUX` | 134 | one menu contributed by a domain module **outside** the Inventory application |
| `MENU` | 62 | one menu inside the Inventory application root subtree |
| `GROUP` | 44 | one security group |
| `CONSTRAINT` | 32 | one declared data constraint |
| `RULE` | 28 | one row-level access rule |
| `AUTOMATION` | 26 | one scheduled job |
| `SEQUENCE` | 12 | one sequence allocator |
| `SYSPARAM` | 5 | one system parameter |
| **TOTAL** | **4,339** | |
| of which **CRITICAL** | **2,042** | 47.1% |

## 4. Instrument validation — all four controls, all classes

| Control | Method | Result |
|---------|--------|--------|
| **I1** second shape | menu count reconciled to an exact identity (1,585 + 64 elements → 1,574 + 37 ids, 35 shared → 1,576); scheduled jobs, groups reconciled by independent regex census (26 = 26, 44 = 44) | **PASS** |
| **I2** positive control | a synthetic module was injected declaring one artefact of **every** class; all ten extractors' counts rose by exactly the expected amount (`method` by 2, as designed) | **PASS — every predicate proved able to fire** |
| **I3** coverage assertion | 149/149 modules processed at every pass; 1,433/1,433 for the system-wide passes; 0 code parse failures; 7 XML parse failures, all enumerated and all outside the module set | **PASS** |
| **I4** zero re-test | 3 zeros re-tested. One was **real** (no declarative automation records — Reg 08 `HA-F-08`). Two were **instrument defects** and were repaired before publication (constraints, configuration-settings fields — `CORR-F-08`) | **PASS — and it fired** |

## 5. Instrument defects found by these controls

| ID | Defect | Effect if unrepaired |
|----|--------|----------------------|
| `CORR-F-07` | gating read only on two element kinds | would have under-counted the configuration-dependent UI surface by **86.3%** (87 vs 633) with a plausible non-zero number |
| `CORR-F-08` | constraint pattern matched a legacy declaration form absent in the target generation | would have published **0 constraints** for a domain that has 32 |
| `CORR-F-09` | inbound cross-module edges searched only inside the domain's own modules | would have made every inbound dependency invisible |
| `CORR-F-10` | object-selection filter partly keyed on **module name** rather than on the declaration | 29 of 148 action rows were included for a reason unrelated to the claim |
| `CORR-F-11` | row-level rule filter transformed an identifier instead of resolving it against the declared-object census | under-counted rules 12 vs 18 — a namespace-mismatched predicate |
| `CORR-F-12` | the population file serialised a detail column by truncating serialised text | every long row unparseable by any downstream consumer |
| `CORR-F-13` | lifecycle-state extraction read only keyword-form declarations | 13 of 14 state vocabularies returned empty |

**All seven were found by the framework's own controls, and all seven were repaired before this
package was frozen.** They are recorded because a framework that only reports its successes cannot be
audited.

## 6. Declared blind spots, with sizes

| Blind spot | Size | Measured? |
|------------|------|-----------|
| Conditional behaviour expressed in code | affects 1,540 of 4,339 items | size yes, content no |
| Financial postings created without a stored reference | — | **no** |
| Effective delete surface vs granted delete surface (`GAP-INV-13`) | floor of 2 objects | **no** |
| Menu-open side effects | **CLOSED** — population 8, mutating 3 (`SR-10`); residual bound is trace depth | **yes** |
| Runtime / deployment reachability | affects **all** 4,339 | **no** — no database evidence established |

A blind spot is only declared here if its size is stated or its size is explicitly stated to be
unknown. **"There may be more" is not a declaration.**
