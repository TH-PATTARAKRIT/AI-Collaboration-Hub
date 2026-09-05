# 28 — P02 POPULATION CLOSURE AND THE FOUR-GENERATION DEPLOYED MEASURE

`LAYER 2 — AUDIT QUARANTINE.` Reference-system observations. Not clean-room input.

**Status: `POPULATION CLOSED AS A PATH-SET QUESTION`. Terminal state UNCHANGED — no blocker closed,
no merge, no freeze.**

---

## 1. What This Closes, And What It Does Not

Population had been **OPEN** since `RE-20`, and P02 had stopped publishing a count because every one it
had published (5, 6, 8/5, 16/7) was superseded. The background content-test sweep has now completed.

**Closed:** the *path set*. Every file larger than 1 MB on this host was tested **by signature, not by
extension** — `16,624` candidates — yielding **39 database-bearing artefacts**. A second, independently
written traversal located paths for all 39. Two instruments, same 39.

**Not closed:** whether the host is the population. This is what is on **this machine**. It is not a
statement about the customer estate, and no claim here should be read as one.

---

## 2. Artefacts Are Not Databases

The 39 artefacts resolve to **17 distinct databases**, keyed on `ir_config_parameter → database.uuid`
— never on filename, business name, or content hash.

| Ratio observed | Meaning |
|---|---|
| `occ_sim` — **7 artefacts, 1 database** | snapshot series of one lab |
| `iTEST02` — **10 artefacts, 1 database** | the same database copied across locations |
| `iEVING` — **2 artefacts, 2 DIFFERENT uuids** | **one business name, two distinct databases**, four months apart |

**`P02-F-28a`.** The `iEVING` case is the argument for uuid-keying, stated as a measurement rather than
a principle: a name-keyed sweep would have reported **one** database here and silently discarded a
distinct one. P04 warned that seven files were one database; the inverse error is equally available and
was present in this population.

---

## 3. Instrument, And Its Controls

Three predicates, all executed offline by `pg_restore -a -n public -t <table>` — **no server started,
nothing restored, no database written**. Column positions are read from each table's `COPY` header **by
name**, never assumed.

| # | Predicate | What it measures |
|---|---|---|
| **A** | `account_move_line.display_type = 'cogs'` | the invoice-side mechanism marker — **the package's headline invariant** |
| **B** | lines posted to accounts typed `expense_direct_cost` | lines on cost-of-revenue-typed accounts, **from any source** |
| **C** | `stock_valuation_layer` rows, and those carrying an `account_move_id` | whether automated valuation posted an accounting entry |

**Control 1 — reproduction of published figures, from the archive, by a separately written extractor.**
`DB-11`'s five marker values reproduce **to the digit**: `product` 381,115 · `payment_term` 39,997 ·
`tax` 25,383 · `line_note` 827 · `line_section` 62 — summing to **447,384**, the published total exactly,
with `cogs` absent. `DB-12` and `DB-13` likewise: **74,982** layers, **57,863** carrying entries.

**Control 2 — per-database injection.** For every database, one synthetic line carrying
`display_type = 'cogs'` is appended and the predicate re-run. **It fires on all 17.** A zero here is a
measured zero, not a silent instrument.

## 4. The Measure

| uuid | gen | database | journal lines | `cogs` | inject. control | type-B lines | SVL table | layers | with entry |
|---|---|---|---|---|---|---|---|---|---|
| `5d5164c4` | 14.0 | odoo_cff_golive_99 | 1,708,287 | **0** | fires | 241,440 | present | 434,152 | 382,163 |
| `25e88cd4` | 14.0 | iErpOCC | 352,350 | **0** | fires | 33,315 | present | 107,202 | 69,655 |
| `45a8e08e` | 16.0 | iSMEs | 447,384 | **0** | fires | 49,957 | present | 74,982 | 57,863 |
| `a1cdeab8` | 16.0 | e8db984d-56e7-489f-80db- | 1,083 | **0** | fires | 48 | present | 1 | 0 |
| `f7d803dc` | 16.0 | iSMeO2C | 0 | **0** | fires | 0 | present | 0 | 0 |
| `6d633b80` | 16.0 | iSCErP | 0 | **0** | fires | 0 | present | 0 | 0 |
| `551ab874` | 18.0 | 4e640e74-6222-4a51-bbcb- | 39,840 | **0** | fires | 7,310 | present | 47,242 | 0 |
| `1d1f5d3e` | 18.0 | iSMEs182 | 3,408 | **0** | fires | 1,704 | present | 1,704 | 1,704 |
| `4b766580` | 18.0 | pankhamhom | 956 | **0** | fires | 31 | present | 201 | 124 |
| `57d32e15` | 18.0 | premiumflexiblepackaging | 5 | **0** | fires | 0 | present | 56 | 0 |
| `96548e18` | 18.0 | T805efaplus | 0 | **0** | fires | 0 | present | 0 | 0 |
| `9138b764` | 18.0 | premiumflexiblepackaging | 0 | **0** | fires | 0 | present | 0 | 0 |
| `a6664233` | 18.0 | occ_sim | 0 | **0** | fires | 0 | **absent** | - | - |
| `66d1b52a` | 19.0 | BK12MAY26 | 563 | **0** | fires | 516 | **absent** | - | - |
| `a1430edc` | 19.0 | iTEST02 | 23 | **0** | fires | 1 | **absent** | - | - |
| `1f6338ae` | 19.0 | iEVING | 15 | **0** | fires | 0 | **absent** | - | - |
| `f4a44cce` | 19.0 | iEVING | 0 | **0** | fires | 0 | **absent** | - | - |
**Total journal lines measured: 2,553,914 across 17 databases and 4 generations.**

