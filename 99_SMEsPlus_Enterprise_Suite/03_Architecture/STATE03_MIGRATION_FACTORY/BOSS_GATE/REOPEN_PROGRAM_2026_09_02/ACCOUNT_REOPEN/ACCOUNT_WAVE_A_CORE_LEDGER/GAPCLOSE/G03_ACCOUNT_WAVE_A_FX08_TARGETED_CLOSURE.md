# G03 — FX-08 TARGETED CLOSURE — BRANCH-COMPANY RATE CONTEXT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
Prior classification: `PARTIALLY VERIFIED` (resolver side confirmed, writer side unsearched)

> Treated separately from `SB-05` as instructed. `SB-05` concerns rates scoped to **no** company.
> `FX-08` concerns rates scoped to the **wrong** company — a branch rather than its root. The
> evidence overlaps in the resolver; the defect and its remedy are different.

---

## 1. Exact scenario

A company hierarchy exists: a root company with one or more branch or subsidiary companies. A user
acting **in the context of a branch company** updates exchange rates. Postings are then made in that
branch company in a foreign currency.

## 2. The two sides, both now verified

### Writer side — `VERIFIED FACT`

`currency_rate_live/models/res_config_settings.py:1374-1376`:
```
def update_currency_rates_manually(self):
    self.ensure_one()
    self.company_id.update_currency_rates()
```
`self.company_id` on the settings record is the **acting company**, which may be a branch.

`currency_rate_live/models/res_config_settings.py:267-290` — inside `update_currency_rates`,
`for company in self:` iterates that recordset, and the write is:
```
CurrencyRate.create({'currency_id': ..., 'rate': rate_value,
                     'name': date_rate, 'company_id': company.id})
```

> The rate is written with **`company.id`** — the acting company — **not** `company.root_id`.

### Resolver side — `VERIFIED FACT` (re-confirmed)

`base/models/res_currency.py:128-131` — `_get_rates` filters
`('company_id', 'in', (False, company.root_id.id))`.

> The resolver reads **only** the root company's rates, plus null-company rates.

## 3. The defect

> **`VERIFIED FACT`.** When the acting company is not its own root, the writer stores
> `company_id = <branch>` and the resolver looks for `company_id ∈ (NULL, <root>)`. The two do not
> intersect. **A rate maintained at branch level is invisible to the conversion that consumes it.**

### Consequence chain

```
branch user updates rates          → rows written with company_id = <branch>
posting in the branch, foreign ccy → _get_rates filters on <root>
                                   → branch rows not matched
                                   → COALESCE branch 2: earliest rate ever for that currency
                                                        in (NULL, root) scope, if any
                                   → COALESCE branch 3: 1.0
```

- **Trigger:** any foreign-currency posting in a non-root company whose rates were maintained in that
  company's own context.
- **Source currency / company currency:** any pair that differs.
- **Date source:** the document or accounting date, per `_compute_currency_rate`.
- **Rate source:** the root company's rates, or a null-company rate, or **par**.

### Posting, GL and reporting consequence

The posting is created with a **stale, foreign, or par** measurement. The entry balances, satisfies
the sign constraint, posts, numbers, hashes and reconciles. GL and every downstream report carry the
wrong company-currency value.

## 4. `BALANCED BUT WRONG` — explicit test

> **The entry balances. The valuation is wrong.**

Every item on the entry resolves through the same call, so all share the same erroneous factor.
Debits equal credits; `balance` and `amount_currency` agree in sign; the trial balance foots.
**No arithmetic control can detect this**, because the error is in the *correspondence to an external
measurement*, not in the internal consistency of the entry.

This is registered as `BW-16`, a distinct case from `BW-01`: `BW-01` arises when **no** rate exists;
`BW-16` arises when a rate **does** exist, was deliberately maintained, and is simply not visible to
the resolver. `BW-16` is the more insidious of the two, because **the tenant has evidence that rates
are loaded.**

## 5. Detectability

| Signal | Available? |
|---|---|
| Error or warning at rate entry | **No** — the write succeeds |
| Error or warning at posting | **No** |
| The rate list shows rates exist | **Yes — and this is precisely what misleads** |
| Displayed rate on the document | Reads the **stored** document rate for invoices and bills (`A1-01`), so par displays as par consistently |
| Trial balance | Foots |
| Integrity hash | Does not cover the transaction-currency amount |

> **Net detectability: none through any accounting control.** The only realistic discovery is a
> human noticing that a foreign-currency document is valued at or near par while the rate table shows
> a correct rate.

## 6. Correction mechanism

Amounts are stored at posting, so entering the rate correctly afterwards does **not** restate them.
Correction requires reversal and re-entry of every affected document after the rates exist in the
resolvable scope. There is no restatement tool in the searched scope
(`addons/account`, `addons/currency_rate_live`) — **`B — NOT FOUND IN SEARCHED SCOPE`**.

## 7. A second, independent inconsistency found

`base/models/res_currency.py:399-406` — `_get_last_rates_for_companies` matches
`x.company_id == company or not x.company_id` — **exact company** or null.
`base/models/res_currency.py:128-131` — `_get_rates` matches **root** company or null.

> **`VERIFIED FACT`:** two rate-resolution helpers in the same file apply **different company
> scoping rules**. A branch-scoped rate is visible to one and invisible to the other.

`INFERENCE:` this makes the displayed rate and the posted rate capable of disagreeing for the same
company and date — one more reason a user maintaining branch rates would believe the configuration
is correct.

## 8. Disposition

> ## `VERIFIED DEFECT`

Writer and resolver disagree on company scope. The failure is silent, produces an internally valid
entry, is not detectable by any accounting control, and is not correctable without reversal.

## 9. SMEsPlus position

**`REJECT`.** One scoping rule, applied identically by every writer and every reader of a
measurement. A measurement written in a context must be resolvable in that context, or the write
must be refused. Combined with `SB-05`'s conclusion: **every rate carries exactly one owning
boundary, and resolution never crosses it, in either direction.**

## 10. Residual

| # | Item | Class |
|---|---|---|
| `FX08-R1` | Whether the settings UI prevents selecting a branch company for rate maintenance | `C — NOT YET SEARCHED` |
| `FX08-R2` | Whether other rate writers (import, external feed) use root or acting company | `C — NOT YET SEARCHED` |
| `FX08-R3` | Runtime confirmation that a branch-written rate is not returned | `INFERENCE` from two verified code paths; recommended cheap test |
