# P01 — SAME-GENERATION FINDING RECONCILIATION

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-08`

**Governing rule, stated before the table so it cannot be read past:**

> Every finding remains bound to the evidence population in which it was measured.
> A finding measured in the series-19 estate is **not** withdrawn because the series-18 deployment
> behaves differently. `NOT REACHABLE HERE` is a statement about **this deployment**, never about
> the finding.

The detailed evidence for each row is in `P01_S18_SOURCE_DEPLOYMENT_COVERAGE_MATRIX.md`; this
document carries only the reclassification and its justification.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. RECLASSIFICATION

| Finding | Prior evidence class | New classification | Why |
|---|---|---|---|
| Order confirmation creates no accounting effect | V18 + V19 **source only** | **CONFIRMED SAME-GENERATION** | 13,735 confirmed orders in a series-18 deployment; no journal entry references a purchase order |
| Bill is the only universal accounting event | V18 + V19 **source only** | **CONFIRMED SAME-GENERATION · STRENGTHENED** | 1,904 bills carry 6,914 items and are the **only** P2P event reaching the ledger in a deployment with 15,522 entries |
| Three-way match is advisory, not a control | V18/V19 source; installed in `E-3`, never observed exercised | **CONFIRMED SAME-GENERATION · STRENGTHENED · QUANTIFIED** | 1,580 lines received-not-invoiced worth **฿29,029,467.66 tax-exclusive** — of which ฿27,490,865.80 on 1,411 lines is receipt-backed — and 183 invoiced-not-received worth ฿1,663,518.07, persist unblocked and unaccrued |
| Receipt valuation gated on item type and valuation mode | V18 **source only** | **CONFIRMED SAME-GENERATION** | the gate is observed closed by stored configuration and the consequence measured on the corrected 558-layer business-document set (over-determination-free core 541), **not** the 1,812 first published — `ERR-P01-27` |
| Order reset-to-draft has no server-side guard | V18 + V19 source | **CONFIRMED SAME-GENERATION (source)** | source re-verified in the deployed generation; **reachability not measured** in this deployment |
| Goods-received clearing bridge exists | V18 source; **"no deployed representative anywhere"** | **CONFIGURED · NOT EXECUTED · POLICY-DEPENDENT** | it now has a deployed representative: `210300 Uninvoiced Receipts`, reconcilable, 171 of 504 (category, company) pairs — carrying **0** journal items |
| Clearing account reconciled only if flagged | V18 source | **LATENT — CONFIG PRESENT, NOT REACHED** | `reconcile = true` on all four accounts; nothing posts, so nothing reconciles |
| Price-difference replay engine | V18 source; **"no v18 deployment exists to check it against"** | **NOT REACHABLE — CONFIGURATION ABSENT AND POLICY CLOSED** | `property_account_creditor_price_difference_categ` is NULL on 126/126; `price_diff_value` is non-zero on 0 of 47,801 |
| **Bill-line account redirected to a stock account** | V19 source | **CONFIGURATION-DEPENDENT — REACHABLE IN PRINCIPLE, NOT EXERCISED** | ~~*the file carrying the override does not exist in the series-18 tree*~~ — **that was my own error (`ERR-P01-30`): the mechanism is present in v18 at `account_move.py:264-279`.** It is inert because `valuation != 'real_time'`, not because it is absent — and `anglo_saxon_accounting` is **already true in company 1**. Deployed bill lines post to expense |
| Period lock re-dates rather than refuses | V18/V19 source; V16 deployment | **NOT REACHABLE — NO LOCK CONFIGURED** | all five lock fields are NULL on all four companies; `po_lock = 'edit'` |
| Correction deletes derived journal items | V18 source | **NOT REACHABLE — POLICY-DEPENDENT** | no `cogs` lines exist to delete under periodic valuation |
| Cross-company auto-generation; guard cannot execute | V19 source + V19 deployment | **NOT INSTALLED — NOT REACHABLE** | `account_inter_company_rules` is not among the 361 installed modules |
| **Landed cost installed everywhere, exercised nowhere** | **deployment verified across the estate** | **NARROWED — counter-example found** | no `stock_landed_cost*` table exists in this archive. The word **"everywhere"** was an estate-wide quantifier over an incomplete estate |
| Vendor advance defaults to an expense account | custom source | **NOT INSTALLED — NOT REACHABLE** | `scgl_purchase_advance_payment` is not installed here |
| Withholding: repeated full withholding, linear | custom series-16 source, **no deployment runs it** | **DEPLOYMENT-DEPENDENT — DIFFERENT MECHANISM** | this deployment uses `l10n_th` 18.0.2.0 with `account_withholding_tax` / `withholding_tax_cert*` / `account_payment.wt_tax_id`. **The series-16 finding does not transfer.** Statutory questions → **P07** |
| PND mapping conflict | custom source | **UNCHANGED** | not a series-18 question; → P07 |
| Referential links are `ON DELETE SET NULL` | V16 + V19 deployment | **UNCHANGED** | a series-18 FK sweep was not run this round; recorded as a gap, not as agreement |

---

## 2. THERE IS NO CONTRADICTION — THE CONTRADICTION WAS MY OWN ERROR

The first version of this document reported one finding as **contradicted for series 18**:
*"the vendor bill line posts straight to the valuation account"*, on the evidence that
`stock_account/models/account_move_line.py` does not exist in the series-18 tree.

**The file does not exist. The behaviour does.** It is in `account_move.py`
(`R1:stock_account/models/account_move.py:264-279`), and AAS-03 Expert C found it by searching for
the behaviour rather than the file name. Verified here before adoption; logged as `ERR-P01-30`.

**So no prior P01 finding is contradicted by this deployment.** What the deployment shows is a
generation difference of a different kind — v18 redirects the bill line to the **input/clearing**
account via `_eligible_for_cogs()`, v19 to the **valuation** account via an explicit
`valuation == 'real_time'` test — and, in this deployment, a mechanism that is **inert by
configuration rather than absent by design**. In company 1, `anglo_saxon_accounting` is already
`true` and `accounts['stock_input']` already resolves to account 176 on **126 of 126** categories;
only the valuation policy stands between the code and the clearing account.

**The count of contradicted findings in this run is therefore zero**, and the entry that produced
it was an error in the search unit, not a difference in the software. That correction is more
useful than the finding it replaces: it says the deployment is **one configuration value** from
routing bill lines to the clearing account, where the first version implied it was structurally
immune.

---

## 3. THE ONE NARROWING, AND WHY IT MATTERS MORE THAN IT LOOKS

**"Landed cost installed everywhere, exercised nowhere."**

The second half survives. The first half — **"everywhere"** — was a universal quantifier over the
estate as P01 then understood it, and this run adds a deployment where landed costs are **not
installed at all**.

The defect is not the count. It is the **shape of the claim**: a universal statement over a
population that was itself incomplete. This is the same error class as `ERR-P01-23`, expressed in
a finding rather than in a census, and it is why
`P01_POPULATION_SELECTION_METHOD_AUDIT.md §5` records the estate size as a **floor**.

**Every universal quantifier in the P01 package is therefore suspect until re-tested against the
corrected estate.** That sweep is not complete and is recorded as an open action.

---

## 4. SUMMARY

| Classification | Count |
|---|---|
| CONFIRMED SAME-GENERATION | 5 (2 of them STRENGTHENED) |
| CONTRADICTED (for series 18) | **0** — the one entry was my own error, `ERR-P01-30` |
| CONFIGURATION-DEPENDENT / POLICY-DEPENDENT | 3 |
| NOT REACHABLE (policy, configuration or lock absent) | 3 |
| NOT INSTALLED | 3 |
| DEPLOYMENT-DEPENDENT — different mechanism | 1 |
| NARROWED | 1 |
| UNCHANGED | 2 |
| **Findings withdrawn** | **0** |

**Nothing was withdrawn.** One finding is contradicted **for one generation**, one universal
quantifier is narrowed, and nine findings that had never been checked against a same-series
deployment now have been.
