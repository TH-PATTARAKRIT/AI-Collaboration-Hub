# P10 — TIME-BASED RECOGNITION MODEL

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001`
Correction applied: `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction)
Process: `P10 — Time-Based Recognition`
Depth: `VERY DEEP / L99999.99999`
Layer: **1 — Clean-room business semantics.** Raw source citations live in Layer 2 and are referenced here by evidence ID only.
Terminal state of this document: `READY FOR CORE ACCOUNTING RECONCILIATION`

---

## 1. What P10 Governs

P10 owns every accounting event whose **date is derived from the passage of time against a schedule**, rather than from the occurrence of a business transaction.

The distinguishing test used throughout this research:

> If the entry would still have to be made even though nothing happened in the business that day, it is a time-based recognition event.

This captures: deferred revenue, deferred expense, prepayment amortisation, accrued expense, accrued revenue, and — by the same test — asset depreciation and loan amortisation. It deliberately **excludes** transaction-driven entries (invoicing, payment, goods movement), which belong to P01–P06.

## 2. The Six Semantic Primitives

~~Every time-based recognition in scope decomposes into exactly six primitives.~~ **CORRECTED — `66` Challenge C §4.**

> Six primitives for **schedule-shaped** mechanisms. Four defects in the model as first stated: **`TR-5` is not primitive** — it is derived from `TR-2 × TR-3` and `TR-1 × TR-4`, and its only irreducible content is a *stable identity*, which is not in the list; **`TR-4` is at least three independently-varying policies** (day-count, rounding, residue destination), settled in different places and differing between the two deferral paths; **two primitives are missing** — the *termination condition* (value-terminated versus count-terminated) and the distinction between *allocating* a known base and *generating* amounts that do not exist until the schedule is computed, which is what loan interest does; and the **accrual instantiates two of six**, so the universal quantifier is contradicted by a mechanism the model's own inclusion test admits.
>
> There is also an internal inconsistency: §3 locates the collapse at *"Accounting Event and Journal are the same act"*, and **`Accounting Event` is a stage with no primitive**.

This decomposition is the analytical spine of the package for the schedule-shaped mechanisms, and is stated with those four repairs outstanding.

| # | Primitive | Definition | Why it must be a first-class object |
|---|-----------|------------|-------------------------------------|
| `TR-1` | **Recognition Base** | The measured amount to be spread, and its currency. | Correction behaviour depends on knowing what the base *was* when the schedule was built. |
| `TR-2` | **Recognition Window** | Start and end instants of the economic service/benefit period. | This is a business fact, independent of any calendar or accounting period. |
| `TR-3` | **Period Grid** | The set of accounting periods the window is cut into. | Belongs to the *company's* fiscal calendar, not to the transaction. |
| `TR-4` | **Allocation Rule** | How the base is distributed across the grid (day-count convention, rounding, residue absorption). | Two systems can agree on base, window and grid and still disagree on every monthly amount. |
| `TR-5` | **Recognition Event** | One (period, amount) pair with a stable identity. | Without identity there is no way to say "this period has already been recognised", so duplicate and lost recognition cannot be detected. |
| `TR-6` | **Posting Act** | The journal entry that realises one recognition event at a point in time. | Posting can be deferred, blocked, re-dated or reversed independently of the event. Event and posting are **not** the same thing. |

> **SCOPED AND PARTLY REFUTED — `66` Challenge C §2.** The collapse holds for **two of the four mechanisms re-verified** — both deferral paths and the accrual — and **not** for the asset or the loan. The asset entry carries **two independent date fields**, a posting date and a period-beginning date. And of the four consequences claimed to follow from the collapse, **only one does**: catch-up exists on a path with no event object, the silent period shift is caused by the shared posting layer and is merely made *undetectable* by the collapse, and currency capability is orthogonal — the loan has the strongest identity of any mechanism and still cannot express a foreign currency.
>
> **The correction that matters for the design:** the asset carries its period **and is still silently re-dated**. So carrying a period is **necessary and not sufficient** — a design can hold the field and never read it, which is what the asset engine does for lock purposes today. Requirement `R-02` must be paired with the reportable-divergence obligation.

**The single most important structural finding of this session is that the reference ERP collapses `TR-5` into `TR-6` for deferrals.** A deferral recognition event has no existence apart from the journal entry that carries it (`E-P10-001`, `E-P10-008`, `E-P10-042`). Everything that follows in this package — duplicate exposure, the absence of catch-up, the silent period shift, the unrepresentable foreign currency — is a consequence of that one collapse.

## 3. The Canonical Trace

The Boss-mandated trace, resolved against the six primitives:

