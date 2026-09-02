# 25 — Multi-Company / Tenant Policy Isolation Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `Layer A evidence gathered (reference ERP official documentation, versions 15.0–19.0, plus explicitly flagged non-official secondary sources). Layer C = CANDIDATE/HOLD only. RISK-U03/GAP-FS-10 explicitly NOT resolved by this file. No Boss decision implied.`

---

## 1. Scope

This file covers Scenarios 25 (internal warehouse transfer, same company) and 26 (inter-company inventory transfer) from the governing prompt §10, and answers the Accounting-side half of Question 15 of the fingerprint register (`01_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` §5): is Costing Method / Inventory Valuation a company-level setting, and can two companies in one database run different costing methods/policies?

**Explicit non-goal, stated up front:** the Inventory-side multi-tenant invariant set — the company-scoping of every concept, and the "cross-company movement = two facts (a sale and a purchase), never one transfer" rule already fixed via `JT-10`/`HX-22` — is **not** re-derived, re-opened, or resolved here. That gap is tracked as `RISK-U03`/`GAP-FS-10` and is Boss-blocking on the Inventory side. This file's job is narrower: what does the reference ERP's own documentation say about how far *Accounting's* costing/valuation policy scope extends across companies in one database, so that the Accounting-side half of the isolation question is evidenced separately from, and does not silently assume alignment with, the still-open Inventory-side gap.

---

## 2. Layer A — Reference ERP Observed Behavior

### 2.1 Financial books are company-scoped by construction

Each company maintains its own chart of accounts; a user can view records and reports across multiple companies at once but can only **work** (post, edit) within a single company's accounting context at a time. Accounts themselves can optionally be marked as shared across companies — documented as useful specifically for consolidation reporting — meaning "shared account" is an opt-in exception to an otherwise per-company chart, not the default.

Evidence: `Reference ERP official documentation — Multi-company, version 19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Chart of accounts, version 18.0, retrieved 2026-09-02`.

### 2.2 Fiscal localization is company-scoped, branches are not independently scoped

Each company can run a different fiscal localization/country package. A **branch**, by contrast, always follows its parent company's localization — the documentation is explicit that an entity operating under a genuinely different country's rules must be modeled as a separate company, not a branch, because branches do not get independent localization scope.

Evidence: `Reference ERP official documentation — Multi-company, version 19.0, retrieved 2026-09-02`.

### 2.3 Products and product data — shared by default, restrictable, with a mixed-sharing exception for Cost

This is the most material finding for the Accounting-side isolation question. The official multi-company documentation states directly:

- Products (and contacts, and equipment) are **shared across companies by default** in a multi-company database. A record's `Company` field, if set, restricts it to one company; left blank, it is visible/usable from every company.
- Critically, sharing is not all-or-nothing at the field level: on a shared product, the **Sales Price and Reference fields are shared**, but the **Cost value is explicitly company-specific**, even while the rest of the product record is shared. The documentation frames this as deliberately allowing different cost structures per company while keeping sales pricing/reference consistent.

Evidence: `Reference ERP official documentation — Multi-company, version 19.0, retrieved 2026-09-02`.

Read together with the Standard Price costing method (file `15`, where Cost is manually defined on the product form and used directly as the valuation basis), this is direct Layer A evidence that **the reference ERP does not treat "one product record" as "one costing input" across companies** — at least one component of cost (the manually-set standard cost) is already built to vary by company even when everything else about the product is shared. This is evidence of a *deliberate, narrow* isolation point inside an otherwise shared record, not evidence of full costing-policy isolation.

### 2.4 Costing Method and Inventory Valuation account routing live on the Product Category, not the company

Per file `15` and file `04`/`11` evidence (Costing Method: Standard/AVCO/FIFO; Stock Input/Output/Valuation accounts) — these fields are configured **on the product category**, and a product inherits from its assigned category unless overridden at the product level for the account fields specifically. Product Category itself is **not** documented, in the official multi-company page fetched for this file, as being company-scoped by default. The official page's blanket statement ("products, contacts, and equipment can be shared or restricted via the Company field") does not explicitly name product categories, and no official documentation page fetched in this research pass confirmed or denied category-level company scoping directly.

