# 19 — P02 ORDER-TO-CASH → CORE ACCOUNTING RECONCILIATION HANDOFF PACK

**LAYER 1 — CLEAN ROOM.** This is the only file in the P02 package cleared for downstream semantic
transfer. It contains no reference-system model name, field name, module name, method name, file path or
source citation. Every statement below is a **business and accounting requirement for SMEsPlus**, derived
from benchmark learning and expressed in SMEsPlus terms.

Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001` · Process P02 Order-to-Cash
Scope model per correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`.

**Status: RECOMMENDATION ONLY. No gate is declared satisfied. No implementation is authorised.**

---

## 1. What Order-to-Cash Actually Is, Stated Once

Order-to-Cash converts a **commercial promise** into **cash**, and it does so through exactly four
financial facts:

1. **Goods or services left the business** — an economic outflow.
2. **The customer became obliged to pay** — revenue and a receivable.
3. **The cost of what left became attributable to that sale** — cost of sales.
4. **The obligation was discharged** — settlement.

Everything else in the process is scheduling, documentation or presentation.

**The single most important thing learned in this research:**

> **Facts 1 and 3 are about the same physical unit, and facts 2 and 3 are recognised on the same
> document. If the system lets the quantity behind fact 2 and the quantity behind fact 1 diverge, then
> fact 3 becomes an estimate — and once it is an estimate, gross margin is unauditable.**

Benchmark systems allow that divergence. SMEsPlus must not.

---

## 2. The Governing Requirement — The Obligation Ledger

**Requirement P02-R-01 (structural, highest priority).**

Between the outflow and the billing there must be a **single ledger of economic obligations**, in which:

- the **outflow** writes one row per unit that physically left, carrying the value at which it was
  relieved from inventory, at the moment it left, in the scope that owns it;
- the **billing** consumes rows from that ledger, never from a quantity field;
- the **cost of sales** is taken from the value on the rows consumed, never re-derived;
- each row is **relieved exactly once and attributed exactly once**, enforced structurally;
- an unconsumed row is a **visible, ageable position**, not an account balance.

This single structure resolves, at the root, six otherwise separate defects observed in benchmark
behaviour: two competing delivery quantities; two competing cost derivations; an unowned clearing
position; a double-valuation path; outflows that produce no financial record; and billing policy leaking
into cost recognition.

**Everything in §3 and §4 either follows from P02-R-01 or is independent of it.**

---

## 3. Requirements Placed On Core Accounting

### 3.1 Positions that must exist as first-class objects

| # | Position | Why P02 needs it |
|---|---|---|
| **P02-R-02** | **Goods delivered, not yet billed** | The outflow has happened; the obligation has not been billed. Must be a **controlled subledger with per-obligation rows and mandatory ageing**, not a general-ledger account. |
| **P02-R-03** | **Billed, not yet delivered** | Where billing precedes performance, the credit is **not** revenue. Must be a contract liability. |
| **P02-R-04** | **Customer advances / deposits** | A deposit received before performance is a **liability by construction**. It must not be resolvable to a revenue account under any configuration. |
| **P02-R-05** | **Cash received, not yet confirmed at bank** | A receipt and a bank confirmation are two events. The intermediate position must be structural and non-optional. |
| **P02-R-06** | **Credit issued, not yet refunded** | A credit note that has not been paid out is an obligation, not a net balance inside receivables. |
| **P02-R-07** | **Unapplied customer cash** | An overpayment must have a named, aged home. It must not sit invisibly inside the receivable control account while the invoice reads as settled. |
| **P02-R-08** | **Tax not yet due** | Where tax becomes due on receipt rather than on invoice, the not-yet-due portion needs its own position. |
| **P02-R-09** | **Impairment / expected credit loss** | Doubtful debt must be a first-class accounting event with a restricted account role, an ageing trigger and a defined reversal on recovery — never a write-off to an operator-chosen account. |

**Eight of these nine positions are absent, unowned, or optional in the benchmark.** Each absence
produced an observed class of silently-wrong ledger states.

