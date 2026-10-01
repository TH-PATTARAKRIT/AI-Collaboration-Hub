# Correction packet U11-R2 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** Which dates on a customer invoice describe the physical delivery or supply, and when the system asks the user to confirm unusual documents.
- **BUSINESS RULE:** A draft customer invoice receives an informational delivery date from the linked sales orders when the sales-delivery capability is installed (the latest order effective date); the base accounting capability leaves the date empty. A separate taxable-supply date exists but is left empty by the base capability and by the Thai pack. [N-U11R2-001] [N-U11R2-002]
- **OPTIONALITY:** The unusual-document confirmation is skipped for automated posting and shown when a person posts from the document form. [N-U11R2-003]
- **RISK:** The delivery date is informational only; no tax-point rule is driven by it in the studied source. [N-U11R2-001] [N-U11R2-004]
- **UNKNOWN:** Any use of the delivery date for tax point or locks beyond display requires runtime confirmation. [N-U11R2-004]
