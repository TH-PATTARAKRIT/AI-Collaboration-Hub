# P09_CONTRADICTION_REGISTER

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

Three registers: contradictions **inside the reference pattern**; contradictions **between session participants**; and items **held for want of evidence**. Nothing in this file is resolved by assertion.

---

## A. CONTRADICTIONS INSIDE THE REFERENCE PATTERN

| ID | The contradiction | Status |
|---|---|---|
| **CN-01** | The dimension structure is presented as configuration and behaves as **schema**. Creating a dimension performs data-definition work; deleting one drops a column with cascade and destroys history. Configuration that cannot be undone is not configuration. | Structural. Not resolvable within the pattern. |
| **CN-02** | A management record is required to carry a company and is strictly scoped, while the **axis it belongs to carries no company field at all** and no tenant concept. The value is scoped; the dimension it lives in is not. | Structural. |
| **CN-03** | The platform enforces a scope check on exactly **one** axis — the one that happens to be a conventional relational field — and structurally cannot enforce it on the others or on the allocation payload. **A control that applies to one of N dimensions is not a control; it is a coincidence of representation.** | Confirmed by challenge. |
| **CN-04** | The allocation must total 100 % where an axis is mandatory, **but only when the caller opts in by execution context**. A rule whose enforcement is elective is not a rule. | Confirmed. |
| **CN-05** | The user interface colours an incomplete allocation red and **saves it anyway**. The signal and the behaviour contradict each other. | Confirmed by challenge. |
| **CN-06** | A posted entry is protected against change by a lock date, a tax lock, a reconciliation guard and a hash chain — and its **management allocation is in none of those lists**. The entry is immutable in its financial dimension and freely mutable in its management dimension, with no audit either way. | Confirmed by challenge. |
| **CN-07** | A financial report presents management records **stamped with the literal posting state "posted"**, including records that were never posted and some that can never be posted. The report asserts a state the data does not have. | Confirmed. |
| **CN-08** | A reallocation rule selects amounts **by dimension** and writes entries carrying **no dimension at all**. The mechanism destroys the trace of its own cause. | Confirmed. |
| **CN-09** | A dimension filter on a reallocation matches on **presence** and moves the **whole balance**. The filter's semantics and the transfer's semantics disagree. | Confirmed by challenge; re-characterised as misallocation, not duplication. |
| **CN-10** | A blank axis column on a budget line means **"any value"** in the budget's matching join and **"not applicable"** to the person who left it blank. | Confirmed by challenge. |
| **CN-11** | Two reporting surfaces answer "which records belong to this cost object" by **structurally different rules** — one strict equality, one wildcard-tolerant join — so a cost object's own profitability total and its budget consumption are not computed over the same rows. | Confirmed by challenge. |
| **CN-12** | Budget consumption is computed on **three different time bases** and presented as three comparable columns. | Confirmed. |
| **CN-13** | A budget's confirmed amount is locked by a view attribute whose condition is a state that an **unguarded action can reset from any state**. The lock is keyed on the thing that unlocks it. | Confirmed by challenge. |
| **CN-14** | Access rules reserve activation of a reallocation to a senior role by restricting **write**, while a **create** call can set the same state directly. The access table and the reachable behaviour disagree. | Confirmed by challenge. |
| **CN-15** | A permission decision about which dimensions a user may see is evaluated **before** a cache whose key contains no user component, while the platform's own documentation in the same file says group-restricted content must be filtered **after** that cache. | Confirmed by challenge. |
| **CN-16** | One business fact — an hour of machine time — produces **up to three** management records from three modules, each carrying the full amount, none marked as a perspective on the same fact. | Confirmed. |
| **CN-17** | The dimension balance converts at **today's** rate into the **reader's** company currency, and is therefore not a property of the data. Two users, or two days, produce two answers. | Confirmed. |
| **CN-18** | The upgrade path aborts on a state that the module's own runtime code treats as normal and handles gracefully. | Confirmed by challenge. |
| **CN-19** | Inter-company mirroring drops the allocation silently and lets the **receiving** company's default outrank the **sending** document, while the module's own test asserts the empty outcome as correct. | Confirmed by challenge. |

