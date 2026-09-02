# 9 Special Team Challenge — Deep-Dive Findings Matrix

Separate from the Veto Council. Deep-dive investigation body for material deltas, contradictions, unknowns and evidence gaps (governing prompt Section 7). 9 findings, `ST-01`–`ST-09`.

---

## ST-01 — G01/G02 carry-forward validity
**Required evidence target:** Boss Closure, PMO Verification, contradiction scan.
**Finding:** The governing prompt's Section 10 default rule ("COA-G01 | CARRY_FORWARD - CLOSED unless direct contradiction is found") is **directly contradicted**. Real current state (`COA_G01_CORR5_POST_PUBLICATION_CLOSURE.md`, `SESSION_CLOSURE_R5.md`): **`COA-G01 = HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING`**, after 5 correction rounds, 2 open Boss-decision items (N-05, C-03), 1 open source-access blocker (N-04), PMO Verification and Boss Gate Decision both "PENDING." **`COA-G02 = NOT STARTED / NOT AUTHORIZED"` (verbatim).**
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/`.
**Classification:** **CONTRADICTION CONFIRMED — do not carry forward as closed.**
**Gate impact:** Directly overrides the governing prompt's Section 10 default for G01 and G02. See [08_GATE_STATUS_AND_ROUTING_REGISTER.md](08_GATE_STATUS_AND_ROUTING_REGISTER.md).
**Next controlled action:** Boss decision on N-05/C-03; reissue Thai PDF access (N-04); commission ChatGPT independent re-audit of CORR5.

---

## ST-02 — G03 "389/389" audit readiness
**Required evidence target:** Source-to-canonical map, 13 Do-NOT-Merge controls, reconciliation report.
**Finding:** **NO EVIDENCE FOUND** for the literal figure "389/389" anywhere in the material read this session (root corpus, `ISOLATED_ACCOUNT_CORR5` BOSS_GATE chain, or the WHT branch diff). Separately, COA-G03 ("AI Semantic Consolidation") is confirmed **not started**, blocked behind G02. The "13 Do-NOT-Merge controls" phrase was also not located.
**Evidence location:** Not found; the figure may live inside the 99-file `COA_G01_EVIDENCE/` or 63-file `COA_G01_SOURCE_PORT/` clusters, which were inventoried by filename this session but not exhaustively content-read.
**Classification:** **`HOLD / EVIDENCE REQUIRED`** — genuinely unlocated, not assumed absent from the whole project.
**Gate impact:** Cannot confirm or deny "389/389" readiness; G03 itself is `NOT_YET_REACHED` regardless.
**Next controlled action:** Targeted content search of `COA_G01_EVIDENCE/` and `COA_G01_SOURCE_PORT/STATE03_LOCAL/` (99 + 63 files, not yet deep-read) specifically for this figure and the Do-NOT-Merge control list.

---

## ST-03 — G04 Account Type / Account Group readiness
**Required evidence target:** 36 Base Kernel, Boss 19 active types, account classification proof.
**Finding:** Two suggestively-named documents exist and were inventoried but not content-verified: `COA_STANDARD/DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md` and `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`. Whether they substantiate "36 Base Kernel" or "19 active types" is **unverified this session**. G04 itself is `NOT_YET_REACHED` per the gate sequence (blocked behind G01 HOLD → G02 not started → G03 not started).
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/` (3 files total).
**Classification:** **`HOLD / EVIDENCE REQUIRED`** — files exist, content not verified, gate not yet reached.
**Gate impact:** None yet — G04 correctly remains `NOT_YET_REACHED` regardless of this file's content.
**Next controlled action:** Content-read `COA_STANDARD/` (only 3 files — low-cost) once G01/G02/G03 clear.

---

## ST-04 — WHT completeness
**Required evidence target:** Purchase WHT, Sales WHT, multi-rate WHT, service-only boundary, 50 TWI, PND3, PND53.
**Finding:** Fully investigated this session — see P0-2/3/4 in [06_P0_MANDATORY_INVESTIGATION_ANSWER_REGISTER.md](06_P0_MANDATORY_INVESTIGATION_ANSWER_REGISTER.md). Summary: purchase PARTIAL, sales PARTIAL, multi-rate HIGH gap open, 50-TWI missing 5 form fields, PND3/53 has a silent monkey-patch duplication risk + hardcoded field, service-only is an unenforced convention. Boss issued **Partial Acceptance** only.
**Evidence location:** Branch `audit/account-wht-grpa-m18-closure-010`, files `01`–`09`.
**Classification:** **CONFIRMED — substantive, real, and honestly incomplete** (this is the single most thoroughly evidenced open item in the whole investigation).
**Gate impact:** Blocks any Financial/Statutory VETO clearance on WHT.
**Next controlled action:** Per Boss's own recorded decision: confirm `l10n_th_withholding_tax_multi` module-baseline inclusion; complete 10-item legal-tax review.

