# P10 — SCHEDULE ENGINE SEMANTIC RESEARCH

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Question under research: **should SMEsPlus build separate domain engines (Option A) or one generalised Time-Based Recognition semantic kernel with domain-specific policies (Option B)?**

The process directive forbids deciding this on code-reuse convenience. The six admissible criteria are: business semantics, accounting semantics, auditability, correction behaviour, period-close behaviour, SaaS boundaries. This document works through all six and then states what the evidence does and does not settle.

---

## 1. Enumeration Method (declared, reproducible)

| Element | Declaration |
|---------|-------------|
| POPULATION | Every code path in the declared reference root that creates or schedules an accounting entry whose date is derived from a period or schedule rather than from a business document date |
| PATTERN | Five independent selecting expressions, run separately (`E1` deferral field carriers, `E2` accrual wizard, `E3` depreciation board, `E4` recurring-entry chain, `E5` amortisation / spreading vocabulary) |
| PATH SET | Both module trees of reference root `RR-1` — the active tree and the archived tree — each enumerated, not assumed |
| UNIT | One module directory |
| SCRIPT | `LAYER2_P10_EVIDENCE/p10_scripts/p10_enum_02_mechanisms.sh`, shipped inside the evidence package and re-runnable unmodified |

**Declared false-negative modes of this enumeration:**
- `E1` misses any mechanism that spreads an amount without using the two deferral date fields.
- `E2`/`E3`/`E4` are identifier-anchored and miss any re-implementation under different names.
- `E5` is vocabulary-anchored and produced a large false-positive population (localisation chart-of-account names containing amortisation vocabulary), which was filtered by inspection, not by pattern. `E5` therefore has an **unmeasured** false-negative rate.
- The whole enumeration is bounded to reference root `RR-1`. It says nothing about `RR-2`, `RR-5` or `RR-6`.

Accordingly the population statement is a **floor, not a total**.

> **CORRECTION `P10-R-01`.** The author's declared pattern returned five. Independent challenge, using a different pattern (journal-entry creation call sites, then classification by hand), returned **seven**, and then demonstrated that its own pattern had missed an eighth because that mechanism materialises entries by *copying* an existing entry rather than creating one. Two enumerations, two different patterns, two different answers, and the second one disproved itself in the same report. The defensible statement is therefore: **at least eight mechanisms exist; no exact total is supportable with the evidence gathered.** See `13_P10_NEGATIVE_CLAIM_REGISTER.md` `NC-01`, class `D`.

## 2. What the Mechanisms Agree On

Only three things:
1. Every one of them ultimately produces an ordinary journal entry with a date.
2. Every one of them uses the shared posting layer, and therefore inherits its soft-posting and its **silent lock re-dating** (`E-P10-035`, `E-P10-036`).
3. Every one of them is company-currency-centric to some degree.

That is the entire shared surface. There is no shared schedule abstraction, no shared allocation function, no shared period grid, no shared event identity, and no shared vocabulary.

## 3. What They Disagree On — the structural comparison

| Axis | `M1` Deferral | `M2` Accrual | `M3` Depreciation | `M4` Loan | `M5` Recurring |
|------|---------------|--------------|-------------------|-----------|----------------|
| Persistent schedule object | none | none | asset + board | loan + schedule lines | none |
| Schedule is recomputable | n/a | n/a | yes, destructively | yes, on re-confirm | n/a |
| Back-link entry → schedule element | none | none (dead code) | to the asset, not the period | **to the individual schedule line** | to the origin entry |
| Entry-type marker | none | none | implicit | explicit | implicit |
| Period grid | calendar months, fixed | single point | months or years, configurable | contractual dates | fixed interval |
| Day-count convention | 30/360, actual, or full-month | n/a | 30/360 or actual calendar | contractual | n/a |
| Residue absorption | forced into last period | n/a | end-of-life adjustment | contractual | n/a |
| Generation trigger | source posting, or report button | manual wizard | confirmation / recompute | confirmation | prior posting |
| In-flight modification | none | n/a | pause, resume, revalue, dispose | reset and re-confirm | change the template |
| Catch-up on change | **path-dependent** — see correction `P10-R-02` | n/a | yes, via a stub entry cut at the modification date | full re-derivation | n/a |
| Lock-date behaviour | silent re-date (path A) / refuse (path B) | silent re-date | explicit guards | posts only up to today | silent re-date |
| Foreign currency | cannot express | single-order only | asset currency | company currency only | inherited |

Reading this table as a designer: **`M4` is the only one of those compared that would survive an audit of its own lineage**, because it is the only one where a posted entry can be traced to the exact schedule element that justified it. `M3` is second. `M1` and `M2` have no lineage at all.

## 4. Criterion by Criterion

### 4.1 Business semantics — **points to A**

