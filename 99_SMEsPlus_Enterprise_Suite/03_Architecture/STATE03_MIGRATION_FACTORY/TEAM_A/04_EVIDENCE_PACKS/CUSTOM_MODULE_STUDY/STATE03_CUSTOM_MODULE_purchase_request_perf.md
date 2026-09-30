> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: purchase_request_perf

## 0. Header
- Module: purchase_request_perf
- License (confirmed in manifest): LGPL-3 (purchase_request_perf/__manifest__.py:25)
- Author (manifest): Patch Team (purchase_request_perf/__manifest__.py:24)
- Version (manifest): 19.0.1.1.0 (purchase_request_perf/__manifest__.py:4)
- Path: addons_Extramodule/addons/purchase_request_perf
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Approval-family support patch (not an approval rule). Speeds up and stabilises the non-core Purchase Request module: adds database indexes, batches price and unit-of-measure lookups on request lines, groups change notes into one chatter message per request, and corrects several computed fields (manifest:8-22).
- Business-visible behaviour changes: (a) urgency level recomputed per request from the required date using fixed day bands: up to 3 days, 7, 15, 29, and beyond (models/purchase_request.py:102-133); (b) a chatter note "Quantity changed" is posted when a line quantity is edited, posted quietly as a note (models/purchase_request_line.py:238-281); (c) purchased quantity is recomputed with unit conversion and excludes cancelled purchase lines (models/purchase_request_line.py:219-233); (d) cancelling a line triggers the request's auto-reject check (models/purchase_request_line.py:283-284).
- Does not decide who approves or what blocks confirmation.

## 2. Attachment to CORE
- Depends declared: purchase_request only (manifest:26-28).
- Core Community objects touched: `purchase.order.line` and `purchase.order` (read for price statistics: models/purchase_request_line.py:77-85, :108-116), `uom.uom` (compatibility lookup, models/purchase_request_line.py:125-188), `ir.sequence` (name numbering, models/purchase_request.py:84-87), chatter (message_post/subscribe). No Community method is overridden. No ALTERS CORE CONTROL.
- Overrides of non-core methods, by name:
  - `purchase.request`: `_auto_init` (ADDS after base: creates three indexes if columns exist, models/purchase_request.py:40-57); `create` (models/purchase_request.py:62-97: ADDS around base — assigns sequence name when name is the placeholder, calls the base create, then subscribes the assignee; the docstring says it replaces a faulty base version but the code still calls the base create at :89); `_compute_urgency_level` (REPLACES base compute, :102-133).
  - `purchase.request.line`: `_auto_init` (indexes, :43-54); `_compute_purchase_product_price` (REPLACES; takes the lowest positive unit price per product across all purchase order lines, :59-91); `_compute_latest_price` (REPLACES; latest unit price from confirmed purchase orders, done with a direct database query, :96-120); `_compute_filter_uom` (REPLACES; compatible-unit cache, :193-214); `_compute_purchased_qty` (REPLACES; adds dependencies, :219-233); `write` (ADDS after base: batched note, cancel hook, :238-285).
- Read of purchase order lines is not scoped by company or by the caller's rights beyond the ORM (the price aggregation at :78-85 uses the caller's environment; the direct database query at :108-116 bypasses ORM access rules and company rules). This means price hints may aggregate across companies (inference from code; not tested).

## 3. New objects, security, automation, external calls
- New models/fields: none. ACLs/groups/rules: none. Data files: none (manifest:29).
- Database objects: creates non-unique indexes on request urgency and required date, on state+requester, on line required date, and on line request-state+cancelled flag (models/purchase_request.py:50-56; models/purchase_request_line.py:46-53), each guarded by an existence check of the columns (:23-38, :31-41).
- Automation: none. External calls: none.

## 4. Odoo 19 compatibility
- Deprecated core API used: `read_group` (models/purchase_request_line.py:78) — deprecated since 19.0 in the Community tree (core:odoo/orm/models.py:2751-2755, decorator warning text). Still exists.
- `tools.create_index` and `column_exists` exist (core:odoo/tools/sql.py:597, :338).
- The module explains that `category_id` is gone from units of measure and uses `relative_uom_id` (core:uom/models/uom_uom.py:41); `category_id` no longer appears in the core unit model search result. Helper names `_get_relative_uoms`, `_get_compatible_uoms` and `get_same_group_uoms` are probed with `hasattr` (models/purchase_request_line.py:156-172); text search of `uom/models/uom_uom.py` finds none of them, so those branches are dead in a plain Community tree.
- Fallback branch that returns every unit of measure when no other path works (models/purchase_request_line.py:187-188) can widen unit choices (inference).
- Names not in Community: `purchase.request`, `purchase.request.line`, `check_auto_reject`, `urgency_level`, `filter_uom`, `latest_price`, etc. — non-core; not checkable.
- Query text in this module refers to purchase order line/order tables directly (models/purchase_request_line.py:108-116); table/column existence in Community 19 not individually verified.

## 5. Custom-to-custom dependencies
- Depends on purchase_request (non-core).
- Required by purchase_request_perf_fix. Its own changelog already contains the same unit-of-measure fix (manifest:19-21), so purchase_request_perf_fix duplicates it (see that file).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the base purchase_request `create` really has the fault described in the docstring (base source not read); if not, the extra sequence assignment could double-consume sequence numbers.
- UNKNOWN — EVIDENCE INSUFFICIENT: the size of the data in the deployed database and therefore whether the indexes have measurable effect.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether cross-company price aggregation occurs in a multi-company deployment.
