# P10 — DEPLOYED EVIDENCE CORRELATION (STAGE E)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
**Added after the rest of the package was written and pushed.** See `14_P10_REVISION_LOG.md` `P10-R-08` for why, and what it corrects.

Stage E of the canonical acquisition flow requires material facts to be correlated across evidence layers. The package originally declared that only one layer was available. **That declaration was wrong.** Deployed database evidence existed on the execution host and was readable. This document is the correlation the package should have contained from the start.

---

## 1. Population and Method

| Element | Declaration |
|---------|-------------|
| POPULATION | Every deployed database archive available on the execution host |
| PATH SET | The host's download directory, enumerated — not assumed |
| PATTERN | Schema extraction from the archive without a running server, then targeted per-table data extraction for the small recognition tables |
| UNIT | One deployed database |
| SCRIPT | `p10_scripts/p10_enum_03_deployed_schema.sh`, shipped and re-runnable |
| CONTROL | **Every zero is printed next to the byte size of the artefact it was counted from**, so an empty extraction cannot be mistaken for an empty table |

Four archives found. **Three readable; one written in an archive format the host's tooling cannot open** — that one is class `C`, NOT SEARCHED, and nothing below applies to it.

## 2. What the Deployed Databases Show

| Fact | Database A | Database B | Database C |
|------|------------|------------|------------|
| Deferral window fields on journal items | present | present | **absent** |
| Deferral relation structure | present | present | **absent** |
| Company-level deferral configuration | all eight settings present | all eight present | **absent** |
| Asset structures | present | present | present |
| Loan structures | present | present | **absent** |
| Periodic transfer structures | **absent** | **absent** | present |
| Chart-of-accounts shape | many-to-many across companies; **no scalar company column at all** | same | **scalar company column, mandatory** |
| Companies in the tenant | 44 | 44 | not examined |
| Companies with deferral accounts or journals provisioned | 43 of 44 | 43 of 44 | n/a |
| Accounts belonging to more than one company | **1** of 544 | **0** of 544 | n/a — structurally impossible |
| Deferral entries ever generated | **0** | **0** | n/a |
| Generation method configured | `on validation` — **all 44 companies** | same | n/a |
| Allocation method configured | 30/360 month basis — **all 44 companies** | same | n/a |
| Companies with asymmetric expense/revenue settings | **0** | **0** | n/a |

## 3. What This Changes

### `P10-F-37` — the deferral function is not present in every deployed database

Database C has no deferral structure of any kind. Any SMEsPlus design, migration plan or reconciliation that assumes the function exists across the estate is wrong for at least one deployed database. Class `A`, scope = that database. This is the same class of finding as the P2P process's discovery that the goods-received-clearing bridge has no physical structure in the deployed databases.

Database C does carry the **periodic transfer** structures that A and B lack. The estate is not on one line of the product; it is on at least two, with **different sets of time-based mechanisms available**.

### The live configuration is the fragile one

All 44 companies in both databases are configured to generate on source-document validation. That is precisely the path that:
- performs **no lock-date check** before generating, so a locked-period recognition entry is silently re-dated (`P10-F-05`);
- has **no catch-up mechanism** (`P10-C-01`, and the correction that scoped it to this path);
- produces a per-document journal shape that the grouped path does not (`P10-F-06`).

**The path the estate actually uses is the one with the weakest period-close and correction behaviour.** The resilient grouped path is used by zero companies. This inverts the practical priority: the grouped-path defects (`P10-F-21`, `P10-S-02`, the cache defect, the duplicate-control defeats) are **latent**, while the validation-path defects are **live**.

### The realised exposure today is nil, and the defects are intact

- Zero deferral entries have ever been generated in either database, so no wrong recognition exists to correct and there is no deferral data to migrate.
- All 44 companies share one identical configuration, so the allocation-policy scope defect (`P10-S-01`) **cannot currently produce a divergence** — every company would supply the same answer. The defect is intact; its realised risk is zero **until the first company changes a setting**.
- The chart of accounts is effectively unshared — one account in one database, zero in the other, belong to more than one company. So the multi-company grouped-generation defect (`P10-S-02`) would, on today's data, most likely **fail loudly** rather than post silently. That is the safer branch of `P10-C-02` — and it remains, as that entry says, an accident of configuration rather than a control. One shared account already exists.

### Two structural facts that are *not* softened

1. Database A and B have **no scalar company column on accounts at all**. The old, strong guarantee that an account belongs to exactly one company is gone at the schema level; what remains is a relation whose current contents happen to be almost one-to-one.
2. All eight per-direction deferral settings are physically present and independently writable in every one of the 44 companies. The asymmetric-configuration risk (`P10-F-17`) is one settings change away in any of them.

## 4. Effect on the Gate

