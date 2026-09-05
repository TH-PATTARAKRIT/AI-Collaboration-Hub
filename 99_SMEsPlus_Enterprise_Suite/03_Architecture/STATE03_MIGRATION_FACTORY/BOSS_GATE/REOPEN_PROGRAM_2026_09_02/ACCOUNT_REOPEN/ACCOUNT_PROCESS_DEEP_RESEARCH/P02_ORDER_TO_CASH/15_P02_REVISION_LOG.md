# 15 — P02 RESEARCH ERROR AND REVISION LOG

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 1. Checkpoint Log — CP-00 … CP-FINAL

All checkpoints ran under AUTO-CONTINUE. **Boss was not contacted at any checkpoint.** No option
selection, checkpoint approval, or routine confirmation was requested.

| CP | Subject | Outcome |
|---|---|---|
| CP-00 | Session boot; governance read; working branch cut from the canonical branch | Complete. Base commit recorded in `00_README_PACKAGE_INDEX.md`. The mandated boot files were sought by name: **the project constitution and the changelog were found; a master index, a system registry and a current-state file were not present under those names in the canonical tree** — recorded as a scoped negative, not as an absence. |
| CP-01 | Evidence acquisition; population and path set declared | Complete. Primary reference source located **outside** the session clone, per the standing rule that a working-tree-only search produces a false "no code access" conclusion. |
| CP-02 | O2C spine read directly by the primary session | Complete. Order lifecycle, billable-quantity computation, invoice preparation, posting routine, cost generation, valuation gate, account derivation. |
| CP-03 | Four parallel evidence tracks dispatched | Complete. T1 return/credit/refund, T2 settlement, T3 tax, T4 scope and close. Each declared its own denominator. |
| CP-04 | Process map, invoice-policy matrix, cost trace, revenue trace | Complete. Three self-corrections logged in §3. |
| CP-05 | Track evidence preserved as Layer-2 extracts | Complete. Four extracts. |
| CP-06 | Business and accounting event registers; event-to-ledger matrix | Complete. 24 business events, 13 accounting events, 16 account roles. |
| CP-07 | Return/credit/refund and settlement matrices | Complete. |
| **CP-07a** | **Constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` received mid-execution** | **Absorbed without reset.** See §4. |
| CP-08 | Scope ownership matrix; cross-process ownership and dependency register | Complete. Three scope holds raised. |
| CP-09 | Edge-case matrix; contradiction register; source link register | Complete. 34 edge cases, 10 contradictions, 69 evidence identifiers. |
| CP-10 | Independent AAS-03 adversarial challenge; AAS+ synthesis; PMO | Complete — see `16`, `17`, `18`. |
| CP-FINAL | Evidence manifest, clean-room scan, hash manifest, push | See `14_P02_EVIDENCE_MANIFEST.md`. |

## 2. Method Statement

| Aspect | Statement |
|---|---|
| Evidence basis | Primary reference source, read-only, static. |
| **Database access** | **Obtained late, after the error recorded as `RE-13`.** The package originally declared none, on an untested negative claim. One deployed archive was extracted offline; results in `21_P02_DEPLOYED_DATABASE_EVIDENCE.md`. **Runtime execution remains absent**, and that is the real reason `C-04` stays open. |
| Parallelism | Four independent evidence tracks plus one independent adversarial challenge. |
| Track authority | **None.** `Independent Review != Truth. Verified Evidence = Truth Basis.` **All eight material track findings were independently re-derived by the primary session** from the same root — five during drafting, three afterwards. The re-derivation of the last three produced **one correction to a track overstatement** (`12` C-11), which is the method's only material catch and the reason the rule exists. |
| Denominators | Declared as POPULATION / PATTERN / PATH SET / UNIT wherever an enumeration is presented as complete, per the standing denominator-completeness rule. |
| Negative claims | Every one carries its search boundary. `NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.` |
| Verdict vocabulary | The words `PASS`, `FAIL`, `APPROVED`, `CERTIFIED`, `PRODUCTION READY` and `SIGN-OFF` are not used as verdicts anywhere in this package. Mechanically scanned at CP-FINAL. |

## 3. Research Errors And Self-Corrections

Preserved, not deleted, per the constitution.

| # | Original conclusion | Correction | How it was caught | Materiality |
|---|---|---|---|---|
| **RE-01** | "With the Thai chart installed and real-time valuation on, the outflow routine raises a hard error at delivery confirmation." | Real-time valuation **cannot be switched on at all** without the three stock accounts — a validation constraint on the product category refuses the change. The runtime guard is a **second** line of defence, and its existence is itself evidence that the configuration constraint is not considered sufficient. Both are further weakened because the accounts and the valuation mode are **company-dependent**, so the constraint validates only the writing company's context. | Re-reading primary source after writing the conclusion. | Moderate — the corrected statement is a **better** control than the original claimed, and the multi-company weakening is a finding the original missed. |
| **RE-02** | "The document date is what a tax authority sees; the accounting date is what the ledger sees — the two diverge." | Sharper and worse: **the tax report keys on the accounting date as well.** The printed tax invoice shows the original date while **both** the VAT return and the ledger use the later period. | Track T3 §1, which read the report engine's own date domain. | High — it changes the shape of the statutory question routed to the tax track. |
| **RE-03** | "Split recognition off means cost of sales is recognised at delivery." | Only if the outbound stock account happens to be an expense account. **A third outcome exists** — split recognition off with an interim outbound account — in which **cost of sales is recognised nowhere** and the value parks in an asset account indefinitely. That third outcome is the **Thai-chart default shape**. | Reading the account resolution independently of the boolean, rather than assuming they moved together. | **Maximum.** It is the headline finding of the package. |

| **RE-04** | "The order line's delivered quantity is **directly user-writable**." | Too strong. At the **data layer** the field is stored with its read-only attribute cleared, so any programmatic path can write it. At the **interface layer** it is rendered read-only whenever the derivation method is not manual — which, for goods with the inventory module installed, it is not. The field is a pure human assertion **for service lines** and for goods without the inventory module; for goods with it, the interface blocks casual overwriting while the data layer does not. | Reading the interface definition after writing the finding, in anticipation of the independent challenge. | **High as a reliance matter, low as a finding.** The underlying violation — that *how much left the business* has two holders and the one governing revenue is the field, not the ledger — **survives unchanged**. What changed is who can reach it and how. Full corrected statement in `05` §3a. |
| **RE-05** | Carried from track T4: "Creating any company rewires stock routing on every other company in the database." | The rewiring routine **returns early unless the acting user holds the multi-company group**. The database-wide unarchive of the shared location **is** unconditional; the rewiring is gated. | Independent re-derivation of a track-sourced finding by the primary session. | Moderate. The scope conclusion stands — the object still has no owning scope — but its scale claim is narrowed. Recorded as `12` C-11. |

| **RE-06** | "The receivable ledger has no duplicate-recognition control at all." | **Wrong.** A duplicate **detector** exists and covers customer invoices, matching on company, commercial partner, document type, total amount and document date. It is **display-only** on the sales side — its only behavioural consumer suppresses automatic posting of **vendor bills** — and its database index is created for purchase documents only. | The primary session **re-testing its own negative claim** before the independent challenge ran. | **High.** The corrected finding is **stronger** than the original: the system already knows how to detect a duplicated customer invoice and does not act on it. Full correction in `04` §11. |

| **RE-07** | `11` §9 stated "8 sound, 21 defect classes, 7 tolerance-zero, 1 unknown". | The table beneath it gives 8 `ok`, **18** `defect class`, **6** `tolerance-zero`, and four other classes. **The headline did not reproduce from its own table.** | Independent challenge **CH-14**; recounted mechanically by the primary session. | **High as a method matter.** This is precisely the enumeration failure the SMEsPlus denominator rule exists to prevent, in the file most likely to be read as a summary. |
| **RE-08** | "The Thai chart supports the inbound interim direction and not the outbound." | **Wrong.** The account is wired to nothing; neither direction is supported. | Independent challenge **CH-01**; re-derived and confirmed. | **Maximum.** It was a headline in two files and it routed a false symmetry question to P01. |
| **RE-09** | "Two confirmed phantom-cost paths follow from the eligibility mismatch." | **One.** The owner-restricted path produces no cost line on an order-linked invoice. | Independent challenge **CH-02**; re-derived and confirmed. | Moderate — removes a claimed defect and reclassifies an edge case as sound. |
| **RE-10** | "The obligation ledger resolves six findings." | **Three of the six are one defect described three times; three are untouched by it.** | Independent challenge **CH-13**; the arithmetic is checkable against the package's own text. | **High.** It was the package's principal structural handoff. |
| **RE-11** | `03` §5 tagged idempotency `FACT VERIFIED` while `03` §6 explicitly declined to advance it. | The two halves carry different tags and the summary row took the stronger one. | Independent challenge **CH-15**. | Moderate — the adversarial-section-not-summary failure inside a single file. |
| **RE-12** | The configuration premise (split recognition on, storable, real-time) was assumed in eleven files and declared in none. | Now declared once, package-wide, in `00` §3b. | Independent challenge **CH-19**/**CH-30**. | High — without it, eleven files reason about a configuration the package's own headline says a Thai company does not have. |

| **RE-13** | "This session had no database or runtime evidence" — repeated in six deliverables and used to explain two undischarged requirements and one open unknown. | **False, and never tested.** Five deployed database archives were on the execution host with restore tooling installed. A declared absence of evidence is a **negative claim**, and this one had no declared search behind it. | Reading a **peer session's memory file**, which recorded the identical error on P10. **Not** found by six self-corrections, and **not** by the twenty-finding independent challenge — every review was scoped at the findings, none at the evidence base. | **Maximum.** It is the package's most-repeated limitation, it bounded the exit assessment, and it was wrong. What one pass over that evidence produced is in `21` — an empirical confirmation of the package's central mechanism claim, and one live exposure the package had not identified. |

| **RE-14** | This session's own research brief for the eight-scenario track asserted that the period-end unrealised-FX revaluation fields might be **v19-only**. | **Wrong.** They are present in v18 at identical definitions (`EV-P02-115`). The finding that matters is that the mechanism is **Enterprise-licensed in both** generations, so a Community-equivalent deployment has never had it. | The track itself, because the brief instructed it to report any wrong path in the brief as a finding. | Moderate. It is recorded because **the brief was written by this session**: a generation difference was asserted from a field list rather than from a check. The instruction that caught it is worth keeping in every brief. |
| **RE-15** | `22` §3.3 listed the mechanism inventory as five, with manual periodic cost "outside the process in both generations". | **Incomplete.** v19 provides an **automated aggregate periodic close** with its own cron (`EV-P02-111`, `EV-P02-112`) — a sixth mechanism. It is configured to run for **zero** companies in the estate, which strengthens rather than weakens the conclusion. | The eight-scenario track; re-verified by the primary session including the cron-domain eligibility count. | High. A mechanism inventory that misses a mechanism is the same defect class as a denominator that misses a member. |

| **RE-16** | `22` TC-01: "6 distinct archives. All 6 examined. 0 remaining." | **REFUTED twice over.** There are **8 archive files / 5 distinct databases by UUID**. Two archives were never opened — Odoo web-backup **ZIPs**, a format the search pattern (`*.dump`, `dump.sql`, `*.backup`) did not cover. And the deduplication key was wrong: file content, where the authoritative key is the database UUID. | Fresh independent AAS-03 challenge; both archives verified present by the primary session. | **Maximum. This is the THIRD evidence-base failure in this package**, after `RE-13` (no search at all) and the tooling gap (default binary refuses two archives). Same class each time: a negative claim resting on a pattern narrower than the claim. |
| **RE-17** | `22` §1 and §3.1: `iSMEs` is "v18-line". | **REFUTED.** It is **Odoo 16.0** on every core module, verified from the installed-module table. The label was **inferred from field presence, not checked.** | Fresh challenge; re-derived by the primary session. | **Maximum.** The only database with transaction volume is on a generation whose source **does not exist on this host**, so its mechanism cannot be read at all. It also means the v18 analysis describes **zero** deployed instances. |
| **RE-18** | `22` TC-15: the mismatch is "predominantly invoice-before-delivery". | **REFUTED.** Measured on the **posted valuation entry's accounting date** — the date that actually determines the period — the direction **reverses**: mismatch 31.6% not 44.5%, cost-before-revenue 707 against 516. And the caveat that permitted the error ("the movement date equals its validation date") is itself false, with **10,871 counter-examples**. | Fresh challenge; reproduced to the unit by the primary session. | **Maximum.** TC-14 (the mismatch exists, 31.6%) survives; TC-15 (its direction) does not. A date field was chosen by convenience, caveated rather than tested, and the caveat was wrong. |
| **RE-19** | `22` TC-03 ("false in all 93"), TC-04 ("88"), TC-08 ("every v19 company has a NULL stock journal"), §12 ("no tax is treated on a cash basis"). | All four **REFUTED**: 91 false + 2 NULL; 89 not 88 (the file's own prose sums to 89); two of three real-time companies **do** carry a stock journal; and **7,738 posted cash-basis entries** exist. | Fresh challenge; each re-derived. | High. TC-03 is the **third** instance in this package of a claim contradicted by evidence in the same file — four lines below it. |

| **RE-20** | `22` TC-01 and `25` §8: the population is "8 files / 5 databases", declared complete. | **REFUTED a fourth time.** A peer reported a database in `~/OCC_BACKUP` — **outside P02's declared path set** of `~/Downloads` + `/Volumes/iMacSys`. The corrective signature sweep then found **16 artefacts / 7 distinct databases across three generations**. And **the sweep itself carried a false negative** of the same family — its plain-SQL arm read only the first 200 KB and missed a database P02 already knew about. | Peer process P04; the sweep's own defect found by checking it against the known population. | **Maximum.** Fourth population correction, third by an outside party. **PATH SET is the denominator component P02 has never got right** — POPULATION, PATTERN and UNIT were declared and executed every time. |
| **RE-21** | Six deliverables state that runtime evidence "does not exist for this session", and the PMO used it to bound EC-08 and C-04. | **REFUTED.** `~/OCC_Odoo18_Simulation_Lab` is a complete Docker Odoo 18 lab — safe, resettable, no customer data — and `scripts/anglo_gross_profit_test.py` **already scripts the outcome-1 scenario end to end**, including the between-delivery-and-invoice snapshot and the interim-balance print. | Following the peer's path-set correction into the same directory tree. | **Maximum. Fifth evidence-base failure, all the same family.** C-04 reclassified from `EVIDENCE REQUIRED` to `AUTHORISATION REQUIRED`. P02 did **not** run the script — it commits transactions and the constitution forbids DB changes. |

| **RE-22** | `26` §9 published "16 database-bearing artefacts … 7 distinct databases". | **A read of a background job that was still running.** On completion: **26 artefacts and climbing**, including an entire unconsidered location — **iCloud Drive** — holding at least five further deployed databases, three of them distinct (`iMSCG` 16.0, `pankhamhom` 18.0, `T805efaplus` 18.0). | Re-reading the sweep output after the count had been published. | **Maximum. Sixth evidence-base failure, and a new class: publishing a partial as a total.** P02 now publishes the **invariant, not the count** — zero COGS in every database tested, population open. |
| **RE-23** | The declared v18 source root is the code the deployment runs. | **Refuted. 66 of 361 installed modules are absent from it**, including `inherit_sales` and `inherit_inventory` — which by name override the two modules P02 is entirely about, and which **exist nowhere on this host**. Two directories share the same build string with 797 and 799 addons, so the build string does not identify code. | P04's warning, checked against `idemo18_uat`. | **Maximum.** It bounds **every** source-derived negative in the package and has already refuted one published `VERIFIED ABSENCE` (`C-32`). **The path set has now failed on all three axes: archives, runtime, and source.** |
| **RE-24** | No cross-validation exists between the settings that jointly determine where cost of sales is recognised — **in either generation**. | **Refuted for v18.** `stock_account/models/product.py:964 _check_valuation_accounts` is an `@api.constrains` — it fires on create/write including imports and scripts — requiring all three category stock accounts when `property_valuation == 'real_time'`. What survives is sharper: the guard is **one-directional** (silent when valuation is unset, which is exactly the deployed `idemo18_uat` state), it **never references `res_company.anglo_saxon_accounting`**, and the field carries **no `default=`**. **v19 removes the guard entirely** (whole-tree 1 file → 0, `property_valuation` persisting 39 → 37 files as the control) and resolves valuation by a category-then-company fallback with no account requirement. | Running P04's onchange lead on P02's own path. The lead itself did not apply; the search for it found this. **Not a missed reading — `EV-P02-045` and `00` §3b already carried the guard.** The package asserted the guard in one file and its absence in another, and published both. | **High.** It corrects one published statement (`22` §13) **against another the package already contained** (`00` §3b), and **leaves four others standing**, because they name the company × category pair the guard does not reach. It also produces `P02-F-05c`: on the target generation the one existing cross-validation of cost-recognition configuration is gone. |
| **RE-25** | Two 14.0 databases measured `cogs = 0` with the injection control reporting 0. | **The control was broken, not the data.** The injected row carried 40 fields while 14.0's `display_type` is column **45 of 66**, so the synthetic marker was never present. Re-measured with the injection sized from the `COPY` header; both now fire and both remain `cogs = 0`. | Reading the control column instead of the result column. | **High.** Two of 17 zeros were uncontrolled at first tabulation. |
| **RE-26** | Predicate B (lines on accounts typed `expense_direct_cost`) discriminates *cost at delivery* from *cost nowhere*. | **Overstated.** Those accounts also take vendor-bill and manual lines. Near-miss: B returned **49,957** for `iSMEs` against a published zero and read as a refutation of P02's own headline; it is the outcome-2 figure `21` already reports. | Checking the package's `DB-10` definition before believing a new number. | **Maximum, had it shipped.** It would have refuted the headline with a figure that corroborates it. |
| **RE-27** | Scenario 8 has **no** deployed population — `lot_valuated` measured 0 everywhere. | **False zero from a predicate that could not fire.** The set-test used `v+0 != 0`; a PostgreSQL boolean is `t`, and `"t"+0 == 0`, so every true boolean was counted as unset. Caught by a positive control on `sale_ok` (which returned an impossible 0). After the fix: **9 lot-valuated templates across 3 deployments, one on 19.0**. | Positive control, not inspection. | **High.** Unfixed, scenario 8 would have been downgraded from a retained defect to latent. |
| **RE-28** | New design candidates issued as `DC-1` … `DC-6`. | **Identifier collision.** The package already uses a two-part scheme (`DC-08-02`, `DC-11-01`, …). Renamed to **`DC-38-01` … `DC-38-06`**. | Mechanical family enumeration at CP-08. | **Low in substance, high in discipline.** A new family invented beside an existing one is a defect even when every row is correct. |
| **RE-29** | Delivered-not-invoiced measured with `qty_invoiced`. | **Wrong counter.** It counts drafts; the accounting counter `qty_invoiced_posted` is non-stored. Posted-only re-measure on `iSMEs`: **1,145 not 47** — a **24× understatement** — and **`P02-F-34b`'s direction reverses**. | AAS-03 Expert 1, CH-4. | **Maximum.** A headline finding published in this same round, withdrawn in the same round. |
| **RE-30** | Thai localisation negatives stated unqualified. | **Single-generation.** The v19 Thai chart is 144 accounts vs 27 and supplies four things declared absent. **The refutations are inside P02's own declared PATH SET.** | AAS-03 Expert 3. | **High.** Four published negatives re-qualified; the rule now stated once, prominently. |
| **RE-31** | `27` §4's withdrawal was sufficient. | **It was not applied to the owning register.** `06` line 70 carried the withdrawn `VERIFIED ABSENCE` verbatim. | AAS-03 Expert 3, C-7. | **Medium.** The defect class is already in memory as *a revision log is not a correction*; it recurred here. |
| **RE-25** | Two v14 databases measured `cogs = 0` with the injection control reporting 0. | **The control was broken, not the data.** The injected row carried 40 fields while v14's `display_type` is column **45 of 66**, so the synthetic marker was never present. Both re-measured with the injection sized from the `COPY` header; both now fire and both remain `cogs = 0`. **A control that cannot fire is indistinguishable from one that found nothing** — the fourth time this package has recorded that shape. | Reading the control column instead of the result column. | **High.** Two of 17 zeros were uncontrolled at the moment of first tabulation. |
| **RE-26** | Predicate B (lines on accounts typed `expense_direct_cost`) discriminates *cost at delivery* from *cost nowhere*. | **Overstated.** Those accounts also receive vendor-bill and manual lines, so `idemo18_uat`'s 7,310 type-B lines are not evidence that delivery-side valuation posted — predicate C shows it did not (0 of 47,242). Predicate C was added because B cannot answer the question. **Near-miss:** B returned 49,957 for `iSMEs` against a published zero and read as a refutation of the headline; it is the outcome-2 figure `21` already reports. | Checking the package's `DB-10` definition before believing my own number. | **Maximum, had it shipped.** It would have refuted P02's headline with a figure that corroborates it. |

**Pattern observation, recorded as method evidence.** The first six corrections came from **re-reading
primary source after writing a conclusion**, or from re-deriving a track's finding — none came from a
reviewer. Each first-pass statement was
plausible and each was narrowed by source. **RE-07 through RE-12 came from the independent challenge, and they are of a different kind.** The
self-found corrections were reachability and scale qualifications around findings that were themselves
correct. The challenge-found ones include **two outright refutations of `FACT VERIFIED` statements**
(RE-08, RE-09), **one inflated structural claim** (RE-10), **one count that did not reproduce from its own
table** (RE-07), and **one undeclared package-wide premise** (RE-12).

The pattern is unambiguous and is recorded as method evidence: **self-review corrected the edges of
findings; independent review corrected the findings, the counts and the claims built on top of them.**
Nothing in the detailed citations was found to be fabricated or misread — **what failed was
aggregation.**

Two of the first six (RE-04, RE-05) were **overstatements of scale
or reachability around a finding that was itself correct** — which is the specific failure mode that makes
a finding easy to dismiss on review even though its substance holds. This is precisely the failure mode the negative-claim standard
describes, and it is the reason the independent challenge in `16_P02_AAS03_CHALLENGE.md` was commissioned
against this package's own claims rather than against the reference.

## 4. Impact Revalidation — Constitution Correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`

