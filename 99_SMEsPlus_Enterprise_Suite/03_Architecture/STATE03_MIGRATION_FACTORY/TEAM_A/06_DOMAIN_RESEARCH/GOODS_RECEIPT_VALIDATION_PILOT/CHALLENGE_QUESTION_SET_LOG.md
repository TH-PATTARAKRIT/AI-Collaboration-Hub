> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Challenge Question Set (CQS) Log — GMVQ-equivalent, renamed per Boss ruling to avoid collision with existing State-02 GMVQ | Master Prompt §9

# CHALLENGE QUESTION SET (CQS) LOG

Used only as a Challenge Question Source per Master Prompt §9: `question → function/control hypothesis → trace/validate → Confirmed / Contradicted / Conditional / Unknown`. No denominator, no percentage, no round cap. A question is closed only when validated to target V, evidenced Not Applicable, or transparently registered Unknown.

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-GRV-01 | Is physical receipt always a single-step vendor→stock move? | "Receipt is always one atomic movement" | **Contradicted** | Documentation shows 1/2/3-step configurable routing (EV-GRV-01/02/03). |
| CQS-GRV-02 | Is a partial receipt automatically split into a backorder without any user action? | "Backorder creation is silent/automatic" | **Conditional** | Documentation describes an edit-then-validate user action producing the backorder, and a separate explicit split action — not evidenced as a fully silent automatic process (EV-GRV-01, forum-corroborated). Needs runtime confirmation for the exact trigger boundary. |
| CQS-GRV-03 | Does landed-cost allocation require perpetual (automatic) inventory valuation? | "Landed cost only works with real-time/automatic valuation" | **Contradicted (material finding)** | Documentation states landed cost works with manual OR automatic valuation, gated instead by costing method being FIFO or AVCO (EV-GRV-06). Design implication: do not gate a landed-cost feature on valuation mode. |
| CQS-GRV-04 | Does three-way matching hard-block vendor-bill payment until goods are received? | "3-way match is a hard payment block" | **Conditional / not confirmed as hard block** | Documentation describes an informational `Should Be Paid` / `Exception` flag on the bill, explicitly stated not to block edits or show an error (EV-GRV-07). Whether the actual *payment execution* step enforces a hard check is `RUNTIME VERIFICATION REQUIRED` — this is the one sub-question left genuinely open. |
| CQS-GRV-05 | Once a FIFO-valued receipt is posted, is its unit value permanently fixed? | "FIFO valuation is immutable once posted" | **Contradicted** | Documentation describes an explicit "Adjust Valuation" action for FIFO/AVCO incoming moves (EV-GRV-04/05 synthesis). |
| CQS-GRV-06 | Does every receipt automatically reconcile to Accounting in real time? | "Every stock movement always creates an immediate journal entry" | **Conditional** | Entirely dependent on the Automatic (perpetual) vs Manual (periodic) valuation configuration; documentation states manual/periodic is the *default* (EV-GRV-05). Design implication: do not assume real-time GL posting as the baseline case. |

## Status

`CLOSED (documentation-tier)`: CQS-GRV-01, 03, 05 — clear, cited, no residual doubt at this evidence tier.
`OPEN (Targeted Validation Needed)`: CQS-GRV-02, 04, 06 — documentation gives a directional answer but the precise mechanical boundary needs Source or Runtime evidence before it can be relied on in any downstream design discussion.

No round cap applied. Further questions may be added on Material Delta (e.g. once GRV-F07 reversal evidence is obtained).
