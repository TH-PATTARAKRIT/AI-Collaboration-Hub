# 44 — P03 AAS-03 TARGETED CHALLENGE

**LAYER 2 — AUDIT QUARANTINE.** Run only against materially changed areas.
Consensus is **not** forced. Per `smeplus-adversarial-section-not-summary-rule`, **§6 is
the citable output of this file, not the headline tables in `26`–`42`.**

Four mandated disproof attempts are §2–§5. Each was run to succeed, not to be seen to run.

---

## 1. The four experts

`E1` Leader Functional Design · `E2` Leadership Database Design ·
`E3` Lead Integration & Localization · `E4` Lead Code & UI Architect.

---

## 2. MANDATED DISPROOF — *"DC-14 creates duplicate economic cost"*

**E2 attempts the disproof and SUCCEEDS.**

An analytic line is not a general-ledger entry. `account.analytic.line` has no path to
inventory carrying value; no valuation layer, no journal item, no stock move reads it. Two
analytic line sets from one computed value therefore create **two records and zero
economic cost**.

**Result: DISPROVED as stated.** `DC-14` does **not** create duplicate economic cost.

**What survives.** Management attribution doubles where both distributions resolve to one
analytic account. That is a real defect of the management ledger — and it is **P09's
ledger, not P03's**. `29` §5 was written to this conclusion and already classifies
`DC-14` as *MULTIPLE ATTRIBUTIONS — ECONOMIC EFFECT DEPENDENT*, so the disproof
**confirms** the disposition rather than overturning it.

**E1 dissents on emphasis:** for a manufacturer, a doubled cost-centre total *is* an
economic misstatement in every sense that matters to a plant manager, even if it never
reaches the statutory ledger. Recorded, not resolved.

## 3. MANDATED DISPROOF — *"No idempotence guard exists for DC-15"*

**E4 attempts the disproof and PARTIALLY SUCCEEDS.**

A guard does exist: `_post_labour` is invoked from exactly one call site, filtered to
orders in state `done` (`mrp_account/models/mrp_production.py:110`). A manufacturing order
does not re-enter `done` in normal operation. So the claim *"nothing prevents a second
post"* is **too strong**.

**Result: PARTIALLY DISPROVED.** The correct statement is narrower and is what `30` §5
carries:

> There is no idempotence control **on the entry**. There is a state filter **at the call
> site**. The marker that would provide entry-level idempotence is written and never read.

**E4 presses further and is refused.** E4 argues the classification should therefore be
*IDEMPOTENCE PARTIAL*. **AAS+ declines** — see `45` §3 — because a call-site filter is not
a property of the entry and does not survive the addition of a second call site, which is
exactly the change any of the fourteen `DESIGN CANDIDATE` requirements would introduce.
**E4's dissent is preserved.**

## 4. MANDATED DISPROOF — *"Analytic netting destroys intended management cost"*

**E3 attempts the disproof and PARTIALLY SUCCEEDS.**

The attribution is **not destroyed**. Two analytic lines are created and persist, each
carrying its own general-ledger account and the same distribution. A report that filters or
groups by GL account, or excludes balance-sheet accounts, shows the full depreciation
charge on the cost centre.

**Result: PARTIALLY DISPROVED.** "Destroys" overstates it. `33` §4 already carries the
corrected form — *RECORD-ONLY NETTING VERIFIED*, with the line-level/balance-level
distinction explicit — so the file was written to the disproved-and-corrected statement,
not to the strong one.

**What survives, and it is enough:** any report that **sums the cost centre** shows zero,
and summing the cost centre is what a cost centre is for. The premise the AAS+ veto rested
on — *depreciation already reaches production cost centres* — remains unusable.

**E2 adds, unprompted:** P09 records that the distribution is a JSON payload and that plans
have **no company field**, so a cost centre may aggregate across companies with nothing
preventing it. **That is a larger defect than the netting** and it is P09's. Noted, not
adopted.

## 5. MANDATED DISPROOF — *"The complete cost-mechanism population is nine"*

**E3 attempts the disproof and SUCCEEDS, twice over.**

1. **Nine is not P04's figure.** P04's branch corrects it to **seven** under its own
   declared unit; nine is reachable only under a *different* unit (posting artefact). P03
   propagated nine from a message without reading the branch — `42` §3.
2. **Neither seven nor nine is complete.** Both count *machine-cost monetisation*. The
   complete cost-injection population, over all manufacturing cost types, is **fifteen**
   (`28`), of which **four are live**.

**Result: DISPROVED.** Nine is neither the peer's number nor the complete population.

**E3's finding against P03's own work.** `28` §3 first asserted *"One is live"* while its
own table marked three further mechanisms reachable. The three were then measured and are
live. **A headline that did not reconcile with the table directly beneath it** — the same
class as `C-07` in round 1 and the third instance in this package. Recorded as
`RE-P03-14`.

## 6. Corrections carried forward — **the citable output**

| ID | Correction | Effect |
|---|---|---|
| `TC-01` | `DC-14` does **not** create duplicate economic cost | Disposition confirmed; E1's dissent on emphasis preserved |
| `TC-02` | *"Nothing prevents a second post"* is too strong — a call-site state filter exists | `30` §5 narrowed to entry-level; E4's push for *IDEMPOTENCE PARTIAL* refused, dissent preserved |
| `TC-03` | *"Destroys"* overstates the netting | `33` §4 carries line-level vs balance-level explicitly |
| `TC-04` | **Nine is wrong twice** — not P04's figure, and not the complete population | `42` §3, `27` §2 |
| **`TC-05`** | **`28` §3's headline did not reconcile with its own table** | Corrected by measurement, not argument — `RE-P03-14` |
| `TC-06` | `DC-13` was recorded *"reachable in principle, not measured"* and is in fact **live** — 987 unbuild orders | `26` §4 corrected. **The only live `DC-*` in the package** |
| `TC-07` | `UNR-P03-09` was deferred to "next round" and was executable in one command | Closed the same session — `47` §2 |

**Seven corrections.** Counted from the table, not asserted.

## 7. What each expert says is still missing

| Expert | Missing |
|---|---|
| `E1` | No deployment exists in which the conversion-cost model has ever run, so **every reachability conclusion is about systems that do not exercise the subject** |
| `E2` | `iTEST02` unread (`UNR-P03-07`) — one tooling upgrade away, and it is the cheapest open item in the package |
| `E3` | The three readable databases are not established as the migration target (`UNR-P03-10`); a "not used here" is not "not used anywhere" |
| `E4` | Concurrency on `_post_labour` is untested and untestable read-only; `UNR-P03-06` stands |

**E1's point is the one to carry.** The runtime evidence is powerful for what it shows and
silent on what a configured plant would do. It bounds the package rather than completing it.
