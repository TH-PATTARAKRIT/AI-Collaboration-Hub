> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Control Applicability Matrix (Master Prompt §4.6) | Documentation-Tier

# CONTROL APPLICABILITY MATRIX

`Applicable` / `Not Applicable` / `Unknown`, each with evidence per Master Prompt §4.6.

| Control dimension | Applicability | Evidence |
|---|---|---|
| Financial | **Applicable** | GRV-F04/F05: receipt valuation and landed cost directly affect GL-relevant value (documentation-tier, `06_BUSINESS_RULE_REGISTER.md`). |
| Inventory | **Applicable** | GRV-F02/F03: receipt is the canonical Stock Truth-creating event per the Backbone Roadmap. |
| Authority (approval / execute / post / reverse distinction) | **Applicable, partially evidenced** | GRV-F02 distinguishes "validate" (execute) from mere draft; GRV-F06 shows a distinct informational post-hoc control (`Should Be Paid`/`Exception`). Full approval-chain semantics (who may validate, who may override) — `Unknown`, source/runtime required. |
| Period / reversal | **Unknown** | GRV-F07 (reversal) is entirely unevidenced this round; period-close interaction with a receipt's valuation timing is not evidenced. |
| Company / data scope (multi-company, multi-tenant) | **Unknown** | No documentation page fetched this round addresses multi-company behavior of receipts, valuation, or bill control. Flagged as GAP-GRV-06. |
| Audit / event | **Unknown** | No documentation evidence this round on what audit trail or event is emitted when a receipt is validated, a backorder is created, or a bill moves to `Exception`. |
| Automation / integration | **Applicable** | The PO → Receipt → (Backorder) → Valuation → Vendor Bill chain is itself a documented, systemic integration; the "should be paid" flag is explicitly described as system-computed, not manual. |

## Reading this matrix

`Applicable` here means the documentation shows the control dimension is *engaged* by this function set — it does not mean the control has been verified to work correctly, or that its precise mechanism is known beyond what is stated in `06_BUSINESS_RULE_REGISTER.md`.
