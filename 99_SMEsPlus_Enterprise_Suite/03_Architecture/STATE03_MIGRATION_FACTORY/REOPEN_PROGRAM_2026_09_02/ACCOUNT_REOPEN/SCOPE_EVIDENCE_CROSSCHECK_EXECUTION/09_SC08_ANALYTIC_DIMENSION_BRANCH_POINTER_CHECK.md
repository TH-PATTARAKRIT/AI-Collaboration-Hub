# 09 — SC-08 ANALYTIC / DIMENSION / BRANCH EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-08` |
| Decision ID | `ACC-DEC-011` |
| Topic | Analytic/dimension model ownership; branch (สาขา) as dimension vs. statutory attribute |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `06_LEGAL_TAX_REVIEW_BRIEF.md` §D item `DBD-6` (required, source pack); `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` "Unresolved objections," items 2 and 4 (deep-study, local numbering) |
| Evidence pointer result | Verified |
| Owner status | Boss / Legal-Tax (dual — ownership assignment is Boss's; the branch statutory-status sub-question is Legal-Tax's) |
| Gate impact | `COA-G07` |
| GL impact known? | Partial — dimension tags attach to GL lines by convention in the benchmark, but no SMEsPlus ownership or design exists yet |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | Unknown — if branch is ruled a statutory reporting unit (not just a dimension), it could affect how BS/PL are filed per branch; this is exactly the open legal-tax question and is not yet answered anywhere in the evidence chain |
| Subledger or interface impact | Analytic |
| Thai menu/report communication issue | Yes — objection 7 in the same deep-study file (not part of this row's cited objections 2/4, but in the same "Unresolved objections" list) separately notes the benchmark's Thai label for Analytic Accounts (`บัญชีวิเคราะห์`) collides with the Thai term for the chart-of-accounts family, a naming-fitness issue for the TBRAC track — disclosed here as adjacent context, not claimed as part of this row's own two cited objections |
| AI Audit SMEsPlus objection | This is one of only two `SC` rows (with `SC-11`, not in this session's scope) carrying a dual `GAP OWNER ROUTING REQUIRED` + `LEGAL_TAX_REVIEW_REQUIRED` status — an owner cannot be meaningfully assigned until the branch statutory-status question is answered, since the answer changes what the "analytic/dimension" design job even is (a UI convenience vs. a compliance-bound structure) |
| Readiness classification | `READY AFTER OWNER ASSIGNED` and `READY AFTER LEGAL_TAX_REVIEW` — **split**, both must clear |
| Next action | Boss assigns an owner in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`; the branch statutory-status question is separately routed to the (uncommissioned) legal-tax reviewer via `06_LEGAL_TAX_REVIEW_BRIEF.md` item `DBD-6`, which explicitly states "feeds `ACC-DEC-011` / `SC-08`" |

## Detail

Both required registers cite "source `05` row `ACC-DEC-011`; source `13` objections 2, 4." Resolving outside the required perimeter to `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md`'s "Unresolved objections noticed" list:

- Objection 2: "Branch (สาขา) sits on both sides of `COA-G07`'s own exception clause ('where accounting treatment does not differ'): if Thai VAT is filed per branch, branch is a regulated attribute, not a dimension — a legal-tax fact that no session has evidenced (`UK-01`)."
- Objection 4: "Analytic coupling was analysed structurally only (`GAP-D01-06`); Team A `INT-07` says 'partially in scope' while Team B `B03` does not name analytic / dimensions as a neighbour at all — the area is currently owned by nobody in the design chain (`GAP OWNER ROUTING REQUIRED`)."

Both are precise, on-point matches: objection 2 is the exact branch-as-dimension-vs-statutory-attribute question named in this row's topic; objection 4 is the exact ownership gap. **Verified.**

This is independently corroborated by a required input: `06_LEGAL_TAX_REVIEW_BRIEF.md` §D item `DBD-6` reads "Branch (สาขา) statutory reporting status — is a branch a separate statutory reporting unit? (feeds `ACC-DEC-011` / `SC-08`)... Source: `13` objections 2, 4... `LEGAL_TAX_REVIEW_REQUIRED`" — the same two objection numbers, cited independently in a different required file, for the same purpose. No discrepancy found across the three documents.
