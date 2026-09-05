# P06_PAYMENT_BANK_RECONCILIATION_STATE_MODEL.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C05)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Supersedes nothing.** This file *derives the semantic state model* from the findings already established in `01_`, `02_`, `03_` and `04_`. Those files remain the evidence; this file is the model.

---

## 1. The seven states the process actually needs

The prompt requires these determined separately. They are listed with what the reference supplies for each.

| # | State the process needs | Reference field | Verdict |
|---|---|---|---|
| S1 | **Payment state** — what we intend and have done | `account.payment.state` (5 values) | exists, but computed from S6/S7 |
| S2 | **Accounting posting state** | `account.move.state` (3 values) | exists, but driven *by* S1 |
| S3 | **Bank transaction state** — the bank's own item | *none* | **absent** |
| S4 | **Bank statement presence** — is there a statement line at all | derivable from `statement_line_id` | implicit only |
| S5 | **Match state** — this payment corresponds to that bank item | `is_matched` | **present but false-positive by configuration** |
| S6 | **Settlement state** — the obligation is discharged | `account.move.payment_state` (7 values) | exists, mutable by two writers |
| S7 | **Reconciliation state** — the ledger legs are squared | `is_reconciled` / partials | exists, terminal branch defaults true |

**Four of seven are supplied cleanly. S3 is absent. S5 is unreliable. S1, S2, S6, S7 are mutually entangled.**

---

## 2. The entanglement, drawn

```
   S1 payment.state ──depends on──> S7 (liquidity residual)
        │                            ▲
        │ write() generates+posts    │
        ▼                            │
   S2 move.state                     │
        │                            │
        └──> S6 move.payment_state ──┘   (depends on matched_payment_ids.state = S1)

   S5 is_matched ──> feeds S6's in_payment-vs-paid decision
        ▲
        └── set True by CONFIGURATION in 2 of 3 branches

   S3 bank transaction state  ── DOES NOT EXIST ──
   S4 statement presence      ── implicit, never asserted ──
```

**Evidence for each arrow** is in `01_P06_PAYMENT_STATE_MODEL.md` findings PSM-F-01 to PSM-F-05 and PSM-F-08 to PSM-F-13. The two cycles — S1↔S7 and S1↔S6 — are the structural finding.

---

## 3. The `is_matched` test, executed

The prompt requires: *test whether `is_matched=True` can exist without a statement; if yes, determine exactly what the flag means, not what its label implies.*

**Test performed:** static trace of **every** assignment to `is_matched` in `$V18E/account/models/account_payment.py:433-455`, re-executed at the supplemental round with the source printed line-by-line.

**Structure: FOUR top-level branches (`:436`, `:439`, `:442`, `:445`), the fourth splitting into two — FIVE assignment sites in total.**

| Site | Line | Condition | `is_matched` | Statement required? |
|---|---|---|---|---|
| 1 | `:438` | `not pay.outstanding_account_id` | `= pay.state == 'paid'` | **no — circular, copied from S1** |
| 2 | `:441` | `not currency_id or not id or not move_id` | `= False` | n/a |
| 3 | `:444` | `currency_id.is_zero(pay.amount)` | `= True` **unconditionally** | **no — zero amount** |
| 4 | `:450` | `journal.default_account_id in liquidity_lines.account_id` | `= True` **unconditionally** | **no — configuration** |
| 5 | `:452` | otherwise | `= currency.is_zero(sum(liquidity residual))` | **yes, indirectly** |

**ANSWER: YES.** Of five assignment sites, **two set `is_matched = True` unconditionally with no bank statement in existence** (sites 3 and 4), **one sets it circularly from the payment's own state** (site 1), one always sets False, and **only site 5 tests anything resembling a bank match** — and even that tests *liquidity-line reconciliation*, which a manual journal entry can also produce.

> **CORRECTION (REV-E-11).** An earlier state of this table listed **three** branches and silently omitted `:439-441`. The correct structure is four branches / five assignment sites, and P02 independently published "four branches" over the wider range `:428-456`. The undercount was found when a peer's citation was compared against this package's own. **The finding is unchanged in direction and stronger in degree** — five sites, of which three can assert a match with no statement.

**What the flag actually means, stated without reference to its label:**

