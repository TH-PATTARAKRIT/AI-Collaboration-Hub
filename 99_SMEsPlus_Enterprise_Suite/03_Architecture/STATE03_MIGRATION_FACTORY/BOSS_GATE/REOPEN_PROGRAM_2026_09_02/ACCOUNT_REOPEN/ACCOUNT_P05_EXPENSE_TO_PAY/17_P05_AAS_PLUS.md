# 17 — P05 AAS+ CONSOLIDATION

`LAYER 2 — AUDIT QUARANTINE` — except **§6, which is Layer 1** and is the only part of this package
that may be transcribed into a Team B reference deliverable.

AAS+ consolidates **without forced consensus**. Where the four experts and the primary research
disagree, the disagreement is recorded and adjudicated on evidence, not reconciled by averaging.

## 1. What the Reference Actually Is, for P05

Stated plainly, because the design consequence follows from it:

> The reference platform has **an expense-claim system**. It does not have an expense-to-pay *process*.
> Around that claim system, three custom modules were bolted on to supply petty cash, employee
> advances and Thai withholding tax. **All three are structurally broken in ways that leave the
> ledger wrong rather than raising an error.**

| Capability | Reference status |
|---|---|
| Employee claim → vendor bill → reimbursement | Present and coherent, with the defects at `10 §1-2` |
| Company-paid expense | Present, structurally different from the above (per-line payments, no lock-aware date, core payable/receivable check disabled) |
| Petty cash | Present as a master record and two balance controls; **its GL redirection and its journal routing are both dead code**, and its tests cannot execute |
| Employee advance | Present; recognises **expense** at disbursement, has **no** integration with the claim system, and both liquidation paths can silently no-op |
| Thai WHT | Present **twice**, in two mutually unaware subsystems that fill the same statutory return from different data |
| Prepaid / accrued / employee receivable / corporate-card clearing | Absent |

## 2. Positions Held Jointly

These survived challenge from at least one adversarial reviewer and are the package's load-bearing
conclusions.

| ID | Position | Basis |
|---|---|---|
| `AP-01` | **The accounting event owner is the approval transition**, executed under `sudo()` by a user explicitly not required to hold accounting rights. | `03 §1`, Expert 1 confirmed |
| `AP-02` | **The claim↔entry relation cannot serve as a reconciliation key.** Four code paths sever it; the guard against partial deletion reads the very field the other three have already cleared. | `08 §3`, Expert 1 confirmed and extended |
| `AP-03` | **Ledger-material expense fields remain writable after posting**, with no propagation, and the apparent model-side guard is an onchange never registered as an inverse. | `11 C-20`, Expert 1 strengthened |
| `AP-04` | **Petty-cash disbursement does not touch the petty-cash account.** Two independent dead paths; zero effective test coverage. | `05 §6`, Expert 2 on four limbs |
| `AP-05` | **An employee advance is recognised as expense at disbursement**, by shipped default, with no receivable and no link to the claim system. | `05 §3`, `02 §3`, Expert 3 |
| `AP-06` | **A hashed, inalterable journal entry can be forced to `cancel`** from a non-accounting document, with reconciliation partials surviving. | `10 EC-13a`, Expert 3 |
| `AP-07` | **Thai WHT is implemented twice and the two implementations disagree**; the custom stack's withholding is invisible to the enterprise PND CSV export. | `07 §2`, Expert 4 |
| `AP-08` | **WHT applicability follows the payment-mode toggle, not the payee.** | `07 §4`, Expert 4 |
| `AP-09` | **Six of eight directive expense classes are absent or conflated.** P05 is predominantly a design problem, not a transfer problem. | `02 §6` |
| `AP-10` | **No cross-document duplicate is detected.** Every duplicate control operates inside the expense document family; the advance system and the claim system cannot see each other at all. | `09 §3`, Expert 3 class **A** |

## 3. Non-Consensus — Recorded, Not Resolved

