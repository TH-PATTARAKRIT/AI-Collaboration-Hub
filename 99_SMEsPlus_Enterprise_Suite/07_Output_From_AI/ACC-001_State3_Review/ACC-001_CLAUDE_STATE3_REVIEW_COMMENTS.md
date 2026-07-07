# ACC-001 Claude State 3 Review Comments

Document ID: SMEPLUS-STATE03-ACC-CLREV-001
Version: v1.0
Status: REVIEWED WITH COMMENTS
Gate Status: HOLD / REVIEW REQUIRED
Owner: Claude AI (SMEsPlus Expert FDS Designer skill, /L99.99)
Reviewer of record: Claude AI (State 3 Review, authorized by Boss 2026-07-07)
Approver: Boss / Final Gate Owner
Reviewed Document: `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` (v1.0, SHA256 prefix 4c38d189a0a4358c, verified at commit 6a947c90d616)
Supporting Inputs Reviewed:
- `04_Review_Gates/ACC-001_L99_REVIEW_GATE_REPORT.md` (v1.0, HOLD / REVIEW REQUIRED)
- `07_Output_From_AI/ACC-001_GAP_ANALYSIS.md` (8 gaps)
- `07_Output_From_AI/ACC-001_EVIDENCE_REGISTER.md` (8 evidence rows)
- `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md` (20 FRs)
Generated: 2026-07-07 (Asia/Bangkok)
Execution Mode: Review / Revision Only — no repository files modified

---

## 1. Review Summary

ACC-001 v1.0 is a coherent, well-scoped module-level FDS draft. Its structure (FR → BR → WF → Entity → API → UI → AC → traceability) follows the FDS Factory standard, its self-disclosure of evidence gaps (§13) is honest, and its Clean Room posture is consistent with ADR-0005/0006. It is a valid basis for revision.

It is **not** yet sufficient to pass the FDS Gate. The material deficiencies fall into five groups:

1. **Traceability is incomplete for 8 of 20 FRs** (confirmed against the module matrix — see §3).
2. **Posting rules are absent.** The FDS defines documents and workflows but never defines the accounting entries each document generates. For an accounting module this is a core functional requirement, not an implementation detail.
3. **Thailand tax logic is named but not specified.** VAT/WHT are listed as functions, but the rules that make them correct (tax point, mandatory tax-invoice fields, rounding, filing formats, numbering reset) are absent and must be authored, then routed to legal/accounting review.
4. **Data model and API coverage have concrete holes** (credit/debit note, bank reconciliation, tax configuration, document sequences, P&L/balance-sheet endpoints).
5. **Acceptance criteria cover only ~half the FRs** and none of the Thai tax correctness rules.

Decision input: **HOLD / REVIEW REQUIRED — REVISION REQUIRED** (revision scope in `ACC-001_REVISION_SCOPE_PROPOSAL.md`). This review does not approve, pass, or certify anything.

---

## 2. Business Completeness Findings

| ID | Section | Finding | Severity | Recommended Disposition |
|---|---|---|---|---|
| RC-01 | §5 | No FR for **opening balances / data migration** (beginning GL balances, open AR/AP items, unclaimed VAT). Every real tenant onboarding needs this. | High | Add FR (proposed FR-ACC-021) or record explicit Boss out-of-scope decision |
| RC-02 | §5/§7 | No FR/WF for **fiscal year-end closing** (P&L close to retained earnings). WF-ACC-004 covers monthly period lock only. | High | Add FR/WF or explicit phase decision |
| RC-03 | FR-ACC-013 | "กระทบยอด" (reconciliation) is named but has **no workflow, no entities** (BankStatement, StatementLine, ReconciliationMatch), **no API, no AC**. | High | Author reconciliation sub-spec in revision |
| RC-04 | §5/§8 | **Partial payment / payment allocation** (one receipt across multiple invoices, partial settlement, over/under payment) unspecified. AR aging is referenced in WF-ACC-003 but has no FR/API/report definition. | High | Add allocation rules + aging report FR |
| RC-05 | §5 | **Advance payment / deposit (เงินมัดจำ/เงินรับล่วงหน้า)** and its VAT treatment missing — common Thai SME scenario; VAT tax point for services is receipt of payment, so deposits trigger VAT. | High | Add FR; tax treatment marked LEGAL_TAX_REVIEW_REQUIRED |
| RC-06 | §5 | **Petty cash** and **post-dated cheques (PDC)** — both routine in Thai SMEs — are not addressed. "Bank & Cash" is too coarse to infer either. | Medium | Explicit in/out-of-scope decision per item |
| RC-07 | §5 | **Recurring/template journals** absent. | Low | Candidate Phase 2; record as decision |
| RC-08 | §8 | **JournalEntry has no source-document linkage** (ref_type/ref_id to Invoice, Bill, Receipt, PaymentVoucher). Without it, subledger→GL drill-down and audit tracing are impossible. | High | Add fields in revision |
| RC-09 | §8 | Multi-currency: only BankAccount carries `currency`; JournalLine/Invoice/Bill have none, and no ExchangeRate entity exists. The data model silently assumes THB-only while OQ-ACC-002 is still open — an inconsistency either way the decision goes. | Medium | Resolve after OQ-ACC-002; note dependency |
| RC-10 | Header | Metadata mismatch: header "Path" says `ACC-001_ACCOUNTING_THAILAND_FDS_PACKAGE.md` but the actual filename is `ACC-001 Accounting Thailand Functional Design Specification Package.md`. | Low | Fix in revision (governance hygiene) |