The four substantive mechanisms answer four different business questions:
- depreciation: *how much of a capitalised asset's service potential was consumed?*
- deferral: *how much of an amount I have already billed have I now earned?*
- accrual: *how much have I earned or incurred that I have not yet billed or been billed?*
- loan amortisation: *what part of a contractual obligation falls due, and what part of it is now short-term?*

Only the second and third are inverses of each other. The first involves an asset with a residual value and a disposal event; the fourth involves a counterparty and a maturity structure. A kernel that models all four has to model "an amount, a window, and a rule" — which is true of all four but *sufficient* for none of them.

### 4.2 Accounting semantics — **points to A for the objects, B for the allocation**

The four have genuinely different accounting anatomies: a contra-asset accumulation; a liability or asset unwinding; a reversing estimate; a liability reclassification. Those are not the same posting patterns and should not be forced into one.

But all four answer one identical sub-question: *given a base, a window, a grid and a convention, what amount belongs to this period?* That sub-question has exactly one correct answer per convention, and the reference product answers it in three separate places with three separate implementations of the same 30/360 arithmetic (`E-P10-005`, `E-P10-031`, and the loan's contractual dates). **The allocation is common; the object is not.**

### 4.3 Auditability — **points strongly to B**

Auditability is where the fragmented approach measurably failed in the reference product. Two of the mechanisms compared have no lineage from posted entry to justifying schedule element, one of those two has lineage code that never executes (`P10-F-09`), and the deferral's deduplication is a proxy on date and state because there is no event to deduplicate on (`P10-F-07`).

A shared kernel that owns exactly one thing — **the recognition event with an identity** — fixes all three, and it fixes them for mechanisms that do not otherwise resemble each other at all. This is the strongest single argument in the entire analysis.

### 4.3a Correction `P10-R-02` — the deferral catch-up claim, corrected

Two independent challengers reached **opposite conclusions** on whether a deferral catch-up exists. The contradiction was adjudicated on evidence, not on reviewer count, and both were partly right:

- On the **validation** path there is no catch-up. Class `A`, bounded to the two deferral source files.
- On the **grouped** path there is one, and it is structural rather than incidental: each run recomputes the deferral position **cumulatively from an unbounded earliest date** and books the whole remaining position at period end with a next-day reversal (`E-P10-046`). A skipped month is therefore absorbed by the next run automatically.

The consequence for the design question is the opposite of the author's first reading: the grouped path is the **more** correction-resilient of the two, and the validation path — the product default — is the fragile one. `P10-F-08` is re-scoped accordingly.

Two further corrections from the same challenge, both accepted:
- the asset catch-up is produced by a **stub entry cut at the modification date**, not by the board recompute, which is purely prospective (`E-P10-048`);
- the asset model in this reference root is named for **asset *and revenue recognition* together**, and still carries live code commentary about inverting amounts for deferred revenue (`E-P10-049`). The two domains were **one engine** in this product line. That evidence is recorded in full in §5a because it bears directly on the Boss's standing warning.

### 4.4 Correction behaviour — **points strongly to B**

Correction is the hardest part of time-based recognition and the part the reference product handles least consistently: full support with catch-up on one mechanism, destructive rebuild on another, nothing at all on a third, and "reset the source document" on a fourth.

Correction semantics reduce, in all four domains, to the same three primitives: *which posted events stand*, *which future events are re-derived*, and *what catch-up delta lands in the current period*. Those primitives do not vary by domain. Implementing them four times has already produced four different answers in the reference product, and there is no reason to expect a different outcome in SMEsPlus.

### 4.5 Period-close behaviour — **points strongly to B**

Every mechanism inherits the same defect — the silent re-dating of a locked-period entry (`P10-F-05`) — because they all delegate to one shared posting layer while none of them owns the distinction between *the period an amount belongs to* and *the date an entry is posted on*.

A kernel that separates `TR-5` from `TR-6` makes this a solved problem once: the recognition event keeps its period; the posting act may be re-dated; the difference becomes a reportable, reconcilable quantity instead of an invisible one. Under Option A this separation must be built, correctly, once per domain engine.

### 4.6 SaaS boundaries — **points to B, with a condition**

Under the corrected scope constitution, the two scope defects found (`P10-F-02`, `P10-F-03`) are both of the form *the executing scope supplied a value the owning scope must supply*. That failure is not domain-specific — it is a property of how a mechanism resolves its policy. A kernel with a single, explicit scope-resolution rule (`policy is resolved from the company that owns the financial effect; ambiguity denies`) removes an entire defect class from all domains at once.

The condition: the kernel must resolve scope, **not** assume tenant-and-company everywhere. Under `REV2-CORR1` the day-count convention *definitions* are PLATFORM reference data, the standardised policy is a TENANT default, and the binding value is COMPANY. A kernel that hard-codes COMPANY for all three would be over-constrained and would be wrong in the other direction.

## 5a. The Evidence Against the Author's Own Framing

The Boss's standing warning is *never assume depreciation and deferred recognition share an implementation merely because both use schedules*. The author framed this session around verifying difference. Independent challenge produced evidence pointing the other way and it must be recorded here, not buried:

1. The asset model in the declared reference root is described as **"Asset/Revenue Recognition"** — one model, two domains, in its own self-description (`E-P10-049`).
2. Its board computation still contains live commentary instructing that amounts be inverted **for deferred revenues** (`E-P10-049`).

Read correctly this does not overturn the difference findings in §3, which are about the *present* implementations and are individually verified. It establishes something narrower and more useful: **the two domains were once served by one engine in this very product line, and the separation is an artefact of product history rather than a demonstrated semantic necessity.** Any argument of the form "the reference product kept them apart, therefore they are semantically apart" is contradicted by the reference product's own naming.

## 5. What the Reference Product's Own Choice Proves — and Does Not

It had at least eight chances to build a kernel and built none. Read honestly, this proves:
- that the domains were *delivered* at different times by different teams under different edition boundaries (`E-P10-044`), which is an organisational fact, not a semantic one;
- that the cost of not having a kernel is observable and has been measured in this session: multiple re-implementations of the same day arithmetic, at least four mutually inconsistent rounding-residue policies, one dead audit link, one absent event identity, two scope defects, one unreachable cancellation branch in the shared teardown, and one silent period shift inherited by every mechanism at once.

It does not prove that a kernel is impossible, and it does not prove that a kernel is right. The reference product is **evidence, not authority** — the canonical acquisition standard says so explicitly.

## 6. The Boss's Explicit Warning, Answered

> *Never assume Asset Depreciation and Deferred Recognition share identical implementation merely because both use schedules.*

They do not share an implementation, and this session verified that rather than assuming it: they differ in day-convention implementation, period-grid configurability, modification support, catch-up, lock-date handling, currency capability and event identity — thirteen axes in §3, of which they agree on two.

But §5a shows the reverse assumption is equally forbidden. The reference product's asset model is **named for both domains** and still carries deferred-revenue commentary. So:

- *they share an implementation because both use schedules* — **refuted**, on thirteen axes;
- *they are semantically distinct because this product separates them* — **also refuted**, by the product's own naming and residual code.

Both convenient inferences fail. What survives is the narrow, evidenced statement in §7: the **allocation, identity, correction and scope-resolution semantics are common; the objects, lifecycles and posting patterns are not.**

## 7. The Recommended Shape — `RECOMMENDATION`, for Boss decision

Neither A nor B as stated. The evidence supports a third shape:

> **Option B-minus: one shared *semantic kernel* — recognition event identity, period grid, allocation convention library, correction algebra, and scope resolution — and separate *domain engines* that own their objects, their posting patterns, their lifecycles and their business rules.**

What the kernel owns (one implementation, all domains):
1. `TR-5` the recognition event, with identity, period, amount, status and version;
2. the period grid, derived from the owning company's fiscal calendar;
3. the allocation convention library (30/360, actual/actual, full-month, contractual), as PLATFORM reference definitions;
4. the correction algebra: which events stand, which are re-derived, what catch-up delta arises;
5. scope resolution: policy is resolved from the company that owns the financial effect; ambiguity denies;
6. the separation of `TR-5` from `TR-6`, so that a re-dated posting never silently moves a recognition period.

What the domain engines own (separately, per domain):
1. the domain object and its lifecycle (asset, deferral, accrual estimate, loan);
2. the recognition base and how it is measured or re-measured;
3. the posting pattern and account derivation;
4. the domain's own business rules, statutory treatment and reporting.

Why this is not "shared code because it is convenient": every element in the kernel list is an item this session found **broken or absent in at least two of the mechanisms compared**, and every element in the domain list is an item this session found **genuinely different across the mechanisms**. The split is drawn along the evidence, not along the code.

`AAS+` records a dissent and a condition on this recommendation in `16_P10_AAS_PLUS.md` §4. **This section is a recommendation to the Boss and is not a decision.**

## 8. What Further Research Can and Cannot Resolve

**Can resolve** (with runtime/database access): whether `P10-F-02` and `P10-F-03` manifest as predicted; the true incidence of asymmetric direction settings; whether a shared chart of accounts across companies exists in the target tenants.

**Cannot resolve by research**: whether SMEsPlus should present prepaid expense separately from deferred charge; whether the tenant may standardise an allocation convention across its companies; whether daily recognition must be supported. These are normative business/architectural choices and are put to the Boss under Stage J of the canonical acquisition flow.
