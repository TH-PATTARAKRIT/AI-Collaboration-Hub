# P04 — POST-DEPRECIATION CONTINUOUS INTERNAL EQUIPMENT USAGE

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-06`. **Everything below the evidence line is a
`DESIGN CANDIDATE`.** The estate has nothing to configure here.

---

## 1. Evidence — what exists

| Question | Answer | Basis |
|---|---|---|
| Any state, flag or event for *"fully depreciated"*? | **No** | `CQ-P04-10` §4 — the only end-of-life logic is the amount clamp |
| Any post-depreciation cost pool? | **No** | no model, no field |
| Can `account.asset` post to an off-balance account? | **No — domain-excluded on all three account fields** | **`P04-F-154`** |
| Is residual value consumed by anything? | **No** | `salvage_value` is excluded from the depreciable base and untouched until derecognition |
| Original daily ratio available as a reference? | **Yes, derivable**: `original_value − salvage_value` over `asset_lifetime_days` | `CQ-P04-02` §2 |

> **`P04-F-154` is the hard constraint.** The carried policy says off-balance double entries
> pair with off-balance. **The asset engine's own accounts cannot be off-balance**, so a
> managerial internal-usage ledger **cannot be built as a configuration of `account.asset`.**
> It must be a separate mechanism. This is the single most consequential design fact in this CQ
> and it is a **fact**, not a preference.

## 2. DESIGN CANDIDATE — the model

| Element | Candidate |
|---|---|
| **Trigger** | Financial depreciation complete (`value_residual = 0`) **and** the equipment remains operational |
| **Residual role** | **Reference, not cap.** Financial residual book value is not consumed — carried policy, and the estate agrees by omission (§1) |
| **Rate reference** | The asset's **original daily ratio**, derivable from source (§1). Whether it is the right rate is a Boss choice, not a fact |
| **Cost pool** | A **managerial period pool**, posted off-balance-to-off-balance, **outside** `account.asset` |
| **Stop conditions** | Equipment ceases to be operational; disposal/derecognition; or an explicit management stop event |
| **Disposal separation** | Financial derecognition and managerial stop are **two events**; neither implies the other |
| **Prohibited** | Cross-posting the managerial pool into financial WIP; re-depreciating a fully depreciated asset |

## 3. Unresolved choices — named, not guessed

| # | Choice | Why it cannot be settled from evidence |
|---|---|---|
| 1 | Is the managerial rate the original daily ratio, a replacement-cost rate, or a policy rate? | All three are defensible; nothing in the estate expresses a preference |
| 2 | Does the managerial pool reconcile to anything, or is it purely statistical? | Determines whether it needs the 100 % invariant of `CQ-P04-05` |
| 3 | Which off-balance account structure pairs with which | Requires a chart decision (**P08**) |
| 4 | Does the equipment record or the asset record own the managerial life? | Depends on the cardinality decision in `P04-F-149` |

## 4. Disposition

> **`CQ-P04-06` — `BOSS DECISION REQUIRED — DECISION PACKAGE READY`**, with the factual half
> `FACT VERIFIED`: **no mechanism exists, and one specific route is closed off by
> `P04-F-154`.** Four named choices, none resolved by inference. Off-balance chart structure
> routed to **P08**.
