**LAYER 2 — AUDIT QUARANTINE.**

# Producer self-corrections found DURING the R3 freeze window — held, not applied

Frozen SHA `1d6238a5574ae8a07e1c7679be024cdeacc84940`. These were found while reviewers were reading
the package. **Under the §3 freeze rule they must NOT be applied until the round closes.** They are
recorded here, outside the package path, and applied afterwards.

## SC-01 — `GAP-INV-09B` is FALSE as published (CRITICAL, producer-found)

Published: *"no deployment in the target generation carries stock"* and *"transactional reachability
for the target generation remains unmeasurable"*.

**Wrong.** A fourth deployment — listed in the package's own artefact census and **not examined** —
is series **19.0.1.3** and is transacted:

| | value |
|---|---|
| generation | **19.0.1.3 — the target generation** |
| modules installed | 251 · domain 34 of 149 |
| **stock movements** | **14,441** |
| **on-hand quantity rows** | **3,642** |

This is the exact defect `GAP-INV-17` names — the census was run after the choice — and the
producer published a negative about the evidence base **while the artefact that falsifies it was
listed in the package's own census file.**

## SC-02 — the valuation finding `RR-F-06` is CONFIRMED and materially strengthened

Tested on the transacted series-19 deployment:

| generation | deployment | stock movements | valuation-ledger rows | movement-linked |
|---|---|---:|---:|---:|
| 16 | transacted | 103,949 | **74,982** | **98.0%** |
| 18 | transacted (a **fifth** deployment, also unexamined) | 51,081 | **47,801** | not measured |
| **19** | **transacted** | **14,441** | **table absent** | — |
| 19 | transacted — replacement object | — | 9,070 rows | **0.0%** |

**Even with 14,441 real movements, a series-19 deployment holds zero movement-linked valuation
records.** The replacement object holds 9,070 rows and every one is a product price update.

The published claim rested on a **non-transacted** series-19 deployment, where the absence could have
been explained by there being nothing to value. **That objection is now closed.**

## SC-03 — reachability evidence extends to a third and fourth series-19 deployment

| Deployment | series | menus present | anomalies | suppression parameter | scheduler | valuation job |
|---|---|---|---|---|---|---|
| `iEVING` | 19 | 46 / 62 | 0 | **not set** | active, ran | active, ran |
| `iTEST02` | 19 | 52 / 62 | 0 | **not set** | active, ran | active, ran |
| **`BK12MAY26`** | **19, transacted** | **46 / 62** | **0** | **not set** | **active, ran 2026-08-03** | **active, ran 2026-08-03** |

**186 menu observations across three deployments, 0 anomalies.** The module-installation inference is
now supported by a third independent replication.

`RR-F-01` (write-by-read not suppressed) now holds on a deployment **with real stock**.

## SC-04 — two further database identities examined; the census figure of 3-of-6 is superseded

`idemo18_uat` — series **18.0.1.3**, 361 modules, 2,462 on-hand rows, 51,081 movements,
**47,801 valuation-ledger rows**. A transacted series-18 deployment.

**5 of 6 identities are now examined.** `GAP-INV-17` narrows but does not close: one identity and all
cloud storage remain unswept, and the ordering defect (census after choice) is historical fact.

## Application plan once the round closes
1. Correct `GAP-INV-09B` in `00A` and `00C`; it becomes **partly closed**, not open.
2. Strengthen `RR-F-06` in `00C` with the three-generation transacted table.
3. Extend `00C` §3 and §5 with the third and fourth deployments; update the reachability figures.
4. Narrow `GAP-INV-17` from 3-of-6 to 5-of-6 examined; keep the ordering defect recorded.
5. Recompute any coverage figure that moves.
6. Record all four as producer self-corrections in the re-challenge report, **found during the freeze
   window and held**, with the freeze-compliance evidence.

## SC-05 — the census identity count is wrong: 5 identities, not 6 — and ALL FIVE are now examined

Re-derived from the package's own census file. The 15 artefact rows resolve to **8** name groups, of
which **2 are this session's own extraction output** and one (`dump`) is a filename artefact of the
plain-SQL copy of an already-counted identity.

**Distinct deployment identities: 5.**

