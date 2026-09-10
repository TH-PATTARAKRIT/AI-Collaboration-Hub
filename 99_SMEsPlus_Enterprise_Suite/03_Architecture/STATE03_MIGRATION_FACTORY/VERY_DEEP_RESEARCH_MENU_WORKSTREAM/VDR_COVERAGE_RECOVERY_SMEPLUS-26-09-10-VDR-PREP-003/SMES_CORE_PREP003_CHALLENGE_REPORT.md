# SMES_CORE_PREP003_CHALLENGE_REPORT.md
# Independent adversarial challenge — round R1, and its disposition

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. Round constitution

| | |
|---|---|
| Frozen baseline challenged | **`a146e004`** |
| Challengers | **three, independent, scoped so that no two share a failure mode**: **A** arithmetic and denominator integrity · **B** predicate and instrument validity · **C** population scope, evidence base and governance |
| Package state during the round | **untouched** |
| Round validity, verified after the round closed | `git log a146e004..HEAD -- <package>` → **0 commits**; working tree → **0 changes**; files modified after the freeze timestamp → **0**. **`GOV-01` did not recur** |
| Findings returned | **A** 19 · **B** 18 + 2 minor · **C** 19 |
| Corrections held by me during the round, outside the package path | 4 (`SC-01` … `SC-04`) |

**Every finding below was re-run by me before disposition.** Where my re-derivation differs from the
challenger's, both numbers are published and the difference in method is stated. A finding is not
adopted because it was reported.

## 2. The verdict in one line

> **The arithmetic is very nearly flawless — 396 of 417 published figures reproduce to the digit,
> including every cell of the Critical Area matrix and the two-grade table — and the sets those figures
> describe are wrong.**

Every material defect sits one rung above the arithmetic: a denominator that moved to absorb the cells
that were failing, a grade that is a class label wearing an evidence label, a union that was never
taken, exclusion reasons that are false against source, and predicates that cannot test the sentence
attached to them. **All of them survive a recount, because passing a recount is exactly what they do.**

## 3. Critical findings — all adopted

