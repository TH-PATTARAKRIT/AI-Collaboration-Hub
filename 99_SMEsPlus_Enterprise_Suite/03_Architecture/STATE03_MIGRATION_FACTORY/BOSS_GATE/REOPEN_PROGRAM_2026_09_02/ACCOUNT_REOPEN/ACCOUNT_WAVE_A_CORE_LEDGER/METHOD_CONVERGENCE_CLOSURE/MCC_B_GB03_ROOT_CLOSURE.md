# MCC_B — `GB-03` ROOT CLOSURE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Parent commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc` · Depth `VERY DEEP / L99999.99999`

> **Recommendation only. Boss is the sole Final Approver.**
> Layer 2 `file:line` citations are held in `LAYER2_MCC_EVIDENCE/MCC_E00`. This file carries the
> reasoning and the disposition; it names mechanisms, not vendor identifiers, wherever it can.

---

## 1. What `GB-03` claims, and the four states it has occupied

`GB-03` — *"Inconsistent company scoping over one rate table."*

| # | State | Round | What established it |
|---|---|---|---|
| 1 | **RAISED** | `CORR1` | Rate resolution differs between paths |
| 2 | **CLOSED WITH EVIDENCE — 4 rules** | `GAPCLOSE` | Four scoping rules enumerated reactively; `FX-08` declared a `VERIFIED DEFECT` |
| 3 | **RE-CHARACTERISED — 6 rules, "complete"** | `MC` author pass | Two further rules found; population declared closed |
| 4 | **RE-OPENED — ≥9 rules, not bounded** | `MC` fresh review | The "complete" claim was bounded by a matching pattern, not by the source; two of its rules withdrawn as characterised |

**The pattern across four rounds is one pattern.** Every time the rule count was declared final, the
next look raised it. No round ever declared the *search pattern* by which it was counting. That —
not the rate table — is what `GB-03` is really about, and it is why this round closes it by
enumerating the **surface** rather than by counting rules again.

---

## 2. Which control was expected, and where it should exist

| Expectation | Layer it would live in |
|---|---|
| One company-scoping rule applied identically by every reader and writer of a measurement | model / ORM |
| A constraint refusing a rate row whose company cannot resolve it | model constraint |
| A record rule limiting who sees whose rates | access / security |
| A uniqueness rule making "the rate for currency C on date D in company X" single-valued | database |
| Identical NULL semantics in every resolver | model + SQL |

---

## 3. Search universe — declared as a PATTERN, not only as a path

This is the correction `ER-CORE` prescribes, and this round applies it to itself.

### 3.1 Pattern

> Every file under the reference source root whose text matches
> `res\.currency\.rate` **or** `res_currency_rate` **or** `model_res_currency_rate`,
> in extensions `.py` `.xml` `.csv`,
> **excluding** `/tests/`, `test_*`, `/i18n/`, and `*__dup_*` duplicate module copies.

### 3.2 Path set — and its first correction

| Path set | Directories | Declared by |
|---|---|---|
| `addons/` | **791** | every prior round (as "797", corrected to 791 by `MCX-04`) |
| `addons_archive/` | **961**, of which **450** are `*__dup_*` duplicates | **NO ROUND, INCLUDING THIS ONE'S FIRST PASS** |
| framework core (`models.py`, `fields.py`, `modules/`) | — | `MC` round (`SRC-E`) |

> ### `MCC-B-01` — the source root contains a SECOND module tree that no round has ever searched.
>
> **`VERIFIED FACT`.** Alongside the 791-directory primary addon tree, the same deployment root holds
> an archive tree of **961 module directories**. Every whole-tree negative claim in the programme's
> history — including the four claims that reached class `A — VERIFIED ABSENCE` — declared its scope
> as the primary tree and **excluded the archive tree without saying so.**
>
> **This round's own first-pass enumeration of the rate-table surface made the identical error**, and
> it is recorded here against this round, not against its predecessors. The first pass returned 14
> files. Extending the path set returned **20**. The pattern was right; the path set was wrong.
> `ER-CORE` says *declare the pattern, not only the path*. The complete form of the rule, learned
> here, is **declare the pattern AND prove the path set** — and the proof of a path set is an
> enumeration of the source root, not a habit.

