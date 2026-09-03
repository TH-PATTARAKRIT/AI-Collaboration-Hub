# 11 — DEEP LEVEL 5: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** The lifecycle table is honest: nine of twenty stages absent, all
nine operational. And §3.2's observation that **there is no "fully depreciated"
state to react to** is a genuine functional discovery that the Boss's hypothesis
had not accounted for.

**Missing.** The re-entry case. §3.2 raises it and stops. What *should* happen when
a fully depreciated machine, running on internal usage cost, receives a capital
improvement and becomes depreciable again? The design must answer it, because the
system permits it at any time, and the answer determines whether internal usage
pauses, continues alongside, or is superseded.

**Risky.** §3.1's sequencing recommendation is correct and it is also unwelcome
news. It says: before any of the interesting costing work can be trusted, somebody
has to fix a manual dropdown and make people fill it in on 280 records. That is
unglamorous data work, and projects routinely skip it and then build sophisticated
allocation on an association that is 40% populated.

**Challenge.** I challenge §2's framing of Management Truth as simply "does not
exist". It does not exist **in the reference ERP**. It exists in every
manufacturing business I have worked with, as spreadsheets. Describing it as an
absence undersells what SMEsPlus is doing and, more practically, it hides the fact
that the requirement already has an existing implementation to be compared against
— the customer's own spreadsheet. That is available evidence and nobody has asked
for it.

**Evidence required next.** The customer's current method for recovering machine
cost into product cost, whatever form it takes.

**Assumed too early.** That "the machine keeps producing after full depreciation"
is the normal case worth designing around. It may be. But nobody has counted how
many of the 27 closed and 217 running assets are actually production machines
rather than air-conditioners and office furniture — and the runtime sample is
visibly full of air-conditioners.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** §4 points 2 and 3 — inherit immutability, treat value as a
derivation — are the correct data conclusions and they are properly grounded in
Levels 2 and 3.

**Missing.** §4 point 1 says "one physical machine, one identity" and does not say
where that identity lives. That is *the* data decision of the whole programme. If
identity lives on the financial object, operations inherits accounting's lifecycle.
If it lives on the operational object, then disposal, revaluation and the parent/
child tree all have to be re-expressed. Level 5 has stated the requirement and
skipped the decision.

**Risky.** §3.3's simplification. The Boss's formula reduces algebraically to
*residual ÷ original lifetime days*. That is clean, and it means the internal usage
rate is **constant for the whole post-depreciation period, forever**, regardless of
how long the machine actually runs. A machine that runs twenty years past full
depreciation accrues twenty years of usage cost at the same daily rate. Whether
that is intended is a design question — but as a data model it means an unbounded,
monotonically increasing balance with no terminating condition. Somebody must own
that.

**Challenge.** I challenge §3.2's row "cumulative internal usage may exceed
residual" being carried as a `DESIGN CANDIDATE` without a stated bound. An
unbounded accumulator in a ledger, even an off-balance one, is a design defect
until a bound or a periodic reset is specified. I am not challenging the business
intent; I am challenging shipping it without a terminating rule.

**Evidence required next.** The decision on identity ownership (§4 point 1), which
is a Boss/architecture decision and not a research item.

**Assumed too early.** That off-balance accounts behave like normal accounts for
reporting, aggregation and period close. Nothing in this session has examined how
the reference product treats that account type in trial balance, closing or
reporting. It is asserted to be "separate" and never verified.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** §3.5's finding is the strongest localisation result of the level:
the boundary the Boss asked to be **maintained by policy** is, on the asset side,
**already enforced by the product's own field domains**. That is a precedent worth
citing in the SMEsPlus design.

**Missing.** The Thai question I raised at Level 4 is still unanswered and it is
now load-bearing. §3.1 proposes absorbing depreciation into inventory value. Under
Thai practice, inventory cost and the tax treatment of depreciation interact, and
the statutory depreciation deduction is claimed on the **asset**, not on the units
produced. Whether absorbing depreciation into inventory creates a timing difference
that must be tracked for tax is **not addressed anywhere in this package**. It
should be.

**Risky.** §3.4. Residual is protected while running and **absorbed into gain or
loss on disposal**. The Boss's design treats residual as a durable reference base
for internal usage. On disposal that base disappears into a single gain/loss figure
and the internal usage ledger has nothing left to reference. Nobody has designed
the disposal path for the management ledger.

**Challenge.** I challenge §2's claim that Truth C is "complete downstream of the
rate". It is complete **for real-time-valued products only**. `08` §6 link 5 is
conditional. For a periodic-valued product the machine cost reaches the unit price
and never reaches the ledger. Calling that "complete" will mislead the design.

**Evidence required next.** Thai treatment of depreciation absorbed into inventory
(`UNR-03`), and the valuation configuration actually in use for the products in
scope.

