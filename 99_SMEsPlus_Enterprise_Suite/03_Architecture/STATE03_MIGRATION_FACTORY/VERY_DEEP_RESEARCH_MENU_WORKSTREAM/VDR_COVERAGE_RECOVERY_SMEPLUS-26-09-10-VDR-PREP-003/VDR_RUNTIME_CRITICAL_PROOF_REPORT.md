# VDR_RUNTIME_CRITICAL_PROOF_REPORT.md
# Runtime proof — five deployment identities examined, three generations, no server started

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Commissioning instruction §9: establish a runtime proof strategy and apply it to the Critical Areas.

> ### R2 correction notice
>
> - **The heading of §2, *"Evidence base — declared, and the whole of it"*, is RETRACTED.** The path set
>   that located these five identities was never published, and an independent sweep of this host found
>   **at least twelve further database identities**, two of them full ERP databases carrying the tables
>   this report measures (`CH-13`, `LESA-F-02`).
> - **`R3-F-01` is corrected: 77 items, not 90; 49 menus, not 62** (`CH-06`).
> - **`R3-F-03`'s denominator is unreconciled** — see §4.
> - The four-grade model, the extraction method and the census itself survived challenge unaltered.

---

## 1. The four reachability grades

Runtime is not binary. This programme grades it, because collapsing the grades is what produced the
previous round's `0% UNMEASURED` and, before that, a false "not installed" on ten installed elements.

| Grade | Claim | Evidence |
|-------|-------|----------|
| **SOURCE PRESENT** | it is declared | a file in the declared path set |
| **RUNTIME REACHABLE** | the declaring module is installed | a row in the deployment's installed-module table |
| **RUNTIME OBSERVED** | the element itself exists in the deployment | a row in the deployment's own record of installed elements |
| **RUNTIME USED** | it carries data | rows in its own table |

**Only RUNTIME OBSERVED and above satisfy the RESEARCH-VERIFIED bar.** Module installation is
`DETERMINED`, and is reported as `DETERMINED`.

## 2. Evidence base — five identities examined; the path set that found them is NOT published

Five deployment identities were located and **all five examined**.

> **What this section is no longer allowed to claim.** R1 asserted that *"the path set was swept and the
> population ranked before selection."* **The sweep and the path set are published nowhere in this
> package** — the intention was stated; the command and its output were not. The denominator contract
> requires a path set to be declared **and executed**, with the output preserved. An independent sweep
> found at least twelve further database identities on this host, including two full ERP databases
> holding the movement, on-hand, installed-module and menu tables — and both holding the valuation table
> `CRITICAL-GAP-01` turns on; one is owned by a role named for this programme. **The five below are
> examined and real. They are not established as the whole population** (`CH-13`).

| Deployment | Generation | Modules | Menus present | Completed movements | Valuation rows |
|-----------|-----------|--------:|--------------:|--------------------:|---------------:|
| `iEVING` | 19 | 216 | 46 / 62 | 0 | 0 |
| `iTEST02` | 19 | 486 | 52 / 62 | 0 | 0 |
| **`BK12MAY26`** | **19 — transacted** | 251 | 46 / 62 | **14,441 movement rows — state basis undeclared, see `R3-F-03`** | 3,642 on-hand records |
| `idemo18_uat` | 18 | — | — | 51,081 | 47,801 |
| `iSMEs` | 16 | — | — | 103,949 | 74,982 |

**Method note.** Every figure was extracted **without starting a database server**, by restoring single
tables from the dumps directly to standard output and by parsing COPY blocks from plain dumps. The
client version matters: the current-generation dumps are unreadable by an older client, which fails on
the file header rather than on the data — a failure that is loud, and was treated as a blocker rather
than as an absence.

## 3. The runtime census — 4,984 applicable items

| Condition | n |
|-----------|--:|
| Declaring module installed on an observed deployment (**DETERMINED**) | 4,196 |
| Declaring module not installed on any observed deployment | 619 |
| Object-level reachability not observed | 96 |
| **RUNTIME REACHABLE**, element confirmed on both current-generation deployments | 46 |
| **RUNTIME REACHABLE — active and has executed** (scheduled jobs) | 11 |
| Optional-module dependent, not installed anywhere observed | 10 |
| Element confirmed on one of two | 6 |