### 3.3 Pattern-completeness check — executed, and it passes

A pattern is not complete because it is declared. Two known false-negative modes were tested:

| Mode | Test | Result |
|---|---|---|
| Access via the currency's one-to-many rather than the model name | search the whole path set for the rate collection accessor outside the returned file set | **10 hits, all on unrelated models** (payroll insurance rate lines, fleet expense rates). **No rate-table site missed.** |
| The table named in a non-scanned extension | search `.sql`, `.yml`, `.yaml`, `.js` for the table name | **0 hits** |
| Records reached by external id rather than model name | search for the shipped rate-row external-id prefix | **0 hits** |

Two **false positives** were also produced by this round's first, looser pattern (which additionally
matched the rate-collection token): two unrelated models in payroll and expense-disallowance. They
are recorded because a pattern's false-positive rate is part of its declaration.

---

## 4. Exact evidence — the bounded surface

> ## The rate-table surface is **20 files**. This is the first bounded enumeration of it in the programme.

| Layer | Files | Role |
|---|---|---|
| Framework model + views + security | 5 | model definition, the resolvers, the record rule, the access rows, the form view |
| Framework shipped data | 1 | demo rate rows |
| Accounting addon | 3 | the reporting currency-table builders, the invoice report dependency map, the access row that widens write rights |
| Accounting reports addon | 1 | unrealised-FX revaluation |
| Live-rate feed addon | 1 | the external rate writer and its scheduled actor |
| Spreadsheet addon | 2 | a client-callable conversion endpoint |
| Subscription reporting addon | 1 | an independent raw-SQL rate resolution |
| Archive tree — localisation | 6 | one model extension, two demo data sets, and their manifests |

**Denominator: 20 files. Evidence read: 20 of 20. Gap: 0.**

---

## 5. The company-scoping rule set — bounded, and the count is not the finding

Over that 20-file surface, the distinct company-scoping expressions applied to the one rate table
number **fourteen**. The count matters far less than its shape, so the shape is given first.

| Behaviour over NULL-company rows | Rules | Layer |
|---|---|---|
| **INCLUDE** them | 6 | record rule · posting-time resolver (×2, main + fallback) · one framework sibling helper · one raw-SQL consolidation helper · one reporting addon's raw SQL |
| **EXCLUDE** them | 6 | four reporting currency-table builders (raw SQL) · one framework sibling helper · the fiscal-year-bounds probe's practical effect |
| **Not applicable** (write-side) | 2 | the model default · the write constraint |

> ### `MCC-B-02` — the defect is not the number of rules. It is that half of them include the shared row and half exclude it, and no layer declares which is correct.
>
> **`VERIFIED FACT`.** Six rules admit a company-less rate row and six refuse it. Two of the
> disagreeing pairs are **sibling methods in a single file**, and one disagreeing pair is
> **posting-time versus report-time over the same posted amount.**
>
> The financial consequence of that last pair is stated in `MCC_G` as its own balanced-but-wrong
> class: **an amount can be posted using a rate that the report converting it cannot see.** The
> report then substitutes par. The ledger and the consolidated report disagree, both are internally
> consistent, and no arithmetic control anywhere can detect it.

---

## 6. Alternate control paths — does the control exist under another name or layer?

The `GB-03` instruction requires this question to be asked before any absence is asserted.

