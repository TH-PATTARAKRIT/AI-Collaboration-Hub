# Correction packet U08-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** Which delivery documents may enter the return step. [N-U08R1-001]
- **BUSINESS RULE:** By the base stock rule, only a completed transfer can be returned. When the sales-delivery capability is installed, a transfer linked to a sales order can also enter the return step regardless of its state. [N-U08R1-001]
- **CONSTRAINT:** The return step builds its list from the moves of the transfer, excluding cancelled moves and moves into inventory-adjustment locations; the warning text that only completed lines can be returned is enforced through that list rather than through the eligibility test. [N-U08R1-002] [N-U08R1-003]
- **RISK:** Users may be able to start a return for a sales-linked delivery that is not yet completed; the effect on stock, quantities and accounting is not established. [N-U08R1-001]
- **UNKNOWN:** Returnable quantity and resulting document for an incomplete sales-linked delivery require runtime confirmation. [N-U08R1-004]
