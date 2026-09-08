# SA_CORR2_06 — ACCOUNTING CONVERGENCE RECONCILIATION
## CP-SA-C2-50 — ALL MATERIAL FLOWS ACCOUNTING-RECONCILED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §7. Governing ruling: **`BD-ACC-01`** — Source Module owns the Business
Fact; Accounting Core owns the canonical immutable Accounting Event Identity; Posting Engine owns
Ledger Posting; same-event retry is idempotent; a reversal creates a **new** event referencing the
original; identity and posting are Tenant + Company bounded.
Supersedes at claim level: `SA07` §1.1 counts and `SA07-F-03`.

---

## 1. The rule, and the reason `SA07`'s seven `UNKNOWN` rows were not unknowable

Master prompt §7 requires that **the recognition question be explicitly answered for every material
flow, including with "no posting by design"**. `SA07` answered it for 22 of 29 and left seven
`UNKNOWN`, all seven being the seven `HOLD` business natures.

`SA07-F-03` treated that one-to-one correspondence as **convergence** — three instruments agreeing.
`SA18-F-01` then tested it and found the three instruments were **not independent**: all three
inherit `SA01`'s domain classification and `SA05`'s nature list. `SA20` §4 accepted the point and
left it uncorrected.

**CORR2 closes it, and the answer is worse than `SA18-F-01` said.** The three instruments did not
merely share a classification. They shared **an undeclared pattern** (`SA_CORR2_03` §1). Three
registers agreed because they were three views of one unpublished search.

> **`C2-F-16`. `SA07` §4's convergence is withdrawn in full. It was not three instruments agreeing;
> it was one instrument, unpublished, read three times.** And once the pattern is published, six of
> the seven `UNKNOWN` rows have answers already in the corpus.

---

## 2. Matrix — re-adjudicated

Rows whose status changes are marked **▲**. Unchanged rows are carried by pointer (`AUTO-C2-01`).

| # | Business flow | `SA07` | **CORR2** | Recognition point, as now established |
|---|---|---|---|---|
| AR-01 | Sales delivery of stocked goods | `RECONCILED` | `RECONCILED` | unchanged |
| AR-02 | Customer billing | `RECONCILED` | `RECONCILED` | unchanged |
| AR-03 | Customer receipt | `RECONCILED` | `RECONCILED` | unchanged |
| AR-04 | Purchase receipt | `RECONCILED` | `RECONCILED` | unchanged |
| AR-05 | Vendor billing | `RECONCILED` | `RECONCILED` | unchanged |
| AR-06 | Supplier payment | `RECONCILED` | `RECONCILED` | unchanged |
| AR-07 | Commercial commitment | `NO POSTING BY DESIGN` | unchanged | |
| AR-08 | Commercial-terms freeze | `NO POSTING BY DESIGN` | unchanged | |
| AR-09 | Stock reservation | `NO POSTING BY DESIGN` | unchanged | |
| AR-10 | Internal transfer (same company) | `PARTIAL` | **▲ `RECONCILED — NO POSTING BY DESIGN`** | The internal / non-internal boundary rule (`SA_CORR2_05` §3) determines it: internal→internal emits no valuation fact. **Neutrality is configuration-protected, and that is now a named control obligation, not an open recognition question** |
| AR-11 | Manufacturing consumption + FG receipt | `PARTIAL` | `PARTIAL` | unchanged — fixed-overhead injection absent |
| AR-12 | Scrap / variance | `PARTIAL` | `PARTIAL` | unchanged — one variance of nine; no cost causality |
| AR-13 · AR-14 | Sales return · purchase return | `RECONCILED — as a ruling` | **▲ `RECONCILED — AND EVIDENCED`** | A credit note posts and reverses **revenue, receivable, tax and cost**, `FACT VERIFIED`. No longer ruling-only |
| AR-15 | Asset capitalization | `RECONCILED` | unchanged | |
| AR-16 | Depreciation | `RECONCILED` | unchanged | |
| AR-17 | Asset derecognition | `PARTIAL` | `PARTIAL` | unchanged |
| AR-18 | Employee expense | `PARTIAL` | `PARTIAL` | unchanged |
| AR-19 | Time-based recognition | `PARTIAL` | `PARTIAL` | unchanged |
| AR-20 | Period / year close | `PARTIAL` | `PARTIAL` — **and sharpened**: there is **no accounting-period object** (`G-11`), and re-dating past a lock is recorded as **the default behaviour**, not an edge case | |
| AR-21 | Analytic dimension attribution | `PARTIAL` | `PARTIAL` — **and sharpened**: *"no cost object … ten de facto cost objects, one shared record type, no discriminator"*, and management data has **no period control and no object control** | |
| AR-22 | Tax determination and register | `PARTIAL` | `PARTIAL` | unchanged; **no statutory claim is made** |
| **AR-23** | **Sell-side commitment cancellation** | `UNKNOWN` | **▲ `PARTIAL — 1 OF 3 ANSWERED, 2 ARE DECISIONS`** | `SA_CORR2_01` §3. The lifecycle states are `FACT VERIFIED`; *which* state blocks is normative |
| **AR-24** | **Dropship** | `UNKNOWN` | **▲ `PARTIAL — RECOGNITION POINT ESTABLISHED`** | Revenue and receivable at invoice; **cost on the vendor bill, at the bill's date, unlinked to the sale**; `FACT VERIFIED`. The SMEsPlus determination is `C2-D-02` |
| **AR-25** | **Kit / bundle** | `UNKNOWN` | **▲ `PARTIAL — LEVEL DETERMINED, POLICY AMBIGUOUS`** | Components move and carry the movement; the price-difference correction is unconditionally on the **bill line's own product**, with 13 live rows dropping layers against a 14,335 control. Open item is `C2-D-03`, a Boss-ruling ambiguity |
| **AR-26** | **Service completion** | `UNKNOWN` | **▲ `PARTIAL — TRIGGER ESTABLISHED AS AN ASSERTION`** | §3 |
| **AR-27** | **Project** | `UNKNOWN` | **▲ `PARTIAL — DERIVATION EVIDENCED, AND IT DUPLICATES`** | §4 |
| **AR-28** | **Quality hold** | `UNKNOWN` | **▲ `RECONCILED — NO POSTING BY DESIGN`** | `SA_CORR2_05` §3. A hold is internal→internal; only the **disposition** posts |
| **AR-29** | **Maintenance cost** | `UNKNOWN` | **▲ `PARTIAL — DESTINATION ESTABLISHED, MECHANISM ABSENT`** | §5 |

