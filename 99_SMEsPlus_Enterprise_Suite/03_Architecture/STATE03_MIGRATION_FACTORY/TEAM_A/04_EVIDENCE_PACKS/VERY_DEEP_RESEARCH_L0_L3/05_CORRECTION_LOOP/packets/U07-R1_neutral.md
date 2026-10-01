# Correction packet U07-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** Which extension points in returns, extra moves and valuation actually run.
- **BUSINESS RULE:** A vendor-return enrichment that would copy the order line and partner onto return moves is declared but never runs, because it is attached to the wrong object with a mismatched signature. [N-U07R1-001] [N-U07R1-002]
- **CONSTRAINT:** An extra-quantity enrichment on receipt moves is also declared but never invoked. [N-U07R1-003]
- **DEPENDENCY:** The helper that labels a move as a customer return or a vendor return exists but no flow calls it, so valuation does not depend on it. [N-U07R1-004]
- **STATE:** Resetting a vendor bill to draft removes the cost-of-sales lines created at posting but does not revalue the receipts. [N-U07R1-005]
- **RISK:** Designs that assume the vendor-return link to the order, or a return classification driving valuation, must be re-derived from the paths that actually run. [N-U07R1-002] [N-U07R1-004]
- **UNKNOWN:** Whether vendor-return moves still end up linked to their order line through another path needs runtime confirmation.