The correction supersedes any wording implying **"Tenant Context + Company Context are mandatory for
every operation"** and installs the three-scope model **PLATFORM / TENANT / COMPANY**.

### 4.1 Handling

| Requirement | Action taken |
|---|---|
| Do not reset | **No reset.** Execution continued from CP-07a. |
| Do not restart from L1 | **No restart.** |
| Do not discard existing evidence | **Nothing discarded.** All four track extracts, all 69 evidence identifiers, all checkpoints and all contradictions preserved unchanged. |
| Do not repeat completed work without material delta | **Nothing repeated.** Deliverables 00–09 were written at company level and are undisturbed by the correction. |
| Update the scope ownership matrix | **Created** as deliverable `20_P02_SCOPE_OWNERSHIP_MATRIX.md`. |
| Update the contradiction register | **C-09 added** by that file's §8. |
| Update the dependency register | **P02-SC-01, SC-02, SC-03 added** to `10_P02_CROSS_PROCESS_OWNERSHIP.md` §3. |
| Update this log | This section. |

### 4.2 Affected-Finding Record, In The Mandated Format

Exactly **one** produced artefact required re-expression.

| Field | Content |
|---|---|
| **Original finding** | Track T4's §9 "tenant-layer gap", commissioned before the correction with the framing *"Tenant = independent customer/corporate group, hard isolation"*, and phrased as *what a tenant layer would have to add on top of the company boundary*. |
| **Scope assumption used** | An implicit two-level model — tenant wraps company — with no PLATFORM level and no notion that an operation might legitimately be tenant-scoped **without** a company context. |
| **Why it is over-constrained** | It admits no PLATFORM scope, so platform reference data has nowhere to live; and it implies that every operation inside a tenant must also carry a company, which the canonical model explicitly denies for tenant-scoped operations. |
| **Correct scope analysis** | Performed in `20_P02_SCOPE_OWNERSHIP_MATRIX.md` §2, §3 and §7 against the three-scope model, with each object's owning, executing, accessing, mutating and referencing scope determined separately, and with the financial-effect question answered independently of the ownership question. |
| **Updated classification** | The T4 **evidence** is unchanged and remains `FACT VERIFIED` — it is scope-neutral observation of a company boundary. The T4 **gap analysis** is superseded by `20` §3 (SF-01 … SF-08) and is retained in the extract with a scope note attached at its head. |
| **Architecture impact** | Three material additions the two-level framing could not have produced: **SD-05** — there is no PLATFORM-scoped object in the P02 transaction path, only platform reference data the path consults; **SF-04** — the shared transit location has **no owning scope at all**, which is a stronger statement than "it is not tenant-aware"; **SD-06** — ownership, availability and financial scope are already three distinct things in the reference, evidenced. |
| **Cross-process impact** | Three scope questions were raised that the two-level framing would have answered by assumption: the currency rate (`P02-SC-01`), the chart of accounts (`P02-SC-02`), and intercompany execution scope (`P02-SC-03`). All three are held and routed, not decided. |
| **Evidence required** | For SC-01: the existing FX ownership ruling plus a determination of whether the rate **table** and the rate **application** are separate objects at separate scopes. For SC-02: whether account structure is a tenant standard companies instantiate, or a per-company object. For SC-03: whether an intercompany pair may cross a tenant boundary — P02's evidenced position is **no by default**, under `UNRELATED INDEPENDENT COMPANIES = SEPARATE TENANTS BY DEFAULT`. |

