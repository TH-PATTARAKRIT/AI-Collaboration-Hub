# 30 — G02-P02 FINAL LINEAGE RECONCILIATION

`LAYER 2 — AUDIT QUARANTINE.` Prompt `[SMEPLUS-26-09-05-G02-P02-O2C-TARGETED-CLOSURE-002]`, task **C1**.
Baseline `ff8be5128483c3ba49b3265f72f1851b6c6bcd64`. **OLD SESSION CONTINUATION — nothing reset.**

**History is not rewritten.** Every original statement below remains in its file. This register records
what superseded it, on what evidence, and what the supersession changes. Where a statement is
*historical narration* of a past state it is marked `NARRATION — CORRECT AS HISTORY`; where it is a
**live claim** still asserting a present fact, it is marked `LIVE — STALE` and corrected in place.

---

## 1. Method

Four disjoint search arms over `00`–`28`, each declared and executed:

| Arm | Pattern | Target class |
|---|---|---|
| A | `no database`, `no runtime`, `no execution`, `no tooling` | evidence-availability claims |
| B | numeric literals: `488,347` `447,384` `40,353` `47,801` `101 evidence` `22 deliverables` `6 of 6` `8 files` `16 artefacts` | count claims |
| C | `two generations`, `both readable generations`, `three generations`, `in either generation` | generation-label claims |
| D | `custom-addon roots`, `wholly unexamined`, `NOT YET SEARCHED` | scope/coverage claims |

**Control.** Arm B's literals were taken from the *superseding* documents (`21`, `26`, `28`) rather than
invented, so a literal that no longer appears anywhere is a signal the arm is mis-specified, not that
the package is clean. All four arms returned hits.

---

## 2. `LIVE — STALE` Statements, Corrected In Place

### L-01 — `03_P02_DELIVERY_COGS_TRACE.md:238`

| | |
|---|---|
| **Original** | *"This session had **no database access** and could not execute it."* |
| **Original evidence** | None. An untested negative about the session's own capability. |
| **Correction source** | `RE-13`, `C-31`, deliverables `21`, `26`, `28`. |
| **Corrected** | The session **has** offline database access to 39 artefacts / 17 databases. What it does **not** have is **authority to mutate a runtime**, which is a different and narrower bound. |
| **Impact** | `C-04` stays open, but **for the correct reason**. Its blocker changes from *evidence absent* to *mutation authority absent* — see `33`. |
| **Layer-1 impact** | None. `19` does not carry this sentence. |

### L-02 — `13_P02_SOURCE_LINK_REGISTER.md:204`

| | |
|---|---|
| **Original** | *"No tooling, no database, no execution."* — as the reproduction instruction for the whole package. |
| **Correction source** | `21`, `28`; `EV-P02-121` … `EV-P02-127`. |
| **Corrected** | Source findings reproduce with read-only shell inspection. **Deployed findings require `pg_restore` 18.6 and the archive path set**, and their reproduction instructions are in `28` §3, not here. |
| **Impact** | A reviewer following §4 alone **cannot** reproduce any deployed finding. This is a reproducibility defect in the register, not in the findings. |
| **Layer-1 impact** | None. |

### L-03 — `15_P02_REVISION_LOG.md:186` (Declared Limitation 1)

| | |
|---|---|
| **Original** | *"No database or runtime evidence. Everything is static-source. `C-04` cannot be closed without it."* |
| **Correction source** | `21`, `28`. |
| **Corrected** | Database evidence is present and extensive. **Runtime** evidence remains absent — and the second clause survives: `C-04` still cannot be closed from static source. |
| **Impact** | The limitation was **half right for the wrong reason**. Splitting it is what makes `33` possible. |

### L-04 — `23_P02_CLOSURE_RECONCILIATION_REGISTER.md:71` (EC-01)

| | |
|---|---|
| **Original** | *"Database denominator closed (6 of 6, deduplicated, positive control)."* |
| **Correction source** | `RE-20`, `RE-22`, `28`. |
| **Corrected** | **Not closed at 6.** The denominator was superseded four further times and now stands at **39 artefacts / 17 databases / 4 generations**, closed **as a path-set question on this host**. |
| **Impact** | `EC-01` is re-derived from scratch in `42`; the old "closed" cell is void. **Declaring a denominator closed is itself a claim, and this one was wrong four times after being declared closed once.** |