```
Source Document        -> carries TR-1 and TR-2
Recognition Base       -> TR-1  (amount + currency + measurement date)
Schedule               -> TR-2 x TR-3 x TR-4 = the derived event set
Period Event           -> TR-5  (one recognition event; MUST have identity)
Accounting Event       -> the decision that TR-5 is now recognisable
Journal                -> TR-6  (the posting act)
Modification           -> a new version of TR-1/TR-2/TR-4 producing a delta event set
Reversal               -> negation of one or more TR-6, with TR-5 preserved
Reporting              -> aggregation over TR-5, NOT over TR-6
Close                  -> freezes TR-6 for a period; MUST NOT silently move TR-5
```

Two of these ten stages are, in the reference behaviour, not separable:

- `Accounting Event` and `Journal` are the same act for deferrals — the entry is created at source-posting time for every future period at once (`E-P10-008`).
- `Reporting` aggregates `TR-6`, not `TR-5`, because `TR-5` does not exist as data.

## 4. The Mechanisms Actually Present in the Reference Product

> **CORRECTION `P10-R-01`, applied after independent challenge.** The primary author's first enumeration declared **five** mechanisms. Independent challenge found **at least two more** that the declared pattern had missed, and demonstrated that the pattern misses any mechanism that materialises entries by copying an existing one. The population is therefore stated as a **floor of eight, not a total**, and the pattern's false-negative mode is declared with it. This is the `PATTERN` clause of the project denominator rule failing exactly as it has failed in previous rounds; it was caught by independent review, not by the author.

Deterministic enumeration (`P10_ENUM_02`, population/pattern/unit/path-set declared in the script header) plus the independent challenge found **at least eight** independent implementations of "a schedule produces dated journal entries" in the declared reference root. No two of them share a line of scheduling, day-count or rounding code — verified for the four named helper functions, class `B` for arbitrary shared utilities.

| Mechanism | What it recognises | Schedule object | Event identity | Trigger |
|-----------|--------------------|-----------------|----------------|---------|
| `M1` Deferral (revenue and expense) | An already-invoiced amount, over its service window | **None** — two dates on a journal item (`E-P10-001`) | **None** (`P10-F-07`) | Source document posting, or a report button (`E-P10-002`, `E-P10-019`) |
| `M2` Accrual | An amount **not** yet invoiced, at one point in time | None — a transient wizard (`E-P10-024`) | None; back-link is dead code (`E-P10-027`) | Manual, per selection of orders |
| `M3` Asset depreciation | A capitalised cost over its useful life | Persistent asset + persistent board (`E-P10-029`) | Yes — entry carries the asset link | Asset confirmation; board recompute |
| `M4` Loan amortisation | A contractual obligation over its term | Persistent loan + persistent schedule lines (`E-P10-032`) | **The strongest of any mechanism examined** — entry carries the schedule-line link and an entry-type marker (`E-P10-033`) | Loan confirmation |
| `M1b` Deferral — grouped path | The same fact as `M1`, in a different journal shape | **None** | **None** | A report button (`E-P10-019`) |
| `M6` Periodic transfer model | A balance moved between accounts on a declared frequency | persistent, with start date, stop date and frequency (`E-P10-067`) | back-link on the generated entry | scheduled automatic run |
| `M7` Automatic entry — period reallocation | A posted amount reallocated across periods | none — transient | counterpart lines | manual, on selected journal items (`E-P10-047`) |
| `M5` Recurring entries | Nothing in particular — repeats a whole entry forward | None; a self-referencing chain (`E-P10-039`) | Origin link only | Posting of the previous occurrence |

`M1`, `M3` and `M4` are edition-gated in the reference product; `M2` and `M5` are in the base accounting module (`E-P10-044`). This is a distribution fact about the reference product, not a constraint on SMEsPlus — but it is the most plausible explanation for why they never converged, and it is therefore evidence about *how the divergence arose*, not evidence that divergence is correct.

## 5. Scope Model (per `SMEPLUS-26-09-04-ACC-REV2-CORR1`)

Applying the canonical scope model — PLATFORM / TENANT / COMPANY, with `OWNERSHIP != AVAILABILITY` and `EXECUTES != OWNS` — to the six primitives:

| Primitive | Owning scope | Rationale |
|-----------|--------------|-----------|
| `TR-1` Recognition Base | **COMPANY** | It is a measured amount in a company's books, in that company's currency of account. |
| `TR-2` Recognition Window | **TENANT** (referenced by COMPANY) | The service period is a customer/contract fact. It does not change when the same contract is billed by a different company of the same tenant. |
| `TR-3` Period Grid | **COMPANY** | The fiscal calendar is a legal boundary. |
| `TR-4` Allocation Rule | **TENANT default, COMPANY binding** | A day-count convention is a policy the tenant may standardise, but the amount it produces is company financial truth, so the *binding* value must be the company's. |
| `TR-5` Recognition Event | **COMPANY** | It is a financial effect. |
| `TR-6` Posting Act | **COMPANY** | It is a journal entry. |
| Day-count convention *definitions* (30/360, actual/actual) | **PLATFORM** candidate | Reference data with no tenant or company semantics. Availability, not ownership. |