### 4.3 Findings Checked And Confirmed Unaffected

Each was re-read against the correction and required no change:

| Deliverable | Why unaffected |
|---|---|
| `01` process map | Describes company-level document flow. Makes no tenant claim. |
| `02` invoice policy | Product- and company-level configuration. The tenant/company split of the *policy* is added in `20` §2 as a design candidate, not a correction. |
| `03` cost trace, `04` revenue trace | Both entirely company-scoped. All nine financial effects are company-owned (`05` §2). |
| `05`, `06`, `07` registers | Event and ledger structure, company-scoped throughout. |
| `08`, `09` matrices | Document and settlement mechanics, company-scoped. |
| `11` edge cases | The multi-company section (§8) reports company-boundary behaviour as observed; it asserts no tenant requirement. |
| `12`, `13` registers | Evidence, not design. |

### 4.4 Peer Dependency Statement

Per the correction's cross-process rule, **this session did not stop** for any peer process. P01
Procure-to-Pay is executing in parallel and its scope determinations are not yet available; that is
recorded as `PEER DEPENDENCY OPEN` **D-05** in `10_P02_CROSS_PROCESS_OWNERSHIP.md` §3 and blocks **only**
the vendor-side symmetry conclusion. All unaffected work continued and completed. Continuous cross-process
scope reconciliation is P11's mandate, not P02's.

