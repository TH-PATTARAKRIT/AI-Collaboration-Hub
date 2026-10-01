# Correction packet U11-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** How an invoice's payment status and its cancellation interact with payments.
- **STATE:** The intermediate status 'in payment' exists as a value but is assigned only through an extension point that the community product leaves at its default, which returns 'paid'. In this product a fully settled invoice therefore shows as paid as soon as the settling payment is posted. [N-U11R1-001] [N-U11R1-002] [N-U11R1-003]
- **BUSINESS RULE:** Cancelling an invoice or bill removes the matching between its lines and any payments, but does not cancel the payments that settled it; those payments remain posted and become unmatched. Only cancelling a payment's own entry cancels that payment. [N-U11R1-004] [N-U11R1-005]
- **OPTIONALITY:** The 'in payment' status becomes available only when an accounting extension that is not part of the community product overrides the status rule. [N-U11R1-001]
- **RISK:** Designs that expect an 'in payment' status, or that expect invoice cancellation to cancel payments, will behave differently; unmatched but posted payments may need follow-up. [N-U11R1-003] [N-U11R1-005]
- **UNKNOWN:** The payment status shown after cancelling a settled invoice requires runtime confirmation.
