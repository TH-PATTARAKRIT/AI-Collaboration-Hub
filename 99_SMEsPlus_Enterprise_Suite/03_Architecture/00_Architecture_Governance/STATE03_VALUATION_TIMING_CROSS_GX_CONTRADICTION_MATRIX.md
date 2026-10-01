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

## 4.1 Related but distinct evidence found since (2026-09-29) — not part of the resolved chain, not self-confirming it further

While closing an unrelated documentation gap (`GAP-MFG-01`, `MFG-F05` — negative-inventory revaluation during a manufacturing order), this session found two sub-official-tier sources (a forum thread, pre-Odoo-19; an Odoo-partner blog, Odoo 19) that **disagree on Odoo version**: the older-version source describes an automatic "Revaluation of WH/MO/XXX (negative inventory)" journal entry; the Odoo 19 blog states raw-material cost is booked only at vendor-bill time, with no such automatic entry in 19. If the Odoo 19 reading holds, it would be consistent with (not contradicting) Step 4's reconciliation — but this is explicitly **not** treated as a further self-confirmation of the chain above. It is recorded here only as related evidence for `CHATGPT_AUDIT` to weigh alongside the main chain, at a lower evidence tier (V1, not V2) than Steps 1–6. Full detail: `MANUFACTURING_VALUATION_PILOT/06_BUSINESS_RULE_REGISTER.md` MFG-F05.

## 4.2 Further related evidence (2026-09-29, `M1` — Manufacturing/BOM/Routing module, not a Gx unit)

`BRP-F03` (Subcontracting BOM) found that a subcontractor's fee is captured into the Finished Goods Valuation Account at vendor-bill-posting time — the same "post at financial-transaction time" pattern as the main chain above. Recorded here as an additional, disclosed data point for `CHATGPT_AUDIT` to weigh, at the same discipline as §4.1's `MFG-F05` entry: **not** treated as a further self-confirmation of the chain, since it comes from the same session/lineage as the original finding. Full detail: `MANUFACTURING_BOM_ROUTING_PILOT/06_BUSINESS_RULE_REGISTER.md` BRP-F03.

## 4.3 Source/dump finding on the same chain (2026-09-30) — `SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`, `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`