---

## 3. Traceability Findings (confirmation of matrix)

I independently re-checked ACC-001 §5 against §12 and against `ACC-001_TRACEABILITY_MATRIX.md`. The matrix is **accurate**:

- 10 FRs MATCHED (internal only, unverified against source evidence);
- 2 FRs PARTIAL (FR-ACC-009, FR-ACC-010 — pending legal review);
- 8 FRs GAP with no or broken mapping: **FR-ACC-011, 012, 013, 015, 018, 019, 020** have no §12 row at all, and FR-ACC-001's mapping (API-ACC-013 / AC-ACC-007) actually belongs to Period Closing, not Accounting Setup — the FR-ACC-001 row is a **mis-mapping**, not a match. Setup has no dedicated API (no endpoint for company/tax-ID/branch/fiscal/document-number configuration) and no dedicated AC.
- Additional AC gaps beyond the matrix: FR-ACC-006 (Reverse) borrows AC-ACC-004 (edit-block) — no AC asserts that a reversal creates a correct opposite-sign journal in an open period. FR-ACC-018/019/020 have no AC.
- No UAT case exists for any FR (consistent with checklist item "QA/UAT test cases: Pending").

Conclusion: Traceability Gate remains **PARTIAL / HOLD**; matrix content confirmed, mis-mapping on FR-ACC-001 newly identified (raised as GAP-ACC-009 in `ACC-001_REMAINING_GAPS_CONFIRMATION.md`).

---

## 4. Thailand Accounting Correctness Findings

All items in this section are functional-design observations; none constitute legal or tax advice, and every rule authored from them must carry `LEGAL_TAX_REVIEW_REQUIRED` until the Accounting Owner / legal reviewer signs off (consistent with GAP-ACC-004 and AS-ACC-003).

| ID | Topic | Finding | Severity |
|---|---|---|---|
| TH-01 | VAT tax point | The FDS never defines the **tax point** (จุดความรับผิดภาษี) — goods vs services differ (delivery vs payment receipt). ภ.พ.30 monthly allocation (BR-ACC-008) cannot be computed correctly without it. | Critical |
| TH-02 | Tax invoice mandatory content | FR-ACC-011 does not enumerate the mandatory fields of a full tax invoice (the words "ใบกำกับภาษี", seller name/address/tax ID, buyer name/address/tax ID + branch code for VAT registrants, serial number, issue date, description/quantity/unit price, VAT amount shown separately). Without a field-level spec, UI/DB/print output cannot be designed or QA'd. | Critical |
| TH-03 | Abbreviated tax invoice | "อย่างย่อ ถ้ารองรับ" ("if supported") is an unresolved scope condition inside a Must-priority FR. Needs a decision: support, or explicitly out of scope Phase 1. | High |
| TH-04 | Credit/debit note linkage | FR-ACC-012 does not require reference to the original tax invoice and a reason code — both are required content for Thai credit/debit notes and drive VAT report adjustment lines. | Critical |
| TH-05 | WHT certificate content & filing | FR-ACC-010 covers calculation + certificate issuance, but: certificate (50 ทวิ) field content unspecified; WHT timing rule (obligation arises at payment, not bill date) unstated; ภ.ง.ด.3 / ภ.ง.ด.53 report FRs absent (only referenced in OQ-ACC-004); cross-border cases (ภ.ง.ด.54 / ภ.พ.36) not declared in/out of scope. | Critical |
| TH-06 | VAT/rounding | Satang rounding for VAT (per-line vs per-document) is unspecified. This is a classic source of 1-satang reconciliation failures between tax invoice, VAT report, and GL. | High |
| TH-07 | Document numbering policy | BR-ACC-009 (uniqueness) is correct but incomplete for tax documents: sequence reset policy (yearly/monthly/never), gap handling for cancelled tax invoices, and cancelled-document retention rules are unspecified. | High |
| TH-08 | Branch code format | Branch handling (BR-ACC-003) should pin the 5-digit branch code convention with "00000" = head office, and buyer-side branch capture on tax documents. | Medium |
| TH-09 | VAT rate configuration | No TaxCode/TaxRate configuration entity or FR exists (standard 7%, zero-rated, exempt, non-claimable input VAT). Hard-coding rates would be a design error. | High |
| TH-10 | e-Tax Invoice / e-Receipt | Confirmed firm gap (GAP-TH-01, OQ-ACC-001) — correctly excluded pending Boss decision; no change requested, dependency noted. | — |

