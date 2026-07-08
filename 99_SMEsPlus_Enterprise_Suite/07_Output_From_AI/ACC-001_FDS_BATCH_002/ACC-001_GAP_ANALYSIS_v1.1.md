# ACC-001 Gap Analysis v1.1

Document ID: SMEPLUS-ACC001-GAPAN-v1.1
Previous Version: SMEPLUS-STATE04-ACC-GAPAN-001 (v1.0, 8 gaps)
Version: v1.1
Batch: FDS-ACC-BATCH-002
Status: DRAFTED — REQUIRES CHATGPT L99 REVIEW
Gate Status: HOLD / REVIEW REQUIRED
Owner: Functional Specification AI
Revised By: Claude AI (/L99.99, FDS-ACC-BATCH-002)
Generated: 2026-07-08 (Asia/Bangkok)

---

## Purpose

Updated gap register reflecting State 3 Review findings (GAP-ACC-001 to GAP-ACC-008, confirmed) plus newly identified gaps (GAP-ACC-009 to GAP-ACC-015), and their disposition after FDS-ACC-BATCH-002 revision.

---

## Gap Register

| Gap ID | Section Affected | Gap Description | Severity | Owner | Required Action | v1.1 Disposition | Status | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| GAP-ACC-001 | FR-ACC-002–005 standalone files | No standalone FDS files for ACC-002–005 (only sections in ACC-001) | High | Functional Specification AI | Draft standalone split files | Split files ACC-002–005 exist on branch SMEsPlus at commit 6a947c90d616; content review deferred to ACC-002–005 batch | PARTIAL — content review pending | HOLD |
| GAP-ACC-002 | Central traceability matrix v0.2 | Only FR-ACC-001 in central matrix; FR-002–020 absent | High | Functional Specification AI / Enterprise Architect AI | Populate module-level matrix + reconcile central matrix | Module-level matrix updated in v1.1 (§12); central v0.2 reconciliation still NOT done (separate PMO-authorized step) | PARTIAL — central reconciliation pending | HOLD |
| GAP-ACC-003 | FR-ACC-011/012/013/015/018/019/020 — no §12 mapping | 7 of 20 FRs had no traceability rows | Medium | Functional Specification AI | Complete mapping | All 7 FRs now mapped in §12 v1.1 | ADDRESSED IN v1.1 — reviewer confirmation required | HOLD |
| GAP-ACC-004 | Thai VAT/WHT detail — Pending Legal Review | Evidence status "Pending Legal Review" — tax rules not yet authored or reviewed | High | Accounting Owner / Legal | Author rules → legal review | Rules authored in §6-B Thai Tax Annex; all tagged LEGAL_TAX_REVIEW_REQUIRED; legal reviewer NOT yet assigned | PARTIAL — authored, legal review not started | HOLD |
| GAP-ACC-005 | API/DB/UI — Draft only | Architecture review not done | Medium | Enterprise Architect AI | Architecture review of §8/9/10 | API and DB significantly extended in v1.1; Architecture review still pending | PARTIAL — extended, not reviewed | HOLD |
| GAP-ACC-006 | Duplicate folders 02_Functional_Design | Byte-identical duplicate folders | Low | PMO | PMO decision to archive | Not addressed in this batch (out of scope per revision order) | OPEN | HOLD |
| GAP-ACC-007 | Nested traceability folder | Self-nested v0.1 matrix folder | Low | PMO | PMO decision to archive | Not addressed in this batch | OPEN | HOLD |
| GAP-ACC-008 | OQ-ACC-001 to OQ-ACC-005 unanswered | Five open questions unresolved | Medium | Boss / Accounting Owner | Boss decisions per item | OQ register expanded to OQ-ACC-001 to OQ-ACC-014 in v1.1 §16; no answers provided (BOSS_DECISION_REQUIRED) | OPEN | HOLD |
| GAP-ACC-009 | FR-ACC-001 mis-mapping in §12 | FR-ACC-001 mapped to API-ACC-013/AC-ACC-007 (Period Closing) — wrong | Medium | Functional Specification AI | Correct mapping; add setup API + AC | Corrected in §12 v1.1; setup APIs API-ACC-S01 to S08 added; AC-ACC-022 assigned | ADDRESSED IN v1.1 — reviewer confirmation required | HOLD |
| GAP-ACC-010 | Posting Rules absent (entire FDS) | No accounting Dr/Cr rules for any document | Critical | Functional Specification AI | Author Posting Rules section | Posting Rules §6-A authored in v1.1 (PR-ACC-001 to PR-ACC-008) | ADDRESSED IN v1.1 — Accounting Owner review required | HOLD |
| GAP-ACC-011 | Thai tax detail absent | Tax point, TI fields, credit/debit note, WHT certificate, rounding, numbering, branch code, TaxCode config all missing | Critical | Functional Specification AI → Accounting Owner / Legal | Author annex → legal review | Thai Tax Annex §6-B authored in v1.1 (TH-01 to TH-09); all tagged LEGAL_TAX_REVIEW_REQUIRED | ADDRESSED IN v1.1 — legal review NOT started | HOLD |
| GAP-ACC-012 | Data entities missing | CreditNote, DebitNote, BankStatement, StatementLine, ReconciliationMatch, TaxCode, WHTType, DocumentSequence, FiscalYear absent; no ref_type/ref_id/company_id/branch_id on core entities | High | Functional Specification AI / Database Design AI | Add entities to §8 | All missing entities added in §8 v1.1; ref_type/ref_id and company_id/branch_id added to core entities | ADDRESSED IN v1.1 — DB Design AI review required | HOLD |
| GAP-ACC-013 | Undecided business scope (REV-08) | Opening balances, year-end close, payment allocation/aging, advance deposit, petty cash, PDC, recurring journals — not decided | High | Boss | Boss decision per item | Each item marked BOSS_DECISION_REQUIRED in §3 Out of Scope; deferred to REV-08 after Boss decisions | OPEN — BOSS_DECISION_REQUIRED | HOLD |
| GAP-ACC-014 | AC coverage incomplete | ~10/20 FRs had no AC; no tax-correctness or negative ACs; no UAT cases | High | Functional Specification AI / QA UAT AI | Expand ACs + create UAT cases | ACs expanded in §11 v1.1: 27 ACs covering all 20 FRs, negative cases, tax correctness; UAT cases still NOT created | PARTIAL — ACs drafted, UAT package pending | HOLD |
| GAP-ACC-015 | Self-approval language in documents | "Pass" self-assessed; AI "Approval" language in §15; "READY FOR..." phrase | Low | Functional Specification AI / PMO | Governance wording correction | §18 "Pass" → "Self-assessed — pending independent review"; §15 corrected; "READY FOR..." replaced | ADDRESSED IN v1.1 | HOLD |

---

## Summary

| Category | Count |
|---|---|
| Total gaps tracked | 15 |
| ADDRESSED IN v1.1 (reviewer confirmation required) | 5 (GAP-ACC-003, 009, 010, 011, 015) |
| PARTIAL (progress made, dependencies remain) | 5 (GAP-ACC-001, 002, 004, 005, 014) |
| OPEN — BOSS_DECISION_REQUIRED | 2 (GAP-ACC-008, 013) |
| OPEN — PMO decision pending | 2 (GAP-ACC-006, 007) |
| CLOSED | 0 |

**No gap is marked CLOSED without independent reviewer confirmation.**

## Gate Impact

All gaps carry Gate Impact = HOLD. FDS-ACC-BATCH-002 revision addresses 5 gaps and makes partial progress on 5 more. Gate cannot PASS until:
- GAP-ACC-004/011: Legal/Accounting Owner review of §6-B
- GAP-ACC-010: Accounting Owner review of §6-A Posting Rules
- GAP-ACC-012: DB Design AI review of §8
- GAP-ACC-005: Enterprise Architect review of §9
- GAP-ACC-014: QA/UAT package created
- GAP-ACC-008/013: Boss decisions on OQ items and REV-08 scope

REQUIRES CHATGPT L99 REVIEW
