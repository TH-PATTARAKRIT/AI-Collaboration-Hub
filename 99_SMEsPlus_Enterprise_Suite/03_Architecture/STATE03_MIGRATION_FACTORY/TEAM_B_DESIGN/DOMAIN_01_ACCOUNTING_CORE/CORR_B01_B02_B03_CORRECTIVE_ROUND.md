# CORR-B01 / CORR-B02 / CORR-B03 — Targeted Design Correction

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-29-MIG-B-D01-CORR-001 |
| Date | 2026-08-29 |
| Domain | DOMAIN_01 — Accounting Core |
| Source of truth | ChatGPT Independent Team B Design Audit, commit `aa60c2d0497cefe804d37953bbfaa597c3476d79`, verified against the live repository before any correction was made |
| Scope | Targeted correction of exactly three material findings. B0–B17 not restarted. No code. No DOMAIN_02. No PMO. No self-approval. |
| Reconciled against | `DOMAIN_01_ACCOUNTING_CORE_K_CORR_B_EXECUTOR_PROMPT.md` (commit `f363ee127b17d0d2743c4c2fde402bd39eabc633`), found on the repository after this round's edits were already underway from the chat-issued directive. The two are consistent; K adds detail (a real Jira key, ERPPLUS-100; four additional regression scenarios; specific required artifact schemas) that this document and [B18](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md) were updated to satisfy, per K's own instruction to prefer repository artifacts over an older chat summary where they add detail. |

## 0. CORR-B Change Log (required schema)

| finding_id | old_statement_or_rule | corrected_statement_or_rule | affected_artifacts | reason | verification_status |
|---|---|---|---|---|---|
| D01-B-AUD-01 | B04 §4: period close is a 4th automatic, permanent Consumption trigger; reopen is "the only path back to correctable" | Period Lock (CAP-04/BINV-02) and Consumption (BINV-06/07, now 3 triggers) are independent, orthogonal gates on Amendment; reopen restores only the Lock condition, never touches Consumption | B04 §2/§3/§4/§5/§8/§9, B05 BINV-06, B07 §1, B08 MP-10, B13 DT-02, B15 §3a/§6 | Original statements were logically contradictory: BINV-07 forbids retracting a Consumption Record, which reopen-restores-correctability required | VERIFIED — B18 Tests 1–3 |
| D01-B-AUD-02 | B08 MP-02: MP-01 + Normal Balance Side implies `Assets = Liabilities + Equity` unconditionally | Proven instead: `Assets + Expenses = Liabilities + Equity + Revenue` holds unconditionally (expanded equation); simple equation is the Revenue=Expenses=0 special case, true post-close once Current Earnings transfers to Equity | B07 §1a/§1b, B08 MP-02, B05 BINV-10, B15 §3a | Original proof silently assumed Revenue/Expense already closed to zero — false during any open period with P&L activity | VERIFIED — B18 Tests 4–5, worked numerically |
| D01-B-AUD-03 | B08 MP-09: aggregation excludes Lines belonging to a *currently* VOIDED Entry | Aggregation is a pure date filter (`date <= D`); Void is always a dated, linked Correction Entry (zero-net reversal), never a status flip, so its effect naturally applies only from its own date forward | B04 §2/§3/§5, B08 MP-09, B05 BINV-11 (new), B13 DT-07 (new), B15 §3a | Status-based filtering let a later void silently change an earlier as-of result — a later event rewriting earlier historical truth | VERIFIED — B18 Test 6–7 |
| (regression finding, not an audit ID) | B05 BINV-11 (as first drafted this round): guarantee proviso said "no fact... added, corrected, or voided" without addressing Amendment | Proviso scoped precisely: guarantee is unconditional for consumed facts; intentionally does not cover an unconsumed fact's pre-consumption Amendment, since "unconsumed" means nothing has relied on the value yet | B05 BINV-11, B08 MP-09 proof requirement | Found while constructing B18 Test 10 — the initial correction's guarantee statement was broader than its own mechanism actually delivered | VERIFIED — B18 Test 10 |

## 1. CORR-B01 — Consumption vs. Period Reopen

### The contradiction, precisely

B04 (original) listed period close as a fourth, automatic Consumption trigger. B05 BINV-06
requires consumption to freeze an Entry permanently. B05 BINV-07 requires a Consumption
Record to be never retracted, deleted, or reversed — by construction. B04 (original) also
described period reopen as "the only path back to correctable" for entries consumed via
period close. **All four of these statements cannot hold simultaneously**: if period close
creates a real, permanent Consumption Record, no reopen — however authorized — can
legitimately restore correctability, because BINV-07 forbids clearing that record by
definition. The design was asserting both "this is permanent" and "this is reversible" about
the same fact.