| Candidate substitute | Exists? | Does it discharge `GB-03`? |
|---|---|---|
| **A model constraint refusing a mis-scoped rate row** | **YES — and no round had found it.** A framework constraint on the rate model rejects any row whose company has a parent | **PARTIALLY.** It forecloses the *branch* half. It does nothing about the *null* half — the constraint passes a company-less row by construction |
| **A record rule** | YES — one, at framework level | **NO.** It admits the company-less row by an **explicit disjunct**, not by omission. And it is bypassed by every raw-SQL path |
| **Application logic substituting for a database constraint** | YES — the model default writes the root company | **NO.** A default is not a control; it is overridable in the form view by any role holding the multi-company group |
| **Access control substituting for the constraint** | Partly | **NO.** The accounting addon *widens* the framework grant: the framework gives write on the rate table to the system role only; the accounting addon adds a routine accounting-manager role with full create/write/unlink. Read is additionally granted to the **public** and **portal** roles |
| **A database uniqueness rule** | YES — `unique(date, currency, company)` | **NO, for the null case.** Under the default null-comparison semantics this does not make company-less rates single-valued. `INFERENCE`, not executed against a live database |
| **A structural constraint making branch-level FX meaningless** | **YES — and this is the strongest one found.** The company currency is a *root-delegated* field: a branch must carry its root's currency, enforced at create, at write-propagation, by a model constraint, and by a read-only form attribute | **SUBSTANTIALLY, for the branch axis.** See `MCC_C` §6 |

---

## 7. Bypass paths — enumerated, and one long-standing assumption is retired

The parent round declined to close `MCU-13` on the stated ground that *"a constraint can be bypassed
by paths that do not go through it (raw SQL: 62 sites)."* **That ground was testable and it does not
hold.**

| Bypass candidate | Result | Class |
|---|---|---|
| **Raw SQL write to the rate table** | **NONE EXISTS.** Across the full 1,752-directory path set, in `.py`, every raw-SQL site touching the rate table is a `SELECT`/`JOIN`. There is no `INSERT` and no `UPDATE` | **`A` — verified absence within the declared pattern and path set** |
| The 62 raw-SQL sites in the accounting addon | **Irrelevant to this constraint.** None of them touches the rate table; the rate table's raw-SQL sites are 8, all reads | `A`, same scope |
| `sudo()` | Does not skip Python constraints | `A` — framework semantics read at core |
| A context flag disabling constraints | **None exists.** The core validation routine has no skip parameter and no caller passes one | **`A` — verified absence in the ORM core** |
| Module install / data loading | Data records are created through the ORM; the constraint fires | `A` |
| Module **upgrade** with pre-existing rows | **NOT COVERED BY THE CONSTRAINT.** Constraints run on write, not retroactively | **`D` — a real residual. See `MCC_C` §7** |
| Migration scripts | 5 migration directories exist in the primary tree; **none references the rate table** | `A`, declared scope |
| Create the company as a root, write rates, then make it a branch | **BLOCKED.** The company model refuses any write containing the parent field, unconditionally, with an explicit error. The hierarchy is immutable after creation | **`A` — verified, and it closes the most plausible bypass** |
| Corrupt the hierarchy path column directly | Would require raw SQL on the company table; **no non-test site writes it** | `A`, declared scope |
| A localisation or custom module overriding the constraint | **NONE** in either tree; the one localisation extending the rate model adds a UI warning only | `A`, declared scope |
| Project custom modules (v18 line, three copies) | **No custom module touches the rate table** | `B` — not found in searched scope; which copy deploys is unknown |

---

## 8. Tenant and company context

| Question | Answer | Basis |
|---|---|---|
| Is the rate row company-aware? | Optionally. The company field is **not required** | `VERIFIED FACT` |
| Is it tenant-aware? | **No tenant entity exists in this domain.** SMEsPlus tenancy is an architecture-level construct with no carrier in the accounting or company model | `VERIFIED FACT`, unchanged from `MCU-61` |
| Can one company's valuation consume another's rate row? | **Yes, by design in two directions**: a descendant resolves against its root, and every company resolves the company-less row | `VERIFIED FACT` |
| Can it cross what SMEsPlus intends as a tenant boundary? | **Determined entirely by how SMEsPlus maps tenants onto companies.** If one tenant is one root company with branches, the crossings above are intra-tenant and benign. If one tenant is one company inside a shared database, the company-less row crosses every tenant in that database | **`INFERENCE` — and it is a Boss design decision, not a research question.** This is `GB-01`, and `GB-03` reduces into it |

---

## 9. Runtime consequence

Not executed against a live database this session; every statement below is read from source.