**And the absence is uniform, which is a cleaner statement than the one this pack originally carried.**
In the benchmark's Thai chart of accounts — enumerated completely — there is **no position for value in
transit in either direction**. An account exists whose name suggests the purchase-side role, and it is
connected to nothing. **Every position Order-to-Cash needs in order to be auditable between its own events
is a position that chart does not have** — and so is the purchase-side equivalent. This is not a
localisation quirk to work around; it is the reason the process has nowhere to put value in transit, and
it is why P02-R-02 and P02-R-05 are stated as structural requirements rather than as configuration.

*(An earlier draft of this pack claimed the purchase side was supported and the sales side was not. That
claim was refuted by independent challenge and is withdrawn.)*

### 3.2 Date discipline

**Requirement P02-R-10.** Every accounting event must carry **two dates**:

- the **occurrence date** — when the business fact happened;
- the **recognition date** — which reporting period it belongs to.

They are normally equal. Where they differ, the difference must be an **explicit, attributed, recorded
act** with a reason — never a silent side effect of a period lock, a document type, or a system clock.

**Requirement P02-R-11.** One declared date rule per accounting event class, and the rule must be
readable from the event itself. Benchmark behaviour used **six** different date rules across the
accounting events of a single business process, none of them stated to the user.

**Requirement P02-R-12.** The date on which revenue is recognised is a **required human assertion**. A
blank date must never be completed from the system clock, and the rule must be identical on the sales and
purchase sides.

### 3.3 Period close

**Requirement P02-R-13.** A closed period must **bar at creation**, not redirect at posting. A benchmark
lock date silently moves an entry into a later open period and posts it; that is a redirect, not a close.

**Requirement P02-R-14.** The close must cover **settlement and matching state**, not only journal
entries. Benchmark behaviour permits the record of *what was matched against what* to be destroyed and
rebuilt across a closed period, so the settlement history of a closed period is mutable while its entries
are not.

**Requirement P02-R-15.** The close must cover the **inventory valuation side**. In the benchmark the
valuation subsystem has no concept of a period lock at all, and its records carry no accounting date of
their own — so a valuation entry relocated by a lock leaves the valuation report and the ledger
disagreeing, with nothing detecting it.

**Requirement P02-R-16.** There must be **no context-level or technical bypass** of a period control. Any
exception must be scoped, time-bounded, attributed to a named person, reasoned, and audited — and no
exception may reach the irreversible close.

**Requirement P02-R-17.** A period may not close while the *goods delivered, not yet billed* position
(P02-R-02) holds an unexplained residual.

### 3.4 Money and currency

**Requirement P02-R-18.** A missing exchange rate must be a **hard stop**. Never a neighbouring date's
rate, never a rate from a later date, never one-to-one. Benchmark behaviour silently substitutes the
earliest rate of any date, and failing that, unity — with no log, no warning and no error.

**Requirement P02-R-19.** Every converted amount must record, on the entry itself, the **rate used, its
source, and its effective date**.

**Requirement P02-R-20.** A receivable in a foreign currency has **two residuals**. Both must be zero
before it is settled, and every ageing, dunning and exposure view must read both.

### 3.5 Account derivation

**Requirement P02-R-21.** Account derivation must be a **total, deterministic function** of the
transaction's own attributes and its scope. It must be replayable and explainable on the entry. Benchmark
behaviour includes selecting an account by **how frequently it was used before** for that counterparty,
and falling back to *the first available control account* when none is configured.

**Requirement P02-R-22.** A missing control account is a **hard stop**, never a silent selection.

---

## 4. Requirements P02 Places On Itself

