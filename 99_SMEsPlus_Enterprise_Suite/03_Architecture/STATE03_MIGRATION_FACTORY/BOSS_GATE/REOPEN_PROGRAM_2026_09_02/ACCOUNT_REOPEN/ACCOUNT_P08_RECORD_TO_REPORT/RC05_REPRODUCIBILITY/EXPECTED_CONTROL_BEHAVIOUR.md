# RC-05 — EXPECTED CONTROL BEHAVIOUR, RECORDED BEFORE EXECUTION

**Written and hashed BEFORE `rc05_balance.py` was run even once.** Required by Boss ruling
`Q-BOSS-03` §2. A control whose expected behaviour is written afterwards cannot fail.

| # | Control | Expected BEFORE the run |
|---|---|---|
| 1 | **POSITIVE — DB-SM** | `lines_posted > 0` and `sum \|debit\|+\|credit\| > 0`. A zero would mean the extraction failed, **not** that the ledger balances |
| 2 | **POSITIVE — DB-BK, DB-EV** | non-zero rows extracted; both open and parse |
| 3 | **NEGATIVE / discriminating population** | DB-BK and DB-EV together hold **~22 posted entries** (P08 `19_`). They must show a **radically smaller** posted population than DB-SM. If all three looked alike, the instrument is not measuring what it claims |
| 4 | **INJECTION** | `--inject-unbalanced 0.01` must raise the unbalanced count by **exactly +1** at `exact`, `1e-7`, `1e-4` — and at `0.005` (0.01 > 0.005). **This is the only proof the predicate can return non-zero** |
| 5 | **DRAFT SPREAD** | printed for every database whether or not it is zero, so a bare posted-zero is never read alone |
| 6 | **FAIL-CLOSED — schema** | a missing required column exits **3** with the column named, rather than reading a wrong column positionally |
| 7 | **PARENT_STATE_DISAGREE** | an observation, **not** a pass/fail. Any non-zero value is a real finding about the extract and is reported as such |

## The claim under test, and what the owner predicts

P08's corrected claim (notification `64_`, at `c7cfd8a`): **0 unbalanced at exact equality and at
`1e-7`, `1e-4`, `0.005`, on both the computed and the stored column, in all three databases** —
i.e. **tolerance-independent**.

**Owner's prediction, recorded so it can be wrong:** all three databases return **0 / 0 / 0 / 0** on
both columns.

**A named uncertainty the run will settle, not the owner:** P08 states the figure as *"across
**169,143**"* **without naming its unit**. This instrument counts **entries (`account_move`)**, and it
prints `POSTED_MOVES_WITH_LINES` **and** `lines_posted` separately. **If `169,143` turns out to be
posted *lines* rather than posted *entries*, then P08's denominator is stated in the wrong unit** —
a defect in the claim, independent of whether the count of unbalanced entries is zero.
**The owner does not predict which. The printed output decides it.**

> **Nothing in this file is a result.** It is a prediction, published so the independent verifier can
> see what was expected before anything ran, and so a control that merely confirms cannot be passed
> off as a control that could have failed.
