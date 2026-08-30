> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 8 of 10 — Thailand Business Reality & Variation Register
> GOVERNING RULE (stricter than the general evidence rule): "No Primary Evidence = Do Not Declare Thailand
> Requirement." This is a SOURCE-CODE-ONLY observation pass — no user interviews, no Thai Revenue Department
> documentation, no live-system access. Findings are classified using the TBRAC vocabulary and are deliberately
> conservative: source code proves "this customer's build has X," never "Thai businesses require X." AI synthesis
> does not replace real-user validation, per governance §17.

# 11 — THAILAND BUSINESS REALITY AND VARIATION REGISTER

## 00 — TBRAC status vocabulary used below

`Textbook Practice` | `Reference ERP Behaviour` | `Observed Customer Practice` | `Verified Thai Business Reality` |
`Industry Variation` | `Company Variation` | `Unknown / Requires Real-User Validation`

Every entry below defaults to the most conservative applicable classification. **No entry in this register is
classified `Verified Thai Business Reality`** — this research pass has no authoritative external source (Revenue
Department documentation, multi-customer comparison, real-user interview) to elevate any finding beyond what a
single customer's source code proves about itself.

## 01 — Register

| # | Observation | Evidence | TBRAC classification | Sales/Purchase-relevant? |
|---|---|---|---|---|
| 1 | Two independent, uncoordinated modules both implement a Thai "tax branch" concept on `res.partner`: `l10n_th_partner.branch` (plain Char code) and `bm_thai_rd_vat_company_search.office_type` (Selection + live Thai Revenue Department VAT web-service lookup). No evidence either module is aware of the other. | Phase 1 CO-15..24 | **Company Variation** (this build's specific history) — NOT asserted as "Thai businesses need two branch fields" | Indirectly — `res.partner` is the shared Party record Sales/Purchase both consume (Phase 1 §02) |
| 2 | Thai legal-entity name composition: a prefix/suffix wrapping around a company's base name (e.g., a "บริษัท ... จำกัด"-style pattern), implemented across two layered modules (`partner_company_type`, `l10n_th_partner`) using a chained `_compute_name()` override. | Phase 1 PTY-18/19 | **Observed Customer Practice** — a real, working customization; whether this exact prefix/suffix convention is universal to Thai limited companies is plausible but not independently confirmed here | Yes — affects how customer/vendor names render on Sales/Purchase documents |
| 3 | Thai tax-branch identifier (`res_partner.branch`) is consumed downstream by the WHT certificate report (`COALESCE(partner.branch, '')`) — a genuine, in-repo coordination point between two otherwise-separate Thai customization efforts. Only the `l10n_th_partner` branch field is used here; the second branch module's `office_type` is never consulted by WHT reporting. | Phase 8 WHT-12 | **Observed Customer Practice** | Indirectly (Accounting-side; interface-only per governance §19) |
| 4 | A complete Withholding Tax (WHT) subsystem exists — dedicated master model, product-level default rates, payment-time netting, and a legal certificate document using real PND1/PND3/PND3a/PND53 form codes and Section-40 income-type taxonomy. It attaches ONLY to `account.move`/`account.payment`/`product.template` — confirmed by exhaustive grep to have **zero** references to `sale.order` or `purchase.order` anywhere across all 5 WHT modules. | Phase 8 WHT-01..15 | **Observed Customer Practice** for the machinery's existence; **Unknown / Requires Real-User Validation** for whether the specific form codes/rates are current and correct (no authoritative government source cross-checked) | No — architecturally Accounting-internal, interface-only to GROUP A |
| 5 | Thai province/district/sub-district (Amphoe/Tambon) address hierarchy exists as an extension of OCA's standard `res.city`/`res.city.zip` models, with a bundled offline Thai gazetteer instead of a live Geonames call. | Phase 8 ADDR-01..08 | **Observed Customer Practice** | **Unknown / Requires Real-User Validation** whether this reaches delivery/shipping address selection — no code path was found reading these fields outside the address-import wizard itself; the claim "Thai delivery documents need district/sub-district" is explicitly NOT asserted |
| 6 | Two functionally byte-identical Thai "amount in words" modules exist (`l10n_th_amount_to_text`, `convert_amount_text_to_thai`) — same author, same code, only cosmetic description differences. Both delegate to the third-party `num2words` library. | Phase 8 TXT-01..07 | **Company Variation** for the duplication itself (a build-history artifact, not a business-reality claim) | Indirectly — feeds the invoice/bill print layout that Sales/Purchase customers and vendors see, but is reached only from `account.move`, not from `sale.order`/`purchase.order` directly |
| 7 | Whether the printed "amount in words" total is a genuine, universal Thai legal-document requirement | No authoritative source consulted | **Unknown / Requires Real-User Validation** — plausible and consistent with general knowledge of Thai business documents, but not independently confirmed by this research pass | — |
| 8 | Thai Purchase Request urgency levels are captured via a Thai-language Selection field on `purchase.request`. | Phase 4 §05 synthesis (PREQ module SMEsPlus extensions) | **Observed Customer Practice** | Yes — directly on the demand-signal layer upstream of Purchase |
| 9 | Whether Company/Branch (Odoo's native parent-child `res.company` hierarchy, distinct from the Thai tax-branch fields above) maps onto how Thai SMEs actually structure legal entities vs. operating branches | No primary evidence gathered this pass beyond the source-code hierarchy mechanics themselves (Phase 1 CO-01..14) | **Unknown / Requires Real-User Validation** | Yes — both Sale and Purchase call `_accessible_branches()` (Phase 1 CO-27/29) |
| 10 | Tax-inclusive vs. tax-exclusive pricing behavior (`account.tax.price_include`) exists as a company-level default with per-tax override (Phase 1 TAX-04) — common in Thai retail (VAT-inclusive shelf pricing is typical) | Phase 1 TAX-04 (mechanism only) | **Reference ERP Behaviour** (the mechanism is generic Odoo, not Thailand-specific) for the field; **Unknown / Requires Real-User Validation** for whether this build's default matches Thai retail convention — not independently checked | Yes — directly affects Sale/Purchase line pricing |

## 02 — Explicitly NOT investigated in this pass (honest scope boundary, not silence)

- VAT filing/reporting mechanics beyond the WHT-adjacent PND report handler reference (`l10n_th_reports` — named as
  a dependency but its own module was not opened).
- E-tax-invoice / e-receipt government integration (a live, current Thai Revenue Department requirement in
  general) — no module matching this description was searched for in this pass; **Unknown / Requires Real-User
  Validation whether this build has one at all.**
- Any live-system, interview, or transactional-data validation of any finding above.

## 03 — Consolidated governing statement

Every Thai-specific customization found across this entire GROUP A research effort (Phases 1, 4, and 8) shares one
architectural pattern: **each is a thin extension of a shared master-data or Accounting model** (`res.partner`,
`res.company`, `account.tax`, `account.move`, `product.template`), reached from Sales/Purchase only through the
same generic hand-off points already documented in `05_INTEGRATED_E2E_LIFECYCLE_MAP.md` and
`06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` — never by a Thailand-specific fork of `sale.order`, `purchase.order`,
or `stock.picking` themselves. This is reported as a **source-code architecture fact** (high confidence, grep-
verified across three phases), not as a claim about how Thai ERP requirements should be scoped for SMEsPlus —
that determination requires real-user/business validation this research pass does not provide.

**Recurring risk pattern worth carrying to the Fit-Gap pack**: at least three instances of uncoordinated
duplicate/parallel Thai customizations were found in this one customer's build (branch modules #1, amount-to-text
modules #6, and the two-uncoordinated-approaches-to-`default_code` generation noted in Phase 1 for an unrelated
concept) — suggesting a pattern of layered, un-reconciled third-party/community-module adoption over time, which
is itself a migration-planning signal independent of any specific Thai requirement.
