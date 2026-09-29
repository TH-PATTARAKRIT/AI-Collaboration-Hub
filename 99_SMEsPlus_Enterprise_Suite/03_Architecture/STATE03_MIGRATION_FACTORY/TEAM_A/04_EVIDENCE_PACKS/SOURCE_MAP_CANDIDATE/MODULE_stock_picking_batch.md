# Source Map (candidate) — `stock_picking_batch`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_picking_batch` |
| Display name | Warehouse Management: Batch Transfer |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `07ecf0f14bd4c361` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_picking_batch/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`
- Direct dependents in 300-module list (2): `delivery_stock_picking_batch`, `stock_fleet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_ro_edi_stock`, `l10n_ro_edi_stock_batch`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / —
- Inventory of user-facing artifacts (counts): menu items 3, views 22, window actions 6, server actions 2, reports 1, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `stock.picking.to.batch` (Batch Transfer Lines); `stock.add.to.wave` (Wave Transfer Lines); `stock.picking.batch` (Batch Transfer)
- Objects extended from other modules (7): `mail.thread`, `mail.activity.mixin`, `stock.warehouse`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `stock.picking.batch` ← Community: `delivery_stock_picking_batch`, `l10n_ro_edi_stock_batch`, `stock_fleet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `mail.activity.mixin`, `stock.warehouse`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`

## 6. Actions / states / validation / automation / security
- State fields found: `stock.picking.batch` → ['draft', 'in_progress', 'done', 'cancel']
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 61 of 61 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — stock_picking_batch
Source revision: 19.0.post20260921 | Module: "Warehouse Management: Batch Transfer" (stock_picking_batch/__manifest__.py:5) | depends: stock (:12) | License LGPL-3 (:32)
Basis: static reading of all models/wizards/views/security; tests read as name outline (45 test methods across 3 files). Covers three concepts on one object: batch transfers, wave transfers (batch flagged as wave), and automatic grouping.

## A. Capabilities and optionality
- A1. Optional feature: enabled from Inventory settings ("Batch, Wave & Cluster Transfers"); not auto_install. stock/models/res_config_settings.py:28; stock/views/res_config_settings_views.xml:18
- A2. Manual batch: group several transfers (same operation type, same company) under one job with a responsible person, description, printable batch report, labels. stock_picking_batch/wizard/stock_picking_to_batch.py:18-53; stock_picking_batch/report/stock_picking_batch_report_views.xml:4-12; stock_picking_batch/models/stock_picking_batch.py:235-237,300-324
- A3. Manual wave: pick individual operation lines (not whole transfers) into a wave; transfers/moves are split when only part is taken. stock_picking_batch/models/stock_move_line.py:15-119 (TEST: tests/test_wave_picking.py:228,257,285)
- A4. Automatic batching: on confirmation/availability, a ready transfer is placed into a compatible open batch, or paired with another ready transfer in a new batch, or given a batch alone. stock_picking_batch/models/stock_picking.py:141-145,197-232 (TEST: tests/test_batch_picking.py:427,523,648)
- A5. Automatic waving: when stock is reserved, eligible operation lines are added to compatible existing waves or grouped into new ones. stock_picking_batch/models/stock_move.py:39-41; stock_picking_batch/models/stock_move_line.py:121-387 (TEST: tests/test_auto_waving.py:192-402)
- A6. Merge several open batches/waves into one; bulk "Unreserve" and "Merge" list actions. stock_picking_batch/models/stock_picking_batch.py:326-361; stock_picking_batch/views/stock_picking_batch_views.xml:317-338 (TEST: tests/test_batch_picking.py:785)
- A7. Extras: put-in-pack for the whole batch, detailed operations list, package view, reception report link, estimated weight/volume, per-type custom properties. stock_picking_batch/models/stock_picking_batch.py:62-66,81-103,287-298,363-411
- A8. Menu "Jobs" with Batch Transfers and Wave Transfers; warehouse operation-type dashboards show counts. stock_picking_batch/views/stock_picking_batch_views.xml:283-284; stock_picking_batch/views/stock_picking_wave_views.xml:134-138; stock_picking_batch/models/stock_picking.py:35-55
- A9. New warehouses: receipt and delivery operation types are created with auto-batch on and grouping by contact. stock_picking_batch/models/stock_warehouse.py:8-17 (implication: default for new warehouses only; existing types unchanged — UNKNOWN — EVIDENCE INSUFFICIENT for retro-application).

## B. Objects, relationships, lifecycle
- B1. Batch/wave record (stock.picking.batch): name from a numbered series, responsible, company, operation type, list of transfers, derived moves and move lines, scheduled date, wave flag, properties, chat and activities. stock_picking_batch/models/stock_picking_batch.py:10-66; stock_picking_batch/data/stock_picking_batch_data.xml:10-24
- B2. Link: each transfer (stock.picking) may belong to at most one batch. stock_picking_batch/models/stock_picking.py:92-96
- B3. Operation type (stock.picking.type) holds the auto-batch policy: on/off, group-by contact / destination country / source location / destination location, wave group-by product / category(+list) / location(+list), max lines, max transfers, auto-confirm (default on), batch properties definition. stock_picking_batch/models/stock_picking.py:13-33
- B4. States: Draft -> In progress -> Done, or Cancelled. Draft->In progress by Confirm (needs at least one transfer; also confirms its transfers). Done/Cancel are derived: cancelled when all transfers cancelled; done when all are done/cancelled. stock_picking_batch/models/stock_picking_batch.py:40-46,144-155,220-228 (state change is tracked in chatter, :444-447)
- B5. Cancel button (in progress only) empties the batch; an in-progress batch left with no transfers is auto-cancelled. stock_picking_batch/models/stock_picking_batch.py:196-197,230-233; stock_picking_batch/views/stock_picking_batch_views.xml:107
- B6. Validate (action_done): removes empty waiting/assigned transfers from the batch (log message), sanity-checks all remaining transfers together, logs "Transferred by Batch" on each transfer, then delegates validation (backorder handling) to the stock transfer's normal validate. stock_picking_batch/models/stock_picking_batch.py:239-281
- B7. Transfer validation side effects: validated transfers leave a batch that still has undone members; backorders created are re-offered to auto-batching/auto-waving. stock_picking_batch/models/stock_picking.py:147-183 (TEST: tests/test_batch_picking.py:969-1250)
- B8. Cancelled transfers/moves leave the batch unless the whole batch is cancelled. stock_picking_batch/models/stock_picking.py:185-190; stock_picking_batch/models/stock_move.py:15-22
- B9. Wave transfers are excluded from normal picking assignment of moves. stock_picking_batch/models/stock_move.py:10-13
- B10. Scheduled date defaults to the earliest of its transfers; setting it manually pushes the date to all transfers. stock_picking_batch/models/stock_picking_batch.py:54-59,157-165
- B11. Setting the batch responsible copies the user to its transfers (with chatter log). stock_picking_batch/models/stock_picking_batch.py:208-209; stock_picking_batch/models/stock_picking.py:117,311-319

## C. Validations, security, multi-company
- C1. Addable transfers must be same company, same operation type (if set), and in waiting/confirmed/ready state (draft also, only while the batch is draft). stock_picking_batch/models/stock_picking_batch.py:105-120,433-442
- C2. Auto-batching requires at least one grouping option when enabled. stock_picking_batch/models/stock_picking.py:79-86
- C3. Merge rules: at least two; same operation type; not mixing batch with wave; same state; not done/cancelled. stock_picking_batch/models/stock_picking_batch.py:326-338
- C4. Done batches cannot be deleted. stock_picking_batch/models/stock_picking_batch.py:212-215
- C5. Wizards: selected transfers must share one company; wave wizard requires same operation type. stock_picking_batch/wizard/stock_picking_to_batch.py:22-24; stock_picking_batch/wizard/stock_add_to_wave.py:25-26,41-50
- C6. Access: stock users (stock.group_stock_user) have full rights on batch and read/write/create on the two wizards. stock_picking_batch/security/ir.model.access.csv:2-4
- C7. Company rule: batch visible only if its company is among the user's allowed companies (rule installed noupdate=0). stock_picking_batch/security/stock_picking_batch_security.xml:3-7
- C8. Auto-batch creation/search runs with elevated rights, so it is not limited by the acting user's own access. stock_picking_batch/models/stock_picking.py:204,222,229
- C9. Company/responsible consistency is enforced by company-check on the responsible, operation type and transfer list. stock_picking_batch/models/stock_picking_batch.py:19-27,47-49; stock_picking_batch/models/stock_picking_batch.py:226
- C10. Limits: max lines / max transfers apply to automatic additions only; a weight parameter is accepted but no weight limit is applied in the merge check. stock_picking_batch/models/stock_picking_batch.py:449-482

## D. Handoffs
- D1. Stock movement, reservation, validation, backorders, packages and reception report: stock (owner); this module orchestrates and calls its validate/assign/put-in-pack logic. stock_picking_batch/models/stock_picking_batch.py:281,285,293; stock_picking_batch/models/stock_picking.py:147-183
- D2. Inventory valuation/accounting: happens through stock/stock_account when transfers are validated; this module adds none. UNKNOWN — EVIDENCE INSUFFICIENT beyond that statement (stock_account not read).
- D3. Approval: none. Audit: chatter logs on batch and transfers (state change subtype, "Transferred by Batch", removed transfers, responsible assignment). stock_picking_batch/data/stock_picking_batch_data.xml:4-8; stock_picking_batch/models/stock_picking_batch.py:268-279
- D4. Delivery/shipping extensions of batches: delivery_stock_picking_batch; Romanian e-transport: l10n_ro_edi_stock_batch; fleet dispatch: stock_fleet. (manifest dependency grep)
- D5. Sales/purchase/POS/manufacturing origins are indirect via the transfers they produce; no direct hook here. UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration that changes outcomes
- E1. Per operation type: auto-batch on/off, grouping keys, wave grouping keys, category and location lists, limits, auto-confirm (draft vs in progress for new automatic batches). stock_picking_batch/models/stock_picking.py:13-33,272
- E2. Multi-location group needed to see source/destination/location grouping options. stock_picking_batch/views/stock_picking_type_views.xml:28-56
- E3. Wave grouping by location matches lines to the nearest configured parent location. stock_picking_batch/models/stock_move_line.py:131-163
- E4. Sequences BATCH/ and WAVE/ with operation-type code inserted into the name; a prefix lacking "/" triggers a warning and a fallback name. stock_picking_batch/data/stock_picking_batch_data.xml:10-24; stock_picking_batch/models/stock_picking_batch.py:416-431 (TEST: tests/test_batch_picking.py:1250,1269)
- E5. Context flags: skip auto-wave, batches being validated (prevents re-merging into the batch being closed). stock_picking_batch/models/stock_move_line.py:124,185; stock_picking_batch/models/stock_picking.py:285-286

## F. Extension path (module names only)
- stock.picking.batch: delivery_stock_picking_batch, l10n_ro_edi_stock_batch, stock_fleet.
- stock.picking.type: delivery_stock_picking_batch, l10n_ar_stock, l10n_it_stock_ddt, l10n_tr_nilvera_edispatch, mrp, point_of_sale, project_stock_account, repair, stock_account, stock_dropshipping, stock_fleet.
- stock.move.line: mrp, mrp_subcontracting, product_expiry, repair, sale_mrp, sale_stock, stock_account, stock_delivery. stock.move: many (purchase_stock, sale_stock, mrp, stock_account and others). stock.picking: see stock_sms note (includes delivery_stock_picking_batch, l10n_ro_edi_stock_batch, stock_fleet as batch-aware).
- Manifests depending on stock_picking_batch: delivery_stock_picking_batch, l10n_ro_edi_stock, l10n_ro_edi_stock_batch, stock_fleet.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether enabling the setting in settings applies groups beyond installing the module (only the module toggle was checked).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end (JS/tour) behaviour under static/, mobile/barcode flows.
- UNKNOWN — EVIDENCE INSUFFICIENT: report layout content (report_picking_batch.xml not read in detail).
- UNKNOWN — EVIDENCE INSUFFICIENT: performance or concurrency behaviour of the automatic grouping on large volumes.