Two scope defects follow directly and are recorded as `P10-F-02` and `P10-F-03`: in both, the **executing** scope (the active company at the moment of execution) supplies a value that the **owning** scope (the document's company) must supply. Under the corrected constitution this is not a multi-company inconvenience — it is a case of a COMPANY-scoped financial effect being parameterised from outside its owning scope, and `MISSING REQUIRED SCOPE = DENY` is not applied.

## 6. Headline Findings

| ID | Finding | Class | Severity |
|----|---------|-------|----------|
| `P10-F-01` | **At least eight** independent time-based recognition implementations exist in the reference product, with no shared kernel and no shared vocabulary. The count is a declared floor, not a total (`NC-01`, class `D`). | VERIFIED FACT for the existence of each; class `D` for any total | Design-governing |
| `P10-F-21` | Inside the grouped deferral generation the direction is passed as a boolean where a direction name is expected, so the comparison can never succeed and the revenue allocation rule is applied on both reports. The display of the same screen uses the correct rule. | VERIFIED FACT | Material — one screen shows one number and posts another |
| `P10-F-02` | The deferral allocation rule is resolved from the **active** company, while the journal and account are resolved from the **document's** company. The auto-post cron makes the mismatch systematic rather than accidental. | VERIFIED FACT (source); runtime reproduction outstanding | Tolerance-zero candidate (company boundary) |
| `P10-F-03` | The grouped deferral generation reads its journal, account, rounding currency and lock-date check from the active company while its source population is multi-company selectable. | VERIFIED FACT (source); consequence is CONDITIONAL — see `P10_CONTRADICTION_REGISTER` `P10-C-02` | Tolerance-zero candidate (company boundary) |
| `P10-F-04` | Generated deferral lines carry no currency dimension at all. A foreign-currency service contract is recognised as a frozen company-currency amount. | VERIFIED FACT | Material |
| `P10-F-05` | A recognition entry whose scheduled period-end falls in a locked period is **silently re-dated**; the grouped path instead refuses. The same economic condition produces opposite behaviour on the two paths. | VERIFIED FACT | Material |
| `P10-F-06` | One economic fact produces two structurally different journal shapes depending on one company setting; switching the setting mid-life migrates nothing. | VERIFIED FACT | Material — direct violation of `ONE ECONOMIC FACT -> ONE RECOGNITION EVENT PATH` |
| `P10-F-07` | A deferral recognition event has no identity. Deduplication is therefore performed on a date-and-state proxy. | VERIFIED FACT | Design-governing |
| `P10-F-08` | No modification path exists for an in-flight deferral other than resetting the source document, and no catch-up mechanism exists on that mechanism. | See `P10_NEGATIVE_CLAIM_REGISTER` `NC-04` for the exact class and boundary | Material |
| `P10-F-09` | The accrual mechanism's audit link back to its source order is dead code: the collection it iterates is never populated. | VERIFIED FACT | Material (auditability) |
| `P10-F-11` | Two date fields carry three different meanings simultaneously: recognition schedule, subscription billing period, and statutory electronic-invoice period. | VERIFIED FACT | Material (semantic overload) |
| `P10-F-12` | The recognition **schedule** is monthly in every configuration; only the **amount computation** can be daily. "Daily recognition" is not available. | VERIFIED FACT | Material |
| `P10-F-15` | A recurring entry template does not carry recognition dates forward; a recurring deferred cost silently stops deferring after the first occurrence. | VERIFIED FACT | Material |

Findings `P10-F-10`, `P10-F-13`, `P10-F-14`, `P10-F-16` and all challenge-originated findings are recorded in `15_P10_AAS03_CHALLENGE.md` and consolidated in `16_P10_AAS_PLUS.md`.

## 7. The Design Question — Statement Only

Whether SMEsPlus should build **Option A** (separate domain engines) or **Option B** (one generalised Time-Based Recognition semantic kernel with domain-specific policies) is answered in `05_P10_SCHEDULE_ENGINE_SEMANTIC_RESEARCH.md` §7 and put to the Boss as a decision package in `16_P10_AAS_PLUS.md` §5. It is **not** answered here, and it is **not** answered from code-reuse convenience, per the process directive.

## 8. Reading Order

1. This document — the model.
2. `02` / `03` / `04` — the three traces (deferred revenue, deferred expense, accrual).
3. `05` — schedule engine semantics and the A/B analysis.
4. `06` / `07` / `08` / `09` — the four matrices.
5. `10` — cross-process ownership; `10b` — scope ownership.
6. `11`–`14` — registers, source links, manifest, revision log.
7. `15`–`17` — challenge, AAS+, PMO.
8. `18` — the handoff pack. **Read `18` §4 before relying on anything in `01`–`09`.**
