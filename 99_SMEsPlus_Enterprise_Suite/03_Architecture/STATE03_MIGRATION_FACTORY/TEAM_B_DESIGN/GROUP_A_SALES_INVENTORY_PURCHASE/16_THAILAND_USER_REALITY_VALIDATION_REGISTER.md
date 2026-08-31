> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 9 — Thailand / User-Reality Design Controls

# 16 — THAILAND / USER-REALITY VALIDATION REGISTER

## 00 — Governing Discipline (TBRAC, Restated as Binding on This File)

TEAM B preserves the distinction Team A's evidence already applies and does not elevate any customer-specific
observation to a Thailand-wide or SME-wide claim: `Reference ERP Behaviour` / `Observed Customer Practice` /
`Company Variation` / `Industry Variation` / `Verified Thai Business Reality` / `SMEsPlus Target Requirement`.
**No item in this register is classified `Verified Thai Business Reality`** — consistent with Team A's own
register, since this session performed no new user validation of its own.

## 01 — TBRAC Items Carried Forward from Team A Evidence (Unmodified Classification)

| # | Observation | TBRAC classification | GROUP A relevance | TEAM B design implication |
|---|---|---|---|---|
| 1 | Two independent, uncoordinated Thai "tax branch" implementations on Party | `Company Variation` | Party is a Shared Master concept both Sales and Purchase consume | TEAM B's canonical Party model (`04` §01) treats Tax-Branch as one attribute, not two; does not design for two competing implementations — see also [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) |
| 2 | Thai legal-entity name composition (prefix/suffix pattern) | `Observed Customer Practice` | Affects how Party names render on Commercial/Supply documents | Not designed into the canonical Party concept — a presentation/localization concern, not a structural one |
| 3 | Tax-branch identifier consumed by WHT reporting | `Observed Customer Practice` | Accounting-interface only | Out of GROUP A design scope, per [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md) §07 |
| 4 | WHT subsystem exists, zero coupling to Commercial/Supply Commitment | `Observed Customer Practice` (existence); `Unknown / Requires Real-User Validation` (form-code currency) | Confirms the Financial Handoff boundary is sufficient — WHT never needs a GROUP A-side capability | Confirmed boundary in [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md) §07 |
| 5 | Thai province/district/sub-district address hierarchy | `Observed Customer Practice` (existence); `Unknown / Requires Real-User Validation` (whether it reaches delivery/shipping) | Potentially relevant to Party addressing used by Sales/Purchase | Not designed as a required capability — no code path evidenced reaching a delivery workflow; carried forward as a real-user-validation item, not assumed necessary |
| 6 | Two byte-identical "amount in words" modules | `Company Variation` (duplication itself) | Print-layout concern, reached only from the Financial Handoff's far side | Out of GROUP A design scope |
| 7 | Whether "amount in words" is a universal Thai legal-document requirement | `Unknown / Requires Real-User Validation` | Same as #6 | Not asserted; carried forward |
| 8 | Thai-language urgency levels on Internal Demand Request | `Observed Customer Practice` | Directly on the demand-signal layer this design covers | TEAM B's canonical Internal Demand Request ([07](07_PURCHASE_CANONICAL_DESIGN.md) §04) does not mandate a Thai-specific urgency taxonomy — a configurable classification field is a reasonable general capability, not asserted as a Thailand-specific requirement here |
| 9 | Whether Company/Branch hierarchy maps onto real Thai SME legal/operating structures | `Unknown / Requires Real-User Validation` | Both Sales and Purchase depend on accessible-branch resolution | Carried forward unresolved — see [14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md) §07 |
| 10 | Tax-inclusive vs. tax-exclusive default pricing (VAT-inclusive retail convention) | `Reference ERP Behaviour` (mechanism); `Unknown / Requires Real-User Validation` (whether this build's default matches Thai retail convention) | Directly affects Sales/Purchase line pricing | TEAM B's canonical Tax Rule ([04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §04) supports a per-tax inclusive/exclusive setting as a general capability; does not assert a Thailand-specific default |

## 02 — Explicitly Not Investigated (Honest Scope Boundary, Restated)

- VAT filing/reporting mechanics beyond the WHT-adjacent interface.
- E-tax-invoice / e-receipt government integration — unresolved whether this build has one at all.
- Any live-system, interview, or transactional-data validation of any item above. This TEAM B session performed
  no new Thailand-specific research of its own; it only reasoned about design implications of Team A's existing
  TBRAC-classified findings.

## 03 — Persona / Real-User-Reality Gaps Carried Forward (from Team A's Persona Matrix)

Per governing prompt §17 discipline, every persona-related claim in Team A's evidence is `Unknown / Requires
Real-User Validation`. TEAM B carries forward, unresolved, the two items Team A flagged as highest-value for a
real-user interview, because both bear directly on design decisions this package leaves open:

1. **Whether staff experience/expect the sequential level-based approval workflow as a two-person, sequential
   process** — directly relevant to [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) APR-002's `HOLD`.
2. **Whether a real Purchase-Request approver uses a different screen/flow than the one the base mechanism
   implements** — relevant to the same HOLD, and to [07](07_PURCHASE_CANONICAL_DESIGN.md) §04's approver-
   assignment design.

Additionally carried forward, relevant to open design decisions elsewhere in this package:

3. **Whether a salesperson promising a delivery date without a hard stock check is a real operational problem in
   practice** — directly relevant to [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) APR-003's confirmation-
   gate policy decision.
4. **Whether external parties (customers/vendors) interact via portal, email, or an entirely separate channel** —
   explicitly flagged by governance as a blind spot no source-code-only research pass can fill; not designed for
   or against in this package.

## 04 — Boss Gate §4.3 Carry-Forward — Fit-Gap Candidate #15

Per Boss Gate §4.3, the statement "many SME businesses expect a salesperson-initiated RMA" (Team A Fit-Gap
candidate #15's rationale) is carried forward here, explicitly, as `HYPOTHESIS / REQUIRES REAL USER VALIDATION` —
**never** treated as a verified Thai/SME-wide fact anywhere in this design package. TEAM B's own decision on the
underlying design question (whether to design a Sales-initiated RMA affordance) is recorded independently in
[17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md)
and does **not** rely on this hypothesis as evidence — it is treated as an open question, not a justification.

## 05 — Consolidated Statement

No claim in this file, or in any other TEAM B deliverable in this folder, asserts a Thailand-wide or SME-wide
business requirement that is not independently classified `Verified Thai Business Reality` by primary evidence —
and no such classification exists anywhere in the approved evidence package. Every Thailand-adjacent design
decision in this package (Tax-Branch handling, Tax-inclusive pricing support, Company/Branch structure, approval
workflow shape) is stated as a **general capability requirement**, with any Thailand-specific default or
mandatory behavior explicitly deferred to real-user validation.
