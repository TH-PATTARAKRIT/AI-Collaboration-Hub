# SA17 — PRE-TEST MATRIX HANDOFF BASELINE

Status: **PREPARED — NOT EXECUTED**
Governing law: master prompt §21 — Phase SA must **not** execute the Pre-Test Matrix. It
prepares the verified handoff baseline only.

---

## 1. What this baseline hands over, and what it does not

**Hands over:** business scenarios, their required inputs, expected outputs, routing, inventory
and accounting impacts, controls, exceptions, expected evidence, unresolved bounded risks, and a
recommended scenario priority.

**Does not hand over:** executable test cases, test data, expected values, environment
definitions, or any statement that a scenario would succeed. Those are the next phase's work.

---

## 2. Scenario handoff table

Priority rule applied: **a scenario the business performs daily and cannot traverse outranks a
scenario it performs rarely and can.** Frequency is judged against an SME's ordinary operation,
not against the volume in any reference deployment.

| Pri | Scenario | Traversability | Required inputs not yet established | Expected evidence | Bounded risk carried |
|---|---|---|---|---|---|
| 1 | **E2E-01** Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | `WITH NAMED BREAK` | price and credit determination (SA-D21); the accounting fact that blocks cancellation (`XD-01`) | movement record; recognition event under BD-ACC-01; settlement; reconciliation | The most common SME transaction is not fully traversable |
| 2 | **E2E-05** Dropship | `NOT TRAVERSABLE` | Supply Nature resolution; whether title passage without own movement requires an inventory event | AR + AP against one commercial act | Control-floor bypass (`SA03-F-02`) is on this path |
| 3 | **E2E-04** Sales → Manufacture → RM shortage → Purchase → Production → Delivery | `NOT TRAVERSABLE` | shortage → purchase trigger, ownership, reservation interaction | linked demand chain; cost accumulation | Two modules must agree on who raises supply |
| 4 | **E2E-07** Kit / bundle | `NOT TRAVERSABLE` | component resolution point; which level carries cost | component movements; one commercial line | BD-ACC-03A/03B set policy at Product Category; a kit and its components may sit in different categories |
| 5 | **E2E-08** Service → completion evidence → AR | `NOT TRAVERSABLE` | what constitutes completion evidence and who owns it | recognition event with no stock movement | Boss has ruled the Service menu with no process study behind it |
| 6 | **E2E-16** Quality hold → availability → cost timing | `NOT TRAVERSABLE` | whether a rejection is an inventory event, a return, or neither | inspection outcome; availability change; cost timing | Sits on the accounting path, not beside it |
| 7 | **E2E-03** Sales → Manufacture → FG → Delivery → AR | `WITH NAMED BREAK` | BOM/routing operating semantics | consumption, production, variance | Fixed-overhead injection path absent (`SA11-F-01`) |
| 8 | **E2E-14** Month close → valuation → AR/AP → Bank → Tax → GL → reporting | `WITH NAMED BREAK` | period object; analytic data; statutory register content | closing position; statements | Three constituent items are `PARTIAL` against recorded Phase S terminal states |
| 9 | **E2E-17** Work order → equipment breakdown → maintenance → resume | `NOT TRAVERSABLE` | whether maintenance cost reaches production cost | downtime; cost destination | The route is written verbatim in a Boss decision |
| 10 | **E2E-18** Project → source facts → analytic dimension → derived view | `NOT TRAVERSABLE` | derivation mechanism; behaviour when a source fact reverses | derived view with no duplicate truth | Boss decision forbids duplicate financial truth; nothing yet enforces it |
| 11 | **E2E-06** MTO / buy-to-order | `WITH NAMED BREAK` | order→purchase linkage and its reservation semantics | linked documents | — |
| 12 | **E2E-09** Purchase → capitalization → depreciation | `WITH NAMED BREAK` | Equipment-side semantics | asset register; schedule; disposal entry | Derecognition entry recorded as draft and deletable |
| 13 | **E2E-10** Expense → approval → payable → payment | `WITH NAMED BREAK` | — | approval record **including that approval occurred** | `XD-03` |
| 14 | **E2E-13** Scrap / by-product / variance | `WITH NAMED BREAK` | normal vs abnormal scrap; cost causality | inventory adjustment; cost effect | Scrap currently has no cost causality |
| 15 | **E2E-02** Purchase demand → Purchase → Receipt → AP → Payment | `TRAVERSABLE` | — | full chain | Approval internal logic open (A2) |
| 16 | **E2E-11** Sales return | `TRAVERSABLE` | — | return movement; reversal event referencing the original | — |
| 17 | **E2E-12** Purchase return | `TRAVERSABLE` | — | as above | — |
| 18 | **E2E-15** Correction / reversal / retry / duplicate | `TRAVERSABLE` | — | idempotent retry; ordering-independent reconciliation | Strongest established area |