## 5. Deliverable Completion Record

| Required deliverable (as named in the directive) | Produced as | Status |
|---|---|---|
| `P02_PROCESS_MAP.md` | `01_P02_PROCESS_MAP.md` | complete |
| `P02_INVOICE_POLICY_MATRIX.md` | `02_...` | complete |
| `P02_DELIVERY_COGS_TRACE.md` | `03_...` | complete |
| `P02_REVENUE_AR_TRACE.md` | `04_...` | complete |
| `P02_BUSINESS_EVENT_REGISTER.md` | `05_...` | complete |
| `P02_ACCOUNTING_EVENT_REGISTER.md` | `06_...` | complete |
| `P02_EVENT_TO_GL_MATRIX.md` | `07_...` | complete |
| `P02_RETURN_CREDIT_REFUND_MATRIX.md` | `08_...` | complete |
| `P02_PAYMENT_RECONCILIATION_MATRIX.md` | `09_...` | complete |
| `P02_CROSS_PROCESS_OWNERSHIP.md` | `10_...` | complete |
| `P02_EDGE_CASE_MATRIX.md` | `11_...` | complete |
| `P02_CONTRADICTION_REGISTER.md` | `12_...` | complete |
| `P02_SOURCE_LINK_REGISTER.md` | `13_...` | complete |
| `P02_EVIDENCE_MANIFEST.md` | `14_...` | complete |
| `P02_REVISION_LOG.md` | `15_...` (this file) | complete |
| `P02_AAS03_CHALLENGE.md` | `16_...` | complete |
| `P02_AAS_PLUS.md` | `17_...` | complete |
| `P02_PMO.md` | `18_...` | complete |
| `P02_CORE_RECON_HANDOFF_PACK.md` | `19_...` | complete — **Layer 1** |
| *(added by correction CORR1)* | `20_P02_SCOPE_OWNERSHIP_MATRIX.md` | complete |

