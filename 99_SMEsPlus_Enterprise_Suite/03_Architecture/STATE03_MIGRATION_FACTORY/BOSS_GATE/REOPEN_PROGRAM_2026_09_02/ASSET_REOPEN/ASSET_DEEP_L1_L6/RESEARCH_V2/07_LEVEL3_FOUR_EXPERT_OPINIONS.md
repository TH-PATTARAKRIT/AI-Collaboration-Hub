# 07 — DEEP LEVEL 3: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** 24 functions traced to source with their triggers, states and GL
effects. §3.2 — catch-up, destroy the future, rebuild — is the correct functional
generalisation and it holds across four different user actions. That is a real
pattern, not a summary.

**Missing.** Nobody has established what the user is *told* when these things
happen. §3.1 says confirming an asset posts journal entries years into the future.
Does the user know? Is there a warning? A functional design that silently posts
sixty future entries on a button press has a consent problem, and I cannot see
from the trace whether the product addresses it.

**Risky.** §3.3. The team has been saying "the asset" throughout this project. After
one re-evaluation there is no such thing — there is a parent and a child, and the
answer to "what is this machine worth" requires knowing that. Every functional
spec written so far that says "the asset's value" is ambiguous and needs revisiting.

**Challenge.** I challenge the completeness of `F24` as a single row. "Transfer,
split, merge" are three different business needs and lumping them into one
`VERIFIED GAP` hides which one actually matters. For a concrete producer, moving a
mixer from one plant to another is a **transfer**, and it is common. Splitting an
asset is rare. Merging is almost never needed. Recording them as one row invites
the design to treat them as one problem.

**Evidence required next.** What the reference ERP does when a business genuinely
needs a transfer — is the practice to dispose and recreate? That is behavioural
evidence and it is worth having before SMEsPlus designs a transfer function.

**Assumed too early.** That "Pause" means what an operations person means by it.
§3.4 shows pause **extends the asset's life**. An operations person pausing a
machine for a three-month overhaul may reasonably expect the depreciation *end
date* to stay fixed and the periods to be skipped. The system does the opposite.
That is a genuine expectation mismatch and it should be surfaced to the Boss.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** §3.2 is as much a data finding as a functional one: **posted rows
are immutable**. Corrections are new rows or reversals. That is exactly the
property an audit-grade sub-ledger needs, and SMEsPlus should inherit it verbatim.

**Missing.** The trace still does not state which of these operations are
transactional as a unit. F11 catches up, writes the asset, posts a revaluation
entry, creates a child asset, confirms the child, rebuilds the parent board, then
cascades to every other child. If that sequence fails halfway, what is left? I
cannot answer that from the source read, and it is exactly the kind of thing that
produces orphaned half-assets in production.

**Risky.** §3.6, the board invariant, is enforced as a **model constraint**. It is
therefore evaluated on write. Any bulk data operation that bypasses the ORM —
which is precisely what a migration does — can leave the invariant violated with
no error at all. Given that the UAT is mid-migration with 280 records, this is not
hypothetical.

**Challenge.** I challenge §3.7's phrasing "then frozen". The distribution is not
frozen; it is *copied at entry-preparation time*. Those are different failure
modes. Frozen implies the system prevents change. It does not — it allows the
change and applies it asymmetrically to future rows only, which is worse, because
the asset row and its own historical entries then disagree and nothing flags it.

**Evidence required next.** A count on the UAT of assets whose current
distribution differs from the distribution on their own posted entries. That
single query would quantify a real exposure.

**Assumed too early.** That the reversal path in §3.2 step 2 is harmless. Reversing
a posted future entry leaves **two** posted rows where there was one. Over an asset
that is re-evaluated three times, the entry count grows and every naive "sum the
depreciation entries" query must exclude reversals and reversed entries correctly.
The engine does this; downstream reporting must too.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** §3.4's separation of what pause does mechanically from what it means
statutorily is the right treatment. The mechanics are proven; the Thai question is
flagged and not answered. That is correct discipline.

**Missing.** Nothing in Level 3 addresses **multi-company**. The company field is
required and the currency is derived from it, and the runtime shows a four-company
database with all 280 assets in one company. Whether an asset can move between
companies, and what that means for a group, is untouched.

**Risky.** §3.1 is a localisation risk that has not been named as one. Posting
entries years into the future interacts badly with Thai monthly and annual filing:
those future-period entries exist in the ledger now. Any report that filters by
posted status rather than by date will include them.

**Challenge.** I challenge the framing of §3.5. Saying lock dates are "respected on
three of five paths" understates it. The **confirm** path is the one that posts
sixty entries at once, and it is the path with no lock-date check in this module.
If the underlying posting layer does not stop it, an asset confirmed today can
post entries into a closed period. That should be raised as a High finding, not a
footnote, and it should be tested on the UAT rather than reasoned about.