| Identity | Generation | Modules | On-hand rows | Movements | Valuation ledger | Examined |
|---|---|---:|---:|---:|---|---|
| `iSMEs` | **16.0.1.3** | 190 | 27,196 | 103,949 | **74,982 rows** | yes |
| `idemo18_uat` | **18.0.1.3** | 361 | 2,462 | 51,081 | **47,801 rows** | yes |
| `iTEST02` | 19.0.1.3 | 486 | 0 | 48 | **table absent** | yes |
| `iEVING` | 19.0.1.3 | 216 | 0 | 0 | not extracted | yes |
| `BK12MAY26` | **19.0.1.3** | 251 | **3,642** | **14,441** | **table absent** | yes |

**`GAP-INV-17` substantially closes.** What remains is the ordering defect — the census was run after
the deployments were chosen — which is historical fact and stays recorded, plus the unswept
cloud-storage exclusion, plus the fact that for two identities a **newer copy exists that was not
used**.

## SC-06 — the generation coverage of the runtime evidence base is three generations, not one

Published: *"reachability is not measured for any other generation"* and *"the only transacted
deployment is series 16"*. Both are now false.

**Three generations are represented — 16, 18 and 19 — and three of the five deployments are
transacted, including one in the target generation.** This is the single largest improvement to the
evidence base in this session and it was found **after** the package was frozen.

## SC-07 — the three-generation valuation table, completed and with its one unexplained column flagged

Measured on the three **transacted** deployments:

| Generation | Stock movements | Valuation-ledger rows | Rows carrying a **movement** link | Rows carrying an **accounting** link |
|---|---:|---:|---:|---:|
| **16** | 103,949 | **74,982** | **98.0%** | 77.2% |
| **18** | 51,081 | **47,801** | **94.0%** | **0.0%** |
| **19** | 14,441 | **table does not exist** | — | — |
| 19 — replacement object | — | 9,070 | **0.0%** | n/a |

**The load-bearing measure is the movement link.** It is near-universal in series 16 (98.0%) and
series 18 (94.0%) and **does not exist in series 19** — the table is gone and its replacement carries
none.

**One column is NOT a trend and must not be read as one.** The accounting link is 77.2% in series 16
and **0.0%** in series 18. That difference is between two earlier generations, is unexplained by this
session, and may be a schema relocation rather than a loss of linkage. **It is reported as measured
and explicitly not interpreted.** Recorded as `GAP-INV-20`.

Stating this separately matters: three columns of that table support one conclusion and the fourth
does not, and merging them would manufacture a trend the evidence does not carry.

## SC-08 — the ten "live" delta menus split into USED and UNUSED, and the split changes their priority

`RUNTIME REACHABLE` was measured as *the menu exists on a deployment*. On the transacted
series-19 deployment the underlying objects can now be counted, and reachable is not the same as used.

| Delta object | series-19 transacted | series-19 (T) | Verdict |
|---|---:|---:|---|
| **reference object** (`DR-F-04`, `GAP-INV-18`) | **11,852 rows** | **21,703 rows** | **REACHABLE AND HEAVILY USED** |
| package object (`DR-F-05`) | 0 | 0 | reachable, **never used** |
| batch / wave object (`DR-F-01`) | table absent | 0 | **not installed / never used** |

**`GAP-INV-18` is materially more serious than published.** The reference object holds **11,852 rows
against 14,441 stock movements — roughly 0.82 rows per movement.** It is on the transaction path,
it binds Inventory documents to point-of-sale, purchase and sales documents, it has **no controls, no
validations and no behaviours**, it is **hidden behind a technical-only group**, and **no prior
research covered it**. Identity is a Critical Area.

**And the two functions the commissioning prompt named explicitly — batch and wave transfers — are
installed nowhere or used nowhere on the deployments observed.** They remain in the population as
source-present and optional-module dependent; they are **not** where the operational risk is.

**Method point: `RUNTIME REACHABLE` and `RUNTIME USED` are different classes and the matrix conflated
them.** A fourth reachability class — `REACHABLE BUT UNUSED` — is required. Recorded as `CORR-F-35`.
Delta-research priority should follow **use**, not reachability, and this session's priority ordering
was set before the distinction existed.

## SC-09 — only 36% of the domain's persistent objects are used on a real deployment

