# Source Map (candidate) — `purchase_edi_ubl_bis3`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_edi_ubl_bis3` |
| Display name | Import/Export electronic orders with UBL |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1f421172d0fdb783` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_edi_ubl_bis3/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase`, `account_edi_ubl_cii`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_sale_purchase_edi_ubl`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `purchase.edi.xml.ubl_bis3` (Purchase UBL BIS Ordering 3.5)
- Objects extended from other modules (3): `account.edi.xml.ubl_bis3`, `account.move`, `purchase.order`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.edi.xml.ubl_bis3`, `account.move`, `purchase.order`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_edi_ubl_bis3
Source revision: 19.0.post20260921 (Odoo 19.0 Community, addons root). Pointers are `module/path:LINE`. (TEST) = derived from module tests only.
Manifest: "Import/Export electronic orders with UBL", category Supply Chain/Purchase (purchase_edi_ubl_bis3/__manifest__.py:2,4).

## A. Capabilities
1. Export a purchase order as an electronic order document in the UBL BIS "Ordering 3" format, identified by the customization id `urn:fdc:peppol.eu:poacc:trns:order:3` and profile `urn:fdc:peppol.eu:poacc:bis:ordering:3` (purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:130-135). CORE to this module.
2. Embed that XML inside the PDF of a single printed order/quotation (module description at purchase_edi_ubl_bis3/__manifest__.py:6-8). The embedding step itself is owned by `purchase`, which asks each registered "builder" for an XML and attaches it (purchase/models/ir_actions_report.py:14-48); this module contributes the builder (purchase_edi_ubl_bis3/models/purchase_order.py:7-8). Base list of builders is empty (purchase/models/purchase_order.py:1401-1402).
3. Import a received order XML into a purchase order: file recognised by its customization id (purchase_edi_ubl_bis3/models/purchase_order.py:10-18), decoded with priority 20 (same file :20-30). Import entry in `purchase` is the "create document from attachment" action (purchase/models/purchase_order.py:1404).
4. Restriction on vendor bills: grouping/ungrouping bill lines by tax is refused if any line is linked to a purchase order (purchase_edi_ubl_bis3/models/account_move.py:8-12).
Optional/conditional: the module is `auto_install: True` with dependencies purchase + account_edi_ubl_cii (purchase_edi_ubl_bis3/__manifest__.py:10,12); no setting or group toggles it.

## B. Objects, relationships, lifecycle
- Works on `purchase.order` and its lines; supplier = order partner, buyer ("customer") = the company's commercial partner (purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:93-94).
- Shipping party = order's delivery address, else the company partner's first delivery-type contact, else the company partner (same file :96-101).
- Only product lines are exported; section/note lines are skipped (same file :49).
- Header carries order name as id, creation date as issue date, order type code 105, note, currency, and the vendor reference as a quotation reference (same file :130-143). Payment term name is exported as a note when set (:181-186).
- Order lines: quantity, extension amount, item name/description, price, line discounts as allowances (:240-261, :333-339 discount reason/factor/base are blanked). Vendor-specific product name/code (product supplier info for this partner) override item name and add a seller item id (:81-89, :289-309).
- Tax/allowance totals incl. early-payment-discount allowances/charges (:188-207); monetary totals block (:209-238).
- Import fills: vendor (from SellerSupplier party), vendor reference (document id), origin (originator document reference), delivery address (Delivery party), lines and document-level allowances/charges (:345-383). Lines whose product cannot be found are logged (:375-376); import lines are created at sequence 0 so they sit above existing lines (purchase_edi_ubl_bis3/models/purchase_order.py:44-57).
- Unresolved data produces a "to do" activity for the current user titled "Some information could not be imported" (:32-42).
- No state machine is added here; export/import do not change PO state (UNKNOWN — EVIDENCE INSUFFICIENT for which PO states the user interface allows import in; state gating lives in purchase/account).

## C. Validations, automation, security, multi-company
- Only validation added: the bill-line grouping refusal (purchase_edi_ubl_bis3/models/account_move.py:11-12).
- No ACL file, no record rules, no groups in this module (directory contains only models/tests/i18n). Access follows `purchase` rules; order and line rules are company-scoped (purchase/security/purchase_security.xml:41-49).
- Multi-company: buyer party and currency are read from the order's own company (purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:94,110-112).

## D. Handoffs
- purchase owns the order, PDF rendering and the attachment-import entry (purchase/models/ir_actions_report.py:10-56; purchase/models/purchase_order.py:1401-1404).
- account owns the document-import mixin (decoder/file-type hooks) that PO inherits (account/models/account_document_import_mixin.py:370,476; purchase/models/purchase_order.py:23) and the bill-to-PO reference matching (account/models/account_move.py:5919).
- account_edi_ubl_cii owns the common UBL builder base (`account.edi.xml.ubl_bis3`) that this builder extends (purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:12) and the (un)group-by-tax check (account_edi_ubl_cii/models/account_move.py:201).
- Bill-matching behaviour (TEST): imported vendor-bill XML is matched to a confirmed PO by reference either in the provided field or in line descriptions (purchase_edi_ubl_bis3/tests/test_account_move_import.py:62-81); several candidate references keep only the one that exists (:83-114); bill partner follows the PO partner including invoice-type child contacts (:116-157). These tests exercise account's matching, not code in this module.
- Export fidelity (TEST): generated XML for a confirmed 2-line PO with discount and tax equals a reference file (purchase_edi_ubl_bis3/tests/test_purchase_order_edi_gen.py:13-51).

## E. Configuration that changes outcomes
- Company VAT/partner data and partner delivery children change party/shipping content (purchase_edi_ubl_bis3/models/purchase_edi_xml_ubl_bis3.py:93-101).
- Vendor product info (name/code) changes item naming (:81-89). Payment term presence toggles the payment terms node (:183).
- Flags fixed in code for export: order currency used (not company currency) and fixed taxes exported as allowances/charges (:114-115).

## F. Effective extension path (module names only)
- Extends: purchase.order, account.move, abstract `purchase.edi.xml.ubl_bis3` (inherits `account.edi.xml.ubl_bis3`).
- Other Community modules extending `purchase.edi.xml.ubl_bis3`: none found. Modules depending on it: test_sale_purchase_edi_ubl (test-only). Counterpart on sales side: sale_edi_ubl.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether XML is attached to emailed quotations (only PDF rendering path verified).
- UNKNOWN — EVIDENCE INSUFFICIENT: Peppol network transmission (no sending code in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: user-interface location of the import action.

