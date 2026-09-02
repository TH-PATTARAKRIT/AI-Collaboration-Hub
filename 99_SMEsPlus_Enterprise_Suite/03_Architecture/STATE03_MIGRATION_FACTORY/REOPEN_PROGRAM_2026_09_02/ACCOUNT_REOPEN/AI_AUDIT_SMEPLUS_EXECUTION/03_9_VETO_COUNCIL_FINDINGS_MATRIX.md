# 9 Veto Challenge Council — Findings Matrix

Primary Gate challenge body. 9 findings, `VC-01`–`VC-09`, one per Council seat (governing prompt Section 6). Each finding carries: Question fingerprint, Delta trigger, Prior evidence relied upon, New evidence inspected, Evidence location, Owner/domain, Classification, Gate impact, Next controlled action.

---

## VC-01 — Audit VETO / Evidence & Governance
**Question:** Does the current Account evidence chain remain consistent across Team A, Team B, Audit, PMO and Boss Closure, without stale PASS propagation?
**Delta trigger:** CP-00 discovered 3 divergent "SMEsPlus"-branch snapshots and a root-level copy materially behind the live worktree.
**Prior evidence relied upon:** None assumed — tested directly.
**New evidence inspected:** Root `03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/` contains 1 ruling file; `ISOLATED_ACCOUNT_CORR5`'s equivalent folder contains ~22 rulings through letter "AX" plus a STATE03 execution prompt, verified via `git log --diff-filter=A` (not alphabetical — letters AH and AQ are each reused).
**Evidence location:** Both paths under `.../STATE03_MIGRATION_FACTORY/BOSS_GATE/`.
**Commit/timestamp:** `ISOLATED_ACCOUNT_CORR5` HEAD `5df588d`, 2026-08-31 16:12.
**Owner/domain:** Governance / Evidence chain.
**Reviewer/verifier status:** Verified directly by this session (Explore agent), not asserted.
**Classification:** **CONFIRMED GAP.** No false PASS was found propagating from the stale copy into a real decision — but the stale copy exists, is structurally identical in naming to the current one, and nothing in the repo marks it as superseded. A future reader (human or AI) consulting the root copy would reach materially wrong conclusions (e.g. would miss the entire 5-round COA-G01 correction cycle and its HOLD status).
**Gate impact:** Does not itself change a Gate status, but invalidates the root copy as a citable source going forward.
**Next controlled action:** Boss to mark the root-level `03_Architecture/STATE03_MIGRATION_FACTORY/` copy as archived/superseded (e.g. rename or add a pointer file) so it cannot be mistaken for current state in a future session.

---

## VC-02 — TBRAC / Thailand Business Reality & User Fitness
**Question:** Which Account conclusions are proven by Thai real-business or authoritative evidence, and which remain source-system or design assumptions?
**Delta trigger:** P0-2/P0-3/P0-4 findings on WHT/TWI/PND.
**Prior evidence relied upon:** None assumed.
**New evidence inspected:** `COA_G01_CURRENT_BLOCKER_AND_DISPOSITION_MATRIX_R5.md` (N-04: authoritative Thai financial-statement PDF `งบการเงิน 2567.pdf` returned "not found" on two tool calls); `03_ACC_WHT_50TWI_GAP_CLOSURE.md` (5 form fields flagged `REQUIRES FORM UPDATE, pending legal-tax review`); `05_ACC_WHT_FINAL_DISPOSITION_AND_BOSS_RECOMMENDATION.md` (10-item `LEGAL_TAX_REVIEW_REQUIRED` register, still open).
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/`; branch `audit/account-wht-grpa-m18-closure-010`.
**Commit/timestamp:** Branch tip `fe356f7`.
**Owner/domain:** Thailand statutory / tax.
**Reviewer/verifier status:** Verified directly.
**Classification:** **CONFIRMED GAP.** Almost every Thai-tax conclusion currently traces to observation of the *old* Odoo source system's module behavior (`l10n_th_*`), not to independently-verified Thai statute or authoritative business documents. The one authoritative source document that was sought (the 2567 financial statement PDF) is currently inaccessible.
**Gate impact:** Blocks any claim of statutory-proven WHT/TWI/PND completeness; keeps P0-2/3/4 at partial/open.
**Next controlled action:** Boss to reissue access to `งบการเงิน 2567.pdf`; commission the 10-item legal-tax review before any WHT/TWI/PND item is upgraded past "source-system observed."

---

## VC-03 — Expert IBPV / Business Process & Design Integrity
**Question:** Does Account remain the Financial Truth Center without duplicate ownership across Sales, Purchase, Inventory, Expense, Employee and Manufacturing interfaces?
**Prior evidence relied upon:** Full Reopen Program commit (`42e04e6`) framing Accounting as "Financial Truth Center."
**New evidence inspected:** `B03_DOMAIN_BOUNDARY_MODEL.md` §3/§4 (Upstream/Downstream Seams table; Inventory valuation explicitly out of scope).
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B03_DOMAIN_BOUNDARY_MODEL.md`.
**Owner/domain:** Architecture / domain boundaries.
**Reviewer/verifier status:** Verified directly.
**Classification:** **RESOLVED for the Inventory boundary specifically** (clean, unambiguous). **NOT DIRECTLY EVIDENCED for Sales, Purchase, Expense, Employee, Manufacturing** — this session's evidence sweep did not surface an equivalent explicit boundary statement for those five interfaces; absence of evidence, not evidence of a problem.
**Gate impact:** None blocking, but leaves 5 of 6 named interfaces unverified.
**Next controlled action:** Extend `B03`-style boundary analysis explicitly to Sales, Purchase, Expense, Employee, Manufacturing before claiming full Financial-Truth-Center integrity.

