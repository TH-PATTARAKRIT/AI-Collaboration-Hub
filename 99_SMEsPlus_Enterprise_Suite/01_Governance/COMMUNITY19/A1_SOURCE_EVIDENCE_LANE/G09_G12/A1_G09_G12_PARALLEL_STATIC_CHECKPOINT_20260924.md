# SMEsPlus Community19 - A1 Parallel Static Checkpoint G09-G12

Date: 2026-09-24
Mode: A1 SOURCE / STATIC EVIDENCE ONLY
Scope: G09 CRM, G10 ACCOUNT_PROCESS, G11 EVENTS, G12 PROJECT_SERVICES
Boss boundary: NO A2 runtime, NO A3, NO MASTER, NO GMVQ/QID answering, NO Formal Coverage.

## 1. Governed scope reconciliation

Controlled Group Structure V2 evidence confirms these group counts:
- G09 CRM = 11 modules
- G10 ACCOUNT_PROCESS = 13 modules
- G11 EVENTS = 8 modules
- G12 PROJECT_SERVICES = 20 modules

The controlled mapping artifact is identified as GROUP_STRUCTURE_V2_CORE.tsv with SHA-256:
203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf

Current repository/library inspection in this run did not expose the row-level TSV itself. Therefore:
- G09 exact 11-name roster: EVIDENCE POINTER KNOWN / ROW MEMBERSHIP NOT YET RETRIEVED
- G10 exact 13-name roster: EVIDENCE POINTER KNOWN / ROW MEMBERSHIP NOT YET RETRIEVED
- G12 exact 20-name roster: EVIDENCE POINTER KNOWN / ROW MEMBERSHIP NOT YET RETRIEVED
- G11 is reconstructable from explicit V2 rule `event* (8)` plus eight LGPL-3 event-family rows in the controlled static registry.

No module name is counted into G09/G10/G12 unless membership is independently evidenced.

## 2. Source anchor status

The authoritative local Community19 source root remains unavailable through the connected desktop path during this checkpoint. To avoid idle time, this run used reproducible public Odoo 19.0 source as a static source anchor only.

Public Odoo 19.0 branch head observed in this run:
25c8ffe566c77be9d078354458d4c77dc449873d

Important boundary: this public branch snapshot is NOT asserted byte-identical to the controlled `Odoo 19.0.post20260921` project source package. Current controlled-source re-anchor remains pending.

## 3. G09 CRM - verified anchor extraction

Anchor module: `crm`.

Manifest / static surface:
- version 1.9, LGPL-3, application module
- direct dependencies: base_setup, sales_team, mail, calendar, resource, utm, web_tour, contacts, digest, phone_validation
- declared security: crm_security.xml + ir.model.access.csv
- declared background/data mechanisms include ir_cron_data.xml, stage/team/lost-reason data, prediction data, recurring plan data, mail subtypes
- static surfaces include lead, stage, team, activity, settings, partner, UTM campaign, reporting, menu and tour views

Core model evidence from `crm.lead`:
- model identity: crm.lead
- inheritance: mail.thread.cc, mail.thread.blacklist, mail.thread.phone, mail.activity.mixin, utm.mixin, format.address.mixin, mail.tracking.duration.mixin
- company control: `_check_company_auto = True`; user_id/team_id/partner_id use check_company where applicable
- lifecycle / state dimensions include lead vs opportunity type, stage_id, active, won_status = won/lost/pending, lost_reason_id
- commercial/data identity includes salesperson, sales team, company, partner/contact, expected revenue, recurring revenue, deadline, probability, UTM source/medium/campaign
- rule: probability constrained to 0..100
- cross-module static handoffs: partner/contact, sales team, calendar meetings, mail/activity, UTM, resource, digest and phone validation

Disposition: A1 STATIC EXTRACTION STARTED. Full G09 11-module roster and per-module extraction remain open.

## 4. G10 ACCOUNT_PROCESS - process-source extraction without owner overclaim

The `account` module is used here as a cross-group process source anchor. This checkpoint does NOT claim that the `account` technical module itself is owned by G10 until the exact V2 roster row is retrieved.

Account manifest static surfaces:
- version 1.4, LGPL-3
- direct dependencies: base_setup, onboarding, product, analytic, portal, digest
- security and ACL declarations present
- process UI/data surfaces include payments, move reversal, unreconcile, resequence, payment register, secure entries, move send, accrued orders, lock exceptions, journals, taxes, bank statements, reconciliation, account moves, analytic, portal and reports
- background/static mechanism: data/service_cron.xml
- post-init hook present

`account.payment` static process evidence:
- model identity: account.payment
- inheritance: mail.thread.main.attachment + mail.activity.mixin
- company control: `_check_company_auto = True`; journal/company/bank/account/partner references carry company checks where applicable
- lifecycle state values: draft, in_process, paid, canceled, rejected
- transaction identity: move_id, journal_id, date, amount, currency, partner, payment method
- process direction: payment_type = inbound/outbound; partner_type = customer/supplier
- reconciliation surfaces: is_reconciled, is_matched, reconciled invoices/bills/statement lines
- internal transfer cross-reference: paired_internal_transfer_payment_id
- control rule: amount >= 0
- accounting handoff: liquidity/counterpart/write-off line classification derives from account.move.line and journal/payment configuration

