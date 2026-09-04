# MCC_E — DENOMINATOR RECONCILIATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Governs `MC-01`, `MC-02`, `MC-04`. Layer 2 citations: `LAYER2_MCC_EVIDENCE/MCC_E01`

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The `41` vs `≥59` mismatch — resolved

The round instruction requires the difference to be attributed to exactly one of: denominator
expansion · reclassification · duplicate elimination · a newly discovered population · an earlier
counting error · a previously hidden unknown class · an inconsistent scope definition.

> ## The answer is **inconsistent scope definition**, and none of the other six.
>
> **`VERIFIED FACT`.** The two figures count **two differently-keyed populations**:
>
> | | `41` | `≥59` |
> |---|---|---|
> | Key scheme | `GAP-*`, `TX-*`, `CL-*`, `FE-*`, `TI-*`, `XM-*` | `MCU-*` |
> | Introduced by | register `21` and its predecessors | file `06`, at the convergence round |
> | Mapping between the schemes | **none exists in any file of the package** | — |
>
> **No arithmetic reconciles them, and none ever could.** Both prior rounds treated the difference as
> a counting dispute and searched for the missing rows. There were no missing rows; there were two
> registers of different things, one of which was created without a crosswalk to the other.

### 1.1 Sub-findings, each verified independently this session

| # | Finding | Evidence |
|---|---|---|
| `E-01` | **Register `21` reconciles exactly to its own count table.** 28 id-bearing rows: A 8 · B 4 · C 7 · D 7 · F 2. Its `Counts` table: 8+4+7+7+2 = 28 | recounted this session |
| `E-02` | The `41` was never reconstructible **because its inputs came from three registers keyed differently**, netted with four items the same report classified as confirmed defects | `G10` §4 vs `C13` §6 vs register `21` |
| `E-03` | The `59` is **24 individually-stated unknowns plus 35 allocated inside three id ranges** with one shared description each. It is a count of id slots | file `06` §2, recounted |
| `E-04` | Five orphan `GAP-*` ids are cited in files `01`–`26` and have no row in register `21`: `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03`. Register `21` holds 14 distinct `GAP-*` ids; files `01`–`26` cite 19 | recounted this session |
| `E-05` | **Neither figure was ever wrong about the *evidence*.** Both were wrong about *what they were counting*. The unknowns themselves were mostly real and mostly stable | comparison of the two registers' contents |

### 1.2 What must happen, and it is not more counting

> A **crosswalk** from the `GAP-*`/`TX-*`/`CL-*` scheme to the `MCU-*` scheme, one row per id, is the
> only artefact that makes any unknown percentage meaningful. It is editorial work of perhaps two
> hours. **Until it exists, no unknown-closure percentage may be published**, and this round
> publishes none.

---

## 2. Independent recount of the source-derived denominators

Fifteen of the twenty-four `D-SRC` denominators were recounted from primary source this session,
using commands written independently of the parent's scripts. Selection favoured the denominators
that carry a conclusion.

| Population | Parent | This round | Result |
|---|---|---|---|
| `P-14` Wave A source files | 18 | **18** | reproduces |
| `P-14` Wave A source lines | 16,044 | **16,044** | reproduces |
| `P-14a` method definitions | 750 | **750** | reproduces |
| `P-10` field declarations | 397 | **397** | reproduces |
| `P-23` explicit failure paths | 153 | **153** | reproduces |
| `P-15a` constraint hooks | 32 | **32** | reproduces |
| `P-15` storage-constraint blocks | 6 blocks | **6 blocks** | reproduces (the *tuple* count is corrected — §3) |
| `P-16` access-control rows | 132 | **132** | reproduces |
| `P-16a` record rules (addon) | 31 | **31** | reproduces |
| `P-09a` menu items | 52 | **52** | reproduces |
| `P-09b` view records | 126 | **126** | reproduces |
| `P-11` window actions | 59 | **59** | reproduces |
| `P-21d` raw-SQL sites | 62 | **62** | reproduces |
| `P-21a` company-domain overrides | 11 | **11** | reproduces |
| `P-21b` privilege-elevation sites | 93 → **94** (corrected in `MCE02`) | **94** | reproduces **the correction**, not the original |

