# Source Map (candidate) — `sale_edi_ubl`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_edi_ubl` |
| Display name | Import electronic orders with UBL |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `307cc18d83608aa5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_edi_ubl/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `account_edi_ubl_cii`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_sale_purchase_edi_ubl`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `sale.edi.xml.ubl_bis3` (Sale BIS Ordering 3.5)
- Objects extended from other modules (3): `sale.order`, `product.product`, `account.edi.xml.ubl_bis3`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order`, `product.product`, `account.edi.xml.ubl_bis3`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 34 of 34 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_edi_ubl
Source revision: 19.0.post20260921 | Module: "Import electronic orders with UBL" (sale_edi_ubl/__manifest__.py:2) | depends: sale, account_edi_ubl_cii (:13) | License LGPL-3 (:17)
Basis: static reading of 3 model files; 1 export test (XML comparison) read. Base import/export engines live in account and account_edi_ubl_cii and were only sampled.

## A. Capabilities and optionality
- A1. Import: turns an incoming electronic purchase order (Peppol BIS Ordering 3 XML, or a PDF carrying such XML) into a draft sales order when uploaded to the sales order list. sale_edi_ubl/models/sale_order.py:10-30; sale_edi_ubl/__manifest__.py:5-11; sale/models/sale_order.py:36,1879-1892
- A2. Export: the printed/downloaded sales order PDF gets the same XML attached, for a single order at a time, when at least one EDI builder is registered. sale_edi_ubl/models/sale_order.py:7-8; sale/models/ir_actions_report.py:10-40 (TEST: tests/test_sale_order_edi_gen.py:13-52 - generated XML equals a reference file for a confirmed two-line order with discount and tax)
- A3. Conditional: bridge, installed automatically when sale and account_edi_ubl_cii are present. sale_edi_ubl/__manifest__.py:15
- A4. Product matching is extended to accept a variant-level code or barcode from the extended identifier fields, after the standard identifiers. sale_edi_ubl/models/product_product.py:12-48; sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:392-399
- A5. No menus or settings; no security file; no data files. sale_edi_ubl/__manifest__.py (no data key)

## B. Business objects, relationships, lifecycle
- B1. Sale order (owner sale) is the target document; converter is a stateless service "Sale BIS Ordering 3.5" built on the invoice UBL BIS3 converter (owner account_edi_ubl_cii). sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:10-13
- B2. File type recognition: an XML whose customization id equals the Peppol order transaction identifier is routed to this converter (decoder priority 20). sale_edi_ubl/models/sale_order.py:10-30
- B3. Imported header: customer from the BuyerCustomer party; order reference = document ID; origin = referenced quotation ID; delivery address from the Delivery party; date, payment term and currency from the base converter; note dropped so the sales order's own terms win. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:339-361; account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:355-365
- B4. Imported lines become order lines; invoice-only fields removed, quantity mapped to ordered quantity, per-line discounts removed, document-level allowances/charges added as extra lines placed above normal lines. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:363-377,401-406; sale_edi_ubl/models/sale_order.py:45-59
- B5. After import, for lines with a matched product the unit price and discount are recomputed from the company's own pricing, i.e. incoming prices are not kept for matched products. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:382-390
- B6. Unmatched product: line kept, and a log "Could not retrieve the product named ..." is produced. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:370-371
- B7. Warnings from the import become a to-do activity for the importing user on the order; a chatter note records the format used. sale_edi_ubl/models/sale_order.py:32-43; account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:373-378
- B8. Export content: order number, creation date, order type 220, note, currency, validity end date, customer reference, buyer/seller/delivery parties, payment term name, lines, allowances/charges, tax totals and anticipated totals. Delivery date and location are blanked. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:116-132,150-175,198-204
- B9. Lifecycle: import creates or fills a draft order; nothing in the module confirms it. Confirmation state of the exported order is unrestricted (test confirms first, not required). sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:382-390

## C. Validations, security, multi-company
- C1. No constraints or access rules of its own. (none found in module)
- C2. Export runs with elevated rights (sudo) when attaching XML to the PDF. sale/models/ir_actions_report.py:28
- C3. Tax computation uses the order's company; import partner/payment-term lookup uses the order's company. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:48,347-349
- C4. Multi-company: seller = order company's commercial partner. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:80. Cross-company file routing on import: UNKNOWN — EVIDENCE INSUFFICIENT.
- C5. Negative item prices are made positive (EN16931 rule BR-27 comment) and emptying taxes handled as extra lines on export. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:53-63

## D. Handoffs
- D1. Generic file upload, attachment handling, duplicate/error handling, chatter: account (document import mixin). sale/models/sale_order.py:36; account/models/account_document_import_mixin.py:282-370
- D2. UBL grammar, party/tax/currency helpers, product lookup framework: account_edi_ubl_cii.
- D3. Price and discount recompute after import: sale (order line compute). No accounting posting, inventory or analytic effect here.
- D4. Peppol network transport of orders is not in this module. UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration/defaults that change outcomes
- E1. Export uses order currency (company-currency option is hard set off) and fixed taxes as allowances/charges (hard set on). sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:100-101
- E2. Shipping party choice: order shipping address, else first delivery-type child of the customer, else customer. sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:83-88
- E3. Product identity data (barcode, internal reference, variant codes) decides whether imported lines match products (search priority order 12 and 14 for variant codes). sale_edi_ubl/models/product_product.py:25-28,42-48

## F. Effective extension path (grep of _inherit)
- F1. This module extends: sale.order, product.product; defines sale.edi.xml.ubl_bis3 inheriting account.edi.xml.ubl_bis3. sale_edi_ubl/models/sale_order.py:5; product_product.py:10; sale_edi_xml_ubl_bis3.py:12
- F2. Module depending on sale_edi_ubl: test_sale_purchase_edi_ubl.

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: import behaviour is untested here (only export has a test); deviations for PDF-embedded XML untested.
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: the older export helper `_export_order_vals` (sale_edi_ubl/models/sale_edi_xml_ubl_bis3.py:304-325) calls a super method not found in the base BIS3 file sampled; whether it is still reachable is unknown.
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: who is allowed to use the upload action (access follows sale order create rights; not verified).

