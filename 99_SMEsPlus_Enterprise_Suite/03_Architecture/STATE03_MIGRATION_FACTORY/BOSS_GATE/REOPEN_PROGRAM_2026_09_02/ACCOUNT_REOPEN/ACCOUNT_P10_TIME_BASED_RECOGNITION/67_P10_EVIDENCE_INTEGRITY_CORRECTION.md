# P10 — EVIDENCE INTEGRITY CORRECTION

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Corrections `P10-R-14` .. `P10-R-22`, raised by challenge classes **A** and **B** against **this round's own repair documents**.

> **The headline conclusion survives, independently re-derived: exactly one company row in the four examined databases carries a period lock.** Everything supporting it needed repair.

---

## 1. The Denominator — `P10-R-14`

| | |
|---|---|
| **Written** | *"1 of 90 companies in the readable deployed estate has any period lock configured"* |
| **Wrong because** | Databases A and B contain **identical company sets** — 44 rows each, intersection 44, union 44. They are two restores forked from one ancestor tenant: different database identifiers, but every company row carries the same creation timestamp, and an earlier snapshot of the same lineage holds one company, the next holds two, the current holds 44. **The union across all four databases is 46 distinct companies, not 90** |
| **Corrected** | **1 of 46 distinct companies** (unit = company), or **1 of 90 company-rows across four database images** (unit = company-instance). Both are true; they are different units |
| **Defect class** | The programme's count-unit-versus-population defect — **in the document written to repair a denominator** |

## 2. The Population — `P10-R-15`

| | |
|---|---|
| **Written** | *"TRUE POPULATION: 10 snapshot files · 7 distinct snapshots · 4 distinct databases"*, under a declared population of *"every deployed-database artefact reachable on this host"* |
| **Wrong because** | The declared population is host-wide; the executed sweep covered **three directories**. A host-wide search finds **23 archive files** in the user's home alone, and magic-byte verification finds **27 archives plus four plain-SQL backup containers**, spanning at least **nine further deployed databases** — a simulation lab of six, a demonstration instance, and three unrelated production-named databases |
| **Corrected** | **The population is a FLOOR, not a total. At least 10 archives across at least 9 databases exist within the declared population; P10 examined 4.** |
| **Defect class** | **Declared-pattern-not-run, fourth occurrence — in the document that declares its own pattern and states that the prior round's globbing "is corrected here"** |

The four examined remain the four the package's findings rest on. **Their selection is now unjustified by the declaration that admitted them**, and no scope-narrowing predicate was ever stated.

## 3. The `raw/` Directory Is Not Raw — `P10-R-16`

Two of the four files under `raw/` are **authored prose, not captured transcripts**. Re-running the shipped probe produces different hit counts from those the file reports — 5 where the file says 10, 3 where it says 16 — because the file mixes numbers obtained by a different command with annotations the script never prints.

> **A directory named `raw/` must contain transcripts. Prose belongs in Layer 1 with its command beside it.** Two artefacts are re-labelled; the two genuine transcripts reproduce byte-identically.

## 4. The Positive Control Was Asserted and Not Executed — `P10-R-17`

The package states that the lock-date zeros carry a control of *"sibling columns populated in 44 of 44, with sample values"*. **The shipped probe prints no sibling column and no sample value.** It prints the lock columns and the row count.

Both challenge classes supplied the missing control independently and **the zeros are read zeros** — creation timestamp, name and currency all populated 44 of 44, and, more strongly, a **lock-family sibling** column populated in every row of every archive.

**The conclusion stands on someone else's control.** P10 asserted an evidence property it did not produce.

## 5. The Byte-Size Control Cannot Do What Was Claimed — `P10-R-18`

The package reasons: *"913 bytes = header only, i.e. the table is genuinely empty, not a failed extraction."*

**Executed test:** extracting a **table that does not exist** exits successfully and writes a 722-byte preamble. The empty-table artefacts are 913–915 bytes and the absent-table artefact is 722. **Byte size cannot separate them**; the package's conclusion is right by a 191-byte margin it never examined.