### Alternatives compared (not blindly accepting the audit's suggested direction)

| Option | Description | Verdict |
|---|---|---|
| A — Keep period-close-as-consumption, delete the reopen claim | Permanent, blanket freeze on every entry in a closed period, forever, no reopen-based exception at all | **Rejected.** Needlessly rigid: CO-06 already keeps Correction no harder than Amendment, so the "protection" this option buys over the adopted option is marginal, while the cost (no lightweight path for a same-day typo in a period closed prematurely) is real. |
| B — New three-state Period concept (Open / Soft-Closed / Hard-Closed) | Formalizes the same split as Option C below, but as a new state machine on Period itself | **Rejected.** Adds conceptual surface area (a new tri-state entity) to achieve exactly what separating two *already-existing* concepts (Period status, Consumption status) achieves for free. |
| **C — Period Lock and Consumption as two independent, orthogonal gates on Amendment (adopted)** | Amendment requires BOTH "unconsumed" AND "period open." Reopen restores only the second condition; it never touches the first, because period close no longer sets the first. | **Adopted.** Minimal change (remove one trigger from an existing list, add one condition to an existing gate rule), reuses all existing machinery, and is the option that makes CO-08's reopen-authorization design meaningful again rather than a no-op or a contradiction. |

### Why Option C is not just "the audit's suggestion, implemented"

The audit's §4 recommended direction and the reasoning that produced Option C converge, but
independently: the audit's own text frames it as "period close is a lock, not consumption" —
this corrective round additionally identified *why* that framing is correct by naming the
structural parallel to Team A's own CF-06 finding (the reference system's `state` field
conflating "is this committed" with "should this count"; this domain's B04 §4 had, on its own
first pass, committed the same category of error between "is the period locked" and "has this
been externally relied upon"). Recognizing the pattern, not just accepting the fix, is what
justifies calling Option C selected rather than merely applied.

### What changed

