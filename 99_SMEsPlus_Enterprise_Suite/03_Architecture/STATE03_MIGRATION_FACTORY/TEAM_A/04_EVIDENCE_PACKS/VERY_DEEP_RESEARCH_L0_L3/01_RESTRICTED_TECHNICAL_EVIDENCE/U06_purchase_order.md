# U06 purchase_order - Restricted Technical Evidence (L2/L3)

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`

- **Unit:** U06 — `purchase_order`
- **Modules owned:** `purchase`, `purchase_requisition`
- **Source revision:** `19.0.post20260921` (Odoo 19 Community, `odoo/addons`)
- **Date:** 2026-10-02
- **Scope rules applied:** source read-only; Community only; DB queried for configuration/structure only (counts, flags, names); no business data recorded; no V-level, coverage %, Gate or Clean-Room statement made.
- **Hand-offs (not studied, recorded only):** `purchase_stock` (receipt creation on approve, received quantity, cancel cascade, receipt type domain) and `purchase_mrp` belong to U07.
- **DISCOVERED SUPPORTING MODULES (read only as far as needed):** `product` (supplierinfo model, `_select_seller`), `analytic` (`_validate_distribution`), `purchase_stock`, `sale_purchase`, `purchase_requisition_stock` (hand-off pointers); also present in DB and extending `purchase.order`: `project_purchase`, `purchase_edi_ubl_bis3`, `purchase_product_matrix`, `purchase_repair`, `mrp_subcontracting_purchase`, `purchase_mrp`, `project_purchase_stock`, `sale_purchase_stock`, `sale_purchase_project`, `purchase_requisition_sale` (not studied).
- **Installed Community modules relevant (DB):** purchase, purchase_requisition, purchase_requisition_stock, purchase_requisition_sale, purchase_stock, purchase_mrp, purchase_product_matrix, purchase_repair, purchase_edi_ubl_bis3, sale_purchase, sale_purchase_stock, sale_purchase_project, project_purchase, project_purchase_stock, mrp_subcontracting_purchase. `account_3way_match` is not present.
- **DB facts used:** 1 company; no purchase orders/lines/agreements/supplier infos; 16 service product templates; company has po_lock=lock, po_double_validation=two_step, amount 5000.
- **Existing Function-ID mapping used:** GRV-F06 (bill control policy part), PDT-F02 and PDT-F03 (PARTIAL only). All else FUNCTION MAPPING REQUIRED.

## Contradictions with brief / prior evidence

- Capability brief lists a `done` state: not present in the `purchase.order` state selection (VDR-U06-C001, VDR-U06-C024); locking is a separate flag (VDR-U06-C003). Prior source-map record `MODULE_purchase.md` already states five states and was found consistent.
- Capability brief says `purchase_requisition` has call-for-tender state machines: in this revision the agreement has types blanket_order / purchase_template and states draft/confirmed/done/cancel (VDR-U06-C235, VDR-U06-C236); tenders are alternatives linked through a technical group model (VDR-U06-C254). Prior record `MODULE_purchase_requisition.md` states the same; no contradiction with it.
- Prior record flagged `rfq` vs `draft` key mismatch in portal as UNKNOWN: confirmed as a source fact (VDR-U06-C025); runtime effect still RT.

## Existing Function-ID mapping decisions

- GRV-F06 (Three-way match / bill control policy): maps to per-product bill control policy only (VDR-U06-C135, VDR-U06-C138, VDR-U06-C139); strict 3-way blocking is Enterprise (VDR-U06-C162).
- PDT-F02 (Per-receipt billing alignment, purchase): PARTIAL (VDR-U06-C166); received quantity belongs to U07.
- PDT-F03 (Bill-before-receipt anomaly): PARTIAL, no anomaly flag found (VDR-U06-C167).
- PDT-F04, GRV-F01..F05, F07, MCT-*: not matched in this unit (receipt/valuation are U07).

## CAP-U06-01 RFQ / PO state machine (draft / sent / to approve / purchase / cancel, plus lock)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing ID covers the order lifecycle itself).

**D1 Business purpose & process semantics.** A purchase document starts as a request for quotation (RFQ, state `draft`), may be sent to the vendor (`sent`), becomes a binding purchase order (`purchase`) after confirmation/approval, and can be cancelled. Locking is a separate flag (`locked`) that freezes a confirmed order when the company policy says so. The capability brief mentions a `done` state: it does NOT exist in this revision VDR-U06-C001 (CONTRA); only residual references remain VDR-U06-C024 VDR-U06-C025.

**D2 Architecture / data / object relationships.** Model `purchase.order` (mixins portal, catalog, mail.thread, activity, document import) holds state VDR-U06-C001, locked VDR-U06-C003, acknowledged VDR-U06-C040, dates VDR-U06-C038, billing status VDR-U06-C037; lines in `purchase.order.line`; tracked fields VDR-U06-C021; chatter subtypes VDR-U06-C020 seeded in data VDR-U06-C039. Integrating Community modules extend the same model: purchase_stock (receipts, U07) VDR-U06-C033 VDR-U06-C034, sale_purchase (origin sale warning) VDR-U06-C035, purchase_requisition (alternatives wizard on confirm) VDR-U06-C043. Calendar helper field VDR-U06-C041.

**D3 Source / technical / workflow logic.**
State diagram (effective behaviour with purchase + purchase_requisition + purchase_stock + sale_purchase installed, as in the DB):
- draft -> sent [message_post with mark_rfq_as_sent, or print_quotation; precondition state == draft] VDR-U06-C004 VDR-U06-C005 VDR-U06-C006
- draft -> to approve / sent -> to approve [button_confirm; not _approval_allowed] VDR-U06-C008
- draft -> purchase / sent -> purchase [button_confirm; _approval_allowed true, via button_approve] VDR-U06-C008 VDR-U06-C009
- to approve -> purchase [button_approve by manager from the form; _approval_allowed true] VDR-U06-C009 VDR-U06-C014
- draft/sent/to approve/purchase -> cancel [button_cancel; not locked, no live bill] VDR-U06-C076 VDR-U06-C077 VDR-U06-C078
- cancel -> draft [button_draft; view only offers it from cancel] VDR-U06-C011 VDR-U06-C012
- (any, purchase) -> locked flag [automatic on approve if company po_lock = lock; button_lock/unlock] VDR-U06-C010 VDR-U06-C016 VDR-U06-C017
- deletion only from cancel VDR-U06-C018
Override chain for transitions: button_confirm = purchase_requisition.button_confirm -> purchase.button_confirm VDR-U06-C043; button_approve = purchase_stock.button_approve -> purchase.button_approve VDR-U06-C033; button_cancel = sale_purchase.button_cancel -> purchase_stock.button_cancel -> purchase.button_cancel VDR-U06-C035 VDR-U06-C034. The Python methods themselves impose no state precondition on approve/draft/cancel VDR-U06-C032.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | Draft -> (send) -> confirm -> approve (or direct) -> purchase; confirmation date stamped VDR-U06-C009; form buttons per state VDR-U06-C013. |
| 2 | Reversal / cancel / negative | cancel / reset-to-draft / delete rules VDR-U06-C076 VDR-U06-C077 VDR-U06-C011 VDR-U06-C018; detailed in CAP-U06-03. |
| 3 | Multi-company / data scope | company rule on orders and lines VDR-U06-C282; see CAP-U06-10. |
| 4 | Side effects & cross-module triggers | picking creation on approve VDR-U06-C033; cancel cascades VDR-U06-C034 VDR-U06-C035; messages with subtype VDR-U06-C020; line additions/qty changes post chatter VDR-U06-C027 VDR-U06-C028. |
| 5 | Configuration & optionality | company po_lock and po_double_validation VDR-U06-C060; send step optional (draft can be confirmed) VDR-U06-C007; lock button only when policy lock VDR-U06-C016. |
| 6 | Validation & constraints | line delete blocked on purchase orders VDR-U06-C026; locked UI read-only VDR-U06-C029 VDR-U06-C030; no server-side lock guard found VDR-U06-C031. |
| 7 | Roles & permissions | Approve button manager-only (view) VDR-U06-C014; Unlock manager-only (view) VDR-U06-C016; Python methods ungated VDR-U06-C017; ACL in CAP-U06-09. |
| 8 | Scheduled / automated | no state-changing cron in these modules; reminder cron only posts mail (CAP-U06-07). |
| 9 | Exception & failure | UserError on delete of non-cancelled order VDR-U06-C018, on line delete VDR-U06-C026; silent skip on non-draft confirm VDR-U06-C007. |
| 10 | Accounting, stock, audit, security & compliance | tracking of state/lock/acknowledged/amount VDR-U06-C021; stock receipts only via purchase_stock (U07) VDR-U06-C033; lock not server-enforced -> compliance risk VDR-U06-C031 VDR-U06-C032. |

**DB reconciliation (config only).** State selection rows in the restored DB match the source: draft, sent, to approve, purchase, cancel VDR-U06-C045. 0 purchase orders exist; all runtime behaviour is source-derived.

**Unknown / Runtime list.** RT: server-side effect of editing a locked order via RPC VDR-U06-C031; RT: programmatic approve/cancel from unusual states VDR-U06-C032; whether the `acknowledge` GET parameter can be triggered by link previews VDR-U06-C023; behaviour of the portal quotation/PO report selection for a draft order VDR-U06-C025; U07: receipt recreation after reset VDR-U06-C089.

## CAP-U06-02 Confirmation and approval (double validation)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Confirming a quotation turns it into a commitment. With two-level approval a manager must approve orders at or above a configurable amount; routine orders under the threshold are committed by ordinary buyers. Confirmation also registers the vendor on the product vendor list so that future orders can reuse the price.

**D2 Architecture / data.** Company fields po_double_validation / po_double_validation_amount / po_lock VDR-U06-C060; settings wizard mapping VDR-U06-C061 VDR-U06-C062; order fields state, date_approve, amount_total VDR-U06-C058; supplierinfo creation VDR-U06-C063 VDR-U06-C064; analytic validation hook VDR-U06-C048 VDR-U06-C049 VDR-U06-C050; agreements alternative wizard VDR-U06-C043 VDR-U06-C072; stock receipts VDR-U06-C069.

**D3 Source / workflow logic.**
button_confirm (purchase_requisition override first, then purchase):
1. skip non-draft/sent orders VDR-U06-C007;
2. `_confirmation_error_message` -> UserError if a product line lacks a product VDR-U06-C046 VDR-U06-C047;
3. `order_line._validate_analytic_distribution()` (effective only if context validate_analytic) VDR-U06-C048 VDR-U06-C049 VDR-U06-C050 VDR-U06-C051;
4. `_add_supplier_to_product()` VDR-U06-C053 VDR-U06-C063 VDR-U06-C064 VDR-U06-C065 VDR-U06-C066 VDR-U06-C067;
5. `_approval_allowed()` -> `button_approve()` else write state `to approve` VDR-U06-C008.
`_approval_allowed`: one_step -> True VDR-U06-C054; two_step -> amount_total strictly below the converted threshold VDR-U06-C055 or user in group_purchase_manager VDR-U06-C057. `button_approve` filters by `_approval_allowed`, silently dropping disallowed orders VDR-U06-C059, writes purchase + date_approve VDR-U06-C009, locks per policy VDR-U06-C010, and (purchase_stock) creates receipts VDR-U06-C033 VDR-U06-C069.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | See D3 steps 1-5 VDR-U06-C046 VDR-U06-C009. |
| 2 | Reversal / cancel / negative | refused with UserError for missing product VDR-U06-C046; unapproved orders wait in `to approve`; cancel/reset in CAP-U06-03. |
| 3 | Multi-company | threshold converted from env.company currency VDR-U06-C055 VDR-U06-C056; supplier info filtered by order company VDR-U06-C095; RT. |
| 4 | Side effects & cross-module | supplier record creation VDR-U06-C063; receipt creation VDR-U06-C069; alternatives wizard VDR-U06-C072; analytic validation VDR-U06-C050; chatter subtype VDR-U06-C020. |
| 5 | Configuration & optionality | one_step default, two_step threshold 5000 VDR-U06-C060; settings visible to purchase managers only VDR-U06-C062; set_values VDR-U06-C061. |
| 6 | Validation & constraints | missing product VDR-U06-C047; analytic 100% rule only with context flag VDR-U06-C050; strict less-than VDR-U06-C055; max 10 sellers VDR-U06-C063. |
| 7 | Roles & permissions | manager override VDR-U06-C057; approve button manager-only in view VDR-U06-C014; Python approve ungated VDR-U06-C074 VDR-U06-C075. |
| 8 | Scheduled / automated | none at confirm time. |
| 9 | Exception & failure | UserError VDR-U06-C046; ValidationError analytic VDR-U06-C050; silent no-op approve VDR-U06-C059; RT: missing rate. |
| 10 | Accounting, stock, audit, security & compliance | amount compared incl. taxes VDR-U06-C058; sudo supplier write VDR-U06-C067; bulk server action bypasses analytic validation VDR-U06-C052; dashboard approval-time metric VDR-U06-C073. |

**DB reconciliation.** Company row: po_lock = lock, po_double_validation = two_step, amount 5000 VDR-U06-C310 VDR-U06-C311; group counts in CAP-U06-09. No orders exist.

**Unknown / Runtime list.** RT: currency threshold across companies VDR-U06-C056; RT: bulk "Confirm RFQ" skipping analytic validation VDR-U06-C052; supplier record side effects at runtime VDR-U06-C124.

## CAP-U06-03 Cancellation, reset to draft, unlock / lock

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Protect financial integrity when an order is withdrawn: locked orders and orders with live vendor bills cannot be cancelled; cancellation is audited and cascades to downstream documents; a cancelled order can be reset to draft; confirmed orders can be frozen (lock) against edits.

**D2 Architecture.** `purchase.order.state`, `locked`, `invoice_ids` VDR-U06-C169; overrides in purchase_stock VDR-U06-C034 VDR-U06-C086 and sale_purchase VDR-U06-C035; agreement cancel VDR-U06-C087; merge VDR-U06-C084; chatter messages on bills VDR-U06-C082 VDR-U06-C083.

**D3 Source / workflow logic.**
- button_cancel (purchase): locked -> UserError VDR-U06-C076; any bill not in draft/cancel -> UserError VDR-U06-C077; write cancel VDR-U06-C078. purchase_stock first cancels non-done pickings/moves VDR-U06-C034; done pickings only get a note VDR-U06-C086; sale_purchase then posts an activity on origin sales orders VDR-U06-C035.
- button_draft: unconditional write draft VDR-U06-C011; offered only from cancel VDR-U06-C012.
- lock/unlock: Python toggles VDR-U06-C017; interface exposure VDR-U06-C016; automatic lock on approve VDR-U06-C010.
State list: cancel -> draft [button_draft] ; draft/sent/to approve/purchase -> cancel [button_cancel, preconditions above]; locked false <-> true [button_lock/unlock; auto-lock on approve].

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | cancel an unlocked, unbilled order -> state cancel VDR-U06-C078. |
| 2 | Reversal / negative | reset to draft VDR-U06-C011; draft bills tolerated VDR-U06-C079; re-confirmation effect on receipts UNKNOWN VDR-U06-C089. |
| 3 | Multi-company | company rule on records VDR-U06-C282; no extra cancel logic by company. |
| 4 | Side effects | pickings/moves cancelled VDR-U06-C034 VDR-U06-C086; sale order activity VDR-U06-C035; refund activity when quantity cut below billed VDR-U06-C088; agreement cancels draft POs VDR-U06-C087. |
| 5 | Configuration | lock policy per company VDR-U06-C060; lock button only under policy VDR-U06-C016. |
| 6 | Validation & constraints | locked or billed -> UserError VDR-U06-C076 VDR-U06-C077; line delete blocked in purchase VDR-U06-C026; price/discount readonly once billed VDR-U06-C080 VDR-U06-C081. |
| 7 | Roles & permissions | Unlock button manager-only in view VDR-U06-C016; Python ungated VDR-U06-C017; bulk list Cancel has no group VDR-U06-C085. |
| 8 | Scheduled | none. |
| 9 | Exception | UserError texts VDR-U06-C076 VDR-U06-C077; cancelled twice is silent VDR-U06-C078. |
| 10 | Accounting, stock, audit | chatter messages VDR-U06-C082 VDR-U06-C083 VDR-U06-C084; tracking VDR-U06-C021; bill linkage persists VDR-U06-C079; lock not server-enforced for edits VDR-U06-C031. |

**DB reconciliation.** Company policy is lock (auto-lock on approve) VDR-U06-C310; no orders or bills present, so cancel/billing paths are source-derived.

**Unknown / Runtime list.** RT: reset-to-draft leaves locked/date_approve VDR-U06-C011; RT: cancelled-order draft bills VDR-U06-C079; UNKNOWN: receipt recreation VDR-U06-C089.

## CAP-U06-04 Vendor pricing and supplier info

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Default price, discount, description, UoM, minimum quantity and lead time on a purchase line from the vendor price list (supplier info), and keep the list populated automatically when a new vendor is first used.

**D2 Architecture.** `product.supplierinfo` (base `product` module) VDR-U06-C103 with company/currency/validity fields; purchase adds company scoping VDR-U06-C095 and currency default VDR-U06-C116; purchase_requisition adds agreement link and visibility filter VDR-U06-C119 VDR-U06-C120. Line-side computed fields selected_seller_id, price_unit, technical_price_unit, date_planned VDR-U06-C091 VDR-U06-C105 VDR-U06-C111.

**D3 Source / logic.** Selection pipeline: `_get_select_sellers_params` VDR-U06-C092 -> `_prepare_sellers` VDR-U06-C093 -> `_get_filtered_supplier` VDR-U06-C094 VDR-U06-C095 -> `_get_filtered_sellers` rules VDR-U06-C096 VDR-U06-C097 VDR-U06-C098 VDR-U06-C099 VDR-U06-C100 -> `_select_seller` ranking VDR-U06-C101 VDR-U06-C102. Price/date/description defaults VDR-U06-C105 VDR-U06-C106 VDR-U06-C107 VDR-U06-C108 VDR-U06-C109 VDR-U06-C110 VDR-U06-C111 VDR-U06-C112 VDR-U06-C123; suggested quantity VDR-U06-C113; allowed UoMs VDR-U06-C114; catalogue VDR-U06-C117 VDR-U06-C118; procurement path VDR-U06-C115; auto-create on confirm (CAP-U06-02) VDR-U06-C063-VDR-U06-C067, VDR-U06-C124.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | vendor + product + qty -> seller selected -> price/discount/date defaults VDR-U06-C091 VDR-U06-C110 VDR-U06-C107. |
| 2 | Reversal / negative | manual price preserved VDR-U06-C105; no seller -> cost fallback VDR-U06-C108 VDR-U06-C109; auto-created seller not removed on cancel. |
| 3 | Multi-company / scope | order company overrides env.company in filter VDR-U06-C095; supplierinfo company default VDR-U06-C103; ranking in env.company currency VDR-U06-C102. |
| 4 | Side effects | supplierinfo auto-create on confirm VDR-U06-C063; blanket orders create/remove supplierinfo VDR-U06-C120. |
| 5 | Configuration | validity dates, min qty, UoM, discount, sequence on the vendor price record VDR-U06-C103; purchase UoM feature VDR-U06-C114. |
| 6 | Validation & constraints | date/qty/UoM/vendor eligibility VDR-U06-C096-VDR-U06-C100; UoM change guard VDR-U06-C204. |
| 7 | Roles & permissions | only managers CRUD supplierinfo VDR-U06-C068; auto-create via sudo VDR-U06-C067. |
| 8 | Scheduled | none (lead time feeds reminder date, CAP-U06-07). |
| 9 | Exception | none raised by selection; no seller -> fallback VDR-U06-C108. |
| 10 | Accounting/stock/audit | price on line drives bill price (CAP-U06-05); lead time -> expected date VDR-U06-C107; hand-off U07 procurement VDR-U06-C115. |

**DB reconciliation.** product_supplierinfo has 0 rows; 16 product templates (all service, purchase_method purchase) VDR-U06-C122.

**Unknown / Runtime list.** RT: selection with real data; RT: multi-company ranking VDR-U06-C102; effect of auto-created min_qty 1 / delay 0 records VDR-U06-C124.

## CAP-U06-05 Vendor bill generation and control

**Function-ID(s):** GRV-F06 (Three-way match / bill control policy) - matches the bill-control policy part only VDR-U06-C135 VDR-U06-C138 VDR-U06-C139; the strict "block payment until received" third leg is absent in Community VDR-U06-C162. PDT-F02 (Per-receipt billing alignment, purchase) - PARTIAL VDR-U06-C166. PDT-F03 (Bill-before-receipt anomaly) - PARTIAL, no anomaly flag found VDR-U06-C167. Remaining sub-capabilities (bill creation, matching screen, auto-complete, EDI/OCR matching) FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Turn confirmed orders into vendor bills, decide how much may be billed (ordered vs received) and keep order/bill links so that billed quantity, billing status and matching screens stay consistent.

**D2 Architecture.** Order fields invoice_ids, invoice_count, invoice_status VDR-U06-C169 VDR-U06-C134; line fields qty_invoiced, qty_received(_method/_manual), qty_to_invoice VDR-U06-C135 VDR-U06-C136 VDR-U06-C141; product purchase_method VDR-U06-C138 VDR-U06-C139 VDR-U06-C140; bill link `account.move.line.purchase_line_id` VDR-U06-C160; match view `purchase.bill.line.match` VDR-U06-C148 VDR-U06-C149; union view VDR-U06-C164; wizard `bill.to.po.wizard` VDR-U06-C153 VDR-U06-C154 VDR-U06-C155.

**D3 Source / logic.** Bill generation: `action_create_invoice` VDR-U06-C125 -> `_prepare_invoice` VDR-U06-C126 VDR-U06-C127 -> section/line loop VDR-U06-C128 VDR-U06-C129 VDR-U06-C130 -> grouping VDR-U06-C131 -> credit-note switch VDR-U06-C132 -> attachment handling VDR-U06-C133. Quantity logic VDR-U06-C135 VDR-U06-C136 VDR-U06-C137. Status VDR-U06-C134. Auto-complete VDR-U06-C144 VDR-U06-C145; matching VDR-U06-C146-VDR-U06-C152; PO from bill lines VDR-U06-C153 VDR-U06-C154 VDR-U06-C155 VDR-U06-C156; EDI/OCR matching VDR-U06-C157 VDR-U06-C158 VDR-U06-C159; hand-off received-qty VDR-U06-C141 VDR-U06-C143 VDR-U06-C168.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | confirm -> receive (or manual qty) -> Create Bill -> post -> status invoiced VDR-U06-C125 VDR-U06-C134 VDR-U06-C135. |
| 2 | Reversal / negative | negative total -> credit note VDR-U06-C132; refund lines subtract VDR-U06-C136; cancel rules VDR-U06-C077. |
| 3 | Multi-company | bills created per company/partner/currency VDR-U06-C131; matching domain by company VDR-U06-C158; see CAP-U06-10. |
| 4 | Side effects | chatter links VDR-U06-C082 VDR-U06-C083; analytic propagation VDR-U06-C161; incoterm VDR-U06-C168; supplier of bill currency/journal VDR-U06-C171. |
| 5 | Configuration & optionality | per-product policy VDR-U06-C138 VDR-U06-C140; 3-way setting is an upgrade option VDR-U06-C162; services default to ordered VDR-U06-C139. |
| 6 | Validation & constraints | single-vendor attachment VDR-U06-C133; matching UserErrors VDR-U06-C150 VDR-U06-C152 VDR-U06-C153; tolerance 0.02 VDR-U06-C157. |
| 7 | Roles & permissions | purchase user CRUD on bills (rule-limited) VDR-U06-C279 VDR-U06-C284; account invoice users read/write PO VDR-U06-C276; policy field edit in manager group VDR-U06-C140. |
| 8 | Scheduled | none; OCR/EDI matching is event-driven VDR-U06-C158. |
| 9 | Exception | zero-quantity bills possible VDR-U06-C165; wizard confirm may leave 'to approve' VDR-U06-C154. |
| 10 | Accounting, stock, audit | draft bills counted as billed VDR-U06-C137; bill-before-receipt allowed under ordered policy VDR-U06-C167; posting entries UNKNOWN VDR-U06-C172; received qty from U07 VDR-U06-C143. |

**DB reconciliation.** 16 service templates with purchase_method purchase VDR-U06-C122; module for 3-way matching not installed (Enterprise) VDR-U06-C162; no bills exist.

**Unknown / Runtime list.** RT: empty bill from non-confirmed order VDR-U06-C165; UNKNOWN accounting on post VDR-U06-C172; U07: received quantity and return handling VDR-U06-C143.

## CAP-U06-06 Line rules and amounts

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Describe what is bought (product lines) and how the document is organised (section/subsection/note), with consistent quantities, units, taxes, discounts, currency and delivery dates.

**D2 Architecture.** `purchase.order.line` (analytic mixin) VDR-U06-C174; amounts via AccountTax engine VDR-U06-C179 VDR-U06-C180 VDR-U06-C181; DB checks VDR-U06-C071 VDR-U06-C175; parent section VDR-U06-C205; order roll-ups VDR-U06-C187 VDR-U06-C206; currency VDR-U06-C192 VDR-U06-C193.

**D3 Source / logic.** Creation VDR-U06-C176 VDR-U06-C177; type immutability VDR-U06-C178; taxes VDR-U06-C182 VDR-U06-C183; discount/UoM VDR-U06-C184 VDR-U06-C185; dates VDR-U06-C187 VDR-U06-C188 VDR-U06-C189 VDR-U06-C106 VDR-U06-C107; analytic default VDR-U06-C190 VDR-U06-C191 VDR-U06-C161; duplicates VDR-U06-C194 VDR-U06-C195 VDR-U06-C196; merge VDR-U06-C197 VDR-U06-C198 VDR-U06-C199 VDR-U06-C200 VDR-U06-C201 VDR-U06-C202; company constraint VDR-U06-C203; UoM change VDR-U06-C204; catalogue VDR-U06-C208.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | add product -> defaults -> amounts computed VDR-U06-C177 VDR-U06-C179. |
| 2 | Reversal / negative | delete lines in draft; blocked after confirm VDR-U06-C026; negative quantity not blocked here VDR-U06-C209. |
| 3 | Multi-company | line company related VDR-U06-C300; tax filter by company VDR-U06-C182; product-company constraint VDR-U06-C203. |
| 4 | Side effects | quantity change posts note VDR-U06-C028; stock moves updated by purchase_stock (U07) VDR-U06-C232. |
| 5 | Configuration | sections/notes/units/analytic optional VDR-U06-C191; rounding via company tax settings VDR-U06-C179. |
| 6 | Validation & constraints | DB checks VDR-U06-C071 VDR-U06-C175; type change VDR-U06-C178; product purchasable VDR-U06-C186. |
| 7 | Roles & permissions | same as order ACL (CAP-U06-09) VDR-U06-C277. |
| 8 | Scheduled | none. |
| 9 | Exception | UserError on type change VDR-U06-C178, merge errors VDR-U06-C197, UoM change VDR-U06-C204. |
| 10 | Accounting/stock/audit | amounts in order currency with stored rate VDR-U06-C180 VDR-U06-C193; report comment mismatch RT VDR-U06-C207. |

**DB reconciliation.** No lines in DB. Analytic applicability selection value added by purchase VDR-U06-C191 (config in DB not separately queried).

**Unknown / Runtime list.** RT: report multi-currency amounts VDR-U06-C207; negative-qty handling VDR-U06-C209.

## CAP-U06-07 Reminders and schedulers

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Ask vendors to confirm delivery before the expected receipt date and track their acknowledgement; notify the buyer when a vendor changes delivery dates.

**D2 Architecture.** ir.cron VDR-U06-C210 -> `purchase.order._send_reminder_mail` VDR-U06-C212 VDR-U06-C213; selection VDR-U06-C215 VDR-U06-C216; settings and groups VDR-U06-C227 VDR-U06-C228; per-partner defaults VDR-U06-C217 VDR-U06-C218 VDR-U06-C219; templates VDR-U06-C223; portal routes VDR-U06-C222 VDR-U06-C225; date-change activity VDR-U06-C224.

**D3 Source / logic.** Cron (daily, user root) -> group check VDR-U06-C212 -> eligible orders VDR-U06-C215 VDR-U06-C216 -> date test VDR-U06-C213 VDR-U06-C214 -> message_post_with_source with reminder template VDR-U06-C213. Manual paths: preview VDR-U06-C220, single-order composer VDR-U06-C221. Vendor side: acknowledge link VDR-U06-C222 VDR-U06-C023, date update route VDR-U06-C225 VDR-U06-C226 -> activity VDR-U06-C224 -> line dates VDR-U06-C232. Dashboard counters VDR-U06-C230.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | reminder N days before expected date VDR-U06-C213; vendor acknowledges VDR-U06-C222. |
| 2 | Reversal / negative | acknowledged orders are excluded VDR-U06-C215 VDR-U06-C234; no decline flow VDR-U06-C233. |
| 3 | Multi-company | partner reminder fields company-dependent VDR-U06-C218 VDR-U06-C217; cron runs in default context; RT. |
| 4 | Side effects | emails/chatter messages VDR-U06-C213; buyer activity on date change VDR-U06-C224; move deadlines VDR-U06-C232. |
| 5 | Configuration | Receipt Reminder group on by default VDR-U06-C227 VDR-U06-C228; per-vendor flag/days VDR-U06-C218 VDR-U06-C219. |
| 6 | Validation | service-only exclusion flawed? VDR-U06-C216; date equality VDR-U06-C214. |
| 7 | Roles | cron user root; routine requires reminder group VDR-U06-C212; portal token access VDR-U06-C287. |
| 8 | Scheduled | cron definition VDR-U06-C210; DB state VDR-U06-C211. |
| 9 | Exception | silent no-op without group/template VDR-U06-C212; portal redirect on bad line id VDR-U06-C226. |
| 10 | Accounting/stock/audit | reminders posted to chatter VDR-U06-C213; no financial effect. |

**DB reconciliation.** Cron `Purchase reminder` active, 1 day, user 1 VDR-U06-C211; ir.default 1 day VDR-U06-C219; group 1 implies reminder group VDR-U06-C229.

**Unknown / Runtime list.** RT: mail delivery; RT: service-only filter VDR-U06-C216; RT: date/timezone edge VDR-U06-C214; RT: portal date update on non-confirmed orders VDR-U06-C226.

## CAP-U06-08 Purchase agreements (purchase_requisition)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Blanket orders fix prices with a vendor for a period; purchase templates are reusable product lists; alternatives (the call-for-tender function in this revision, not a separate state machine VDR-U06-C235) compare competing quotations and let the buyer pick the best.

**D2 Architecture.** `purchase.requisition` (+ line) VDR-U06-C236; `purchase.order.requisition_id` and `purchase.order.group` VDR-U06-C254 VDR-U06-C255; `product.supplierinfo` link VDR-U06-C120; wizards VDR-U06-C072 VDR-U06-C258; settings group VDR-U06-C265 VDR-U06-C268; sequences VDR-U06-C237.

**D3 Source / logic.**
Agreement state diagram:
- draft -> confirmed [action_confirm; needs lines; blanket needs price>0 and qty>0; creates supplierinfo] VDR-U06-C242 VDR-U06-C243
- confirmed -> done [action_done; no draft/sent/to-approve POs; removes supplierinfo] VDR-U06-C244
- draft/confirmed -> cancel [action_cancel; removes supplierinfo, cancels draft POs] VDR-U06-C245 VDR-U06-C087
- cancel -> draft [action_draft; no checks] VDR-U06-C246
Line rules VDR-U06-C248 VDR-U06-C249 VDR-U06-C250; qty_ordered VDR-U06-C251; template price default VDR-U06-C252. PO side: onchange VDR-U06-C253; vendor read-only VDR-U06-C267; price selection filter VDR-U06-C119; line pricing from agreement VDR-U06-C121. Alternatives: group VDR-U06-C254; create VDR-U06-C257 VDR-U06-C258; confirm wizard VDR-U06-C256 VDR-U06-C072; best-line logic VDR-U06-C259 VDR-U06-C260 VDR-U06-C261; merge VDR-U06-C262.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | blanket confirm -> POs from it priced via supplierinfo -> close VDR-U06-C242 VDR-U06-C253 VDR-U06-C244. |
| 2 | Reversal / negative | cancel, reset, delete rules VDR-U06-C245 VDR-U06-C246 VDR-U06-C247. |
| 3 | Multi-company | company on agreement, rules VDR-U06-C264, type/company change guard VDR-U06-C238. |
| 4 | Side effects | supplierinfo create/remove VDR-U06-C243 VDR-U06-C250; PO messages VDR-U06-C257; alternatives cancel VDR-U06-C072. |
| 5 | Configuration | install via settings; alternatives group VDR-U06-C265 VDR-U06-C268; template ignores dates VDR-U06-C238 VDR-U06-C266. |
| 6 | Validation | dates VDR-U06-C239; price/qty VDR-U06-C242; no cap by quantity VDR-U06-C251 VDR-U06-C269. |
| 7 | Roles | purchase user CRUD, manager read rows VDR-U06-C263 VDR-U06-C292; alternatives group gates tab only VDR-U06-C265. |
| 8 | Scheduled | none. |
| 9 | Exception | UserErrors VDR-U06-C238 VDR-U06-C242 VDR-U06-C244 VDR-U06-C248. |
| 10 | Accounting/stock | agreement receipt type via purchase_requisition_stock (U07) VDR-U06-C271; commitment not enforced VDR-U06-C269. |

**DB reconciliation.** Module installed; 0 agreements; alternatives group not enabled; sequences BO/PT VDR-U06-C270.

**Unknown / Runtime list.** RT: quantity/date commitment not enforced VDR-U06-C269; UNKNOWN: supplierinfo date range VDR-U06-C272.

## CAP-U06-09 Roles and security

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 Business purpose.** Provide buyer and purchase-administrator roles, accounting visibility, vendor portal access and company-scoped data.

**D2 Architecture.** Groups VDR-U06-C273 VDR-U06-C274 VDR-U06-C275; ACL csv VDR-U06-C276-VDR-U06-C281 VDR-U06-C263; record rules VDR-U06-C282-VDR-U06-C285 VDR-U06-C264; menu/button groups VDR-U06-C286 VDR-U06-C014 VDR-U06-C016; portal VDR-U06-C287.

**D3 Logic.** ACL grants model-level CRUD per group; record rules add company and portal-partner scoping; view-level groups hide the Approve/Unlock buttons and the policy field; Python methods remain ungated VDR-U06-C295.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | buyer creates/edits; manager approves/unlocks VDR-U06-C276 VDR-U06-C014. |
| 2 | Reversal / negative | access denied for non-internal dashboard VDR-U06-C230; portal redirect VDR-U06-C287. |
| 3 | Multi-company | company rules VDR-U06-C282 VDR-U06-C285 VDR-U06-C264. |
| 4 | Side effects | sudo supplier write VDR-U06-C067; sudo acknowledge in portal VDR-U06-C023. |
| 5 | Configuration | optional groups VDR-U06-C275; reminder default VDR-U06-C227. |
| 6 | Validation | n/a beyond ACL. |
| 7 | Roles & permissions (declared) | VDR-U06-C273-VDR-U06-C285; Python ungated VDR-U06-C295; inherited manager rights VDR-U06-C292. |
| 8 | Scheduled | cron runs as root VDR-U06-C210. |
| 9 | Exception | AccessError redirects VDR-U06-C287. |
| 10 | Security/compliance | broad bill rights for buyers VDR-U06-C294 VDR-U06-C293; control on UI only VDR-U06-C295. |

**DB reconciliation.** ACL rows: purchase 35, purchase_requisition 7 (+2 stock manager); rules: purchase 8, purchase_requisition 2 VDR-U06-C290; groups 75/76/77/78/115 present, manager group has 2 direct members, user group 0 VDR-U06-C291 VDR-U06-C229.

**Unknown / Runtime list.** RT: effective permissions per user; portal sharing links.

## CAP-U06-10 Multi-company / data scope and exception behaviour

**Function-ID(s):** FUNCTION MAPPING REQUIRED. (Related existing ID MCT-F02 inter-company automation: not found in these modules VDR-U06-C305.)

**D1 Purpose.** Keep each company's purchasing data separate, check cross-company references and make failure modes explicit.

**D2 Architecture.** company_id on order, line, agreement VDR-U06-C296 VDR-U06-C300 VDR-U06-C303; global sequence VDR-U06-C298; rules VDR-U06-C282 VDR-U06-C264; picking type domain VDR-U06-C302; supplier filter VDR-U06-C095.

**D3 Logic.** with_company at creation VDR-U06-C297 and billing VDR-U06-C301; product-company constraint VDR-U06-C203 VDR-U06-C307; agreement company sync VDR-U06-C304; approval threshold env.company VDR-U06-C309; error catalogue VDR-U06-C306 VDR-U06-C308 VDR-U06-C133 VDR-U06-C150 VDR-U06-C152 VDR-U06-C238 VDR-U06-C242 VDR-U06-C244 VDR-U06-C248.

**Ten dimensions**

| # | Dimension | Findings |
|---|---|---|
| 1 | Happy path | single-company flow with shared numbering VDR-U06-C298. |
| 2 | Reversal / negative | not applicable beyond CAP-U06-03. |
| 3 | Multi-company | VDR-U06-C296-VDR-U06-C304; RT only. |
| 4 | Side effects | none inter-company in these modules VDR-U06-C305. |
| 5 | Configuration | per-company po_lock / approval VDR-U06-C310. |
| 6 | Validation | VDR-U06-C203 VDR-U06-C307. |
| 7 | Roles | company rules VDR-U06-C282. |
| 8 | Scheduled | cron has no per-company loop in code VDR-U06-C210. |
| 9 | Exception | catalogue VDR-U06-C306 VDR-U06-C308. |
| 10 | Compliance | numbering shared across companies VDR-U06-C298. |

**DB reconciliation.** 1 company VDR-U06-C310; no multi-company evidence; no inter-company modules in installed list.

**Unknown / Runtime list.** RT: all multi-company items VDR-U06-C309 VDR-U06-C056 VDR-U06-C102.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U06-C001 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:105-111 | 'to approve', 'To Approve' | FACT | always | CONTRA | purchase.order.state selection is exactly draft/sent/to approve/purchase/cancel; there is no 'done' state in the base selection (CONTRA: capability brief lists a done state). | N-U06-001 |
| VDR-U06-C002 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:111 | default='draft' | FACT | always | — | state is readonly, indexed, not copied (copy=False), tracked, default draft. | N-U06-010 |
| VDR-U06-C003 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:112-116 | Locked Purchase Orders cannot be modified | FACT | always | — | locked is an independent Boolean (default False, copy=False, tracking=True), not a state value. | N-U06-002 |
| VDR-U06-C004 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:479-483 | mark_rfq_as_sent | FACT | always | — | message_post with context mark_rfq_as_sent writes state draft->sent for draft orders only (filtered state == 'draft'). | N-U06-004 |
| VDR-U06-C005 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:562-573 | 'mark_rfq_as_sent': True | FACT | always | — | action_rfq_send opens the mail composer with mark_rfq_as_sent in context; template is the RFQ template when context send_rfq else the PO template. | N-U06-004 |
| VDR-U06-C006 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:611-613 | print_quotation | FACT | always | — | print_quotation writes draft->sent for draft orders and returns the quotation report action. | N-U06-004 |
| VDR-U06-C007 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:625-628 | not in ['draft', 'sent'] | FACT | always | — | button_confirm iterates orders and 'continue's (silently skips) any order not in draft or sent. | N-U06-005 |
| VDR-U06-C008 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:634-638 | write({'state': 'to approve'}) | FACT | always | — | after checks, button_confirm calls button_approve when _approval_allowed else writes state 'to approve'. | N-U06-006 |
| VDR-U06-C009 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:615-619 | _approval_allowed() | FACT | always | — | button_approve filters self by _approval_allowed(), writes state 'purchase' and date_approve=now; it does not test the current state and ignores the 'force' argument. | N-U06-007 |
| VDR-U06-C010 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:618 | lock_confirmed_po == 'lock' | FACT | company po_lock = lock | — | button_approve sets locked=True on approved orders when the company po_lock is 'lock'. | N-U06-007 |
| VDR-U06-C011 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:621-623 | def button_draft | FACT | always | RT | button_draft writes state 'draft' with no state check and does not reset locked, date_approve or acknowledged; RT: effect on a locked/approved order not exercised. | N-U06-057 |
| VDR-U06-C012 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:142 | button_draft | FACT | always | — | form button Set to Draft is invisible unless state == 'cancel'. | N-U06-012 |
| VDR-U06-C013 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:134-141 | name="button_approve" | FACT | always | — | form header buttons: Send RFQ (draft), Confirm (draft or sent), Approve (to approve), Send PO and Acknowledge (purchase); visibility is state-based. | N-U06-012 |
| VDR-U06-C014 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:136 | groups="purchase.group_purchase_manager" | FACT | always | — | the Approve Order form button carries groups=purchase.group_purchase_manager (interface-only restriction). | N-U06-164 |
| VDR-U06-C015 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:145 | or locked | FACT | always | — | Cancel button visible for draft, to approve, sent, purchase and hidden when locked. | N-U06-012 |
| VDR-U06-C016 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:146-147 | button_unlock | FACT | always | — | Lock button shown only if not locked, state purchase and company policy 'lock'; Unlock shown if locked and restricted to group_purchase_manager. | N-U06-050 |
| VDR-U06-C017 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:651-655 | def button_unlock | FACT | always | — | button_lock/button_unlock simply write locked True/False with no state or group check in Python. | N-U06-056 |
| VDR-U06-C018 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:408-412 | you must cancel it first | FACT | always | — | unlink is guarded by an ondelete hook: UserError unless state == 'cancel'. | N-U06-008 |
| VDR-U06-C019 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:414-422 | line.date_planned = line._get_date_planned | FACT | always | — | copy() drops default_product_id from context and recomputes each copied line's date_planned from its selected seller (lead time). | N-U06-010 |
| VDR-U06-C020 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:529-539 | mt_rfq_approved | FACT | always | — | _track_subtype: purchase from 'to approve' -> mt_rfq_approved; purchase otherwise -> mt_rfq_confirmed; 'to approve' -> mt_rfq_confirmed; 'sent' -> mt_rfq_sent. | N-U06-016 |
| VDR-U06-C021 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:111 | tracking=True | FACT | always | — | tracked fields on the order include state (111), locked (116), acknowledged (120), partner_id (93), user_id (158) and amount_untaxed (137). | N-U06-016 |
| VDR-U06-C022 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:601-602 | def action_acknowledge | FACT | always | — | action_acknowledge sets acknowledged=True with no state, user or group check. | N-U06-009 |
| VDR-U06-C023 | FUNCTION MAPPING REQUIRED | purchase/controllers/portal.py:155-156 | action_acknowledge | FACT | portal route called with acknowledge param | — | GET /my/purchase/<id> with kw acknowledge calls order_sudo.action_acknowledge() (sudo, any state) before rendering. | N-U06-022 |
| VDR-U06-C024 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1032 | ['purchase', 'done'] | FACT | always | CONTRA | retrieve_dashboard still filters states ['purchase','done'] although 'done' is not a state (CONTRA: stale reference; the brief's 'done' state does not exist). | N-U06-021 |
| VDR-U06-C025 | FUNCTION MAPPING REQUIRED | purchase/controllers/portal.py:152 | 'rfq','sent' | FACT | portal report type request | — | portal selects the quotation report when state in ['rfq','sent']; 'rfq' is not a state key (draft is), so a draft order viewed by token would get the PO report. | N-U06-021 |
| VDR-U06-C026 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:342-347 | _unlink_except_purchase | FACT | always | — | line unlink hook: for order state 'purchase' and display_type not section/subsection/note raises UserError 'Cannot delete a purchase order line which is in state'; lock is not consulted. | N-U06-017 |
| VDR-U06-C027 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:313-316 | Extra line with | FACT | always | — | creating a product line on a purchase-state order posts the message 'Extra line with <product>' on the order chatter. | N-U06-052 |
| VDR-U06-C028 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:324-335 | track_po_line_template | FACT | always | — | writing product_qty on a line of a purchase-state order posts a note via template track_po_line_template when the quantity differs. | N-U06-052 |
| VDR-U06-C029 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:246 | readonly="state == 'cancel' or locked" | FACT | always | — | order_line one2many is readonly in the form when state is cancel or locked. | N-U06-018 |
| VDR-U06-C030 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:405-406 | readonly="invoice_status == 'invoiced' or locked" | FACT | always | — | payment_term_id and fiscal_position_id are readonly when fully billed or locked. | N-U06-018 |
| VDR-U06-C031 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:112 | locked = fields.Boolean( | INFERENCE | purchase, purchase_stock, purchase_mrp, purchase_requisition read | RT | grep of 'locked' in purchase/purchase_requisition/purchase_stock/purchase_mrp models finds only purchase_order.py:112,617-618,642-655; no server-side write guard on locked orders was found (only view readonly and cancel check). RT needed to confirm via RPC edit. | N-U06-019 |
| VDR-U06-C032 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:615-617 | self = self.filtered | INFERENCE | always | RT | button_approve/button_cancel/button_draft impose no state precondition in Python (lines 615-649, 621-623); only view conditions gate them. Programmatic misuse possible (e.g. approve a cancelled order); RT to confirm. | N-U06-020 |
| VDR-U06-C033 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:179-181 | _create_picking() | FACT | purchase_stock installed (hand-off U07) | — | purchase_stock overrides button_approve: calls super then self._create_picking() (receipt creation on approval). | N-U06-015 |
| VDR-U06-C034 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:231-235 | return super().button_cancel() | FACT | purchase_stock installed (hand-off U07) | — | purchase_stock.button_cancel cancels non-done pickings and stock moves first (action_cancel) then calls super().button_cancel(), whose UserErrors (locked/billed) abort the transaction. | N-U06-015 |
| VDR-U06-C035 | FUNCTION MAPPING REQUIRED | sale_purchase/models/purchase_order.py:55-57 | _activity_cancel_on_sale | FACT | sale_purchase installed | — | sale_purchase.button_cancel calls super then self.sudo()._activity_cancel_on_sale() scheduling a warning activity on origin sale orders. | N-U06-015 |
| VDR-U06-C036 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1028 | 'to approve' | FACT | always | — | dashboard 'late' counts include states draft, sent and to approve whose date_order is in the past. | N-U06-016 |
| VDR-U06-C037 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:127-131 | Waiting Bills | FACT | always | — | invoice_status selection no / to invoice / invoiced, computed and stored, copy=False. | N-U06-001 |
| VDR-U06-C038 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:88-90 | Order Deadline | FACT | always | — | date_order ('Order Deadline') required, default now, copy=False; date_approve ('Confirmation Date') readonly, copy=False. | N-U06-007 |
| VDR-U06-C039 | FUNCTION MAPPING REQUIRED | purchase/data/purchase_data.xml:5-19 | RFQ Approved | FACT | always | — | three message subtypes seeded for purchase.order: RFQ Confirmed, RFQ Approved, RFQ Sent. | N-U06-016 |
| VDR-U06-C040 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:119-121 | vendor has acknowledged the receipt | FACT | always | — | acknowledged Boolean (copy=False, tracking=True): vendor acknowledgement of the PO. | N-U06-009 |
| VDR-U06-C041 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:206-209 | date_calendar_start | FACT | always | — | date_calendar_start = date_approve when state purchase else date_order (stored calendar helper). | N-U06-001 |
| VDR-U06-C042 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1380-1388 | state == 'cancel' | FACT | always | — | _is_readonly returns True only when state == 'cancel' (used by the product catalogue). | N-U06-018 |
| VDR-U06-C043 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:95-97 | skip_alternative_check | FACT | purchase_requisition installed | — | purchase_requisition.button_confirm returns the alternatives-warning wizard when open alternatives exist and context skip_alternative_check is not set. | N-U06-036 |
| VDR-U06-C044 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:545-556 | email_template_edi_purchase_done | FACT | always | — | RFQ composer template is purchase.email_template_edi_purchase when context send_rfq is truthy, otherwise email_template_edi_purchase_done; lookup failure yields template_id False. | N-U06-004 |
| VDR-U06-C045 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:105-111 | 'cancel', 'Cancelled' | OBSERVATION | restored DB | — | DB: purchase.order state selection rows are draft, sent, to approve, purchase, cancel (ir_model_fields_selection); 0 purchase orders and 0 lines exist. | N-U06-001 |
| VDR-U06-C046 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:625-632 | raise UserError(error_msg) | FACT | always | — | button_confirm calls _confirmation_error_message and raises UserError(error_msg) before any other action. | N-U06-026 |
| VDR-U06-C047 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:657-668 | missing a product | FACT | always | — | _confirmation_error_message: any line with no display_type, not is_downpayment and no product_id -> 'Some order lines are missing a product'. | N-U06-026 |
| VDR-U06-C048 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:632 | _validate_analytic_distribution | FACT | always | — | button_confirm calls order_line._validate_analytic_distribution() for each order. | N-U06-035 |
| VDR-U06-C049 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:745-753 | business_domain='purchase_order' | FACT | analytic installed | — | _validate_analytic_distribution skips display_type lines and calls _validate_distribution(product, business_domain='purchase_order', company). | N-U06-035 |
| VDR-U06-C050 | FUNCTION MAPPING REQUIRED | analytic/models/analytic_mixin.py:182-196 | validate_analytic | FACT | analytic installed | — | _validate_distribution does anything only if context validate_analytic is truthy; then every mandatory plan must sum to 100% else ValidationError 'One or more lines require a 100% analytic distribution.' (DISCOVERED SUPPORTING MODULE: analytic). | N-U06-035 |
| VDR-U06-C051 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:135 | validate_analytic | FACT | always | — | form Confirm buttons (lines 135 and 138) pass context validate_analytic=True. | N-U06-035 |
| VDR-U06-C052 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:921-933 | action_confirm_rfqs | FACT | always | — | server action 'Confirm RFQ' (list/kanban binding, no group restriction) runs records.button_confirm() without the validate_analytic context; list header Cancel has no group either (591-593). | N-U06-040 |
| VDR-U06-C053 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:633 | _add_supplier_to_product | FACT | always | — | button_confirm calls order._add_supplier_to_product() before evaluating approval. | N-U06-031 |
| VDR-U06-C054 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1251-1255 | po_double_validation == 'one_step' | FACT | always | — | _approval_allowed is True if company po_double_validation == 'one_step'. | N-U06-027 |
| VDR-U06-C055 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1256-1259 | amount_total < | FACT | po_double_validation = two_step | — | under two_step, allowed if amount_total < env.company.currency_id._convert(po_double_validation_amount, order currency, order company, date_order or today); strict less-than. | N-U06-028 |
| VDR-U06-C056 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1257-1259 | self.env.company.currency_id._convert | INFERENCE | two_step; multi-company users | RT | the source currency of the threshold is env.company.currency_id (the user's current company), while the amount is stored in the order company's terms; mismatch possible when env.company != order.company. RT in a multi-company setup. | N-U06-039 |
| VDR-U06-C057 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1260 | group_purchase_manager | FACT | always | — | a user in purchase.group_purchase_manager is always allowed to approve (final OR clause). | N-U06-028 |
| VDR-U06-C058 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:40-44 | total_amount_currency | FACT | always | — | amount_total is the tax-engine total_amount_currency (incl. taxes) of non-structure lines, stored; used by the approval comparison. | N-U06-029 |
| VDR-U06-C059 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:615-617 | self.filtered(lambda order: order._approval_allowed()) | FACT | always | — | button_approve silently drops orders for which _approval_allowed() is False (no error, empty return {}). | N-U06-030 |
| VDR-U06-C060 | FUNCTION MAPPING REQUIRED | purchase/models/res_company.py:16-23 | po_double_validation_amount | FACT | always | — | company fields: po_double_validation (one_step default / two_step), po_double_validation_amount Monetary default 5000, po_lock (edit default / lock). | N-U06-034 |
| VDR-U06-C061 | FUNCTION MAPPING REQUIRED | purchase/models/res_config_settings.py:37-44 | po_order_approval | FACT | always | — | settings set_values maps boolean po_order_approval -> two_step/one_step and lock_confirmed_po -> lock/edit on the company. | N-U06-034 |
| VDR-U06-C062 | FUNCTION MAPPING REQUIRED | purchase/views/res_config_settings_views.xml:11-24 | group_purchase_manager | FACT | always | — | the Purchase settings app (approval toggle + minimum amount, lock, warnings, agreements, receipt reminder) is visible only to group_purchase_manager. | N-U06-034 |
| VDR-U06-C063 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:682-691 | len(line.product_id.seller_ids) <= 10 | FACT | always | — | _add_supplier_to_product: partner = parent if the vendor is a contact; adds a seller only if neither partner nor contact already sellers the product and the product has <= 10 sellers. | N-U06-031 |
| VDR-U06-C064 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:670-680 | 'min_qty': 1.0 | FACT | always | — | _prepare_supplier_info: sequence = max existing +1 (or 1), min_qty 1.0, price, currency_id, discount from line, delay 0. | N-U06-031 |
| VDR-U06-C065 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:693-695 | _compute_price(price, default_uom) | FACT | line UoM != template UoM | — | price is converted from the line UoM to the template UoM before creating the seller record. | N-U06-031 |
| VDR-U06-C066 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:700-703 | supplierinfo['product_uom_id'] | FACT | line has a selected_seller_id | — | when the line has a selected seller, product_name, product_code and product_uom_id are copied into the new supplierinfo. | N-U06-031 |
| VDR-U06-C067 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:707-708 | regardless of the user access rights | FACT | always | — | template.sudo().write seller_ids so the supplierinfo is created regardless of the user's rights. | N-U06-032 |
| VDR-U06-C068 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:20 | product_template_purchase_user | FACT | always | — | purchase user has read-only access on product.template; supplierinfo create/write/unlink only for purchase manager (line 31). | N-U06-076 |
| VDR-U06-C069 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:179-181 | def button_approve | FACT | purchase_stock installed (hand-off U07) | — | approval is the hook where purchase_stock creates receipts (hand-off point to U07). | N-U06-036 |
| VDR-U06-C070 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:211-219 | date=(order.date_order or fields.Datetime.now()).date() | FACT | always | — | currency_rate is the company->order currency conversion rate at date_order (stored, precompute). | N-U06-037 |
| VDR-U06-C071 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:105-112 | _accountable_required_fields | FACT | always | — | DB check: a product (accountable) line needs product_id, product_uom_id and date_planned unless is_downpayment. | N-U06-117 |
| VDR-U06-C072 | FUNCTION MAPPING REQUIRED | purchase_requisition/wizard/purchase_requisition_alternative_warning.py:14-23 | skip_alternative_check | FACT | purchase_requisition installed | — | wizard offers keep alternatives (re-run button_confirm with skip_alternative_check) or cancel other draft/sent/to-approve alternatives then confirm. | N-U06-146 |
| VDR-U06-C073 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1050-1051 | po.date_approve - po.create_date | INFERENCE | always | — | approval wait is measured in the dashboard as days_to_order = average(date_approve - create_date) for purchase orders created in the last 3 months (lines 1040-1060). | N-U06-037 |
| VDR-U06-C074 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:615-619 | return {} | FACT | always | — | button_approve returns an empty dict (no UI action) and, unlike button_confirm, neither validates the order nor creates supplier records. | N-U06-038 |
| VDR-U06-C075 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:2 | access_purchase_order, | INFERENCE | always | — | purchase user has write on purchase.order (csv line 2) and button_approve has no group check in Python (lines 615-619); therefore any writer can call approve when _approval_allowed is True (one_step, or under threshold). | N-U06-038 |
| VDR-U06-C076 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:641-644 | You must first unlock them | FACT | always | — | button_cancel raises UserError listing display names of locked orders: 'Unable to cancel purchase order(s) ... You must first unlock them.' | N-U06-045 |
| VDR-U06-C077 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:646-648 | related vendor bills | FACT | always | — | button_cancel raises UserError if any invoice_ids has state not in ('cancel','draft'): 'You must first cancel their related vendor bills.' | N-U06-046 |
| VDR-U06-C078 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:649 | self.write({'state': 'cancel'}) | FACT | always | — | cancel writes state 'cancel' on all selected orders in one write; the method has no current-state precondition. | N-U06-058 |
| VDR-U06-C079 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:178-184 | line.qty_to_invoice = 0 | INFERENCE | order not in state purchase | RT | qty_to_invoice is 0 whenever order state != 'purchase' (178-184), so after cancellation lines show nothing to bill; draft bills (not blocking cancel, c02) stay linked via purchase_line_id and still count in qty_invoiced (line 202). RT to observe. | N-U06-047 |
| VDR-U06-C080 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:422 | line.invoice_lines | FACT | always | — | price/date/name recompute is skipped for lines that already have invoice_lines (continue when line.invoice_lines). | N-U06-051 |
| VDR-U06-C081 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:291-293 | readonly="qty_invoiced != 0" | FACT | always | — | line price_unit (291) and discount (293) are readonly in the form when qty_invoiced != 0. | N-U06-051 |
| VDR-U06-C082 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:171-184 | This vendor bill has been created from | FACT | always | — | account.move.create posts a chatter message with links to source orders when lines carry purchase_line_id and the move is not a reversal. | N-U06-089 |
| VDR-U06-C083 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:186-199 | has been modified from | FACT | always | — | account.move.write posts 'This vendor bill has been modified from: <PO>' when new purchase orders appear among line links. | N-U06-089 |
| VDR-U06-C084 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:892-897 | rfqs.filtered(lambda r: r.state != 'cancel').button_cancel() | FACT | always | — | action_merge posts 'RFQ merged with ...' on survivor and on each merged RFQ and then cancels the merged RFQs via button_cancel. | N-U06-049 |
| VDR-U06-C085 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:591-593 | Are you sure you want to cancel | FACT | always | — | list views carry a header Cancel button (confirmation prompt) with no group restriction; the form Cancel is hidden when locked. | N-U06-045 |
| VDR-U06-C086 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:201 | was cancelled | FACT | purchase_stock installed (hand-off U07) | — | for done pickings purchase_stock only posts the note 'The purchase order ... this receipt is linked to was cancelled.' and leaves them untouched; open pickings and moves are cancelled (231-233, 235). | N-U06-048 |
| VDR-U06-C087 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:118-127 | cancellable_pos.button_cancel() | FACT | purchase_requisition installed | — | agreement action_cancel unlinks lines' supplier info, cancels only linked POs in state draft (button_cancel, so locked/billed rules apply), posts a note, then state 'cancel'. | N-U06-054 |
| VDR-U06-C088 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order_line.py:173-178 | You should ask for a refund | FACT | purchase_stock installed (hand-off U07) | — | when a stock-product line quantity is cut below billed quantity and bill lines exist, an activity on the first bill invites a refund. | N-U06-055 |
| VDR-U06-C089 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | purchase_stock installed | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether receipts/moves cancelled by an earlier cancellation are recreated when the order is reset to draft and confirmed again (U07 hand-off); needs RT or U07 evidence. | N-U06-059 |
| VDR-U06-C090 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1236-1243 | Unsuported anymore | FACT | always | — | get_confirm_url is kept only for backward compatibility; reminder/reception/decline types all return the acknowledge url (no vendor confirm/decline flow). | N-U06-009 |
| VDR-U06-C091 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:272-283 | _select_seller( | FACT | always | — | selected_seller_id = product._select_seller(partner, abs(product_qty), date from order.date_order, uom=line UoM, params) else False; recomputed on product/vendor/qty/date/UoM change. | N-U06-060 |
| VDR-U06-C092 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:768-773 | force_uom | FACT | always | — | _get_select_sellers_params passes order_id and force_uom=True on every line selection. | N-U06-065 |
| VDR-U06-C093 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1019-1021 | _get_filtered_supplier | FACT | always | — | _prepare_sellers = sudo seller_ids filtered by _get_filtered_supplier(env.company, product, params) and sorted by (sequence, -min_qty, price, id). | N-U06-062 |
| VDR-U06-C094 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:118-119 | s.partner_id.sudo().active | FACT | always | — | base filter: company empty or equal, vendor active, and variant empty or equal. | N-U06-062 |
| VDR-U06-C095 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:151-154 | params['order_id'].company_id | FACT | purchase installed | — | purchase overrides _get_filtered_supplier: if params has order_id with a company, that company replaces env.company for the filter. | N-U06-177 |
| VDR-U06-C096 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1037-1040 | seller.date_end < date | FACT | always | — | sellers with date_start > date or date_end < date are skipped (bounds inclusive); date defaults to context today. | N-U06-063 |
| VDR-U06-C097 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1041-1042 | params.get('force_uom') | FACT | force_uom param set (purchase lines) | — | with force_uom a seller whose UoM differs from both the requested UoM and the product UoM is skipped. | N-U06-065 |
| VDR-U06-C098 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1043-1044 | partner_id.parent_id | FACT | partner given | — | only sellers whose partner is the order partner or its parent are considered. | N-U06-066 |
| VDR-U06-C099 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1033-1046 | float_compare(quantity_uom_seller | FACT | quantity not None | — | quantity is converted into the seller UoM and compared with seller.min_qty at Product Unit precision; below min_qty the seller is skipped. | N-U06-064 |
| VDR-U06-C100 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1047-1048 | seller.product_id != self | FACT | always | — | a variant-specific seller applies only to that variant. | N-U06-062 |
| VDR-U06-C101 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1069-1074 | res.partner_id == seller.partner_id | FACT | always | — | _select_seller keeps only eligible sellers of the first partner met (res.partner_id == seller.partner_id), then sorts by discounted price in company currency, sequence, id and returns the first. | N-U06-067 |
| VDR-U06-C102 | FUNCTION MAPPING REQUIRED | product/models/product_product.py:1058-1068 | record.env.company.currency_id | FACT | always | — | ranking price = seller.currency_id._convert(price_discounted -> env.company currency, at date) unrounded; env.company (not order company) is the target. | N-U06-077 |
| VDR-U06-C103 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:51-53 | Lead Time | FACT | always | — | supplierinfo.delay (Lead Time, days) default 1, required; min_qty required default 0; currency_id required; company_id defaults to env.company. | N-U06-060 |
| VDR-U06-C104 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:70-74 | _compute_price(rec.price, product_uom) | FACT | always | — | price_discounted = price converted to product UoM x (1 - discount/100). | N-U06-067 |
| VDR-U06-C105 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:419-423 | line.technical_price_unit != line.price_unit | FACT | always | — | price/date/name recompute (depends on qty, UoM, company, partner) is skipped when there is no product/company, bills exist, skip_uom_conversion is set, or technical_price_unit != price_unit (manual price). | N-U06-070 |
| VDR-U06-C106 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:426-427 | line.selected_seller_id or not line.date_planned | FACT | always | — | date_planned is (re)set to _get_date_planned(selected seller) when a seller is selected or no date exists. | N-U06-069 |
| VDR-U06-C107 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:349-366 | seller.delay if seller else 0 | FACT | always | — | _get_date_planned = order.date_order + seller.delay days (0 without seller); today + delay if no date_order. | N-U06-069 |
| VDR-U06-C108 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:453-477 | standard_price | FACT | no selected seller | — | without a selected seller, discount=0 and price_unit = product standard_price converted by UoM, tax-included fix, and cost currency -> order currency at date_order. | N-U06-068 |
| VDR-U06-C109 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:455-460 | unavailable_seller | FACT | no selected seller | — | if the partner has no applicable seller row and the line already has a price and UoM unchanged, the price is left alone (continue). | N-U06-070 |
| VDR-U06-C110 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:479-483 | line.selected_seller_id.price | FACT | selected seller exists | — | with a seller: price = tax-fixed seller.price converted to order currency at date_order then to the line UoM; discount = seller.discount. | N-U06-068 |
| VDR-U06-C111 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:485-490 | 'technical_price_unit': price_unit | FACT | always | — | _reset_price_unit writes price_unit and technical_price_unit together (the manual-override detection reference). | N-U06-070 |
| VDR-U06-C112 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:309-310 | technical_price_unit | FACT | always | — | create sets technical_price_unit = price_unit when a price is supplied without technical value. | N-U06-070 |
| VDR-U06-C113 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:550-566 | seller_min_qty | FACT | always | — | _suggest_quantity: smallest min_qty among date-valid sellers of the order partner (variant empty/equal); sets quantity (or 1.0) and the seller UoM; otherwise quantity 1.0. | N-U06-071 |
| VDR-U06-C114 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:411-417 | allowed_uom_ids | FACT | always | — | allowed_uom_ids = product UoM / product.uom_ids / UoMs of sellers with matching/empty variant. | N-U06-072 |
| VDR-U06-C115 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:662-690 | date=max(fields.Date.context_today | FACT | procurement path (U07) | — | _prepare_purchase_order_line (procurement/replenishment path) selects seller at date max(order date, today) with force_uom param, converts price/currency and sets discount from seller; used by purchase_stock (hand-off). | N-U06-075 |
| VDR-U06-C116 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:147-149 | property_purchase_currency_id | FACT | always | — | supplierinfo onchange partner: currency = partner.property_purchase_currency_id or env.company currency. | N-U06-110 |
| VDR-U06-C117 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1208-1215 | ordered_by='min_qty' | FACT | always | — | catalogue price/min qty uses _select_seller with quantity None, product UoM and ordered_by min_qty and returns price_discounted converted to order currency. | N-U06-075 |
| VDR-U06-C118 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1329-1336 | pol._reset_price_unit(price) | FACT | always | — | catalogue add-line: if a seller is selected the line price is reset to seller.price (currency converted) and discount to seller.discount. | N-U06-075 |
| VDR-U06-C119 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/product.py:17-22 | purchase_requisition_id | FACT | purchase_requisition installed | — | _prepare_sellers drops sellers tied to an agreement unless it equals params.order_id.requisition_id, so blanket prices apply only on POs of that agreement. | N-U06-074 |
| VDR-U06-C120 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:248-261 | 'purchase_requisition_line_id': self.id | FACT | blanket order with vendor | — | agreement line creates (sudo) a supplierinfo: vendor, variant, UoM, template, price, requisition currency, link to the line. | N-U06-141 |
| VDR-U06-C121 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:261-292 | po_lines_without_requisition | FACT | purchase_requisition installed; PO has agreement | — | for PO lines whose product is on the agreement, price = agreement price converted to line UoM, seller picked with the agreement UoM and date_planned/name set; other lines use the base computation. | N-U06-144 |
| VDR-U06-C122 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:22-29 | product.type == 'service' | OBSERVATION | restored DB | — | DB: product_supplierinfo has 0 rows; product_template has 16 rows, all type service with purchase_method 'purchase'. | N-U06-079 |
| VDR-U06-C123 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:428-451 | default_names | FACT | always | — | line description is reset to the product purchase description (with vendor product name/code) only if empty or equal to a default name; custom descriptions are kept and only the vendor prefix is fixed. | N-U06-069 |
| VDR-U06-C124 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:682-708 | def _add_supplier_to_product | INFERENCE | always | — | auto vendor record on confirm sets min_qty 1.0 and delay 0 (a19) and no date range; later price selection will treat it as an unbounded one-unit-minimum price (consequence derived from a19 and p06/p09). | N-U06-078 |
| VDR-U06-C125 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:760-763 | def action_create_invoice | FACT | always | — | action_create_invoice(attachment_ids) builds invoice vals per order, merges them, creates in_invoice moves and returns the bill action. | N-U06-080 |
| VDR-U06-C126 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:933-944 | 'invoice_origin': self.name | FACT | always | — | _prepare_invoice: move_type from context default_move_type else in_invoice; narration=note, currency, partner, fiscal position, bank, origin=PO name, payment term, company. | N-U06-086 |
| VDR-U06-C127 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:931 | bank_ids.filtered_domain | FACT | always | — | partner_bank_id = first bank of the commercial partner with company empty or equal to the order company. | N-U06-086 |
| VDR-U06-C128 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:774-787 | pending_section | FACT | always | — | section/subsection lines are held as pending and emitted only when a following line exists; every other line (incl. notes) is converted with _prepare_account_move_line. | N-U06-086 |
| VDR-U06-C129 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:628-647 | 'quantity': -self.qty_to_invoice | FACT | always | — | _prepare_account_move_line: quantity = qty_to_invoice (negated for in_refund), discount, taxes, product UoM, purchase_line_id=self.id, is_downpayment. | N-U06-086 |
| VDR-U06-C130 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:640 | _convert(self.price_unit | FACT | always | — | bill line price_unit = PO-currency price converted to the bill currency at the bill date, unrounded. | N-U06-086 |
| VDR-U06-C131 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:792-805 | x.get('currency_id') | FACT | always | — | invoice vals are grouped by (company_id, partner_id, currency_id); lines concatenated; invoice_origin joins distinct origins. | N-U06-087 |
| VDR-U06-C132 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:813-816 | action_switch_move_type | FACT | always | — | after creation, bills whose rounded amount_total < 0 are converted via action_switch_move_type (to refunds). | N-U06-087 |
| VDR-U06-C133 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:823-824 | single vendor at a time | FACT | attachment_ids given | — | with attachments and more than one resulting bill: ValidationError 'You can only upload a bill for a single vendor at a time.' | N-U06-096 |
| VDR-U06-C134 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:46-68 | order.invoice_status = 'to invoice' | FACT | always | — | _get_invoiced: state != purchase -> 'no'; any non-zero line qty_to_invoice (Product Unit precision) -> 'to invoice'; all zero and invoice_ids -> 'invoiced'; else 'no'. | N-U06-085 |
| VDR-U06-C135 | GRV-F06 | purchase/models/purchase_order_line.py:171-184 | purchase_method == 'purchase' | FACT | order state purchase | — | qty_to_invoice = product_qty - qty_invoiced if product purchase_method == 'purchase', else qty_received - qty_invoiced; 0 if order state != purchase. | N-U06-083 |
| VDR-U06-C136 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:197-207 | move_type == 'in_refund' | FACT | always | — | _prepare_qty_invoiced sums bill lines (in_invoice +, in_refund -) converted to the line UoM, for moves not cancelled. | N-U06-084 |
| VDR-U06-C137 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:202 | not in ['cancel'] | INFERENCE | always | — | the filter excludes only cancelled moves (or payment_state invoicing_legacy), therefore draft bills also count as billed quantity. | N-U06-084 |
| VDR-U06-C138 | GRV-F06 | purchase/models/product.py:13-18 | On received quantities | FACT | always | — | product.template.purchase_method selection: 'purchase' (On ordered quantities) / 'receive' (On received quantities); stored computed, editable. | N-U06-082 |
| VDR-U06-C139 | GRV-F06 | purchase/models/product.py:22-29 | default_purchase_method | FACT | always | — | _compute_purchase_method: service -> 'purchase'; otherwise the field default_get value falling back to 'receive'. | N-U06-082 |
| VDR-U06-C140 | FUNCTION MAPPING REQUIRED | purchase/views/product_views.xml:66-69 | purchase_method | FACT | always | — | the purchase_method radio sits in the product form 'bill' group, which is restricted to group_purchase_manager. | N-U06-094 |
| VDR-U06-C141 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:225-238 | line.qty_received_method = 'manual' | FACT | purchase without purchase_stock | — | base received-qty method: consu/service -> 'manual' (qty_received_manual), else False; _prepare_qty_received returns the manual value for manual lines. | N-U06-088 |
| VDR-U06-C142 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:260-270 | qty_received_manual | FACT | always | — | writing qty_received stores qty_received_manual when the method is manual, else resets it to 0. | N-U06-088 |
| VDR-U06-C143 | GRV-F06 | purchase_stock/models/purchase_order_line.py:37-41 | line.qty_received_method = 'stock_moves' | FACT | purchase_stock installed (hand-off U07) | — | with purchase_stock consumable products switch to qty_received_method 'stock_moves' (received quantity from done moves and returns; U07 owns the computation). | N-U06-088 |
| VDR-U06-C144 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:54-61 | _prepare_invoice() | FACT | always | — | bill form auto-complete from a PO copies _prepare_invoice values except company and (if equal) move_type, keeps existing currency when lines exist. | N-U06-080 |
| VDR-U06-C145 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:63-65 | po_lines = self.purchase_id.order_line | FACT | always | — | auto-complete adds all PO lines not already linked to the bill via _add_purchase_order_lines (quantity = qty_to_invoice, which may be 0). | N-U06-080 |
| VDR-U06-C146 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:102-108 | is_purchase_matched | FACT | always | — | is_purchase_matched is False if any product bill line has no purchase_line_id; used as matching indicator. | N-U06-080 |
| VDR-U06-C147 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:143-156 | Purchase Matching | FACT | always | — | action_purchase_matching opens the match view for the bill's vendor (and commercial partner) and company scope. | N-U06-080 |
| VDR-U06-C148 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:83-105 | pol.product_qty > pol.qty_invoiced | FACT | always | — | match view PO side: purchase-state order lines with product_qty > qty_invoiced or qty_to_invoice != 0, plus down-payment lines already invoiced. | N-U06-080 |
| VDR-U06-C149 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:107-131 | aml.purchase_line_id IS NULL | FACT | always | — | match view bill side: draft/posted vendor bill product lines with no purchase_line_id. | N-U06-080 |
| VDR-U06-C150 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:163-165 | at least one Purchase Order line | FACT | always | — | action_match_lines raises UserError unless at least one PO line is selected; PO lines alone create a draft bill (146-161). | N-U06-097 |
| VDR-U06-C151 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:174-192 | zip(po_lines, matching_bill_lines) | FACT | always | — | matching pairs PO and bill lines by product (zip order), re-links extra bill lines to the last PO line, deletes unmatched selected bill lines and adds leftover PO lines to the single residual bill. | N-U06-080 |
| VDR-U06-C152 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:206-214 | same vendor | FACT | always | — | action_add_to_po raises UserError for bill lines of different commercial partners (206-207) or of several POs (213-214), or when no bill lines are selected (203-204). | N-U06-097 |
| VDR-U06-C153 | FUNCTION MAPPING REQUIRED | purchase/wizard/bill_to_po_wizard.py:16-17 | Are these Down Payments | FACT | always | — | wizard action_add_to_po raises UserError 'There are no products to add...' when selected bill lines carry no product. | N-U06-097 |
| VDR-U06-C154 | FUNCTION MAPPING REQUIRED | purchase/wizard/bill_to_po_wizard.py:19-35 | button_confirm() | FACT | always | — | wizard creates (or extends) the PO from bill lines, calls button_confirm() immediately and links each bill line to its new PO line (zip by product). | N-U06-100 |
| VDR-U06-C155 | FUNCTION MAPPING REQUIRED | purchase/wizard/bill_to_po_wizard.py:43-62 | 'is_downpayment': True | FACT | always | — | down-payment conversion creates PO lines with product_qty 0, is_downpayment True, price converted to PO currency; bill lines link to them. | N-U06-090 |
| VDR-U06-C156 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:724-745 | Down Payments | FACT | always | — | _create_downpayments creates a 'Down Payments' section line once and appends lines after it. | N-U06-090 |
| VDR-U06-C157 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:13 | TOLERANCE = 0.02 | FACT | always | — | total tolerance for matching an incoming bill to a PO is 0.02. | N-U06-091 |
| VDR-U06-C158 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:370-390 | common_domain | FACT | always | — | matching candidates: same company, state 'purchase', invoice_status in ('to invoice','no'); by order name, then partner_ref; total match within tolerance, then OCR subset or EDI per-line matching. | N-U06-091 |
| VDR-U06-C159 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:434-448 | no_match | FACT | always | — | last resort: single PO by vendor (child_of) and total within tolerance, else 'no_match'. | N-U06-091 |
| VDR-U06-C160 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:528 | ondelete='set null' | FACT | always | — | account.move.line.purchase_line_id: Many2one to PO line, ondelete set null, copy=False; purchase_order_id related. | N-U06-080 |
| VDR-U06-C161 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:549-554 | _related_analytic_distribution | FACT | always | — | bill line analytic distribution is merged with the linked PO line's distribution. | N-U06-109 |
| VDR-U06-C162 | GRV-F06 | purchase/views/res_config_settings_views.xml:42-44 | 3-way matching | INFERENCE | Community tree | — | the 3-way matching option is module_account_3way_match with widget upgrade_boolean (module absent from the Community addons tree: ls found no account_3way_match); Community only offers the bill-control policy and the matching screens. | N-U06-093 |
| VDR-U06-C163 | FUNCTION MAPPING REQUIRED | purchase/report/purchase_report.py:91-94 | qty_to_be_billed | FACT | always | — | report qty_to_be_billed replicates the policy: ordered minus billed if purchase_method == 'purchase', else received minus billed. | N-U06-083 |
| VDR-U06-C164 | FUNCTION MAPPING REQUIRED | purchase/report/purchase_bill.py:33-43 | invoice_status in ('to invoice', 'no') | FACT | always | — | purchase.bill.union lists posted bills plus purchase-state orders with invoice_status in ('to invoice','no') for auto-complete. | N-U06-080 |
| VDR-U06-C165 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:760-833 | def action_create_invoice | INFERENCE | always | RT | no state or 'nothing to bill' check exists inside action_create_invoice (only attachment check); for non-purchase orders qty_to_invoice=0 so zero-quantity lines/bills can result. RT to confirm. | N-U06-099 |
| VDR-U06-C166 | PDT-F02 | purchase/models/purchase_order_line.py:182 | line.qty_received - line.qty_invoiced | INFERENCE | purchase_method = receive | — | PARTIAL fit to PDT-F02: under the receive policy billable quantity follows qty_received so each receipt raises the billable amount; receipt-quantity source is U07. | N-U06-095 |
| VDR-U06-C167 | PDT-F03 | purchase/models/purchase_order_line.py:180 | line.product_qty - line.qty_invoiced | INFERENCE | purchase_method = purchase | — | PARTIAL fit to PDT-F03: under the ordered policy qty_to_invoice does not depend on receipt, so a bill before receipt is allowed and no warning for it was found in the purchase files read. | N-U06-098 |
| VDR-U06-C168 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:289-291 | invoice_incoterm_id | FACT | purchase_stock installed (hand-off U07) | — | purchase_stock._prepare_invoice adds invoice_incoterm_id from the PO incoterm. | N-U06-095 |
| VDR-U06-C169 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:70-75 | order_line.invoice_lines.move_id | FACT | always | — | invoice_ids/invoice_count are stored computeds from order_line.invoice_lines.move_id. | N-U06-080 |
| VDR-U06-C170 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:947-974 | account.action_move_in_invoice_type | FACT | always | — | action_view_invoice shows the vendor-bill action: form for one bill, list for several, closes if none. | N-U06-080 |
| VDR-U06-C171 | FUNCTION MAPPING REQUIRED | purchase/models/account_invoice.py:77-100 | property_purchase_currency_id | FACT | always | — | bill partner onchange sets currency from the vendor's purchase currency and, if none chosen via context, picks a purchase journal in that currency. | N-U06-080 |
| VDR-U06-C172 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | stock_account/account posting | RT | UNKNOWN - EVIDENCE INSUFFICIENT: accounting entries and price-difference treatment when a bill linked to a PO line is posted (belongs to account/stock_account and U07). | N-U06-101 |
| VDR-U06-C173 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_bill_line_match.py:146-161 | 'move_type': 'in_invoice' | FACT | always | — | _action_create_bill_from_po_lines creates a draft vendor bill (currency: lines' currency, else company currency) and adds the PO lines. | N-U06-080 |
| VDR-U06-C174 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:98-101 | line_subsection | FACT | always | — | display_type selection: line_section, line_subsection, line_note (False for product lines). | N-U06-102 |
| VDR-U06-C175 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:109-112 | _non_accountable_null_fields | FACT | always | — | DB check: display_type lines must have no product, price_unit 0, product_uom_qty 0, no UoM and no date_planned. | N-U06-104 |
| VDR-U06-C176 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:305-308 | values.update(product_id=False | FACT | always | — | create forces product/price/qty/UoM/date empty for display_type lines; other lines get missing fields via _prepare_add_missing_fields. | N-U06-104 |
| VDR-U06-C177 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:649-660 | _prepare_add_missing_fields | FACT | order and product given | — | missing name/price/qty/UoM/taxes/date_planned are derived through onchange_product_id when only product and order are supplied. | N-U06-104 |
| VDR-U06-C178 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:321-322 | You cannot change the type of a purchase order line | FACT | always | — | write raises UserError if display_type is being changed. | N-U06-105 |
| VDR-U06-C179 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:123-133 | total_excluded_currency | FACT | always | — | price_subtotal/price_total/price_tax are computed by AccountTax base-line engine from tax_ids, quantity, price and rounding (stored). | N-U06-106 |
| VDR-U06-C180 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:135-151 | rate=self.order_id.currency_rate | FACT | always | — | base line uses order currency (or company currency), rate = order.currency_rate, partner and company of the order. | N-U06-106 |
| VDR-U06-C181 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:30-35 | not x.display_type | FACT | always | — | order totals are computed from non-display_type lines only via the tax totals summary. | N-U06-106 |
| VDR-U06-C182 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:153-159 | _filter_taxes_by_company | FACT | always | — | _compute_tax_id = product.supplier_taxes_id filtered by line company then mapped by the order fiscal position (or default fiscal position). | N-U06-107 |
| VDR-U06-C183 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:468-473 | _compute_tax_id | FACT | always | — | changing fiscal_position_id or company triggers order_line._compute_tax_id(). | N-U06-107 |
| VDR-U06-C184 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:161-164 | price_unit_discounted | FACT | always | — | price_unit_discounted = price_unit x (1 - discount/100). | N-U06-106 |
| VDR-U06-C185 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:499-505 | product_uom_qty | FACT | always | — | product_uom_qty (stored) = product_qty converted into the product UoM. | N-U06-102 |
| VDR-U06-C186 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:44 | purchase_ok | FACT | always | — | line product domain requires purchase_ok; ondelete restrict on product and UoM. | N-U06-117 |
| VDR-U06-C187 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:226-234 | min(dates_list) | FACT | always | — | PO.date_planned (stored, editable) = earliest date_planned of non-display lines (False if none). | N-U06-108 |
| VDR-U06-C188 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:362-365 | onchange_date_planned | FACT | always | — | onchange of order date_planned pushes the date to all non-display lines. | N-U06-108 |
| VDR-U06-C189 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:428-438 | _must_delete_date_planned | FACT | always | — | onchange override removes date_planned updates from line commands when the change came from order_line, preventing feedback overwrite. | N-U06-108 |
| VDR-U06-C190 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:368-379 | _get_distribution | FACT | analytic installed | — | analytic_distribution default from distribution model by product, category, partner, partner category, company; recomputed on product/partner change. | N-U06-109 |
| VDR-U06-C191 | FUNCTION MAPPING REQUIRED | purchase/models/analytic_applicability.py:10-15 | 'purchase_order' | FACT | analytic installed | — | purchase adds business_domain 'purchase_order' to analytic plan applicability (cascade on uninstall). | N-U06-114 |
| VDR-U06-C192 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:459-466 | property_purchase_currency_id | FACT | always | — | order currency (precomputed, editable) = vendor property_purchase_currency_id else company currency (with order company context). | N-U06-110 |
| VDR-U06-C193 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:211-219 | _get_conversion_rate | FACT | always | — | currency_rate from company currency to order currency at order date, stored. | N-U06-110 |
| VDR-U06-C194 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:313-318 | draft_orders | FACT | always | — | duplicated_order_ids is computed only for state draft orders; others get False. | N-U06-111 |
| VDR-U06-C195 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:332-348 | duplicate_po.state != 'cancel' | FACT | always | — | duplicates = same company and vendor, other id, not cancelled, and (order.origin = other.name or equal partner_ref); orders without partner_ref are skipped. | N-U06-111 |
| VDR-U06-C196 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:155 | duplicated_order_ids | FACT | always | — | form shows a warning banner for draft orders with duplicates; nothing blocks confirmation. | N-U06-118 |
| VDR-U06-C197 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:838-852 | state in ['draft', 'sent'] | FACT | always | — | action_merge: only draft/sent RFQs; fewer than two -> UserError; groups by _prepare_grouped_data; no group with 2+ -> UserError. | N-U06-112 |
| VDR-U06-C198 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:863-879 | <= 86400 | FACT | always | — | RFQs merge into the oldest by date_order; lines with same product, UoM, analytic distribution, discount and date_planned within 24h are summed; others moved. | N-U06-112 |
| VDR-U06-C199 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:764-766 | min(self.price_unit, rfq_line.price_unit) | FACT | always | — | _merge_po_line adds quantities and keeps the lower price_unit. | N-U06-112 |
| VDR-U06-C200 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:922-923 | rfq.dest_address_id.id | FACT | always | — | merge key = (partner, currency, dropship address); purchase_requisition adds agreement; purchase_stock adds receipt type. | N-U06-112 |
| VDR-U06-C201 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:236-238 | rfq.requisition_id.id | FACT | purchase_requisition installed | — | agreements module extends the merge key with requisition_id. | N-U06-112 |
| VDR-U06-C202 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:184-186 | rfq.picking_type_id.id | FACT | purchase_stock installed (hand-off U07) | — | inventory integration extends the merge key with picking_type_id. | N-U06-112 |
| VDR-U06-C203 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:184-199 | _check_order_line_company_id | FACT | always | — | constraint on company_id/order_line: products of a company not in the order company's accessible branches raise ValidationError naming company and products. | N-U06-116 |
| VDR-U06-C204 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:117-132 | change of unit of measure can not be done | FACT | always | — | _update_uom raises UserError if a PO line uses a UoM other than the product's current UoM, else rewrites lines' product_uom_id. | N-U06-113 |
| VDR-U06-C205 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:525-544 | last_sub | FACT | always | — | _compute_parent_id links lines to the preceding subsection or section. | N-U06-102 |
| VDR-U06-C206 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:137-141 | amount_untaxed | FACT | always | — | amount_untaxed, amount_tax, amount_total, amount_total_cc are stored, readonly computeds (amount_untaxed tracked). | N-U06-106 |
| VDR-U06-C207 | FUNCTION MAPPING REQUIRED | purchase/report/purchase_report.py:6 | not multi-currency | INFERENCE | always | RT | file comment says reports are not multi-currency while the query joins a currency table (line 112) and divides by po.currency_rate (line 81); header comment possibly stale. RT in a multi-currency DB. | N-U06-119 |
| VDR-U06-C208 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1316-1321 | pol.unlink() | FACT | catalogue panel | — | catalogue quantity 0 deletes the line on draft/sent orders but only sets product_qty 0 on other states. | N-U06-102 |
| VDR-U06-C209 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:23 | digits='Product Unit' | INFERENCE | always | — | product_qty is required with Product Unit precision; no sign constraint is declared in the module (negative quantities not blocked here). | N-U06-120 |
| VDR-U06-C210 | FUNCTION MAPPING REQUIRED | purchase/data/ir_cron_data.xml:4-10 | model._send_reminder_mail() | FACT | always | — | ir.cron 'Purchase reminder': runs as base.user_root, every 1 day, code model._send_reminder_mail() on purchase.order (noupdate, forcecreate). | N-U06-123 |
| VDR-U06-C211 | FUNCTION MAPPING REQUIRED | purchase/data/ir_cron_data.xml:4 | Purchase reminder | OBSERVATION | restored DB | — | DB: ir_cron id 30 'Purchase reminder' active=true, interval 1 days, priority 5, user_id 1; its server action 659 is code 'model._send_reminder_mail()'. | N-U06-123 |
| VDR-U06-C212 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1064-1068 | group_send_reminder | FACT | always | — | _send_reminder_mail returns immediately unless env.user has purchase.group_send_reminder; template email_template_edi_purchase_reminder must exist. | N-U06-132 |
| VDR-U06-C213 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1069-1081 | reminder_date_before_receipt | FACT | always | — | cron path: orders = _get_orders_to_remind(); posts the reminder template via message_post_with_source (is_reminder, mt_comment) when date_planned - reminder_date_before_receipt days equals today. | N-U06-125 |
| VDR-U06-C214 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1073 | datetime.today().date() | FACT | always | RT | comparison is (date_planned - N days).date() == datetime.today().date() using server-local naive dates; orders without date_planned are skipped. | N-U06-134 |
| VDR-U06-C215 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1134-1142 | receipt_reminder_email', '=', True | FACT | always | — | _get_orders_to_remind: partner set, state purchase, acknowledged False, receipt_reminder_email True. | N-U06-124 |
| VDR-U06-C216 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1142 | != ['service'] | INFERENCE | always | RT | service-only exclusion is p.mapped('...product_tmpl_id.type') != ['service']; for an order with two or more distinct service templates the mapped list has several entries so it still passes the filter (list inequality). RT to confirm. | N-U06-133 |
| VDR-U06-C217 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:247-251 | with_company(order.company_id) | FACT | always | — | receipt_reminder_email and reminder_date_before_receipt on the PO are stored computeds (editable) from the vendor's company-dependent values. | N-U06-126 |
| VDR-U06-C218 | FUNCTION MAPPING REQUIRED | purchase/models/res_partner.py:41-44 | company_dependent=True | FACT | always | — | res.partner receipt_reminder_email and reminder_date_before_receipt are company_dependent. | N-U06-126 |
| VDR-U06-C219 | FUNCTION MAPPING REQUIRED | purchase/data/purchase_data.xml:41 | reminder_date_before_receipt | OBSERVATION | source default + restored DB row | — | ir.default sets res.partner.reminder_date_before_receipt = 1 as fallback for the company-dependent field; DB has this default (ir_default row = 1). | N-U06-126 |
| VDR-U06-C220 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1083-1097 | send_reminder_preview | FACT | reminder group | — | send_reminder_preview sends the reminder template to the current user's email only and returns a toast message. | N-U06-129 |
| VDR-U06-C221 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:876-887 | _send_reminder_mail(send_single=True) | FACT | reminder group | — | server action 'Send Reminder' (form binding, group_send_reminder) calls _send_reminder_mail(send_single=True), which opens the mail composer for that order. | N-U06-129 |
| VDR-U06-C222 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1234-1249 | acknowledge=True | FACT | always | — | get_acknowledge_url and get_update_url build portal URLs with &acknowledge=True / &update=True. | N-U06-127 |
| VDR-U06-C223 | FUNCTION MAPPING REQUIRED | purchase/data/mail_template_data.xml:81-124 | Vendor Reminder | FACT | always | — | template 'Purchase: Vendor Reminder': from buyer or user email, shows expected date (or 'undefined') and an Acknowledge link; attaches the PO report; auto_delete. | N-U06-127 |
| VDR-U06-C224 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1351-1378 | Date Updated | FACT | always | — | vendor date change creates/extends a warning activity 'Date Updated' for the buyer listing product, original and new dates. | N-U06-128 |
| VDR-U06-C225 | FUNCTION MAPPING REQUIRED | purchase/controllers/portal.py:166-194 | _update_date_planned_for_lines | FACT | portal route | — | jsonrpc POST /my/purchase/<id>/update (auth public + token): converts dates to noon in the order user's timezone and updates the lines; returns 204. | N-U06-128 |
| VDR-U06-C226 | FUNCTION MAPPING REQUIRED | purchase/controllers/portal.py:175-190 | line_id = int(id_str) | INFERENCE | portal route | RT | the update route does not check order state or acknowledged flag; any line id of the order with a valid date string is changed. RT to confirm. | N-U06-135 |
| VDR-U06-C227 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:36-38 | purchase.group_send_reminder | FACT | always | — | base.group_user implies purchase.group_send_reminder (noupdate), so every internal user has the reminder group by default. | N-U06-130 |
| VDR-U06-C228 | FUNCTION MAPPING REQUIRED | purchase/models/res_config_settings.py:21-22 | implied_group='purchase.group_send_reminder' | FACT | always | — | settings field group_send_reminder (Receipt Reminder, default True) toggles that implied group. | N-U06-130 |
| VDR-U06-C229 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:36-38 | group_send_reminder | OBSERVATION | restored DB | — | DB: res_groups_implied_rel has group 1 (base.group_user) implying group 78 (group_send_reminder) and group 77 (group_warning_purchase: Purchase Warnings enabled). | N-U06-130 |
| VDR-U06-C230 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:981-982 | raise AccessDenied() | FACT | always | — | retrieve_dashboard raises AccessDenied for non-internal users; counts draft, sent, late, not-acknowledged and late-receipt orders by priority and by current user. | N-U06-121 |
| VDR-U06-C231 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:497-506 | is_reminder | FACT | always | — | mail notification: reminder mails show a plain 'View' button; other mails link to the portal confirm url with title View Quotation/View Order. | N-U06-121 |
| VDR-U06-C232 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order_line.py:105 | _update_move_date_deadline(new_date) | FACT | purchase_stock installed (hand-off U07) | — | inventory integration pushes a changed line date_planned to receipt move deadlines. | N-U06-131 |
| VDR-U06-C233 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1236-1243 | Unsuported anymore | FACT | always | — | only the acknowledge mechanism remains; there is no vendor confirm/decline flow in the reminder mail. | N-U06-127 |
| VDR-U06-C234 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:119-121 | acknowledged | FACT | always | — | acknowledged stops further automatic reminders because _get_orders_to_remind requires acknowledged False (r06). | N-U06-127 |
| VDR-U06-C235 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:21-23 | 'purchase_template' | FACT | purchase_requisition installed | CONTRA | requisition_type is blanket_order (default) or purchase_template; there is no separate 'call for tender' type or state machine (CONTRA: capability brief); tenders are modelled as alternatives (g20+). | N-U06-137 |
| VDR-U06-C236 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:34-42 | ('done', 'Closed') | FACT | always | — | agreement state draft/confirmed/done(Closed)/cancel, required, copy=False, tracked. | N-U06-139 |
| VDR-U06-C237 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:85-95 | purchase.requisition.blanket.order | FACT | always | — | create assigns name from sequence blanket.order (BO) or purchase.template (PT) with the agreement company. | N-U06-137 |
| VDR-U06-C238 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:97-111 | You cannot change the Agreement Type or Company | FACT | always | — | write: changing requisition_type or company on a non-draft agreement raises UserError (after the write, rolled back); templates clear dates; a new name is issued. | N-U06-152 |
| VDR-U06-C239 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:77-83 | End date cannot be earlier than start date | FACT | always | — | constraint date_end >= date_start, else ValidationError listing agreements. | N-U06-152 |
| VDR-U06-C240 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:47-62 | already an open blanket order | FACT | always | — | vendor onchange only warns if the vendor already has a confirmed blanket order in the company. | N-U06-139 |
| VDR-U06-C241 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:64-70 | property_purchase_currency_id | FACT | always | — | requisition currency = vendor purchase currency else company currency. | N-U06-137 |
| VDR-U06-C242 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:129-140 | does not contain any product lines | FACT | always | — | action_confirm: no lines -> UserError; blanket order lines need price_unit > 0 and product_qty > 0; each line creates a supplierinfo; state confirmed. Templates skip those checks. | N-U06-140 |
| VDR-U06-C243 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:248-261 | create a supplier_info only in case of blanket order | FACT | always | — | _create_supplier_info only for blanket orders with a vendor, written with sudo. | N-U06-141 |
| VDR-U06-C244 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:146-156 | To close this purchase requisition | FACT | always | — | action_done: UserError if any linked PO is draft/sent/to approve; then unlinks the lines' supplier info and writes state done. | N-U06-142 |
| VDR-U06-C245 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:118-127 | requisition_line.supplier_info_ids.sudo().unlink() | FACT | always | — | action_cancel removes supplier info, cancels draft POs and sets state cancel. | N-U06-143 |
| VDR-U06-C246 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:142-144 | def action_draft | FACT | always | — | action_draft sets state draft with no checks; the view offers it only from cancel. | N-U06-139 |
| VDR-U06-C247 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:158-161 | You can only delete draft or cancelled requisitions | FACT | always | — | deletion allowed only for draft or cancel agreements. | N-U06-152 |
| VDR-U06-C248 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:216-229 | You cannot have a negative or unit price of 0 | FACT | blanket order confirmed | — | creating a line on an active blanket order requires price > 0 and creates a supplierinfo if none exists for product/vendor. | N-U06-153 |
| VDR-U06-C249 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:231-241 | self.supplier_info_ids.write | FACT | always | — | line write: price <= 0 on an active blanket order -> UserError; otherwise price propagates to the line's supplierinfo. | N-U06-148 |
| VDR-U06-C250 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:243-246 | to_unlink.supplier_info_ids.unlink() | FACT | always | — | deleting a line of an active agreement also deletes its supplierinfo. | N-U06-148 |
| VDR-U06-C251 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:184-199 | purchase_order.state == 'purchase' | FACT | always | — | qty_ordered = sum of product_qty of PO lines (same product, UoM converted) of linked POs in state purchase; no cap or constraint uses it. | N-U06-145 |
| VDR-U06-C252 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:206-214 | line.requisition_id.requisition_type != 'purchase_template' | FACT | template in draft with vendor | — | template line price defaults from _select_seller at date_start else standard_price. | N-U06-144 |
| VDR-U06-C253 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:36-93 | if self.state != 'draft': | FACT | always | — | onchange requisition_id fills partner, fpos, payment term, company, currency, origin (appends), note, order date = max(now, date_start); lines rebuilt only if state draft; qty = line qty for templates else 0; taxes from vendor taxes of agreement company and parents. | N-U06-144 |
| VDR-U06-C254 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:10-20 | implode (delete) group | FACT | purchase_requisition installed | — | purchase.order.group groups alternative POs; write deletes groups with <= 1 order. | N-U06-149 |
| VDR-U06-C255 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:30-34 | Alternative POs | FACT | always | — | alternative_po_ids is related to the group's orders, domain id != self and state in draft/sent/to approve. | N-U06-137 |
| VDR-U06-C256 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:95-108 | What about the alternative Requests for Quotations | FACT | always | — | button_confirm opens the warning wizard with alternatives in draft/sent/to approve (not self) unless skip_alternative_check. | N-U06-146 |
| VDR-U06-C257 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:112-121 | origin_po_id | FACT | always | — | create with context origin_po_id adds the new PO to the origin's group (or creates the group). | N-U06-149 |
| VDR-U06-C258 | FUNCTION MAPPING REQUIRED | purchase_requisition/wizard/purchase_requisition_create_alternative.py:59-100 | copy_products | FACT | always | — | create-alternative wizard builds one RFQ per chosen vendor copying date_order, buyer, dropship address, origin; currency/payment term from the vendor; lines copy product, qty, UoM, analytic; the agreement link is not copied (default_requisition_id False). | N-U06-147 |
| VDR-U06-C259 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:191-234 | get_tender_best_lines | FACT | always | — | get_tender_best_lines picks per product the lowest price_total_cc, lowest unit price and earliest date_planned among alternatives, skipping cancel/purchase lines and zero quantities. | N-U06-147 |
| VDR-U06-C260 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:294-322 | action_clear_quantities | FACT | always | — | action_clear_quantities zeroes product_qty on non-cancel/purchase lines; action_choose clears the same product's quantities on other alternatives. | N-U06-147 |
| VDR-U06-C261 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:253-259 | line.price_subtotal / line.order_id.currency_rate | FACT | always | — | price_total_cc = price_subtotal / order currency_rate (company currency, stored). | N-U06-147 |
| VDR-U06-C262 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:240-247 | _merge_alternative_po | FACT | always | — | merging RFQs also merges their alternatives. | N-U06-147 |
| VDR-U06-C263 | FUNCTION MAPPING REQUIRED | purchase_requisition/security/ir.model.access.csv:2-8 | access_purchase_requisition_purchase_order_group | FACT | always | — | ACL: purchase user full CRUD on requisition, line, alternative wizards and order group; purchase manager read-only rows on requisition/line. | N-U06-165 |
| VDR-U06-C264 | FUNCTION MAPPING REQUIRED | purchase_requisition/security/purchase_requisition_security.xml:4-14 | domain_force | FACT | always | — | record rules: company_id in company_ids for requisition and line. | N-U06-175 |
| VDR-U06-C265 | FUNCTION MAPPING REQUIRED | purchase_requisition/security/purchase_requisition_security.xml:16-18 | group_purchase_alternatives | FACT | always | — | group purchase_requisition.group_purchase_alternatives ('Manage Purchase Alternatives') gates the PO Alternatives tab only; model methods are not gated. | N-U06-150 |
| VDR-U06-C266 | FUNCTION MAPPING REQUIRED | purchase_requisition/views/purchase_requisition_views.xml:38-46 | action_done | FACT | always | — | form buttons: New Quotation (confirmed), Confirm (draft), Close (confirmed and not template), Reset to Draft (cancel), Cancel (draft/confirmed); status bar hidden for templates. | N-U06-150 |
| VDR-U06-C267 | FUNCTION MAPPING REQUIRED | purchase_requisition/views/purchase_views.xml:9-16 | requisition_type == 'blanket_order' | FACT | always | — | PO vendor is read-only when the agreement is a blanket order; agreement picker domain: state confirmed, vendor equal or empty, same company. | N-U06-144 |
| VDR-U06-C268 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/res_config_settings.py:9 | group_purchase_alternatives | FACT | always | — | settings field group_purchase_alternatives (implied group) appears only when agreements are enabled. | N-U06-150 |
| VDR-U06-C269 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:64-65 | requisition.date_start | INFERENCE | always | RT | only the onchange sets date_order >= agreement start; no server constraint was found tying PO dates/qty to agreement validity or ordered qty. RT to confirm. | N-U06-154 |
| VDR-U06-C270 | FUNCTION MAPPING REQUIRED | purchase_requisition/security/purchase_requisition_security.xml:16-18 | Manage Purchase Alternatives | OBSERVATION | restored DB | — | DB: purchase_requisition installed; 0 agreements; group 115 (Manage Purchase Alternatives) has no implied-group link from base.group_user (feature off); sequences BO/PT exist with number_next 1. | N-U06-157 |
| VDR-U06-C271 | FUNCTION MAPPING REQUIRED | purchase_requisition_stock/models/purchase_requisition.py:17-19 | Operation Type | FACT | purchase_requisition_stock installed | — | purchase_requisition_stock adds warehouse and required picking_type_id on the agreement (hand-off U07/DISCOVERED SUPPORTING MODULE). | N-U06-151 |
| VDR-U06-C272 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether agreement vendor price date ranges interact with the PO date (supplierinfo created by agreements has no date_start/date_end set in _create_supplier_info). | N-U06-156 |
| VDR-U06-C273 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:11-16 | group_purchase_user | FACT | always | — | group_purchase_user ('User') implies base.group_user; privilege Purchase. | N-U06-160 |
| VDR-U06-C274 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:18-24 | base.user_admin | FACT | always | — | group_purchase_manager ('Administrator') implies group_purchase_user and is populated with base.user_root and base.user_admin. | N-U06-160 |
| VDR-U06-C275 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:26-32 | group_warning_purchase | FACT | always | — | two optional feature groups: group_warning_purchase and group_send_reminder. | N-U06-166 |
| VDR-U06-C276 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:2-6 | access_purchase_order_portal | FACT | always | — | purchase.order ACL: user CRUD, manager CRUD, account readonly read, account invoice read+write, portal read. | N-U06-161 |
| VDR-U06-C277 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:7-10 | purchase_order_line_invoicing_payments | FACT | always | — | purchase.order.line ACL mirrors the order ACL (user/manager CRUD, account readonly read, account invoice read+write) and portal read (line 15). | N-U06-161 |
| VDR-U06-C278 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:11-14 | access_bill_to_po_wizard | FACT | always | — | bill.line.match: purchase user read, account readonly read, account invoice read+write; bill_to_po wizard: purchase user read/write/create. | N-U06-161 |
| VDR-U06-C279 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:25-29 | access_account_move_line_manager | FACT | always | — | purchase user: account.move CRUD, account.move.line read/write/create (no delete); purchase manager: account.move.line CRUD; plus read on analytic line, partial reconcile, journals, taxes. | N-U06-163 |
| VDR-U06-C280 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:30-33 | access_product_supplierinfo_purchase_manager | FACT | always | — | purchase manager: res.partner CRU (no delete), product.supplierinfo and pricelist item CRUD, account.account read. | N-U06-164 |
| VDR-U06-C281 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:34-36 | access_report_purchase_order_user | FACT | always | — | read-only access to purchase.bill.union and purchase.report for purchase user and (report) manager. | N-U06-161 |
| VDR-U06-C282 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:40-50 | purchase_order_comp_rule | FACT | always | — | global rules: purchase.order and purchase.order.line company_id in company_ids. | N-U06-162 |
| VDR-U06-C283 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:52-61 | portal_purchase_order_user_rule | FACT | always | — | portal rule: partner_id child_of user.commercial_partner_id; read/write/unlink on, create off (ACL limits portal to read). | N-U06-162 |
| VDR-U06-C284 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:63-74 | purchase_user_account_move_rule | FACT | always | — | purchase user is limited to in_invoice/in_refund/in_receipt moves and lines by rule. | N-U06-163 |
| VDR-U06-C285 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:75-91 | purchase_order_report_comp_rule | FACT | always | — | portal rule for lines (order partner child_of commercial partner) and company rules for bill union (company_ids + False) and purchase.report. | N-U06-162 |
| VDR-U06-C286 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:5-8 | groups="group_purchase_manager,group_purchase_user" | FACT | always | — | root Purchase menu visible to purchase user and manager; Configuration menu to manager only (line 19). | N-U06-164 |
| VDR-U06-C287 | FUNCTION MAPPING REQUIRED | purchase/controllers/portal.py:143-148 | _document_check_access | FACT | portal route | — | portal order page uses auth public with access_token or logged-in access check; AccessError/MissingError redirect to /my. | N-U06-168 |
| VDR-U06-C288 | FUNCTION MAPPING REQUIRED | purchase/models/res_partner.py:34-38 | groups='purchase.group_purchase_user' | FACT | always | — | purchase_order_count on partner readable only by purchase user group; stat button listing hidden otherwise. | N-U06-161 |
| VDR-U06-C289 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:898-910 | group_ids | FACT | always | — | server action Merge RFQs is bound to list view with group_ids account.group_account_invoice (not a purchase group). | N-U06-161 |
| VDR-U06-C290 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:1-36 | access_purchase_bill_union | OBSERVATION | restored DB | — | DB: ir_model_access rows from module purchase = 35 (csv declares 35 data lines); module purchase_requisition = 7 (+2 from purchase_requisition_stock for stock manager); ir_rule rows from purchase = 8, purchase_requisition = 2. | N-U06-169 |
| VDR-U06-C291 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:18-24 | base.user_root | OBSERVATION | restored DB | — | DB: group_purchase_manager has 2 direct user members; group_purchase_user has 0 direct members; groups 75/76 implied chain 76->75->1. | N-U06-172 |
| VDR-U06-C292 | FUNCTION MAPPING REQUIRED | purchase_requisition/security/ir.model.access.csv:4-5 | access_purchase_requisition_manager | INFERENCE | always | — | the manager rows on requisition/line are read-only but group_purchase_manager implies group_purchase_user which holds full CRUD, so effective manager rights are full. | N-U06-165 |
| VDR-U06-C293 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:22-24 | access_res_partner_purchase_user | FACT | always | — | purchase user read-only on res.partner; creating vendors needs the manager row (line 30) or other modules. | N-U06-171 |
| VDR-U06-C294 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:25 | access_account_move,account.move | INFERENCE | always | — | purchase user holds account.move CRUD (line 25) restricted by rule to vendor move types (x12), i.e. broad bill rights. | N-U06-171 |
| VDR-U06-C295 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:131-133 | name="locked" | INFERENCE | always | — | approval and unlock controls rely on button groups in the form; Python methods carry no group checks (button_approve 615-619; button_unlock 654-655). | N-U06-170 |
| VDR-U06-C296 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:160 | default=lambda self: self.env.company.id | FACT | always | — | company_id required, indexed, default env.company; partner_id/user_id/dest_address_id use check_company. | N-U06-173 |
| VDR-U06-C297 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:397-405 | self.with_company(company_id) | FACT | always | — | create evaluates defaults and the sequence under with_company(company_id). | N-U06-176 |
| VDR-U06-C298 | FUNCTION MAPPING REQUIRED | purchase/data/purchase_data.xml:22-28 | <field name="company_id" eval="False"/> | FACT | always | — | sequence purchase.order (prefix P, padding 5) has company_id False: one shared numbering across companies. | N-U06-176 |
| VDR-U06-C299 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:143 | fiscal_position_id = fields.Many2one | FACT | always | — | fiscal_position_id and payment_term_id domains restrict to company-less or order-company records. | N-U06-173 |
| VDR-U06-C300 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:60 | related='order_id.company_id' | FACT | always | — | line company_id is the stored related of the order company; line rule uses it. | N-U06-175 |
| VDR-U06-C301 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:769 | order = order.with_company(order.company_id) | FACT | always | — | bill generation runs in the order's company context and creates moves per company (811). | N-U06-178 |
| VDR-U06-C302 | FUNCTION MAPPING REQUIRED | purchase_stock/models/purchase_order.py:24 | warehouse_id.company_id | FACT | purchase_stock installed (hand-off U07) | — | receipt type (picking_type_id) is required with a domain on warehouse company = order company; recomputed when the company changes (line 88). | N-U06-181 |
| VDR-U06-C303 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:20 | check_company=True | FACT | always | — | requisition vendor_id and user_id use check_company; company_id required default env.company. | N-U06-179 |
| VDR-U06-C304 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase.py:52-56 | self.company_id = requisition.company_id.id | FACT | always | — | choosing an agreement sets the PO company and currency from the agreement. | N-U06-179 |
| VDR-U06-C305 | FUNCTION MAPPING REQUIRED | purchase/__manifest__.py:11 | 'depends': ['account'] | INFERENCE | always | — | purchase depends only on account; no inter-company module is installed or referenced in purchase/purchase_requisition (no hook found). | N-U06-184 |
| VDR-U06-C306 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:408-412 | In order to delete a purchase order | FACT | always | — | UserError sites on PO: delete non-cancelled (412), confirm missing product (631), cancel locked (644) or billed (648), merge (<2 or no match 842/851), no attachment (1414), 'Unsupported operator' ValidationError (369). | N-U06-183 |
| VDR-U06-C307 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:194-199 | Please change the company of your quotation | FACT | always | — | company/product mismatch ValidationError message advises changing the quotation company or removing products of other companies. | N-U06-182 |
| VDR-U06-C308 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1413-1417 | No attachment was provided | FACT | always | — | create_document_from_attachment raises UserError when no attachment is given; orders created with default partner of the user. | N-U06-183 |
| VDR-U06-C309 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1252-1259 | self.env.company.currency_id | INFERENCE | multi-company | RT | approval threshold and price ranking (p12) use env.company; both flagged RT because the DB has one company. | N-U06-185 |
| VDR-U06-C310 | FUNCTION MAPPING REQUIRED | purchase/models/res_company.py:10-23 | po_lock | OBSERVATION | restored DB | — | DB: 1 company; po_lock = 'lock', po_double_validation = 'two_step', po_double_validation_amount = 5000.0 (non-default lock and approval are ON); multi-company paths cannot be observed. | N-U06-186 |
| VDR-U06-C311 | FUNCTION MAPPING REQUIRED | purchase/models/res_company.py:22-23 | po_double_validation_amount | OBSERVATION | restored DB | — | DB values in m15 mean confirm by non-manager above 5000 goes to 'to approve' and approved orders become locked in this configuration (derived from a15/a09/a10/s10). | N-U06-034 |
| VDR-U06-C312 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:105-111 | 'sent', 'RFQ Sent' | INFERENCE | always | — | purpose derived from the state set (draft RFQ, RFQ sent, to approve, purchase order): negotiation states precede the committed 'purchase' state and approval is a dedicated state. | N-U06-003 |
| VDR-U06-C313 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:625-639 | order.button_approve() | INFERENCE | always | — | transition summary derived from button_confirm (625-639), button_approve (615-619), button_cancel (641-649), button_draft (621-623) and the print/send paths (479-483, 611-613). | N-U06-011 |
| VDR-U06-C314 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:138 | id="draft_confirm" | FACT | always | — | a Confirm Order button exists for state draft (draft_confirm) as well as for sent (bid_confirm, line 135): sending is not mandatory before confirming. | N-U06-013 |
| VDR-U06-C315 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:146 | lock_confirmed_po == 'lock' | FACT | always | — | the manual Lock button is hidden unless the company policy is 'lock' (and state purchase, not locked); the Python button_lock (651-652) has no policy check. | N-U06-014 |
| VDR-U06-C316 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | purchase_stock installed | RT | UNKNOWN - EVIDENCE INSUFFICIENT: receipt recreation after reset-to-draft and re-confirm (purchase_stock _create_picking is called from button_approve, but its handling of previously cancelled receipts was not read). | N-U06-023 |
| VDR-U06-C317 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:625-639 | Deal with double validation process | INFERENCE | always | — | WHAT of confirmation derived from the sequence: error check (629-631), analytic validation (632), supplier registration (633), approval or to-approve (634-638). | N-U06-024 |
| VDR-U06-C318 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1251-1260 | po_double_validation_amount | INFERENCE | always | — | the purpose of the two-step mechanism follows from the threshold comparison: orders below the amount or by managers are directly approved, others wait. | N-U06-025 |
| VDR-U06-C319 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:615-619 | 'date_approve': fields.Datetime.now() | FACT | always | — | state effects of confirm/approve: button_approve writes state 'purchase' + date_approve; button_confirm writes 'to approve' when not allowed (638). | N-U06-033 |
| VDR-U06-C320 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1256-1259 | self.amount_total < | FACT | two_step | — | the comparison operator is '<' so an order whose amount_total equals the converted threshold is not auto-approved. | N-U06-041 |
| VDR-U06-C321 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | multi-currency | RT | UNKNOWN - EVIDENCE INSUFFICIENT: behaviour of _convert when no currency rate exists for the order date (res.currency._convert not read in this unit). | N-U06-042 |
| VDR-U06-C322 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:641-655 | def button_lock | INFERENCE | always | — | WHAT of this capability summarised from button_cancel (641-649), button_draft (621-623), button_lock/unlock (651-655). | N-U06-043 |
| VDR-U06-C323 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:646-648 | purchase_orders_with_invoices | INFERENCE | always | — | purpose: the cancel guard exists to prevent cancelling orders that already have live (non-draft, non-cancelled) vendor bills. | N-U06-044 |
| VDR-U06-C324 | FUNCTION MAPPING REQUIRED | purchase/views/purchase_views.xml:142-147 | button_unlock | INFERENCE | always | — | state list for the capability: cancel->draft (reset), any open state->cancel, locked toggled by lock/unlock buttons shown per conditions. | N-U06-053 |
| VDR-U06-C325 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:272-283 | line.selected_seller_id = seller.id if seller else False | INFERENCE | always | — | purpose: the selected seller feeds price/discount/date/name defaults (see p15-p20) so buyers need not re-enter negotiated vendor terms. | N-U06-061 |
| VDR-U06-C326 | FUNCTION MAPPING REQUIRED | product/models/product_supplierinfo.py:33-41 | date_start | FACT | always | — | supplierinfo optional restrictions: company_id, product_id (variant), date_start, date_end (all optional). | N-U06-073 |
| VDR-U06-C327 | FUNCTION MAPPING REQUIRED | purchase/models/product.py:13-18 | Control bills based on ordered quantities | INFERENCE | always | — | purpose of the bill control policy as stated in the field help: control bills on ordered or on received quantities. | N-U06-081 |
| VDR-U06-C328 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:127-131 | compute='_get_invoiced', store=True, readonly=True | FACT | always | — | invoice_status is a stored, readonly computed field (no, to invoice, invoiced), never edited directly. | N-U06-092 |
| VDR-U06-C329 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:30-35 | order_lines = order.order_line.filtered | INFERENCE | always | — | structure lines (display_type) are excluded from the totals, so organising a document does not affect amounts (also see l02). | N-U06-103 |
| VDR-U06-C330 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order_line.py:123-133 | AccountTax._add_tax_details_in_base_line | INFERENCE | always | — | line amounts depend on the AccountTax engine, fiscal position (via tax_ids) and the order currency rate (see l06, l07, l09). | N-U06-115 |
| VDR-U06-C331 | FUNCTION MAPPING REQUIRED | purchase/models/purchase_order.py:1064-1081 | def _send_reminder_mail | INFERENCE | always | — | purpose of the reminder routine derived from its selection and date test: remind vendors N days before expected receipt. | N-U06-122 |
| VDR-U06-C332 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | mail server | RT | UNKNOWN - EVIDENCE INSUFFICIENT: mail delivery, rendering and outgoing mail server configuration (needs runtime). | N-U06-136 |
| VDR-U06-C333 | FUNCTION MAPPING REQUIRED | purchase_requisition/__manifest__.py:10-12 | Blanket orders | FACT | purchase_requisition installed | — | manifest description: calls for tenders collect competing offers; blanket orders give predetermined pricing with vendors. | N-U06-138 |
| VDR-U06-C334 | FUNCTION MAPPING REQUIRED | purchase_requisition/models/purchase_requisition.py:129-130 | def action_confirm | FACT | always | — | action_confirm/action_done/action_cancel carry no group check in Python and the form buttons carry no groups attribute (views 42-45), so any purchase user (ACL line 2) can run them. | N-U06-155 |
| VDR-U06-C335 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:11-24 | Administrator | INFERENCE | always | — | WHAT of the role model: two purchase groups plus accounting groups in ACL (csv 2-13) and a portal group (csv 6, 15). | N-U06-158 |
| VDR-U06-C336 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:6 | access_purchase_order_portal | INFERENCE | always | — | purpose of portal access: read-only access for vendors limited by rule to their own partner tree (rule 52-61). | N-U06-159 |
| VDR-U06-C337 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:26-28 | group_warning_purchase | FACT | always | — | warnings group and reminder group are optional features; alternatives group is declared in purchase_requisition; reminder group is default-on via base.group_user (36-38). | N-U06-167 |
| VDR-U06-C338 | FUNCTION MAPPING REQUIRED | purchase/security/purchase_security.xml:40-44 | Purchase Order multi-company | INFERENCE | always | — | purpose of company rules: records visible only for company_ids of the user. | N-U06-174 |
| VDR-U06-C339 | FUNCTION MAPPING REQUIRED | purchase/models/res_company.py:10-14 | po_lock | OBSERVATION | restored DB | — | DB: select count(*) from res_company = 1; multi-company behaviour unobservable. | N-U06-180 |
