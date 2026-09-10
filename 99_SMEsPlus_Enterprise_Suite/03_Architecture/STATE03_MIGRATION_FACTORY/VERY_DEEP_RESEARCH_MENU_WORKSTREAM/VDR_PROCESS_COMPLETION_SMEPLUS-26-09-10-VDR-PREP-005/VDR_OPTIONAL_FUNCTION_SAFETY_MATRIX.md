# VDR_OPTIONAL_FUNCTION_SAFETY_MATRIX.md
# Optional function safety — expected, observed, risk, control

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 04.

---

## 1. The same retraction applies here

PREP-004 published `OPTIONAL_FUNCTION 22.36%` by inheriting a **subject-level** determination to the
elements each subject governs. The challenger's finding on configuration applies identically, and a
sharper one applies here too: **6 rows that the grading run itself labelled a defect were awarded
verification.**

**`OPTIONAL_FUNCTION` returns to 0.00% research-verified.** The research below stands; the grade does not.

## 2. Population, verified twice

| Class | rows | via module install | group-gated | activation recorded as "none" |
|-------|-----:|-------------------:|------------:|------------------------------:|
| OPTIONAL MODULE FEATURE | 707 | 606 | 61 | 40 |
| OPTIONAL CORE FEATURE | 263 | 0 | 243 | 20 |

**25 distinct modules and 14 capability groups.** Re-derived twice from two different files, agreeing.

**`OS5-F-00` — 60 rows are classed optional and record no activation condition.** No activation
condition means no deactivation condition, so they cannot meet the standard. **Recorded as a register
defect and left visible.** Repairing it silently would change a population.

## 3. The structural finding

> **Module deactivation is destructive. Capability-switch deactivation is not.**

| | Module uninstall | Capability switch off |
|---|---|---|
| Schema | **tables dropped, columns dropped, with cascade** | **none** |
| Stored values | **destroyed** | **always survive** |
| Dependents | **force-uninstalled with it** | unaffected |
| Deletion guards | **skipped** | not involved |

**40 tables and 278 columns on models the modules do not own** are destroyed across the 25 subjects.
**Not one of the 25 is safe.** Nine of the 14 capability groups are.

**This single result decides module-versus-switch for every SMEsPlus capability.**

## 4. The safety matrix — §10's required form

### `OS5-F-01` — capability OFF, capability still active
| | |
|---|---|
| **Expected** | turning a capability off withdraws it from everyone |
| **Observed** | the switch removes an **implication** on the holder group and never a **direct** membership. Confirmed at runtime: **8, 7 and 6 gates** on the three current-generation deployments are held directly with no implication |
| **Risk** | **HIGH.** A capability believed withdrawn remains exercisable |
| **Root cause** | the switch operates on the holder's implication list; the settings display reads the same list, so display and reality diverge together |
| **Impact** | mostly role groups, where direct assignment is intended. **Two capability gates on the transacted deployment are affected**, one of them multi-company |
| **SMEsPlus implication** | a switch must revoke what it grants, and its displayed state must be computed from **actual holders** |
| **Required control** | on switch-off, enumerate and revoke every holder; recompute the displayed state from membership, never from an implication |

### `OS5-F-02` — module removal destroys structures it does not own
| | |
|---|---|
| **Expected** | uninstalling a module removes the module |
| **Observed** | **278 columns on foreign models dropped with cascade**; fields on surviving models unlinked when their target is removed; **deletion guards declared not to run at uninstall are skipped** |
| **Risk** | **HIGH** — silent, irreversible history loss |
| **Root cause** | ownership is per-column, and the uninstall path is schema-level |
| **Impact** | landed costs: **the posted entries survive and the documents that explain them do not** |
| **SMEsPlus implication** | capability boundaries must not be schema boundaries; removal must never be a destructive default |
| **Required control** | a capability may add columns only to models it owns; anything else is a relation |

### `OS5-F-03` — silent behavioural degradation
| | |
|---|---|
| **Expected** | removing expiry handling disables expiry handling |
| **Observed** | **FEFO silently becomes FIFO.** The strategy record is deleted, the referencing fields are set to null, and the resolver falls through — **no error, no log**. 15 columns of expiry history destroyed, and expired stock **returns to available quantity** |
| **Risk** | **HIGH** — wrong stock is picked and nothing reports it |
| **Root cause** | a strategy modelled as a record contributed by an optional module, with a silent fallback |
| **SMEsPlus implication** | a removal strategy is a first-class value, not an optional record |
| **Required control** | an unresolvable strategy must **refuse**, never fall back |

### `OS5-F-04` — deactivation that does not stay deactivated
Three subjects declare auto-install; every dependency is a re-install trigger, so uninstalling one is
**reverted the next time any dependency is installed**. A second mechanism that might have resurrected
them on a routine update was tested and ruled out — reachable only at database creation. **A determined
negative.**

### `OS5-F-05` — configuration display differs from capability state
Covered by `OS5-F-01`; recorded separately because it is the **user-visible** half: the interface is not
merely incomplete, it is **wrong**, and a person acting on it believes a capability is off.

### `OS5-F-06` — 220 sites where an optional module changes core behaviour
Every one of the 25 overrides at least one method on a model it does not own; **31 are
create/write/delete-level**. The concentration is the transfer-completion path — three subjects override
the pre-completion hook. **Whether a transfer can be completed depends on which optional modules are
installed.**

## 5. Ranking

**Destructive:** expiry handling · the routing-operations switch · the work-order-dependencies switch ·
subcontracting · the delivery module (83-module cascade).
**Lossy:** the remaining 20 modules.
**Safe:** **none of the 25 modules.** Nine of the 14 capability groups.

## 6. Why the dimension is 0.00%

§9 requires **twenty** attributes per optional function, per element — activation trigger and
configuration, module and dependency, six impact axes, deactivation behaviour, historical data,
fallback, silent degradation and residual automation. **All of that is established per subject. None of
it is established per element**, and the previous round's grade came from asserting that the second
follows from the first.

**Subject-level knowledge is real and it is not element-level verification.**