---

## 5. Findings

**`FACT VERIFIED` — `P02-F-28b` (the invariant, now on a four-generation base).**

> **`display_type = 'cogs'` does not occur once — in any of 17 distinct deployed databases, across
> generations 14.0, 16.0, 18.0 and 19.0, over 2,553,914 journal lines.** Every one of the 17 zeros is
> individually injection-controlled.

The published position was *at least 10 distinct databases across 3 generations*. That was stated as a
floor and the floor holds; it is now **17 across 4**. **Generation 14.0 was not previously known to the
package at all**, and its schema differs — cost-of-revenue is reached through `user_type_id →
account_account_type`, not the `account_type` column every later generation uses, so the predicate had
to be rewritten for it rather than assumed portable.

**`FACT VERIFIED` — `P02-F-28c`: v19 deletes the valuation layer, confirmed in deployed reality.**
`stock_valuation_layer` is **absent from all four deployed 19.0 databases**. Until now this was a
source-only claim about the reference tree. It is now observed in deployments.

**`FACT VERIFIED` — `P02-F-28d`: outcome 3 measured directly, not inferred from configuration.**

| database | gen | valuation layers | layers carrying an accounting entry |
|---|---|---|---|
| `551ab874` `idemo18_uat` | 18.0 | **47,242** | **0** |
| `57d32e15` `pfp-staging` | 18.0 | **56** | **0** |

Against a spread that runs to **100%** (`iSMEs182`, 1,704 of 1,704), **88%** (`odoo_cff`, 382,163 of
434,152), **77%** (`iSMEs`, 57,863 of 74,982) and **65%** (`iErpOCC`, 69,655 of 107,202). **The
instrument plainly finds non-zero where non-zero exists**, so these two zeros discriminate.

This is `P02-F-05` outcome 3 — *cost of sales recognised nowhere* — **observed as an outcome and
counted**, where the package previously inferred it from configuration (`property_valuation` unset on
126 categories). **47,242 valuation events produced not one accounting entry**, and nothing in the
system reports this.

---

## 6. Corrections Made During This Round

**`RE-25` — an instrument defect that produced two uncontrolled zeros.** The injection control built a
40-field row, while v14's `display_type` sits at **column 45 of 66**. The synthetic line therefore never
carried the marker and the control returned **0** — reported as a zero that had *not* been controlled.
Both v14 databases were re-measured with the injection sized to the actual column count; both now
control (`fires`) and both remain `cogs = 0`. **A control that cannot fire is indistinguishable from a
control that found nothing, which is the failure this package has now recorded four times.**

**`RE-26` — a predicate stated more strongly than it measures.** Predicate **B** was first described as
discriminating *cost at delivery* from *cost nowhere*. **It does not.** Accounts typed
`expense_direct_cost` receive lines from vendor bills and manual entries as well as valuation postings,
so `idemo18_uat`'s 7,310 type-B lines are **not** evidence that delivery-side valuation posted — and
indeed predicate C shows it did not, 0 of 47,242. Predicate C exists because B cannot answer this.
Corrected before publication.

**A near-miss worth recording.** Predicate B, run first, returned **49,957** for `iSMEs` where the
package publishes **zero** — which read as a refutation of the headline. It is not. The package's zero
is the `cogs` **marker**; 49,957 is lines on cost-of-revenue-*typed* accounts, which is exactly what
outcome 2 produces and what deliverable `21` already reports in the same section. **Publishing it as
written would have "refuted" the headline with a figure that corroborates it.** What caught it was
reading the package's own definition of `DB-10` before believing a number of my own.

**`P02-F-28e` — one absence explained, and kept out of the v19 group.** `occ_sim` (18.0) also reports
`stock_valuation_layer` absent. **That absence is module state, not generation:** `stock`,
`stock_account` and `sale_management` are all `uninstalled`, while `account_move_line` has 124 TOC
entries in the same archive, proving it reads. It is **not** counted with the four structural v19
absences. **Consequence for `C-04`:** that lab snapshot is not a perpetual-valuation environment, so the
existing `anglo_gross_profit_test.py` could not run against it as it stands.

---

## 7. What This Does Not Establish

- **Not runtime.** Everything here is posted history and configuration read from archives at rest. **No
  transaction was executed.** `C-04` remains `AUTHORISATION REQUIRED`.
- **Not the customer estate.** Seventeen databases on one host.
- **Not a source-behaviour claim.** The bound of `RE-23` stands: the generation carrying most of these
  transactions has no matching source tree here.
- **No blocker is closed by this round.** It widens and controls the evidence base; it decides nothing.
