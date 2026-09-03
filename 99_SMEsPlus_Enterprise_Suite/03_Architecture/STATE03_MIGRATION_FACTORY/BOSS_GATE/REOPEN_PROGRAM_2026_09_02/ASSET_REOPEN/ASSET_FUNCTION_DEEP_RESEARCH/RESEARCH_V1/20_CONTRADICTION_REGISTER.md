# 20 — Contradiction Register

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `OPEN-ITEM REGISTER — NOTHING BELOW IS CLOSED BY THIS SESSION`

---

## 1. Purpose and Format

Per file column requirements: Claim / Evidence A / Evidence B / Severity / Impact / Possible Explanations / Required Proof / Resolution Status. Resolution Status uses `UNRESOLVED` explicitly, never ambiguous synonyms like "open" or "pending."

---

## CR-01 — Equipment↔Asset Native Link

- **Claim**: The reference ERP natively links an Equipment record to a fixed-asset Asset record.
- **Evidence A (for)**: None located as official documentation.
- **Evidence B (against)**: Two independent forum threads explicitly frame this as an integration a business must build via customization (adding a link field), implying no native field exists.
- **Severity**: `BLOCKING`
- **Impact**: Both Cost Lineage A and B (file `19`) fail at their first link without this. Hypothesis A cannot be operationally implemented without an equivalent mechanism being built new.
- **Possible Explanations**: (a) genuinely absent in all documented versions; (b) present in a version/edition not covered by this session's search; (c) present but under different terminology this session's queries did not match.
- **Required Proof**: Direct inspection of a live reference-ERP instance's Equipment form fields across several versions, or an official documentation page explicitly describing such a field, not yet located.
- **Resolution Status**: `UNRESOLVED`

## CR-02 — "Product" Field on Equipment

- **Claim**: Equipment has a native Product field.
- **Evidence A (for)**: A third-party "link Equipment and Products" module's existence implies some users want this and don't have it, which is actually evidence *against* nativeness, not for it — listed here as a claim this file tested and found weak support for, not as a genuine two-sided conflict.
- **Evidence B (against)**: No official documentation page located describing a native Product field on Equipment.
- **Severity**: `MATERIAL`
- **Impact**: Affects file `05`'s lineage-mapping confidence.
- **Possible Explanations**: Terminology/version variance; genuinely absent.
- **Required Proof**: Direct instance inspection.
- **Resolution Status**: `UNRESOLVED`

## CR-03 — Royal Decree Number for Thai Depreciation Caps

- **Claim**: Thai statutory depreciation-rate caps are set by Royal Decree No. 145.
- **Evidence A (for)**: The Boss's own prompt states this number; one secondary community source used the same number in an unrelated context.
- **Evidence B (against)**: A directly retrieved Thai tax-advisory summary page (Sherrings) references Royal Decrees 620 and 473 in its own citations, not 145, when discussing the same rate table.
- **Severity**: `BLOCKING` for any SMEsPlus documentation that cites a specific decree number as its statutory authority.
- **Impact**: If SMEsPlus cites the wrong decree number in a compliance-facing document, that is a credibility and potentially compliance-review risk.
- **Possible Explanations**: (a) 145 is the correct principal decree and 620/473 are later amending decrees the secondary source cited instead of the base decree; (b) the Boss's prompt (and the community source echoing it) is simply mistaken about the number; (c) multiple decrees govern different aspects and both citations are partially correct.
- **Required Proof**: Direct retrieval and reading of the Royal Decree gazette text itself, cross-checked by decree number, under the Revenue Code's depreciation provisions.
- **Resolution Status**: `UNRESOLVED`

## CR-04 — Whether "Daily Calculation" Applies to Tax Depreciation, Accounting Depreciation, or Both

- **Claim** (Boss assertion, restated): Thai depreciation uses daily calculation.
- **Evidence A (for, tax side)**: Secondary community-forum source explicitly states daily (365/366-day) tax depreciation is Thai business practice.
- **Evidence B (against/qualifying)**: The directly retrieved authoritative-leaning tax-advisory source describes a "proportion to the period from acquisition" principle without using the word "daily"; IAS 16 (accounting side) imposes no day-count mandate at all, leaving method choice to the entity.
- **Severity**: `MATERIAL`
- **Impact**: Determines whether SMEsPlus's tax-depreciation computation engine must be day-precise, and whether that requirement extends to the statutory accounting books as well or only the separate tax computation.
- **Possible Explanations**: The assertion may be correct for tax depreciation specifically (Revenue Code proration read literally as daily) while not applying to accounting depreciation at all (TAS 16 leaves this open) — i.e., not a true contradiction but a scope-precision issue in how the Boss's one-line assertion was phrased.
- **Required Proof**: Primary Royal Decree/Revenue Department text (see CR-03).
- **Resolution Status**: `UNRESOLVED`

## CR-05 — Depreciation Participation in Manufacturing Cost Lineage (Hypothesis A)

- **Claim**: Active depreciation flows into production cost (Boss Hypothesis A).
- **Evidence A (for)**: None located in reference-ERP documentation; Hypothesis A is stated as Boss-approved business intent, not as an observed system behavior — this file does not treat the Boss's own hypothesis-framing as "evidence for," only as the claim under test.
- **Evidence B (against)**: File `11` §3 — no documented mechanism connects Asset depreciation to Work Center cost; file `19` Lineage A shows the break occurs at the very first link.
- **Severity**: `BLOCKING` for any Hypothesis-A design that assumes reference-ERP adaptation rather than original construction.
- **Impact**: Reframes Hypothesis A from "adapt an existing pattern" to "build new," with corresponding schedule/review implications.
- **Possible Explanations**: The reference ERP simply does not implement this pattern (most likely, given convergent negative evidence across files `04`, `06`, `11`, `12`); alternatively, a non-core/enterprise-only module not covered by this session's public-documentation search might implement it.
- **Required Proof**: Direct instance inspection, or a documentation page for a module edition not searched in this session.
- **Resolution Status**: `UNRESOLVED`

## 2. Register Roll-Up

| Severity | Count |
|---|---:|
| `BLOCKING` | 3 (CR-01, CR-03, CR-05) |
| `MATERIAL` | 2 (CR-02, CR-04) |
| **Closed by this session** | **0** |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
