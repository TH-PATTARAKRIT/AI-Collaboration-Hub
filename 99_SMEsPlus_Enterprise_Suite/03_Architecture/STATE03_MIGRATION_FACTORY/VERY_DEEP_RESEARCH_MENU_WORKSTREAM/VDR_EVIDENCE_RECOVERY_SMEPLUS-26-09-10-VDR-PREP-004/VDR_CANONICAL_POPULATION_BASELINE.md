# VDR_CANONICAL_POPULATION_BASELINE.md
# Population Version 5 — frozen, and derivable from a published rule

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 04.

---

## 1. Frozen populations

| Population | Count |
|------------|------:|
| `TOTAL_DISCOVERED` | **5,074** |
| `APPLICABLE` | **5,074** |
| `NON_APPLICABLE` | **0** |
| `CONFIG_DEPENDENT` | **946** |
| `OPTIONAL` | **970** |
| `RUNTIME_TESTABLE` | **5,074** |
| `CRITICAL` | **737 distinct** (912 area-memberships across 15 areas; 175 are second or later mappings) |
| **Applicable dimension cells** | **30,870** |

**Every Learning ID appears exactly once**: 5,074 rows, 5,074 distinct identifiers — verified by
enumeration, not asserted.

## 2. The class rule table — nineteen classes, and the denominator is now derivable from it

The previous version's denominator corresponded to **no published rule**: the spec's table yielded
30,921, applying its container rule uniformly yielded 30,836, and the register published 30,906.
**`CONTAINER` is now a published class**, and 30,870 falls out of the table alone.

| Class rule | n | Applicable dimensions |
|------------|--:|----------------------|
| `FIELD` | 1,846 | CONF · OPT · SRC · RUN · DATA · SEC · XMOD |
| `BEHAVIOUR` | 614 | PROC · SRC · RUN · DATA · XMOD · EDGE |
| `GATEDELEM` | 525 | CONF · OPT · SRC · RUN · SEC |
| `VIEW` | 493 | CONF · OPT · SRC · RUN · SEC |
| `BUTTON` | 431 | PROC · CONF · OPT · SRC · RUN · SEC · EDGE |
| `SETTING` | 237 | CONF · OPT · SRC · RUN · DATA · XMOD |
| `ACTION` | 201 | PROC · CONF · OPT · SRC · RUN · SEC |
| `ACL` | 180 | SRC · RUN · SEC |
| `MENUX` | 134 | PROC · CONF · OPT · SRC · RUN · SEC |
| `OBJECT` | 96 | all nine |
| `HANDOFF` | 90 | SRC · RUN · XMOD |
| `RULE` | 46 | SRC · RUN · SEC |
| `MENU` | 45 | PROC · CONF · OPT · SRC · RUN · SEC |
| `GROUP` | 44 | CONF · OPT · SRC · RUN · SEC |
| `CONSTRAINT` | 32 | SRC · RUN · DATA |
| `AUTOMATION` | 26 | PROC · CONF · OPT · SRC · RUN · DATA · XMOD · EDGE |
| **`CONTAINER`** *(new)* | **17** | **SRC · RUN · SEC** |
| `SEQUENCE` | 12 | CONF · SRC · RUN · DATA |
| `SYSPARAM` | 5 | CONF · OPT · SRC · RUN |

`CONTAINER` is a grouping menu node that binds no action. It invokes nothing, so process,
configuration and optional-function are inapplicable — **but it is a record in the deployment's
registry and its visibility is determinable**, so source, runtime and security remain applicable. That
last clause is the correction: the previous round made runtime and security `NA` on containers too,
which would have excluded a record that demonstrably exists.

## 3. Denominator lineage — every version preserved

| Version | Cells | What moved, and why |
|---------|------:|---------------------|
| V3 (PREP-003 R1) | 30,741 | 180 cells `NA`'d **after failing their grade** — unauthorised |
| V3 under its own rule table | 30,921 | what the published rule actually yields |
| V4 (PREP-003 R2) | 30,906 | 180 restored; container rule applied to **3 of 17** |
| **V5 (PREP-004, current)** | **30,870** | container rule applied to **all 17**; runtime + security restored on containers |

**No denominator may change again without closing the measurement round, issuing Version 6, documenting
the delta, and recalculating from zero.** Silent drift is prohibited and, at three versions of visible
lineage, is now also detectable.

## 4. Exclusions

**None.** `VDR_CONTROLLED_EVIDENCE_ADMISSION_REGISTER.md` governs what evidence may enter;
this baseline governs what population is measured, and **nothing has been excluded from it.**
Cells leave a denominator only by the class rule table above.

## 5. Freeze declaration

| | |
|---|---|
| Population Version | **V5** |
| Register | `LAYER2_AUDIT_QUARANTINE/MACHINE_REGISTERS/POPULATION_V5.csv` |
| Rows | 5,074 · distinct ids 5,074 · cells 30,870 |
| Frozen for | the PREP-004 measurement round and its independent challenge |