Row counts taken for all **47 persistent owned objects** against the transacted series-19 deployment:

| Class | Objects | Share |
|---|---:|---:|
| **USED — carries rows** | **17** | **36.2%** |
| present, **0 rows** — reachable, never used | 19 | 40.4% |
| table absent — module not installed | 11 | 23.4% |

**The single most useful reachability number in the package**, and it did not exist before this
measurement: **the domain's object surface is 36% used, 40% dormant and 23% not deployed** on a real
transacted installation.

### The object ranking, and what it does to `GAP-INV-18`

| Rank | Object | Rows |
|---:|---|---:|
| 1 | stock movement | 14,441 |
| **2** | **the reference object** | **11,852** |
| 3 | movement line | 10,017 |
| 4 | the series-19 valuation replacement | 9,070 |
| 5 | movement document | 6,688 |
| 6 | on-hand quantity | 3,642 |

**The reference object is the second most populated object in the entire Inventory domain** — more
populated than the movement document and than on-hand quantity — and it is:

- covered by **no** prior research,
- hidden behind a **technical-only** group so no ordinary user or menu-driven study sees it,
- carrying **no controls, no validations, no behaviours**,
- binding Inventory documents to **point-of-sale, purchase and sales** documents.

`GAP-INV-18` should be **re-graded to CRITICAL** and is a candidate for its own `CRITICAL-GAP`.
Identity is a Critical Area and this is the largest unresearched identity surface in the domain.

**Method point.** Reachability was measured as *can it be reached*. Use is *is it reached*. The two
differ on **40% of the object surface**, and the difference is only visible with a transacted
deployment — which this session did not have when it wrote the reachability matrix.

## SC-10 — the identity object is the order-to-cash traceability spine, and `DR-F-04` under-describes it (**CRITICAL**)

`DR-F-04` said the reference object "carries references to point-of-sale orders, purchase orders and
sales orders". That was read from **source declarations**. Measured in **data** on the transacted
series-19 deployment it is both **narrower and far more important**:

| Link | Rows | Against | Density |
|---|---:|---:|---|
| **reference ↔ stock movement** | **13,163** | 14,441 movements | **91.1%** |
| **reference ↔ sales order** | **6,661** | 6,665 sales orders | **99.94%** |
| reference ↔ purchase order | 11 | 31 purchase orders | 35.5% |
| reference ↔ point-of-sale order | **0** | 18 | declared, unused |
| reference ↔ production order | **0** | — | declared, unused |
| the object itself | **11,852 rows** | — | 2nd most populated object in the domain |

**Seven modules declare a relation to it** — inventory movement, inventory document, sales,
purchase, point-of-sale, manufacturing and repair — so the source surface is wider than `DR-F-04`
stated (it omitted manufacturing, repair and the two Inventory objects themselves).

> **In data this object is the join between stock movements and sales orders: essentially every sales
> order and nine in ten stock movements carry one.** It is the order-to-cash traceability spine of
> this deployment.

And it has **no controls, no validations, no behaviours, no record rule** and is reachable only
through a menu gated to a **technical-only** group. **No prior research covered it, and no register in
either package describes it as a traceability mechanism.**

**`GAP-INV-18` should be promoted to a `CRITICAL-GAP`.** Identity and Audit Trail are both Critical
Areas and this is the largest unresearched identity surface measured anywhere in the programme.

### Method point — the first instrument was wrong and nearly produced a false negative
The links are many-to-many and live in **join tables**, not in columns on the parent documents. A
first check looked for a reference column on the parent tables, found none populated, and would have
recorded **"0% populated"**. **The relation type determines where the evidence lives**, and a column
check cannot see a many-to-many. Recorded as `CORR-F-36`.

---

# R3-B CHALLENGE FINDINGS — producer verification before adoption

## R3B-01 — CONFIRMED IN FULL. `RC-F-01` IS FALSE AND IS WITHDRAWN. (CRITICAL)

Published: *"Zero occurrences, across 5,193 lines, of feature toggle, optional module, optional
function, conditional field, conditional menu or opt-in — and the word toggle itself appears zero
times… None of that surface exists in the prior research at all."*

**Verified against the prior corpus myself. The claim is false.**

