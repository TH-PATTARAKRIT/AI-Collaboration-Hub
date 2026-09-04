# 17 — P02 AAS+ SYNTHESIS

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

AAS+ preserves disagreements and contradictions. It does **not** resolve them by averaging, and it does
not present consensus where none exists.

## 1. What The Package Actually Establishes

Reduced to its irreducible core, after 77 evidence citations, four evidence tracks and one independent
challenge:

> **Order-to-Cash in the reference is not one process with one ledger. It is three subsystems — a
> commercial one, a physical one and a financial one — each internally coherent, connected to the others
> by mutable scalar fields rather than by events, and reconciled after the fact by balance matching in
> accounts that nobody owns.**

Every finding in this package is a consequence of that sentence:

| Consequence | Where |
|---|---|
| Two answers to *how much left* | `05` §4, `05` §3a |
| Two answers to *how much was billed* | `01` S6 |
| Two independent valuations of the same physical unit | `03` §1 |
| Six different date rules across 13 accounting events | `06` §2 |
| Four different cost bases for one credit note | `08` §4 |
| Ten ledger states that are balanced and wrong, none detected | `07` §3 |
| Five subledgers, two of which have no owner | `07` §4 |
| A period lock that redirects rather than bars | `11` §6 |

## 2. The Design Synthesis — One Architecture, Not A List Of Patches

Thirty-one design candidates were raised across the package. They are **not** thirty-one changes. They
collapse into **five structural decisions**, and the rest follow.

### D-I — The Obligation Ledger

*Resolves: DC-02-02, DC-03-02, DC-08-02, DC-10-01, and P02-R-01/24/29. **Does NOT resolve** DC-03-01 (a producer defect), the chart gap in `07` §5, or the service case — see `10` §2a.*

Between the physical outflow and the billing there is **one ledger of economic obligations**. The outflow
writes rows; the billing consumes rows; cost of sales is the value on the rows consumed. Each row is
relieved once and attributed once, structurally. An unconsumed row is a **visible, ageable position**.

This decision removes, at the root, the **second cost derivation** and everything that follows from it —
the standard-price fallback, the double-valuation class and the invoice-quantity coupling into cost, which
the package had counted as three findings and which are one.

**It does not remove**, and must be accompanied by: `D-VI` below (atomic completion, for the
unpicked-completion hole), the chart requirement in `07` §5 (for the unowned clearing position), and an
explicit statement of what an obligation row contains for a **service**, which no design candidate in this
package currently supplies. `10` §2a records the corrected count.

**It remains the highest-value single change in the package** — but on one defect properly counted, not
six.

### D-II — Events, Not Fields

*Resolves: DC-05-01, DC-08-06, DC-09-05, and P02-R-33.*

Every business fact that can influence a financial fact emits an **immutable event record** — type,
occurrence time, asserting actor, asserted scope, values asserted, what it consumed. Matching and
unmatching are events. A quantity assertion is an event. "The current value of a field" is not.

Eleven of the twenty-four business events in `05` currently have no identity at all. This decision gives
all twenty-four one.

### D-III — Two Dates On Every Accounting Event

*Resolves: DC-06-01, DC-11-01 in part, and P02-R-10/11/12.*

**Occurrence date** — when the business fact happened. **Recognition date** — which period it is reported
in. Normally equal. Where they differ, the difference is an explicit, attributed, reasoned act. Never a
side effect of a lock, a document type, or a system clock.

Six date rules become one rule per event class, and the rule is readable from the event.

### D-IV — Scope Is Ownership, Not Ambient State

*Resolves: `20` SF-01 … SF-08, and P02-R-23 in part.*

Scope is stamped once at the origin of a business transaction and carried. It is never re-derived from the
execution environment at each hop, and configuration that **belongs to** a scope is never **resolved
from** the acting context. Missing scope denies; unprovable ownership denies; absent scope is never a
wildcard.