| Path | Consequence |
|---|---|
| Posting a foreign-currency entry | Resolves root-or-null, then falls back to the earliest rate ever recorded in that scope, then to par. **Three fallbacks, only the last of which is documented anywhere** |
| Consolidated / multi-company reporting | Resolves the acting company's root **only**, excluding company-less rows, then substitutes par |
| **The two disagree** | An entry can be posted at a real rate and reported at par, or vice versa. Both sides balance |
| Unrealised-FX revaluation | Uses the posting-time resolver, so it agrees with posting and disagrees with the consolidated report |
| Client-callable conversion endpoint | Takes a caller-supplied company id, browses it without an access check, and silently returns **par** when the record rule denies the rows. A wrong number, not an error |

---

## 10. Was the original closure a false positive, or the reopening a false negative?

Both questions are answered, because the instruction requires both.

| Question | Answer |
|---|---|
| Was `GAPCLOSE`'s closure of `FX-08` a **false positive**? | **PARTIALLY YES.** Its resolver-side facts are correct and re-verified. Its **writer-side** premise — that a rate can be stored against a branch — is **contradicted by a constraint that forbids exactly that**, and by an immutable company hierarchy that forecloses the only route to it. See `MCC_C` |
| Was the `MC` round's reopening a **false negative** about the constraint? | **NO — the reopening was correct**, and its refusal to declare `FX-08` invalid on the spot was also correct. Its **stated reason for that refusal** (the 62 raw-SQL sites) is what does not survive: those sites do not write the rate table, and nothing else does either |
| Was `MCE-007`'s withdrawal of rules 3 and 5 correct? | **YES for rule 3** (the scheduled feed iterates roots only). **YES for rule 5's characterisation** — the model default writes the root, which makes it a *mitigation*, not a defect vector |
| Is the count "≥9" right? | **It was right as a lower bound and wrong as a description.** The true figure over the bounded surface is **14**, and the count was never the finding |

---

## 11. Proof matrix

| Stage | Result |
|---|---|
| **Expected control** | One scoping rule, applied identically by every reader and writer |
| **Search universe** | Pattern declared §3.1; path set 791 + 961 directories + framework core; **20 files**; completeness tested against three false-negative modes |
| **Exact evidence** | 14 distinct scoping expressions; 6 include the company-less row, 6 exclude it, 2 are write-side |
| **Alternate control paths** | 6 candidates tested; **two** substantially discharge part of the blocker — a model constraint on the branch axis and root-delegation of the company currency; **none** discharges the null axis |
| **Bypass paths** | 12 enumerated; **11 closed with a declared scope**; **1 real residual** — module upgrade over pre-existing rows |
| **Tenant / company context** | Crossing is real and intentional at the company layer; its tenant meaning is undetermined **by design choice, not by missing evidence** |
| **Runtime consequence** | Posting-time and report-time resolution disagree over the company-less row; both balance; no arithmetic control detects it |
| **Final disposition** | §12 |

---

## 12. Final disposition of `GB-03`

> ## `PARTIAL` — split into two axes, one closed and one not
>
> **Axis 1 — the BRANCH axis: `VERIFIED SAFE`, with one residual.**
> A model constraint forbids a rate row from naming a company that has a parent; the company
> hierarchy cannot be altered after creation; no raw-SQL write to the rate table exists anywhere in
> the source root; no context flag skips Python constraints; and a branch cannot even hold a currency
> different from its root's. Five independent layers, and the strongest of them is structural rather
> than procedural. **Residual: rows created before the constraint existed, carried in by an upgrade or
> a database import, are not revalidated.** Class `D`.
>
> **Axis 2 — the NULL-COMPANY axis: `VERIFIED DEFECT`, and it is unchanged and unclosed.**
> The company-less rate row is admitted by an explicit disjunct in the record rule, defaults are
> overridable, the uniqueness rule does not constrain it, six resolvers admit it and six refuse it,
> and a routine accounting role can create one. This axis is `SB-05` and `T0-07`, and `GB-03`
> reduces into `GB-01` — **the SMEsPlus company/tenant boundary decision** — exactly as the parent
> gate report predicted.

**`GB-03` is therefore NOT closed, but it is now bounded, and its two halves have different owners:**
one is research-complete, one is a Boss design decision. That is a materially better position than
"re-opened, ≥9 rules, unbounded", and it is the first time in four rounds that a rule count has been
produced from a declared pattern over a proven path set.

