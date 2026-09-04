# C03 — ACCOUNT_WAVE_A_CONTRADICTED_CLAIMS_REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`

The six research claims contradicted by independent review, each **independently re-examined against
primary source by this session** — not accepted on the reviewer's authority.

Disposition: `CONFIRMED` · `CORRECTED` · `RESCOPED` · `RETRACTED` · `UNKNOWN` · `HOLD`.

---

## `CC-01` — Fiscal year model

| Step | Content |
|---|---|
| **Primary claim** | "A search for a fiscal-year model across the entire 797-module tree returns no result. The fiscal year exists only as two integers on the company." |
| **Search scope** | One grep for the token `account.fiscalyear`, over the addons root |
| **Primary evidence** | An empty result set |
| **Reviewer contradiction** | Expert 1, and independently the challenge unit: the model exists, spelled `account.fiscal.year` |
| **New evidence** | `account_accountant/models/account_fiscal_year.py:11-55` — name, start date, end date, owning company; constraints rejecting an end before a start, rejecting child companies, and rejecting overlaps. Reached via a group and a settings toggle (`views/account_accountant_menuitems.xml:6`). Manager rights are full create/write/delete (`security/ir.model.access.csv:9`). Consumed only at `account_accountant/models/res_company.py:162,185,193` for boundary derivation and at `.../res_currency.py:10` for rate grouping |
| **Corrected claim** | A fiscal-year entity exists as an **optional, fully mutable, deletable calendar override**. It has no state, no close action, no posting, no balance and no link from any entry |
| **Impact** | The dependent conclusion — no year-end closing entry, result computed at report time — **survives and is strengthened**. The negative was load-bearing for nothing; the positive finding beneath it was |
| **Disposition** | **`RESCOPED`** |

---

## `CC-02` — Lock-date re-dating mechanism

| Step | Content |
|---|---|
| **Primary claim** | "On create, an entry dated in a locked period has its date silently rewritten to lock date + 1 day." |
| **Search scope** | `account_move.py` around the located `timedelta(days=1)` expression |
| **Primary evidence** | `account_move.py:3127-3129` |
| **Reviewer contradiction** | Expert 1, Expert 3, Expert 4 and the challenge unit — **all four independently**. The cited lines are inside `copy_data`, the duplication path. The challenge unit issued `VETO-01` |
| **New evidence** | Three mechanisms: `copy_data` (`:3113-3131`) for duplication and reversal; `_compute_date` (`:800-815`) for **non-sale documents, unconditionally, with no lock consulted**; `_post` (`:4933-4936`) when a lock is violated. The rule is `_get_accounting_date` (`:5655-5691`), which returns period-end or today, not lock+1, and branches on a numbering pattern deduced from the journal's highest existing number |
| **Corrected claim** | See `C07` §5. The accounting date is a system-derived value; for non-sale documents the derivation is unconditional and, in the ordinary case, does not return the document date |
| **Impact** | **The finding became more serious.** A tenant with no locks configured still has period attribution altered. This session additionally found a case none of the four reviewers reported: a **current-month** bill takes **today**, not its document date (`C07` §2 consequence B) |
| **Disposition** | **`CORRECTED`** — and the veto is resolved by correction, not dismissal |

---

## `CC-03` — Lock exceptions append-only

| Step | Content |
|---|---|
| **Primary claim** | "Exceptions are append-only — managers may create but not write or delete them." |
| **Search scope** | `security/ir.model.access.csv` rows for the lock-exception model |
| **Primary evidence** | Two access rows, read as granting create but not write |
| **Reviewer contradiction** | Expert 1, and independently the challenge unit |
| **New evidence** | `account_lock_exception.py:258-266` — a revoke action that checks the manager group and then writes `active = False` and an end timestamp **through elevated privilege**, deliberately escalating past the access rule cited as proof |
| **Corrected claim** | The **same single role grants and revokes**. There is no segregation of duties on the override control |
| **Impact** | `CONTRA-11`. Moves the control from "well shaped but under-justified" to "structurally unsound". Drives `ST-16` |
| **Disposition** | **`CORRECTED`** |

