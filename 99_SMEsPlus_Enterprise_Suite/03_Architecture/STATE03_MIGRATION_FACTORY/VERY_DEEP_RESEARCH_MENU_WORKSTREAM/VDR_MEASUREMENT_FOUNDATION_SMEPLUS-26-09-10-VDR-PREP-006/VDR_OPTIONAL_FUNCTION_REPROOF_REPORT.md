# VDR_OPTIONAL_FUNCTION_REPROOF_REPORT.md
# Optional function — rebuilt, and still not measurable per element

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 14.

---

## 1. What was retracted

PREP-004 published `OPTIONAL_FUNCTION 22.36%` by inheriting a **subject-level** determination to the
elements each subject governs — and **6 rows the grading run itself labelled a defect were awarded
verification.** PREP-005 retracted it to 0.00%. **This round does not restore it.**

## 2. What IS proven, per subject

**39 subjects: 25 optional modules and 14 capability groups**, each with activation **and** deactivation
established from source, coverage 39 of 39 in every pass.

### The structural result — the most transferable finding in the programme

> **Module deactivation is destructive. Capability-switch deactivation is not.**

| | Module uninstall | Capability switch off |
|---|---|---|
| Schema | **tables and columns dropped, with cascade** | **none** |
| Stored values | **destroyed** | **always survive** |
| Dependents | **force-uninstalled with it** | unaffected |
| Deletion guards | **skipped** | not involved |

**40 tables and 278 columns on models the modules do not own** are destroyed across the 25 subjects.
**Not one of the 25 is safe.** Nine of the 14 capability groups are.

### The four cases where effects outlive the subject

**FEFO silently degrades to FIFO** — no error, no log, unrecoverable configuration, and expired stock
returns to available quantity · **landed costs**: the posted entries survive and the documents
explaining them are destroyed · **quality control**: removing it removes a hard completion gate ·
**subcontracting**: an uninstall path that swallows its own failure in a bare catch-all.

### Deactivation that does not stay deactivated

Three subjects declare auto-install; every dependency is a re-install trigger. A second mechanism that
might have resurrected them on a routine update was **tested and ruled out** — reachable only at
database creation. A determined negative.

## 3. What is NOT proven

§20 requires, **per optional function**: source presence · activation path · deactivation path · runtime
effect · menu · field · process · data · security · cross-module · fallback · silent degradation ·
historical data behaviour.

**All of that is established per subject. None of it is established per element.** Converting the first
into the second is exactly the defect that was retracted.

**And one axis is still unmeasured at any level: whether any of it has fired on a real deployment.**
Everything above is source semantics.

## 4. A register defect that survives, and is left visible

**60 rows are classed optional and record no activation condition.** No activation condition means no
deactivation condition, so they cannot meet the standard. **Recorded as a defect and not repaired** — a
silent repair would change a population, and populations change only through a new version with a
documented delta.

**5 of the 14 capability-group subjects were recorded in the register as settings-field names rather
than group identifiers.** Any search keyed on the register's own strings returns a **false zero** for
those five.

## 5. Coverage

| | |
|---|---:|
| Optional Function Coverage, per element | **0.00%** |
| Floor | 96% |
| | **FAIL** |

## 6. The rule this produced for SMEsPlus

**Anything designed as a module inherits destructive removal; anything designed as a capability switch
does not.** That single result decides module-versus-switch for every SMEsPlus capability, and it does
not depend on the coverage figure being zero.
