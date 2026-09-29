# Source Map (candidate) — `purchase_requisition`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_requisition` |
| Display name | Purchase Agreements |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d8628384f1d6fb59` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_requisition/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase`
- Direct dependents in 300-module list (2): `purchase_requisition_sale`, `purchase_requisition_stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 1, views 12, window actions 3, server actions 0, reports 1, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `purchase.requisition.alternative.warning` (Wizard in case PO still has open alternative requests for quotation); `purchase.requisition.create.alternative` (Wizard to preset values for alternative PO); `purchase.order.group` (Technical model to group PO for call to tenders); `purchase.requisition` (Purchase Requisition); `purchase.requisition.line` (Purchase Requisition Line)
- Objects extended from other modules (8): `purchase.order`, `purchase.order.line`, `product.supplierinfo`, `product.product`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`, `analytic.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `purchase.requisition.create.alternative` ← Community: `purchase_requisition_sale`, `purchase_requisition_stock`; open-license custom/third-party scanned: —
- `purchase.requisition` ← Community: `purchase_requisition_stock`; open-license custom/third-party scanned: —
- `purchase.requisition.line` ← Community: `purchase_requisition_stock`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `purchase.order`, `purchase.order.line`, `product.supplierinfo`, `product.product`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`, `analytic.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `purchase.requisition` → ['draft', 'confirmed', 'done', 'cancel']
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_purchase_alternatives`); record rules 2 (of which company-scoped by text 2); access rows 7

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 44 of 44 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_requisition (Purchase Agreements)
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: depends `purchase` only; no auto_install; description still speaks of "calls for tenders and blanket orders" (purchase_requisition/__manifest__.py:6-14,14). In this revision the agreement object only has two types, Blanket Order and Purchase Template (purchase_requisition/models/purchase_requisition.py:21-23); the "call for tender" function is realised by linking competing RFQs as "Alternatives" on the purchase order (purchase_requisition/models/purchase.py:10-34, 162-234).

## A. Capabilities and how they are switched on
1. Purchase agreements (blanket order / purchase template): CONDITIONAL on installing via the Purchase setting "Purchase Agreements" (purchase/models/res_config_settings.py:18; purchase/views/res_config_settings_views.xml:31-36). Menu under Purchase > Orders (purchase_requisition/views/purchase_requisition_views.xml:218-222; parent purchase/views/purchase_views.xml:11).
2. RFQ created from an agreement ("New Quotation" button, visible only when agreement is Confirmed) (purchase_requisition/views/purchase_requisition_views.xml:38-41; action default `requisition_id` at :12-15).
3. Purchase Alternatives (link RFQs from different vendors, compare, choose): CONDITIONAL on group "Manage Purchase Alternatives" (purchase_requisition/security/purchase_requisition_security.xml:16-18), enabled by setting shown only when agreements are enabled (purchase_requisition/models/res_config_settings.py:9; purchase_requisition/views/res_config_settings_views.xml:11-17). The PO "Alternatives" tab requires that group (purchase_requisition/views/purchase_views.xml:18). Model code itself is not group-gated (purchase_requisition/models/purchase.py:162-189).
4. PDF report "Purchase Agreements" bound to the model (purchase_requisition/report/purchase_requisition_report.xml:3-12; content: vendor, validity, lines with ordered qty, linked orders, purchase_requisition/report/report_purchaserequisition.xml:15-99).
5. Agreement-specific vendor price lines created automatically for blanket orders (see B).