This is the decision the reference most clearly does not make, and the one whose absence produced the most
subtle defect in the package — a clearing-account reconciliation that silently does nothing when the
acting company and the document's company differ.

### D-VI — Physical Completion And Valuation Are One Act

*Resolves: DC-03-01, and P02-R-25.*

Separated out from D-I after the independent challenge showed it is a **producer** defect that no
downstream ledger can absorb: the valuation gate runs before any ledger could be written, so a ledger
inherits the gate exactly. A completed outflow without a valuation record must be structurally
unrepresentable.

The challenge also established that the reachable case is the **mixed picking**, and that the field a
reviewer would naturally query — the movement-level marker — **conceals** it (`03` §2). Any control built
here must be built on the movement-**line** marker.

### D-V — Close Means Closed

*Resolves: DC-11-01, and P02-R-13/14/15/16/17.*

A closed period **bars at creation**, covers **matching state** as well as entries, covers the
**valuation side**, has **no technical bypass**, and cannot be left while the goods-delivered-not-billed
position holds an unexplained residual.

### What Does Not Collapse

Four decisions are genuinely independent of the five above and must be taken on their own merits:

| # | Decision | Why it stands alone |
|---|---|---|
| 1 | **A missing exchange rate is a hard stop** (P02-R-18) | A data-integrity rule, not a structural one. |
| 2 | **A customer advance is a contract liability by construction** (P02-R-04) | A recognition-policy rule. |
| 3 | **Impairment is a first-class event** (P02-R-09) | A new accounting event, not a restructuring of existing ones. |
| 4 | **Account derivation is a total deterministic function** (P02-R-21/22) | A rule about how a single field is computed. |

## 3. Preserved Disagreements

AAS+ records these **unresolved**. None is settled by this package.

### DIS-01 — Where cost-of-sales timing belongs

| Position | Argument |
|---|---|
| **A — platform invariant** | Cost timing is an accounting truth, not a preference. Letting tenants choose creates a platform that produces incomparable financials and a support burden that never ends. The reference's own configuration surface is the proof: three reachable outcomes, one of which recognises cost nowhere, and no cross-validation between the two objects that determine it. |
| **B — tenant-scoped versioned policy** | Different jurisdictions, industries and audit regimes genuinely differ. A platform that forbids the choice will be rejected by the first tenant whose auditor requires the other treatment. |
| **Where they agree** | It must be **declared, versioned, effective-dated, validated against the chart it depends on, and period-locked**. Neither position accepts an unversioned boolean whose meaning depends on an unrelated account configuration. |
| **Status** | `BOSS CONTROLLED DECISION` **B-01**. Not resolved. Interacts with `DEPENDENCY OPEN` D-01. |

### DIS-02 — Whether the obligation ledger belongs to P02 or to Inventory

| Position | Argument |
|---|---|
| **A — Inventory owns it** | It is a consequence of the outflow. Inventory already owns valuation layers; the obligation row is the same object seen from the sales side. |
| **B — a shared ledger owned by neither** | Making it Inventory's makes P02 a consumer of a structure designed for a different purpose, and the history of this codebase is that such structures acquire sales-specific fields until they are neither. |
| **Where they agree** | **P02 may not create, alter, or re-value an outflow.** Whoever owns the ledger, that constraint holds. |
| **Status** | Unresolved. Routed to Core Accounting Reconciliation and to the Inventory track. |

### DIS-03 — Whether the exchange rate is platform, tenant or company data

Stated in full in `20_P02_SCOPE_OWNERSHIP_MATRIX.md` §4. The likely answer is a **shape** — the rate
*source* and the rate *as applied and frozen on an entry* being different objects at different scopes —
rather than a choice among three. `HOLD — SCOPE EVIDENCE REQUIRED` **P02-SC-01**.

### DIS-04 — Whether the reference's return/credit independence is a defect or a requirement