> **15 of 15 reproduce.** `MC-04` repeatability holds for the mechanical layer, for the third
> consecutive independent recount. **The parent round's evidence base is sound. Its scope statements
> were not.** That distinction is the whole of this round's position on the method.

### 2.1 A false divergence this round produced, and caught

The first recount of the access-control rows returned **152** against the parent's **132**. The cause
was this round's own arithmetic — subtracting one header line from the file's total line count while
the file contains **20 blank separator lines**. Counting data rows directly returns **132**.

**Recorded because the failure mode is the finding.** A denominator produced by an expression over a
file's shape, rather than by counting the objects, is not a denominator. It was caught by inspecting
a divergence instead of publishing it — and publishing it is precisely what three prior rounds did
with the `41`.

---

## 3. Denominators that do NOT survive, and the corrected values

| Population | Parent value | Corrected | Basis |
|---|---|---|---|
| `P-10a` database-wide configuration keys | **5, "complete"**, status `CONVERGED` | **6, of which 3 material** | The sixth is the documented bypass of the constraint aligning entry numbering with the accounting date. **Independently re-derived this session** — see §3.1 |
| `P-08a` rate-table scoping rules | **6, "complete"** | **14** over a **20-file** bounded surface | `MCC_B` §5, `MCC_E00` |
| `P-15` storage-constraint tuples | 11 | **9** | `MCX-05`; re-confirmed: the block count 6 is right, the tuple count was not |
| `P-11a` object buttons | 55 | **not reproducible** | withdrawn at `MCE02`; not re-attempted here |
| Addon directories (bounding denominator) | 797, corrected to 791 | **791 primary + 961 archive = 1,752** | `MCC-B-01` |
| `P-25` unknowns | 41, then 59 | **not a single population** — §1 | — |

### 3.1 `P-10a` re-derived, and this round's own pattern fails a third time

Enumerating the configuration-key population by **call site** rather than by literal returns **6**
sites, complete:

| # | Key | Material? |
|---|---|---|
| 1 | presentation — footer display | no |
| 2 | batch size for document generation | no |
| 3 | presentation — invoice terms (Wave B) | no |
| 4 | **suppresses FX-difference posting** | **YES** — database-wide, no company dimension |
| 5 | **bypasses the entry-numbering/date alignment constraint** | **YES** — the sixth key, missed by the parent |
| 6 | **alters reconciliation side effects** | **YES** — database-wide |

`set_param` sites in the accounting addon: **zero.** The keys are read here and written elsewhere.

> ### `MCC-E-01` — the pattern failed again, in a third distinct way, and it was this round's pattern.
>
> The parent's pattern matched single-line `get_param('literal')` and missed a call spanning lines.
> **This round's corrected, multi-line-tolerant pattern matched only single-quoted literals and missed
> the double-quoted one.** Two different regexes, two different blind spots, one population of six.
>
> **The transferable rule is not "write a better regex."** It is:
> **enumerate by the CALL SITE, then READ each site. Never extract the value with a second pattern.**
> The call-site token search returned all six on the first attempt, in both rounds. Only the
> value-extraction step ever failed. Carried to `MCC_K` as `ER-CORE-2`.

---

## 4. Population records — the material denominators, with full definitions

Format per the round instruction. `Last material delta` is the round at which the value last moved.