| # | Requirement |
|---|---|
| **P02-R-23** | **Billing policy and cost-recognition policy must be declared together** as one named, versioned, effective-dated recognition profile held at the appropriate scope. They must never be independent settings on unrelated objects that are never validated against one another. |
| **P02-R-24** | **Cost-of-sales quantity comes from the obligation ledger, never from an invoice line.** |
| **P02-R-25** | **Physical completion and valuation are one atomic act.** A completed outflow with no valuation record must be structurally unrepresentable. |
| **P02-R-26** | **A physical return and a commercial credit are two events with an explicit recorded relationship** — linked, deliberately unlinked with a reason, or pending. Neither silent coupling nor silent independence is acceptable. |
| **P02-R-27** | **The cost basis of a reversal is the cost of the specific units being reversed**, taken from the obligation ledger. Never a re-derivation, never a current master-data price, and never a rule that changes because a different date was chosen. |
| **P02-R-28** | **One definition of "this movement is a return"**, used by valuation and accounting alike. |
| **P02-R-29** | **The duplicate-revenue control sits on the obligation, not on the order document.** Every revenue-recognising document consumes from the same ledger, whatever route created it. |
| **P02-R-30** | **Consolidated billing produces a first-class document with structural links to every source obligation.** Provenance is never free text, and consolidation is never a silent default. |
| **P02-R-31** | **Cost-of-sales generation is idempotent by construction** — a uniqueness constraint on the pair (accounting document line, cost effect). Never protection by the ordering of a posting routine. |
| **P02-R-32** | **Over-delivery has one behaviour**, independent of billing policy. |
| **P02-R-33** | **Every business event that can influence a financial fact emits an immutable event record** carrying event type, occurrence time, asserting actor, asserted scope, values asserted, and what it consumed. "The current value of a field" is not an event. |
| **P02-R-34** | **The intent to credit is decided visibly at the moment of the return**, never by a hidden default. |

---

## 5. Scope Determinations Handed Over

Per the three-scope model — PLATFORM / TENANT / COMPANY; missing required scope denies; unprovable
ownership denies.

**Settled:**

| # | Determination |
|---|---|
| SD-01 | **Every financial effect in Order-to-Cash is COMPANY-scoped.** Nine financial events, all company-owned. No P02 event creates a financial effect at tenant or platform scope. |
| SD-02 | **The commercial layer above the financial one is TENANT-scoped** — customer identity, product identity, commercial terms. A tenant with several companies has one customer, not several. |
| SD-03 | **Reporting that spans companies is TENANT-scoped and read-only.** It may aggregate company facts; it may not create one. |
| SD-04 | **A period close is COMPANY-scoped.** One company may close while another is open. |
| SD-05 | **There is no PLATFORM-scoped object in the Order-to-Cash transaction path.** Platform scope appears only in reference data the path consults — units, currency codes, jurisdiction identities. |
| SD-06 | **Ownership, availability and financial scope are three distinct things** and must remain distinguishable. Owned stock can be unavailable, and stock in a company's records can be outside its financial scope. |

**Held — routed to Core Accounting Reconciliation, not decided here:**

| # | Question | P02's position |
|---|---|---|
| SC-01 | Is an exchange rate platform reference data, tenant-owned policy, or company accounting truth? | Likely a **shape**, not a choice: the rate *source* and the rate *as applied and frozen on an entry* are different objects at different scopes. Intersects the existing rate-ownership ruling. |
| SC-02 | Is the account structure a tenant-owned standard that companies instantiate, or a per-company object? | Not decided. P02's requirement is scope-independent: **the nine positions of §3.1 must exist.** |
| SC-03 | May an intercompany pair cross a tenant boundary? | **No, by default.** Unrelated independent companies are separate tenants by default; two companies that trade and are not in the same tenant are ordinary third parties. An intercompany mirror is a **tenant-scoped operation with two company-scoped effects**, must run under a scoped service identity, and must produce a **reconciled** pair — equal untaxed amount, declared treatment of any tax divergence, one agreed accounting date, one agreed rate. |

**One scope lesson that must not be lost:**

> **Configuration that BELONGS TO a company must never be RESOLVED FROM the acting context.**
> In the benchmark, valuation configuration is company-specific but is read from whichever company the
> operator is currently acting as. One live consequence: a clearing-account reconciliation silently does
> nothing when the two differ. Scope is ownership, not ambient state.

---

## 6. Decisions Requiring Boss Ruling

| # | Decision |
|---|---|
| **B-01** | **When is cost of sales recognised?** At outflow, at billing, or under a declared policy? And is that timing a tenant-configurable versioned policy, or a platform invariant? It may not be an unversioned flag whose meaning depends on an unrelated account configuration. Three outcomes are reachable in the benchmark, and in **one of them cost of sales is never recognised at all** — which is the default shape under the Thai chart. |
| **B-02** | **Is revenue recognised on billing or on performance?** This is a recognition-policy decision with statutory consequences and cannot be inherited from a benchmark default. |

