# U176 — pos.payment.method: POS Payment Method Types and Session Close Accounting
**Unit**: U176 | **Module**: point_of_sale | **Group**: G11 | **Priority**: P1
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Payment Method Types

The POS payment method model uses a computed type field with three possible values. The type resolves from the linked journal: a cash-type journal produces a cash payment method, a bank-type journal produces a bank payment method, and the absence of a qualifying journal produces a "customer account" (pay-later) method. This design means type is not written directly — it is always derived from the journal relationship. Only cash and bank journals are permitted; assigning any other journal type raises an error at the user interface layer.

Cash payment methods carry a stored Boolean flag marking them as the cash-register method for counting. A constraint prevents the same cash method from being assigned to more than one point-of-sale shop. Bank payment methods carry an outstanding account, which serves as the transit account when bank payment records are created at session close.

## Payment Records

Each payment registered in a POS order produces a `pos.payment` record. This record holds the amount, the payment method reference, the order reference, the payment timestamp, and a flag that marks cash returned as change. When a payment uses a terminal (Enterprise or third-party module), additional card data fields store the card type, brand, last-four digits, cardholder name, authorisation code, issuer bank, payment mode, transaction identifier, and payment status.

The `session_id` field on `pos.payment` is a stored relational field derived from the order's session, making it practical to query all payments for a session without joining through orders.

## Session Close Accounting Pipeline

When a session is closed, the system creates a single master journal entry in the configuration's designated accounting journal. The close process accumulates all payments from closed orders into six separate buckets: split-cash, combined-cash, split-bank, combined-bank, split-pay-later, and combined-pay-later. The split-versus-combined distinction is determined by whether the payment method has the "Identify Customer" option enabled.

For cash payments, the system creates individual bank statement lines in the cash journal. The counterpart account for each line is either the intermediary POS receivable account (combined path) or the specific customer's receivable account (split path). Matching receivable lines in the master journal entry are created and then reconciled against the statement lines.

For bank payments, the system creates `account.payment` records in the bank journal. Combined bank payments produce one payment record per payment method per session, using the outstanding account as the source and the intermediary POS receivable as the destination. Split bank payments produce one payment record per customer per payment, using the customer's receivable as the destination. These payment records are then reconciled against the corresponding receivable lines in the master journal entry.

Pay-later payments produce only receivable lines in the master journal entry, with no cash statement lines or bank payment records. They represent deferred customer account balances.

## Intermediary Receivable Account

The POS intermediary receivable (default POS receivable) is the clearing account that appears on both sides of the reconciliation at session close. For cash, it sits between the cash journal and the master entry. For bank, it sits between the bank payment record and the master entry. Each payment method can optionally override this account via its own receivable account field; if blank, the company-level default POS receivable account is used.

## Cash Difference Handling

The theoretical closing balance is computed as the opening balance plus all cash payments plus all cash-in/cash-out transfers recorded during the session. When the cashier's counted balance differs from this theoretical amount, the difference is posted as a separate bank statement line to either the cash journal's profit account (surplus) or loss account (shortfall). Both accounts must be configured on the journal or the close will raise an error.

The `cash_register_difference` field on the session holds this gap in real time. The `post_closing_cash_details()` method stores the counted cash value before the final accounting run.

## Terminal Integration Architecture

The terminal selection field on the payment method is populated by an override method that returns an empty list in Community. This means the field exists in the model and is included in session data sent to the front end, but no terminal options are available unless an Enterprise module or certified third-party add-on overrides the method. The UI hides the terminal field entirely when the list is empty, and also when the payment method type is cash or pay-later, since terminals are incompatible with those types.

## QR Code Payments

When a payment method is configured for the QR code integration type, the system generates QR codes using the bank account attached to the payment method's journal. A pre-generated amount-less QR is cached as a computed field for offline use. The QR generation method enforces that a bank account is present and a QR code method has been selected. An error check confirms the bank account's configuration is compatible with the chosen QR method before saving.

## Thai PromptPay Integration

The Thai accounting localisation extends the bank account model to support PromptPay QR codes via three proxy identifier types: mobile number, merchant tax ID, and e-wallet ID. The encoding follows the EMV QR standard (tag 29) and is restricted to THB currency. This extension operates entirely at the bank account layer. The Thai localisation module does not depend on or extend the POS module — Thai QR payments in POS work through the standard QR code payment method type by linking the method to a Thai bank account configured with a PromptPay proxy.

## Bank Statement Architecture (v19)

In Odoo 19, the POS session does not hold a reference to an `account.bank.statement` header record. Instead, individual `account.bank.statement.line` records carry a direct Many2one reference back to the session. Cash payments, cash-in/cash-out entries, and the cash difference correction are all individual statement lines linked to the session via this field.

## Write-Protection During Active Sessions

The payment method model enforces that all fields except the display sequence are read-only while any open POS session is using the payment method. Attempting to change the journal, accounts, or split setting during live service raises an error listing the open sessions, requiring the operator to close all sessions before modifying the configuration.
