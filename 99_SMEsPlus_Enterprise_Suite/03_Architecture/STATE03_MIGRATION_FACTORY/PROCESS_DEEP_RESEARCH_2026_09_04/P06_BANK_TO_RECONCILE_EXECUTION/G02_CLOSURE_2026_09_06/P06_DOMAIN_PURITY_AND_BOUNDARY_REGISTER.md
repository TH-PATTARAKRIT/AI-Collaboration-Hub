# P06_DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G03)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> Prompt §3: *"If an evidence path starts researching another process's internal functional domain, STOP that path, classify it as `EXTERNAL DOMAIN BOUNDARY` or `DOMAIN CONTAMINATION`, preserve only the minimum interface fact required by P06, and return to P06."*
>
> **Four paths were stopped. One of them was already inside a foreign domain when it was caught.** This register exists so the boundary is auditable rather than asserted.

---

## 1. Paths stopped, with the exact stop point

| ID | The path | Where it was heading | **Classification** | Minimum interface fact preserved | Stop point, executed |
|---|---|---|---|---|---|
| `PDR-F-01` | `BR-01` — locating what generates a deferral entry | Recognition mechanics: `_get_deferred_periods`, period grids, convention selection, `generate_deferred_*_entries_method` | **`EXTERNAL DOMAIN BOUNDARY`** | *Deferral generation hangs off `_post()`, i.e. the act of posting a document, not the act of settling one.* Nothing further | Read `account_accountant/models/account_move.py:109-115` and **stopped at the call**. `_generate_deferred_entries`'s body was opened **only** for `BR-02`'s account pair, and its period-splitting loop below `:299` was not read |
| `PDR-F-02` | `BR-02` — which accounts the deferral touches | Deferral amount computation, rounding policy, `force_balance` on the final period, tax treatment of deferred lines | **`EXTERNAL DOMAIN BOUNDARY`** | *The pair is `(the P&L line's own account, the company deferral account)`. Neither is receivable, payable or liquidity.* Therefore P06 reconciles invoiced value | Read `:297-298` and the `deferred_account` assignment at `:268`. **Stopped.** The rounding and period loop immediately below was visible and not read |
| `PDR-F-03` | `BR-03` — does the accrual link to what settles it | **P10's `F-05` / `AL-6` — detecting the superseded accrual.** This is explicitly P10's problem by P10's own statement | **`EXTERNAL DOMAIN BOUNDARY`** — *and the temptation here was real: the question "how would you detect it" is interesting and is not P06's* | *The accrual's only link to its business object is a chatter message on the order. `move_vals` contains no structured source reference.* | Read `account/wizard/accrued_orders.py:235-262`. **Did not open** `_compute_move_vals`'s amount derivation (`:107-232`), the purchase/sale order-line quantity logic it calls, or anything in P10's package about detection |
| `PDR-F-04` | `MD-P06-13` — P02 names a database `iErpOCC` outside P10's examined four | A new deployed-database enumeration | **`DOMAIN CONTAMINATION` — caught before execution** | *P06's own deployment-population statements remain floors.* Nothing else | **Not executed.** Recorded as `P06-OQ-120` and routed. Reading it would have been widening on three counts at once: a new database, a P02 artefact, and a population P06 never declared |

## 2. The boundary that was *not* respected by a naive reading, and why the split matters

**`PDR-F-05` — `H06-3` contains two questions, and only one of them is P10's.**

P10 wrote: *"The accrual is the one mechanism with a settlement relationship and has no link to its settlement… detecting the superseded accrual is P10's problem (`F-05`, `AL-6`)."*

Read as one statement, that hands the whole item to P10 and P06 records `EXTERNAL — HANDOFF ONLY` and moves on. **That reading would have been wrong, and it would have looked disciplined.** The item decomposes:

| Half | Owner | Basis |
|---|---|---|
| **Detecting that an accrual has been superseded by its actual document** | **P10** | P10 says so, and it is a recognition-lifecycle question |
| **What happens to the accrual pair once it is sitting in the reconciliation population** | **P06** | It is two open items on a reconcilable account, and the matching predicate is P06's |

**Accepting P10's ownership statement wholesale would have suppressed `P06-B-59`.** Domain purity is a rule about *where you research*, not a rule about *what you are allowed to notice*. Deferring to a peer's scoping is not the same as respecting a boundary — the boundary here runs **through** the item, not around it.

*This is the `refusals-outperform-contributions` shape inverted: the discipline that usually pays here would have cost a HIGH finding.*

## 3. Interface facts imported from P10 — the complete list

Nothing else from P10 informs any P06 conclusion. Each was **re-executed against source** before use; none is held on P10's authority.

| # | Interface fact | P10 source | P06 verification |
|---|---|---|---|
| 1 | No recognition event is settlement-triggered | `H06-1` | **`BR-01`** — independently confirmed |
| 2 | The deferral timing effect on the receivable is nil | `H06-2` | **`BR-02`** — independently confirmed |
| 3 | The accrual has no link to its settlement | `H06-3` | **`BR-03`** — independently confirmed |
| 4 | Structural and corrective reversals are not distinguished in the ledger | `H06-4` | **`BR-04`** — independently confirmed **and sharpened** |
| 5 | P10's evidence base is four databases in which the deferral mechanism **never generated an entry**; P06 must not read it as deployed-behaviour evidence | §3 | **Honoured. No P10 deployment figure is cited as P06 evidence anywhere in this round** |
| 6 | `X-08` / `D-08` / `PD-08` status is `OPEN — PEER EVIDENCE` | `53_`:30, `19_`:19,59, `10_`:36 | **`BR-05`** — status field read directly at `1fea562` |

**Four of six are P10 assertions that P06 re-derived from primary source. Zero were adopted on authority.** Item 5 is a constraint, not a claim. Item 6 is a status field, which is the one thing only the owner can state.

## 4. Domains not entered

Executed as a negative, and stated with its denominator: of the **109** files in P10's package at `1fea562`, **12** name P06 and were read; **97 were not opened**.

No file was read from any P05, P07, P08, P09 or P11 branch in this round. No Sales, Purchase, Inventory, Manufacturing, Asset, Equipment or Maintenance domain was researched. The only non-`account`/`account_accountant` source files touched were **`account/wizard/accrued_orders.py`** — which lives in the `account` module P06 owns — and nothing in `purchase` or `sale`, whose order-line logic that wizard calls and which was deliberately not followed (`PDR-F-03`).

## 5. Purity self-assessment

**`PDR-F-06` — the boundary held, but it was tested once by a P06 finding rather than by a P10 one.**

`BR-03` surfaced that the accrual's only provenance record lives in `mail.message` — a table `om_data_remove` empties by unfiltered SQL (`44_` OMD-F-01). That is a P06-domain fact about a P10-domain object. **It was recorded as an open question (`P06-OQ-121`) and not pursued**, because pursuing it means asking what P10's mechanism loses when chatter is deleted, which is P10's question. **The observation is preserved; the investigation is not opened.** That is the correct disposition of a fact that arrives across a boundary, and it is recorded here so that the restraint is auditable rather than invisible.
