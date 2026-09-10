# VDR_PRIOR_WORKFLOW_COMPLETENESS_RECHECK.md
# Re-checking the prior workflow corpus — and re-checking the re-check

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Commissioning instruction §12: recheck prior workflow completeness.

---

## 1. Scope of this recheck

Two objects are rechecked, not one:

1. the **prior workflow corpus** — `[SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]`, 26 files, 5,193
   lines, 29 menus, 41 functions;
2. **PREP-002's own reconciliation of it** — `00D_PRIOR_RESEARCH_RECONCILIATION_MATRIX.md`.

The second is included because a reconciliation is a claim like any other, and because PREP-002's
reconciliation contains a **critical retraction** whose propagation had never been audited.

## 2. Standing position on the prior corpus — unchanged and restated

| Prior conclusion | Disposition | Basis |
|------------------|-------------|-------|
| Inventory emits facts; Accounting decides postings | **VALID** | corroborated: the 7 objects carrying financial fields carry values and account references, not posting decisions |
| A completed movement fact is immutable; corrections are new reversing facts | **VALID** | corroborated: the write-off and teardown documents are terminal by construction |
| The 19-menu accounting-dependency lock | **PARTIAL** | the dependency is real and unchanged; the object it reasoned about has been replaced |
| The valuation ledger is the per-movement valuation record | **SUPERSEDED** | 0 declarations in the target generation; the table does not exist on a real deployment of it |
| The valuation report menu | **OUTDATED** | no counterpart in the target generation |
| Conclusions derived from valuation-layer behaviour | **UNVERIFIED in the target generation** | true of the prior generation; no evidence establishes them for the current one |

**No prior conclusion is marked CONTRADICTED, and none is silently replaced.** Per PREP-002 §17, prior
conclusions are preserved as audit lineage; `BOSS-DEC-01` decides whether re-derivation is required
before they may support a SMEsPlus design.

**On process depth, the prior corpus is better than the delta programme assumed.** Measured: PROCESS
278 occurrences across 22 of 26 files, CONFIGURATION 363 across 24 — **both exceed OUTPUT (232)**. The
output-over-input asymmetry is real (3.1×) and larger than the commissioning premise stated, but *"prior
research is process-thin"* is **not supported**. A delta aimed at process internals would be aimed at
the dimension prior research covered best. Its genuine gap is **runtime reachability** — 21 weak hits,
zero positive control, because no runtime evidence base existed when it was written.

## 3. Defects found in PREP-002's own reconciliation

### `PW3-F-01` — the PREP-002 retraction was never propagated into its own matrix

This is a new defect, found in this session, in my own prior round's package.

`00D` `RC-F-01` retracted the optional-function zero and PREP-002's Layer-1 report drew the correct
consequence in words:

> *"the stated delta for the 29 `PARTIAL` menus is now **runtime reachability alone**, not
> 'optional-function + runtime'."*

**The matrix beneath it was never edited.** Enumerated from the frozen file:

| Check | Result |
|-------|-------:|
| Matrix rows with status `PARTIAL` | **32** |
| — of those, whose `Prior OPTIONAL` cell still reads **no** | **32 of 32** |
| — of those, whose `Required delta` still reads *"optional-function + runtime dimensions"* | **32 of 32** |

Every one of the 32 rows still asserts the retracted claim, in the same file whose §3 retracts it and
whose §4 states the opposite. **A reader who consults the matrix — the machine register, the artefact a
downstream team would actually parse — gets the withdrawn answer.**

`RC-F-03` in the same file compounds it, still reading *"the real gaps are optional function (zero) and
runtime reachability (zero)"* two sections after the optional-function zero was withdrawn.

> **Root cause, and it is a catalogued one:** a retraction was written into the narrative and into the
> roll-up, and never carried into the rows. **A revision log is not a correction.** The corrected text
> made the uncorrected table feel safe.

### `PW3-F-02` — the roll-up totals do not match the rows they summarise