---

## ST-05 — Monthly close / year-end close
**Required evidence target:** Period close, month 12 close, income/expense close, retained earnings transfer.
**Finding:** See P0-5/6/7. Monthly close: resolved, recurring by design. Month-12: resolved, deliberately kept separate from Fiscal Year Close (a corrected design decision, not an oversight). Retained earnings: resolved with 1 disclosed residual.
**Evidence location:** `B02`, `B03`, `B05`, `B07`, `B08`, `B10`, `B11`, `B19` (`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`).
**Classification:** **RESOLVED**, best-evidenced cluster of the 9 Special Team items.
**Gate impact:** None blocking.
**Next controlled action:** None required.

---

## ST-06 — Account × Inventory valuation interface
**Required evidence target:** Stock truth owner, valuation event, COGS, adjustment, return, landed cost, accounting posting boundary.
**Finding:** Core boundary resolved (see P0-8). Landed cost, returns, and adjustment-specific posting flows were **not individually evidenced** this session — only the general "Inventory owns valuation method, Accounting owns posting the result" principle was confirmed.
**Evidence location:** `B03_DOMAIN_BOUNDARY_MODEL.md` §3/§4.
**Classification:** **RESOLVED at the principle level; PARTIAL at the scenario level** (landed cost / returns / adjustments not individually traced).
**Gate impact:** Sufficient to route to Joint Session (see file 09); insufficient to claim full interface closure.
**Next controlled action:** Joint Account×Inventory session to trace landed-cost, return, and adjustment postings specifically.

---

## ST-07 — Migration financial continuity
**Required evidence target:** Opening balance, historical detail, GL/TB/subledger tie-out, AR/AP aging, asset roll-forward.
**Finding:** See P0-10. GL/TB tie-out and historical continuity: resolved (MG-C11, MG-C04/C07/C05/C09). AR/AP aging and asset roll-forward: confirmed scope absence, "no research performed."
**Evidence location:** `B10_CANONICAL_MIGRATION_REQUIREMENTS.md`; `TEAM_A/A3_DOMAIN_PRIORITIZATION.md`.
**Classification:** **MIXED — confirmed gap on AR/AP + Assets.**
**Gate impact:** Blocks full migration-reconciliation sign-off.
**Next controlled action:** Commission a Team-A-style research pass for AR/AP and Fixed Assets subledgers.

---

## ST-08 — SaaS isolation and lifecycle
**Required evidence target:** Tenant/company isolation, template immutability, version upgrade preview, upgrade audit trail.
**Finding:** See P0-9. Isolation resolved. Template mechanics confirmed open (`B13` DT-03). Upgrade preview and upgrade audit trail not directly evidenced.
**Evidence location:** `B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md`; `B13_DESIGN_OPTION_TRADEOFF_REGISTER.md`.
**Classification:** **MIXED — 1 resolved, 1 confirmed open, 2 not evidenced.**
**Gate impact:** Blocks COA-G04S (SaaS lifecycle gate) from opening.
**Next controlled action:** Boss decision on `B13` DT-03; separate research pass on upgrade preview/audit trail.

---

## ST-09 — AI auditability and exception control
**Required evidence target:** Reproducibility, explainability, confidence limits, exception escalation, no invented transactions.
**Finding:** A real exception/failure framework exists (`B11_EXCEPTION_FAILURE_MODEL.md`, e.g. scenario 20 on delayed Fiscal Year Close) — but it governs *data/timing* exceptions in the deterministic design, not "AI decision" exceptions, because no AI-driven decision capability exists inside Accounting Core's own functional design (consistent with P0-12/VC-09). The *process* that produced this design pack itself is reproducible by construction: every CORR round is independently re-audited (ChatGPT) and SHA-256-manifested (`COA_G01_SHA256SUMS.txt`).
**Evidence location:** `B11_EXCEPTION_FAILURE_MODEL.md`; `COA_G01_EVIDENCE/COA_G01_SHA256SUMS.txt`.
**Classification:** **RESOLVED for the design-production process; NOT APPLICABLE for in-product AI decisions** (none exist yet in this domain).
**Gate impact:** None blocking today; re-open if an in-product AI feature is later proposed for Accounting Core.
**Next controlled action:** None required at this time.