### `CH-01` — the denominator moved to absorb the cells that failed
*(A-01, A-02, B-01, B-02, C-01. Verified by re-running the package's own build logs.)*

```
pre-closure log       PROCESS 1564 applicable / 1030 determined = 65.86%
                      RUNTIME 5074 / 4984 = 98.23%
                      remaining NOT_VERIFIED: 400 BUTTON PROCESS · 96 OBJECT PROCESS
                                              90 HANDOFF RUNTIME · 38 MENUX PROCESS
button-resolution log button resolution: located 348, not located 52  → PROCESS 88.11%
post-closure log      PROCESS 1474 / 1474 = 100.00%   RUNTIME 4984 / 4984 = 100.00%
                      remaining NOT_VERIFIED: {}
```

**52 + 38 = 90 PROCESS cells and 90 HANDOFF RUNTIME cells — 180 — stopped being `NOT_VERIFIED` and
became `NA`, and both denominators fell by exactly that amount.** The published 30,741 is not what the
package's own §3 rule table produces; that table yields **30,921**.

Three rules were breached at once:
- §3 — *"`NA` is never assigned to an individual row."* It was, on 90 rows (52 of 431 buttons, 38 of 134 extension menus).
- §6 — an exclusion requires *Learning ID · reason · evidence · reviewer · status* in an exclusion register. **No exclusion register existed.**
- §8 — *"No percentage may rise because a predicate was relaxed."* It rose, from 65.86% / 98.23% to 100.00% / 100.00%.

B-01 states the consequence most sharply: **`NOT_DETERMINED` does not occur once in 30,741 cells.**
`DETERMINED` was not a test with two outcomes; it was a synonym for *applicable*. **I diagnosed
100%-everywhere as a drift signature in §4 of my own specification, then published a grade carrying that
exact signature and did not turn the diagnosis on it.**

### `CH-02` — 48 of the 52 button exclusion reasons are false against source
*(B-03. Verified against the reference tree.)*

The recorded reason on all 52 was *"the invoked method is not declared in the domain source — the
process belongs to another domain."*

- **41** have no method at all: the button carries no `name` attribute. Read at the cited pointer, they are framework discard controls — `<button string="Cancel" … special="cancel"/>` — **declared inside domain modules**.
- **7** name `cancel_button`, all declared in the domain's own wizard views with `special="cancel"`, which overrides the name. `def cancel_button` **does not exist anywhere in the reference tree** — it is a label, not a method.
- **4** survive as genuinely external.

The instrument read an XML `name=` attribute as a Python method name, failed to find a definition, and
attributed the process to another domain. **Seven of the misattributed elements are cancel controls —
the subject of the EDGE dimension — removed from measurement while the package publishes `EDGE 2/47` as
its most pointed result.**

### `CH-03` — 98.7% of RESEARCH-VERIFIED was class membership, not measurement
*(A-05, B-05, B-06, B-07. Re-derived; my split differs from A's and both are published.)*

| | mine | A's |
|---|---:|---:|
| verified cells that are all-or-nothing within their class | **9,424** | 9,362 |
| verified cells carrying an item-level decision | **61** | 123 |

Only **7 of ~90 class/dimension pairs vary within class at all**. For `SOURCE`, `DATA_MODEL`,
`CROSS_MODULE` and `SECURITY` the grade never varies — so for those four the two grades the
specification says *"must never be merged"* were merged into the same class table that already decides
applicability.

- `SOURCE` was an **unconditional literal** — `v='VERIFIED'` with no condition, unable to return anything else — and it supplied **5,074 of the 9,485 verified cells (53.5%)**. Meanwhile 186 of its "reproducible pointers" resolve to no file and 2,159 carry no line.
- `SECURITY` is **inverted**: the 270 graded verified are the security objects themselves, and their `SECURITY_CONDITION` field is **empty on all 270**; the 3,788 items that actually carry the enumeration §7 demands are graded not-verified. The Security Critical Area's population *is* the set defining its own verified cells — the 60.1% is self-referential.

### `CH-04` — the single 100% Critical Area is an artefact of `CH-01`
*(A-04, B-04, C-02, and my own `SC-02`.)* All four Area-15 items are handoff elements; restore the
`RUNTIME` cell the rule table marks applicable and each acquires a failing cell — their own reachability
field reads `UNMEASURED`. **Area 15 falls to 8/12 = 66.7%; Critical Areas at 100% falls to 0 of 15;
Overall Verified Coverage falls to 0.00%.**

### `CH-05` — a published zero is falsified inside the declared path set
*(B-13. Verified independently; my count differs slightly from B's and both are published.)*

`VENDOR / EDITION-RESTRICTED = 0` was published as a determined absence. It is wrong, and the classifier
that produced it **had no branch capable of emitting the class** — the strings `VENDOR`, `EDITION`,
`RESTRICTED`, `DEPRECATED` occur zero times in the register. There was no instrument, so there was no
census.

```
domain modules resolvable in the reference root : 126
licence distribution : {'OEEL-1': 70, 'LGPL-3': 55, 'OPL-1': 1}
edition-restricted   : 71 modules   (B reports 70, counting OEEL-1 only)
population items declared inside one : 1,411   (27.8%)   (B reports 1,375)
```

**More than a quarter of the population sits in edition-restricted modules, inside the very tree the
zero was declared against.** This is `CORR-F-37`'s shape once more: a control that could not fire.

## 4. Material findings — all adopted

| ID | Finding | Source | Verification |
|----|---------|--------|--------------|
| `CH-06` | **10 of the 90 runtime-verified items are recorded as installed on no deployment.** The predicate prefix-matched `OPTIONAL MODULE DEPENDENT` into the observed set. By the report's own grade table: **52 menus, not 62**; **80, not 90**. Symmetrically, 19 objects whose table exists with 0 rows are graded not-verified, though a present table *is* the element existing | A-06, B-08 | **exact** |
| `CH-07` | **`DATA_MUTATION: YES` fires on the guard that prevents the mutation.** The pattern alternative `_unlink_\w+` matches the method's own name; the segment includes the `def` line. **15 deletion guards counted as data mutations** (B found 14). Consequently the report's *"second shape … Agreement: exact"* is falsified — an AST pass over call nodes cannot agree exactly, because call nodes carry no `_unlink_*` identifier. **Exact agreement was achievable only by reusing the same accessor** | B-09 | **confirmed, 15** |
| `CH-08` | **`912` is the sum, not the union.** Distinct items = **737**; 175 memberships are second or later mappings. Found independently by A, C **and** by me before the round opened | A-03, C-05, `SC-04` | **exact** |
| `CH-09` | **`FUNCTION_COMPLETE` = YES on all 5,074 rows** of the machine register while the matrix publishes 0 for fourteen areas; `VERIFIED_DIMS` sums to 30,741 against a true 9,485. Legacy columns from the pre-two-grade build. **This is the defect `PW3-F-01` indicts, committed inside the package that names it** | A-09, C-06 | **confirmed** |
| `CH-10` | **Two predicates do not test their own sentence.** `CROSS_MODULE_CALL` matches *any* ORM model access including same-domain, so `P3-F-04`'s *"call into another domain"* is not established. `ERROR` is a bare substring `'raise'`, firing on comments and identifiers. The declared positive control injected a cross-domain call — which fires identically on an in-domain call, so it could not fail the way the predicate fails | A-13 | **accepted** |
| `CH-11` | **`EDGE = 2` is a hardcoded two-identity list**, not a measurement, and both rows carry an empty evidence field. Meanwhile 583 EDGE cells are `DETERMINED` on the string *"NO REVERSE/CANCEL ROLE DETECTED"* — the vocabulary of a failed search promoted to a determination, against the programme's own standing rule that no-evidence-found is not function-does-not-exist | B-15 | **confirmed** |
| `CH-12` | **"All twenty facets established" for the 17 process-verified items is unsupported.** None carries a facet record; 10 sit at the register's lowest status; the grading predicate keys on a status held by 63 rows, not 17. The report declares nine of the twenty not covered at all, so the claim contradicts its own §2. A third definition (11 facets) lives in the extraction script | A-12 | **confirmed** |
| `CH-13` | **The evidence base is not "the whole of it."** The path set was never published. At least 12 further database identities exist on this host, two of them full ERP databases carrying the tables this package measures — one owned by role `smeplus` — and a controlled-install lab whose evidence directory is named for the exact configuration `CRITICAL-GAP-01` needs. C declares its own sweep a floor, not a census | C-07 | **accepted** |
| `CH-14` | **`BOSS-DEC-10` is omitted from the carry-forward register.** The 5,074-item denominator rests on the stop-at-one-hop rule, which the programme classifies as a **provisional research control** subject to an open Boss decision. The register that exists so no reader has to guess what is inherited dropped the most consequential open decision in the lineage | C-08 | **confirmed in the PREP-001 decision register** |
| `CH-15` | **The three container menus are still fully applicable in my own register.** I accused the predecessor of not landing a correction in its rows, then did not land mine | C-09, `SC-01` | **confirmed** |
| `CH-16` | **The pre-commit identifier sweep is blind to every identifier this package owns.** The shipped script's pattern contains none of the five owned families, so its clean result was computed over **zero** of them. I ran a repaired sweep and **shipped the unrepaired one** | B-14 | **confirmed: 0 occurrences of the owned families in the shipped script** |
| `CH-17` | **A denominator under a retraction is unreconciled.** *"100% of 3,680 completed movements"* sits beside the same package's table reading **14,441** under the heading *"Completed movements"* — the movement-table row count. Either the heading mislabels its state basis, or the retraction's 100% covers 25.5% of the population. The dumps are outside the frozen package, so no query I can run from it reaches the authority | A-14, B-16 | **confirmed unreconciled** |
| `CH-18` | **The code that assigns every published grade is not in the package.** the dimension-build script emits 39 columns; the register carries 69. **No shipped script writes `DET_*` or `RV_*`.** The package is not reproducible at the level of the grades this review was commissioned to test | A-10, B-17 | **confirmed** |
| `CH-19` | **`33 distinct optional modules` and `twelve capability switches`.** 33 counts distinct activation *strings*; 8 are not modules and 101 elements have no module route. Atomic modules = **25**. Switches: 16 values, 15 group routes, 14 atomic — **12 reproduces under no reading** | A-08 | **confirmed** |
| `CH-20` | **The TRIGGER marginal omits 82 of 962.** onchange + constrains = **94**, published as 13. The row sums to 880 under a heading declaring n = 962. The other ten marginals reproduce exactly | A-07 | **confirmed** |
| `CH-21` | **`P3-F-01` publishes the platform base rate as a domain finding.** A control over 120 random modules gives 97.2% unhandled platform-wide against the published 98.9%; and the population instrument selects *away* from exception handlers by 3.6× relative to unselected functions in the same files — **the selection criterion partly produces the finding** | B-11 | **accepted** |
| `CH-22` | **`EXCEPTION: HANDLED` fires on the English word in a docstring** (1 of 4 positives — a 25% false-positive rate on the positive class), and **`PRECONDITION: guard-if at entry`** counts any guard anywhere in the body: 45 of 102 are not at entry, one 17 lines into a 60-line body. An AST test for a true entry guard yields 47, not 102 | B-10, B-12 | **accepted** |

## 5. Minor, adopted

`CH-23` the 512-table attributes the 52 removed buttons' reason to the 31 retained ones — disjoint sets.
`CH-24` *"Fourteen [areas] are below 100%"* — thirteen are; area 6 is not computable, which is not below
100%. `CH-25` the configuration 100% coverage assertion counts 26 automation rows whose recorded
condition is a runtime activation statement. `CH-26` *"both current-generation deployments"* while three
exist. `CH-27` the canonical rule's *"minimum set"* modality is not carried into *"required 15 of 15"*.
`CH-28` `CRITICAL-GAP-04`'s *"a design prohibition to adopt"* reads imperatively before deferring —
rephrased to a recommendation. `CH-29` the declared path set (*"1,624 source files of 149 modules"*) is
a scanned-file count; the 122 resolvable modules hold 1,903 Python files. `CH-30` the extraction script
declares 7 not-covered facets, the report 9; 11 + 7 = 18 ≠ 20. `CH-31` `633` and `709` gated elements in
the same file. `CH-32` the shipped sweep writes a flat manifest and is not the code that produced the
shipped manifest.

## 6. Not adopted — carried forward instead

A-17 found a **third** defect in the frozen PREP-002 package: `00D` §2 states *"30 nodes with no prior
coverage"* while its own components are 17 + 16 = 33; the 14→17 correction was not carried into the 30.
**Verified and correct — and it is a defect in a frozen predecessor, not in this package.** It joins
`PW3-F-01` and `PW3-F-02` as a forward correction. The frozen artefact is not edited.

## 7. Confirmations — recorded so their silence is not read as absence of testing

| Control | Result |
|---------|--------|
| Freeze, by two independent units (git history, filesystem mtime) | **honoured; `GOV-01` did not recur** |
| Manifest — all 23 hashes recomputed, not sampled | **23 of 23, 0 mismatches** |
| Fifteen Critical Areas against the frozen canonical rule | **verbatim, name-for-name and in order; nothing invented** |
| LAYER 1 clean-room, 24 vendor tokens across all root documents | **no leak** (the only hits were the challenger's own pattern inside "Stock Quantity") |
| Approval / certification / self-certification / Boss foreclosure | **none issued** |
| Published arithmetic | **396 of 417 figures exact**, including all 15 matrix rows, all 46 blocking ratios, all four censuses |
| AST node resolution in the facet extractor | **614 of 614 exact; 0 fallbacks, 0 ambiguous, 0 name mismatches** |
| Parse-loop coverage | **0 read failures, 0 parse failures across 169 files** |
| Clean-room token check, tested by injection | **fires correctly; the word-boundary guard behaves as documented** |
| Generation basis | **content-based, not a path name or a manifest version string** |

## 8. Disposition of the round

**Round R1 is INVALIDATED as a review baseline** — not because the freeze was broken, but because the
corrections it forced are material enough that reviewers would be reading a superseded package. Per §15
a new clean baseline is created rather than the frozen one edited.

**Corrections applied: 32 findings + 4 self-found = 36.** The resulting figures are in
`VDR_PREP003_FINAL_READINESS_REPORT.md`. They are worse in every direction, which is the point.

**No challenger approved anything, and none was asked to.**
