# ACC-001 UI Handoff Review Notes (State 3)

Document ID: SMEPLUS-STATE03-ACC-UIREV-001
Version: v1.0
Status: REVIEWED WITH COMMENTS — **NOT a UI handoff; do not send to UI/Figma**
Gate Status: HOLD / REVIEW REQUIRED (UX Gate: HOLD per L99 gate report)
Owner: Claude AI (State 3 Reviewer, /L99.99)
Approver: Boss / Final Gate Owner
Source: ACC-001 v1.0 §10 (UI / Screen Mapping), §4 (Roles), §11 (AC)
Generated: 2026-07-07 (Asia/Bangkok)

---

## Purpose

Assess whether ACC-001 §10 is functionally sufficient to become a UI handoff after revision. Per Boss order, nothing is sent to UI/Figma from this review. This document records readiness deficiencies only.

## Overall Assessment

§10 is a screen inventory, not a handoff. It maps 15 screens to FRs but contains none of the handoff-required content (fields, validation, status behavior, approval behavior, error behavior, audit visibility, open UI questions). **UI handoff readiness: NOT READY FOR HANDOFF — blocked pending revision** (this is a readiness observation, not a gate status).

## Screen-Level Findings

| Screen | Finding | Severity |
|---|---|---|
| SCR-ACC-010 Tax Invoice / Receipt | Two legally distinct documents merged into one screen. Tax invoice content rules (mandatory fields, branch, cancellation) differ entirely from receipt behavior. Split into two screens. | High |
| Missing screen — Credit / Debit Note | FR-ACC-012 has no screen. Requires original-invoice selection, reason capture, VAT adjustment preview. | High |
| Missing screen — Bank Reconciliation | FR-ACC-013 reconciliation has no screen (statement import, match/unmatch, difference handling). | High |
| Missing screens — WHT filing reports | SCR-ACC-009 covers the certificate; ภ.ง.ด.3 / ภ.ง.ด.53 report views (pending OQ-ACC-004 format decision) have no screen. | Medium |
| Missing screens — Setup sub-areas | SCR-ACC-002 is a single "Accounting Setup" screen for company/tax ID/branch/fiscal periods/document numbering/tax codes/WHT types — too coarse; needs sub-screen decomposition once REV-03/REV-04 define the configuration objects. | Medium |
| SCR-ACC-005 Journal Entry Form | Status model incomplete for UI: statuses implied across §7/§11 are Draft → Submitted → Approved/Rejected/Revision-Requested → Posted → Reversed, but no status enumeration exists anywhere in ACC-001. UI cannot render state behavior without it. | High |
| SCR-ACC-012 Period Closing | Strong pre-close checklist design (WF-ACC-004) — good handoff candidate once check-result presentation and blocking behavior are specified. | Low |
| SCR-ACC-014 / SCR-ACC-015 | Evidence Panel and Audit Log Viewer are Reuse (SaaS Foundation); handoff should reference the Foundation design system components rather than redesigning. | Low |

## Cross-Cutting UI Requirements Absent from ACC-001

1. **Field-level definitions** — no screen has a field list; blocked until REV-03/REV-04 (tax fields, entities) complete.
2. **Role × screen access matrix** — §4 roles exist but no mapping of which role sees/edits which screen (BR-ACC-010 implies it; not specified).
3. **Thai/English bilingual output** — Thai-language document output is named in module scope but no screen/print template requirement states which documents render in Thai, bilingual, or per-tenant configurable.
4. **Print/PDF layouts** — tax invoice, receipt, credit/debit note, WHT certificate, payment voucher all require statutory-content print layouts; none specified (depends on REV-03, LEGAL_TAX_REVIEW_REQUIRED).
5. **Error/validation behavior** — ACs define blocking outcomes (e.g., AC-ACC-001 unbalanced journal) but no error-message or inline-validation requirements exist.
6. **Closed-period and posted-document affordances** — UI must visibly disable edit on posted/closed items (BR-ACC-002/004); unstated.

## Open UI Questions (for future handoff, not for action now)

| ID | Question | Owner |
|---|---|---|
| UIQ-ACC-001 | Journal entry grid: line-entry style and account lookup behavior for Thai account names/codes? | Figma UX UI AI (after handoff) |
| UIQ-ACC-002 | Document print preview inside web app vs direct PDF download? | Boss / UX |
| UIQ-ACC-003 | Thai Buddhist calendar year display on tax documents vs CE internally? | Accounting Owner / UX |
| UIQ-ACC-004 | Mobile scope for approvals (Approver role) in Phase 1? | Boss |

## Handoff Preconditions (checklist for a future UI Handoff Draft)

- [ ] REV-01 posting rules (drives document forms)
- [ ] REV-03 tax annex authored (drives statutory fields/layouts)
- [ ] REV-04 entities finalized (drives field lists)
- [ ] Status enumeration for all documents defined
- [ ] Role × screen matrix authored
- [ ] Boss decisions on OQ-ACC-001/002/003 and REV-08 scope
- [ ] ChatGPT L99 + PMO review of revised ACC-001 v1.1

No UI handoff is prepared or sent by this document.

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
