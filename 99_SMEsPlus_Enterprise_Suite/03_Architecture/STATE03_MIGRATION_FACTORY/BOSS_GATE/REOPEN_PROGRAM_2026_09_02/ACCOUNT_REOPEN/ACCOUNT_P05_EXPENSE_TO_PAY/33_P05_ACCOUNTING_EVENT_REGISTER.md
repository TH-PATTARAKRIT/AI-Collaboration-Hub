# 33 — P05 ACCOUNTING EVENT REGISTER (CONSOLIDATED, WITH DEPLOYMENT REACH)

`LAYER 2 — AUDIT QUARANTINE`
Supersedes `03 §2` as the citable accounting-event register; `03` is retained as audit lineage.

| ID | Accounting event | Emitted by | Entry state at emission | Date used | Lock consulted at derivation | Reach |
|---|---|---|---|---|---|---|
| `AE-01` | Employee claim recognised | approval → bill preparation | **draft** | derived `accounting_date` | **Yes** (third branch only) | LIVE |
| `AE-02` | Employee claim posted | post action | posted | unchanged | yes (core, at post) | LIVE |
| `AE-03` | Company-paid cost recognised | approval → per-line payment preparation | **draft** | the expense date | **No** | LIVE |
| `AE-04` | Company-paid cost posted | post action via the payment | posted | unchanged | yes (core, at post) | LIVE |
| `AE-05` | Advance recognised **and posted in one action** | advance request button | **posted immediately** | **server date** (`date.today()`) | yes (core) | LATENT |
| `AE-06` | Advance liquidated vs vendor bill | reconcile wizard | posted immediately | the vendor bill's date | yes (core) | LATENT |
| `AE-07` | Advance cash return | clearing wizard | posted immediately | wizard date | yes (core) | LATENT |
| `AE-08` | Float top-up | manual bill | posted on user action | move date | yes (core) | LATENT |
| `AE-09` | **WHT withheld** | payment register write-off line | with the payment | payment date | yes (core) | **LIVE (4 of 4 distinct DBs)** |
| `AE-10` | Claim reversal | reverse-moves | reversal posted | context today | yes (core) | LIVE |
| `AE-11` | Draft entry destroyed on refusal | refuse action | — | — | n/a | LIVE |
| `AE-12` | Entry force-cancelled from a non-accounting document | raw `state` write | `cancel` | — | **lock yes; hash lock NO** | LATENT (trigger) / **LIVE (core gap)** |
| `AE-13` | **Vendor down payment recognised and posted** *(new)* | purchase advance wizard, under `sudo()` | **posted immediately** | wizard date | yes (core) | **LIVE (4 of 4 distinct DBs)** |
| `AE-14` | **WHT certificate issued** *(document, no GL effect)* | certificate wizard | n/a | the printed `date` is **correct in 97.79%**; the column named `payment_date` is a **create-time artefact in 100%** of 5,201 rows (corrected — `39 RE-10`) | n/a | **LIVE (4 of 4 distinct DBs)** |

## 1. Recognition Timing — the position, unchanged and reviewer-confirmed

> Expense is recognised at **approval**, not at posting, not at payment, and not at the date the cost
> was incurred. The approval transition is the accounting event owner, it runs elevated, and the
> document state is *derived from* the entries rather than driving them.

`hr_expense_sheet.py:711-721, 746-760, 264-309`. Confirmed exact by AAS-03 Expert 1 (`16 §4.1`).

## 2. Date Derivation Defects, by reach

| ID | Defect | Reach |
|---|---|---|
| `RI-06` | Advance bill dated by the **server's** date, not the user's context date — shifts period assignment across a UTC offset at month and year boundaries | LATENT |
| `03 §3.1` | Claim accounting date derived from the **clock** in two of three branches; the third computes the first open period **after** the lock and books there | LIVE |
| `03 §3.3` | On the company-paid branch `date_maturity` falls to **today** while the entry date is the expense date — ageing and entry date diverge by construction | LIVE |
| `TX-20` | **Corrected (`39 RE-10`).** The certificate's printed date is sound; the `payment_date` column is a create-time artefact in 100% of 5,201 rows and carries no payment information | **LIVE, empirically confirmed in corrected form** |

## 3. Correction / Reversal Lifecycle Coverage

| Operation | Behaviour | Reach |
|---|---|---|
| `CREATE` / `CONFIRM` / `POST` | traced (`AE-01`..`AE-04`) | LIVE |
| `PARTIAL` | partial payment only; no partial approval — approval is whole-sheet | LIVE |
| `CANCEL` | **three different cancels with three different semantics** (`10 EC-11`) | LIVE / LATENT |
| `REVERSE` | reverses non-draft with `cancel=True`, **unlinks draft outright**, and nulls the back-link first | LIVE |
| `REFUND` | standard credit note on the vendor path | LIVE |
| `CORRECT` | **no correction event exists** — correction is by mutation of the source record with no propagation (`TZ-03`) | LIVE |
| `BACKDATE` | employee branch computes the date *away* from a back-dated cost; company branch takes it raw and fails at post | LIVE |
| `SETTLE` / `RECONCILE` | traced; claim↔entry link severable by four paths | LIVE |
| `CLOSE` | no close routine in the P05 surface (`21 NC-11`, class B); a period can close with draft expense entries | LIVE |
| `REOPEN` | not traced — class **C** | — |
| `LOCKED PERIOD` | enforcement symmetric at post; **derivation** lock-aware on one branch only; hash lock defeatable (`AE-12`) | LIVE |
| **WHT reversal** | **no hook exists in any WHT module** — class **A** (`21 NC-14`). A `done` certificate can outlive a cancelled WHT line. | **LIVE (4 of 4 distinct DBs)** |