## B. Objects, relationships, lifecycle
- purchase.requisition: name from per-type, per-company sequence BO/PT (purchase_requisition/models/purchase_requisition.py:85-95; purchase_requisition/data/purchase_requisition_data.xml:4-17), vendor, buyer (defaults to current user), start/end date, currency (vendor purchase currency else company currency, :64-70), company, lines, linked purchase orders (:14-45).
- purchase.requisition.line: product, UoM, quantity, unit price, description variants, analytic distribution mixin, ordered quantity (computed), link to vendor price records (:164-182).
- purchase.order gains `requisition_id` ("Agreement"), and a technical group model `purchase.order.group` used to relate alternative POs (purchase_requisition/models/purchase.py:10-34).
- product.supplierinfo gains link to the agreement line (purchase_requisition/models/product.py:10-11).
- State machine (purchase_requisition/models/purchase_requisition.py:34-42): Draft -> Confirmed (`action_confirm`) -> Closed (`action_done`); Draft/Confirmed -> Cancelled (`action_cancel`); Cancelled -> Draft (`action_draft`, no checks, :142-144; button shown only from Cancelled, views :44). Status bar hidden for Purchase Templates and Close button hidden for them (views :43,46).
- Gates on transitions:
  - Confirm: needs at least one line (:131-132); for blanket orders every line needs price > 0 and quantity > 0 (:133-138); on confirm a vendor price record is created per line (:139; created as superuser :253-261). Templates skip those checks.
  - Close: refused while any linked PO is draft/sent/to approve (:150-152); on close vendor price records of the lines are deleted (:153-155).
  - Cancel: deletes the lines' vendor price records and cancels linked POs that are in state draft only; confirmed POs are kept (:118-127; TEST purchase_requisition/tests/test_purchase_requisition.py:856-880).
  - Delete: only draft or cancelled (:158-161).
  - Type or company change only in draft, otherwise error; changing to template clears dates; name is re-issued from the matching sequence (:97-111).
- Line behaviour: on a Confirmed/active blanket order, new lines need price > 0 and a vendor price record is created if none exists for that vendor/product (:216-229; TEST :109-149); price edits are blocked at 0 or below and propagate to vendor price records (:231-241); deleting an active line removes its vendor price record (:243-246). Template line price defaults from vendor price list (by start date, quantity, UoM) else product cost (:206-214; TEST :607-641).
- Ordered quantity = sum of quantities on linked POs in state Purchase for the same product, UoM-converted, shown on the first line of a product only (:184-199; TEST :643-659).
- Purchase order side (purchase_requisition/models/purchase.py): choosing an agreement fills vendor, fiscal position, payment term, company, currency, origin (appended), notes, order date not earlier than agreement start (:36-67); lines are (re)built only while PO is draft; quantity is copied for templates, 0 for blanket orders (:71-93); taxes come from product vendor taxes of the agreement company or its parent companies (:85; TEST :820-854). Vendor is read-only on PO when agreement is a blanket order (purchase_requisition/views/purchase_views.xml:11). Agreement picker limits to Confirmed agreements of same company and same/no vendor (:14).
- Line price for an agreement RFQ comes from the agreement line, converted for UoM, with fallback to standard behaviour for products absent from the agreement (:261-292; TEST :78-107).
- Alternatives: `alternative_po_ids` is the set of POs in the same group; the group deletes itself when it holds one PO or fewer (purchase_requisition/models/purchase.py:16-20, 143-150; TEST :226-262).
  - "Create alternative" wizard: multiple vendors, optional copy of products; creates RFQs copying order date, buyer, delivery address, origin, quantities, UoM, section/note lines, analytic; vendor currency and payment terms come from each vendor; the agreement link is NOT copied (purchase_requisition/wizard/purchase_requisition_create_alternative.py:44,59-100; TEST :322-354).
  - Best-line comparison: per product best total (company currency), best unit price and earliest planned date; cancelled and confirmed lines and zero lines ignored; ties all kept (purchase_requisition/models/purchase.py:191-234; TEST :151-225). Company-currency total = subtotal / order currency rate (:253-259; TEST :356-427).
  - "Choose" zeroes competing quantities of the same product on other RFQs; "Clear" zeroes selected lines not confirmed/cancelled (:294-322; views :61-92).