| Population | Inclusion rule | Exclusion rule | Source of denominator | Count | Evidence | Gap | Unknown | Last delta | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| Wave A source files | The 18 files declaring the 21 Core-Ledger models | tests, translations | `_name` declaration sites | 18 | 18 | 0 | — | `MC` | **CONTESTED** — `MCX-11`/`MCX-12` show the lock dates and a 1,158-line journal extension live outside it. **The definition, not the count, is the defect** |
| Rate-table surface | Files matching the rate model or table token, `.py`/`.xml`/`.csv` | tests, translations, duplicate module copies | declared pattern over 1,752 dirs + core | **20** | 20 | **0** | 0 | **`MCC`** | **HIGH** — three false-negative modes tested, false positives recorded |
| Rate-table scoping rules | Distinct company-scoping expressions over that surface | — | read at each of the 20 files | **14** | 14 | 0 | 0 | **`MCC`** | **HIGH** |
| Config keys | Distinct keys read or written in the addon | — | **call sites, then read** | **6** | 6 | 0 | 0 | **`MCC`** | **HIGH** — method changed, not just the number |
| Shipped rate rows | Every rate record in either tree, manifest-resolved | — | `.xml`/`.csv` scan + manifest | **165** (162 + 3), **0 in `data`** | 165 | 0 | 0 | **`MCC`** | **HIGH** |
| Access rows (addon) | Data rows in the access file | header, blank lines | direct row count | 132 | 132 | 0 | 0 | `MC` | **HIGH** — reproduced 3× |
| Elevation sites | Elevation calls in the addon's model directory | tests | token count | **94** | 94 | **94 uninspected** | — | `MC`+`MCE02` | HIGH count, **ZERO assessment** |
| Raw-SQL sites | Raw-cursor calls in the addon's model directory | tests | token count | 62 | 62 | **62 uninspected** | — | `MC` | HIGH count, **ZERO assessment** |
| Module directories (bounding) | Directories in the source root's module trees | — | directory count | **1,752** (791 + 961) | — | — | — | **`MCC`** | **HIGH — and it moved this round** |
| Unknowns | — | — | **two incompatible schemes** | — | — | — | — | — | **NONE. `PERCENTAGE NOT REPORTABLE`** |

---

## 5. Definitional stability — the harder test, and it fails

A denominator is stable when its **definition** survives contact with new evidence. Counting the same
thing twice is not stability.

| Definition | Challenge | Survives? |
|---|---|---|
| "Wave A source files = the 18 files declaring the 21 models" | The five lock dates, the five effective-lock computed fields, the fiscal-year definition and the FX-difference posting targets all live on the **company** model, outside the 18 | **NO.** The definition selects by *model declaration site*; Wave A's semantics are not confined to the models it declares |
| "The addon tree is the bounding surface for whole-tree negatives" | A second module tree of 961 directories sits in the same source root | **NO** — `MCC-B-01` |
| "The rate-table surface is the accounting addon plus the framework" | The surface includes a reporting addon, a live-feed addon, a spreadsheet addon, a subscription-reporting addon and two archive-tree localisations | **NO — and this round fixed it by declaring a pattern over a proven path set** |
| "Access rows = file lines minus the header" | The file contains blank separator lines | **NO** — §2.1 |
| "The config-key population = single-line `get_param('…')` matches" | A multi-line call, and a double-quoted literal | **NO, twice** — §3.1 |

> ### `MCC-E-02` — five of five definitions tested failed. The failure is always the same shape.
>
> **Every one of them defined a population by a *proxy for the source* — a path, a file shape, a
> regular expression, a model-declaration site — rather than by the source itself.** The proxy is
> always narrower than the thing, and always in a direction the author cannot see, because the author
> chose the proxy.
>
> **This is the general form of `GB-04`, `GB-07` and `ER-CORE`, and it is the single most transferable
> result available from this programme.** It is carried to `MCC_K`.

---

## 6. Reportable percentages