| Criterion | Before | After |
|-----------|--------|-------|
| `EC-01` Scope Bounded | Four surfaces declared unbounded, including database | Database surface **now bounded** for three of four archives; one archive is class `C` |
| `EC-04` Tolerance-Zero Closed | NOT SATISFIED — defects unreproduced | **Still NOT SATISFIED.** The deployed evidence bounds the *realised* exposure to nil today; it does not reproduce or refute the defects, because reproduction requires executing the code, not reading the data |
| `EC-08` Package Complete | "Cross-layer correlation could not be performed at all" | **Corrected.** Stage E performed across source and deployed-database layers; runtime and UI layers remain absent |

`P10-U-01` and `P10-U-02` move from `UNKNOWN` to **partially dispositioned**: the deployment context that decides their severity is now known; the code behaviour still needs an executing reproduction.

## 5. What This Evidence Cannot Do

It is **schema and stored data**, not behaviour. It cannot show what the code does when it runs. Every finding in `01`–`09` that describes a code path remains source-verified and unreproduced. Reading a database is a layer above reading source; it is still a layer below running the system.

---

# REVISION 2 — THE FOURTH ARCHIVE, AND WHAT P10 EXTRACTED BUT NEVER READ

Revision 1 declared the fourth deployed archive unreadable and classed the question `C — NOT SEARCHED`. **That was wrong, and it was the `P10-R-08` defect recurring inside the document written to correct `P10-R-08`.** Found by independent challenge; every figure below re-verified by P10.

## 6. The Archive That Opens

P10 had run **one** database tool from the default path and inferred a boundary from its error message. **A newer version of the same tool was already installed on the host.** With it, the archive opens: its table of contents lists 26,804 entries; the schema extract is 6.2 MB.

**Standing rule, restated because the earlier formulation was too weak:**

> A negative about your own capability must name **the tool, its version, the search for alternatives, and the command output**. One tool's error message is a result, not a boundary.

## 7. What the Fourth Archive Shows

| Probe | D (the reopened archive) | A | B | C |
|-------|--------------------------|---|---|---|
| Deferral window fields | present | present | present | absent |
| Deferral relation structure | present | present | present | absent |
| Company-level deferral configuration | present | present | present | absent |
| Periodic transfer structures | absent | absent | absent | present |
| Companies | **1** | 44 | 44 | 1 |
| Company-table columns | **263** | 195 | 188 | 141 |
| Asset schedules | **12** | 36 | 36 | 685 |
| Deferral entries ever generated | **0** (artefact 913 B, header only) | 0 (886 B) | 0 (886 B) | n/a |
| **Any period lock set** | **fiscal-year, tax, sale and purchase all set; hard lock unset** | **none on any of 44** | **none on any of 44** | **none** |

## 8. Three Consequences, Two of Which Overturn Revision 1

### `P10-F-37` understated the divergence — the estate is on at least **three** product lines

Revision 1 said two. The company table carries 263, 195, 188 and 141 columns across the four archives. The fourth is a distinct, later line again.

### The live-exposure argument is **withdrawn**

Revision 1, and `29` and `32` after it, argued that the estate runs the silently-re-dating path and is therefore exposed. **A lock violation requires a lock.** No company in A, B or C has one. The defect **cannot fire** in the three databases P10 used to argue exposure, and **can** fire only in the one P10 had excluded.

This does not touch the source finding. It changes what the Boss is deciding: not *how to remediate a live misstatement*, but *which behaviour to specify before the first company closes a period* — a cheaper decision, taken earlier, with a wider option set.

### `NC-25`'s restatement was wrong

The class-`A` claim is about **deferral** entries in one relation table. It was restated in the gate report and the handoff pack as *"zero **recognition** entries"* — P10's own superordinate term. **769 asset schedules exist across the four archives.** Both documents are corrected.

## 9. The Evidence P10 Produced, Sized, and Did Not Read

P10's own shipped script extracts the company table from every archive. The lock-date columns were in **every extract**. P10 reported the artefact's byte size and never printed the columns — then routed the question they answer as *"obtainable and not obtained"*.

> This is the **inverse** of the programme's executed-not-quoted defect: the command ran, the artefact was sized as a control, and **the column that decided the question was never printed.** A byte-size control proves an extraction is not empty. It proves nothing about whether anyone looked inside.

## 10. The Population Was Still Not Enumerated

Revision 1 declared the population as *every* deployed archive on the host, and the path set as *enumerated, not assumed*. **The shipped script globs one directory.** At least three further deployed-database artefacts exist elsewhere on the volume, two of them earlier snapshots of databases already examined — a time series P10 does not have — and one carrying the estate's own authoritative installed-module list.

`NC-32`. The declared-pattern-not-run defect, in the document that declares its own pattern.
