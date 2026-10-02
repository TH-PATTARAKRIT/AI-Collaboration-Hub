# U153 Neutral Knowledge — Equipment Maintenance Module

**Unit:** U153 | **Claims:** 22 | **Module Status:** PRESENT

---

## Overview

The equipment maintenance application is a standalone application within the supply chain category. It depends only on the messaging framework module and installs without requiring accounting, manufacturing, or inventory modules. It tracks equipment assets, organises maintenance requests through a configurable pipeline, and computes reliability statistics from historical repair data.

---

## Neutral Claims Reference

| Claim-ID | Neutral Statement |
|----------|-------------------|
| U153-C01 | The equipment maintenance application has a single framework dependency on the messaging module and installs as a self-contained application. |
| U153-C02 | Maintenance pipeline stages are stored in a dedicated model that carries a sequence number, a kanban fold flag, and a completion flag. |
| U153-C03 | A stage is designated as a terminal (done) stage via a Boolean flag, and requests that enter such a stage have their close date automatically set. |
| U153-C04 | The module ships with four default pipeline stages — two open stages and two terminal stages — that are protected from data-update overwrites after installation. |
| U153-C05 | Maintenance requests are built on the full messaging and activity framework, enabling CC chatter and scheduled activity management. |
| U153-C06 | Each maintenance request carries a type classification distinguishing corrective from preventive work. |
| U153-C07 | Maintenance requests carry planned start and end datetimes; the system enforces that the end time may not precede the start time. |
| U153-C08 | The planned duration of a maintenance request is derived automatically from the scheduled start and end times and stored in hours. |
| U153-C09 | Preventive maintenance requests support configurable recurrence with interval, unit, and optional end date, all stored on the request record itself. |
| U153-C10 | Closing a recurring preventive request automatically spawns a copy for the next scheduled occurrence; the new request starts in the first pipeline stage. |
| U153-C11 | The close date on a maintenance request is managed automatically and always reflects whether the current stage is a terminal stage. |
| U153-C12 | Changing the stage of a maintenance request resets the kanban status indicator to the default value unless the caller explicitly overrides it. |
| U153-C13 | Equipment records are chatter-enabled and carry full lifecycle fields including serial number uniqueness enforcement, cost, warranty, and scrap date. |
| U153-C14 | Equipment reliability metrics (mean time between failures, mean time to repair, estimated next failure, and latest failure date) are derived automatically from closed corrective maintenance requests via a shared mixin. |
| U153-C15 | The system computes average repair time and inter-failure interval from historical closed corrective requests; the next failure estimate is a linear projection from the last failure date plus the computed interval. |
| U153-C16 | Maintenance teams support multi-member assignment, aggregate pending request counts (by priority, kanban state, and scheduling status), and allow inbound email to create requests automatically via an alias. |
| U153-C17 | Maintenance teams provide a live dashboard showing counts of open requests broken down by scheduling status, priority, and blocking state. |
| U153-C18 | Access control uses a single manager group; all authenticated users have base access, while the equipment manager group grants full create, write, and delete rights over equipment and stages. |
| U153-C19 | Regular users see only their own maintenance requests (as creator or assigned technician) or records they follow; equipment managers see all records across the company. |
| U153-C20 | All four primary maintenance models enforce company-scoped data isolation via standard multi-company record rules. |
| U153-C21 | Closing or completing maintenance requests produces no financial entries in the Community edition; the equipment cost field is a static reference figure with no accounting integration. |
| U153-C22 | Preventive maintenance request copies are generated synchronously when the parent request is closed — not by any scheduled background process — as no scheduled automation is shipped with this module version. |