| ID | Disagreement | Positions | AAS+ disposition |
|---|---|---|---|
| `NC+01` | Severity of `F-05`'s reassigned recordset | Primary research: a defect discarding employee bills. Expert 2: real, but no caller in `ENT18` consumes the return value, so the blast radius is the return value only. | **Expert 2 governs** — a defect whose only consumer is unused is a latent defect. Recorded as latent, not live. `AAS+ does not average the two.` |
| `NC+02` | Whether `F-06`'s reachability matters | Expert 3: neither button is reachable from the documented happy path. Also Expert 3: `state` has no ORM guard, so a plain write re-exposes the path. | **Both hold.** The UI path is closed; the API path is open. Recorded as *"not reachable by a user following the UI; reachable by anything else"* — the distinction is load-bearing for a SaaS product with an API. |
| `NC+03` | Whether `TX-20`'s UI contradiction is a live defect | Expert 4: code defect class `A`; rendered outcome class `D`, not executed. | **Held at `D`.** AAS+ declines to promote it. Closing it needs runtime (`20 U-02`). |
| `NC+04` | Whether the petty-cash balance leak is a company-isolation failure | Primary research: balance sums across all companies. Expert 2: the compute is not `sudo()`, so it **is** filtered; the real effect is per-user divergence, and the genuine unscoped access is elsewhere. | **Expert 2 governs.** The primary research's version is withdrawn; `TZ-02` is re-based on Expert 2's citation. |
| `NC+05` | Whether `account_disallowed_expenses` is in P05's scope at all | It is `auto_install` with `account_reports`, so it is probably present; but it has **no** connection to the expense path. | **Recorded as present-but-unconnected.** It does not close the `tax non-deductible` requirement; `TX-24` stands. |

## 4. The Veto

> **`AASV-01` — AAS+ VETOES ANY IMPLEMENTATION START ON P05.**

Not because the research is thin, but because of what it found:

1. **Thirteen tolerance-zero boundaries are open**, seven of them raised by independent review. `EC-04`
   forbids a conditional advance past any one of them.
2. **Five gating unknowns remain** (`20 §2`), the first of which — which modules are actually deployed —
   makes every custom-module finding conditional. A design built on the wrong conditional is worse
   than no design.
3. **`EC-07`'s counter has not started** (`16 §6`). Pass one produced 60 new material findings, a new
   material population and 7 new tolerance-zero boundaries.
4. **The primary research was corrected on 12 of its 32 findings**, every correction from independent
   review. A body of work with that correction rate has not converged.

The veto is on *implementation*. It is **not** on the design input at §6, which is Boss-decidable now.

## 5. What Is Safe to Rely On

| Reliance | Status |
|---|---|
| The ten positions at §2 | **Reliable** — each survived at least one adversarial attempt to disprove it |
| The negative claims at `21` | **Reliable within their stated scopes only.** No `B`/`C`/`D` was upgraded. |
| The GL matrices at `05` | **Reliable for the two core branches**; the petty-cash row carries Expert 2's stated classes and no higher |
| Any statement about the **deployed** system | **NOT reliable** — `20 U-01` |
| Any statement resting on runtime behaviour | **NOT reliable** — `20 U-02`; all such claims are marked `SUPPORTED INTERPRETATION` |
| Any Thai statutory conclusion | **NOT asserted.** `HOLD / EVIDENCE REQUIRED` throughout |

## 6. LAYER 1 — CLEAN-ROOM DESIGN INPUT

> **This section only** may be transcribed into a reference package. It contains no vendor model,
> field, path, method or menu name. It states business requirements derived from what the research
> established, not from how the reference implemented it.

### 6.1 Required Distinctions

An expense-to-pay design must type these separately, because conflating any pair was the direct cause
of a defect found in this research:

1. **Who funded the cost first** — the employee, the business, a cash float, or a card.
2. **What kind of cost it is** — direct, prepaid, accrued.
3. **Who is owed, and in what character** — an employee owed a reimbursement is not a supplier owed an
   invoice, even where both are settled the same way.