---

## VC-04 — Expert IDTM / Data, Identity, Reconciliation & Integrity
**Question:** Are COA, GL, TB, subledger, opening/closing continuity and migration reconciliation sufficiently evidenced to prevent double-counting?
**New evidence inspected:** `B05_ACCOUNTING_INVARIANT_BASELINE.md` BINV-10/BINV-14; `B10_CANONICAL_MIGRATION_REQUIREMENTS.md` MG-C11/C04/C07; `TEAM_A/A3_DOMAIN_PRIORITIZATION.md` (AR/AP and Assets "deferred… no research performed").
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`; `TEAM_A/`.
**Owner/domain:** Data integrity / migration.
**Reviewer/verifier status:** Verified directly.
**Classification:** **MIXED.** GL/TB double-counting controls: **RESOLVED**. AR/AP and fixed-asset subledger reconciliation: **CONFIRMED GAP** (explicit scope absence).
**Gate impact:** Blocks P0-10 from closing; does not block GL/TB-level claims.
**Next controlled action:** Open a dedicated AR/AP + Assets research pass (Team A style) before migration reconciliation can be claimed complete.

---

## VC-05 — Expert IESA / ERP & SaaS System Integrity
**Question:** Are SaaS COA Template, Tenant, Company Instance, versioning, upgrade and reporting boundaries clear and evidence-backed?
**New evidence inspected:** `B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md` CO-09/CO-10; `B13_DESIGN_OPTION_TRADEOFF_REGISTER.md` DT-03 ("Not approved… requires its own follow-up design attention").
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`.
**Owner/domain:** SaaS architecture.
**Reviewer/verifier status:** Verified directly.
**Classification:** **MIXED.** Tenant/company isolation: **RESOLVED**. Standard template mechanics: **CONFIRMED OPEN** (explicitly unapproved, carried open through Round 7). Upgrade preview / upgrade audit trail / reporting boundary: **NOT DIRECTLY EVIDENCED** in this pass.
**Gate impact:** Blocks P0-9 from closing.
**Next controlled action:** Boss decision required on `B13` DT-03 (template option) before COA-G04S can open.

---

