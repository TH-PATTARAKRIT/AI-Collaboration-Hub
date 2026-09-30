> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: stock_picking_reference_no

Module: stock_picking_reference_no ("Stock Picking Reference No")
License (confirmed in manifest): LGPL-3
Author (manifest): not stated in manifest
Version (manifest): 19.0.1.0
Path: addons_Extramodule/addons/stock_picking_reference_no
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Third-party (source-readable)

## 1. Business capability
- Shows, on a transfer form, the reference(s) of the previous transfer(s) in the chain, e.g. the receipt that feeds a quality-control transfer (stock_picking_reference_no/models/stock_picking.py:8-13; manifest summary, __manifest__.py:1-15).
- Purpose is traceability between chained transfers; display only.

## 2. Attachment to CORE
- Core module depended on: stock (__manifest__.py:1-15).
- stock.picking (core:stock/models/stock_picking.py:538): new computed, non-stored text field reference_no (models/stock_picking.py:8-13). It follows the origin links of the transfer's stock moves (core:stock/models/stock_move.py:102) to the origin transfers' names, comma-joined (models/stock_picking.py:15-19).
- Form: the field is added inside the "Other Information" group of the transfer form (views/stock_picking_view.xml:9-12; core:stock/views/stock_picking_views.xml:328).
- Core method overrides: none. Only a new computed field.
- ALTERS CORE CONTROL: no.

## 3. New objects, security, automation, external calls
- New models: none. Security: none shipped; inherits core stock.picking access and rules. No company scoping change.
- Cron, server actions, external calls: none.

## 4. Odoo 19 compatibility
- Checked in Community 19: stock.move.move_orig_ids exists (core:stock/models/stock_move.py:102); form anchor group name="other_infos" (core:stock/views/stock_picking_views.xml:328) and view stock.view_picking_form (core:stock/views/stock_picking_views.xml:110) exist.
- No mismatches found.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: original author / upstream source (manifest has no author or website; classification as third-party comes from the batch file only).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior when the origin move belongs to a different company than the current user's allowed companies (the name lookup follows core record access; not observed).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the field is used in printed delivery/transfer documents (no report template in module).
