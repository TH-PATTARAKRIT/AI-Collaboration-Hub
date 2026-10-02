# U160 — helpdesk: Customer Support Ticket Lifecycle
**Status:** ABSENT  
**Date:** 2026-10-02  
**Researcher:** DeepSeek STATE03 VDR Worker  
**Source tree:** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/`

---

## Presence Check

Command executed:
```
ls ".../odoo/addons/helpdesk"
```
Result: `No such file or directory`

Secondary scan for related names (`help`, `desk`, `support`, `ticket`) across 693 addons: **no matches**.

The `helpdesk` module is **NOT PRESENT** in the Odoo 19 Community edition addons tree scanned.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U160-C01 | F-ABSENT-01 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk` | directory | ABSENT | MODULE_NOT_FOUND | BLOCKING | The `helpdesk/` directory does not exist in the Community addons tree; the module is not shipped with Odoo 19 Community. | The customer support ticket management add-on directory is absent from the Community edition software package |
| U160-C02 | F-ABSENT-02 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/__manifest__.py` | file | ABSENT | MODULE_NOT_FOUND | BLOCKING | No `__manifest__.py` exists; the helpdesk add-on has no declared Community presence or dependency list. | The add-on descriptor file that would declare the module's dependencies and Community license is absent |
| U160-C03 | F-ABSENT-03 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/models/helpdesk_ticket.py` | file | ABSENT | MODULE_NOT_FOUND | BLOCKING | No `helpdesk.ticket` ORM model is present; fields `team_id`, `user_id`, `stage_id`, `priority`, `sla_ids` cannot be verified in Community. | The ticket data model that would store customer issues, assignee, team, priority, and SLA references is absent |
| U160-C04 | F-ABSENT-04 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/models/helpdesk_sla.py` | file | ABSENT | MODULE_NOT_FOUND | BLOCKING | No `helpdesk.sla` ORM model is present; SLA time constraints, deadline computation, and stage-reached logic cannot be verified. | The service level agreement model that would define response time targets and track whether deadlines are met is absent |
| U160-C05 | F-ABSENT-05 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/models/helpdesk_team.py` | file | ABSENT | MODULE_NOT_FOUND | BLOCKING | No `helpdesk.team` ORM model is present; team-level assignment policies (manual / round-robin / least-active) cannot be verified. | The support team configuration model that would define ticket routing rules and agent assignment strategies is absent |
| U160-C06 | F-ABSENT-06 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/controllers/portal.py` | file | ABSENT | MODULE_NOT_FOUND | INFO | No portal controller exists; customer self-service access to tickets via the website portal cannot be verified in Community. | The web portal controller that would allow customers to submit and track their own support requests through a browser interface is absent |
| U160-C07 | F-ABSENT-07 | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/helpdesk/security/helpdesk_security.xml` | file | ABSENT | MODULE_NOT_FOUND | INFO | No security XML is present; `helpdesk.group_helpdesk_user` and `helpdesk.group_helpdesk_manager` access groups cannot be verified in Community. | The access control definitions that would create role-based permission groups for support agents and managers are absent |

---

## Summary

All 7 claims are ABSENT-class. The helpdesk module — providing customer support ticket lifecycle, SLA enforcement, team-based routing, and portal self-service — is an **Enterprise-only feature** in Odoo 19. It is not present in the Community edition addons tree examined.

**Migration implication:** Any SMEsPlus Enterprise Suite helpdesk requirements must be sourced from the Odoo Enterprise license tier or a third-party Community replacement module.