---

## 5. Posting Rules Finding (structural)

The FDS Factory content standard requires "Posting Rules, if applicable". For an accounting module they are applicable and **entirely absent**: nothing defines the journal generated by an AR invoice (Dr AR / Cr Revenue / Cr Output VAT), a vendor bill (Dr Expense / Dr Input VAT / Cr AP), a payment with WHT (Dr AP / Cr Bank / Cr WHT Payable), a receipt, or a credit/debit note. WF-ACC-002/003 say "ระบบ post accounting" without stating what is posted. This blocks DB design, API design, QA design, and legal review alike. **Highest-priority revision item.**

---

## 6. API / DB / UI / QA Coverage Findings

| Area | Finding |
|---|---|
| API | Missing endpoints: accounting setup (FR-ACC-001), tax invoice issuance (FR-ACC-011), credit/debit note (FR-ACC-012), bank statement import + reconciliation (FR-ACC-013), P&L and balance-sheet reports (FR-ACC-015 — only trial balance and GL exist), export (FR-ACC-018), journal reject/revision action (WF step 5 has approve/reject/revise; only submit/post/reverse endpoints exist). Cross-cutting API conventions (tenant scoping, pagination, idempotency on POST, error model) deferred to Enterprise Architect review per GAP-ACC-005. |
| DB | Missing entities: CreditNote/DebitNote, BankStatement + reconciliation entities, TaxCode/TaxRate, WHTType/WHTRate configuration, DocumentSequence, FiscalYear (distinct from period), ExchangeRate (pending OQ-ACC-002), CostCenter/Project dimension (pending OQ-ACC-003). JournalEntry/JournalLine lack source-document reference and company/branch scope fields (AS-ACC-005 asserts scope on every transaction, but no entity carries the columns). |
| UI | SCR-ACC-010 merges Tax Invoice and Receipt — different documents, different rules; recommend split. No screen exists for credit/debit note, bank reconciliation, WHT filing reports (ภ.ง.ด.3/53 vs the certificate screen), or accounting setup sub-areas (numbering, tax codes, WHT types). |
| QA/UAT | Zero UAT cases (gate report action 7). AC set (10) covers happy paths only; no AC for Thai tax correctness (tax point, rounding, credit-note VAT adjustment), no negative/edge ACs for closed-period posting via API, cross-tenant access, or reversal in a closed period. |

---

## 7. Governance / Wording Findings

| ID | Finding |
|---|---|
| GV-01 | ACC-001 §18 Clean Room checklist marks its own rows "Pass" — self-assessment presented in approval language. Per Constitution §3 (AI must not approve its own work), rewrite as "Self-assessed — pending independent review". Substantively the Clean Room posture appears sound; the wording is the problem. |
| GV-02 | `ACC-001_GAP_ANALYSIS.md` closes with target state "READY FOR CHATGPT L99 RE-REVIEW". "READY" is outside the two controlled phrases permitted under /L99.99. Recommend PMO-approved rewording to "REQUIRES CHATGPT L99 REVIEW". |
| GV-03 | ACC-001 §15 asks Claude to output an "Approval / Hold Decision". Under /L99.99 Claude may output HOLD only, never approval. This review complies (HOLD); recommend §15 wording be corrected in revision so the template never invites AI approval. |

---

## 8. What Is Good (retain in revision)

- Scope/out-of-scope split (§3) is realistic for a Phase-1 Thai SME accounting core.
- BR-ACC-001/002/004 (balanced entry, no-edit-after-post, closed-period lock) are the correct non-negotiables and are individually testable.
- Reuse mapping to SaaS Foundation (§14) is explicit and consistent with FR reuse tags.
- Honest §13 self-disclosure of evidence status and §16 open questions — do not lose these in revision.
- WF-ACC-004 pre-close checklist (unposted / missing-evidence / pending-approval checks) is a strong governance-aligned design.

---

## 9. Review Decision Input

```text
State 3 Review Result: REVIEWED WITH COMMENTS
FDS Gate: HOLD / REVIEW REQUIRED — REVISION REQUIRED
Evidence Gate: PARTIAL / HOLD (unchanged)
Traceability Gate: PARTIAL / HOLD (unchanged; one new mis-mapping found)
All downstream gates (API/DB/UX/QA/Build/Production): HOLD (unchanged)
```

This document is review input only. It approves nothing, passes nothing, and certifies nothing.

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
