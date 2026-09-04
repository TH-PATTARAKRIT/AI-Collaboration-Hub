# 28 — P05 HANDOFF COMPLETENESS REGISTER

`LAYER 2 — AUDIT QUARANTINE`
Each element is exactly one of `COMPLETE` · `PARTIAL — with exact missing evidence` ·
`BLOCKED — with exact external blocker` · `NOT APPLICABLE — evidence verified`.
**No "mostly complete" status is used.**

## 1. Register

| # | Element Core Reconciliation needs | Status | Exact missing evidence / blocker |
|---|---|---|---|
| `HE-01` | **Cost by nature** (expense recognised, by account) | **COMPLETE** | Recognition trigger, amount and account-resolution chain are fully traced and reviewer-verified (`03`, `05 §1-2`, `02 §2.1`). Database corroboration: 37,055 vendor bills, 143,811 entries. |
| `HE-02` | **Cost by cost centre / project** | **PARTIAL** | Attribution reaches the expense **debit line only**; tax lines and the payable/outstanding credit line carry none (`06 §2`, class A within the five files). Missing: a design position placing attribution on the cost event rather than one leg — `17 §6 DI-15`. Routed to P09 (`30 §5`). |
| `HE-03` | **Employee obligation balance** | **PARTIAL** | Distinguishable by **counterparty only**, never by account: the employee's payable resolves to `res.partner.property_account_payable_id`, the same field a supplier uses (`04 §2`, `05 §1`). Missing: a design position separating employee from supplier obligations at ledger level — `17 §6 DI-02`. |
| `HE-04` | **Supplier obligation balance** | **COMPLETE** | Standard vendor-bill payable; traced and reviewer-verified. |
| `HE-05` | **Advance outstanding balance** | **BLOCKED** | External blocker: **no advance asset account exists on this path** — disbursement debits a P&L expense account, and it is the shipped default (`05 §3 GL-04`, `10 E3-01`). There is nothing to report a balance from. Unblocks only on Boss decision `BD-02`. Module is latent in all six registries (`24 §3`). |
| `HE-06` | **Float (petty cash) position** | **BLOCKED** | External blocker: the float account is never credited by spending against it, so the balance is structurally overstated and its control is a one-way ratchet (`05 §6`, upheld on four independent lines). Unblocks only on a SMEsPlus design position. Module is latent in all six registries. |
| `HE-07` | **Withholding payable and certificate basis** | **PARTIAL** | Mechanically traced end to end (`07 §3`) and **empirically evidenced at production scale** (5,201 certificates, `25 §3`). Missing: (a) which of the **two installed subsystems** is the system of record — P07/P11 (`30 §3`, `H-P07-1`); (b) all statutory determinations, `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| `HE-08` | **Non-deductible / add-back basis** | **NOT APPLICABLE — EVIDENCE VERIFIED** | `account_disallowed_expenses` is **report-only** — a read-only SQL aggregation with no write path to any journal (class **A**) — and has **no connection** to the expense path (class **A**) (`07 §6`). It is additionally **installed in no registry** (`24 §3`). There is no such basis to hand over, and that is now evidenced rather than assumed. The derived requirement (does a Thai add-back obligation need more?) is P07's. |
| `HE-09` | **Claim-to-entry audit trail** | **BLOCKED** | External blocker: four code paths sever the link and the guard against partial deletion reads the field the other three have cleared (`08 §3`, `30 §4 H-P08-2`). Unblocks only on the platform-level event-identity primitive routed to P11 (`H-P11-2`). Not P05's to close. |
| `HE-10` | **Period-close completeness of unrecorded obligations** | **BLOCKED** | External blocker: nothing accrues an unapproved claim, and a period can close containing **draft** expense entries because entries are created at approval and posted later (`03 §1`, `08 §4`). No accrual mechanism exists in the P05 surface (`21 NC-09`, class B). Unblocks on Boss decision `BD-04` and P08's period-control position. |

## 2. Tally

| Status | Count |
|---|---|
| `COMPLETE` | **2** (`HE-01`, `HE-04`) |
| `PARTIAL` | **3** (`HE-02`, `HE-03`, `HE-07`) |
| `BLOCKED` | **4** (`HE-05`, `HE-06`, `HE-09`, `HE-10`) |
| `NOT APPLICABLE — EVIDENCE VERIFIED` | **1** (`HE-08`) |

## 3. Delta Against the Prior Package

The prior statement was *"six of ten handoff elements are unsuppliable or partial"* (`19 §6`).
That count is **unchanged at six** — but its composition has moved, and the movement is the point:

| Element | Was | Now | Why |
|---|---|---|---|
| `HE-08` non-deductible | "No" — reported as a gap | **`NOT APPLICABLE — EVIDENCE VERIFIED`** | Expert 4 settled the mechanism (report-only, class A) and `24` showed the module is installed nowhere. The gap was real but it is not P05's to fill, and it is now evidenced rather than asserted. |
| `HE-05`, `HE-06` | "No" | **`BLOCKED` with a named unblock condition** | The blocker is now precisely stated as a design decision (`BD-02`) or a design position, not a research gap. |
| `HE-09`, `HE-10` | "No" | **`BLOCKED`, routed to P11 / P08** | Ownership determined: these are not P05-closable. |
| `HE-07` | "Partial" | **`PARTIAL`, with production evidence added** | 5,201 certificates measured; the residue is narrowed to the system-of-record question and statute. |

**Net: no element moved to `COMPLETE`, but every non-complete element now has an exact missing item
and a named owner.** That is the closure this continuation could legitimately deliver; it is not the
same as delivering readiness.

## 4. Consequence for Core Reconciliation

P11 should plan on receiving **two complete elements, three partial, four blocked, one not
applicable** — not a complete expense subledger. Specifically, P11 cannot expect from P05: an advance
receivable balance, a float position, a claim-to-entry audit trail, or period-close completeness of
unrecorded obligations.