A separate Source/Dump Deep Research Worker (Boss's local Claude Code session, read-only against `odoo-19.0.post20260921` Community source) reviewed this same chain against actual code, consolidated in `TEAM_A/04_EVIDENCE_PACKS/STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` `D-06`. This is a materially different kind of input than §4.1/§4.2 above — those were additional documentation-tier data points from the *same* session/lineage; this is source-code-tier evidence from an *independent* session, though still not runtime and still not the CHATGPT_AUDIT/independent-reviewer step this matrix requires to close. **This finding does not upgrade the chain's status — it remains `Material Finding — Independently Unverified`** — but it identifies specific points of agreement and disagreement worth handing to whichever reviewer eventually takes this up:

- **Step 1 (`GRV-F04`)**: source shows the generic "posts in real time at every movement" claim is **contradicted by source, not merely incomplete** — ordinary receipt/delivery moves to/from a Supplier/Customer location do not themselves create a journal entry in the standard UI configuration (an inference from code reading, not a runtime observation).
- **Step 3 (`IAV-F03`)**: the "adjustments post immediately, unconditionally" claim is **conditional** on the product's category having a configured Loss Account — not evidenced as truly unconditional.
- **Step 4 (`PCO-F03`)**: the source worker's reading draws a distinction this document's Step 4 did not make explicit — **Stock Closing itself is not a self-reversing entry** (it directly adjusts the accumulated subledger-vs-GL gap); the Reversal-Date-bearing, self-cancelling mechanism belongs to the separate Accrued Orders/WIP wizards. Both exist and both matter to the overall reconciliation, but they are not the same mechanism, and Step 4's original wording conflated them.
- **No code implementing a distinctly-named negative-inventory "revaluation" entry** was found (an absence finding, consistent with — not further self-confirming — §4.1's `MFG-F05` Odoo-19-blog reading).

**Limitation, stated by the source worker itself**: this is `SRC-STATIC` + `INFER` evidence — reading code and inferring behavior, not observing a running system — and is `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`: the actual `iTEST02` test database carries ~696 non-Community tables, and at least one license-open third-party module (`cr_effective_date_entries`) manipulates picking accounting dates after the fact in a way that could interact with this chain's timing assumptions (its own code references a model that does not exist in Odoo 19, a separate compatibility concern — see `MANUFACTURING_VALUATION_PILOT/22_UNKNOWN_AND_GAPS.md`). This session (STATE03 Integration/Architecture Knowledge Owner) never read the source directly and has not declared any part of this chain closed or reopened on the strength of this finding alone.

## 4.4 Second independent-lineage corroboration (2026-10-02) — DeepSeek correction packet `U10-R2`, plus a distinct, related inert-hook finding (`U10-R1`)

A second, separate research lineage — DeepSeek (Primary Source/Dump Research Worker, running through its own Claude Code harness, Atomic Boundary `U10`, correction packet `U10-R2`) — independently re-derived the same lock-date mechanism `GAP-PCO-01` already recorded from the prior (2026-09-30) source worker: posting an entry inside a locked period does **not** refuse it; the entry's date is silently shifted to the first open date not blocked by the violated lock(s), and the stock-closing entry posts through the same path so the shift applies to it too (`VDR-U10R2-C001`–`C004`, source pointers `account/models/account_move.py:5704/5706`, `stock_account/models/res_company.py:78`). This is **independent corroboration from a second lineage**, not a new claim — it does not change the §4 status (`Material Finding — Independently Unverified`), but it does strengthen the evidence tier for the lock-date half of this question specifically: two separately-sourced static-code readings now agree. Still not AWT/runtime-confirmed; still not `CHATGPT_AUDIT`-closed. DeepSeek itself flags the per-lock-type date outcome and its effect on numbering/period reports as needing execution (`RUNTIME/AWT_REQUIRED`).

**Distinct, related finding, same packet set (`U10-R1`, correction request CR-004)**: a full-tree search found that two hooks U10's original evidence credited with "COGS delta booking/refund" at invoice time (`_stock_account_get_last_step_stock_moves`, `_get_related_invoices`) have **no caller anywhere in the addons tree** outside their own override chain (sales-delivery/purchase-receiving extend and call `super()`, but nothing invokes the base method) — i.e. these two specific hooks appear **inert in this revision**. This is **not** the same mechanism as the Stock-Closing/lock-date chain above and does not itself resolve or reopen the main `GRV-F04`/`SDV-F05`/`PCO-F03` chain — it concerns a narrower, COGS-matching-at-invoice-time code path. Recorded here only because it touches the same general valuation-timing neighborhood and should be in front of whoever eventually examines that mechanism in depth (`CHATGPT_AUDIT` or AWT). This session (verifier) finds both `U10-R1` and `U10-R2` internally consistent, properly hedged (FACT for direct reads, INFERENCE labelled for the "no caller found" / "effect per lock type" conclusions, RT flagged where runtime is genuinely required) — classified `ACCEPTED` at the static-evidence level per the 2026-10-01 Standing Instruction; this session cannot independently re-derive the source pointers itself (no source-tree access). Full verifier detail: `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` §10.

**Third confirmation (2026-10-02, `TXA2`, Thai Tax Core lane)**: the same lock-date "posted entry inside a lock is re-dated to the first open date, not refused" mechanism was independently re-derived a third time, as part of the Thai Tax Core boundary `TXA2` (CAP-TXA2-03), without reference to `U10-R2`. Three separately-sourced static-code readings (2026-09-30 source worker, `U10-R2`, `TXA2`) now agree on this specific sub-mechanism. Status unchanged (`Material Finding — Independently Unverified`, `RUNTIME/AWT_REQUIRED` for exact per-lock outcome) — agreement across three static reads strengthens confidence further but still does not substitute for `CHATGPT_AUDIT` or AWT execution. Full verifier detail: `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` §23.

## 5. What would close this

Per `STATE03_BOSS_GATE_QUEUE.md` `BGQ-03` and the CHATGPT_AUDIT package (`STATE03_CHATGPT_AUDIT_PACKAGE_BGQ03.md`):

1. `CHATGPT_AUDIT` (or an independent Claude Code session with no prior context) independently re-derives or falsifies Step 4's reconciliation from the same class of Odoo 19 documentation.
2. AWT (runtime) confirmation once `BGQ-04`'s environment is authorized — this closes the V2 ceiling, not the independence gap, but is the other half of full confidence.

Both are Boss-gated or audit-gated; neither is self-executable by TEAM_A.