---

## 7. Statutory Questions Routed To The Accounting-Tax Track

All eight are **held**. This package has no authority to state Thai law and does not.

| # | Question |
|---|---|
| S-01 | Which date is the VAT tax point, and may a tax document bearing one date be declared in a later period? |
| S-02 | Is VAT on services due on receipt, and is an accrual-only configuration compliant? |
| S-03 | May the accounting-system invoice serve as the statutory tax invoice, and what are its mandatory particulars and branch identification? |
| S-04 | Do the reports produced correspond to the statutory filing forms? |
| S-05 | Are the withholding rates, the income-type mapping, and the remittance condition correct and current? |
| S-06 | Must a withholding certificate be issued and retained, and how is tax withheld **by customers** evidenced and claimed? |
| S-07 | Does Thai law require gap-less, immutable, sequentially numbered tax invoices? |
| S-08 | Is the standard rate current, and must other rates be reported separately? |

**Three structural findings that are not statutory but must reach the tax track:**

**First, and most serious.** The benchmark localisation's **statutory support export writes the accounting
date into a column headed "Invoice Date"**. The accounting date is the one that posting can silently
relocate. So the schedule a company hands to its accountant in support of its VAT return prints, under a
heading that says *Invoice Date*, a date that is not the invoice date and may fall in a different month,
quarter or fiscal year. Whether that is a filing defect or a labelling defect is question S-01/S-04; that
it is a defect is a code fact, not a legal opinion.

**Second.** Four of the six VAT taxes in that chart carry **no tax group**, and the report counts tax
exclusively from the standard-rate group — so a zero-rated or exempt sale is grouped nowhere.

**Third.** in the benchmark
localisation, the taxes representing **withholding suffered on the company's own receipts** carry no
report tags, while the taxes representing withholding the company collects and remits all do. Because the
statutory reports select rows by tag, **customer-side withholding appears on no report at all.** That is
an asymmetry inside the localisation itself, not a question of law.

---

## 8. Reliance Statement

This package is **research output**. It is not a design, not a specification, and not an authorisation.

- Nothing here has been implemented, tested or proven at runtime.
- **A live deployment was examined, and it confirmed the central mechanism finding by direct count:** in a
  Thai company carrying 447,384 journal lines, the invoice-side cost mechanism has **never executed**. That
  deployment recognises cost at delivery instead, with **no position connecting cost to the revenue it
  belongs to** — so a shipment billed in a later period puts the two in different periods permanently, and
  **nothing in the system can detect it**. That exposure is live, not theoretical.
- **Runtime execution was still not performed.** Whether cost recognition can be generated twice remains
  open and cannot be settled by reading data.
- An earlier draft of this pack stated that **no** database evidence existed. That was wrong and untested,
  and it is withdrawn.
- Six process areas were **not searched** and could contribute further Order-to-Cash events:
  subscriptions, point of sale, e-commerce, rental, projects, and manufacturing.
- **Eight business situations have no analysis in this work and are open gaps, not settled questions:**
  drop-shipping; **customer credit control**, which is a gate *before* the first step of this process and is
  absent from it entirely; period-end revaluation of open foreign-currency receivables; bill-and-hold;
  outbound consignment; warranty and return provisions arising at the point of sale; freight and delivery
  charges with their tax treatment; and serial- or lot-identified cost of sales.
- An independent adversarial review of this work produced **twenty findings that changed it**, including
  **two that refuted conclusions it had stated as verified fact**. It examined roughly **half** the
  underlying evidence; the other half has been reviewed once, not twice.
- The benchmark is a **learning source only**. Nothing here authorises copying its code, schema, data
  structures, workflow implementation or interface.
- Two consecutive clean independent passes have **not** occurred. This is the first Order-to-Cash package
  and the first independent challenge against it.

**Terminal state: READY FOR CORE ACCOUNTING RECONCILIATION.**
