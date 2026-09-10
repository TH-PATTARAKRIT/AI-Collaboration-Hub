# VDR_OPTIONAL_FUNCTION_ACTIVATION_DEACTIVATION_MATRIX.md
# What activation adds, and what deactivation destroys

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 07.

---

## 1. The half that had never been established

Every prior round classified **activation** and left **deactivation** unmeasured — and deactivation was
the reason `OPTIONAL_FUNCTION` could never reach the depth standard. It is measured here, for all 39
subjects: **25 optional modules and 14 capability groups.**

Coverage: **25 of 25 and 14 of 14 in every pass.** Manifest parse 1,433 of 1,433, 0 failures; syntax
index 16,208 files, 0 failures.

## 2. The single most important structural result

> **Module deactivation and capability-switch deactivation are not the same mechanism, and the
> difference is destructive versus reversible.**

| | Module uninstall | Capability switch off |
|---|---|---|
| Schema changes | **yes** — tables dropped, columns dropped | **none.** No schema operation exists on any switch path |
| Stored values | **destroyed** | **always survive** — the switch is a query-time visibility mask |
| Dependent subjects | **force-uninstalled with it** | unaffected |
| Deletion guards | **skipped** during uninstall | not involved |
| Reversible | **no** | usually — with four measured exceptions |

**Anything designed as a module in SMEsPlus inherits destructive removal; anything designed as a
capability switch does not.** That is a design rule derived from measurement, and it is the most
transferable finding in this report.

## 3. Modules — 25 subjects

`tables` = owned models dropped · `cols` = columns dropped from models the module does **not** own ·
`blast` = modules force-uninstalled with it · `ovr` = method overrides on foreign models.

| Module | Licence | tables | cols | blast | ovr | Effect beyond its own records |
|--------|---------|-------:|-----:|------:|----:|-------------------------------|
| delivery | open | 4 | 8 | **83** | 13 | resets the cash-on-delivery payment provider |
| quality_control | **restricted** | 5 | 23 | 13 | 18 | **removes a hard block on completing transfers** |
| mrp_subcontracting | open | 0 | 11 | 9 | **53** | archives locations and operation types; unlinks routes **inside a bare `except: pass`** |
| product_expiry | open | 1 | 15 | 4 | 23 | **FEFO silently becomes FIFO** |
| stock_picking_batch | open | 3 | 14 | 8 | 16 | in-flight deletion guard **skipped** |
| stock_barcode | **restricted** | 1 | 15 | 8 | 11 | deactivation **not durable** |
| mrp_mps | **restricted** | 4 | 17 | 0 | 2 | — |
| stock_landed_costs | open | 3 | 4 | 5 | 4 | **value persists, provenance destroyed** |
| mrp_plm | **restricted** | **8** | 4 | 1 | 10 | — |
| stock_sms · whatsapp_stock | mixed | 1 · 0 | 2 · 1 | 0 | 2 · 1 | write a company-wide flag to false; **deactivation not durable** |
| 10 × delivery carriers | **restricted** | 0–2 | 10–22 each | 0–1 | 1–6 | — |
| stock_dropshipping · stock_fleet · pos_pricer · quality_control_worksheet | mixed | 0–2 | 1–8 | 0–1 | 3–23 | `pos_pricer` calls an **external store** during uninstall |
| **TOTAL** | **17 restricted / 8 open** | **40** | **278** | | **220** | |

**Not one of the 25 is safe.** Every module drops at least one column from a model it does not own —
**278 columns of history destroyed** across the set, on models that survive.

**The restricted-edition axis covers 68% of the module subjects**, including three of the five largest.

## 4. Capability groups — 14 subjects

No schema operation runs on any switch path; stored values always survive. **Nine are safe — nothing
executes on disable.** Four mutate records beyond themselves, and one refuses rather than mutates:

| Group | On disable | Reversible? |
|-------|-----------|-------------|
| routing operations | **mass-archives every routing operation** — an unbounded search-and-archive | **NO.** Re-enable restores only those sharing the single most recent modification timestamp. **Asymmetric by construction** |
| work-order dependencies | elevated write clearing a flag on all matching bills of material | not restored, and it **fires on every settings save while the flag is off** — it has no previous-state guard, unlike the other three |
| multi-location | archives an internal operation type on warehouses already in a simplified flow | **yes**, symmetric. No location record is touched |
| by-products | toggles a quality test type | **yes**, symmetric |
| production lot | **refuses**: raises an error if any product is still tracked | n/a — it never mutates |

> **The asymmetric one is the finding.** A switch whose *off* path archives an unbounded set and whose
> *on* path restores only the most recently touched subset is not a toggle; it is a one-way door
> wearing a toggle's interface. Any SMEsPlus capability switch must restore exactly what it suspended.

## 5. Where value or quantity effects outlive the module — the four cases

