# 02 — LEGAL-TAX REVIEW ROUTING EXECUTION RECORD

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-014` (commissioning) |
| Batch A Approved Direction | Proceed with Legal-Tax Review routing for WHT / VAT / CIT / DBD-NPAE |
| Batch A Control Status | `LEGAL_TAX_REVIEW_REQUIRED` |
| Boss Approval Record | branch `boss/account-batch-a-research-routing-approval-2026-09-02`, commit `fa75eb0ebfd8c3eee41b0e78c7afb39cbac7e751`, §2 row 2 |
| Source Routing Pack | `06_LEGAL_TAX_REVIEW_BRIEF.md`, branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`, commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| Gate Impact | `COA-G05`, `COA-G06` |

`Zero authoritative Thai statutory citations exist in the Account chain today` (source pack, citing `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` EG-03). This record does not add, remove, or resolve any statutory item. It executes the routing instruction: confirm the item count is unchanged, assign Owner/Evidence Location/Status/Gate Impact/Next Action at the category level, and confirm the brief is ready to hand to a reviewer.

## Category-level execution table

| Category | Item count | Owner | Evidence Location | Status | Gate Impact | Next Action |
|---|---|---|---|---|---|---|
| A. Withholding Tax (WHT) | 10 numbered items (`WHT-1`..`WHT-10`) + 6 engineering-risk items (`WHT-Eng-1`..`6`, detail withheld per source pack to avoid transcribing unreviewed engineering conclusions as fact) | UNASSIGNED — licensed Thai tax/accounting adviser | `06_LEGAL_TAX_REVIEW_BRIEF.md` §A | `LEGAL_TAX_REVIEW_REQUIRED` (all items, no exception) | `COA-G06`; cross-references `ACC-WHT-06` (see `03_ACC_WHT_06_RESEARCH_EXECUTION_RECORD.md`) | Boss commissions reviewer; hand §A only |
| B. Value Added Tax (VAT) | 6 numbered items (`VAT-1`..`VAT-6`) | UNASSIGNED | `06_LEGAL_TAX_REVIEW_BRIEF.md` §B | `LEGAL_TAX_REVIEW_REQUIRED` (all items) | `COA-G06` | Boss commissions reviewer; hand §B only |
| C. Corporate Income Tax (CIT) | 5 numbered items (`CIT-1`..`CIT-5`) | UNASSIGNED | `06_LEGAL_TAX_REVIEW_BRIEF.md` §C | `LEGAL_TAX_REVIEW_REQUIRED` (all items) | `COA-G06` | Boss commissions reviewer; hand §C only |
| D. DBD / NPAE statutory reporting | 6 numbered items (`DBD-1`..`DBD-6`), including `DBD-6` branch (สาขา) statutory status which also feeds `ACC-DEC-011` (SC-08) | UNASSIGNED | `06_LEGAL_TAX_REVIEW_BRIEF.md` §D | `LEGAL_TAX_REVIEW_REQUIRED` (all items) | `COA-G05`, `COA-G06` | Boss commissions reviewer; hand §D only |

**Total: 27 numbered statutory items + 6 engineering-risk items, all `LEGAL_TAX_REVIEW_REQUIRED`. Zero resolved by this or any prior AI session.**

## Required evidence-return format (unchanged, carried forward from source pack)

Each item the reviewer addresses must be returned with: Authoritative source, Citation, Effective date, Reviewer (name + credential), Conclusion, Implementation impact, Open questions. This structure is required so the reviewer's output can be re-imported into the source register without reinterpretation.

## Commissioning routing (execution of §E of the source brief)

| Step | Action | Owner | Status |
|---|---|---|---|
| 1 | Select a licensed Thai tax/accounting adviser (CPA or Revenue-Department-registered preparer) | Boss | `UNASSIGNED — NOT YET SELECTED` |
| 2 | Hand reviewer sections A–D of `06_LEGAL_TAX_REVIEW_BRIEF.md` only (not the raw source package) — clean-room boundary between Layer 1 process reference and Layer 2 audit quarantine | Boss | `PENDING STEP 1` |
| 3 | Require reviewer output in the evidence-field format above, item by item | Boss / Reviewer | `PENDING STEP 1` |
| 4 | Re-import reviewer citations into source file `10` (`10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` cross-reference) and update each `LEGAL_TAX_REVIEW_REQUIRED` status individually | Next execution session (not this one) | `PENDING STEP 1–3` |

## Explicit non-claim

No item in sections A–D is closed, narrowed, or answered by this record. Only a named, credentialed reviewer's output, or a directly cited statute/regulation, may close a `LEGAL_TAX_REVIEW_REQUIRED` status — consistent with source pack §E.5, which this record does not override.
