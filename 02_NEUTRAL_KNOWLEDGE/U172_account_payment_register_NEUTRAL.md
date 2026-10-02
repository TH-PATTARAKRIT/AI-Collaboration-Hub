# U172 — account.payment.register: Wizard Payment Posting Chain
**Unit**: U172 | **Module**: account (wizard) | **Group**: G03
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Wizard Model Architecture

The register-payment wizard is a transient model — its records are ephemeral and are auto-purged after the session closes. The wizard receives its source lines through context when it is opened from an invoice or journal item list. On initialisation, it filters those lines to only those carrying an outstanding residual balance on a receivable or payable account. Lines from different root companies, or mixing customer-side and vendor-side accounts in the same wizard invocation, are rejected immediately with a user-visible error.

## Invoice-to-Payment-Group Batching

Before anything is displayed to the user, the wizard groups the incoming lines into batches. Each batch is defined by a five-part key: the partner, the account, the line currency, the partner bank account (taken from the invoice's own bank field when the document is an invoice), and whether the account is receivable (customer) or payable (vendor). Lines sharing the same key are collected into one batch.

The payment direction for each batch is derived from the arithmetic sign of the combined balance of its lines: a positive aggregate balance means money is being received; a negative one means money is being sent. When a partner has exactly one bank account associated with both directions, the wizard can merge otherwise separate inbound and outbound batches for that partner into a single unified batch.

When only one batch results, the wizard enters an editable, single-partner mode. When multiple batches are present (for example, when paying invoices for several different partners in one action), the wizard enters a read-only summary mode where the user cannot change amounts or partners.

## Currency Handling

The wizard currency is resolved in a fixed priority order: the currency of the selected journal takes precedence, followed by the source currency of the batch, then the company's own currency. This means choosing a foreign-currency journal automatically switches the payment into that foreign currency.

Available journals are restricted to bank, cash, and credit-type journals of the company, further filtered to those that have payment method lines compatible with the direction of the payment (inbound or outbound).

When selecting a specific journal automatically, the wizard tries combinations from most specific to least specific: a journal whose currency matches the batch currency and whose linked bank account matches the partner's bank account is preferred; if none exists, it relaxes to currency-only, then bank-account-only, then any matching journal.

## Memo Auto-Population

The payment memo is derived from the source documents. For a single invoice, the invoice's payment reference is used first, then its vendor bill reference, then the invoice name. For multiple outbound documents, all available references are collected, deduplicated, sorted, and joined. For multiple inbound documents, the company generates the next sequential batch payment communication identifier.

## Amount and Installment Handling

The default amount shown is the outstanding residual of the covered lines, accounting for installment payment terms. The wizard supports four installment modes: paying only the next unreconciled installment, paying only the overdue amount, paying all installments falling before a specified date, or paying the full remaining balance. When the user manually types a different amount, it is stored separately so that currency or date changes can convert it correctly rather than resetting it.

## Partial Payment and Difference Handling

When the user pays less than the total residual, a payment difference arises. The user selects one of two outcomes: leave the invoice partially open (the residual remains for a future payment), or mark the invoice as fully paid by writing off the difference to a nominated account with a user-specified label. For early payment discounts, the system automatically populates the write-off lines with the discount counterpart entries computed from the invoice terms.

When the write-off account is the company's currency exchange gain or loss account and the payment currency differs from the source, the difference is handled by forcing a fixed balance on the payment entry rather than adding a separate write-off line, letting the reconciliation engine place the exchange difference directly.

## Payment Creation Sequence

Confirming the wizard triggers a three-stage sequence. First, all payment records are created in draft state in a single database operation, with invoice synchronisation skipped during creation. Second, all created payments are posted in one batch call, suppressing automatic re-delivery of linked sale invoices. Third, the unreconciled lines on the posted payments are matched against the original invoice lines by account; for each shared account the system calls the reconciliation engine on the combined set, then links each payment back to its source moves.

The sequence is always: create → post → reconcile. Reconciliation is not deferred.

## Group vs. Per-Invoice Payments

When group-payment mode is active and the wizard is in editable mode (single-batch or grouped multi-invoice), a single payment is created covering all invoices in the batch. When group-payment mode is off, each invoice gets its own payment record. In the multi-batch (read-only) mode, the grouping decision is applied independently within each batch.

## Bank Account and Trust Validation

Before payment creation, batches whose payment method requires a validated partner bank account are checked. If the batch lacks a bank account, or if the bank account is present but has not been marked as trusted for outgoing payments, that batch is silently skipped. If all batches fail this check, creation is aborted with an error directing the user to validate the recipient bank account.

## Draft Invoice Guard

When any of the source lines belongs to an invoice still in draft state, the difference-handling option is forced to "keep open" regardless of the user's selection, preventing a write-off from being created against an unconfirmed document.

## Multi-Branch Support

When source lines span sibling branch companies (different branches sharing a common root, but the root itself is not in the batch), the wizard creates payments with elevated access rights to avoid cross-company visibility restrictions. In that case, the normal post-creation redirect to the payments list is suppressed to prevent access errors for the initiating user.
