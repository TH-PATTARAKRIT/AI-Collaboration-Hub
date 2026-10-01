# Correction packet U10-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** Two extension points that select stock movements or invoices related to an invoice or movement are declared and extended by the purchase-receiving and sales-delivery capabilities. [N-U10R1-001] [N-U10R1-003]
- **BUSINESS RULE:** Nothing in the studied code base calls either extension point, so they do not influence invoice posting, cost-of-sales booking or refund handling in this version. [N-U10R1-002] [N-U10R1-004]
- **DEPENDENCY:** Earlier statements that tie cost-of-sales delta booking and refund handling to these two extension points are not supported; the actual mechanism must be re-established from the invoice-line cost-of-sales logic. [N-U10R1-002]
- **RISK:** A target design built on the assumption that these extension points drive cost-of-sales timing would be wrong; the real triggers are a separate, still-to-be-confirmed path. [N-U10R1-002] [N-U10R1-004]
- **UNKNOWN:** Whether another installed or future module invokes these extension points is not established beyond the searched source tree.
