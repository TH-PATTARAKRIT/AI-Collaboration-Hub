# 4 AI Expert Roles — Overlay Review Matrix

These roles review and comment only. **Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

---

## Leader Functional Design
**Overlay scope:** Expert IBPV / Team B / Figma-UX / UAT flow.
**Review:**
- **AR/AP:** No dedicated WHT-receivable GL account type and no customer-certificate tracking model exist for sales-side WHT (`02_ACC_WHT_SALES_SIDE_PROOF.md`) — functional-flow risk if a UAT scenario exercises sales WHT before this is designed.
- **Tax (WHT):** Multi-rate payments silently drop GL tagging in the source behavior (`08_ACC_WHT_MULTI_TYPE_MULTI_RATE_CHALLENGE.md`) — a real functional risk to carry into any SMEsPlus payment-registration flow design, not just a documentation gap.
- **Close:** Monthly/Fiscal-Year close is well-specified and test-backed (`B19`) — low functional risk.
- **Account × Inventory interface:** Boundary is clean at the principle level; landed-cost/return/adjustment flows are untraced — moderate risk of UI/flow surprises at those specific scenarios.

**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

---

## Leadership Database Design
**Overlay scope:** Team A / Team B / Team C / Migration proof.
**Review:**
- Data-identity invariants (BINV-09 through BINV-14) are well-formed and internally consistent, including the Round-2 correction that separated ordinary Period close from Fiscal Year close (`M-AUD-05`).
- GL/TB migration proof (MG-C11) is concrete and testable.
- **Real migration-proof risk:** AR/AP and fixed-asset subledgers have zero research performed — any migration attempt today would have no data-identity guarantee for those two subledgers.
- The `COA_G01_EVIDENCE`/`COA_G01_SOURCE_PORT` cluster (99 + 63 files) likely contains further reconciliation detail not yet content-verified — flagged for follow-up, not assumed either way.

**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

---

## Lead Integration & Localization
**Overlay scope:** Expert IBPV / Team C / Thai accounting-tax-localization.
**Review:**
- **WHT:** Real, substantive, partial — Boss's own Partial Acceptance decision is the accurate current status; do not represent as closed.
- **VAT/CIT:** Zero research performed anywhere in the inspected corpus — this is a genuine open scope question (in-scope-but-unresearched vs. explicitly deferred), not yet a "gap" because it was never opened.
- **PND3/PND53:** Working code path exists but carries a real code-quality/localization risk (duplicated `tax_report_pnd.py` logic, hardcoded WHT-condition export value) that would need remediation before being treated as SMEsPlus's own design, not just proof against the old source.
- **50-TWI:** 5 concrete form-field gaps identified and already correctly routed to legal-tax review — good practice, no action needed beyond completing that review.

**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

---

## Lead Code & UI Architect
**Overlay scope:** Team C / Team D / Expert IDTM / QWeb-Code-UI proof. Future implementation impact only; no Team C authorization; no UI/API code design performed or implied by this note.
**Review:**
- Two specific defects were observed in the *old source system* during WHT proof work and should NOT be inherited by any future SMEsPlus implementation: (1) `wizard/account_payment_register.py:64` gates WHT GL tagging on `len(wt_tax) == 1`, silently dropping tagging for multi-rate payments; (2) `tax_report_pnd.py` logic is duplicated across two modules, making PND export output deployment-dependent.
- These are noted purely as forward-looking implementation-risk flags for whenever Team C/D work is authorized — **no such authorization exists today**, and none is implied here.

**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**
