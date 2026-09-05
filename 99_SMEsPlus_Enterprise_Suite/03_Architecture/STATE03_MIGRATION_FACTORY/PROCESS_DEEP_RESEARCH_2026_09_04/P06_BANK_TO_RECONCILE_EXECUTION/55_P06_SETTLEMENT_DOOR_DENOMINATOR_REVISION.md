# P06_SETTLEMENT_DOOR_DENOMINATOR_REVISION.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S16)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do NOT keep an old denominator after material peer evidence."*

---

## 1. What round 3 said, and why it was imprecise

Round 3 recorded (`35_` PH-F-05, `40_` `P06-B-53`):
> *"**P05 supplies an eighth settlement door P06 did not count.**"*

**Round 3's own revision log already caught half of the problem** (`39_` R-15): *"that is a **settlement** door on a different axis from the seven **ingestion** doors, not an eighth ingestion door."*

**This round establishes the other half: it was not an eighth of anything. P05 had already counted it.**

---

## 2. P05's actual denominator, retrieved verbatim

`08_P05_SETTLEMENT_RECONCILIATION.md` §1 "Settlement Paths" — header `| Path | Instrument | Producer | Reconciles against |`, **seven rows**:

| Path | Instrument | Reconciles against |
|---|---|---|
| `S-01` Employee reimbursement | outbound `account.payment` via the register | the expense bill's payable line |
| `S-02` Company-paid expense | `account.payment` created **at approval** | bank statement, via the outstanding account |
| `S-03` Advance payment to employee | standard outbound payment | the advance bill's payable line |
| `S-04` Advance liquidation vs vendor bill | manual `entry` + `js_assign_outstanding_line` | the vendor bill's payable line |
| **`S-05` Advance cash return** | **manual two-line `entry`, no payment object** | **nothing — see `SR-04`** |
| `S-06` Petty cash float top-up | vendor bill then normal payment | holder payable |
| `S-07` WHT settlement | payment write-off line | see `07` |

**SDD-F-01 — `SR-04` is path 5 of P05's own 7. P05 counted it, named it, and classified it `FACT VERIFIED`.** P06's "eighth door" framing implied P05 had missed it. **P05 had not. P06 had.**

---

## 3. Two denominators, two units — stated so they are never added again

| Denominator | Owner | Unit | Count | Boundary |
|---|---|---|---|---|
| **Bank-event ingestion doors** | **P06** | a way a *bank event* enters `account.bank.statement.line` | **7** | the six `account_bank_statement*` modules + `account_online_synchronization` + core `account`; declared POPULATION/PATTERN/PATH SET/UNIT |
| **Settlement paths** | **P05** | a way an *expense obligation* is settled | **7** | `hr_expense`, `hr_expense_petty_cash`, `scgl_advance_expense_request` only |

**SDD-F-02 — These are different units over different populations. Neither is a subset of the other, and "7 + 1 = 8" was never valid arithmetic.**
This is the **fourth** instance of the `count unit vs population` defect in the P06 programme (after REV-E-05, REV-E-06, REV-E-08). **Recorded as REV-E-12.**

---

## 4. P05's denominator carries a limitation P06 must carry with it

**SDD-F-03 — P05's seven is author-enumerated and unbounded.**
`NOT FOUND` for `POPULATION|PATTERN:|PATH SET|UNIT:|DENOMINATOR` in `08_P05_SETTLEMENT_RECONCILIATION.md`. P05 publishes denominator commands elsewhere in its package (`01_` §17, `13_` §34) but **not for the settlement-path table**. P05 also never writes the word "seven" — the count is the row count of one table.

Its boundary is stated: *"Boundary: `hr_expense`, `hr_expense_petty_cash`, `scgl_advance_expense_request`"* — **three expense modules. It is not a system-wide settlement census.**

**Consequence for P06:** P06 may cite `S-05` as `FACT VERIFIED` — P05 source-links it (`advance_request_reconcile.py:62-92`) and corroborates it internally (`EC-07`). **P06 may not cite "7 settlement paths" as a system denominator.** It is the enumeration of one process's own scope.

---

## 5. The revision

| | Old | New |
|---|---|---|
| P06 ingestion doors | 7 | **7 — unchanged** |
| "Eighth settlement door" | asserted | **WITHDRAWN** |
| `S-05` / `SR-04` | "found by P05, missed by P06" | **`FACT VERIFIED`, path 5 of P05's 7, counted by its owner** |
| `P06-B-53` | *"An eighth settlement door"* | **restated** — see below |
| Denominator discipline | two units merged | **two units, separately declared, never summed** |

**`P06-B-53`, restated:**
> **`P06-B-53` — Cash can move through a bank journal producing no `account.payment` at all (P05 `S-05` / `SR-04`), so it is invisible to payment listings, payment-based reports, and the bank-reconciliation matching model that keys on payments. INHERITED FROM P05, which owns and has counted it. P06 records it because it changes what P06's matching model can see, not because it is a P06 discovery. Flagged for deduplication at P11. Severity to P06: LOW. Severity in P05's register is P05's to set.**

---

## 6. What is genuinely material to P06

Stripped of the denominator error, one real thing remains, and it matters:

**SDD-F-04 — There exists a cash movement through a bank journal with no payment object, and P06's matching model keys on payments.**
`SR-04`: *"The cash movement will **not** appear in payment listings, payment-based reports, or the bank-reconciliation matching model that keys on payments."*

**Consequence:** when that cash lands on a bank statement, the matching engine has no payment to offer as a candidate. The line falls through to suspense or to a manual write-off — **and suspense has no ageing** (`P06-B-18`). So a legitimate cash return becomes unidentified money in an account no standard report ages.

**That is a genuine P06 finding, and it survives the correction intact.** It is the reason the door mattered — not the count.

---

## 7. Requirement

| ID | Requirement |
|---|---|
| `SDD-R-01` | Every movement of cash through a bank or cash journal produces a first-class settlement object. A journal entry that moves cash without one is not permissible. |
| `SDD-R-02` | The matching model keys on the settlement object, not on a payment record, so that every cash movement is matchable regardless of which process produced it. |
| `SDD-R-03` | Denominators from different processes are never summed. Each carries its own POPULATION, PATTERN, PATH SET and UNIT, and cross-process totals are constructed at P11 from the declared units, not from the headline numbers. |
