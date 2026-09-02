# 06 — LEGAL-TAX REVIEW BRIEF

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-014` (commissioning) |
| Source | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` EG-03, OB-01/02/03/16/18; `21_BOSS_FINAL_GATE_PACKAGE.md` §6 item 5; `22_NEXT_PROMPT_RECOMMENDATION.md` §2 item 3; source `10_TAX_WHT_VAT_CIT_REPORTING_MAP.md` (referenced, not reproduced verbatim here) |
| Owner | UNASSIGNED — a licensed Thai tax/accounting adviser, to be commissioned by Boss |
| Status | `LEGAL_TAX_REVIEW_REQUIRED` for every item below, without exception |
| Gate Impact | `COA-G05`, `COA-G06` |

`No Evidence = No Progress.` This brief does not give legal or tax advice. It routes open statutory questions to a qualified reviewer and defines the evidence format their answer must arrive in. **Zero authoritative Thai statutory citations exist in the Account chain today** (source `20` EG-03) — every line below is currently unsupported by a cited legal or tax source and must remain `LEGAL_TAX_REVIEW_REQUIRED` until either a qualified Thai legal-tax/accounting reviewer signs off, or an authoritative legal/tax source is attached.

## Required evidence field format (per item)

Each item the reviewer addresses must be returned using this exact structure so it can be re-imported into the source register:

| Field | Description |
|---|---|
| Authoritative source | Statute, Revenue Department regulation/order, DBD notification, TFRS for NPAEs section, etc. |
| Citation | Section/article/order number |
| Effective date | Date the cited provision took effect (or "unchanged since [year]") |
| Reviewer | Name and credential (e.g., licensed Thai CPA, Revenue Department-registered tax preparer) |
| Conclusion | Plain-English statement of what SMEsPlus must do |
| Implementation impact | Which SMEsPlus account/report/process this affects |
| Open questions | Anything the reviewer could not resolve |

## A. Withholding Tax (WHT)

| # | Item | Source in Account package | Status |
|---|---|---|---|
| WHT-1 | Multi-rate WHT categories and percentages (services, rent, professional fees, transport, advertising, etc.) — see also `04_ACC_WHT_06_MODULE_BASELINE_DECISION_PACK.md` | 10 §2 (referenced); A2 §B.1 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-2 | Sales-side WHT chain: no report grid, no received-certificate tracking, CIT-credit chain unevidenced | 10 objection 10; OB-03 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-3 | Purchase-side WHT liability recognition and payment cycle | 10 §2 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-4 | Tax-group closing accounts: benchmark Thai template **nets purchase-side WHT liabilities against sales-side WHT assets** — flagged as a design risk, must not be inherited without confirmation | 10 §2.2; 18 ST-07; OB-01 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-5 | PND3 (individual payee WHT return) | 10 §5 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-6 | PND53 (juristic payee WHT return) | 10 §5 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-7 | PND1 (employment income WHT) — scope status itself undecided, see `ACC-DEC-009` | 10 objection 7/9 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-8 | PND54 (payments to non-residents) — scope status itself undecided | 10 objection 9 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-9 | PP36 (VAT self-assessment on services from abroad) where applicable | 10 §5 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-10 | Candidate monthly WHT filing calendar — dates are unverified and must not become design constants | 10 objection 8; OB-16 | `LEGAL_TAX_REVIEW_REQUIRED` |
| WHT-Eng-1..6 | Six engineering risk items flagged in source 10 around WHT posting/reporting mechanics (see source file for detail; not reproduced here to avoid transcribing unreviewed engineering conclusions as fact) | 10 §2 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |

## B. Value Added Tax (VAT)

| # | Item | Source | Status |
|---|---|---|---|
| VAT-1 | Output VAT recognition and reporting | 10 §3 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| VAT-2 | Input VAT recognition and reporting | 10 §3 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| VAT-3 | Exempt VAT — benchmark's exempt-input-VAT template **contradicts its own Thai description** in the instance observed | 10 objections 4, 6; OB-02 | `LEGAL_TAX_REVIEW_REQUIRED` |
| VAT-4 | Non-deductible input VAT — no template observed in the benchmark | 10 objection 6; OB-02 | `LEGAL_TAX_REVIEW_REQUIRED` |
| VAT-5 | Undue VAT accounts present in the Thai template but with no attached process | 10 objection 6; OB-02 | `LEGAL_TAX_REVIEW_REQUIRED` |
| VAT-6 | PP30 (monthly VAT return); benchmark template provides grid lines 1–12 (evidenced fact, not a legal conclusion) | 21 §2 item 6 | `LEGAL_TAX_REVIEW_REQUIRED` (grid *usage* rules still need review even though grid *lines* are evidenced) |

## C. Corporate Income Tax (CIT)

| # | Item | Source | Status |
|---|---|---|---|
| CIT-1 | PND50 (annual CIT return) | 10 §4 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| CIT-2 | Bad-debt deductibility rules | 10 §4 (referenced); 20 EG-06 | `LEGAL_TAX_REVIEW_REQUIRED` |
| CIT-3 | Depreciation rate evidence (statutory rates by asset class) | 10 §4 (referenced); 12 §6 | `LEGAL_TAX_REVIEW_REQUIRED` |
| CIT-4 | Legal reserve requirement, if relevant to SMEsPlus's target entity types | 10 §4 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| CIT-5 | Tax Units / group filing treatment | 22 §2 item 3 (referenced as "Tax Units group filing") | `LEGAL_TAX_REVIEW_REQUIRED` |

## D. DBD / NPAE (statutory financial reporting)

| # | Item | Source | Status |
|---|---|---|---|
| DBD-1 | DBD statutory statement format | 22 §2 item 3; 09 §5 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| DBD-2 | Cash-flow statement requirement for NPAE-basis entities | 09 objection 6; OB-18 | `LEGAL_TAX_REVIEW_REQUIRED` |
| DBD-3 | Statutory books (which books are legally required, in what form) | 22 §2 item 3 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| DBD-4 | Audit trail requirements at statutory level (distinct from SMEsPlus's own internal audit-trail design in source 14) | 14 OBJN-03 (referenced) | `LEGAL_TAX_REVIEW_REQUIRED` |
| DBD-5 | Thai statutory report display names (distinct question from Thai *menu* names — see `08` for the TBRAC usability track; this item is about legally mandated report titles) | 22 §2 item 3 | `LEGAL_TAX_REVIEW_REQUIRED` |
| DBD-6 | Branch (สาขา) statutory reporting status — is a branch a separate statutory reporting unit? (feeds `ACC-DEC-011` / SC-08) | 13 objections 2, 4 | `LEGAL_TAX_REVIEW_REQUIRED` |

## E. Commissioning instructions for Boss

1. Select a licensed Thai tax/accounting adviser (CPA or Revenue-Department-registered preparer). Owner field is `UNASSIGNED` until named.
2. Hand the reviewer sections A–D of this brief (not the raw source package, to preserve the clean-room boundary between Layer 1 process reference and Layer 2 audit quarantine — see session memory on clean-room rules).
3. Require the reviewer's output in the evidence-field format above, item by item.
4. On return, this session's successor re-imports the reviewer's citations into source file `10` and updates every `LEGAL_TAX_REVIEW_REQUIRED` status above to either `LEGAL_TAX_REVIEW_COMPLETE — <conclusion>` or a narrowed follow-up question.
5. No item in this brief may be marked complete by an AI session. Only a named, credentialed reviewer's output — or a directly cited statute/regulation — may close a `LEGAL_TAX_REVIEW_REQUIRED` status.
