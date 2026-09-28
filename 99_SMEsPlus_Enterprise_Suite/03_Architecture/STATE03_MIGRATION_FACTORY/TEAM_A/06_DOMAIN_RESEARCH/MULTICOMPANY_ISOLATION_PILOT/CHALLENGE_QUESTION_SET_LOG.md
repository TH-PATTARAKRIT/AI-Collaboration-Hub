> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx9)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-MCT-01 | Is multi-company isolation "all or nothing," or configurable per-behavior? | "Multi-company means everything is either shared or separate" | **Contradicted** | Inter-Company Transactions has 4 independently toggleable behaviors; Chart of Accounts can be shared or not, independent of that. |
| CQS-MCT-02 | Can a user be natively restricted to one warehouse the same way a warehouse is bound to one company? | "Symmetric ease — if warehouse→company is a simple field, user→warehouse should be too" | **Contradicted** | Warehouse→company is a required native field; user→warehouse restriction requires manually built record rules/groups, evidenced by community demand and a third-party app market. |
| CQS-MCT-03 | Does inter-company stock-move sync carry its own independent valuation on each side, or copy the source valuation across? | Assumed: independently computed, respecting each company's own accounting | **Unknown** | Not evidenced by documentation this round — a real, unresolved question given how much this Deep Study has already found about valuation-timing nuance. |

## Status

`CLOSED (documentation-tier)`: CQS-MCT-01.
`CLOSED (documented absence, not documented mechanism)`: CQS-MCT-02.
`OPEN`: CQS-MCT-03 — flagged as a genuinely important open question given the rest of this Deep Study's valuation-timing findings.
