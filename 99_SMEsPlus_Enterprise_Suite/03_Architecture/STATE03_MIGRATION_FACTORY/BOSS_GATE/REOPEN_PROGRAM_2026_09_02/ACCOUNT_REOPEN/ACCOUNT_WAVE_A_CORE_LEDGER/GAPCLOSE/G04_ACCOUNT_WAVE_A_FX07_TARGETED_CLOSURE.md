# G04 — FX-07 TARGETED CLOSURE — IS THE REVALUATION CONTROL CONTAMINATED?

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
Prior classification: `NOT PROVEN`

---

## 1. Original claim

Raised by fresh Reviewer A (`IF-01`): the multicurrency revaluation report — the compensating control
that would surface a wrong FX valuation — **resolves rates through the same `_get_rates` path** and
**guards only against a zero rate**, so it inherits the par fallback of `SF-01`.

## 2. Exact search scope

`addons/account_reports/models/account_multicurrency_revaluation_report.py` and
`addons/account_reports/wizard/multicurrency_revaluation.py`. Method:
targeted read of the report's option initialiser and the wizard's entry creation.
No other module searched — stated per `DR-NC-02`.

## 3. Source evidence

`account_reports/models/account_multicurrency_revaluation_report.py`, in
`_custom_options_initializer`:

- **the same resolver is used** —
  `rates = active_currencies._get_rates(self.env.company, options.get('date').get('date_to'))`
- rates are normalised against the company currency — `rates[key] /= company_rate`
- **the only guard** —
  ```
  for currency_rates in options['currency_rates'].values():
      if currency_rates['rate'] == 0:
          raise UserError(_("The currency rate cannot be equal to zero"))
  ```
- a user override exists — a previously supplied rate is preferred if present, and `custom_rate` is
  set when any supplied rate differs from the resolved one.

`account_reports/wizard/multicurrency_revaluation.py:169-178` — `create_entries` builds an
`account.move`, posts it, and creates a dated reversal.

## 4. Analysis

Where a currency has no rate row with a non-empty value in the resolvable scope, `_get_rates` returns
**`1.0`** (`base/models/res_currency.py:140`).

`1.0 ≠ 0`, so the zero guard **passes**.

The report therefore presents, and the wizard can post, a revaluation computed against a **fabricated
par measurement**, with no warning.

## 5. Contradiction evidence sought

Three possible refutations were tested against the source:

| Possible refutation | Result |
|---|---|
| A separate guard elsewhere in the report rejects a par or absent rate | **Not found** in the searched scope |
| The report resolves rates by a different path than posting | **Refuted** — it calls `_get_rates`, the same path |
| The user override makes the resolved rate advisory | **Partially true and insufficient** — the override is optional and the par value is the **presented default** |

## 6. Final narrow claim

> Within `addons/account_reports`, the multicurrency revaluation report resolves rates through
> `_get_rates`, the same path that returns `1.0` when no usable rate exists, and its only rate guard
> rejects zero. A par-valued revaluation is therefore presentable and postable without warning. A
> user-supplied rate override exists and is optional.

## 7. Disposition

> ## `VERIFIED DEFECT` — the compensating control is contaminated

**Confidence: high.** Both the resolution path and the guard were read directly; the claim is a
direct reading, not an inference.

### Why this matters more than it appears

`SF-01`'s severity rested partly on the expectation that a periodic revaluation would eventually
surface a wrong valuation. It would not: fed the same par rate, the revaluation computes a difference
of approximately zero against a wrong carrying amount and reports **no adjustment required**.

> The control that should detect the error **confirms it**.

This is the third independent reason `SF-01` is undetectable, after the absent forward warning and
the withdrawn display-divergence signal (`A1-01`).

## 8. SMEsPlus position

**`EXTEND`.** The post-and-reverse revaluation pattern itself is sound and worth adopting — including
its custom-rate capability and its guard against reversing over a prior unreversed entry. What must
change: **an unavailable measurement must halt, not default**, at every consumer, and a valuation
control must never share the failure mode of the thing it validates.

## 9. Residual

| # | Item | Class |
|---|---|---|
| `FX07-R1` | Whether the wizard applies further guards beyond the report's option initialiser | `B — NOT FOUND IN SEARCHED SCOPE` in the sections read |
| `FX07-R2` | Whether any localization overrides the guard | `C — NOT YET SEARCHED` |