## C. Validations, automation, security, multi-company
- Constraints: end date not before start date (purchase_requisition/models/purchase_requisition.py:77-83); warning (not block) when vendor already has a confirmed blanket order in the company (:47-62).
- No scheduled action or automatic expiry found: `date_end` is used only for the date constraint and display (grep of models: :25,77-79,108; views :131).
- No code compares ordered quantity to agreed quantity, or checks agreement validity dates when a PO is confirmed (`qty_ordered` informational, :179-199; `date_start` only sets default dates, purchase_requisition/models/purchase.py:64-67, purchase_requisition/models/purchase_requisition.py:268-269).
- Security: rows for Purchase User = full access on agreement, line, both wizards and `purchase.order.group`; Purchase Manager rows are read-only (purchase_requisition/security/ir.model.access.csv:2-8), but Manager implies User (purchase/security/purchase_security.xml:18-22), so effective manager rights are the union (TEST users created with one group each: purchase_requisition/tests/common.py:14-33; a user cancels/resets/copies an agreement, test_purchase_requisition.py:25-32).
- Record rules: agreement and line limited to `company_id in company_ids` (purchase_requisition/security/purchase_requisition_security.xml:4-14). Vendor and buyer fields declare company check (purchase_requisition/models/purchase_requisition.py:20,28).
- Multi-company: sequence chosen by agreement company (TEST :594-605); child-company agreements use parent-company taxes (TEST :820-854).

## D. Approval implications and handoffs
- The agreement itself has no approval step or approver field; confirming/closing/cancelling is available to any Purchase User (ACL above). Approval happens only at the PO: `button_confirm` sends the PO to "To Approve" unless approval is allowed (one-step, amount under the two-step threshold, or user is Purchase Manager) (purchase/models/purchase_order.py:625-639, 1251-1259). Alternatives in "To Approve" still count as open (purchase_requisition/models/purchase.py:96-97).
- Confirming a PO that has open alternatives opens a decision wizard: keep others open, or cancel the other RFQs then confirm (purchase_requisition/models/purchase.py:95-110; purchase_requisition/wizard/purchase_requisition_alternative_warning.py:14-23; TEST :151-225). Cancel of the others follows purchase's rules (locked or billed POs cannot be cancelled, purchase/models/purchase_order.py:641-651).
- Vendor-price handoff to product/purchase: blanket-order vendor prices are visible to price selection only on POs of that same agreement (other POs hide them) (purchase_requisition/models/product.py:17-22).
- Audit: dates and state are tracked (purchase_requisition/models/purchase_requisition.py:24-25,41); chatter note posted on the PO when it is created from/linked to an agreement (purchase_requisition/models/purchase.py:122-142).
- Owned elsewhere: PO lifecycle, receiving and billing (purchase, purchase_stock, account); stock link added by purchase_requisition_stock; service link by purchase_requisition_sale.

## E. Configuration that changes outcomes
- Agreement type (price checks, quantity copy, close button); vendor purchase currency; company sequences; two-step PO approval setting and amount (purchase/models/res_config_settings.py:12-14); group_purchase_alternatives; Purchase warnings group affects wizard messages (purchase_requisition/wizard/purchase_requisition_create_alternative.py:20,29-40).

## F. Effective extension path (module names only)
- Extending purchase.requisition and purchase.requisition.line: purchase_requisition_stock. Extending the create-alternative wizard: purchase_requisition_stock, purchase_requisition_sale. Alternative-warning wizard and `purchase.order.group`: no extenders found.
- Modules referencing `requisition_id`/agreement links: purchase_requisition_stock (procurement flow).
- Depending modules: purchase_requisition_stock, purchase_requisition_sale.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side compare list and many2many alternative widgets (static JS not analysed).
- Grep across the addons root found the group "Manage Purchase Alternatives" referenced only in this module (security definition, setting, PO tab); no other Community group implies it. Assignment beyond the setting: UNKNOWN — EVIDENCE INSUFFICIENT.
- UNKNOWN — EVIDENCE INSUFFICIENT: enforcement of blanket-order validity dates or quantity ceilings outside this module.

