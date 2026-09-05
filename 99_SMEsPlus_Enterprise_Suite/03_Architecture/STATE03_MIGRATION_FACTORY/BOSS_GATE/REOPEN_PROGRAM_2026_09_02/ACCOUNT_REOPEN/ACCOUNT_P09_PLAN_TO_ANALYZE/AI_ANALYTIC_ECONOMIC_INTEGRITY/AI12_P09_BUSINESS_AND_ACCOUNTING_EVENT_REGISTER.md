# AI12 — P09_BUSINESS_EVENT_REGISTER and P09_ACCOUNTING_EVENT_REGISTER

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room. Two registers in one file because the continuation's central finding is precisely that **the reference pattern does not distinguish them**, and separating the registers is the first step in stating the requirement.

---

## PART A — BUSINESS EVENT REGISTER

A **business event** is a real-world act. It is not an accounting entry and not a management record.

| ID | Business event | Carries an economic effect to attribute? | Produces a financial event? | Produces a management record? |
|---|---|---|---|---|
| BE-01 | a supplier delivers goods or services | yes | yes | yes, correctly |
| BE-02 | a customer is invoiced | yes (revenue) | yes | yes, correctly |
| BE-03 | an employee incurs an expense | yes | yes | yes, correctly |
| BE-04 | **an asset consumes a period of its useful life** | **yes** | yes | **yes, twice, netting to zero** |
| BE-05 | a prepayment or deferred revenue is recognised into a period | yes | yes | **yes, twice, netting to zero** |
| BE-06 | an employee spends time on a task | yes | **no** | yes, with no financial counterpart |
| BE-07 | a machine runs for a period | yes | **no** | yes, up to three records |
| BE-08 | inventory is consumed or produced | yes | yes | conditionally |
| BE-09 | a payment is received or made | **no new cost** — it settles an existing one | yes | normally none |
| BE-10 | **a period boundary is crossed** (cut-off, accrual) | **no new cost** — it re-times an existing one | yes | **yes, twice, netting to zero** |
| BE-11 | **tax becomes exigible on payment** (cash basis) | **no new cost** — it re-times a tax already recognised | yes | **yes, twice, netting to zero on every surface** |
| BE-12 | a balance is reclassified between accounts | **no** | yes | yes, netting to zero — **arguably correct** |
| BE-13 | a discount is granted | yes (negative) | yes | yes, correctly |

**The register makes the diagnosis visible.** BE-04 and BE-05 carry a real economic effect and attribute nothing. BE-10 and BE-11 carry **no new** economic effect, so attributing nothing is defensible — but they attribute nothing *by accident*, through the same broken arithmetic, not by design. BE-12 attributes nothing and that is correct.

**The system cannot tell these three situations apart, because it has no representation of "does this event carry an economic effect to attribute".** That is `AI-M-01`, and this register is its evidence.

## PART B — ACCOUNTING EVENT REGISTER

An **accounting event** is the identified thing the ledger records. **The reference pattern has no such object** — this is P09's standing blocking dependency `DEP-P09-01`, inherited from the Core Ledger study and unchanged by this continuation.

The register below is therefore a **specification of what SMEsPlus must build**, not a description of what exists.

| Property | Requirement | Why the continuation makes it non-negotiable |
|---|---|---|
| **identity** | immutable, unique, assigned at recognition | management records currently reference a **row**, so no query can ask "what did this event attribute?" |
| **economic-effect flag** | declares whether the event carries an effect to attribute | without it, net zero is ambiguous between correct and defective (BE-10 vs BE-04) |
| **attribution rows** | names which of its rows carry the economic effect | this is the whole fix: the event knows, the row cannot |
| **attribution** | held at **event** level, not row level | `AI-S-01` — a row-level carrier cannot express a rule whose subject is the event |
| **completeness check** | the event's management records shall sum to the event's declared attribution | would have caught all five symmetric mechanisms at creation |
| **provenance class** | derived-from-posted-ledger / derived-from-unposted / operational-only / allocation-result | base package `B-02`, unchanged |
| **reversal** | a reversal is a new event referencing the original | not a deletion of records |

**AI-AE-01.** The completeness check is the single control that would have prevented every defect in `AI07`. It is cheap, it is checkable at creation, and it requires only that the event know its own intended attribution. **P09 recommends it as the highest-value single requirement produced by this continuation.**

## PART C — THE MAPPING THAT DOES NOT EXIST

| Layer | Reference pattern | Consequence |
|---|---|---|
| business event → accounting event | **no object** | cannot ask what a business act cost |
| accounting event → journal rows | implicit in one entry | acceptable |
| journal row → management record | **1:N, and the only link that exists** | attribution is a property of rows |
| management record → business event | **no path** | cannot ask what a cost centre's charge was *for* |

**The management record can name a dimension and an amount, and can never name the reason.**

## CHECKPOINT

**CP-AI12(a) — EVENT REGISTERS ISSUED.** The business register makes the three-way distinction the system lacks; the accounting register specifies what must be built. Auto-continue.