**What would close what remains:** a decision on whether a company-less rate row is legitimate in
SMEsPlus at all. If it is not, the remedy is one constraint and one record-rule edit, and the
fourteen scoping expressions collapse to one question with one answer. **No further research
produces that decision.**

---

## 13. CORRECTION NOTICE — applied before the round closed

> **`GB-06`'s remedy, exercised. Corrections land by id in the file they contradict; the original
> text stands so the lineage is visible.** Governing record: `LAYER2_MCC_EVIDENCE/MCC_E01`.

| # | Claim in this file | Correction |
|---|---|---|
| `B-1` | §3.2 "archive tree — **961** directories … no round including this one's first pass" | **UNDERSTATED.** The correct figure for *manifested modules outside the primary tree* is **962** = 959 in the archive tree **plus 3 module directories sitting directly under the source root**, which this round missed entirely. Raised by a fresh reviewer; reproduced here |
| `B-2` | §3.2 the localisation consequence | **NOT STATED AND MATERIAL.** The primary tree holds **2** localisation modules; the archive tree holds **904**. **Every localisation claim in the programme's history is bounded to a tree containing 2 of 906 localisations** |
| `B-3` | §5 "the distinct company-scoping expressions number **fourteen**" | **CONTESTED, AND BOTH COUNTS ARE DEFENSIBLE.** A fresh reviewer independently enumerated the same bounded surface and returned **12 distinct expressions over 29 sites**, collapsing six identical raw-SQL predicates into one. This round counted **14 sites bearing an expression**. **Neither is wrong; the UNIT of count was never defined.** A bounded population with an undefined unit is not yet a denominator — recorded as a finding in `MCC_E` §5 and carried to `MCC_K` |
| `B-4` | §7 "raw-SQL write to the rate table — **NONE EXISTS**" | **STANDS, STRENGTHENED.** Independently reproduced across four version trees by a second, line-wrap-tolerant method |
| `B-5` | §7 "corrupt the hierarchy path column directly" | **STRENGTHENED.** The hierarchy path column is in the ORM's forbidden-names list and is silently stripped from both create and write; its only writers are the ORM's own hierarchy maintenance, driven by the parent field, which is itself blocked. **And even a corrupted path would not defeat the rate constraint**, which reads the parent field, not the path — it would instead silently re-point the resolver at a different root |
| `B-6` | §12 "Axis 1 — the BRANCH axis: `VERIFIED SAFE`" | **QUALIFIED BY AN ACCEPTED VETO.** Boundedness rests on **one Python constraint that fires only at create time, with no database-level constraint behind it**. It is not bounded against direct database access, and an already-corrupt row is never revalidated. A fresh reviewer vetoes *any convergence claim resting on that constraint alone*; **this session accepts the veto**, and §12's residual `MCC-C-R1` is the reason the axis is reported with a residual rather than as closed |
| `B-7` | §5 the null-company disagreement | **CONFIRMED INDEPENDENTLY AND SHARPENED.** A fresh reviewer states the arithmetic consequence exactly: a currency whose only rate row is company-less converts **at the stored rate in the ledger** and **at 1.0 in every report built on the reporting currency table**, silently. Two verified sites, one table |
| `B-8` | §5 the rule set as a whole | **A NEW MEMBER EXISTS IN v19 AND IS NOT IN THIS FILE'S COUNT.** The v19 ORM **core** adds a raw-SQL rate resolver reachable from any grouped monetary aggregation, bypassing every record rule, converting at **today** rather than the record's date, and introducing a **fourth** fallback semantic (earliest *future* rate). Zero occurrences in either v18 core. Registered `MCU-20`, `GATING` for any conclusion meant to carry into v19 |

### The disposition does not move, and one sentence is added to it

`GB-03` remains **`PARTIAL`** — branch axis research-complete with a residual, null axis an unclosed
verified defect reducing into the Boss company/tenant decision. **Added: the null axis is not merely
unclosed on this build; it is WIDER on the version SMEsPlus is targeting.**
