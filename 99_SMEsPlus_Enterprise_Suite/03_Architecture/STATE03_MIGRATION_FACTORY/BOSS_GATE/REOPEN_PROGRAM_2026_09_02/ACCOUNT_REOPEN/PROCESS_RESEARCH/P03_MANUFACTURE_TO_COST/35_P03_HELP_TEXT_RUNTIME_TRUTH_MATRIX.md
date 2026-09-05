# 35 — P03 HELP-TEXT / RUNTIME TRUTH MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. The text, verbatim

`mrp_account/models/product.py:126-128`, on the production-account field:

> *"This account will be used as a valuation counterpart for both components and final
> products for manufacturing orders. If there are any workcenter/employee costs, this value
> will remain on the account once the production is completed."*

## 2. Truth by layer

| Layer | What it asserts / does | Verdict |
|---|---|---|
| **Help-text truth** | Work-centre and employee costs **remain** on the production account after completion | **FALSE** |
| **Source truth** | `_post_labour` debits the production account by exactly `_cal_cost()` — work-centre **and** employee cost — clearing them (`mrp_account/models/mrp_production.py:82-91`) | The text names precisely what is cleared |
| **Source truth, second half** | `extra_cost` is capitalised at `:53-54` and appears in **no** relief entry | The one residue that genuinely remains is **not mentioned** |
| **Configuration truth** | The clearing is gated on `valuation == 'real_time'` (`:74`). For periodic valuation nothing is posted, so the costs *do* remain — the help text is accidentally right in a case it does not name | **CONFIGURATION DEPENDENT** |
| **Runtime truth (`iSMEs`)** | Work-centre and employee costs are **zero on every order**, so neither clearing nor residue occurs. `extra_cost` is zero on all 10,764 rows | Neither the text nor the defect has any effect in the live data |
| **Accounting truth** | The production account should net to zero per order; `DC-03` and `DC-04` are the two ways it does not | — |

## 3. Classification

> **DOCUMENTATION DEFECT — and specifically an inverting one.** The text names as permanent
> the residue that is cleared, and omits the residue that is permanent.

Not a runtime defect: the code does what it was designed to do. Not merely incomplete:
a reader following it looks for the balance **in the wrong place and for the wrong
reason**, which is worse than silence.

The `CONFIGURATION DEPENDENT` qualifier in §2 is retained rather than dropped, because
under periodic valuation the sentence is true. **A documentation defect that is correct in
an unnamed minority case is still a defect**, but reporting it without the qualifier would
overstate it.

## 4. Why P03 records this at all

The finding is small in amount and zero in the live data. It is retained because of what
it demonstrates about evidence weight, which is a governing rule rather than a detail:

> **Field help text is not evidence of behaviour.** Here it is the *inverse* of behaviour.
> Any SMEsPlus requirement derived from reading vendor help text — rather than from the
> code path and the data — inherits an error that no amount of review of the requirement
> itself will catch.

`smeplus-secondary-source-defect-class` records exactly this class: *a summary may locate a
source but never be the evidence*. This is that class, inside the product, and it was found
by P04 and verified by P03 rather than taken on either side's word.

## 5. Contradiction register entry

Already carried as `CTR-P03-07` — `16` §1. Class **CONTRADICTED**. Severity **Low** in
amount, **Medium** as a method warning.
