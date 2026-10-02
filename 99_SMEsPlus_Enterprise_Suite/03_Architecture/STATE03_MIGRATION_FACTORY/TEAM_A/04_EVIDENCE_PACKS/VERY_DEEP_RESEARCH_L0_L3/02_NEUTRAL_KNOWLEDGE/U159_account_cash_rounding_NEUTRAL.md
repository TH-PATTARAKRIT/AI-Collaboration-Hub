# U159 Neutral Knowledge — Invoice Cash Rounding (Thai-Relevant)

**Unit:** U159 | **Research date:** 2026-10-02
**Rule:** No code names, no dotted paths, no file extensions, no backticks — plain prose only

---

## What Cash Rounding Is

In some jurisdictions, the smallest denomination of physical currency is larger than the smallest unit of account. For example, a currency with two decimal places may have no coin for one or two hundredths of a unit. When customers pay in cash, the invoice total must be rounded to the nearest coin that actually exists. The cash rounding feature automates this adjustment so the accounting entry remains balanced and the invoice face value matches what the customer pays.

---

## How the Configuration Record Works

A dedicated configuration record holds all the parameters that govern how rounding operates. It stores a precision step — the smallest coin value — along with a choice of rounding direction: always up, always down, or to the nearest value. It also holds two posting accounts (one representing a gain when rounding reduces the total, one representing a loss when rounding increases it), both of which are set per company so multi-company environments can use different account codes. The only constraint is that the precision step must be a positive number.

---

## How the Rounding Amount Is Calculated

When an invoice is saved in draft, the system sums all of the non-receivable, non-payable journal lines (excluding any existing rounding line) to get the current invoice total in the invoice's currency. It then applies the configured rounding rule to that total and computes the difference between the rounded result and the original total. If the invoice currency differs from the company's functional currency, the difference is converted at the invoice date exchange rate. The result is a balance delta and an invoice-currency amount delta.

---

## How the Rounding Journal Line Is Created

If the computed delta is not zero, the system either creates a new journal line or updates the existing one. The new line carries a special classification that distinguishes it from ordinary product lines, tax lines, and payment term lines. The account posted to depends on the chosen strategy.

Under the first strategy, the rounding delta is posted to the profit or loss account on the configuration record: if the rounding increased the total (the customer pays more), the difference goes to the loss account; if the rounding decreased the total (the company collects slightly less), it goes to the profit account. This line appears as a visible separate item on the invoice.

Under the second strategy, the system instead finds the existing tax line with the largest absolute balance and adjusts it by the rounding delta, using that tax line's account and tax classification. No separate line is added; the VAT balance is simply nudged.

---

## Sequence and Invoice Total Impact

The rounding line is assigned a sequence number that places it after tax lines and before payment term lines in the display order. In computing the invoice total, the rounding delta always contributes to the overall amount. Whether it inflates the tax subtotal or the untaxed subtotal depends on the strategy: a line created under the first strategy (no tax attribution) counts as untaxed; a line created under the second strategy (carrying the original tax attribution) counts as tax.

---

## Payment Term Alignment

When an invoice has payment terms that split the total into instalments, each instalment is also subjected to the rounding calculation. The system adds the rounding difference to each instalment's foreign-currency amount before finalising the payment schedule, keeping every due amount consistent with the configured precision.

---

## Feature Activation

The cash rounding capability is inactive by default. It becomes available only after a company administrator enables a dedicated toggle in the accounting settings. This activates a security group that makes the cash rounding selector visible and editable on invoice forms. The field is editable only while the invoice remains in draft; once confirmed, the rounding configuration is locked.

---

## Interaction with Fiscal Positions

Fiscal positions in this system remap tax codes and accounts for cross-border or special-regime transactions. They have no effect on cash rounding. The accounts used for rounding are configured solely on the rounding record itself and cannot be remapped through a fiscal position.

---

## Relevance for Thai Billing

Thai accounting practice typically rounds invoice totals to the nearest whole baht. Since the precision step accepts any positive number, setting it to one whole unit achieves this outcome without any code modification. The first strategy — adding a separate visible line — aligns with the expectation that a Thai tax invoice shows the rounding explicitly. The profit and loss accounts must be mapped to the appropriate accounts in the Thai chart of accounts, and this mapping is set per company.