| Position | Argument |
|---|---|
| **A — it is a defect** | Goods come back and revenue is not reversed; goods do not come back and cost is reversed anyway. Both are wrong economically. |
| **B — it is a requirement** | A credit note is a **commercial** act, a return is a **physical** one, and they genuinely occur independently: goods returned but not credited (pending inspection), credit granted without return (damaged, written off in the field), partial credit on a full return. Forcing coupling breaks all three. |
| **Resolution offered, not imposed** | **DC-08-01** — not coupling, and not silent independence, but an **explicit recorded relationship**: linked, deliberately unlinked with a reason, or pending. This satisfies B while removing what makes A dangerous. |
| **Status** | The design candidate is offered; it is **not approved**. |

### DIS-05 — Whether a warning that nothing consults is worse than no warning

Raised by the duplicate-detector finding (`04` §11). One view: a warning surfaced to a user is a control,
because users act on it. The other: an unconsulted warning creates the *appearance* of a control and makes
the gap **harder** to find in an audit, not easier. **This package takes the second view** in `DC-04-07`
and records that it is a position, not a fact.

## 4. What AAS+ Will Not Say

- It will **not** say the reference is wrong. The reference is a working system whose trade-offs were
  taken deliberately. This package identifies where SMEsPlus must take them **differently**, and why.
- It will **not** say P02 is ready for anything. See `18_P02_PMO.md`.
- It will **not** resolve DIS-01 through DIS-05. They are preserved.
- It will **not** state a Thai statutory conclusion. Eight are held with their sources named.
- It will **not** treat agreement between two evidence tracks as proof. Corroboration reached
  independently is recorded as corroboration.

## 5. Independent Challenge Findings

Recorded in full in `16_P02_AAS03_CHALLENGE.md` — twenty package-changing findings and six accepted
coverage gaps, every one of the twenty independently re-derived by the primary session before it changed
anything.

**AAS+ records the four that changed a *design position*, not merely a statement:**

| # | What changed | Design consequence |
|---|---|---|
| 1 | The obligation ledger resolves **one** defect counted three times, not six. | `D-I` narrowed; **`D-VI` split out** as an independent decision. The package's principal structural handoff was overstated and is now stated at its true weight. |
| 2 | The delivered-quantity field is a **cache** for goods; the real second holder is the four methods with no outflow behind them. | The design question moves from *"how do we stop two holders disagreeing?"* to **"how is the performance of a service evidenced?"** — a different and harder question the package had not asked. |
| 3 | The reset-to-draft guard **already exists** and is wired on the purchase side only. | A control the package proposed to build is already built. The fix is wiring, not design. |
| 4 | Cost of sales can be debited to **Revenue** when the product yields no expense account. | A new failure mode with no design candidate against it, and it nets revenue against itself on one document with no error. |

**AAS+ position on the challenge itself.** The panel examined roughly **half** the evidence base and found
twenty defects, two of which refuted verified facts. **There is no basis for treating the unexamined half
as sound**, and AAS+ declines to synthesise any conclusion from `08`, `09` or accounting events AE-05
through AE-13 as though it were twice-verified. It is not.

## 6. Preserved Disagreement Arising From The Challenge

**DIS-06 — whether an obligation ledger can serve a service sale at all.**

| Position | Argument |
|---|---|
| **A** | It can. A service obligation row is written by whatever asserts performance — a timesheet, a milestone, a completion confirmation — and the ledger is agnostic about what produced the row. |
| **B** | It cannot, and pretending otherwise is the reference's own mistake repeated. For goods the ledger row is *evidence*; for a service it would be *an assertion recorded in a ledger-shaped table*, which adds ceremony without adding truth. The honest design names the assertion as an assertion. |
| **Where they agree** | Whatever it is called, it must carry **who asserted, when, and on what basis** — which is `D-II`. |
| **Status** | Unresolved. Raised by the challenge, not by the primary session, and preserved.
