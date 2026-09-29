# STATE03 Valuation-Timing Cross-Gx Contradiction Matrix

Document ID: `STATE03-VALUATION-TIMING-CONTRADICTION-MATRIX`
Version: 1.0
Date: 2026-09-29
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture & Knowledge Acquisition Deep Study
Boss: Sole Final Approver
Status: `Material Finding — Independently Unverified` (Boss ruling 2026-09-29) — routed to `CHATGPT_AUDIT` per `STATE03_CHATGPT_AUDIT_PACKAGE_BGQ03.md`

## 1. Purpose

Boss's 2026-09-29 ruling on `BGQ-03` requires: "Valuation Timing Finding... ยังไม่ถือเป็น Canonical Architecture Truth จนกว่า Independent Audit จะยืนยัน... สถานะเป็น `Material Finding — Independently Unverified`." This matrix is the single consolidated evidence chain for that finding, so `CHATGPT_AUDIT` (and Boss) can review the whole reconciliation in one place instead of across six pilot folders.

This document does not itself change any finding. It restates, with exact locations, what was found, where, in what order, and why the resolution is flagged as independently unverified.

## 2. The chain

| Step | Gx | Function | What was found | Status before Gx6 | File |
|---|---|---|---|---|---|
| 1 | Gx1 | `GRV-F04` — Inventory valuation at receipt | Generic claim: "perpetual valuation posts in real time whenever stock enters/leaves the warehouse" | Documentation-tier, unqualified | `GOODS_RECEIPT_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` |
| 2 | Gx2 | `SDV-F05` — COGS/valuation timing at delivery | More specific, conflicting claim: Odoo 19 "no longer creates journal entries upon physical receipt or delivery"; posts "at the time of the financial transaction (vendor bill/customer invoice)," with a Stock Variation buffer account | **Evidence Conflict with Step 1** — flagged as such, not silently picked | `SALES_DELIVERY_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md`; `22_UNKNOWN_AND_GAPS.md` `GAP-SDV-01` |
| 3 | Gx4 | `IAV-F03` — Financial posting timing (adjustments) | Third data point: inventory adjustments post immediately, unconditionally | **3-way Evidence Conflict** (Step 1 vs. Step 2 vs. Step 3 all looked different) | `INVENTORY_ADJUSTMENT_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md`; `22_UNKNOWN_AND_GAPS.md` `GAP-IAV-01` |
| 4 | Gx6 | `PCO-F03` — Month-end Stock Closing + accrual entries | **THE RESOLVING FINDING**: no entry at movement; entry at invoice time; month-end Stock Closing + self-reversing accrual (Reversal Date) sweeps up anything uninvoiced by period end. Reframes Step 1 as the incomplete/generic half, Step 2 as the accurate half, and Step 3 as consistent (an adjustment has no future invoice to defer to, so it *is* its own financial transaction) | Resolved (documentation-tier, high confidence) — reached by the **same session** that found Steps 1–3 | `PERIOD_CUTOFF_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` `PCO-F03` |
| 5 | Gx7 | `MFG-F01`/`MFG-F02` — Manufacturing consumption/completion | Confirms the rule a third way: manufacturing postings are automatic/immediate because manufacturing has no external vendor-bill/customer-invoice equivalent — consistent with, not a fourth exception to, Step 4 | Confirmation, same reconciling logic, same session | `MANUFACTURING_VALUATION_PILOT/01_EXECUTIVE_RESEARCH_SUMMARY.md` |
| 6 | Gx8 | `RTG-F02`/`RTG-F03` — Consumable/Storable expense timing | Confirms the rule a fourth way via an independent *documentation source* (not an independent *reviewer*): storable COGS posts at customer-invoice time, consumables expense at vendor-bill time | Confirmation, same reconciling logic, same session | `PRODUCT_ROUTING_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` `RTG-F02`/`RTG-F03` |

## 3. Why this is flagged, not just recorded as good research

The reconciliation (Step 4) is genuinely well-evidenced and internally consistent, and the addendum trail is auditable — nothing in Steps 1–3 was deleted or silently rewritten; each carries a "RESOLUTION UPDATE" cross-reference to Step 4. That is correct process.

What it is **not**: independent verification. One continuous TEAM_A session raised the 3-way conflict (Steps 1–3), then resolved its own conflict (Step 4), then confirmed its own resolution twice more (Steps 5–6). This is exactly the scenario the 9 Veto Council Charter's Special Team mechanism and the Independent Challenge Rule's "two or more Council mandates materially disagree" / "conflicting evidence" triggers exist for (see Council 04 finding in `00_PRE_PROMPT_9VETO_CHALLENGE_STATE03_DEEP_STUDY_MASTER_PROMPT.md`), and no Special Team or independent reviewer was activated before this document.

None of Steps 1–6 have reached AWT (runtime) confirmation — every one remains at documentation-tier (V2), evidenced by WebSearch-synthesis only (direct `WebFetch` to odoo.com blocked in this container).

## 4. Current status (per Boss ruling 2026-09-29)

`Material Finding — Independently Unverified.`

Not: `Resolved`, not: `Canonical Architecture Truth`, not: usable as a frozen input to TEAM_B design until `CHATGPT_AUDIT` (or another independent reviewer) confirms it, or Boss otherwise accepts it.

## 5. What would close this

Per `STATE03_BOSS_GATE_QUEUE.md` `BGQ-03` and the CHATGPT_AUDIT package (`STATE03_CHATGPT_AUDIT_PACKAGE_BGQ03.md`):

1. `CHATGPT_AUDIT` (or an independent Claude Code session with no prior context) independently re-derives or falsifies Step 4's reconciliation from the same class of Odoo 19 documentation.
2. AWT (runtime) confirmation once `BGQ-04`'s environment is authorized — this closes the V2 ceiling, not the independence gap, but is the other half of full confidence.

Both are Boss-gated or audit-gated; neither is self-executable by TEAM_A.