Disposition: G10 PROCESS STATIC EVIDENCE ADVANCED; exact 13-module owner roster remains unresolved.

## 5. G11 EVENTS - exact 8-module roster reconstruction

Group Structure V2 explicitly moved `event* (8)` into G11 EVENTS. The controlled static registry identifies exactly these eight LGPL-3 event-family modules in that core set:
1. event
2. event_booth
3. event_booth_sale
4. event_crm
5. event_crm_sale
6. event_product
7. event_sale
8. event_sms

The same static registry separately shows `event_sale_iot` and `event_social` as OEEL-1, therefore they are not eligible Community rows.

`event` anchor static evidence:
- version 1.9, LGPL-3
- dependencies: barcodes, base_setup, mail, phone_validation, portal, utm
- declared security + ACL files
- static views cover event, ticket, mail schedule, registration, slots, type, stage, tags, questions/answers, settings, partner and menus
- background mechanism: ir_cron_data.xml

`event.event` model evidence:
- inheritance: mail.thread + mail.activity.mixin
- company/identity: company_id, organizer_id with check_company, responsible user
- lifecycle/state: kanban_state = normal/done/blocked/cancel plus stage_id
- registration rules: seats_max, seats_limited, seats_reserved/used/available/taken, registration_ids
- registration openness is computed from cancellation state, dates, ticket sale availability and seat availability
- event communications: event_mail_ids; language/timezone fields
- event questions, slots and tickets are first-class static relationships
- cross-module static handoffs: mail/activity, portal, UTM, partner, barcode, phone validation; overlay modules bridge CRM, Sales, Product/Accounting and SMS

Disposition: G11 ROSTER RECONCILED AT STATIC LEVEL / DEEP PER-MODULE EXTRACTION STILL OPEN.

## 6. G12 PROJECT_SERVICES - verified project anchor extraction

Anchor module: `project`.

Manifest / static surface:
- version 1.4, LGPL-3, application module
- dependencies: analytic, base_setup, mail, portal, rating, resource, web, web_tour, digest
- declared security: project_security.xml + ir.model.access.csv + ir.model.access.xml
- static surfaces include project, project stage, task, task type, role, tags, milestones, partner, settings, activity plan/type, portal/share, reports and menus
- background mechanism: ir_cron_data.xml
- post-init and uninstall hooks present

`project.task` model evidence:
- identity: project.task
- inheritance: portal.mixin, mail.thread.cc, mail.activity.mixin, rating.mixin, mail.tracking.duration.mixin, html.field.history.mixin
- lifecycle state values: 01_in_progress, 02_changes_requested, 03_approved, 1_done, 1_canceled, 04_waiting_normal
- project stage is separately modeled by project.task.type
- data/identity: project_id, company_id, partner_id, assignees, tags, priority, deadline, allocated hours
- hierarchy: parent_id / child_ids with recursive project/company/partner behavior
- service-delivery controls: milestone_id, task dependencies, recurrence fields, portal access, rating and tracking
- company/tenant-relevant static controls: project and partner domains include company constraints; company_id is propagated/computed
- cross-module static handoffs: analytic, partner, portal, mail/activity, resource, rating and web

Valid prior carry-forward evidence identifies `hr_timesheet`, `sale_project` and `sale_timesheet` as important Project/Service bridge targets, but exact G12 membership for those modules remains CURRENT-SOURCE / ROSTER RE-ANCHOR PENDING in this checkpoint.

Disposition: A1 STATIC EXTRACTION STARTED / exact 20-module roster still open.

## 7. Open evidence gaps and contradictions

1. GROUP_STRUCTURE_V2_CORE.tsv row-level content is not currently exposed through the accessible GitHub/Library paths, despite the controlled SHA-256 pointer being verified.
2. The public Odoo 19.0 source branch used in this run is a reproducible source anchor but may contain commits after the controlled project package date; no byte-equality claim is made.
3. Historical/mixed-source MODULE_MASTER_REGISTER_FULL.csv is SECONDARY EVIDENCE ONLY and is not allowed to substitute for current Community19 controlled source.
4. No runtime reachability, configuration reachability or UI behavior is inferred from source presence.

## 8. Next A1 work

- Retrieve/reconstruct exact row-level G09, G10 and G12 rosters without guessing.
- Deepen all eight G11 modules from manifest into model/security/rule/view/test/dependency maps.
- Continue G09 CRM module family static extraction once exact membership is resolved.
- Continue G10 accounting process overlay extraction while maintaining ACCOUNT_BASE vs ACCOUNT_PROCESS ownership boundaries.
- Continue G12 project/service bridge extraction after exact membership re-anchor.
- Re-anchor every public/static observation to the controlled Community19 source package when authoritative source access returns.

Status: A1 WORK IN PROGRESS / CURRENT-SOURCE RE-ANCHOR PENDING / NO A2 AUTHORIZED.