### `OD4-F-01` — FEFO silently degrades to FIFO, with no error and no log
The expiry module contributes a single removal-strategy record. On uninstall that record is deleted;
the strategy fields on locations and product categories declare no delete behaviour, so the framework
**sets them to null**, and the strategy resolver falls through to first-in-first-out. **Every
FEFO-configured location and category silently becomes FIFO. Picking order changes permanently and the
configuration cannot be recovered.** 15 columns of expiry history are destroyed with it, and removing
the module's availability computation **returns expired stock to available quantity**.

> The researcher's own prediction here was a hard error, on the strength of a raise elsewhere in the
> strategy resolver. **The prediction was wrong and the tested result was published instead** — the
> strategy string cannot survive to reach that raise, because the record carrying it is deleted first.

### `OD4-F-02` — landed costs: the books keep the adjustment, the reason disappears
Validation posts accounting entries and writes value onto movements through the valuation-accounting
module. Those entries and the resulting value rows are owned elsewhere and **survive**. The landed-cost
documents, their lines and the valuation-adjustment lines are **dropped**, along with the flag that
marks an accounting line as a landed-cost line. **The value persists; the record of what was adjusted
and why is gone.**

### `OD4-F-03` — quality control: uninstalling removes a completion gate
The module raises a hard error on transfer completion while checks are outstanding, and gates the
pre-completion hook. Remove it and **transfers that were blocked complete freely.** Cancellation also
unlinks pending checks.

### `OD4-F-04` — subcontracting: a silent-failure uninstall path
Its uninstall hook clears warehouse route references, archives locations and operation types, then
attempts to unlink the routes **inside a bare catch-all that passes**. On failure — the code's own
comment names the case, a route still in use by a rule — **an active, now-unreferenced route is left
behind with no error and no log line.**

### `OD4-F-05` — three modules cannot be durably deactivated
Three subjects declare auto-install. Every dependency becomes a re-install trigger, so uninstalling one
is **reverted the next time any dependency is installed**. Deactivation is not a stable state for them.
*(A second mechanism that might have resurrected them on a routine update was tested and ruled out —
it is reachable only at database creation. A determined negative.)*

### `OD4-F-06` — 220 sites where an optional module changes core behaviour
Every one of the 25 overrides at least one method on a model it does not own. **31 are create/write/
delete-level** on foreign models. The concentration that matters is the transfer-completion path: the
pre-completion hook is overridden by three of the subjects, the completion action by two, and the
validate button by one. **Whether and how a transfer can be completed depends on which optional modules
are installed.**

Only 4 deletion guards exist across the 25, and **3 of them are skipped during uninstall** — including
the one that normally refuses to delete a completed batch.

## 8. Corrections to the register this measurement forced

| Correction | Detail |
|-----------|--------|
| The 25 modules supply **606** of the 707 optional-module rows, not all 707; 61 are group-gated | counting rows, not activation tokens |
| The 14 groups supply **243** of the 263 optional-core rows, not all 263 | as above |
| **60 rows are classed OPTIONAL yet record no activation condition** | an internal contradiction in the register: no activation condition means no deactivation condition. **Recorded as a defect, not silently reconciled** |
| **5 of the 14 group subjects were recorded as settings-field names, not group identifiers** | any search keyed on the register's strings returns a **false zero** for those five. The true identifiers were read from the security declaration |
| **The dedicated valuation-ledger model does not exist in the current generation at all** | it is replaced by a differently-named object owned by the valuation-accounting module. **Any analysis keyed on the old name returns a false zero in this generation** — independently corroborating this round's valuation re-derivation |

## 9. Ranking

| Class | Subjects |
|-------|----------|
| **Destructive** — irreversible loss beyond the module's own records | product expiry (FEFO unrecoverable) · routing-operations switch (asymmetric mass archive) · work-order-dependencies switch (unguarded elevated write) · subcontracting (silent-failure hook) · delivery (83-module cascade) |
| **Lossy** — core records survive, contributed detail destroyed | the remaining 20 modules |
| **Safe** | **none of the 25 modules.** 9 of the 14 capability groups |

## 10. What is not determinable from source, and what would settle it

1. **Whether any of this has fired on a real deployment** — everything above is source semantics. Settled by module-state history plus a column-existence check against a deployment.
2. **Whether the 60 contradictory register rows are a classification defect or genuinely optional-with-no-switch** — settled by re-running the classifier and inspecting its fallback branch.
3. **704 relational field sites (8.7% of 8,124) whose target is supplied dynamically** and is statically unresolvable — settled by a loaded-registry dump.
4. **Whether the subcontracting silent-failure path actually fires** — depends on live rule state; settled by counting rules referencing a subcontracting route on a deployment.
5. **Fields declared outside code, and manually created fields** — outside the syntax-level pattern used.

Each is a bounded measurement with a named instrument. **None is a question for the Boss.**
