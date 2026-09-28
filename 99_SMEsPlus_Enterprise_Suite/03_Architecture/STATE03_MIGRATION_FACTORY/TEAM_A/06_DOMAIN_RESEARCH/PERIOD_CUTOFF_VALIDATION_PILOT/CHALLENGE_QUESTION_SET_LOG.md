> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx6)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-PCO-01 | Are the Gx1/Gx2/Gx4 valuation-timing findings genuinely contradictory, or reconcilable once the full architecture is understood? | "These are three incompatible claims" | **Resolved — reconcilable, not contradictory** | The month-end Stock Closing/accrual mechanism (EV-PCO-02) explains all three: movement doesn't post (Gx1's claim was the incomplete/older picture), invoice posts (Gx2, confirmed), and period-end sweeps up the rest (this Gx) — adjustments (Gx4) post immediately because they have no future invoice to defer to, which is consistent, not contradictory, once framed this way. |
| CQS-PCO-02 | Is a Hard Lock truly irreversible, with no documented correction path? | Assumed: some override exists | **Confirmed as documented, mechanism for post-lock correction unconfirmed** | Documentation states Hard Lock is irreversible "to meet accounting requirements in certain countries" — no correction mechanism found this round; logged as an open gap, not assumed to not exist. |
| CQS-PCO-03 | Does Stock Closing happen automatically, or is it a required manual monthly action? | Assumed: automatic | **Unknown** | Documentation describes a "Generate Entry" action without stating whether it can be scheduled — not confirmed either way. |

## Status

`CLOSED (documentation-tier, high confidence)`: CQS-PCO-01 — the headline resolution of this Gx.
`CLOSED (as documented, mechanism gap remains)`: CQS-PCO-02.
`OPEN (Targeted Validation Needed)`: CQS-PCO-03.