**Evidence required next.** A confirm attempt against a locked period on the UAT.
It is a five-minute test and it converts a High risk into a fact either way.

**Assumed too early.** That the equipment status flip at `F22` is harmless. It is a
custom override that mutates a record in **another domain** as a side effect of a
financial confirmation, with no transaction boundary stated and no reverse on
cancel. Confirm an asset, then cancel it, and the equipment stays flipped.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** The trace is genuine. Every row in §1 corresponds to a method that
was read, and the four `VERIFIED GAP` rows correspond to searches that returned
nothing. The thirteen guards in §4 are enumerated from the constraint and guard
methods, not inferred.

**Missing.** The view layer is still only partly closed. In particular the
**wizard's** view is unexamined, and that wizard is where five different accounting
events are selected. Which options a given user actually sees, and under what
conditions, is not established.

**Risky.** `F23` is the finding I want carried forward loudest. A custom module
ships a file that implements "deactivate the equipment when the asset is sold",
and the module's package initialiser **never imports it**. It is not a subtle bug.
It means a documented, intended, believed-in behaviour does not run at all, and
nothing anywhere reports that. If one such defect exists in this custom module,
the correct assumption is that others do.

**Challenge.** I challenge any inference that the custom modules in the workspace
behave as read. `F22` and `F23` come from the same small module, and one of them is
dead. I found two further constructs in that module that target framework
generations that have passed: a field attribute removed after v16, and a
display-name hook removed after v16. Neither will raise an error; both will simply
do nothing. **The module runs, and parts of it are inert.** Verifying which parts
requires the running system, not the source.

**Evidence required next.** `G1-01` and `G1-02`, still open, still not closable
from static evidence. Plus a behavioural check on the UAT: sell an asset that has
an equipment link and see whether the equipment is deactivated.

**Assumed too early.** That "the code exists" means "the behaviour happens". `F23`
is the counter-example and it was found only because the package initialiser was
read as well as the model file. That check should be applied to every custom module
this project relies on, not just this one.

---

## AAS+ CONSOLIDATION — LEVEL 3

### Agreements

1. Posted entries are immutable; every change is catch-up + reverse-future +
   rebuild-forward. All four. **This is the level's headline and it should be
   inherited by SMEsPlus verbatim.**
2. Confirming an asset posts its entire remaining life immediately. All four.
3. An upward re-evaluation creates a second asset record; asset counts are not
   machine counts. All four.
4. Pause shifts the calendar and extends the end date; it does not skip periods.
   All four.
5. `F23` is dead code. All four.

### Disagreements — preserved

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D3-01` | Severity of the missing lock-date check on confirm | Expert 3: High, escalate. Expert 4: unknown until the posting layer is checked; do not assign severity to an untested path. **Unresolved — recorded as `UNR-09` at severity "High if confirmed", and the test is specified** |
| `D3-02` | Whether `F24` should be one gap or three | Expert 1: three, because only transfer matters commercially. Experts 2/4: one, because the source contains none of them and the distinction is a design question, not a research finding. **Unresolved — `39` records transfer separately at Expert 1's insistence** |
| `D3-03` | "Frozen" vs "copied at preparation time" for analytic | Expert 2's correction accepted by the other three. **Resolved — `06` §3.7 and `21` use the corrected wording** |

### Contradictions confirmed at Level 3

| ID | Summary |
|----|---------|
| `CTR-02` | The custom equipment link's disposal behaviour is dead code |
| `CTR-06` | The board invariant is ORM-enforced only, and the population was loaded by migration |

### Evidence gaps

| ID | Gap | Status |
|----|-----|--------|
| `G3-01` | Transactional boundaries of the multi-step modify operation | Open → `41` `UNR-10` |
| `G3-02` | Lock-date behaviour on confirm | Open → `41` `UNR-09` |
| `G3-03` | Assets whose current analytic differs from their posted entries' | Open → `41` `UNR-11` |
| `G3-04` | Multi-company behaviour of assets | Open → `41` `UNR-12` |
| `G3-05` | Whether other custom behaviours are similarly inert | Open → `41` `UNR-13` |

### Consolidated position at the end of Level 3

The engine is **better built than the project has been giving it credit for**. It
is immutable-by-construction, self-correcting on rounding, and defended by thirteen
guards and one strong invariant. Those properties are worth transferring.

The risks are not in the engine. They are in three other places:

1. **Configuration** — one field silently chooses between two incompatible day
   arithmetics (`16`, `17`).
2. **Custom code** — at least one believed-in behaviour does not execute (`19`).
3. **Expectation** — pause, re-evaluate and confirm all behave differently from
   how an operations reader would predict (§3.1, §3.3, §3.4).

### Gate to Level 4

Open. Level 4 must establish whether any of this reaches production costing.