---

## 3. Controls the Pre-Test Matrix must exercise

| Control | Why it must be tested early |
|---|---|
| Approval **occurrence** is recorded, not only assigned | `XD-03`: the occurrence half was populated on 0 of 27,874 rows in the evidenced estate |
| A cross-module auto-created document meets the target module's own control floor | `SA03-F-02`: the one boundary write bypasses a hard gate |
| Every accounting-determining constraint holds on non-interface write paths | `SA11-F-02` / ND-06: three findings share the "enforced by the screen" mechanism |
| A period lock binds the entry, not the path | `SA10-F-05` / ND-07: two defeat paths, one leaving no record |
| A reservation survives an adjustment | `SA06-F-04` / ND-05 |
| Context-internal transfer neutrality is asserted, not configured | `SA06-F-05` |
| Same-event retry is idempotent; a reversal creates a new event referencing the original | BD-ACC-01 |
| No cross-company statutory posting, offsetting or filing | BD-ACC-02 |

---

## 4. Nature DNA determinations to be carried into Functional Design

| # | Determination | Source |
|---|---|---|
| ND-01 | Supply Nature is a resolved, immutable per-line fact with its resolution inputs retained | `SA05` §2 |
| ND-02 | A single physical-movement ledger; six quantity concepts named separately | `SA06` §1 |
| ND-03 | An automatic cross-module document may not enter a module below that module's control floor | `SA03-F-02` |
| ND-04 | Recording that an approval occurred is mandatory output | `SA08` §3 |
| ND-05 | A reservation is a first-class, addressable business fact | `SA06-F-04` |
| ND-06 | A control that exists only in the user interface is not a control | `SA11-F-02` |
| ND-07 | A period lock is a property of the entry, not of the path that reaches it | `SA10-F-05` |
| ND-08 | Segregation of duties degrades to a **recorded compensating control**, never a silent exception | `SA11` §7.4 |

Each carries an independent rationale in its source register. Master prompt §22 requires that
rationale to survive into design; a determination transcribed without it is inheritance by
another name.

---

## 5. Mandatory Functional Design record element (from `SA12-F-01`)

Every material function's design record must contain an explicit
**"what we deliberately did not inherit"** section, in the form modelled by `SA09-F-02`:
list the reference behaviour, mark it as learning, then state the SMEsPlus position on each item.

This is required because it is the one Nature DNA obligation that is satisfied by writing
nothing, and therefore the one that fails silently.

---

## 6. Bounded risks handed to the next phase

| Risk | Bound |
|---|---|
| Seven business natures cannot be routed | Bounded to SA-D05, D17, D18, D19, D20 — one consolidated research programme, `SA16` |
| The isolation specification is unproven | Bounded: 58 invariants specified, 0 proven; cited as design intent only |
| Fixed production overhead has no mechanism | Bounded to the normal-capacity decision, Boss-owned |
| The evidence base is thin on the demand-and-supply front end | Bounded and measured, `SA00` §7 |
| This session's challenge is not independent | Bounded and declared, `SA13` §1 |

---

## 7. What the next phase must not assume

- That a `TRAVERSABLE` classification means a scenario would succeed. It means every hop has an
  evidenced producer, consumer and compatible interface — nothing more.
- That the Account interfaces are blocked. They are not; nine are `READY-WITH-DELTA` and the
  deltas are named (`SA13` §4).
- That a specification is a control.
- That any Phase S terminal state has been improved by this session. None has.

---

`SA17 — PREPARED`. The Pre-Test Matrix is **not executed** in this phase.

Boss remains the sole Final Approver.