**Secondary, non-official evidence (flagged, not cited as Layer A):** forum posts and third-party app/module listings describe a `Company` field being available on the product category form in at least some builds, defaulting to blank (globally shared) unless deliberately set — with at least one third-party marketplace module existing specifically to *add* company-restriction to categories, implying this is not uniformly a built-in behavior across all versions/editions. This is **not** an official-documentation citation and is marked accordingly.

| Claim | Source Type | Fact Status |
|---|---|---|
| Product Category has an optional `Company` field, blank = shared globally | Community forum answers + third-party app listing, not official documentation | `CONFLICTING / HOLD — NOT CONFIRMED IN OFFICIAL DOCUMENTATION FETCHED THIS SESSION` |
| Costing Method and Stock Input/Output/Valuation accounts are configured at the category level | Official documentation (file `04`/`15` evidence base) | `VERIFIED` |
| Whether that category-level configuration is itself company-scoped, shared-by-default, or requires a separate restriction step | Not found in official documentation fetched this session | `HOLD / EVIDENCE REQUIRED` |

**Consequence:** this session can verify, from official documentation, that costing method lives on a shared-by-default kind of record (the category, by analogy to the confirmed product behavior in §2.3) but **cannot** verify from official documentation alone whether the reference ERP enforces category-level company isolation the same way it explicitly does for product Cost. This is recorded as a genuine evidentiary gap, not resolved by inference.

### 2.5 Accounting settings (Valuation Method, Periodic Valuation cadence) are accessed through a company-specific settings context

The Accounting settings screen where Valuation Method and Periodic Valuation cadence are configured (file `03` evidence base) is reached through the standard company-scoped settings architecture described in §2.1 — a user works within one company's accounting context at a time. No official documentation page fetched in this session states in so many words "Valuation Method is a company-dependent field," but this follows directly from the general company-scoping behavior of the Accounting settings screen (§2.1) applied to the specific settings screen documented in file `03`. This is recorded as `CANDIDATE (inference from confirmed general behavior)`, not `VERIFIED (explicit statement)`.

### 2.6 Internal transfer, same company — no accounting event by default

Documentation and forum evidence converge on a specific, useful finding for Scenario 25: by default, the reference ERP does **not** create any accounting journal entry for an internal transfer between locations/warehouses of the same company. The stated reasoning is that valuation is defined to change only when stock enters or leaves the company (purchase, sale, production, scrap) — an internal transfer, by definition, does neither. Creating a journal entry for a same-company internal transfer requires deliberately opting in (either via the standard "force accounting entries" location setting or a dedicated add-on), and is explicitly documented as non-default behavior.

Evidence: `Reference ERP official documentation — Inventory valuation configuration, version saas-16.4, retrieved 2026-09-02` (general valuation-trigger framing); corroborating community/forum evidence on the internal-transfer-specific default (marked secondary, consistent with the no-entry-by-default framing already present in official valuation-trigger documentation).

### 2.7 Inter-company transfer — modeled as two linked, separately-owned financial events

Configuration exists (Companies → Inter-Company settings) to auto-generate a sale order in the supplying company and a purchase order in the receiving company from a single triggering document, with optional auto-validation. Each generated document (sale, purchase, and their respective delivery/receipt and invoice/bill) is a normal, company-scoped financial event in its own company's books — the documentation describes linked documents, not a single cross-company transfer record.

Evidence: general Multi-company documentation (§2.1–2.2) plus corroborating community/forum documentation on the Inter-Company configuration screen's mechanics (marked secondary where it goes beyond the general documentation).

**This corroborates, from the Accounting side, the design already fixed on the Inventory side (`JT-10`/`HX-22`): cross-company movement is two facts — a sale and a purchase — never a single transfer record.** This file treats that alignment as a favorable cross-check, not as new authority to reopen `JT-10`.