**20 of 20 deliverables produced.** Number prefixes are for ordering only; every mandated filename is
preserved verbatim within its prefixed name.

## 6. Declared Limitations

Stated plainly so no reader over-relies on this package.

1. **No database or runtime evidence.** Everything is static-source. `C-04` cannot be closed without it.
   > **`L-03` CORRECTION (`30`, C1).** **Half of this is false.** Database evidence is present and
   > extensive (`21`, `28`). **Runtime** evidence remains absent, and the second clause stands: `C-04`
   > cannot be closed from static source. Splitting the two is what makes the `33` authorisation pack
   > possible.
2. **Path set bounded to the O2C spine.** Subscriptions, point of sale, e-commerce, rental, projects,
   manufacturing and deferred-revenue modules were **NOT YET SEARCHED** and are excluded by declaration.
   Any of them could add an O2C-relevant event.
3. **Reporting layers largely out of scope.** The claim that no exception report exists for
   delivered-not-invoiced is `NOT YET SEARCHED`, not a verified absence.
4. **All three findings that initially rested on a single track's reading have since been independently
   re-derived** by the primary session — record and the one correction produced in `12` §5 and §6.
5. **Localisation modules were not enumerated as their own denominator** for the year-close negative claim.
6. **Only two localisation modules exist in this tree**, which bounds every claim about chart defaults.
7. **All Thai statutory questions are held.** This package has no authority to state Thai law and does not.
0. **The package's own statement of what evidence it had was wrong** (`RE-13`), and no review caught it.
   **Scope one review at the evidence base itself, not only at the findings.**
8. **`EC-07` is not satisfied, and the first pass was not clean.** One independent challenge has run. It
   produced **twenty package-changing findings and six accepted coverage gaps**, including **two outright
   refutations of statements this package had tagged `FACT VERIFIED`**. A second consecutive clean pass has
   not occurred and cannot be claimed.
9. **The challenge examined roughly half the evidence base.** It verified **no** citation in the return /
   credit / refund or settlement / FX / deposit extracts, so `08`, `09`, accounting events AE-05…AE-13 and
   edge cases 18–30 are **once-verified, not twice-verified**. There is no basis for assuming the
   unexamined half is cleaner than the examined half.
10. **Eight business situations have no case in this package** and are accepted as gaps, not closed:
    drop-shipping, credit control, period-end unrealised FX revaluation, bill-and-hold, outbound
    consignment, warranty/return provision at point of sale, freight charges and their tax treatment, and
    serial/lot-identified cost of sales.
