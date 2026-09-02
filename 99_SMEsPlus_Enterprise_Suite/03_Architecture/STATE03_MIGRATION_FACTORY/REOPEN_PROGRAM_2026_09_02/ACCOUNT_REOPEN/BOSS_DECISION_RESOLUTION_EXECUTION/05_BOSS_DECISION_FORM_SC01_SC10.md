# 05 — BOSS DECISION FORM (`SC-01`..`SC-10`, 13 decision components)

`Boss is the sole Final Approver.` No component below is pre-filled as approved. Select one option per component; options are limited to those that apply, per governing-prompt §9.2's list of seven.

---

### `DC-01` — Fixed assets, depreciation, disposal (`ACC-DEC-004`)
**Options:** ☐ IN FOR DEEP RESEARCH · ☐ OUT OF CURRENT ACCOUNT SCOPE · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** IN FOR DEEP RESEARCH
**Why recommended:** Evidence is Verified; the Thai chart template already instantiates 22 `asset_fixed` + 6 `asset_non_current` accounts (12 asset classes) — the strongest existing template backing of any `SC` row — and every SME with capital equipment has this need.
**Evidence link:** `12_ASSET_DEFERRED_RECOGNITION_MAP.md` §2–§3 (deep-study package, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` `ACC-DEC-004`).
**Risk if accepted:** Commits Team A/Accounting Core research capacity to an area whose benchmark behavior is entirely black-box (`OEEL-1`, never opened); Thai statutory depreciation rates/lives are unverified (`LT-01`/`LT-02`), so early design may need rework once Legal-Tax returns.
**Risk if deferred:** `M-AST-01..05` are already classified `Mandatory` in the deep-study menu register; continued deferral leaves this area permanently unscoped, blocking asset roll-forward at migration cutover (`G-B5` GAP) and BS-presentation completeness.
**Downstream prompt pack:** `PP-06`
**Gate impact:** No gate defined (`COA-G04`/`G05`/`G06` side effects)

---

### `DC-02` — Deferred revenues/expenses, recognition schedules (`ACC-DEC-005`)
**Options:** ☐ IN FOR DEEP RESEARCH · ☐ OUT OF CURRENT ACCOUNT SCOPE · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** IN FOR DEEP RESEARCH
**Why recommended:** Boss AJ already activates a `Prepayments` business-facing account type for this purpose even though the Thai template ships zero rows of it — evidence that the need is Boss-recognized, only unbuilt.
**Evidence link:** `12_ASSET_DEFERRED_RECOGNITION_MAP.md` §4–§5 (`FT-03`, `FT-04`).
**Risk if accepted:** No benchmark "model" precedent exists in this instance version (`FT-07`) — research must design deferral mechanics largely from first principles rather than adapting an observed pattern.
**Risk if deferred:** Revenue/expense recognition-timing mismatches stay unaddressed; deferral-balance migration at cutover stays an open `GAP` (§8 of `12`) indefinitely.
**Downstream prompt pack:** `PP-06`, sequenced behind `DC-01`
**Gate impact:** No gate defined (`COA-G04`/`G05`/`G06` side effects)

---

### `DC-03` — Budgets / budgetary positions / budget analysis (`ACC-DEC-006`)
**Options:** ☐ IN FOR DEEP RESEARCH · ☐ OUT OF CURRENT ACCOUNT SCOPE · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** HOLD / EVIDENCE REQUIRED
**Why recommended:** Of all 10 `SC` rows this has the weakest evidentiary basis for an immediate IN ruling: `account_budget` is not installed in the benchmark at all (zero behavior evidence), the deep-study package classifies it `Conditional` not `Mandatory`, and no owner exists even provisionally.
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §4, `UK-03`.
**Risk if accepted (HOLD maintained):** Budget-vs-actual reporting stays undesigned; if Thai SME owners in fact rely on budget planning day-to-day, a prolonged HOLD leaves a real management need unaddressed.
**Risk if deferred further without any evidence-gathering:** unchanged — the HOLD itself does not worsen the position, but a future IN ruling made *without* first closing this evidence gap risks committing design effort against zero benchmark precedent and no owner.
**Downstream prompt pack:** None until Boss ruling
**Gate impact:** No gate defined

---

### `DC-04` — Treasury / Cash & Bank owner (`ACC-DEC-007`)
**Options:** ☐ OWNER ASSIGNMENT REQUIRED · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** OWNER ASSIGNMENT REQUIRED
**Why recommended:** Scope (bank journals, statement-import formats, reconciliation, cheques, PromptPay, bank feeds, PDPA review) is not in dispute — only a named owner is missing.
**Evidence link:** `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §B; `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` `VC-03`.
**Risk if accepted:** Low — naming an owner has no design cost by itself and immediately unblocks `PP-07`, which has no dependency on any other item in this package.
**Risk if deferred:** Bank/cash handoffs (`HO-11`/`HO-12`) stay "ownerless" indefinitely; Thai-market-specific questions (which banks offer live feeds, PromptPay handling, PDPA compliance) remain unresearched.
**Downstream prompt pack:** `PP-07`
**Gate impact:** No gate defined; unblocks `HO-11`/`HO-12`

---

### `DC-05A` — Employee expenses, Tax Returns menu, Cash Roundings, WT Certificates (`ACC-DEC-008`)
**Options:** ☐ IN FOR DEEP RESEARCH · ☐ OUT OF CURRENT ACCOUNT SCOPE · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** IN FOR DEEP RESEARCH (conditional on Accounting owning these controls)
**Why recommended:** The HR-expense handoff is concretely mapped (`HO-31`); the other three sub-items are evidenced at menu-label depth only, and WT Certificates specifically has no Thai translation installed in the benchmark — Boss should weigh this unevenness before ruling all four together.
**Evidence link:** `A1` §C.4; `08` objections 5–6; `04` `HO-31` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` `ACC-DEC-008`).
**Risk if accepted:** Ruling all four IN uniformly risks scoping WT Certificates/Cash Roundings/Tax Returns menu items whose actual Thai business process is still only menu-label evidence, not a mapped handoff.
**Risk if deferred:** HR-expense reimbursement — a routine, well-evidenced SME transaction — stays unscoped despite being the strongest sub-item here.
**Downstream prompt pack:** None named in `12_NEXT_CONTROLLED_PROMPT_PACKS.md`; PMO recommends Boss authorize a new pack if ruled IN
**Gate impact:** No gate defined

---

### `DC-05B` — Manufacturing valuation, price difference, inventory write-down (`ACC-DEC-008`)
**Options:** ☐ JOINT_SESSION_REQUIRED
**Recommended option:** JOINT_SESSION_REQUIRED
**Why recommended:** These sub-items cannot be closed from the Account side alone (`07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` explicit); ownership itself is one of the Joint questions.
**Evidence link:** `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` agenda items 6–7; `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §D.
**Risk if accepted (convened):** Coordination cost — requires a named Inventory-side attendee, an Account-side attendee, and a neutral clean-room reviewer for the `OB-13` back-door-inheritance veto checkpoint.
**Risk if deferred:** `OB-11` already flags a "gate scope mismatch" (`COA-G06` doesn't cover costing methods) — the longer this stays unconvened, the longer that mismatch persists unaddressed on both sides.
**Downstream prompt pack:** `PP-04`
**Gate impact:** Account + Inventory Backbone baseline HOLD

---

### `DC-06A` — VAT/CIT ownership model (`ACC-DEC-009`)
**Options:** ☐ LEGAL_TAX_REVIEW_REQUIRED
**Recommended option:** LEGAL_TAX_REVIEW_REQUIRED
**Why recommended:** VAT and CIT research "remain zero"; the benchmark's own exempt-input-VAT template contradicts its own Thai description (`17` `VC-06`) — an ownership ruling now would rest on internally-inconsistent, unreviewed material.
**Evidence link:** `06_LEGAL_TAX_REVIEW_BRIEF.md` §B–§C; `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` `VC-06`.
**Risk if accepted (commissioned):** Time/cost to engage a licensed Thai CPA or Revenue-Department-registered preparer; ownership stays undecided until the reviewer returns.
**Risk if deferred:** `COA-G06` stays `HOLD` indefinitely; if design proceeds anyway without review, SMEsPlus risks inheriting the benchmark's own tax-group WHT-netting defect (`OB-01`: purchase-side WHT liabilities netted against sales-side WHT assets — "must not be inherited").
**Downstream prompt pack:** `PP-03`
**Gate impact:** `COA-G06`

---

### `DC-06B` — `PND1`/`PND54`/`PP36` scope (`ACC-DEC-009`)
**Options:** ☐ LEGAL_TAX_REVIEW_REQUIRED
**Recommended option:** LEGAL_TAX_REVIEW_REQUIRED
**Why recommended:** `06_LEGAL_TAX_REVIEW_BRIEF.md` §A already marks `WHT-7`/`WHT-8`/`WHT-9` (`PND1`/`PND54`/`PP36`) `LEGAL_TAX_REVIEW_REQUIRED` without exception.
**Evidence link:** `06_LEGAL_TAX_REVIEW_BRIEF.md` §A rows `WHT-7`–`WHT-9`.
**Risk if accepted:** Same commissioning cost as `DC-06A` — note the two can share one engagement.
**Risk if deferred:** These forms remain in the Thai chart template with undecided scope status indefinitely, risking accidental exclusion of a legally required filing if design proceeds without a scope ruling.
**Downstream prompt pack:** `PP-03`
**Gate impact:** `COA-G06`

---

### `DC-07` — Approval-before-posting workflow (`ACC-DEC-010`)
**Options:** ☐ IN FOR DEEP RESEARCH · ☐ OUT OF CURRENT ACCOUNT SCOPE · ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** HOLD / EVIDENCE REQUIRED
**Why recommended:** The `ACC-004` draft workflow is "assumed in the close checklist but scoped by nobody" (`17` `VC-07` / `OBJN-07`); a ruling issued without first tying it to `CO-02` (segregation of duties) risks the same control being designed twice.
**Evidence link:** `14 OBJN-07` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` `ACC-DEC-010`); `17` `VC-07`.
**Risk if accepted (IN or OUT ruled now, without the `CO-02` tie-in):** Risk of re-designing segregation-of-duties controls twice — once implicitly via this workflow, once explicitly at `CO-02`.
**Risk if deferred indefinitely:** Approval-before-posting stays an assumed-but-undesigned control, weakening the close checklist's own integrity claim.
**Downstream prompt pack:** None named in `12`; Team B designs at `CO-02` once unblocked
**Gate impact:** `CO-02`

---

### `DC-08A` — Analytic / dimension model ownership (`ACC-DEC-011`)
**Options:** ☐ OWNER ASSIGNMENT REQUIRED
**Recommended option:** OWNER ASSIGNMENT REQUIRED
**Why recommended:** "Currently owned by nobody in the design chain" (`13` §8 finding 4) — Team A calls it "partially in scope," Team B's own boundary model does not name it as a neighbour at all.
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §1, §8 finding 4.
**Risk if accepted:** Low — naming an owner is a low-cost action that unblocks a dedicated research pass.
**Risk if deferred:** `COA-G07` has no stated acceptance criteria at all (`UK-08`); deferring the owner assignment means this gate cannot even define what would satisfy it, let alone move.
**Downstream prompt pack:** None named in `12`; PMO recommends a new dedicated pack once owner is named
**Gate impact:** `COA-G07`

---

### `DC-08B` — Branch (สาขา) statutory status (`ACC-DEC-011`)
**Options:** ☐ LEGAL_TAX_REVIEW_REQUIRED
**Recommended option:** LEGAL_TAX_REVIEW_REQUIRED
**Why recommended:** Whether branch is a per-branch VAT-filing unit (statutory attribute) or a management dimension is unanswered (`13` `UK-01`; `06` `DBD-6`).
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §2 `DIM-02`, `UK-01`; `06_LEGAL_TAX_REVIEW_BRIEF.md` §D `DBD-6`.
**Risk if accepted:** Commissioning cost — shareable with `DC-06A`/`DC-06B` under one reviewer engagement.
**Risk if deferred:** The dimension model (`13` §2) stays undecided, blocking both the `COA-G07` proof and the branch-level management report candidate (`MR-02`).
**Downstream prompt pack:** `PP-03`
**Gate impact:** `COA-G06` / `COA-G07`

---

### `DC-09` — Financial Reporting design owner (`ACC-DEC-012`)
**Options:** ☐ OWNER ASSIGNMENT REQUIRED
**Recommended option:** OWNER ASSIGNMENT REQUIRED
**Why recommended:** Naming the owner now is not blocked by `COA-G01`/Legal-Tax sequencing — only the design *work* is (`10` §C).
**Evidence link:** `09 RU-08` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` `ACC-DEC-012`); `10` §C.
**Risk if accepted:** Minimal — an owner who waits for `COA-G01`/Legal-Tax to clear costs nothing in the interim.
**Risk if deferred:** When `COA-G01` and the Legal-Tax review do clear, Financial Reporting design would start with no owner in place — a fresh delay at the worst possible time, since `COA-G05` gates the entire statement-production layer.
**Downstream prompt pack:** `PP-08`, sequenced behind `PP-02` + `PP-03`
**Gate impact:** `COA-G05`

---

### `DC-10` — Standard COA template mechanics, `B13 DT-03` (`ACC-DEC-013`)
**Options:** ☐ HOLD / EVIDENCE REQUIRED
**Recommended option:** HOLD / EVIDENCE REQUIRED
**Why recommended:** "Explicitly unapproved... unchanged" across a prior round already (`17` `VC-05`); every one of the 12 underlying asset-class template rows is individually tagged `COA-G06 LEGAL_TAX_REVIEW_REQUIRED` (`12` §2) — the statutory basis for these mechanics has not been reviewed. Boss retains full authority to rule APPROVE / REJECT / MODIFY directly at any time; this recommendation is that Boss have the depreciation-rate/TFRS-for-NPAEs Legal-Tax findings in hand first, not that Boss cannot rule today.
**Evidence link:** `17 VC-05` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` `ACC-DEC-013`); `12_ASSET_DEFERRED_RECOGNITION_MAP.md` §2, §6.
**Risk if accepted (HOLD maintained):** `COA-G04S` stays blocked, and — because `COA-G01` unblock plus this ruling together gate nearly every downstream `COA-Gxx` step — this is arguably the single highest-leverage HOLD in this package.
**Risk if Boss instead rules now without the Legal-Tax findings:** Mechanics get fixed before the statutory basis is confirmed, risking the same kind of rework already found necessary in the benchmark's own contradictory VAT template (`VC-06`).
**Downstream prompt pack:** None until Boss ruling — carries forward
**Gate impact:** `COA-G04S`

---

## Explicit non-claim

No option above is pre-selected. Every checkbox is empty. This form recommends; Boss decides.
