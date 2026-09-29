# Source Map (candidate) — `account_fleet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_fleet` |
| Display name | Accounting/Fleet bridge |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d6731c94ed2c6ffd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_fleet/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `fleet`, `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Manage accounting with fleets
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `account.automatic.entry.wizard`, `account.move`, `account.move.line`, `fleet.vehicle.log.services`, `fleet.vehicle`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.automatic.entry.wizard`, `account.move`, `account.move.line`, `fleet.vehicle.log.services`, `fleet.vehicle`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 39 of 40 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_fleet (Accounting/Fleet bridge)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/account_fleet.json. All pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge module linking vendor-bill lines to company vehicles; depends on fleet and account only (account_fleet/__manifest__.py:8).
- Conditional-on-install: `auto_install` is true, so it appears automatically once both fleet and account are present (account_fleet/__manifest__.py:16). Not a standalone/optional application.
- Adds a "Vehicle" reference on journal/invoice lines; shown only for purchase-type documents (vendor bill, vendor refund, vendor receipt) and hidden by default as an optional column (account_fleet/views/account_move_views.xml:9-16).
- On the first posting of a vendor bill, each product line that carries a vehicle and has no service record yet produces a "Vendor Bill" service log entry on that vehicle, with a chatter note linking to the bill (account_fleet/models/account_move.py:9-29). Core behaviour of the bridge; skipped silently if the seeded "Vendor Bill" service type is missing (account_fleet/models/account_move.py:10-12).
- Vehicle form gets a "Bills" statistic button opening the vendor bills that reference the vehicle (account_fleet/views/fleet_vehicle_views.xml:9-17; account_fleet/models/fleet_vehicle.py:33-44).
- Service-log form gets a "Service's Bill" button (green label when the bill is posted, warning label otherwise) and the cost field becomes read-only when linked to a bill line (account_fleet/views/fleet_vehicle_log_services_views.xml:12-30).
- Period-shifting (deferral/accrual) transfer wizard keeps the vehicle on the counter-lines that hit the original account (account_fleet/wizard/account_automatic_entry_wizard.py:9-15); (TEST) confirmed for "change period" action (account_fleet/tests/test_account_fleet.py:13).

## B. Business objects, relationships, lifecycle
- Vendor bill line -> Vehicle (many-to-one, indexed when set) (account_fleet/models/account_move.py:35).
- Vendor bill line <-> Fleet service log (effectively one-to-one; the log holds the line reference) (account_fleet/models/account_move.py:38-39; account_fleet/models/fleet_vehicle_log_services.py:10).
- Service log cost is derived from the linked line's debit value and cannot be edited directly while linked; edits must be made on the accounting entry (account_fleet/models/fleet_vehicle_log_services.py:12-13, 25-32).
- Service log vehicle follows the line's vehicle; never blanked by the link (account_fleet/models/fleet_vehicle_log_services.py:17-23).
- Lifecycle gates:
  - Creation of the service log happens only at posting (not in draft) and only for vendor invoices (`in_invoice`), not refunds/receipts, and only for product-type lines (account_fleet/models/account_move.py:17-21).
  - Reset-to-draft then change of vehicle then re-post re-creates the log under the new vehicle; the old vehicle's log is removed (TEST: account_fleet/tests/test_fleet_vehicle_log_services.py:108).
  - Removing the vehicle from a line, or deleting the line, deletes the linked service log (account_fleet/models/account_move.py:54-61); (TEST) line deletion after draft-reset (account_fleet/tests/test_fleet_vehicle_log_services.py:66).
  - Re-posting after price change updates the log cost (TEST: account_fleet/tests/test_fleet_vehicle_log_services.py:52).
- Bill counter on vehicle excludes cancelled entries and counts purchase-type documents only (account_fleet/models/fleet_vehicle.py:19-31).

## C. Validations, automation, security, multi-company
- Blocking rule: a service log tied to a bill line cannot be deleted directly by a user (error), except when triggered by bill-line changes (context bypass) (account_fleet/models/fleet_vehicle_log_services.py:45-50); (TEST) (account_fleet/tests/test_fleet_vehicle_log_services.py:89).
- Direct amount edits on a linked log are rejected (account_fleet/models/fleet_vehicle_log_services.py:25-27).
- Vehicle is designed to become mandatory on vendor bill/refund lines when a per-line "need vehicle" flag is true, but the flag is always false in this module (account_fleet/models/account_move.py:37, 41-42; view requirement at account_fleet/views/account_move_views.xml:11). No other Community module sets the flag (grep across addons root found `need_vehicle` only in account_fleet). Effective behaviour: vehicle is optional in Community.
- Visibility of bill count/list is limited to users in the accounting read-only group; others see zero (account_fleet/models/fleet_vehicle.py:13-17).
- Bridge ships no ACL, groups, or record rules of its own (no security folder). Access and company scoping of service logs and vehicles are owned by fleet (fleet/security/ir.model.access.csv:8,18; fleet/security/fleet_security.xml:62).
- Cleanup deletions of logs are done with elevated rights (account_fleet/models/account_move.py:56,60). Log creation at posting is not elevated (account_fleet/models/account_move.py:26); whether an accountant without fleet rights can post such a bill: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company: no company field added here; log company follows fleet's own vehicle/company rules (fleet/models/fleet_vehicle.py:45). Cross-company mismatch between bill company and vehicle company: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- Accounting (account): owns bill posting, lines, period-transfer wizard; this bridge hooks posting and the wizard (account_fleet/models/account_move.py:9; account_fleet/wizard/account_automatic_entry_wizard.py:6).
- Fleet (fleet): owns vehicle, service types, service logs, driver/cost reporting; receives the auto-created "Vendor Bill" service record (account_fleet/data/fleet_service_type_data.xml:3-6).
- Audit trail: chatter note on the service log referencing the bill (account_fleet/models/account_move.py:23,27-28); cost field is tracked (account_fleet/models/fleet_vehicle_log_services.py:12-13).
- No inventory, approval, or e-invoicing handoff in this module.

## E. Configuration / defaults that change outcomes
- Seeded service type "Vendor Bill", category "service" (account_fleet/data/fleet_service_type_data.xml:3-6). If deleted/archived-away, log creation is silently skipped (account_fleet/models/account_move.py:10-12).
- No settings toggle; no company-level configuration. Behaviour depends only on installing both parent modules.

## F. Effective extension path (module names only)
- On fleet.vehicle: account_fleet, hr_fleet (grep of `_inherit` across addons root).
- On fleet.vehicle.log.services: account_fleet, hr_fleet.
- Dependents/related manifests mentioning the bridge: none found besides itself; stock_fleet and test_discuss_full reference fleet, not account_fleet.
- Extensions of the new line fields (vehicle_id / need_vehicle / vehicle_log_service_ids): none found outside account_fleet.

## G. Not verified
- Access-right outcome for posting users lacking fleet rights: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company vehicle/bill mismatch: UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour when a bill is cancelled (not draft-reset) with logs present: UNKNOWN — EVIDENCE INSUFFICIENT.
- Any rule beyond what is cited above is not asserted as universal.