**Assumed too early.** That Off-Balance is a Thai-admissible presentation. It is an
account classification in one product. Thai statutory financial statements have a
prescribed form. Whether accounts of that type are simply excluded, or must be
disclosed, is unestablished, and the whole management-ledger design rests on it.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** §3.1's component table is the right way to present a design
hypothesis: each component separately classified, with the unbuilt ones named. It
does not let a coherent story hide three missing pieces.

**Missing.** Nothing in Level 5 addresses **volume**. Deriving a per-machine daily
rate and allocating it across operations means generating cost records at a
granularity the reference system never contemplated. The asset engine posts two
lines per asset per month. Per-machine, per-operation allocation is a different
order of magnitude and nobody has sized it.

**Risky.** `08` §6 link 2 — the hourly rate is **snapshotted onto the work order at
creation**. A monthly-derived rate therefore does not retroactively apply to work
orders already open when the rate is computed. For a plant with work orders
spanning month ends, that is a systematic leakage, and §3.1 does not mention it.
I raised it at Level 4 and it has not been carried into Level 5.

**Challenge.** I challenge §4 point 4, "the day convention is an explicit decision,
per company". Per **company** may be the wrong grain. The evidence shows the
convention is a field on **each asset**. A population can legitimately be mixed,
and on the UAT it may already be. Specifying the decision at company level assumes
a uniformity that has not been verified — see `UNR-02`.

**Evidence required next.** The distribution of computation modes across the 280
assets. That single query answers both `UNR-02` and my challenge here.

**Assumed too early.** That the reference system's absence of Management Truth
means it is safe to build one anywhere we like. The absence is a design decision by
a mature product. It may reflect a real difficulty — such as the reconciliation and
audit burden of a second ledger — rather than an oversight.

---

## AAS+ CONSOLIDATION — LEVEL 5

### Agreements

1. The system holds two complete truths and one half-truth, with no bridges. All four.
2. Nine of twenty lifecycle stages are absent, all on the operational side. All four.
3. There is **no "fully depreciated" state**; the trigger for internal usage mode
   must be constructed. All four. **New this session.**
4. Residual is protected while running and **absorbed into gain/loss on disposal**.
   All four.
5. The Boss's instruction to derive the internal rate from a daily rather than
   monthly basis is **correct and now proven necessary**. All four.
6. The Boss's insistence on separating cost pool from allocation driver is
   **vindicated by the evidence** — the reference system's conflation of the two is
   exactly why it cannot answer "which machine". All four.

### Disagreements — preserved

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D5-01` | Whether unbounded cumulative internal usage is acceptable | Expert 2: not without a stated bound or reset. Expert 1: the business intent is clear and a bound is a policy choice, not a defect. **Unresolved — escalated to the Boss as `UNR-B3`** |
| `D5-02` | Where machine identity should live | Expert 2 says the decision is missing; no expert proposed an answer. **Open architecture decision, not a research finding** |
| `D5-03` | Whether "Truth C is complete downstream of the rate" | Expert 3: only for real-time-valued products. **Resolved in Expert 3's favour — `10` §2 to be read with `08` §6 link 5's condition** |
| `D5-04` | Grain of the day-convention decision | Expert 4: per asset, not per company. **Resolved in Expert 4's favour pending `UNR-02`** |

### Items the experts raised that the Boss's hypotheses do not yet cover

| # | Item | Raised by |
|---|------|-----------|
| 1 | Re-entry: a fully depreciated asset receiving a capital improvement | Expert 1 |
| 2 | A terminating rule or bound for cumulative internal usage | Expert 2 |
| 3 | Disposal path for the management ledger once residual is absorbed | Expert 3 |
| 4 | Rate snapshotting on work orders spanning a month end | Expert 4 |
| 5 | Volume/granularity of per-machine per-operation cost records | Expert 4 |
| 6 | Unabsorbed depreciation — where it goes when usage is below capacity | AAS+, from §3.1 |

**All six are recorded in `41` and surfaced in the Boss pack.** None of them
invalidates the Boss's design; each is a hole in it that will otherwise be found
during build.

### Consolidated position at the end of Level 5

The Boss's design programme is **coherent, evidence-compatible and original**.
Nothing in five levels of forensic work contradicts its direction, and two of its
distinctive insistences — daily rather than monthly basis, and cost pool separate
from allocation driver — are **positively vindicated** by primary source evidence.

The design is also **less complete than it appears**, in six specific places listed
above, and it rests on two components that must be repaired first: an
Asset↔Equipment association that is manual, unconstrained and partly inert, and an
Operation model with no equipment dimension at all.

### Gate to Level 6

Open. Level 6 must now try to break all of this.