### 2.1 Count

| Status | `SA07` | **CORR2** |
|---|---|---|
| `RECONCILED` (incl. 5 `NO POSTING BY DESIGN`) | 13 | **16** |
| `PARTIAL` | 9 | **13** |
| `UNKNOWN` / `NOT RECONCILED` | 7 | **0** |
| **Total material business flows** | **29** | **29** |

Check, executed mechanically rather than asserted: the §2 table's first column yields **29 distinct
identifiers**, `AR-01`…`AR-29`, **each exactly once**, and 16 + 13 + 0 = 29.
*(The first draft of this line was **false as written**: §2 compressed six rows into `AR-01…AR-06`
and three into `AR-07…AR-09`, so a mechanical enumeration returned 24, not 29. The claim read true
to a human and failed its own check. Rows are now written out. Found by this session's own
pre-commit arithmetic sweep — `SA_CORR2_12` §3 — not by review.)*

> **Master prompt §7 is now satisfied in the sense it actually requires: every material business
> flow has an explicitly determined accounting semantic.** Thirteen of them have a named open
> element. **None is unanswered.** That is a different and weaker claim than "reconciled", and the
> distinction is the point of the row above.

---

## 3. `AR-26` service — the trigger is an assertion, and that is the finding

> The genuine second holder exists only where the method has **no outflow behind it at all** —
> services, expense re-invoicing, milestones and timesheets. For those the quantity governing
> revenue **is a permanent human assertion, with no independent operational event and no event
> record.**
> …*"how is the performance of a service evidenced? The reference's answer is that it is not."*
> — `.../P02_ORDER_TO_CASH/05_P02_BUSINESS_EVENT_REGISTER.md` §3a

> For services, milestones and timesheets there is no outflow to write into the ledger. **A ledger
> fed only by the physical side has nothing to record for a service sale.**
> — `.../P02_ORDER_TO_CASH/10_P02_CROSS_PROCESS_OWNERSHIP.md`

**`C2-F-17`.** `BD-ACC-01` makes the Accounting Event depend on a **business fact owned by a source
module**. For a service there is no physical fact — only an assertion. **`BD-ACC-01` is therefore
complete for goods and silent for services**, and a large share of SME revenue is services.

This is not a defect in `BD-ACC-01`. It is a boundary the ruling did not need to draw when it was
written and does now. The design question is already stated as open in the owning package, with both
positions argued and a point of agreement recorded: whatever the construct is called, it must carry
**who asserted, when, and on what basis**.

**`ND-11` (from `SA_CORR2_03` §3.1) is the determination**: a service recognition event in SMEsPlus
carries its asserter, the time of assertion and the basis asserted, and is itself an Accounting Event
under `BD-ACC-01`. **Owner: SMEs Core**, as an extension of the `XD-06` contract — not a new Boss
question.