> **`is_matched` means: "the liquidity leg of this payment has no residual, OR this payment was configured in a way that makes a residual impossible."**

It is a **residual-exhaustion flag**, not a confirmation flag. Its label — *"Is Matched With a Bank Statement"* — asserts a fact about the external world that the field never tests.
**Classification: FACT VERIFIED.** This is the evidence base for `P06-B-06` and contradiction `C-01`.

---

## 4. The semantic state machine P06 must specify

> **CLASSIFICATION (amended by AAS-03 E1-C-03): this section is a `DESIGN CANDIDATE`, not `FACT VERIFIED`.** The four facts, their owners and the five invariants are P06's proposal derived from business semantics. Only the *gap analysis* against the reference (the "Present in reference?" column) is evidenced.

Derived from business semantics, **not** transcribed from the reference. Per the clean-room rule, what transfers is the accounting requirement, not the implementation.

**Four independent facts, each separately written, each with an owner:**

| Fact | Owner | Written by | May never be derived from |
|---|---|---|---|
| **INTENT** — an obligation is due to be settled, for an amount, to a party, on a date | the originating process (P01/P02/P05) | that process | any downstream fact |
| **INSTRUCTION** — the business has irrevocably told a bank or provider to move money | P06 | the instruction act | the accounting |
| **CONFIRMATION** — an external party asserts the money moved | **external**, recorded by P06 | ingestion of a bank event | configuration, ever |
| **SETTLEMENT** — the obligation is discharged in the ledger | P06, applied to the obligation | reconciliation of the ledger legs | the payment record alone |

**Required transitions, with the reference's gap noted:**

| Transition | Present in reference? |
|---|---|
| intent → instructed | only as the boolean `is_sent` (SSM-F-05) |
| instructed → **irrevocable** | **NOT FOUND** — no state means "past the point of no return" |
| instructed → confirmed | **NOT FOUND** — no confirmation fact exists |
| instructed → **rejected by the bank** | `action_reject`, a bare assignment with no cause and no unwind (SSM-F-03) |
| confirmed → settled | reconciliation |
| settled → **unsettled by a returned item** | **NOT FOUND** in v18; present in a v14 custom module |
| settled → corrected | destroys the reconciliation silently (attack A5) |

**Non-negotiable invariants for the target:**
1. CONFIRMATION may be written only by an ingested external bank event. No configuration path may set it.
2. SETTLEMENT may not be asserted while a ledger residual stands (PSM-F-13).
3. INSTRUCTION must be a state, not a flag, and must have an irrevocable point.
4. Every state carries its writer, its timestamp, and — for terminal negatives — its cause.
5. No state may be computed from another. Derived *views* are permitted; derived *facts* are not.

---

## 5. Why the reference model cannot simply be corrected into this shape

Two structural reasons, both evidenced:

**First: the ingestion layer fuses two facts at creation.** A bank statement line **is** a journal entry by delegation (`_inherits`), and `create` force-posts it (BER-F-01). There is no "observed but not yet accounted" state, so CONFIRMATION and the accounting effect cannot be separated after the fact — they are the same record.

**Second: the reconciliation act destroys its own input.** Validating a match clears and rebuilds every line of the statement entry (RM-F-01). A model that needs to record *what was matched to what, and what it looked like before* cannot be built on an operation that deletes both.

**Consequence for the target: the bank-event object and the accounting entry must be separate records from the outset, and matching must be an additive record rather than a rewrite.** These are the two decisions everything else in P06 depends on.

---

## 6. Status

**CP-C05 COMPLETE.** The `is_matched` test is executed and answered. No blocker closes on this file alone — it converts `P06-B-06` from a gap statement into a specified requirement, which is what the handoff needs.

| Item | Status |
|---|---|
| `P06-B-06` no bank-confirmation fact | **remains open — HOLD — DESIGN DECISION REQUIRED**, now with a specified target semantics |
| `P06-B-04` four payment-intent entry points | remains open; the INTENT/INSTRUCTION split above is the closure path |
| `P06-B-05` posting-state authorship | remains open; §5 explains why it cannot be resolved inside the reference shape |
| C-01 | **evidence strengthened** — the flag's meaning is now stated positively, not only as a contradiction |

---

# End
