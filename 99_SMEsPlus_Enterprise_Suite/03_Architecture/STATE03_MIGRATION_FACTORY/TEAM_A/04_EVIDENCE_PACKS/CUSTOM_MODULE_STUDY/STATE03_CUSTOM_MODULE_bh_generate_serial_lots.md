> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: bh_generate_serial_lots

- Module: bh_generate_serial_lots
- License (confirmed in manifest): LGPL-3 (bh_generate_serial_lots/__manifest__.py:27)
- Author (manifest): SCGL (bh_generate_serial_lots/__manifest__.py:12)
- Version (manifest): 19.0.1.0.0 (bh_generate_serial_lots/__manifest__.py:4)
- Path: addons_Extramodule/addons/bh_generate_serial_lots
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Extends the "Generate Serials/Lots" pop-up on stock moves so lot names follow a structured naming pattern: part reference, warehouse-receipt reference, original first-lot name, then a start and end sequence of the units covered by that lot (pattern documented at bh_generate_serial_lots/__manifest__.py:9-10).
- Adds three input boxes to the pop-up (Part Refer, WH in REF, Qty LOT) and a live preview line (static/src/widgets/generate_serial_dialog_inherit.xml:12-66).
- The two reference boxes are pre-filled from the product internal reference and the transfer name (static/src/widgets/generate_serial_dialog_inherit.js:59-91).
- Makes the printed lot label taller (19mm to 26mm), reduces lot-name font with wrapping, and enlarges the barcode area (report/report_lot_label.xml:9-24).

## 2. Attachment to CORE
- Core module `stock`, client-side component `GenerateDialog` (core:stock/static/src/widgets/generate_serial.js:12): the module patches setup (js:43-53) and REPLACES the generate action (js:128-222) rather than calling the core one. The replacement re-implements the same steps as core (core:stock/static/src/widgets/generate_serial.js:57-108) and then renames the generated lot names. Business effect: REPLACES core behavior of the client-side generate button; drift risk if core changes.
- Server call is still the core stock.move method `action_generate_lot_line_vals` (js:148-151; core:stock/models/stock_move.py:1137). No server-side Python in this module.
- Dialog template `stock.generate_serial_dialog` (core:stock/static/src/widgets/lots_dialog.xml:9) is extended by inserting rows before/after the "First Lot" row (xml:9, xml:42).
- Report template `stock.report_lot_label` (core:stock/report/report_lot_barcode.xml:4) is modified by attribute change of the box size (core:...:22), replacement of the lot-name block (core:...:31) and barcode style change (core:...:38).
- Naming rule (business terms): when any of the three inputs is filled and a per-lot quantity is given, each generated lot name is rebuilt with part ref, receipt ref, original name and running unit range; when no per-lot quantity is given, only the prefix is added (js:172-192).
- Core-control impact: none on posting, lock dates, valuation, approvals, security, multi-company or numbering of documents. It does change the text of lot/serial names, but core sequence/uniqueness controls are not modified in this module. ALTERS CORE CONTROL: not found in code read.

## 3. New objects, security, automation, external calls
- New models: none. Security groups/ACLs/record rules: none. Crons/server actions: none. External calls: none (only internal ORM reads of stock.picking name and product default_code, js:64-84).
- Read of company primary colour in label style is from core field (core:base/models/res_company.py:90).

## 4. Odoo 19 compatibility
- Checked by grep in Community tree: patched class `GenerateDialog` exists (core:stock/static/src/widgets/generate_serial.js:12); refs nextSerial, nextSerialCount, totalReceived, keepLines, lots exist (core:...:30-34); template stock.generate_serial_dialog and stock.report_lot_label exist; imports getId and x2ManyCommands exist (core:...:2,7).
- No mismatch found for the references listed. The label xpath depends on core markup (`height:19mm` text and `name="lot_name"`) which are present (core:stock/report/report_lot_barcode.xml:22,31). The private datapoint members used (`_createRecordDatapoint`, `_applyCommands`, `_currentIds`, `_onUpdate`) mirror core usage (core:...:85-107) but are internal APIs.
- Data files listed in manifest do not include the CSS-only files as data; the CSS asset path is declared (manifest:20) but the file content was not read (not checked).

## 5. Custom-to-custom dependencies
- None declared (depends: stock only, manifest:14).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the sequence-range in lot names matches how the customer counts units in the receiving process (js:176-178 uses per-lot quantity and total quantity only).
- UNKNOWN - EVIDENCE INSUFFICIENT: behaviour for serial-tracked products versus lot-tracked (rename logic is not conditioned on tracking type, js:172-192).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether lot-name uniqueness constraints in core can be violated by long composed names (no Python check reviewed).