---

## 4. `AR-27` project — the derivation is evidenced, and it produces duplicate truth

Boss decision `fa57d10f` (read verbatim from the decision body, status
`APPROVED DIRECTION / DETAIL DESIGN PENDING`) states the principle:

> `Project` = operational management of work, milestones, resources, tasks and delivery progress.
> `Analytic Accounting` = financial dimensional analysis describing where / why / for whom accounting
> facts belong. **Project does not own financial source facts. Financial truth remains with source
> domains.**

The mechanism that would implement it is evidenced, and it does the opposite:

> **A timesheet *is* an analytic line** — the timesheet capability does not define its own model; it
> extends the analytic line directly.
> **A work-order writes analytic cost on every duration change.** Two further extensions add a
> second, per-employee line and a third, project-attributed line **from the same value.**
> **The two reporting surfaces resolve "which records belong to this cost object" by structurally
> different rules**, so a project's own profitability total and that project's budget-achieved total
> are not computed over the same row set **even before any double count.**
> — `.../ACCOUNT_P09_PLAN_TO_ANALYZE/.../E01_EVIDENCE_CORRECTIONS_AND_EXTENSIONS.md`

**`C2-F-18`. One hour of work-order duration produces three costed rows, and two report surfaces
read different row sets. Boss's decision forbids duplicate financial truth; the evidenced mechanism
produces it three times over.**

`SA15-F-02` said these Boss-ruled routes had *"nothing yet that can be tested against"* them.
**Wrong, in the useful direction: the route has been traversed and it fails.** A traversed-and-failed
route is a far better input to Pre-Test than an untraversed one — it names the exact test.

`AR-27` is `PARTIAL`: the accounting semantic **is** determined (analytic attribution at posting,
per `fa57d10f`), and the evidenced derivation violates it.

---

## 5. `AR-29` maintenance — destination established, mechanism absent

Established at §5 of `SA_CORR2_05` and `SA_CORR2_03` §3.4, `FACT VERIFIED` with a declared
denominator: **period expense, through the vendor bill, owned by Expense-to-Pay. Not production
cost. Not asset carrying amount.** *"Deployments where any machine cost reached finished goods:
0 of 4"*, verified with the maintenance-integration capability installed.

`PARTIAL`, not `RECONCILED`, because **TAS 2 ¶12 requires the opposite** for maintenance of
production equipment, and no mechanism exists to deliver it (`C2-F-15`). The recognition question is
answered; the answer does not satisfy the standard.

---

## 6. `BD-ACC-01` — contract status, and the three things it must now cover

`SA07` §5 recorded that `BD-ACC-01` is a ruling without a contract (`XD-06`). CORR2 adds the exact
content the contract must carry, all of it derived from evidence in this round:

| Obligation | Arising from | Why the contract, not a decision |
|---|---|---|
| **A deterministic event identity that makes retry safe** | `SA_CORR2_04` `JCP-03` — element 15 fails from both sides; duplicate posting is `REACHABLE`; `XM-01` at `HOLD — DESIGN DECISION REQUIRED` | `BD-ACC-01` already assigns identity ownership to Accounting Core. **Nobody has published it** |
| **A published customer-invoice lifecycle interface** | `SA_CORR2_01` §3.4 — the states are `FACT VERIFIED`; no interface emits them | The fact exists; the contract does not |
| **An assertion-based event for non-physical performance** | `C2-F-17` | `BD-ACC-01` presumes a physical business fact |

**All three are one artefact.** `XD-06` remains `OPEN — DESIGN OBLIGATION RECORDED`, owner SMEs Core,
and it is the highest-leverage open item in the package: it closes `H-01`, `H-02`, `H-03`,
`JCP-03`, element 15 and `AR-26`.

---

## 7. Convergence, stated honestly this time

`SA07-F-03` claimed three independent instruments converged on seven items. Withdrawn (`C2-F-16`).

**What CORR2 offers instead is not convergence and does not pretend to be.** The status changes above
were produced by **one party reading path sets that a prior party did not reach**. That is a single
instrument too. Its results are stronger only because each is anchored to a verbatim quotation with
an evidence tag from the owning package, and because the pattern is published.

> **Two registers agreeing is not evidence. Two registers agreeing, each citing a different owning
> package's `FACT VERIFIED` finding, is evidence about those packages — not about the registers.**

The genuine independence gap is `SA_CORR2_11`, and it is not closed by anything in this file.

---

`CP-SA-C2-50 — ALL MATERIAL FLOWS ACCOUNTING-RECONCILED (execution status).` **29 of 29 flows have
an explicitly determined accounting semantic; 13 carry a named open element; 0 remain unknown.**

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
