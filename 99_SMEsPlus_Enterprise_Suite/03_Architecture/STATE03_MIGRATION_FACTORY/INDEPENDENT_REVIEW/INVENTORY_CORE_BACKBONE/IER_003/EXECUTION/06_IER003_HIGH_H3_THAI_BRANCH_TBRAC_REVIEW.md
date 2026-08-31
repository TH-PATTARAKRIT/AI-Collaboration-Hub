# 06 — High H3 (GRPA-H8): Two Thai Branch Concepts — Independent Verdict

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently test GRPA-H8's classification, distinguish structural conflict from Thai business/regulatory reality (TBRAC) | Independent Evidence Reviewer | `l10n_th/models/res_partner.py`, `addons_extra/l10n_th_partner/models/res_partner.py`, `res_company` table | 2026-09-01 | Boss | **CONFIRMED CONFLICTING PRACTICE — WITH ONE CORRECTION** | Remains an Inventory Gate decision-point, not a blocker; `REQUIRES REAL USER VALIDATION` stands |

## TEAM A's claim (A14 Part 1, GRPA-H8; reused from GROUP A Scenario 11)

Two structurally uncoordinated Thai "branch" concepts: (a) "Branch" implemented as a child `res.company` record, and (b) a separate "Thai Tax Branch" `Char` field on `res.partner` with zero structural connection to the company hierarchy.

## What this review found

### Two branch mechanisms — confirmed as genuinely separate and uncoordinated

| Mechanism | Module | Field | Character |
|---|---|---|---|
| A | `l10n_th` (official Thai localization, `02 OTHER/`) | `res.partner.l10n_th_branch_name` — **computed**, `_compute_l10n_th_branch_name()` | Derived display value from `partner.company_registry` (Thailand's tax-ID field): if the partner is a Thai company and `company_registry` is set, shows "Branch {code}", else "Headquarter". Not independently stored; not user-editable. |
| B | `l10n_th_partner` (third-party addon, author "Ecosoft", `addons_extra/`) | `res.partner.branch` — **stored** `Char`, label "Tax Branch", help text "Branch ID, e.g., 0000, 0001, ..." | User-entered, independent of `company_registry` |

Both modules are confirmed **installed** in this customer's database (`ir_module_module`: `l10n_th`, `l10n_th_partner`, `l10n_th_reports` all `state='installed'`). Cross-checked both files fully: neither references the other's field, neither reads or writes the other's value. **This independently corroborates the core GRPA-H8 finding — two genuinely uncoordinated branch representations coexist and are both live in this customer's system**, not merely theoretically present in the source tree.

### Correction: the "child res.company" characterization is not confirmed by this dataset's actual data

`res_company.parent_id`/`parent_path` (standard Odoo multi-company hierarchy columns) **do exist** in the schema — the structural *capability* for a child-company branch pattern is real. But this specific customer's database contains **exactly one `res.company` row**, with `parent_id` unset. There is no second, child company record to examine — meaning the specific claim "branch is implemented as a child `res.company` record" cannot be verified as this customer's *actual practice* from this dataset; it can only be confirmed as a *structurally available* Odoo mechanism. TEAM A's own A5 §3 language ("Branch... is a child `res.company` record") states this more definitively than the data supports. Recorded as a targeted correction, not a rejection: the two-Char-field conflict (mechanisms A and B above) is fully confirmed regardless of this correction.

### TBRAC challenge — addressed directly

Per the readiness record's TBRAC instruction, this review does not treat either implementation as Thailand-wide statutory truth. Both are one customer's (or one vendor pairing's) implementation choices. No Thai Revenue Department source, statute, or regulation was consulted by this review — the regulatory question underneath ("what does Thai law actually require for branch-level tax/inventory reporting") remains genuinely untested, exactly as TEAM A's own TH-INV-01 already discloses.

## Independent verdict

**`CONFLICTING EVIDENCE` (structural conflict) combined with `REQUIRES REAL USER VALIDATION` (which pattern, if either, reflects correct/intended practice)** — TEAM A's own dual classification is upheld, with the correction above folded in.

- Evidence read: both branch-field implementations in full; both modules' install state; the customer's actual company-table cardinality (1 row, unbranched).
- What remains unknown: (1) whether the customer's real business operations use either field meaningfully or if both are vestigial/unused (this dataset's `stock_move` table has only 48 rows total across 2 states — see [09](09_IER003_DATABASE_DUMP_REVERIFICATION_REPORT.md) — too small a sample to infer operational usage of either branch field); (2) the underlying Thai statutory requirement itself.
- **Inventory Gate blocking: `DECISION-POINT ONLY`**, not a hard blocker — consistent with TEAM A's own framing that this scopes a future canonical-design decision rather than proving Stock Truth is currently wrong.
- Stock Truth impact: Indirect — confirmed no core `stock.*` model references either branch field directly; the impact is entirely at a future warehouse/location-scoping design layer, if SMEsPlus chooses to make branch a first-class Inventory dimension.
- Accounting interface impact: Indirect, via journal/tax context — unchanged from TEAM A's assessment.
- SaaS/tenant impact: High, unchanged from TEAM A's A10 SAAS-02 assessment — now strengthened by direct confirmation that both mechanisms are simultaneously live in production data, not a source-only hypothetical.
- Migration impact: High, unchanged.
- Thailand impact: Direct — this is the one item in the entire five-High set that is genuinely a statutory/business-reality question, not a source-research gap.
- **Next owner / next action**: `REQUIRES REAL USER VALIDATION before either source pattern is adopted or replaced` (TEAM A's own next action, upheld unchanged) — an external dependency, not a Team A re-research task.

No Unknown was converted to a Fact — the structural conflict is now confirmed with higher precision (module names, install state, exact field mechanics); the business-reality question underneath is left exactly as open as TEAM A left it.