## VC-06 — Financial / Accounting / Tax / Statutory VETO
**Question:** Are WHT, VAT, CIT, period close, retained earnings and financial statement semantics supported by Thai statutory/accounting evidence?
**New evidence inspected:** See P0-2, P0-5, P0-6, P0-7. **VAT and CIT: searched, zero mentions found anywhere in Team A, Team B, or the WHT branch corpus** — `TEAM_A/A2_SYSTEM_KNOWLEDGE_MAP.md` / `A3_DOMAIN_PRIORITIZATION.md` defer "Tax/VAT/WHT" downstream as "captured as dependencies only… with no research performed."
**Evidence location:** As cited per question in file 06.
**Owner/domain:** Financial/Tax/Statutory.
**Reviewer/verifier status:** Verified directly.
**Classification:** Period close and retained earnings: **RESOLVED**. WHT: **PARTIAL, HIGH gap open**. **VAT and CIT: `HOLD / EVIDENCE REQUIRED` — no research has been performed on either, anywhere in the inspected corpus.**
**Gate impact:** VAT/CIT absence blocks any claim of full statutory-semantics coverage; must not be silently assumed "in scope elsewhere" without confirmation.
**Next controlled action:** Boss to confirm whether VAT/CIT are in-scope for Accounting Core or explicitly deferred to a separate Tax domain — currently undecided, not merely unresearched.

---

## VC-07 — Security / Privacy / Resilience VETO
**Question:** Are SoD, permissions, tenant/company isolation, audit trail, backup/recovery and destructive action controls evidenced?
**New evidence inspected:** `B07` (Audit Event scoped per-company after red-team finding, `B16` Persona 5); BINV-12 (Recorded-At immutable).
**Owner/domain:** Security / Resilience.
**Reviewer/verifier status:** Verified directly.
**Classification:** Tenant/company isolation and audit-event scoping: **RESOLVED**. **Segregation of Duties, granular permissions, backup/recovery, and destructive-action controls: NOT DIRECTLY EVIDENCED** in this pass — the full `B09` CO-01–CO-16 control list was not exhaustively read against these specific topics.
**Gate impact:** Cannot currently support a claim that SoD/backup/destructive-action controls are evidenced; must remain open rather than assumed present.
**Next controlled action:** Targeted read of the full `B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md` CO-01–CO-16 list specifically against SoD, backup/recovery, and destructive-action scenarios.

---

## VC-08 — Clean-Room / IP / Provenance VETO
**Question:** Did any Odoo/source schema, ORM, workflow, naming, XML, QWeb or architecture leak into SMEsPlus target design?
**New evidence inspected:** `B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` ("Critical Vendor-Derived Design Risk = 0"; explicit review of the only 3 vendor-behavior terms appearing in B02–B13, none adopted); `TEAM_A/05_QUARANTINE/CLEAN_ROOM_QUARANTINE_REGISTER.md` / `21_QUARANTINE_REGISTER.md` ("No OEEL-1 or OPL-1 source body was opened"); `19_PROVENANCE_REGISTER.md`.
**Evidence location:** `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B14_CLEAN_ROOM_PROVENANCE_MATRIX.md`; `TEAM_A/05_QUARANTINE/`.
**Owner/domain:** Clean-room / IP.
**Reviewer/verifier status:** Verified directly — this is the most rigorously self-documented area found in the entire corpus.
**Classification:** **RESOLVED.** No leakage found; proprietary Odoo Enterprise modules held black-box/metadata-only; SAP/NetSuite used only as external comparison points, never adopted as design source.
**Gate impact:** None — supports clean-room compliance.
**Next controlled action:** None required; maintain the same provenance-logging discipline for future domains.

---

## VC-09 — AI Control / Automation / Human Oversight VETO
**Question:** Which AI-assisted Account/COA decisions may be proposed, and which must remain deterministic, reproducible and human/Boss-approved?
**New evidence inspected:** `B09` CO-16 (materiality is a required human policy input, never AI-computed); every `BOSS_GATE` document's repeated line "Boss is the sole Final Approver. No Evidence = No Progress. Never Skip Gate."; the project's own `.claude/skills/smeplus-state02-governance-controller` skill definition ("Boss remains Sole Final Approver; Claude Code is Preparer/Executor only").
**Owner/domain:** AI governance.
**Reviewer/verifier status:** Verified directly, corroborated by 3 independent artifacts (design doc, gate documents, live skill config).
**Classification:** **RESOLVED at governance/process level.** Accounting Core's own functional design contains zero AI-driven classification or proposal mechanism — all rules are deterministic. AI's actual role (research, design drafting, audit) is consistently bounded by Boss-approval language across every layer checked.
**Gate impact:** None blocking.
**Next controlled action:** None required; re-verify if/when an actual in-product AI feature is proposed for Accounting Core (none exists today).
