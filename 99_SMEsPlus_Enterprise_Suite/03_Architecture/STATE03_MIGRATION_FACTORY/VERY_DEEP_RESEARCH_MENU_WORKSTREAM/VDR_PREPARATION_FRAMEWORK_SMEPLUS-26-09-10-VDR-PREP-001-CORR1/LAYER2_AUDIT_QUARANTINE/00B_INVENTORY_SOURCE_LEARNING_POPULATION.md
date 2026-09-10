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
STEP 8  LEARNING IDS       5,074 rows / 4,699 distinct identities  (v1 published 4,339 rows only)
```

## 2. Why the closure is stopped at one hop

Running the relational closure to fixpoint was **executed, not assumed**, and it degenerates to
1,559 objects across 1,071 modules — effectively the whole system. The iteration table is in
`00_SOURCE_LEARNING_MASTER_LIST.md` §7.

A second degeneration was measured one level down: treating universally-extended shared objects
(the configuration-settings object, the product objects, the unit-of-measure object) as **owned**
expands the module set from **100 → 445** in a single step. (The **100** is the 99 modules that touch
the core object family plus one that contributes a menu without touching it; the fixpoint table's
iteration-1 figure of 99 counts only the former. Both are correct measurements of different sets, and
the difference is stated because independent challenge found the two numbers side by side with no
reconciliation — `C-25`.) This is why `Ownership Class` is a
mandatory schema field and why only `OWNED` objects expand the module set.

> **A domain boundary is a decision published as a set with its complement. It is not a derivation.**

The boundary set (10 objects) is published in Register 05 §1. The module set (149) is published in
`MACHINE_REGISTERS/inv_modset_final.json`. **The mechanically-derived module set draws in the
manufacturing, quality, point-of-sale, repair, field-service and delivery clusters**; whether the
research subject keeps them is `BOSS-DEC-02` — put to Boss with the derived set attached, rather than
trimmed by an author.

## 3. Population — v2, rebuilt after the independent challenge

**5,074 rows over 4,699 distinct identities.** Both are published because they measure different
things: a **row** is a declaration site, an **identity** is a thing. v1 published rows only, against a
declared unit of one-thing-one-row — challenge finding `A-08`.

| Class | Rows | Distinct | Unit |
|-------|-----:|---------:|------|
| `FIELD` | 1,846 | 1,809 | one declared field on an owned object; a field declared by two modules is two sites, one thing |
| `BEHAVIOUR` | 614 | 502 | one override / validation / handler / UI method (dependency declarations counted separately at 483) |
| `GATEDELEM` | 525 | 371 | one visibility-gated element inside a view definition — **added by challenge `C-04`** |
| `VIEW` | 493 | 493 | one view definition on an owned object |
| `BUTTON` | 431 | 383 | one control inside a view definition |
| `SETTING` | 237 | 232 | one configuration-settings field |
| `ACTION` | 201 | 200 | one action record targeting an owned object |
| `ACL` | 180 | 178 | one object-level access grant — **corrected from 176 by challenge `A-04`** |
| `MENUX` | 134 | 134 | one menu contributed outside the domain's own application |
| `OBJECT` | 96 | 96 | one owned or boundary object — **added by challenge `C-04`** |
| `HANDOFF` | 90 | 90 | one external object on the domain's boundary — **added by challenge `C-04`** |
| `MENU` | 62 | 62 | one menu inside the domain's root menu subtree |
| `RULE` | 46 | 46 | one row-level access rule — **corrected from 28 by challenge `A-02`** |
| `GROUP` | 44 | 34 | one security group |
| `CONSTRAINT` | 32 | 32 | one declared data constraint |
| `AUTOMATION` | 26 | 26 | one scheduled job in a domain module; **16 are bound to an owned object, 10 are not** (`A-09`) |
| `SEQUENCE` | 12 | 12 | one sequence allocator |
| `SYSPARAM` | 5 | 5 | one declared system parameter |
| **TOTAL** | **5,074** | **4,699** | |
| of which **CRITICAL** | **2,461** | | |

### Research state, per item, derived from evidence — not asserted

| State | Items | What it means here |
|-------|------:|--------------------|
| `S1 SOURCE LOCATED` | 4,256 | a reproducible pointer resolves to primary evidence, with its root and generation recorded |
| `S3 CONFIG VERIFIED` | 755 | every configuration or gating condition affecting the item is identified |
| `S4 FUNCTION VERIFIED` | 63 | the item's behaviour has been read and described from source |

**v1 recorded `DISCOVERED` for all 4,339 rows** while the package published `S1 100%` and an `S4`
numerator. The population file — the sole authority under the Constitutional Rule — supported neither.
Challenge finding `C-02`.

### Mandatory columns v1 omitted (`C-03`, `C-20`)

`ownership_class` · `source_root` · `generation_basis` · `reachability` · a real `research_status` ·
a populated `register_coverage`. `reachability` is `UNMEASURED` for **all 5,074** items, because no
runtime evidence base was established (`GAP-INV-09`). It is a column with one value, and that is the
honest state.

## 4. Instrument validation — executed; two of the four did not do what was claimed

| Control | Method | Result |
|---------|--------|--------|
| **I1** second shape | menu count reconciled to an exact identity (1,585 + 64 elements → 1,574 + 37 ids, 35 shared → 1,576); scheduled jobs and groups reconciled by independent regex census | **EXECUTED — AGREED on 6 of 7 classes; DISAGREED on none, and that is the problem: on row-level rules it agreed at 28 and 28 was wrong, because the second instrument shared the first one's accessor (`CORR-F-27`)** |
| **I2** positive control | a synthetic module was injected declaring one artefact of **every** class it covered; each of those **ten** extractors' counts rose by exactly the expected amount | **EXECUTED — RESULT RECORDED.** Ten of the fifteen element classes were covered; the control's own coverage was not declared at the time (challenge `C-27`). A predicate proved able to fire on an injected artefact **in the declaration form the injection used** — the rule extractor passed this control and still could not read the second declaration form (`CORR-F-27`) |
| **I3** coverage assertion | 149/149 modules processed at every pass; 1,433/1,433 for the system-wide passes; 0 code parse failures; 7 XML parse failures, all enumerated and all outside the module set | **EXECUTED — RESULT RECORDED** |
| **I4** zero re-test | 3 zeros re-tested. Two were **instrument defects**, repaired before publication (`CORR-F-08`). The third was re-run in the **same class of query** against the same evidence base, which is repetition rather than corroboration — and no positive control for it exists anywhere in the root (challenge `B-14`, `CORR-F-25`) | **EXECUTED — 2 of 3 re-tests were controls; the third was not** |

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

**These seven were found by the framework's own controls and repaired before the package was frozen.**

**Eight more were found by independent challenge, and they are the more important half.**

| ID | Defect | What it produced |
|----|--------|------------------|
| `CORR-F-22` | method-body resolver returned the first definition in walk order, on a method overridden in two modules | 2 mutating menus reported instead of 3 |
| `CORR-F-23` | a menu bound to an action the platform **materialises at install time** from a scheduled job was invisible to the action census | a 4th mutating menu missed; *"all 7 resolved"* published while the register's own table showed one unresolved |
| `CORR-F-24` | the toggle taxonomy had five mechanisms; an **undeclared runtime parameter** is a sixth | the Pilot's most severe control finding was mis-classified into a class it is not in |
| `CORR-F-25` | a zero re-run in the **same class of query**, with no positive control available anywhere | a zero presented as re-tested that could only ever be zero |
| `CORR-F-26` | a **syntactic** predicate counting a **semantic** claim | 9 null-company rules published; the register's own appendix printed a 10th |
| `CORR-F-27` | the extractor read one of the **two declaration forms** the platform accepts for a rule's target | 28 rules published against 46; **a CRITICAL finding inverted** |
| `CORR-F-29` | security and view classes scoped by module membership, when a module can grant, rule or extend without declaring | 176 grants for 180, 492 views for 493 |
| `CORR-F-30` | the ownership rule as published is **circular in sequence** — evaluable only as a fixpoint | a rule a reader cannot execute in the order given |

**Fifteen instrument defects in one Pilot, of which the seven the producer caught were the smaller
half.** They are recorded because a framework that only reports its successes cannot be audited — and
because the ratio is the finding: **8 of 15 were reachable only from outside.**

## 6. Declared blind spots, with sizes

| Blind spot | Size | Measured? |
|------------|------|-----------|
| Conditional behaviour expressed in code | affects 1,540+ items of 5,074 | size yes, content no |
| Financial postings created without a stored reference | — | **no** |
| Effective delete surface vs granted delete surface (`GAP-INV-13`) | floor of 2 objects | **no** |
| Menu-open side effects | **CLOSED** — population 8, mutating 3 (`SR-10`); residual bound is trace depth | **yes** |
| Runtime / deployment reachability | affects **all 5,074**; the `reachability` column carries `UNMEASURED` on every row | **no** — no database evidence established |

A blind spot is only declared here if its size is stated or its size is explicitly stated to be
unknown. **"There may be more" is not a declaration.**