`B04` §2 (VOIDED description), §3 (event table), §4 (Consumption Gate — rewritten), §5 (Void),
§8 (diagram), §9 (mandated-questions table) · `B05` BINV-06 (trigger list corrected to three),
residual-assumption note · `B07` §1 (Consumption Record row) · `B08` MP-10 (rewritten) ·
`B13` DT-02 (rewritten, original recommendation kept visible and explicitly withdrawn) ·
`B15` §3a (new), §6 (assumption #2 revised, old wording kept visible per instruction).

## 2. CORR-B02 — Accounting Equation Mathematics

### The defect, precisely

MP-02 (original) claimed: entry-level balance (MP-01) plus correct Normal Balance Side per
Account Category implies `Assets = Liabilities + Equity` across the whole Ledger, with no
further condition. This is false during an open reporting period with any Revenue or Expense
activity — the claim silently assumed Revenue and Expense accounts are already empty
(equivalent to assuming the period had already been closed), which is exactly the "hidden
assumption that P&L has already closed" the audit named.

### The corrected proof (full derivation in [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-02)

Summing MP-01 over every Entry gives a grand-total identity (total debits = total credits,
across all accounts). Partitioning accounts by Normal Balance Side and rearranging that
identity proves, unconditionally: `Assets + Expenses = Liabilities + Equity + Revenue` — true
at every moment, open period or not, with no assumption about closing status. Current
Earnings (`Revenue − Expenses`, B07 §1b) is then defined so the expanded equation can be
regrouped as `Assets = Liabilities + (Equity + Current Earnings)` for reporting purposes. At
actual period close, Current Earnings is transferred into formal Equity and Revenue/Expense
reset to zero (BINV-10, strengthened) — substituting Revenue = Expenses = 0 into the expanded
equation collapses it exactly to the simple form, using the updated Equity figure. The simple
equation is proven as a special case, not asserted as a separate, independent fact.

### Why this satisfies the audit's stated requirements

Works during an open period (the expanded equation needs no closing assumption); explains the
post-closing position (the simple equation is the Revenue=Expenses=0 special case, tied
explicitly to what CAP-09/BINV-10 must do at close); no circular reasoning (built from MP-01 +
Normal Balance Side alone, both already established); no hidden closing assumption (none is
used in the derivation); conceptual only (an algebraic identity over B07's entities, no
schema, no implementation).

### What changed

`B07` §1a (corrected overclaim), §1b (new — Current Earnings) · `B08` MP-02 (rewritten with
full proof), MP-08 (cross-reference to Void as a zero-net instance) · `B05` BINV-10
(strengthened to require the Current Earnings transfer) · `B15` §3a (new).

## 3. CORR-B03 — Historical As-of / VOID Time-Consistency

### The defect, precisely

B04 (original) allowed an unconsumed COMMITTED Entry to move directly to VOIDED via a status
flip. MP-09 (original) excluded a VOIDED Entry's Lines from aggregation based on *current*
status. Consequence: an Entry valid and committed at D1, voided later at D2, would vanish from
a "balance as of D1" query performed after D2 — a later event silently rewriting an earlier,
already-reported historical truth.

### Alternatives compared

| Option | Description | Verdict |
|---|---|---|
| **A — Voiding is always a dated, linked Correction Entry (a pure MP-07 reversal, zero net effect) — adopted** | No status flip anywhere; the voiding Entry's own Lines, dated at the void's own (later) date, are what remove the effect, and only from that date forward, via the ordinary "date <= D" filter every Entry already uses | **Adopted.** Requires no new machinery — MP-09 gets *simpler* (one fewer special case), not more complex, and naturally produces correct prospective-only semantics. |
| B — Keep VOID as a distinct status; make MP-09 filter on the void's *effective date* instead of current status | Preserves a conceptually separate Void mechanism | **Rejected.** Leaves an unresolved sub-question the option doesn't itself answer: is "effective date" the void event's date (correct) or the original entry's date (retroactive — reintroduces the same rewrite problem, relocated)? Requires new date-tracking machinery Option A does not need. |

### Why Option A is preferred on more than just "less code"

Prospective-only semantics (a void takes effect when recorded, never retroactively) is the
only reading consistent with "a report issued as of D1 reflected the truth as of D1" — and
Option A produces this automatically, as a structural consequence of using the same date
filter every other Entry uses, rather than as a separately-designed rule that could drift out
of sync (which is exactly the class of defect that produced this finding in the first place).

### What changed

`B04` §2 (VOIDED redefined), §3 (Voided event corrected), §5 (rewritten — void is always a
linked correction) · `B07` (no entity change — Correction Link's existing cardinality rule
already covers this) · `B08` MP-09 (status-based exclusion removed entirely) · `B05` BINV-11
(new invariant) · `B13` DT-07 (new) · `B15` §3a (new).

## 4. CORR-B04 — Propagation Check

Every artifact listed in the audit's "Affected artifacts at minimum" for all three findings
was updated (§1–§3 above). Additional propagation performed beyond the audit's minimum list,
found by searching for downstream dependents:

- `B12` — AD-04/AD-07 amended with a note that the mechanism was corrected while the
  objective/measurement criterion are unchanged (the fix corrects *how* the goal is achieved,
  not *what* the goal is).
- `B16` — §13 addendum added, honestly recording that the internal red-team review did not
  catch any of these three defects, despite genuinely catching six others.
- `F`, `G`, `H` — updated below (§6).
- Session closure — new corrective-round closure written (see SESSION_ARCHIVE).

No artifact was found asserting a claim dependent on the corrected wording that was missed —
verified by re-reading every B0x file's cross-references to BINV-06, BINV-07, MP-02, MP-09,
period-close, reopen, and VOID after making the edits above.

## 5. CORR-B05 — Focused Red-Team Regression

See [B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md).

## 6. Six Assumptions — Status After This Round

Per explicit instruction, not escalated to Boss during this round:

```
1. Rounding method .................................. OPEN, unchanged
2. Period close / Consumption ....................... REVISED (see B15 §6) — the internal
                                                        contradiction is fixed; a narrower
                                                        residual question remains open
3. COA template/instance ............................. OPEN, unchanged
4. Broad audit tamper-evidence scope .................. OPEN, unchanged
5. Correction shape flexibility ....................... OPEN, unchanged (Void, B13 DT-07,
                                                        is now understood as an instance of
                                                        this same flexibility, not a new
                                                        open question)
6. CO-02/CO-06 coupling ............................... OPEN, unchanged
```

**No assumption was resolved by Team B fiat. Assumption #2's revision was a correction of an
internally contradictory design, not a judgment call Team B made on Boss's behalf — the audit
itself required this, distinguishing it from the other five, which remain genuine open
choices.**