---

## 3. Isolation Register — Isolated (Per-Company) vs Shared (Global-Unless-Restricted)

| Concept | Isolation Status per Layer A Evidence | Evidence Basis | Fact Status |
|---|---|---|---|
| Chart of Accounts | Per-company by default; individual accounts can be explicitly marked shared (consolidation use case) | §2.1 | VERIFIED |
| Fiscal localization / statutory package | Per-company; branches inherit parent, cannot diverge | §2.2 | VERIFIED |
| Product master record (name, reference, sales price) | Shared globally by default; restrictable via a `Company` field | §2.3 | VERIFIED |
| Product Cost (standard-price input) | Company-specific even on an otherwise-shared product record | §2.3 | VERIFIED |
| Product Category (parent of Costing Method, Valuation/Input/Output accounts) | Not confirmed either way by official documentation fetched this session; secondary sources suggest a shared-by-default pattern analogous to products, with company-restriction as an opt-in/add-on in at least some builds | §2.4 | HOLD |
| Costing Method (Standard/AVCO/FIFO) | Inherits the Category's isolation status (§2.4) — therefore itself `HOLD` until Category isolation is confirmed | §2.4 | HOLD |
| Stock Input / Output / Valuation accounts | Same inheritance as Costing Method — `HOLD` | §2.4 | HOLD |
| Valuation Method (Perpetual/Periodic) and Periodic Valuation cadence | Company-scoped by inference from the general settings architecture; not an explicit official statement | §2.5 | CANDIDATE |
| Lock Dates | Company-scoped (settings/records screen consistent with §2.1) | §2.1, `23_...` file §2.6 | CANDIDATE (inferred, consistent pattern) |
| Journals | Not directly evidenced in this research pass; presumed company-scoped by the general chart-of-accounts pattern | §2.1 (analogy) | HOLD |
| Same-company internal transfer (Scenario 25) | No accounting event by default; opt-in only | §2.6 | VERIFIED |
| Inter-company transfer (Scenario 26) | Two separate, company-scoped financial events (sale + purchase), linked by configuration, not merged | §2.7 | VERIFIED |

---

## 4. Layer C — Neutral SMEsPlus Candidate Semantics

All entries below are `CANDIDATE` or `HOLD` only.