4. **Whether money has moved yet.**

The reference types only the first, and derives the rest from the account a cost happens to land in.

### 6.2 Required Positions

| ID | Requirement | Why — from evidence |
|---|---|---|
| `DI-01` | **A cash advance creates an asset — a receivable from the employee — never an expense.** Expense is recognised when the cost is evidenced, not when money is handed over. | The reference recognises expense at disbursement by shipped default, and the only universally available clearing route books a cash receipt that never happened. |
| `DI-02` | **Employee obligations are held distinctly from supplier obligations**, at ledger level and not only by counterparty identity. | Three of five payable kinds land in one account; separating them requires a counterparty report rather than a balance. |
| `DI-03` | **A cash float is company-owned by construction.** Its balance is a company's cash position and must be scoped, queried and constrained as such; its uniqueness is per company, never global. | Derived from the object's own financial semantics under the scope-aware rule, not assumed. |
| `DI-04` | **Authorising a cost and recording it are two events with two owners.** The authoriser must not be the emitter of the ledger fact. | The reference emits the entry from the approval transition, elevated, by a user not required to hold accounting rights. |
| `DI-05` | **Every accounting fact carries an immutable identity that no later action can sever.** Correction is by a new, linked fact — never by detaching, deleting or force-cancelling an existing one. | Four paths sever the claim↔entry link; a hashed entry can be force-cancelled; refusal after approval destroys the draft entry outright. |
| `DI-06` | **A posted fact is closed to amendment.** Where a business change is needed, it produces a new fact. | Amount, currency, date, product and quantity remain writable after posting with no propagation. |
| `DI-07` | **An entry's date derives from a document fact, never from the clock**, and never steps over a closed period to find an open one. | Two of three date branches use "today"; one actively computes the first open period after the lock; one custom path uses the server's date, not the user's. |
| `DI-08` | **Duplicate control keys on the cost event, not on the document.** | Every duplicate control found operates inside one document family; three cross-document duplicate classes are undetected, one of them structurally. |
| `DI-09` | **Statutory reference data is platform-scoped.** Only its ledger mapping is company-scoped. | Conflating them forces the statutory rate to be duplicated per company with nothing keeping the copies equal, and the duplication mechanism was itself found defective. |
| `DI-10` | **Tax withheld at settlement is a function of the payee and the nature of the payment, never of how the cost was funded.** | Withholding is currently reachable on one funding branch and structurally unreachable on the other. |
| `DI-11` | **One statutory obligation has exactly one system of record.** | Two implementations fill the same return from different data and different counterparty identifiers, and one silently omits the other's amounts. |
| `DI-12` | **A control that cannot be shown to execute is not a control.** Every declared control needs a proof of execution and a test that fails when it is removed. | A guard listing protected fields did not contain them; two GL redirections were dead; a computed permission was never consulted; a declared flag had no consumer; a module's tests could not run at all. |
| `DI-13` | **An operation determines its executing scope before it resolves its authoriser, its accounts, or its counterparty.** Missing required scope denies; it never resolves to an arbitrary first match. | Approver, float record and expense account were each resolved by "first match wins" with no scope assertion. |
| `DI-14` | **A settlement is a single fact.** The amount paid, the amount withheld and the amount printed on the advice are one number each, derived from one source. | Those three are currently three unreconciled numbers, and the printed one is computed from a field that corrupts across a recompute batch. |
| `DI-15` | **Analytic attribution attaches to the cost, not to one leg of its entry**, and survives every funding route. | Attribution reaches the debit line only, and the entire advance and float chain carries none. |

### 6.3 Explicitly Out of Scope for Transfer

The reference supplies **no** usable pattern for: prepaid expense, accrued expense, employee
receivable, corporate-card clearing, cross-document duplicate detection, or a withholding lifecycle
that survives reversal. These are **new design**, and must not be presented to Team B as a transfer.