| **CN-20** | An allocation is copied to **both** legs of a balanced pair and the analytic amount is the negated signed balance — so the mechanism that exists to attribute a cost is arithmetically guaranteed to attribute **nothing**. The system faithfully records two management facts whose sum is zero. | Confirmed by P09 on an incoming peer finding. |
| **CN-21** | When the source object carries **no** allocation the key is *deliberately omitted* so that each row may find its own — which for a balanced pair means the two legs can be attributed to **different** cost objects, producing a residue that corresponds to no economic event. The fallback designed to add information can subtract correctness. | Mechanism confirmed; outcome configuration-dependent. |

| **CN-22** | The mechanism that exists to attribute cost has **no concept of which row carries the cost**. Eligibility is decided by whichever code built the row values, so the same faithful mechanism gives the right answer for a vendor bill and zero for a depreciation. | Confirmed by the continuation. |
| **CN-23** | **Five** mechanisms allocate both legs of a balanced pair, three of them in core accounting — yet the product's own management consumers all filter to profit-and-loss accounts, which is only coherent if balance-sheet rows were never meant to be allocated. **The writers and the readers disagree about what the ledger is.** | Confirmed by the continuation. |
| **CN-24** | For the cash-basis pair the two legs share **one account**, so the account-bucketing that rescues every other case cannot apply. **The one mechanism no surface can see is in core accounting, on a path used by every organisation on cash-basis tax.** | Confirmed by the continuation. |
| **CN-25** | The accrued-orders counterpart is weighted by **tax-inclusive** totals and applied against **tax-exclusive** balances, so the cancellation is approximate and leaves a residue. **A clean zero is recognisable as wrong; a small residue looks like a real cost.** | Confirmed by the continuation. |
| **CN-26** | A net of zero is the **correct** answer for a reclassification transfer and the **wrong** answer for a depreciation, and the system represents both identically. Correctness and defect are indistinguishable in the data. | Confirmed by the continuation. |

## B. CONTRADICTIONS BETWEEN SESSION PARTICIPANTS — PRESERVED, NOT RESOLVED

Per the constitution, AAS+ preserves disagreement. These are live.

| ID | Position A | Position B | Disposition |
|---|---|---|---|
| **DIS-01** | The research team held that the row-multiplication in the report view is an exposure (CH-CAND-05). | X3 enumerated every caller and **disproved the exposure**, while finding the mechanism stronger than stated. | **B prevails on the exposure claim.** A carries forward only as a latent-hazard note in `P09_EDGE_CASE_MATRIX` EC-44. Not merged into agreement. |
| **DIS-02** | The research team's wording implied the privileged-axis cache could be indefinitely stale. | X2 showed it is invalidated on every write path that matters, bounded to one request. | **B prevails.** The team's separate scope claim is unaffected and stands. Both are recorded; the superseded wording is corrected in place. |
| **DIS-03** | The research team characterised CH-CAND-04 as "transferred as if it were total". | X1 established it is a **misallocation** in which the unallocated fraction is not picked up anywhere either. | **B prevails on characterisation.** A is not wrong, it is imprecise, and imprecision at this severity is treated as a defect. |
| **DIS-04** | X1 could not verify the tenant custom-root findings and declared class C. | X3, which had the paths, verified them and added a statutory finding. | **Not a disagreement about fact — a disagreement about coverage.** Both records retained; the class-C declaration is retained *as written*, because retro-fitting it would destroy the evidence that the brief was incomplete. |
| **DIS-05** | X1 flagged a count discrepancy against the evidence base and declined to call it an error. | The research team reconciled it as two correct measurements of different units. | **No party was wrong.** Retained in full because the *unit* defect it exposed is the project's own standing lesson. |
| **DIS-06** | X4 could not locate the access rows for the budget objects and declared class B, routing it as a dependency. | No other participant searched for them. | **Open.** Recorded as `DEP-P09-04`. Not closed by anyone's assumption. |
| **DIS-07** | The research team's original scope position asserted tenant **and** company context for every analytic object. | The scope-aware constitution correction supersedes that wording. | **The correction prevails.** The superseded position is retained verbatim in `P09_REVISION_LOG` §R1 so that the over-constraint is legible rather than erased. |
| **DIS-08** | P09 published row E19 stating that a posted depreciation produces management records from the asset's own allocation. | P04 established that those records **net to zero**. | **B prevails on effect.** A was true of the records and false of the effect. P09 re-verified all three steps from primary source before accepting. Corrected in place, logged at `14` §R9. **A peer process corrected a published P09 finding; that is recorded, not smoothed over.** |
| **DIS-09** | P04 reports that its finding contradicts a premise underpinning a standing costing veto recorded by a prior Asset package. | The prior Asset package holds the original premise. | **P09 does not adjudicate.** Two parallel evidence tracks disagreeing is a Boss-level reconciliation, not a P09 determination. Recorded as a pointer in `E01` Part D and nothing more. |