`00D` §2 records a correction: *"Current nodes that map to a prior menu: **29** — corrected from 32;
three mapped nodes are grouping containers."* §4's roll-up carries the corrected figures.

**The matrix rows do not.** Enumerated:

| Status | §4 roll-up asserts | Matrix rows actually contain | Δ |
|--------|-------------------:|-----------------------------:|--:|
| `PARTIAL` | 29 | **32** | +3 |
| `MISSING` | 16 | 16 | 0 |
| `NOT APPLICABLE` | 17 | **14** | −3 |
| total | 62 | 62 | 0 |

The three rows that should have moved from `PARTIAL` to `NOT APPLICABLE` are identifiable, and I have
identified them by joining the matrix against `POPULATION_V3` on the container determination:

| Learning ID | What the node is | Population evidence |
|---|---|---|
| `LI-INV-MENU-0028` | the products grouping node under configuration | **CONTAINER — invokes nothing** |
| `LI-INV-MENU-0034` | the adjustments grouping node | **CONTAINER — invokes nothing** |
| `LI-INV-MENU-0042` | the transfers grouping node | **CONTAINER — invokes nothing** |

Exactly three, matching the stated correction exactly. The correction was **right**, and it was **never
applied to the population it described**.

> **The rule this re-proves:** corrections land on the row naming the identifier and nowhere else.
> Audit the text by identifier, never the disposition column — and enumerate register totals rather
> than asserting them.

### `PW3-F-03` — a third defect, found by an independent challenger

`00D` §2 records *"Current nodes with **no** prior coverage: **30**"*, then breaks that down as
*"grouping containers **17** — corrected from 14"* and *"action-bearing and never in prior scope: **16**"*.

**17 + 16 = 33, not 30.** The 14 → 17 correction was applied to the component and never carried into the
sub-total above it. Verified independently. It is the same defect as `PW3-F-02`, one line higher, and it
went unnoticed by me in the round that reported the other two — *"enumerate register totals rather than
asserting them"* applies to the sub-total I did not enumerate.

### Both accusations were verified by a third party — and so was the accusation turned around

An independent challenger re-counted `00D` and confirmed `PW3-F-01` (32 / 32 / 32) and `PW3-F-02`
(29/16/17 asserted against 32/16/14 enumerated) exactly, and independently reproduced the three-container
identification by the same join. **It then asked whether this package commits the defect it names, and
the answer was yes:** the three grouping containers were still carried at full applicability in this
package's own machine register, unchanged (`CH-15`). The prose accused; the rows did not follow. **They
are corrected in the R2 register**, where five dimensions on each of the three are now `NA` by the
container rule.

## 4. What is NOT done about it in this session — and why

**`00D` is not edited.** It sits in the frozen PREP-002 package, under `GOV-01` discipline: I committed
into a package while challengers were reading it once, and the rule I wrote that same hour forbids it.
The corrections above are published **forward**, in this package, carrying the identifiers
`PW3-F-01`, `PW3-F-02` and `PW3-F-03`, with the frozen artefact left intact as audit lineage.

The corrected statement of record, superseding the matrix cells:

> For the **29** menus in prior scope, the prior corpus covers **PROCESS, CONFIGURATION and OPTIONAL
> FUNCTION**. Its outstanding dimension is **RUNTIME REACHABILITY alone**. Three further nodes
> previously counted as covered are grouping containers with no function and are `NOT APPLICABLE`.

## 5. Recheck disposition

| Question | Answer |
|----------|--------|
| Is the prior workflow corpus complete against the derived population? | **No** — 16 action-bearing menus were never in its scope, **10 of them live on an observed deployment** |
| Is any prior conclusion contradicted by current evidence? | **No.** Superseded and unverified, yes; contradicted, no |
| Is PREP-002's reconciliation of it sound? | **No — two defects, both found here, both in the tables rather than the prose** |
| Does this change the disposition? | It does not rescue it. **HOLD stands** |
