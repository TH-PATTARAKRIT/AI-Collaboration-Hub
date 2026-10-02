# U123 — account: Year-End FX Adjustment Close (Neutral Knowledge)
## Date: 2026-10-02
## Gap ID: GAP-048
## Status: GATE-PENDING

---

## What FX Adjustment Mechanism Exists in Community at Reconciliation Time

Odoo 19 Community handles foreign currency exchange differences automatically and exclusively at the point of reconciliation. When two journal items are matched — for example, an invoice in a foreign currency against a payment — the system compares the functional currency (company currency) amounts of the two items. If the exchange rate moved between the invoice date and the payment date, the two sides will not balance in company currency even though they balance in the foreign currency. The system calculates this residual and creates a small balancing entry called an exchange difference journal entry.

This mechanism is built into the reconciliation process itself. No manual action or scheduled batch is required. The entry is created in the same database transaction as the matching record, is automatically dated to the most recent date among the matched items, and is posted immediately if both matched items were already in a posted state.

The exchange difference entry is a standard double-entry: one line is posted to the original receivable or payable account (to bring its residual to zero) and a second line is posted to either the gain account or the loss account depending on the direction of the rate movement. A gain results when the functional currency value of the receipt exceeds the original invoice value; a loss results when it falls short.

All three configuration items — the exchange journal, the gain account, and the loss account — are set at company level. The system raises a blocking error and refuses to create the entry if any of these three is missing.

When a matched pair is later unreconciled, the system automatically reverses the exchange difference entry as part of the same unreconciliation action.

---

## What Is Absent: Unrealized FX Revaluation Wizard

There is no unrealized foreign currency revaluation wizard in the Community edition of Odoo 19. Such a wizard would allow a company to revalue all open foreign currency balances at year-end using the closing rate, creating period-end unrealized gain and loss entries for balance sheet items (receivables, payables, bank accounts) that remain open at the financial year end. This is a standard requirement under IFRS and many other accounting frameworks.

In Enterprise editions of Odoo, this functionality is provided by a dedicated wizard accessed from the accounting closing menu. In Community, this wizard is entirely absent. Confirmed by exhaustive search of the account module wizard directory and model files: no file, class, or method matching revaluation, unrealized FX, or FX adjustment batch exists in Community.

This absence is the core finding of GAP-048. A company closing its books under multi-currency accounting in Community cannot perform a year-end balance sheet FX revaluation without a custom development or a manual workaround (for example, posting manual journal entries to the exchange gain or loss accounts and reversing them on the first day of the new period).

---

## Year-End Close Process for Foreign Currency Balances in Community

Community does not include a dedicated year-end closing wizard. The period-closing mechanism available in Community consists of:

1. **Fiscal year lock date** — a configurable date on the company record that prevents any new journal entries from being posted on or before that date. This is set manually by the accountant after completing the period.

2. **Hard lock date** — an irreversible form of the fiscal lock date that cannot be removed once set. Intended for permanently closing historical periods.

3. **Tax return lock date** — a separate lock that prevents posting of tax-bearing entries for submitted periods.

4. **Secure entries wizard** — a wizard that applies an inalterable cryptographic hash to all posted journal entries up to a chosen date, protecting them from retroactive modification.

None of these mechanisms creates or forces any foreign currency adjustment. The lock dates purely prevent new or changed entries; they do not trigger any revaluation computation.

For foreign currency balances that remain open at year-end in Community, the exchange difference will only be recorded when the items are eventually reconciled in a future period. Until reconciliation, the balance sheet will carry those items at their original transaction rate without any year-end revaluation.

---

## Gain and Loss Account Configuration

The company configuration record holds three foreign currency accounting settings:

- **Exchange Gain or Loss Journal** — a general journal used as the home for all exchange difference entries. Both gains and losses are posted to this journal.
- **Gain Exchange Rate Account** — the income-type account credited when an exchange gain arises. The selection is restricted to accounts in the income internal group.
- **Loss Exchange Rate Account** — the expense-type account debited when an exchange loss arises. The selection is restricted to expense account types.

These three settings must all be populated before the system can create any exchange difference entry. Missing configuration causes an immediate user error.

---

## Summary for GAP-048

GAP-048 status is PARTIAL. Community contains a working exchange difference mechanism that handles FX at reconciliation time. What is absent is the year-end unrealized balance sheet revaluation. The gap is real: any company using foreign currencies will need a custom solution or a manual period-end process to comply with accounting standards that require balance sheet FX revaluation at each reporting date.
