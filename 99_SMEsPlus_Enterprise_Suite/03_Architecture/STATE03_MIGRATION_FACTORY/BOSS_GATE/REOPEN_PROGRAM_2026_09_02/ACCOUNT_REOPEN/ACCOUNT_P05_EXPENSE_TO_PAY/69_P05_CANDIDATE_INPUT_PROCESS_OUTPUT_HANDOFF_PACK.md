# 69 — P05 CANDIDATE INPUT / PROCESS / OUTPUT / HANDOFF PACK

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05C-06` · **PHASE S CANDIDATE EVIDENCE ONLY**

> **NOT FINAL CONTRACTS.** Every item is a PHASE S candidate to be validated in PHASE B when all
> eleven sessions are reconciled. **AI EOS is NOT ACTIVE.**

Labels used: `FACT VERIFIED — P05` · `SUPPORTED INTERPRETATION — P05` · `CANDIDATE INPUT` ·
`CANDIDATE OUTPUT` · `CANDIDATE HANDOFF` · `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED` ·
`EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE`.

> **Mapping to the A–E negative-claim classes (added after AAS-03 Expert 2 — `RE-44`).** This file ran
> two vocabularies without stating how they relate, so a negative claim could sit in the first
> vocabulary and silently escape the second. They are **not** interchangeable:
>
> | Label above | What it asserts | Carries an A–E class letter? |
> |---|---|---|
> | `FACT VERIFIED — P05` | a **positive** claim, reproduced from source or data | no — A–E classes negatives only |
> | `SUPPORTED INTERPRETATION — P05` | a reading the evidence supports but does not compel | no |
> | `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED` | evidence was sought and not obtained | **yes — required** |
> | any statement of the form *"no X exists / is published / was observed"* | a **negative** claim | **yes — required, with POPULATION + PATTERN + PATH SET + UNIT** |
>
> Under this mapping four rows below were non-conformant. They are corrected in place.

---

## A. CANDIDATE INPUTS

> **Denominator reconciliation (added after AAS-03 Expert 1 challenge).** `CI-01`, `CI-02` and `CI-03`
> are **disjoint and exhaustive** over the deployed expense population: `own_account` **2** +
> `company_account` **357** + `petty_cash` **634** = **993**. They are three values of one typed
> funding field, so they are genuinely distinct classes — but an earlier draft mis-cited `CI-01`'s
> count as 993 (the total). Corrected above; recorded as `RE-31`.
>
> **Terminology — two different gates share the word "authorisation".** `CI-05` is *pre-spend*
> authorisation: a request to be allowed to incur a cost, with **no accounting effect**, deployed
> nowhere. The `authorised` state in §B is *claim* authorisation, which **does** emit the accounting
> fact. **They are unrelated in the evidence** and must not be conflated. Flagged by Expert 1.
>
> **The partition is clean on the typed field and NOT clean across the record (added after AAS-03
> Expert 2 — `RE-39`).** The three classes above partition the population **by the typed funding
> field**, which is what the counts measure. They do **not** partition it by the float-holder link:
>
> ```
> payment_mode = 'company_account', float-holder link SET     :  26
> payment_mode = 'company_account', float-holder link unset   : 331
> payment_mode = 'petty_cash',      float-holder link SET     : 634
> payment_mode = 'own_account',     float-holder link unset   :   2
> ```
>
> **26 rows are typed as business-funded while carrying a float-holder link.** The two fields that
> define `CI-02` and `CI-03` disagree on those rows. This is **not** a counting error — `CI-02` = 357
> and `CI-03` = 634 are both correct on their stated basis — but it means the funding route of those
> 26 records is **`C — NOT DECIDABLE` from the data alone**: a stale link left by a route change and a
> genuine second funding path are equally consistent with what is stored. Reported by Expert 2,
> reproduced by the author, and **not previously recorded by any file in this package.**
>
> **The reimbursement route has no observed claim (`RE-40`).** Both `own_account` rows are
> **unattached to any claim** (`sheet_id` null on 2 of 2). Every statement this package makes about
> reimbursement-route *claim* behaviour therefore rests on **source reading with zero observed
> instances** — it is not contradicted by the data, it is **untouched** by it.
>
> **Counts vs classes.** The **7 Candidate Inputs** here are *input events*. `68 CQ-P05-02`'s **3
> classes** are *classification outcomes* P05 can decide. Different axes: `CI-01` and `CI-03` are two
> input events that both resolve to the "employee claim" outcome. Neither count is wrong; the axes
> differ and are now stated.

### `CI-01` — Employee-incurred cost with evidence
| Field | Value |
|---|---|
| Business meaning | A person spent their own money on the business's behalf and seeks reimbursement |
| Producer / actor class | Employee (internal actor). **Producer internals not researched.** |
| Minimum data semantics | payer identity · cost description · amount · currency · date incurred · evidence artefact (receipt) · expense category |
| Required state / precondition | none — capture creates no obligation |
| Date semantics | *date incurred* is a business fact distinct from any accounting date |
| Amount / currency | amount in the currency spent; a company-currency equivalent is derived, and the derivation may use a **rate implied by two user-entered numbers** rather than a rate table |
| Scope | COMPANY |
| P05 validation | non-zero amount when attached to a claim; category resolvable to an expense account |
| Correction reference | pre-obligation — correction is free-form until claimed |
| Evidence | **FACT VERIFIED — P05** · **2 rows** on the v18 target (`payment_mode = own_account`). *Corrected — an earlier draft cited 993, which is the total across all three funding routes, not this class. `RE-31`.* |

### `CI-02` — Business-funded cost
| Field | Value |
|---|---|
| Business meaning | The business paid directly (card, account, cash) — no reimbursement is owed to a person |
| Producer / actor class | Employee or agent recording a business-funded spend |
| Minimum data semantics | as `CI-01`, plus **counterparty (vendor) identity** |
| Required state / precondition | a funding route must be nominated |
| Scope | COMPANY |
| P05 validation | **DEFECTIVE** — counterparty is optional while the settlement asserts a supplier relationship |
| Evidence | **FACT VERIFIED — P05** · **357 rows** (`payment_mode = company_account`) |

### `CI-03` — Cash-float-funded cost
| Field | Value |
|---|---|
| Business meaning | Spent from a named holder's cash float |
| Producer / actor class | Float holder |
| Minimum data semantics | as `CI-01`, plus **float-holder identity** |
| Required state / precondition | holder exists; a balance/limit control is asserted |
| Scope | **COMPANY** (derived: the float's balance is a company's cash position) |
| P05 validation | claim ≤ holder balance; single holder per claim |
| Evidence | **FACT VERIFIED — P05** · **634 rows (63.8%)** (`payment_mode = petty_cash`) — **the dominant input class** |

### `CI-04` — Vendor obligation for a service or consumable
| Field | Value |
|---|---|
| Business meaning | A supplier is owed money for a non-inventory good or service |
| Producer / actor class | Vendor / procurement. **P01 owns the procurement lifecycle — not researched.** |
| Minimum data semantics | vendor identity · amount · currency · document date · tax attributes |
| Scope | COMPANY |
| Evidence | **FACT VERIFIED — P05** · 37,055 vendor bills observed in the v16 population |

### `CI-05` — Pre-spend authorisation request
| Field | Value |
|---|---|
| Business meaning | Permission to incur a cost, before it is incurred |
| Producer / actor class | Requesting employee |
| Required state | approval by a named authoriser |
| Accounting effect | **NONE** — a request is not an obligation |
| Evidence | **FACT VERIFIED — P05** · module installed in **none** of eight registries → the input class exists in design, **not in any evidenced deployment** |

### `CI-06` — Funds advanced against a future cost
| Field | Value |
|---|---|
| Business meaning | Money given to a person before the cost exists |
| Correct P05 meaning | creates an **asset — a receivable from the holder** |
| Observed reference behaviour | recognises an **expense** at disbursement instead, by shipped default |
| Scope | COMPANY |
| Evidence | **FACT VERIFIED — P05** (source + shipped demo data) · installed in **none** of eight registries |

### `CI-07` — **NOT AN INPUT CLASS — a cross-cutting property.** Re-labelled after challenge.
| Field | Value |
|---|---|
| **Corrected classification** | **This is a PROPERTY that any of `CI-01`, `CI-02` or `CI-04` may carry — not a fourth input class.** Expert 1 established it does not conform to the input schema (no distinct producer, no distinct data semantics, no distinct scope). Retained under this ID for lineage; **excluded from the input count.** `RE-32`. |
| Business meaning | An obligation exists now, but the period it belongs to is not "now" |
| Producer / actor class | **same as its host input** — no distinct producer |
| P05 determination | P05 can establish **that an obligation exists**, its amount, counterparty, company and evidence |
| P05 limit | **P05 cannot decide the recognition profile.** |
| Label | `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE` → `CH-09` |
| Evidence | **SUPPORTED INTERPRETATION — P05** — no prepaid/accrual mechanism exists in the P05 surface (class B, three modules, declared pattern) |

---

## B. P05 PROCESS SEMANTIC CORE

**Business purpose.** Turn a cost incurred on the business's behalf into a correctly classified,
correctly attributed, correctly owed and settlement-ready obligation — and keep a provable trail from
the cost to the obligation.

**P05-owned truth**
1. That a cost occurred, evidenced, at a business date.
2. What kind of cost it is, at the granularity of an expense account.
3. **Who funded it first** — the axis the reference platform actually types.
4. **Who is owed**, and in what character.
5. Whether the obligation is authorised.
6. Whether it is ready to be settled.
7. The attribution the cost should carry.
8. The lineage from cost to obligation to correction.

**Trigger classes** — capture · grouping into a claim · submission · **authorisation** · posting ·
settlement · correction.

**State transitions (evidenced)**
`captured → claimed → submitted → authorised → recorded → settled`, with `refused` and `reset`
branches. The document state is **derived from** the accounting artefacts rather than driving them.

> **The model is incomplete against the reference, and that is the finding.** There is **no state or
> transition representing post-recording mutation**, yet amount, currency, date and category remain
> writable after recording with no propagation. The reference permits a change to a recorded
> obligation that the state model cannot express. Flagged by Expert 1; carried as `SR-02`.

**The three states that must not be conflated** — `CQ-P05-03`:
| State | Meaning | Reference behaviour |
|---|---|---|
| **Operational approval** | a manager permits the spend/claim | approval also **emits the ledger fact**, elevated |
| **Accounting recognition** | the obligation enters the books | occurs **at approval**, in draft |
| **Settlement readiness** | the obligation may be paid | a separate posting act |

> **`PSC-01` FACT VERIFIED — P05 — CORRECTED.** **Two of these three collapse into one transition**,
> executed by a user explicitly not required to hold accounting rights: operational approval also
> creates the accounting entry, in draft. **Settlement readiness does not collapse with them** — it is
> a separate method, on a different state gate, behind a different permission group, exactly as the
> table above already said. **SMEsPlus must separate the two that are collapsed.**
>
> *An earlier draft read "these three collapse into one transition", contradicting the table
> immediately above it. Caught by AAS-03 Expert 4 and re-verified by the author against the two
> methods in source. `RE-45`.*
>
> **The correction does not soften the finding — it relocates it.** The collapsed pair is the
> dangerous one: the ledger fact is emitted by the approval act itself, by an actor with no
> accounting right. The separate posting step is the part the reference gets right.

**Classification decisions.** Funding route (typed) · expense account (derived through a four-step
fallback, one step unreachable on the business-funded route) · counterparty character · tax attributes.

**Validations / controls.** Approver may not be the claimant (bypassed for administrators) ·
single funding route per claim · single float holder per claim · float balance ≥ claim ·
non-zero amount · company consistency of claim lines · evidence attachment **not required**.

**Accounting-relevant effect.** DR cost account(s) + DR recoverable tax; CR the obligation.
Attribution rides the **debit line only**.

> **Carve-out (added after Expert 1 flagged an unreconciled tension).** The line above describes the
> **observed reference behaviour on the evidenced population**. It is **not** a P05 assertion that an
> expense obligation should always be expensed rather than capitalised. **P05 has not determined, and
> is not competent to determine, whether any obligation should be capitalised** — that is P04's, and
> `CH-08` exists precisely because P05 cannot decide it. Where an obligation carries an asset
> relation, the posting rule above is **out of P05's authority** and the case diverts to `CH-08`.

**Analytic effect.** Carried on the cost line; **absent** from tax and obligation lines; **absent**
from the entire float and advance chain.

**Tax/WHT interface effect.** Purchase taxes on an expense line are forced **price-included**
regardless of configuration. WHT is not recognised at obligation creation; it materialises **at
settlement** as a deduction, and is reachable only on the reimbursement route.

**Payable effect.** One obligation per claim on the reimbursement route; **one per line** on the
business-funded route.

> **This asymmetry is a source-level reading that the deployment cannot test (added after AAS-03
> Expert 2 — `RE-41`).** Every claim on the target carries **exactly one line** — the
> lines-per-claim distribution is `{1: 979}` with no exceptions. Where claim and line are always 1:1,
> *"one per claim"* and *"one per line"* make **identical predictions**, so no observation on this
> deployment can distinguish them. The asymmetry is retained as a **`SUPPORTED INTERPRETATION`** from
> source, **downgraded from the `FACT VERIFIED` treatment it was receiving by association** with the
> verified counts around it. A deployment with multi-line claims would be required to test it.

**Correction / reversal semantics.** Three distinct cancels — **itemised at `74 §2`** (refuse a claim · cancel the accounting artefact · force-cancel from a non-accounting document) · reversal severs the claim↔entry link ·
post-recording mutation of amount/currency/date is possible without propagation · **no correction
event is published**.

**Terminal P05 states.** `settled` · `refused` · `reset-to-draft` (line-level lineage severed —
**narrowed, see below**) ·
`recorded-but-unsettled`.

---

## C. CANDIDATE OUTPUTS

| ID | Output | Meaning | Payload | Accounting meaning at the P05 boundary | Consumer class | Evidence |
|---|---|---|---|---|---|---|
| `CO-01` | **Settlement-ready payable** | An authorised obligation owed to an identified party | payable identity · amount · currency · counterparty · counterparty character · company · authorisation state · due metadata · correction lineage | a credit obligation exists | settlement (P06) | **FACT VERIFIED** |
| `CO-02` | **Cost recognition event** | A cost belongs to a company at a date | cost account · amount · currency · company · date · source-cost reference | a debit to expense | ledger (P08) | **FACT VERIFIED** |
| `CO-03` | **Attribution assertion** | Which cost object bears the cost | dimension value · amount portion · cost line reference · **company** | none by itself | P09 | **FACT VERIFIED** — debit line only. *`company` added after AAS-03 Expert 3: every other COMPANY-scoped output carried it; without it the consumer must re-open P05 records to learn the company.* |
| `CO-04` | **Withheld-tax event** | Tax withheld from a settlement | withholding basis · rate reference · **withheld amount + its currency basis** · counterparty · company · settlement reference · **income-type / form classification** · **certificate identity** · **branch identifier** | a reduction of cash paid vs obligation settled | P07 statutory, P06 settlement | **FACT VERIFIED** for the mechanics; four fields added after Expert 3 — see note |

> **`CH-04a` — `CO-04` payload gap, found by AAS-03 Expert 3 and accepted.** The original payload
> omitted four fields a statutory consumer structurally needs, **all already documented in this
> package's own evidence**, none requiring statutory research:
> **(a) income-type / form classification** — a real stored field whose value the package's own
> evidence shows can be silently reset by a compute side-effect, so a consumer re-opening the record
> is not safe; **(b) certificate identity** — 1,417 of 5,201 certificates in the examined population
> carry **no certificate number at all**, 1,414 of them completed, so the event cannot otherwise be
> cross-referenced to its document; **(c) branch identifier** — the two installed withholding
> subsystems store branch identity in **two different fields that can diverge**; **(d) currency
> basis** of the withheld amount, left ambiguous.
>
> **Whether P05 can freeze (a)–(c) at settlement time, or must declare that it cannot, is a question
> for P07 — not resolvable by P05 research.**
| `CO-05` | **Float movement** | A named float was drawn down or replenished | holder · float account · amount · company · direction | a credit/debit to a company cash position | treasury / P06 | **SUPPORTED INTERPRETATION** — no live-posted instance observed. *Negative re-stated with its boundary after Expert 2 (`RE-43`):* class **B — searched, not observed**; POPULATION = accounting entries on `idemo18_uat`; PATTERN = an entry whose counterpart is a named float account; UNIT = one accounting entry. **Not** a claim that the reference cannot produce one. |
| `CO-06` | **Correction event** | A previously published P05 truth has changed | original reference · what changed · new values · reason · timestamp · actor | reversal or amendment | all consumers | **UNRESOLVED — SPECIFIC EVIDENCE REQUIRED**: **no such event is published by the reference.** Candidate output derived from the defect, not from observed behaviour. *Boundary and class added after Expert 2 (`RE-43`) — this was a domain-wide negative carrying neither:* class **A within the P05 modules read** (POPULATION = the P05 modules named in `13` and `81 §3`; PATTERN = any published event carrying a correction reference; UNIT = one event definition). **Outside those modules it is class `C — NOT SEARCHED`**, and `81 §2` shows that region is 47.1% of the deployment. |

---

## D. CANDIDATE HANDOFFS

| ID | Producer → Consumer | Meaning | Minimum payload | Precondition | Scope | Correction relation | Evidence | PHASE B must validate |
|---|---|---|---|---|---|---|---|---|
| `CH-01` | **P05 → P08** | cost recognition | `CO-02` | authorised | COMPANY | must carry reversal linkage | FACT VERIFIED | that P08 accepts P05's event identity and forbids silent mutation |
| `CH-02` | **P05 → P09** | attribution | `CO-03` **incl. company** | cost line exists | COMPANY | must survive reversal | FACT VERIFIED | that attribution on one leg is sufficient, or that P09 requires full-entry balance |
| `CH-03` | **P05 → P06** | settlement-ready payable | `CO-01` | authorised, unsettled | COMPANY | correction must be able to withdraw it | FACT VERIFIED | that P06 can settle without re-deriving P05 truth |
| `CH-04` | **P05 → P07** | withheld-tax event + attributes | `CO-04` | settlement occurring | COMPANY (mapping) / PLATFORM (rate reference) | correction must reverse the withholding | FACT VERIFIED (mechanics) / statutory **D** | which system of record owns the statutory return |
| `CH-05` | **P05 → payroll settlement route** | an employee obligation settled through a payslip instead of a payment | payable identity · employee · amount · company | authorised | COMPANY | must not permit double settlement | **SUPPORTED INTERPRETATION** | that exactly one settlement route consumes a given obligation |
| `CH-06` | **P05 → P02** | a cost marked re-invoiceable | cost reference · customer document reference · amount · **company** | cost recorded | COMPANY | correction must propagate | **SUPPORTED INTERPRETATION** | ownership of the re-invoice decision |
| `CH-07` | **P08 → P05** *(inbound)* | period/lock state governing whether P05 may record | period open/closed per company and date | — | COMPANY | — | FACT VERIFIED (consumed) | that P05 reads a lock rather than computing around it |
| `CH-08` | **P05 ↔ P04** | an expense obligation may relate to an asset | obligation reference · counterparty · amount · company · **the fact that an asset relation is asserted** | obligation exists | COMPANY | **a P05 correction must withdraw the asserted relation; what P04 does with that is not P05's to know** | **UNRESOLVED — SPECIFIC EVIDENCE REQUIRED**. Only the *declaration* is evidenced (`DP-01`). **P04 not researched, not waited for.** | who decides capitalisation, and when |
| `CH-09` | **P05 → P10** | an obligation whose recognition profile P05 cannot decide | obligation reference · amount · currency · counterparty · company · service period **if stated on the source document** · evidence | obligation exists and is authorised | COMPANY | correction must reach the schedule | **CANDIDATE HANDOFF** — derived from P05's own limit, **not** from P10 research | whether P05's payload is sufficient for P10 to build a schedule |

---

## E. ORPHAN CANDIDATES

**Not to be fixed by researching the neighbouring domain. These are PHASE B validation targets.**

| ID | Orphan | Why |
|---|---|---|
| `ORPH-01` | **`CO-06` correction event — output with no producer** | P05 *should* publish a correction event; the reference publishes none. Every consumer therefore has a correction blind spot. **Highest-value orphan.** |
| `ORPH-01a` | **Withholding correction — no mechanism at all, not merely no event** | Added after Expert 3, who established that `ORPH-01`'s framing **understates** the withholding case. For a completed withholding certificate there is **no correction or cancellation mechanism of any kind** across the six withholding modules — only deletion, itself blocked by a restrict constraint. This is not "the event is not published"; it is **"the correction cannot be performed."** Class **A** within those six modules. |
| `ORPH-02` | **`CI-05` pre-spend authorisation — input with no deployed producer** | The class exists in design and in source; installed in **none** of eight registries. Either an unused capability or a real gap. *Class letter added after Expert 2 (`RE-43`):* class **A** — POPULATION = the eight `ir_module_module` registries enumerated in `44`; PATTERN = the module `name`; UNIT = one registry row. This is a strong negative because the registry is the authority on installation, not a proxy for it. |
| `ORPH-03` | **`CI-06` advance — input whose correct output has no home** | If an advance creates a receivable, the receivable's owner is undetermined: P05 creates it, but who monitors and clears it? *Class letter added after Expert 2 (`RE-43`):* the ownership gap is class **E — NOT AN EVIDENCE QUESTION**. No search settles it; it is a design decision reserved to PHASE B. Recording it as an unmet evidence need would have been wrong. |
| `ORPH-04` | **`CH-05` / `CH-03` — two settlement consumers, no arbiter** | An employee obligation can be settled by payment **or** by payroll. Nothing in P05 prevents both. Duplicate-settlement risk with **ambiguous ownership**. |

### Added after AAS-03 Expert 2

> **`RE-42` — the severed-lineage claim is narrowed, not withdrawn.** This package framed the break at
> the **line** grain: the line-level link from accounting line back to the cost record is null
> **table-wide** (0 non-null rows anywhere), which is correct and reproduced twice. But the
> **claim-level** key on the accounting entry **survives**:
>
> ```
> accounting entries carrying a claim reference : 712 of 712
> claims carrying an accounting entry           : 712 of 979
> amount reconciles claim -> entry              : 711 of 712  (99.86%)
> ```
>
> Because every claim has exactly one line, that surviving key **fully reconstructs** the
> cost→obligation link for the 712 claims that have an entry at all. **The corrected statement:**
> line-level lineage is severed unconditionally; claim-level lineage survives and is recoverable
> **on this deployment's one-line-per-claim shape**, and would not be on a multi-line claim.
> For the remaining **267 claims with no accounting entry**, no key recovers anything, because there
> is nothing to recover to — that is `PC-01`, and it is untouched by this narrowing.
>
> **`DUP-07` — duplicate-candidate rows, `C — NOT DECIDABLE`.** Expert 2 found, and the author
> reproduced, **11 groups covering 23 rows** identical on (description, employee, amount, date).
> The descriptions are routine recurring narratives (fuel, tolls, parts transport) that would
> legitimately repeat. **Calling them duplicates and calling them legitimate repeats are both
> overclaims** on the fields available. Disposition **`C — NOT DECIDABLE FROM THIS EVIDENCE`**;
> distinguishing evidence would be a receipt or document number, a quantity, or a product line.
> This is **not** covered by `DUP-03`..`DUP-06`, which are all *"no cross-document detection control
> exists"* findings — a different claim from *"identical rows are present."*

## F. COUNTS

| | |
|---|---|
| Candidate Inputs | **6** (`CI-01`..`CI-06`). `CI-07` **re-classified as a cross-cutting property, not an input class** (`RE-32`) — retained for lineage, excluded from the count. |
| Candidate Outputs | **6** (`CO-01`..`CO-06`) |
| Candidate Handoffs | **9** (`CH-01`..`CH-09`) — 7 outbound, 1 inbound, 1 bidirectional-unresolved |
| Orphan / ambiguous | **5** (`ORPH-01`, `ORPH-01a`, `ORPH-02`, `ORPH-03`, `ORPH-04`) |
