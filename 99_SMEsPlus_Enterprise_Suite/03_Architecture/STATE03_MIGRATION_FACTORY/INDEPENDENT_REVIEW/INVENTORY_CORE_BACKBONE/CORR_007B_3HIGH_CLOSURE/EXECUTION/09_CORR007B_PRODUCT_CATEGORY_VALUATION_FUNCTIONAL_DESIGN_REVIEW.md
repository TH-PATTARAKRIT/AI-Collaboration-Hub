# CORR-007B — Clean-Room Learning Summary: Product Category Valuation Policy

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Mode: Clean-room remediation / business-semantics learning / no development authorization

## 0. Clean-Room Remediation Notice

This file is the current clean-room learning version of the prior file `09`.

The previous version contained implementation-level excerpts that should not be used for Team B, Team C, or Development handoff. This rewritten version keeps the same learning structure and business conclusions while removing source code, method names, field declarations, file paths, and vendor-specific implementation instructions.

This file is a business-learning artifact only. It is not a Gate PASS and does not authorize Team B, Team C, or Development.

## 1. Purpose

Boss challenged whether inventory valuation policy belongs at the product category level and how that affects standard cost, moving/average cost, FIFO, periodic valuation, perpetual valuation, stock journal, stock valuation, stock variation, and reconciliation.

This document answers that challenge in clean-room language without exposing source implementation.

## 2. Clean-Room Boundary

Allowed in this document:

- business meaning of product category valuation policy;
- decision matrix for SMEsPlus;
- accounting impact at business-rule level;
- risk and open gap classification;
- acceptance criteria for future functional design.

Not allowed in this document:

- source code;
- method names;
- field names;
- class names;
- file paths;
- vendor-specific account-field structure;
- instruction that SMEsPlus must copy the reference system.

## 3. Business Finding: Product Category as Valuation Policy Owner

The business learning is that Product Category can act as the policy owner for inventory valuation behavior. This means products under the same category may share valuation timing, costing method, and related accounting treatment.

For SMEsPlus, this should not be copied mechanically. It should be treated as a design candidate:

| Policy Owner Option | Meaning | Design Risk |
|---|---|---|
| Company-level policy | One default valuation behavior per company. | Simple, but may be too broad for mixed product types. |
| Product Category policy | Products in the same category share valuation behavior. | Good for control, but category governance becomes critical. |
| Product-level policy | Each product can have its own valuation behavior. | Flexible, but high audit and maintenance risk. |
| SMEsPlus-native valuation policy object | A separate controlled policy can be assigned to product groups/categories. | Strong governance, but requires original design and more UX. |

Recommended direction for review: do not assume the reference structure is the target. Decide the SMEsPlus policy owner explicitly.

## 4. Product Inheritance Logic in Business Terms

The clean-room learning is that a product can inherit valuation behavior from a higher-level business grouping, with a fallback default if no category-specific policy exists.

SMEsPlus must decide:

1. Can category override company default?
2. Can product override category?
3. Can a company use different valuation policies for different product categories?
4. Can a category have different policies per company in a multi-company SaaS tenant?
5. What happens when a product moves from one category to another?
6. What happens to historical valuation if the policy changes?

These are Team B functional design questions, not evidence conclusions.

## 5. Manual vs. Automated / Periodic vs. Perpetual

Boss's screenshot language can be understood at business level as two valuation timing patterns:

| Business Label | Clean-Room Meaning | Accounting Impact |
|---|---|---|
| Manual / Periodic | Accounting value is summarized at closing rather than posted for every movement. | Month-end close becomes the main valuation event. |
| Automated / Perpetual | Accounting value is recognized closer to each stock movement. | GL is updated continuously, then reconciled. |

SMEsPlus must define the labels used in its own UI. It does not need to adopt the reference system's wording.

## 6. Cost Method Learning

Valuation timing and cost calculation method are separate concepts.

| Cost Method | Business Meaning | Design Consideration |
|---|---|---|
| Standard cost | Product value uses a controlled fixed cost until changed. | Easy to explain; needs variance handling. |
| Average cost | Product value changes based on accumulated cost history. | Practical for many SMEs; requires clear recalculation and audit rules. |
| FIFO | Product value follows first-in-first-out cost layers. | Strong audit trail; more complex migration and reversal handling. |

SMEsPlus must decide which methods are allowed, by which product group, and whether method changes are locked after transactions exist.

## 7. Inventory Accounts and Accounting Mapping

The clean-room learning is that inventory valuation requires at least the following accounting concepts:

| Accounting Concept | Business Meaning | SMEsPlus Design Requirement |
|---|---|---|
| Stock valuation asset | Balance sheet value of inventory on hand. | Must reconcile to stock quantity/value. |
| Stock variation or COGS-related account | Profit and loss impact from inventory movement or valuation adjustment. | Must align with Thai accounting policy. |
| Price difference / variance | Difference between expected cost and actual purchase cost. | Must be controlled and reportable. |
| Stock journal | Journal used for inventory valuation entries. | Must be explicitly configured and auditable. |
| Income / expense mapping | Category-level or product-level revenue and expense treatment. | Must not be confused with inventory valuation itself. |
| Inbound/outbound clearing concept | Temporary or contra treatment for receipt/delivery timing. | Must be designed in SMEsPlus terms, not copied from reference naming. |

The prior evidence indicates that screenshot terminology and reference-system terminology may not map one-to-one. SMEsPlus should define its own accounting labels and mapping rules.

## 8. Category-Level Valuation Matrix

A clean-room Team B design should produce a matrix at least at this level:

| Category Setting | Movement-Time GL Impact | Close-Time GL Impact | Required Control |
|---|---|---|---|
| Periodic + Standard cost | Usually none or limited during movement. | Closing calculates inventory value and variance. | Strong monthly close checklist. |
| Periodic + Average cost | Movement affects quantity; value is summarized later. | Closing recalculates value by accumulated cost. | Cost recomputation proof and cut-off control. |
| Periodic + FIFO | Movement affects quantity; value is summarized later. | Closing must respect layer order. | Layer integrity and migration proof. |
| Perpetual + Standard cost | Movement can create accounting impact immediately. | Close checks variance and reconciliation. | Variance account and exception control. |
| Perpetual + Average cost | Movement can update accounting value based on average cost. | Close validates remaining differences. | Recalculation and backdate governance. |
| Perpetual + FIFO | Movement can update accounting value using cost layers. | Close validates layer and GL consistency. | Strong reversal/return handling. |

This matrix is not final design. It is the minimum structure Team B must complete before Gate review.

## 9. Multi-Company / SaaS Implications

Because SMEsPlus is SaaS and multi-company, valuation policy must be designed with tenant and company isolation from the beginning.

Required questions:

1. Is Product Category shared across companies?
2. If shared, can each company assign different valuation behavior to the same category?
3. If one company changes valuation method, does it affect another company?
4. How are standard templates protected from tenant customization?
5. How is reporting comparability preserved across companies?
6. Can a tenant customize category valuation policy without breaking canonical reporting?

These questions connect directly to the SaaS invariants and must not be left implicit.

## 10. Screenshot Terminology Risk

Boss's screenshot terms are useful as business prompts, but not as final target labels.

Risk: if Team B copies labels from a reference screen, SMEsPlus may inherit a historical implementation model rather than designing its own control model.

Clean-room handling:

| Screenshot Term Type | Handling |
|---|---|
| Business concept | Keep and translate into SMEsPlus semantics. |
| Vendor UI label | Do not copy automatically. |
| Vendor account structure | Treat as learning input only. |
| Thai accounting requirement | Validate separately with Accounting/Tax. |
| SMEsPlus target label | Create independently and approve through Gate. |

## 11. Open Gaps Preserved

| Gap | Clean-Room Statement | Owner |
|---|---|---|
| Category policy owner | SMEsPlus has not approved whether valuation policy sits at company, category, product, or separate policy object. | Team B / Boss |
| Periodic vs. perpetual support | SMEsPlus has not approved whether one or both modes are supported. | Team B / Accounting |
| Cost method governance | Method change, lock, backdate, and migration rules are not approved. | Team B / Audit |
| Account mapping | Stock valuation, variation, variance, COGS, and clearing treatment need Thai accounting validation. | Accounting/Tax + Team B |
| Multi-company behavior | Category valuation behavior per company/tenant is not yet designed. | IESA / Team B |
| Historical reporting | What happens after policy changes remains undecided. | Team B / Reporting |

## 12. Acceptance Criteria for a Future SMEsPlus Design

A future Team B document must show:

1. approved valuation policy owner;
2. category/company/product override rules;
3. allowed cost methods;
4. allowed valuation timing modes;
5. account mapping matrix;
6. migration opening balance rule;
7. backdate and correction governance;
8. effect on Balance Sheet and Profit and Loss;
9. Thai statutory/accounting validation;
10. clean-room review result before Team C handoff.

## 13. Disposition

`N-A12-01` remains:

`HIGH FUNCTIONAL DESIGN GAP — REOPENED`

This file confirms that the Product Category valuation topic can be learned and discussed safely in clean-room business terms. It does not close the item, does not approve a target design, and does not authorize downstream development.

Boss remains the sole Final Approver.