Object-level detail, where tables were read directly: **49 objects are not persistent** (wizards and
abstractions — no rows *by construction*, a determination, not a gap); **19 are reachable but unused** —
the table exists and holds zero rows; **11 tables are absent** because the module is not installed on
the transacted deployment; the remainder are **RUNTIME OBSERVED with row counts**, from 1 row up to
**14,441**.

> **The never-transacted row is the informative one.** The 19 reachable-but-unused objects are the rows
> that validate the instrument: a census that returned only populated tables would be indistinguishable
> from one that silently dropped empty ones.

## 4. Findings

### `R3-F-01` — **corrected.** RUNTIME is 1.52% RESEARCH-VERIFIED: **77 of 5,071 — 49 menus, 17 objects, 11 scheduled jobs**

R1 published 90 of 4,984 (1.81%) and *"62 menus"*. Three corrections apply (`CH-06`, `CH-01`): **ten
menus were graded observed by a prefix match that swept in `OPTIONAL MODULE DEPENDENT`** — the same ten
this report's own census lists as *not installed anywhere observed*; **three were grouping containers**;
and the denominator returns to 5,071 because the 90 handoff runtime cells were never authorised to leave
it.

> **An open upgrade candidate, deliberately not applied:** the 19 objects whose table exists with zero
> rows are graded not-verified, although a present table arguably *is* the element existing in the
> deployment. Applying it would raise the number, and a number that rises must be moved by evidence a
> reader can identify — not by the author's judgement mid-correction. Carried to PMO as a question.
Everything else is known-installed, not known-present. The distinction is not pedantry: an
element can be in an installed module and still not exist in a given deployment.

### `R3-F-02` — 619 items (12.4%) belong to modules installed on no observed deployment.
They are
`SOURCE PRESENT` only. They are **not excluded** — under §8 an element is not dropped for being
inactive — but no runtime claim is made about them, in either direction.

### `R3-F-03` — the correction that inverted a headline — **and whose own denominator is unreconciled**
A previous round published *"series 19 is not
writing per-movement valuation."* **False.** The value **relocated onto the movement row**: 100% of
**3,680** completed movements on the transacted current-generation deployment carry one.

> **UNRESOLVED (`CH-17`).** §2's evidence table gives **14,441** for the same deployment under a column
> headed *Completed movements*; that figure is the movement-table row count. Either the heading
> mislabels its state basis, or this retraction's *"100%"* covers **25.5%** of the population. The dumps
> sit outside the frozen package and no query reachable from it settles which. **Recorded as unresolved
> rather than rounded to either side** — it sits underneath a retraction and a re-stated Critical Gap,
> the worst possible place for an unreconciled denominator.

The comparison had
**no state basis** (the deployment measured had zero completed movements) and **no configuration
control** (every located current-generation deployment runs periodic valuation, under which no movement
posts, in *any* generation). `RR-F-06` retracted; `CRITICAL-GAP-01` re-stated at material weight rather
than withdrawn.
> **Two rules follow, and both are now standing:** declare the state basis in the same line as the
> number; and before attributing a difference to a generation, control the configuration.

### `R3-F-04` — the "not installed" defect.
Ten items were reported as not installed on the basis of
domain-set membership, a predicate that was **never tested against the installed-module table**. All ten
are installed. The error contradicted another matrix inside the same package. `CORR-F-42`.
> **The rule:** a claim about a deployment must be answered by a query against that deployment.

### `R3-F-05` — the Critical Areas have almost no runtime proof — after correction, almost none at all
Across the fourteen populated Critical
Areas, `RUNTIME` research-verified counts remain, after correction: Financial Posting 1/16 · Inventory
Valuation 1/12 · Identity 1/61 · **every other area 0**. Those three single observations are now the
**only** research-verified cells anywhere in the fifteen Critical Areas. The Critical Areas are the part of this domain where runtime
evidence matters most, and they are where there is least of it. **This single dimension is, on its own,
sufficient to hold the certification.**

## 5. What would close it

Element-level observation for the Critical Area populations — **737 distinct items** (912 is the sum of
the per-area counts, not the union — `CH-08`) — read from the deployments' own element records rather
than inferred from module installation. The instrument for this exists and
has fired (it produced the 90). It was not run at Critical Area scale in this session. **Stated as
outstanding work, not as a limitation of the evidence base.**