| Candidate ID | Statement | Status | Depends On |
|---|---|---|---|
| `L25-C01` | If SMEsPlus adopts a category-like (or equivalent) shared valuation-policy concept, its company-scoping must be an explicit, verified design decision — not an assumed default — precisely because the reference ERP's own default-sharing behavior for the analogous concept (product master data, §2.3) is "shared unless restricted," and this session could not confirm from official documentation whether the same default applies to the policy-carrying record (§2.4). | CANDIDATE | `RISK-U03` / `GAP-FS-10` (sharpens, does not resolve) |
| `L25-C02` | A costing-input field that must vary by company even when its parent record is shared (the reference's company-specific Cost field on an otherwise shared product, §2.3) is a useful pattern to evaluate for any SMEsPlus concept where a shared master record co-exists with company-specific financial inputs. | CANDIDATE | `JT-01`, `JT-02` |
| `L25-C03` | The "no accounting event for same-company internal transfer, by default" pattern (§2.6) is a useful default to evaluate for SMEsPlus, but must be reconciled against the Inventory-side rule that every concept is company-scoped and that cross-company movement is always two facts — the same-company case may still need to be a tracked *physical* movement fact even where no financial event fires. | CANDIDATE | Inventory-side company-scoping design (not reopened here) |
| `L25-C04` | The reference's two-fact modeling of inter-company transfer (§2.7) is consistent with, and does not contradict, the already-fixed `JT-10`/`HX-22` design. This is recorded as a cross-check result, not as new evidence authorizing any change to that design. | CANDIDATE (cross-check only) | `JT-10`, `HX-22` |

---

## 5. Explicit Cross-Reference to RISK-U03 / GAP-FS-10

`RISK-U03`/`GAP-FS-10`, as carried into this session, states that the Inventory-side multi-tenant invariant set itself does not yet exist, and that this is Boss-blocking. This file does **not** attempt to construct or complete that invariant set. What this file adds is a narrower, Accounting-side observation that sharpens the risk rather than resolving it: even if/when the Inventory-side multi-tenant invariant set is completed, the reference ERP's own evidence in §2.4 shows that the analogous Accounting-side concept (the policy-carrying category-like record) is, at best, unconfirmed for company isolation and, per the shared-by-default pattern demonstrated for the record it most resembles (§2.3), plausibly shared-by-default unless someone deliberately restricts it. **This means a completed Inventory-side multi-tenant invariant set would not, by itself, guarantee that costing/valuation *policy* is isolated per company on the Accounting side — that is a separate design question this file surfaces but does not answer.** `RISK-U03`/`GAP-FS-10` therefore remains exactly as open as it was entering this session; this file's contribution is evidence that the eventual resolution must explicitly cover the Accounting-side policy-sharing question too, not only the Inventory-side fact/movement scoping question.

---

## 6. Scenario 25 / 26 Evidence Table

| Sub-Case | Reference Evidence | Accounting-Side Observation | SMEsPlus Candidate/HOLD |
|---|---|---|---|
| Scenario 25 — internal transfer, same company, same costing policy | §2.6 — no accounting event by default | No financial recognition question arises because no financial event fires; the physical movement is the only fact in play | `L25-C03`, CANDIDATE |
| Scenario 25 — internal transfer, same company, but source/destination locations carry different Valuation/Input/Output account overrides (product-level or location-level override observed in file `04`/`11`) | Not directly evidenced by an official source in this pass beyond the general override mechanism (file `04`) | If accounting entries are opted into for internal transfers (§2.6), differing account overrides between locations could produce a financial entry even within one company — this was not evidenced in depth here | HOLD — flagged for file `04`/`11`, not resolved here |
| Scenario 26 — inter-company transfer, same costing method both companies | §2.7 — two linked, separately-owned financial events | Each company applies its own costing method to its own leg (sale in Company A, purchase in Company B); no cross-company costing continuity is implied or evidenced | Consistent with `JT-10`; CANDIDATE |
| Scenario 26 — inter-company transfer, **different** costing methods between the two companies | §2.4 (category-level, isolation unconfirmed) + §2.7 (two separate events) | If Category isolation per company is confirmed in a future pass, this case is unremarkable (each company simply applies its own method to its own leg, as in any independent purchase/sale). If Category is *not* isolated per company, a shared category could silently force the same costing method on both companies' legs even though the transfer is modeled as two independent events — a policy-sharing gap masquerading as transaction-level independence | HOLD — this is the sharpest material open item this file surfaces; directly feeds `RISK-U03`/`GAP-FS-10` per §5 |

---

## 7. Open HOLD / Unknown Register (This File)

1. Whether Product Category (or the SMEsPlus equivalent policy-carrying concept) is company-scoped by default in the reference ERP — `HOLD`, not confirmed by official documentation fetched this session; only secondary/non-official sources address it.
2. Whether Journals are company-scoped — `HOLD`, not directly evidenced this session, only inferred by analogy to the confirmed Chart-of-Accounts pattern.
3. Whether Valuation Method / Periodic Valuation cadence is an explicitly company-dependent field or only company-scoped by virtue of the settings screen's general architecture — `CANDIDATE` (inferred), not `VERIFIED`.
4. Whether a shared category between two companies with different intended costing methods would silently force one method onto both companies' inter-company transfer legs in the reference ERP — `HOLD`, would require direct product-testing evidence this session did not gather (documentation-only research per the governing prompt's read-only/deep-research mode).
5. The full Inventory-side multi-tenant invariant set (`RISK-U03`/`GAP-FS-10`) — `HOLD`, explicitly out of this file's scope and not attempted here.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