---

## `CC-04` — Rate types

| Step | Content |
|---|---|
| **Primary claim** | "There is no rate-type dimension — no spot, average, closing or historical rate." |
| **Search scope** | The framework rate model and the account module's rate extension — **not** the module's currency-table builder |
| **Primary evidence** | The stored rate model's field list and unique constraint |
| **Reviewer contradiction** | The challenge unit, and independently Expert 3 |
| **New evidence** | `account/models/res_currency.py:105-160` — a temporary currency table with an explicit `rate_type` column and four builders for `current`, `closing`, `historical`, `average`, selected by a translation-adjustment flag |
| **Corrected claim** | Storage holds one measurement per currency per day per company root. **Valuation bases are derived at query time.** Both halves are true and they are different layers |
| **Impact** | **Positive.** Coverage `H-13`/`H-15` improve; `GAP-H01` re-scoped to "no *posting* mechanism found; a *valuation* mechanism exists"; and the corrected evidence produced `ST-05`, an `ADAPT` |
| **Disposition** | **`RESCOPED`** |

---

## `CC-05` — Numbering-control configuration parameter

| Step | Content |
|---|---|
| **Primary claim** | "A tenant-writable configuration value disables the numbering/date-alignment control tenant-wide." |
| **Search scope** | The constraint method and its parameter lookup |
| **Primary evidence** | `sequence_mixin.py:154-179` |
| **Reviewer contradiction** | Expert 4 — wrong in **both** directions |
| **New evidence** | Writing the parameter requires the system-administrator group, so it is **not** tenant-writable. And the configuration store carries **no company dimension**, so the effect is **not** confined to a tenant |
| **Corrected claim** | A system-administrator-level value with **database-wide** effect. In a shared deployment, one write disables the control for every tenant, invisibly |
| **Impact** | Re-filed from the control matrix (file 14) to the SaaS boundary register (file 16) as `SB-01`. Drives `ST-29` `REJECT` and `TI-01` |
| **Disposition** | **`CORRECTED`** |

---

## `CC-06` — Thai localization source availability

| Step | Content |
|---|---|
| **Primary claim** | The source registry omitted Thai localization, implying it was unavailable |
| **Search scope** | The accounting, advanced-accounting, reporting and framework modules |
| **Primary evidence** | Those modules |
| **Reviewer contradiction** | The challenge unit |
| **New evidence** | `l10n_th` and `l10n_th_reports` are present in the same verified build |
| **Corrected claim** | Thai localization **implementation** evidence exists and is readable. Its **content was not adopted** by this session's research team |
| **Impact** | **No statutory position changes.** All seven Thai items remain `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track. Reading an implementation establishes what it does, never what the law requires |
| **Disposition** | **`RESCOPED`** |

---

## Summary

| Disposition | Count | Claims |
|---|---|---|
| `CORRECTED` | 3 | `CC-02`, `CC-03`, `CC-05` |
| `RESCOPED` | 3 | `CC-01`, `CC-04`, `CC-06` |
| `RETRACTED` | 0 | — |
| `CONFIRMED` | 0 | — |
| `UNKNOWN` | 0 | — |
| `HOLD` | 0 | — |

### Observations for the gate

1. **No contradicted claim was retracted outright.** In every case a real behaviour had been
   observed; what was wrong was the mechanism, the boundary, or the actor.
2. **Three of six became more serious after correction** (`CC-02`, `CC-03`, `CC-05`). Correction is
   not the same as softening.
3. **Two of six improved the model** (`CC-01`, `CC-04`) — the corrected evidence supplied a better
   architectural position than the original claim did.
4. **Four of six were failures of search scope, not of reasoning.** They are addressed structurally
   by the negative-claim standard rather than by re-reading.
5. **The four reviewers converged independently on `CC-02`.** A finding that four separate reviewers
   reach without coordination is the strongest signal in this package, and it points at the accounting
   date — which is accordingly the subject of its own forensic (`C07`).
