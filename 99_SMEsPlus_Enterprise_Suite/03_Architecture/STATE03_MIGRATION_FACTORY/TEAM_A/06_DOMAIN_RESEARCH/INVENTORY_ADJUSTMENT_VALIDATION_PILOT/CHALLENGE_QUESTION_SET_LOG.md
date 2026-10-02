> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx4)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-IAV-01 | Does an inventory adjustment's financial posting follow the same manual/automatic valuation-mode dependency as a receipt (Gx1) or delivery (Gx2)? | "All stock-quantity-changing events share one valuation-timing rule" | **Contradicted / Conditional — new hypothesis, not confirmed** | Documentation for this specific function states an unconditional "no additional steps needed" immediate Balance Sheet update, with no valuation-mode qualifier found — raising rather than resolving the cross-Gx question (`GAP-IAV-01`). |
| CQS-IAV-02 | Is scrapping goods accounted for identically to an ordinary quantity-correction adjustment? | "Scrap is just another adjustment" | **Contradicted** | Scrap requires its own dedicated Loss Account / Inventory Loss location configuration, documented as a distinct financial-control surface (EV-IAV-02/03). |
| CQS-IAV-03 | Can an applied inventory adjustment be undone/reversed the same way a receipt or delivery can (Reverse Transfer / Credit Note)? | Carried forward from GRV-F07/SDV-F06/F07 | **Contradicted (partially)** — resolved 2026-09-29 | A distinct native mechanism exists (`Revert Inventory Adjustment`, checkbox + Actions menu) — closer to Reverse Transfer than to a freeform new adjustment, but not identical to either receipt/delivery mechanism. See `06_BUSINESS_RULE_REGISTER.md` IAV-F06, `GAP-IAV-02` (closed). |

## Status

`CLOSED (documentation-tier)`: CQS-IAV-02, CQS-IAV-03.
`OPEN (Evidence Conflict, cross-Gx — now Material Finding, Independently Unverified)`: CQS-IAV-01 — feeds the same lineage as `GAP-SDV-01`/Gx1 `GRV-F04`.
