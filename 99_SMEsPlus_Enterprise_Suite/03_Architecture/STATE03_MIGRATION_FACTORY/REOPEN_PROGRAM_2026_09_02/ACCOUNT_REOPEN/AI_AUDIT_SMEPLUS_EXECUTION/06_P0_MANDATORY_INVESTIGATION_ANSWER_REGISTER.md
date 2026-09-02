# P0 Mandatory Investigation Answer Register

Each of the 12 P0 questions from the governing prompt, answered strictly from evidence actually located this session. "NO EVIDENCE FOUND" is used verbatim where nothing was located, rather than inferring an answer.

---

### P0-1. Is COA-G03 ready for fresh independent audit, and what exact evidence supports or blocks it?

**Corrected finding — the governing prompt's premise does not match reality.** The literal string "COA-G03" appears in the corpus, but not with the status the prompt assumes. Per `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`, the real 8-gate sequence is:
- **COA-G01 = "Source Baseline Reconciliation."** Currently **`HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING`** (verbatim, `COA_G01_CORR5_POST_PUBLICATION_CLOSURE.md` / `SESSION_CLOSURE_R5.md`), after 5 correction rounds (CORR1–CORR5). Open blockers: **N-04** — the authoritative Thai financial-statement PDF (`งบการเงิน 2567.pdf`) returned "not found" on two independent tool calls, Boss must reissue file access; **N-05** and **C-03** both explicitly flagged "ACCEPTED RESIDUAL UNKNOWN / BOSS DECISION REQUIRED"; PMO Verification and Boss Gate Decision both "PENDING." CORR5 itself is "SUBMITTED FOR CHATGPT INDEPENDENT RE-AUDIT" — not yet re-audited.
- **COA-G02 = "NOT STARTED / NOT AUTHORIZED."**
- **COA-G03 = "AI Semantic Consolidation"** (classify source accounts by business meaning, consolidate equivalent rows to one canonical account). It is explicitly a **future gate, blocked behind G02**, and has not started. `COA_G01_CURRENT_BLOCKER_AND_DISPOSITION_MATRIX_R5.md` states the final canonical account count is "OUT OF SCOPE / PROHIBITED IN CORR5 … Determined only at COA-G03."

**Answer: G03 is not ready for audit because it has not started — G01 is the gate actually in-cycle, and G01 itself is on HOLD, not ready-for-audit.** This directly contradicts the governing prompt's Section 10 default ("COA-G01 | CARRY_FORWARD - CLOSED unless direct contradiction is found") — a direct contradiction was found. See [08_GATE_STATUS_AND_ROUTING_REGISTER.md](08_GATE_STATUS_AND_ROUTING_REGISTER.md).

*Separately, not to be confused with the above:* the Team B **conceptual design blueprint** for Accounting Core (capability model, invariants, domain boundaries — B01–B21) is a different, already-closed matter — Boss ruled it **"APPROVE WITH CONTROL"** (`AH_BOSS_FINAL_GATE_RULING.md`). Development/production are explicitly **not** authorized by that ruling.

---

### P0-2. Is WHT fully evidenced for purchase-side, sales-side, service-only, multi-rate, payment, certificate and filing scenarios?

**No — substantive but explicitly incomplete, per Boss's own recorded decision.** From branch `audit/account-wht-grpa-m18-closure-010` (tip `fe356f7`, "Boss Partial Acceptance decision recorded"):
- Domain ownership resolved: WHT confirmed Accounting/Tax-owned, zero Inventory (`stock.*`) dependency (`05_ACC_WHT_FINAL_DISPOSITION_AND_BOSS_RECOMMENDATION.md`).
- **Purchase-side: PARTIAL** — net-of-WHT payment math proven and test-backed, but "service-only" is an unenforced convention and certificate issuance is a manual wizard step (`01_ACC_WHT_PURCHASE_SIDE_PROOF.md`).
- **Sales-side: PARTIAL** — code path exists, but no dedicated WHT-receivable GL account type, no customer-certificate tracking model, zero test coverage (`02_ACC_WHT_SALES_SIDE_PROOF.md`).
- **Multi-rate: HIGH GAP, unresolved** — the source module drops WHT GL tagging entirely when a single payment carries 2+ distinct WHT rates (`wizard/account_payment_register.py:64`, gated on `len(wt_tax) == 1`) (`08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md`, `09_ACC_WHT_MULTI_MODULE_TARGETED_PROOF.md`).
- **Boss's own recorded decision:** domain transfer accepted; **full WHT closure explicitly NOT accepted**; `ACC-WHT-06` (multi-rate) held at HIGH pending Boss confirmation of whether `l10n_th_withholding_tax_multi` is part of the intended module baseline. A 10-item `LEGAL_TAX_REVIEW_REQUIRED` register remains open in every deliverable.