| Metric | Value |
|---|---|
| Source-derived denominators reproduced under independent recount | **15 of 15 (100%)** — denominator: the 15 selected for recount, listed §2 |
| Rate-table surface evidence coverage | **20 of 20 files (100%)** — the only population in the programme at full evidence coverage |
| Rate-table scoping-rule assessment | **14 of 14 (100%)** |
| Config-key assessment | **6 of 6 (100%)** |
| Gating-unknown closure | **8 of 17 (47.1%)** — denominator: the inherited gating set, §`MCC_D` |
| Elevation-site assessment | **0 of 94 (0%)** |
| Raw-SQL-site assessment | **0 of 62 (0%)** |
| Whole-package evidence coverage | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` (the parent's 95.5% is invalidated by an unapplied correction notice) |
| Unknown closure across the package | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` (two incompatible id schemes, no crosswalk) |
| Contradiction resolution | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` (the metric was widened at the parent gate; `MC-07`) |

---

## 7. Verdict on the denominators

> ## `PARTIALLY VERIFIED`
>
> **The counts are sound and reproduce.** Fifteen of fifteen, on a third independent recount, by a
> reviewer with no stake in them.
>
> **The definitions are not.** Five of five tested definitions failed, always by substituting a proxy
> for the source. Four denominators changed materially this round, and one of them — the bounding
> denominator for every whole-tree negative claim in the programme — changed because a second module
> tree was found in the same directory that everyone had been searching.
>
> **A denominator that moves when you look at it more carefully is not yet a denominator.**
> `MC-01` cannot be `MET`.

---

## 8. CORRECTION NOTICE — applied before the round closed

> **`GB-06`'s remedy, exercised.** Governing record: `LAYER2_MCC_EVIDENCE/MCC_E01`.

| # | Claim in this file | Correction |
|---|---|---|
| `E-C1` | §2 "`P-21b` privilege-elevation sites — 93 → **94** (corrected in `MCE02`) · this round **94** · reproduces **the correction**" | **WRONG, AND THE CORRECTION IT ENDORSED IS ALSO WRONG.** Under the parent's **declared** pattern the count is **93**; **94** arises only from a looser pattern that additionally matches the single de-elevation call. The parent's original **93** was right and `MCE02`'s `MCX-06` correction to 94 is **NOT PROVEN**. Independently reproduced by a fresh reviewer running the declared command verbatim. **Recount result is therefore 15 of 15 reproducing the ORIGINAL figures, not 14 plus a correction** |
| `E-C2` | §2 recount table, `P-13` not listed | **A DENOMINATOR THAT DOES NOT REPRODUCE WAS OMITTED FROM THE RECOUNT.** `P-13` "Wave A models = **21**" is published as source-derived. A mechanical enumeration of model declarations over the same 18 files returns **22**. The omitted model creates and links journals and is one of the nine enabling company-consistency checking. **`P-13` is author-derived wearing a source-derived label** — the one thing the convergence round was convened to eliminate, in the canonical matrix |
| `E-C3` | §3 "Addon directories — 791 primary + 961 archive = **1,752**" | **CORRECTED to 791 primary directories + 962 manifested modules outside them** (959 archive + 3 directly under the source root). The directory figure and the module figure are different populations and this file conflated them |
| `E-C4` | §5 "five of five definitions tested failed" | **SIX of six.** A sixth failed in this round's own hands after the table was written: the **unit of count** over a bounded population was never defined, so two disciplined enumerations of the same surface returned 12 and 14 |
| `E-C5` | §4 population table, "Shipped rate rows — 165, 0 in `data`" | **The `data` figure STANDS** and was independently reproduced across four version trees. **The characterisation of the demo rows as company-less is WITHDRAWN** — the loader supplies the model default. See `MCC_E01` `MCCX-01` |
| `E-C6` | §7 verdict | **UNCHANGED — `PARTIALLY VERIFIED` — and better evidenced.** A third and fourth independent recount now stand behind the counts, and two further definitional failures stand behind the verdict on the definitions |

### `MCC-E-03` — the sixth definitional failure, and it is the most transferable one

> **A population can be bounded, its path set proven, its pattern declared and its false-negative modes
> tested — and two careful enumerations will still disagree, because nobody said what one member IS.**
>
> Over the identical 20-file rate-table surface: **12** distinct scoping *expressions*, **14** *sites
> bearing an expression*, **29** *read/write sites* if write-side and UI-domain sites are separated.
> All three are correct answers to three different questions that were never distinguished.
>
> **Rule: a denominator is `POPULATION + PATTERN + PATH SET + UNIT`. Three of the four have been
> learned in this programme, one per round. The fourth is stated here for the first time.**