### L-05 — `18_P02_PMO.md:60` (EC-08) and `14_P02_EVIDENCE_MANIFEST.md:97`

| | |
|---|---|
| **Original** | *"Twenty-two deliverables, 101 evidence identifiers"* / *"101 evidence identifiers, `EV-P02-001` … `EV-P02-101`"*. |
| **Correction source** | Mechanical enumeration at this baseline. |
| **Corrected** | **29 deliverables** and **`EV-P02-001` … `EV-P02-127`, contiguous, no gaps** — verified with an instrument that reads both the register's bare `\| NNN \|` rows and the full `EV-P02-nnn` form. |
| **Impact** | Counts only; no finding changes. **Recorded because a full-form-only regex reports 7 phantom gaps in this register**, and that instrument defect has now been made twice. |

### L-06 — `26_P02_V18_DEPLOYMENT_EVIDENCE.md:195`

| | |
|---|---|
| **Original** | *"three generations, 488,347 journal lines — zero cost-of-sales entries."* |
| **Correction source** | `28`, `EV-P02-123`. |
| **Corrected** | **Four generations (14.0, 16.0, 18.0, 19.0), 2,553,914 journal lines, zero `cogs` markers**, every zero injection-controlled. |
| **Impact** | **Strengthens.** The claim's direction is unchanged and its base is 5.2× larger. |

### L-07 — `00_README_PACKAGE_INDEX.md:90` (index row for `24`)

| | |
|---|---|
| **Original** | *"across both readable generations"*. |
| **Corrected** | Written when two generations were readable. **Four are now readable**; `24`'s scenarios were analysed against two. |
| **Impact** | **Material — this is a coverage gap, not a wording gap.** Carried into `35` (C6) as the reason each scenario needs its generation basis restated rather than inherited. |

---

## 3. `NARRATION — CORRECT AS HISTORY` (No Correction Required)

| Ref | Statement | Why it stands |
|---|---|---|
| `00:213-214`, `14:110-111` | *"…five deployed archives were on the host"* | Both are explicitly narrating **what `RE-13` found at the time**. The five-archive figure is correct as the state then discovered. |
| `12:148`, `15:60` (`RE-13`) | *"no database or runtime evidence… repeated across six deliverables"* | This **is** the correction entry. Preserving the original wording is required by §3 of the constitution. |
| `18:258-266` | v18 discovery narrative, `40,353` lines | Correct for the artefact then measured. See D-01 below. |
| `22:33` (`TC-02`) | *"SURVIVES, AND IS STRONGER"* | Still true, and now on a wider base. |

---

## 4. Reconciled Discrepancies That Are Not Errors

### D-01 — `idemo18_uat` journal-line count: 40,353 vs 39,840

`18` and `22` publish **40,353**; `28`'s measure returns **39,840** for the same `database.uuid`
`551ab874`. **Both are correct.** They are **two different artefacts of one database** — the
`OCC_BACKUP` snapshot and `4e640e74-…dump` — taken at different times. Similarly `47,801` valuation
layers (`18`, `19`) versus `47,242` (`28`).

**This is recorded, not resolved away.** It establishes a rule the package had not stated: **a
`database.uuid` identifies a database, not a measurement.** Any figure quoted from a deployed database
must name the **artefact**, because two snapshots of one uuid legitimately disagree. Registered as
`P02-F-30a`, and applied throughout `31`–`37`.

### D-02 — `27` §9 heading *"Two v18 Databases Analysed"*

Correct as written for that round. `28` raises the analysed set to 17. No edit; `27` §12 already
carries the forward pointer.

---

## 5. What C1 Changes Downstream

| Consumer | Change |
|---|---|
| `33` (C-04) | Blocker reclassified: **not** evidence-absence (L-01, L-03) but **mutation authority**. |
| `35` (eight scenarios) | Generation basis must be **restated per scenario**, not inherited from a two-generation round (L-07). |
| `37` (risk/blocker) | `EC-01`'s "closed" cell is void; populations re-derived, not inherited (L-04). |
| `42` (PMO) | All counts re-derived (L-05); `EC-08`'s deliverable and evidence figures replaced. |
| `19` (Layer 1) | **No change.** None of the stale statements reached the clean-room file — verified by scan, with an injection control. |

**No finding was withdrawn by C1.** Six statements were corrected, one coverage gap was opened
(`L-07`), and one apparent contradiction resolved into a rule (`P02-F-30a`).