---

### P0-3. Is 50 TWI certificate behavior evidenced, including source, mapping and rendering boundary?

**Partially.** `03_ACC_WHT_50TWI_GAP_CLOSURE.md` (branch `audit/account-wht-grpa-m18-closure-010`): a suspected branch-numbering gap was resolved as a non-defect, but **3 tax-form checkboxes and 2 WHT-condition checkboxes are genuinely missing** from the print template — classified **`REQUIRES FORM UPDATE`**, pending legal-tax review. (The root-corpus snapshot alone shows **NO EVIDENCE** for this question — the branch is materially ahead of the stale root copy here.)

---

### P0-4. Are PND3 and PND53 reporting/export boundaries evidenced?

**Partially, with an open code-quality risk.** `04_ACC_WHT_PND3_PND53_FILING_PROOF.md`: the CSV export code path is real and tested, but a **silent monkey-patch** was found — `tax_report_pnd.py` is duplicated across two modules, making output deployment-dependent — and the "WHT Condition" export column is **hardcoded to `'1'`** rather than derived. No SMEsPlus-native export-boundary design exists yet; this is proof-of-behavior against the old source system, not a target design.

---

### P0-5. Is monthly close evidenced as monthly carry-forward rather than a vague year-end process?

**Yes — resolved.** Period is modeled as a bounded, independently-openable/closeable span (`B03_DOMAIN_BOUNDARY_MODEL.md` §2); Fiscal Year is "composed of one or more contiguous Periods" (`B07_CONCEPTUAL_INFORMATION_MODEL.md` §1/§3); CAP-04 "Period Control" (`B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md`) is the recurring open/close mechanism, explicitly glossed as "an ordinary Period close (month/quarter)" (`B08`, line 89). Tested via named regression scenarios ("Month-End Close Operator" persona, "Jan + Feb YTD P&L after Jan month close") in `B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md`.

---

### P0-6. Is month 12 evidenced as both monthly close and year-end close where applicable?

**Resolved — and the answer is deliberately "no, not combined."** A prior correction round (`CORR-B2-03/04`, finding `M-AUD-05` in `B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md`) explicitly rejected generalizing year-end behavior onto every ordinary Period close. The corrected model keeps them separate: `PeriodClosed` (CAP-04) is "a posting lock only"; `FiscalYearClosed` (CAP-09) is a separate, higher-authorization action, independently timed from any period boundary. `B07` §1e: a Fiscal Year being "Elapsed-but-not-yet-Closed for a real, often multi-week window… is normal, expected operation." `B11_EXCEPTION_FAILURE_MODEL.md` scenario 20 is built around this gap being tolerated by design.

---

### P0-7. Is retained earnings under Equity / Account Category 3 evidenced and reconciled to income/expense close?

