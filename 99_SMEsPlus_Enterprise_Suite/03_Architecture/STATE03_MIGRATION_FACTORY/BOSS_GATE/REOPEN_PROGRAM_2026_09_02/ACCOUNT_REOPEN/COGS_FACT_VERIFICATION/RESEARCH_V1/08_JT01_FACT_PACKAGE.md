# 08 — JT-01 Fact Package: Which Concept Owns Valuation Policy

Source definition: `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` — "`JT-01` | Which concept owns valuation policy. | Valuation report, close, landed cost, category design"

## 1. What Is Already Established (Fact)

- Product Category is the primary policy-carrying record for Costing Method and Stock/Valuation accounts in the reference ERP (DR file `04`, `11`).
- Product-level fields can override Category defaults for Income/Expense accounts, with observed precedence rules for several (not all) of the twelve tested cases (DR file `11`).
- The Category-level "Automated/Manual" (pre-19) or company-default-with-category-override (19.0, reconstructed) visibility gate itself is not a stable concept across versions (`CGS-U02`).
- Company-level settings (Continental/Anglo-Saxon accounting package) interact with Category, but whether this interaction is company-exclusive with no category override is unconfirmed (`CGS-U13`).

## 2. What Remains Unknown

| Unknown | Routed Register ID | Why It Blocks JT-01 |
|---|---|---|
| Expense Account field holds different account *types* under different modes, under the same label | `CGS-U06` | A single "owning concept" cannot be named if the field's meaning itself is mode-dependent |
| No confirmed answer on whether accumulated Stock Valuation Account balance re-classes on category reassignment | `CGS-U07` | Ownership of valuation policy is meaningless without knowing what happens when ownership (category) changes |
| No confirmed mechanical answer for effect of changing category/policy/account on existing stock | `CGS-U08` | Same reason |
| Journal-level fallback existence below Category is unconfirmed | `CGS-U09` | Affects whether Category is truly the terminal owner or an intermediate layer |
| Fiscal Position override scope vs. product-level account is `HOLD` | `CGS-U11` | A fourth candidate "owner" (Fiscal Position) is not ruled out |
| 19.0 field-by-field account model mapping incomplete | `CGS-U12` | Cannot name the owning concept in the *current* reference version with confidence |
| Continental/Anglo-Saxon company-exclusivity unconfirmed | `CGS-U13` | A company-level concept may compete with Category as "owner" |
| Whether Product Category is company-scoped by default is unconfirmed against official documentation | `CGS-U42` | If Category is not company-isolated, it cannot safely be the sole "owner" in a multi-tenant design without an additional isolation layer |

## 3. Fact vs. Configuration vs. Interpretation vs. Assumption vs. Target Design

| Layer | Statement |
|---|---|
| **FACT** | The reference ERP documents Category as the default carrier of Costing Method and Stock accounts, with Product as an override layer, in at least the versions and fields directly evidenced in DR files `04`, `11`. |
| **CONFIGURATION** | Whether a given deployment's Category or Product actually holds a value is a per-tenant configuration fact, not knowable in the abstract. |
| **INTERPRETATION** | Reading "Category is the policy owner" as a general architectural principle (rather than a version-specific UI default) is an interpretation this session makes explicit, not a directly-quoted statement from any source. |
| **ASSUMPTION** | That SMEsPlus should adopt a Category-as-owner model at all is not proven anywhere — it is the reference pattern, not a demonstrated requirement. |
| **TARGET DESIGN** | Not addressed in this session. SMEsPlus's own valuation-policy-owning concept, and whether it should mirror Category/Product at all, is a design decision for a later session, informed by but not decided by this fact package. |

## 4. Disposition

**PARTIALLY VERIFIED.** The reference pattern (Category owns, Product overrides) is fact-supported for the versions and fields directly evidenced. It cannot be treated as SMEsPlus's answer to "which concept owns valuation policy" because: (a) the field-level meaning shifts by mode (`CGS-U06`), (b) company-scoping of the candidate owner itself is unconfirmed (`CGS-U42`), and (c) the effect of changing ownership on existing stock is undocumented (`CGS-U07`, `CGS-U08`). New evidence (items in file `05` §"What This Means", points 2–3) could upgrade this from PARTIALLY VERIFIED toward FACT VERIFIED for the reference pattern, but closing `JT-01` itself always requires a SMEsPlus-specific Boss/design ruling on top of the facts, not facts alone — this file supplies the facts, not the ruling.

## 5. Does New Evidence Materially Change the Proposed Joint Decision?

No new evidence was acquired this session beyond re-verification (per the evidence ceiling in file `05`). The disposition above is therefore unchanged from the DR session's own position — this session's contribution is organizing the fact base specifically around the `JT-01` question, not new findings.
