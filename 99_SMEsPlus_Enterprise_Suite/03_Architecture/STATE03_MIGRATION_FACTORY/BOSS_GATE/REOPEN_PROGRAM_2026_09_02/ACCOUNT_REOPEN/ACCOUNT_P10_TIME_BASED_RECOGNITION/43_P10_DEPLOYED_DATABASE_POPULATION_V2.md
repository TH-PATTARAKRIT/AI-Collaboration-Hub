# P10 — DEPLOYED DATABASE POPULATION, VERSION 2

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D06`.

---

## 1. Enumeration Method — declared and executed

| Element | Declaration |
|---------|-------------|
| POPULATION | Every deployed-database artefact reachable on this host |
| PATH SET | The whole reference volume plus the user's download, desktop and document directories — **enumerated, not globbed** |
| PATTERN | Archive and plain-dump extensions, four variants |
| UNIT | One **snapshot file**; snapshots are then grouped into **distinct databases** |
| TOOL | Database restore utility, **version 18.6**, located by an explicit search of the host rather than by default path resolution |

The prior round declared this population and then globbed **one directory**. That is corrected here.

## 2. The True Population

> **CORRECTED — `67` §2, `P10-R-15`. THIS IS A FLOOR, NOT A TOTAL.** The declared population is host-wide; the executed sweep covered **three directories**. A host-wide search finds **23 archive files** in the user's home alone and, with magic-byte verification, **27 archives plus four plain-SQL containers** spanning **at least nine further deployed databases**. **Declared-pattern-not-run, fourth occurrence — in the document that says it corrects it.**
>
> P10 examined **4**. Their selection is no longer justified by the declaration that admitted them, and no scope-narrowing predicate was ever stated.

**Examined: 10 snapshot files · 7 distinct snapshots · 4 distinct databases. Existing within the declared population: at least 10 databases.**

| DB | Snapshots found | Copies | Note |
|----|-----------------|--------|------|
| **A** | 1 | 1 | plus one archived copy in a compressed container, not extracted — class `C` |
| **B** | **2** — one recent, one four months earlier | 1 each | **time series available** |
| **C** | 1 | 1 | the older product line |
| **D** | **2** — one recent, one a month earlier | recent ×1, earlier ×**4** identical copies in four locations | **time series available**; the four copies are one snapshot |

Four of the ten files are duplicate copies of a single D snapshot. Counting files as databases would have produced **ten**; counting snapshots as databases would have produced **seven**; the correct denominator for a per-database question is **four**.

> This is the programme's count-unit rule applied prospectively rather than after correction: **the unit is declared before the number is used.**

## 3. Per-Archive Record

| Field | A | B | C | D |
|-------|---|---|---|---|
| Readable? | yes | yes | yes | **yes — corrected from "no"** |
| Tool used | restore utility | restore utility | restore utility | **restore utility 18.6, found by explicit host search** |
| Product line indicator (company-table columns) | 195 | 188 | 141 | **263** |
| Companies | 44 | 44 | 1 | **1** |
| Deferral window fields | present | present | **absent** | present |
| Deferral relation structure | present | present | **absent** | present |
| Company deferral configuration | present, all 8 | present, all 8 | **absent** | present |
| Periodic transfer structures | absent | absent | **present** | absent |
| Lock-exception object | present | present | **absent** | present |
| Asset table rows | 36 | 36 | 685 | 12 |
| — of which **templates** (`model`) | **36** | **36** | 16 | **12** |
| — of which **real assets** | **0** | **0** | **669** | **0** | 
| Deferral entries ever generated | **0** | **0** | n/a | **0** |
| Total journal entries | not counted — class `C` | not counted — class `C` | **183,590** | **10** |
| Entries carrying an asset link | not counted — class `C` | not counted — class `C` | **30,038** (17,513 posted) | **0** |
| Evidence class | FACT VERIFIED | FACT VERIFIED | FACT VERIFIED | FACT VERIFIED |

Every count above was produced with the artefact's byte size printed beside it, and every zero carries a positive control.

## 4. What the Reopened Archive Changes

1. **The estate is on at least three product lines**, not two. Four distinct company-table shapes.
2. **D is not a production database.** One company, twelve asset schedules defined, **ten journal entries in total**, none carrying an asset link. It is a test or seed database.
3. **D is the only archive with lock dates set** — see `44`.

## 5. Declared Residual Gaps

> **CORRECTION `P10-R-12` applies to the asset rows above.** They were first published as "769 asset schedules across the estate". 100 of the 769 are **templates**, not assets, and **three of four databases hold no assets at all** — only templates. See `52`.

| Gap | Class |
|-----|-------|
| The compressed container holding a second A snapshot was not extracted | `C — NOT SEARCHED` |
| Total journal-entry counts for A and B were not taken | `C — NOT SEARCHED` |
| The modification history of C's three candidate re-date signatures | `UNRESOLVED — EVIDENCE REQUIRED` |
| The two available time series (B and D) were not differenced | `C — NOT SEARCHED` |
| An installed-module manifest exists in the compressed container and would bound the localisation surface | `C — NOT SEARCHED` |

These are recorded as unsearched, not as absent, and are carried into the unresolved-evidence register.