**Yes — resolved, with one disclosed residual.** `B07_CONCEPTUAL_INFORMATION_MODEL.md` §1b–1f defines Current Earnings and "Reported Retained Earnings" (direct-posted RE balance + every elapsed Fiscal Year's Current Earnings) as a non-overlapping decomposition of Reported Equity. `B05_ACCOUNTING_INVARIANT_BASELINE.md` BINV-10 (rewritten 4 times) and BINV-14 formalize the guarantee: no Entry ever posts a closing transfer, and Reported Equity is a pure function of committed Entries + elapsed Fiscal Years, independent of *when* a close is declared. `B10_CANONICAL_MIGRATION_REQUIREMENTS.md` MG-C15 requires exactly one migrated Equity account per Company designated as "the" RE account. **Residual (disclosed, not hidden):** that designation is assumed correct/unique on migration, not independently re-derived (BINV-14 note).

---

### P0-8. Is Account × Inventory valuation/COGS interface clear enough to route to Joint Session without Account falsely closing Inventory Stock Truth?

**Yes — clearly resolved.** `B03_DOMAIN_BOUNDARY_MODEL.md` §3/§4: Inventory/Costing owns valuation methodology (FIFO / weighted-average / standard cost) as "the result of a valuation method decided elsewhere"; Accounting Core owns only committing the resulting value movement as a balanced Entry (CAP-02). Explicitly out of scope for Accounting Core: "Inventory valuation methodology." This is consistent with the Full Reopen Program's own framing (`42e04e6`): Accounting = "Financial Truth Center," Inventory = "Stock Truth Center," with a named Joint track. **Routed to Joint Session, not claimed as Account-only closure** — see [09_ACCOUNT_X_INVENTORY_INTERFACE_QUESTION_REGISTER.md](09_ACCOUNT_X_INVENTORY_INTERFACE_QUESTION_REGISTER.md).

---

### P0-9. Are SaaS tenant/company isolation, standard template, company instance and immutable versioning evidenced?

**Mixed.** Tenant isolation (CO-10, `B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md`) and company isolation (CO-09, CAP-05, BINV-03) are **resolved**. **Standard template mechanics are explicitly OPEN** — `B13_DESIGN_OPTION_TRADEOFF_REGISTER.md` DT-03 recommends an option but states plainly: "Not approved… requires its own follow-up design attention regardless of Boss's gate decision," and is listed as an open assumption through Round 7. Immutable versioning is evidenced for specific facts (BINV-12 Recorded-At, BINV-09 Account Category freeze, versioned Fiscal Calendar) rather than as one unified template-versioning concept. Upgrade-preview and upgrade-audit-trail specifically were **not directly evidenced** in this pass.

---

### P0-10. Is migration reconciliation evidenced across GL, TB, subledger, AR/AP aging, assets and historical continuity?

**Partially.** GL/TB reconciliation and historical continuity are **resolved**: `B10_CANONICAL_MIGRATION_REQUIREMENTS.md` MG-C11 requires the migrated Raw Cumulative Trial Balance to reconcile exactly to the source system's TB as of cutover; MG-C04/MG-C07 require historical Entries/Periods to import already-Consumed/Closed; MG-C05/MG-C09 require correction-linkage and messy change-history to migrate un-laundered. **AR/AP aging and fixed-asset roll-forward are explicitly NOT evidenced** — `TEAM_A/A3_DOMAIN_PRIORITIZATION.md` states both are "Deferred, captured as dependencies only… with no research performed." This is a genuine scope absence, not a discovered defect.

---

### P0-11. Are clean-room and source-provenance controls sufficient to prevent source architecture leakage?

**Yes — thoroughly evidenced, the best-documented area found.** `B14_CLEAN_ROOM_PROVENANCE_MATRIX.md`: "Critical Vendor-Derived Design Risk = 0"; explicit review of the only 3 vendor-behavior terms appearing anywhere in B02–B13, confirming none were adopted. `TEAM_A/05_QUARANTINE/CLEAN_ROOM_QUARANTINE_REGISTER.md` / `21_QUARANTINE_REGISTER.md`: "No OEEL-1 or OPL-1 source body was opened at any point"; proprietary Odoo Enterprise modules held as black-box/metadata-only; undeclared-license modules quarantined, not read for design content. `19_PROVENANCE_REGISTER.md`: no finding rests on unavailable provenance tiers. The source system being ported from is **Odoo**, not SAP or Salesforce — SAP Business One and NetSuite appear only as external comparison points, explicitly logged as never adopted as design source.

---

### P0-12. Is AI authority limited to proposal/classification while deterministic financial controls and Boss approval remain non-probabilistic?

**Yes, at the governance/process level; not applicable as an in-product feature.** Accounting Core's own functional design (CAP-01–09, BR-01–15, CO-01–16) is 100% deterministic rules — no AI-driven classification or proposal mechanism exists anywhere inside it. `B09` CO-16 explicitly requires materiality be "a policy input, never computed or invented by this domain's design," supplied by a human Controller/CFO role. Every gate document in the `BOSS_GATE` chain repeats verbatim: **"Boss is the sole Final Approver. No Evidence = No Progress. Never Skip Gate."** `TEAM_A/01_SOURCE_REGISTRY/A0_GOVERNANCE_VERIFICATION.md` names the AI executor lineage explicitly (Claude, ChatGPT) performing research/design/audit, never final approval. This is independently corroborated by the project's own `.claude/skills/smeplus-state02-governance-controller` skill definition, which states plainly: "Boss remains Sole Final Approver; Claude Code is Preparer/Executor only."

---

## Summary table

| P0 | One-line disposition | Evidence strength |
|---|---|---|
| 1 | G03 not started; G01 (the gate actually in-cycle) is HOLD, not ready | Strong — direct, current |
| 2 | WHT partial; multi-rate is a HIGH open gap; Boss issued Partial Acceptance only | Strong — direct, current |
| 3 | 50-TWI: 5 form fields missing, pending legal-tax review | Strong — direct, current |
| 4 | PND3/53: real but has a silent duplication risk + hardcoded field | Strong — direct, current |
| 5 | Monthly close: resolved, recurring by design | Strong |
| 6 | Month-12: resolved — deliberately NOT merged with year-end | Strong |
| 7 | Retained earnings: resolved, 1 disclosed residual | Strong |
| 8 | Account×Inventory boundary: resolved, clean | Strong |
| 9 | Isolation: resolved. Template: OPEN. Versioning: partial | Mixed |
| 10 | GL/TB: resolved. AR/AP + assets: no research performed | Mixed |
| 11 | Clean-room: resolved, rigorously documented | Strong |
| 12 | AI control: resolved at governance level; not a product feature | Strong |
