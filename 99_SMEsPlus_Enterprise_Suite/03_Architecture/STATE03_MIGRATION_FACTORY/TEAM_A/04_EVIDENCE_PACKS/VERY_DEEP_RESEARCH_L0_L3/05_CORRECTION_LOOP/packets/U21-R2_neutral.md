# Correction packet U21-R2 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** How long an e-mailed second-factor code remains valid.
- **BUSINESS RULE:** An e-mailed second-factor code is valid for a window of between one and two hours from issue, depending on when in a one-hour counter period it was generated. The code is not single-use. [N-U21R2-001] [N-U21R2-002]
- **RISK:** The extended window beyond the stated one hour allows code reuse up to two hours after issue. [N-U21R2-002]
