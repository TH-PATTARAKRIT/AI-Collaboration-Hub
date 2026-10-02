# Correction packet U13-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** How an imported electronic invoice's tax total is reconciled with the system's own computation.
- **BUSINESS RULE:** On the newer import path a difference of up to three hundredths between the document's tax total and the computed one is accepted and corrected; the older path corrects rounding-level differences without a stated limit; a limit of five hundredths appears only in a comment. [N-U13R1-001] [N-U13R1-002]
- **DEPENDENCY:** Two generations of export and import builders coexist; which one runs for a given format depends on the effective extension order. [N-U13R1-003] [N-U13R1-004]
- **UNKNOWN:** The effective export builder per format requires runtime confirmation. [N-U13R1-004]
