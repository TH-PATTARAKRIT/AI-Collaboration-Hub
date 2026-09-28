> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Team A (Maker) | Documentation-Only | Boss sole Final Approver

# 00 — DOMAIN INDEX

Gx7 of the continuous STATE03 Deep Study run. Backbone Roadmap Lane C scenario 7: *"Manufacturing Raw Material consumption -> WIP -> Finished Goods -> financial valuation interface."*

## Relationship to the Gx6 resolution

This Gx **generalizes, not contradicts,** the Gx6 finding. Manufacturing has no external vendor-bill/customer-invoice event to defer to, so — like Gx4's inventory adjustments — its stock-value-changing events post automatically at the manufacturing event itself (component consumption, production completion), not deferred to a later financial-transaction event. This is the same underlying rule as Gx6 (`post at the financial-transaction event`) applied to a case where the manufacturing event *is* the financial-transaction event. See `06_BUSINESS_RULE_REGISTER.md` `MFG-F01`/`MFG-F02`.

Same taxonomy as prior Gx (01, BASELINE_CARRY_FORWARD, 04, 06, 11, CONTROL_APPLICABILITY_MATRIX, 19, 22, CHALLENGE_QUESTION_SET_LOG, 25, AWT_BACKLOG).