> **The correct control for "the table exists and is empty" is the presence of the `COPY <table> (…) FROM stdin;` line.** One line, not shipped. And the probe **did** print a byte size for an absent table on one archive, in the same format used for real extractions.

This is a **third** distinct defect in the same family: `R-08` is *not looking*; the extraction-review gap is *not reading what you have*; this is **a control that cannot detect the failure it was adopted to detect**.

## 6. Four Further Corrections

| # | Written | Corrected |
|---|---------|-----------|
| `P10-R-19` | *"The newer lock columns do not exist on"* the older-line database | **Class `E`.** Three lock columns exist there, including a differently-named period-lock field found on no other archive. The zero is real; **the explanation carried to the Boss was false**, and it is the explanation that carries the "cannot fire here" argument |
| `P10-R-20` | Company-table column counts 195 / 188 / 141 / 263, used as the product-line indicator | **Class `E`.** True: **194 / 187 / 141 / 259**. The probe counted trailing table constraints as columns. The four-distinct-shapes conclusion survives on corrected numbers; the published numbers were a parse artefact, and one of the four was computed on a different basis from the other three |
| `P10-R-21` | *"D is not a production database — ten journal entries"* | **Class `E`.** The discriminator was never computed for the comparison group. Counted: **A has 16 journal entries, B has 6 against 44 companies, D has 10, C has 183,590.** On P10's own metric **B is less production-like than D**. Only one database carries production volume |
| `P10-R-22` | *"769 asset schedules"*, then corrected to *"669 real assets"* | **Still imprecise.** Of the 669, **three are cancelled or draft and two are closed** — not schedules that generate entries. The state column was read for one bit and its other four values discarded |

## 7. What the Challenges Obtained That P10 Had Declared Unobtainable

**The installed-module manifests were extracted from containers sitting in P10's own primary path set.**

| Fact | Value |
|------|-------|
| **Deployed major version** | **19.0+e** — a fact the package never states anywhere |
| **Deployed database engine** | PostgreSQL 15 |
| Installed modules | 251 / 216 / 179 across three snapshots |
| **Thai localisation modules installed** | **Nine**, named |

> The localisation surface the package routed as *"class `C`, would bound the localisation surface"* **is now bounded**, by opening a file that was in the directory the sweep was supposed to cover.

## 8. One Item Could Not Be Obtained, and Why

A snapshot dated **2026-08-26** — newer than anything P10 read — exists on the host inside a private messaging application's media store. **Reading it was refused by this session's permission controls, and no attempt was made to work around that.**

> **Consequence, stated plainly: "no lock exists in the estate" is a statement about four images dated between 2026-07-11 and 2026-08-03. It does not reach 2026-08-26.** The package's own prohibited-phrasing rule — that exposure may not be claimed without evidence — **applies symmetrically to the negative claim**, and did not.

## 9. What Survived

| Claim | Status |
|-------|--------|
| **Exactly one company row carries a period lock** | **FACT VERIFIED** — independently re-derived by two challenges across four archives plus three additional snapshots |
| Database D: 10 journal entries, 0 asset-linked, 0 deferral entries | **FACT VERIFIED**, with adequate controls |
| The deferral mechanism is absent from the older-line database | **FACT VERIFIED** — no `COPY` line for its relation table |
| The lock values are unaffected by the column mis-count | **FACT VERIFIED** — constraints are trailing, so indices did not shift. **Luck, not design** |
| The re-date cannot fire in the databases examined | **Stands**, on a corrected denominator and a corrected explanation |
| The deployed estate has generated **no deferral entry** | **FACT VERIFIED** across every archive carrying the structure |

## 10. Correction Arithmetic — this round

| | Count |
|---|-------|
| Corrections raised this round | **22** |
| Against the round's own repair documents | **9** |
| Found by P10's own review | **2**, both peer-prompted |
| Found by the four split challenge classes | **20** |
| Of which by the two classes P10 had never run before (evidence base, method) | **13** |

**The two challenge classes that had never been run before found more defects than the two that had.** That is the strongest available argument for the split protocol, and it is also the strongest available argument against trusting any round in which they were not run.
