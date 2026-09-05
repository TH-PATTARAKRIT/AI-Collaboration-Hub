# P06_PERIOD_CLOSE_WRONG_MOVE_RECONCILIATION.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S13)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope:** material delta only. `28_` REFUSE / RELOCATE / PROCEED stands unchanged.

---

## 1. The point under revalidation

`28_` PC-F-07 recorded that the one indirect lock-date block on the un-reconcile path fires on the **wrong move**.

`$V18E/account/models/account_bank_statement_line.py:475-490` — `action_undo_reconciliation` performs no lock check. An indirect check is reached because `Command.clear()` unlinks journal items and `$V18E/account/models/account_move_line.py:1700-1703` calls `_check_fiscal_lock_dates()` on posted moves — **but `self.move_id` there is the statement line's own move.**

| | |
|---|---|
| **Intended control target** | the accounting fact being retroactively altered — the **counterpart invoice**, whose residual and payment status change |
| **Actual target** | the **statement line's own move** |
| **Does it protect accounting truth?** | **No.** A statement line dated in an open period can un-reconcile an invoice dated inside a hard-locked period. |
| **Does another move remain mutable?** | **Yes — the counterpart, which is the one that matters.** |
| **Cross-period consequence** | the closed period's ageing, payment status and cash-basis tax position change, with the compensating reversal landing in an open period |

**PCW-F-01 — The scoping defect does not depend on whether the block fires.** Round 3 rated the *existence* of the block medium-high confidence pending a test (`P06-OQ-20`). **Whether or not it fires, it fires on the wrong record.** The finding is independent of the open question.

---

## 2. P08 confirms it from the ledger side, and goes further

**PCW-F-02 — P08 classifies the un-match gap as a `VERIFIED ABSENCE`, with a wider denominator than P06's.**
P08 `REC-11`: *"Un-matching is **not blocked in a closed period**. `A VERIFIED ABSENCE`, scope = the two settlement models in full and the entire reconciliation-plan region of the item model; **the pattern set covered every lock-check symbol**."*

P06's denominator was five files and one pattern family. **P08's is a symbol-complete sweep of the same region. Two independent denominators, same result.**

**PCW-F-03 — And P08 supplies the deeper cause P06 did not have.**
`REC-05`: *"**A match carries no event date.** Its as-of date is the later of the two matched documents' dates. Matching two prior-period items today retroactively closes them in a re-run of that prior period's ageing, with nothing in the data to explain the difference."*

**This reframes the whole finding.** The lock check cannot be pointed at the right move **because the reconciliation event has no date of its own to check.** A control needs a date to compare against a lock; the matching act has none. **The wrong-move scoping is a symptom; the missing event date is the cause.**

That is the same gap P08 raised as an inbound dependency on P06 — `XP-05`, accepted as `P06-B-57` (`53_` PIN-F-08).

**PCW-F-04 — P08 also records that removing a match removes its own audit trail** (`REC-13`), which closes the loop with `60_` DFI-F-04.

---

## 3. RELOCATE — confirmed by P08 and P04, and wider than P06 measured

P08 `PC-29a`: *"**The irrevocable lock refuses a *reopen*, but it does not refuse a *posting*.** … an entry aimed at an irrevocably locked period is **relocated forward and posted**, not rejected. **The product's own test asserts this**, moving a full annual charge across a fiscal-year boundary."*

**PCW-F-05 — The behaviour is asserted by a product test, which raises its evidential standing: it is intended, not an oversight.** P08 `P08-PEER-01`, corroborating P04 `P04-F-61`.

P08 also names the asymmetry as its own contradiction `P08-CONTRA-16`: the same cut-off **hard-refuses** an asset re-evaluation with an explicit error while silently re-dating a posting. **One control, two opposite behaviours.**

---

## 4. Lock-date inheritance — P08 refines P06's finding

P08 `PC-08`: *"Hierarchy handling is **asymmetric**: the four relaxable cut-offs are evaluated per ancestor and may be relaxed per ancestor; the irrevocable cut-off is the strictest value across the whole ancestor chain and **cannot be relaxed at any level**."*
P08 `PC-06`: *"The year-end parameters are delegated to the **root** of the company tree, so **a subsidiary cannot hold its own year-end**"* → `P08-CONTRA-09`.

**PCW-F-06 — This closes the loop with `P06-B-27`.** P06 established that `root_id` delegation covers `fiscalyear_last_day` and `fiscalyear_last_month` but **not `vat`**. P08 states the consequence: **a company that may be a distinct legal entity cannot hold its own year-end.** Two processes, two halves of one finding.

**And P08 adds three P06 did not have:** `PC-11` — the widest derogation ("everyone, forever") produces **no exception record at all**; `PC-12` — the window depth is unbounded; `PC-14` — **no screen lists the exceptions granted**.

---

## 5. The answer P06 needed, supplied by P08

`PC-17`: *"Closing a month is the movement of a cut-off date. It is not a state transition, **because there is no object to transition** … **no field anywhere answers 'is month M closed?'** — only 'is date D at or before cut-off L, for this user'."*

**PCW-F-07 — This resolves `F-17` and explains every close finding in P06 at once.** There is no close *object*, so:
- there is nothing for a reconciliation to be checked against;
- "closed" is per-user, because derogations are per-user;
- a reconciliation cannot be refused for a period, because the period is not a thing.

**P06 adopts P08's `SC-CL-02`** — *"Accounting period as an object (does not exist in the benchmark) — COMPANY"* — as the prerequisite for every P06 close requirement.

---

## 6. Requirements

| ID | Requirement | Origin |
|---|---|---|
| `PCW-R-01` | A settlement event carries **its own date**, and that date is what every period control tests. | P08 `REC-05`, `P06-B-57` |
| `PCW-R-02` | A period is a **first-class object with a state**, not a movable date. | P08 `SC-CL-02` |
| `PCW-R-03` | A control that protects a closed period tests **every** fact it alters, not only the record that triggered it. | `28_` PC-F-07 |
| `PCW-R-04` | Posting into a closed period is **refused with a named cause**, never silently re-dated. | P08 `P08-RQ-PC-02` |
| `PCW-R-05` | A derogation is scoped, time-boxed, recorded and listable. | P08 `PC-11`, `PC-14` |

**Coordination:** P08 owns the close architecture (`F-17` resolved to P08). P06 supplies the settlement-event date it requires and adopts its requirements. **P06 does not decide P08's architecture.**