| Term | Occurrences | Files |
|---|---:|---:|
| *capability* | **56** | 17 of 26 |
| *optional* | 48 | 11 |
| *conditional* | 25 | 12 |
| *capability switch* | 6 | 3 |
| *visible only* | 8 | 1 |
| *Hidden unless* | 5 | 1 |

The prior corpus contains a **dedicated function** — `INV-F-26 "Change a capability switch"` — with all
eight process dimensions filled, including *"State transition: capability on ↔ off"*, *"Quantity
impact: enabling traceability where untracked stock already exists leaves balances with no batch
identity"*, and *"Cost impact: enabling or disabling valuation changes whether value events are
produced at all"*. It contains a **dedicated menu study** of the switch panel — *"Required fields:
none; it is a switch panel"*, *"Optional fields: every capability switch"*, *"Visibility rules:
switches reveal dependent switches; some cannot be turned off once data exists"* — rated
**configuration risk HIGH**, with a named open gap `GAP-MD-14` (switch-off guards, versioning).

> **The prior corpus's optional-function coverage is better than this session's own delta produced.**

**Cause — and it is this framework's own catalogued defect, committed by its author.** The measurement
searched for *my* vocabulary. The corpus uses *"capability switch"*. **The positive control was the
word `toggle` — drawn from the same wrong vocabulary — so it could not fire, and its failure to fire
was read as confirmation instead of as the warning it was.**

**A positive control drawn from the same vocabulary as the search term tests nothing.** Recorded as
`CORR-F-37`.

### What falls with it
- `RC-F-01` — **WITHDRAWN**.
- `GAP-INV-19` — **WITHDRAWN**.
- `COMPLETE = 0` — premise gone; must be re-derived.
- The 32 `PARTIAL` rows — their stated delta *"optional-function + runtime"* is wrong on the optional half.
- The §4 framing in the coverage recalculation.
- **The decision not to re-research the 32 becomes better justified, not worse**: prior coverage is stronger than published.

## R3B-11 — CONFIRMED. `RESEARCH-COMPLETE = 0` was unfalsifiable by construction.
The register carries **one ordinal `research_status` per row**, so no row can hold three dimensions.
"No item has all three" is true of every possible content of the file. `CORR-F-38`: the schema needs
**three independent dimension columns**, not one ordinal.

## R3B-02 — CONFIRMED. Three mapped nodes are containers.
Verified in source: all three carry no action. **Mapped action-bearing 29 (not 32); containers 17
(not 14).** The coverage report's 17 and the matrix's 14 never reconciled.

## R3B-04 — CONFIRMED EXACTLY. Numerator/denominator mismatch.
S4 63 → **59** applicable; S3 755 → **677** applicable. Corrected: PROCESS **1.33%**,
CONFIGURATION **15.30%**.

## R3B-10 — CONFIRMED. Non-applicable decomposition.
containers 17, unreachable 635, **overlap 4**, union **648**. Total right, decomposition wrong by 4.

## R3B-05 — CONFIRMED AND UNDERSTATED.
`delivery.carrier` has **264 fields across 24 modules** on my own recount (R3-B said 228).
`delta_evidence.txt` reported **0 fields, 0 required, 0 controls, 0 behaviours** because the extractor
scoped fields to the *menu's* module. **`DR-F-08` was published on an object measured at zero on every
dimension, with 46 edges beside it, and no control flagged the contradiction.** `CORR-F-39`.

## R3B-03, R3B-07, R3B-09, R3B-13, R3B-14, R3B-15, R3B-17, R3B-18, R3B-19 — ACCEPTED
All are specific, evidenced and correct in kind. Notably: two further prior menus study objects that
no longer exist (`OUTDATED` = 3, not 1); the 85,832-row evidence is **not inside the frozen package**;
`stock.reference` also links **manufacturing orders**, omitted from `DR-F-04`; a generation label
contradiction (series 16 written as series 18); the dimension instrument is unpublished; four
identifier families uncited in the carry-forward register; and negated groups double-counted.

## R3-B's additional observation — ACCEPTED AND MATERIAL
An optional device-integration module **clears the group restriction on the Inventory Configuration
menu on install**, and it is installed on one observed deployment. This is the same class as the
prior package's `MM-F-08` and it lands in the SaaS/Security critical area.
