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
| **Database access** | **None.** No runtime execution, no query, no dump. Every statement is static-source derived unless explicitly marked. This is a declared limitation, not an oversight — it is why `C-04` remains `UNRESOLVED — EVIDENCE REQUIRED`. |
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
