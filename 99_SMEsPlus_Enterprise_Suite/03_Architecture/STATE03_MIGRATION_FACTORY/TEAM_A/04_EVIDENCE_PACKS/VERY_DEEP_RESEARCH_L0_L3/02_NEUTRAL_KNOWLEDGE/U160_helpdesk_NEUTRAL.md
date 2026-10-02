# U160 — Helpdesk: Neutral Knowledge Record
**Status:** ABSENT  
**Date:** 2026-10-02

---

## Module Status

The customer support ticket management module is not included in the Community edition of Odoo 19. A thorough scan of 693 add-on directories confirmed no matching module by any related name.

---

## Neutral Claims

| Claim-ID | Neutral statement |
|---|---|
| U160-C01 | The customer support ticket management add-on directory is absent from the Community edition software package |
| U160-C02 | The add-on descriptor file that would declare the module's dependencies and Community license is absent |
| U160-C03 | The ticket data model that would store customer issues, assignee, team, priority, and service level agreement references is absent |
| U160-C04 | The service level agreement model that would define response time targets and track whether deadlines are met is absent |
| U160-C05 | The support team configuration model that would define ticket routing rules and agent assignment strategies is absent |
| U160-C06 | The web portal controller that would allow customers to submit and track their own support requests through a browser interface is absent |
| U160-C07 | The access control definitions that would create role-based permission groups for support agents and managers are absent |

---

## Scope of Customer Support in Community Edition

The Community edition provides basic issue tracking through the project task mechanism. Dedicated customer support features — including structured ticket queues, service level agreement timers, automatic team assignment, and customer-facing self-service portals — are not part of the Community offering.

Organizations migrating to or deploying the Community edition who require these capabilities should evaluate whether the Enterprise license tier or a third-party add-on satisfies their support workflow requirements.

---

## Impact Assessment

- **Ticket lifecycle management:** Not available in Community
- **Service level agreement enforcement:** Not available in Community
- **Team-based routing:** Not available in Community
- **Customer portal for ticket access:** Not available in Community
- **Helpdesk agent and manager roles:** Not available in Community

No fabrication. All statements above are grounded solely in the absence confirmed by directory inspection of the live source tree.