## C. HELD — EVIDENCE REQUIRED

| ID | Item | Class | Route |
|---|---|---|---|
| HOLD-TH-01 | whether Thai statutory practice requires cost-centre or department segregation in management accounts, tax reporting or withholding-tax certificates | not evidenced in code | **Accounting-Tax track.** No statutory claim is made anywhere in this package. |
| HOLD-TH-02 | whether the tenant department-dimension extension is intended to satisfy such a practice | design question | Accounting-Tax track |
| HOLD-TH-03 | a **statutory** Thai capability is present in two deployment copies and absent from the third | D | Accounting-Tax track, elevated severity |
| HOLD-SC-01 | scope of the work centre as a cost object | scope evidence required | PD-01 → P03 / P11 |
| HOLD-SC-02 | whether the deployed tenant custom set contains the department dimension at all | D | PD-06 → P11 |
| HOLD-EQ-01 | how non-asset equipment cost should be tracked — **no reference precedent exists** | design decision | Boss determination; see `P09_COST_OBJECT_MODEL` CO-03 |
| HOLD-BC-01 | whether SMEsPlus requires commitment accounting visible in the ledger | design decision | Boss determination; PD-03 → P01 |
| HOLD-AS-01 | whether the prior Asset package's costing-veto premise survives the P04 finding | cross-track reconciliation | **Boss.** P09 does not adjudicate between parallel evidence tracks. **Unchanged by the continuation, which strengthens the underlying finding without settling the track disagreement** |
| HOLD-AI-01 | whether the analytic ledger is intended as a cost-attribution ledger or a balanced subledger | design intent, not evidenced in source either way | **DESIGN DECISION REQUIRED AT FINAL GATE.** The most load-bearing open item of the continuation |

## D. NOT SEARCHED — NEVER TO BE RESTATED AS ABSENCE

Carried forward verbatim from the evidence base and the matrices. Each is class **C** or **D**, and per the negative-claim standard **none may be converted to class A** by restatement, citation, or elapsed time.

| ID | Item | Class |
|---|---|---|
| NS-01 | budget control implemented outside the two budget modules | C |
| NS-02 | alternative reporting aggregation for the seven non-groupable allocation carriers | C |
| NS-03 | producers reached through a variable-held model name | C |
| NS-04 | a compensating upgrade script in other modules' migration directories | C |
| NS-05 | whether the integer-versus-JSON comparison in the report filter matches correctly | C |
| NS-06 | tenant custom modules extending the report layer | C |
| NS-07 | whether any deployed tenant view strips the node the runtime patch depends on | C |
| NS-08 | the pooled-connection blast radius of the report's shadow object | C |
| NS-09 | statutory export formats outside the three export-family name patterns | C |
| NS-10 | which of the three tenant custom copies is deployed | **D** |
| NS-11 | whether an ordinary accountant role inherits write on the ledger row | C |
| ~~NS-12~~ | ~~whether any other event type allocates both legs symmetrically~~ | **CLOSED** by the continuation sweep — five mechanisms found. Replaced by `SW-U-01`, `SW-U-02`, `SW-U-04` |
| NS-13 | the full set of programmatic posting paths bypassing mandatory-axis validation | **B from P09's position** — enumerated by P04, not re-enumerated by P09 |
| SW-U-01 | allocation write sites using record assignment rather than a values dictionary — the continuation sweep's own declared false-negative mode | **C** |
| SW-U-02 | off-balance-sheet account rows | **C** |
| SW-U-04 | tenant custom modules — the continuation sweep covered the reference root only | **C** |

## E. TERMINAL STATE

**26 INTERNAL CONTRADICTIONS RECORDED · 9 PARTICIPANT DISAGREEMENTS PRESERVED UNRESOLVED · 9 ITEMS HELD · 15 UNSEARCHED ITEMS DECLARED (ONE CLOSED BY THE CONTINUATION). NO GATE MOVED.**
