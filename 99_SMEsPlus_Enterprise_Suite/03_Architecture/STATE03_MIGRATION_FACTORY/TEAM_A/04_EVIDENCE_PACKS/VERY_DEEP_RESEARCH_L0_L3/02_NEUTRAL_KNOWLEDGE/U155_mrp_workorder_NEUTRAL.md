# U155 Neutral Knowledge — Work Order Lifecycle in Manufacturing

**Unit:** U155 | **G Group:** G07 | **Priority:** P2  
**Date:** 2026-10-02

---

## Overview

A work order (sometimes called a work centre operation) is a discrete production task that must be executed at a named physical or virtual work centre. Work orders belong to a manufacturing order and collectively describe how a finished product is produced step by step. The community edition of this manufacturing platform bundles work order management directly inside the core manufacturing module rather than providing it as a separately installable extension.

---

## Neutral References by Claim

**C01 — Standalone extension is absent**  
In the community edition the work order feature is not packaged as an independent installable extension. No separate directory exists for such a package. The work order model and its supporting views are embedded in the base manufacturing module.

**C02 — Module bundling rather than dependency**  
The core manufacturing module declares dependencies only on the product catalogue, inventory, and resource calendar modules. There is no reference to a separate work order extension in its dependency list because the work order model is delivered from within the same module.

**C03 — Views included in core module**  
The manufacturing module includes dedicated view files and report templates for work orders, confirming that the user interface for managing work orders is part of the standard community installation without any additional package.

**C04 — Work order record structure**  
Each work order is an independent database record linked to its parent manufacturing order. Records are displayed and sorted by their sequence number, scheduled calendar slot, planned start date, and internal identifier.

**C05 — Work centre assignment**  
Every work order must be assigned to exactly one work centre. The assignment drives calendar-based scheduling by reserving a slot in the work centre's resource calendar. The assignment is mandatory and subject to same-company rules.

**C06 — Five-state lifecycle**  
A work order progresses through five possible states during its life: waiting (blocked by a predecessor), ready to begin, in progress, finished, or cancelled. The initial state when a work order is created is ready to begin.

**C07 — Automatic blocked versus ready transitions**  
The system automatically moves a work order between the waiting and ready states based on whether the quantity available to process is greater than zero. This quantity depends on how much has been produced by predecessor work orders in the same chain.

**C08 — Time tracking via productivity records**  
Actual time spent on a work order is stored as a series of individual time log records. Each log record captures who worked, when they started and stopped, the duration, and why time was spent (the category of productive or non-productive activity).

**C09 — Actual versus expected duration**  
The system computes a real duration by summing all completed time log intervals grouped by activity category. It also computes a duration per unit of output and a percentage deviation comparing actual against expected time, providing an efficiency indicator.

**C10 — Starting a work order opens a timer**  
When a user starts a work order a new open-ended time log record is created immediately, capturing the start time and the identity of the user. The work order state advances to in progress. A calendar slot is reserved for the work centre if one does not already exist.

**C11 — Finishing a work order closes all timers**  
When a work order is finished all open time log records are closed with the current time. The work order state advances to finished, the actual quantity produced is recorded, and the hourly cost of the work centre is captured at the moment of completion so that cost reporting remains consistent even if the rate changes later.

**C12 — Productive versus performance time classification**  
Time log records are automatically classified as productive when total duration does not exceed the expected duration. When a work order runs over its expected time the excess is classified under a performance loss category, distinguishing efficient operation from reduced-speed operation.

**C13 — Productivity log record structure**  
Each time log record stores the work centre, the work order, the user, a loss reason, a start timestamp, an end timestamp, and a computed duration. Duration is derived from the difference between start and end times, adjusted for the work centre's productivity conversion rules.

**C14 — Closing open timers at work order end**  
When a work order finishes, the system closes any still-open time log records by writing the current time as the end time. If the total duration already exceeds the expected amount, the excess portion is separated into a distinct performance record to maintain accurate categorisation.

**C15 — Work orders block manufacturing order closure**  
A manufacturing order cannot advance to the stage where it is ready to close until every associated work order has reached either the finished or the cancelled state. Any work order still waiting, ready, or in progress prevents the manufacturing order from proceeding.

**C16 — Automatic work order creation from bill of materials**  
When a manufacturing order is in draft state, the system reads the operations defined on the bill of materials and creates a corresponding work order for each one. Each work order inherits the operation name, work centre, and sequence from the bill of materials definition.

**C17 — Sequential or dependency-based chaining**  
Work orders can be chained in two ways. When a bill of materials is configured for simple sequencing, each work order automatically waits for the one before it to finish. When dependency-based mode is active, each work order reads the explicit predecessor relationships defined on the bill of materials operations and replicates those relationships between the resulting work orders.

**C18 — Calendar-aware scheduling with alternative work centres**  
The planning algorithm checks the assigned work centre's calendar for the first available time slot. It also evaluates any alternative work centres and selects whichever offers the earliest finish time. The chosen slot is recorded as a calendar leave entry so it appears in scheduling views.

**C19 — Expected duration formula**  
The expected duration for a work order accounts for work centre setup time, cleanup time, the number of production cycles needed for the requested quantity, the operation's cycle time per unit, and the work centre's time efficiency percentage. Alternative work centres use the same formula recalculated with their own capacity and efficiency values.

**C20 — Scheduling conflict detection**  
The system can identify work orders that have overlapping planned time intervals at the same work centre. This is evaluated by comparing date ranges across all non-completed work orders at the same location and displaying a visual warning when overlaps are found.

**C21 — Cyclic dependency prevention**  
Work orders may not be arranged in a circular dependency chain. Attempting to create a cycle raises an error. Dependencies are stored in a many-to-many relationship table with two directions: which work orders are blocking this one, and which work orders this one is blocking.

**C22 — Progressive quantity propagation through the chain**  
The quantity that a work order is ready to process is limited to the minimum quantity already produced by all its predecessors. This enables continuous flow production where downstream work orders can begin as soon as any upstream quantity becomes available, rather than waiting for the full batch.

---

## Terminology Bridge

| Technical name | Plain description |
|---|---|
| mrp.workorder | Individual work order record inside a manufacturing order |
| mrp.workcenter | A physical or virtual production station with a defined calendar and cost |
| mrp.workcenter.productivity | A single time log record for a period of activity at a work centre |
| resource.calendar.leaves | A calendar slot reservation blocking time at a work centre |
| blocked_by_workorder_ids | The set of work orders that must complete before this one can begin |
| loss_id / loss_type | Classification of time as productive, reduced-speed, or blocked |
| duration_expected | The planned duration in minutes, derived from the operation and work centre parameters |
| qty_ready | The quantity this work order is currently able to process given predecessor progress |
