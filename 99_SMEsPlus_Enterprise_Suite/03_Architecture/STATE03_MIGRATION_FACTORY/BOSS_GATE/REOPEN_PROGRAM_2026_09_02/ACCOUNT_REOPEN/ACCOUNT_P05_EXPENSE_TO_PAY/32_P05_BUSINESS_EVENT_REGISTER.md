# 32 — P05 BUSINESS EVENT REGISTER (CONSOLIDATED, WITH DEPLOYMENT REACH)

`LAYER 2 — AUDIT QUARANTINE`
Supersedes `01 §2` as the citable business-event register. `01 §2` is retained as audit lineage.
The added column is `REACH`, derived from `24 §3`: `LIVE` = the owning module is installed in at
least one evidenced deployment; `LATENT` = confirmed in source, installed in none.

Invariant tested per row: `ONE BUSINESS FACT → ONE CANONICAL EVENT OWNER → ONE ACCOUNTING EFFECT PATH`.

| ID | Business event | Canonical event owner | Trigger | Accounting effect | Owner integrity | Reach |
|---|---|---|---|---|---|---|
| `BE-01` | Expense request raised (pre-spend authorisation) | advance request | user submits | **none** | OK | LATENT |
| `BE-02` | Expense request approved | advance request | named approver | **none** | OK | LATENT |
| `BE-03` | Advance disbursement authorised | advance request | `button_post_bill` | **creates AND posts a vendor bill** | **`EX-01`** | LATENT |
| `BE-04` | Advance paid to employee | payment | payment registration | settles employee payable | OK | LATENT |
| `BE-05` | Employee incurs cost, obtains evidence | expense line | manual / e-mail / OCR | **none** | OK | LIVE |
| `BE-06` | Expenses grouped into a claim | expense report | submit | **none** | OK | LIVE |
| `BE-07` | Claim approved | expense report | `_do_approve` | **creates the journal entry (draft)** | **`EX-02`** | LIVE |
| `BE-08` | Claim posted | entry / payment | `action_sheet_move_post` | posts the entry | OK | LIVE |
| `BE-09` | Employee reimbursed | payment | payment registration | settles employee payable | OK | LIVE |
| `BE-10` | Company-paid cost logged | payment, **one per line** | `_do_approve` | outstanding-account credit | **`EX-03`** | LIVE |
| `BE-11` | Petty cash float replenished | entry flagged as float top-up | manual bill | debits the float account | OK | LATENT |
| `BE-12` | Petty cash spent | expense line, mode `petty_cash` | claim approval | **credits the EMPLOYEE payable, not the float** | **`EX-04` / `TZ-01`** | LATENT |
| `BE-13` | Advance liquidated against actual cost | reconcile wizard | manual | offsets advance vs vendor bill | OK | LATENT |
| `BE-14` | Unused advance returned in cash | clearing wizard | manual | DR cash / CR the first advance line's account | **`EX-05` / `TZ-13`** | LATENT |
| `BE-15` | WHT withheld at settlement | payment register | payment registration | write-off line to the WHT account | OK | **LIVE (4 of 4 distinct DBs)** |
| `BE-16` | WHT certificate issued | certificate | manual wizard | **none** (document only) | **duplicate-permitting — `TX-13`** | **LIVE (4 of 4 distinct DBs)** |
| `BE-17` | Claim refused after approval | expense report | approver | **deletes the draft entry** | **`EX-06`** | LIVE |
| `BE-18` | Claim reset to draft after posting | expense report | user with reset right | reverses, then **detaches** entries | **`EX-07`** | LIVE |
| `BE-19` | Advance request reset / rejected after billing | advance request | requester / approver | **raw `state='cancel'` write on posted entries** | **`EX-08` / `TZ-05`** | LATENT |
| `BE-20` | Expense line edited after posting | expense line | any editor | **no propagation to the posted entry** | **`EX-09` / `TZ-03`** | LIVE |
| `BE-21` | **Vendor down payment billed** *(new — evidenced live)* | purchase advance wizard | wizard | **creates AND posts a vendor bill under `sudo()`; never deducted from the final bill** | **`TZ-11`, `TZ-12`, `SC-02`** | **LIVE (4 of 4 distinct DBs)** |

## 1. Single-Owner Violations by Reach

| Reach | Violations |
|---|---|
| **LIVE** | `EX-02` (approval emits the ledger fact), `EX-03` (one claim → N accounting objects), `EX-06` (refusal destroys the draft entry), `EX-07` (reset orphans entries), `EX-09` (post-posting mutation), plus `BE-21`'s trio |
| **LATENT** | `EX-01` (advance is requisition + approval + accounting in one document), `EX-04` (petty cash), `EX-05` (clearing account collapse), `EX-08` (raw state write) |

## 2. Events With No Owner At All

| Missing event | Consequence | Evidence |
|---|---|---|
| Prepaid recognition and amortisation | no mechanism exists in the P05 surface | `21 NC-08`, class B |
| Accrual of an unapproved claim at period end | a period can close with the obligation unrecorded, and with **draft** entries inside it | `21 NC-09`; `08 §4` |
| Employee receivable on an over-advance | the over-advance is a **credit to expense**, not a receivable | `10 EC-08` |
| Corporate-card clearing | no process model; a card **journal type** and **account type** do exist and are reachable from the company-paid path | `21 NC-04` / `NC-E-06` |
| Cross-document duplicate detection | three classes undetected, one structurally | `09 §3`; `26 TZ-06` |
