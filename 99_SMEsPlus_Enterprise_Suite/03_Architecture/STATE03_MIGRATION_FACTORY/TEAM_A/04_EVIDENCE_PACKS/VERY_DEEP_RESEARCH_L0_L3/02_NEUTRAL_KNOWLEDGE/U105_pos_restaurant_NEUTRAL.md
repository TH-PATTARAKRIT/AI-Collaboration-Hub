# U105 — pos_restaurant: Neutral Knowledge Layer

**Status**: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
**Unit**: U105 — Table and Floor Management for Restaurant Point of Sale (GAP-038)

---

## Overview

The restaurant point-of-sale extension adds a layered spatial model on top of the core point-of-sale module. The fundamental entities are floor plans, tables, and courses. These entities extend the base order and configuration models and are loaded into the client session before any orders begin.

---

## Neutral Reference Index

### NR-U105-001 — Floor Plan Data Model Registration
The restaurant extension introduces a dedicated floor plan entity that participates in the standard session data loading mechanism. This entity is separate from the core point-of-sale models and is only activated when the restaurant module is enabled on a configuration.

### NR-U105-002 — Floor Plan Ordering
Floor plans are presented to operators in a deterministic sequence. The ordering uses a numeric priority field as the primary sort key, falling back to the name when priorities match. This controls the left-to-right tab order shown on the restaurant interface.

### NR-U105-003 — Floor Plan to Terminal Association
A floor plan can be shared across multiple point-of-sale terminals within a single deployment. The association is a many-to-many link that is constrained to terminals that have the restaurant module active, preventing non-restaurant terminals from being associated.

### NR-U105-004 — Floor Plan to Table Composition
Each floor plan acts as a container for its tables. The tables are owned by the floor and are accessible as a collection from the floor record. Deleting a floor deactivates rather than deletes its tables.

### NR-U105-005 — Floor Background Imagery
Floor plans support an optional background image that is stored as a binary object. When present, the image is used as the canvas background for the visual floor editor, and table positioning is not constrained to the alignment grid. A separate background color field is available as a fallback when no image is provided.

### NR-U105-006 — Session-Scoped Floor Loading
At session startup only the floor plans assigned to the current terminal are loaded into the client. This domain restriction prevents a terminal from displaying or editing floors that belong to other terminals in a multi-terminal restaurant installation.

### NR-U105-007 — Delete Protection During Active Sessions
Floors cannot be removed while any associated terminal has an open session. The system checks for open sessions across all restaurant-enabled terminals linked to the floor and presents a descriptive error naming the specific floor and session combination that blocks the deletion.

### NR-U105-008 — Write Protection During Active Sessions
Structural modifications to the floor configuration, specifically reassigning it to different terminals or deactivating it, are blocked while an active session exists. This prevents in-flight orders from referencing a floor that has just been detached from their terminal.

### NR-U105-009 — Server-Side Floor Creation from Client
The restaurant interface supports creating a new floor from within an active session without reloading. A server method accepts the floor name, color, and terminal identifier, creates the floor record, and returns just the fields needed by the client to render the new floor tab immediately.

### NR-U105-010 — Guarded Floor Deactivation
The deactivation path for a floor checks for draft orders on any of its tables before proceeding. If draft orders exist the operation is refused. If the floor is clear all its child tables are also deactivated in the same operation.

### NR-U105-011 — Table Data Model Registration
Restaurant tables are a distinct entity that also participates in session pre-loading. Like floors, they are only loaded when the restaurant module is active on the terminal.

### NR-U105-012 — Table Number as Display Identifier
Each table carries an integer display number that appears on the floor plan tile. The number is required and defaults to zero. Together with the floor name it forms the human-readable table identifier shown in order management screens.

### NR-U105-013 — Table Shape for Visual Rendering
Tables have a shape attribute restricted to square or round. This is used by the floor plan renderer to draw the correct geometric shape for each table, not to affect any business logic. Both shapes support the same dragging, resizing, and ordering behavior.

### NR-U105-014 — Table Pixel Coordinates
Each table stores its position as floating-point horizontal and vertical pixel offsets from the top-left of the floor canvas. These coordinates are updated by the client when the operator drags or resizes a table and written back to the server in real time.

### NR-U105-015 — Self-Referential Table Merging
Tables can be grouped by linking one table as the parent of another. A child table delegates order lookup to its parent and its visual position is derived from its attachment side relative to the parent rather than from its own stored coordinates. The merge relationship is stored as a single nullable parent reference on the child table.

### NR-U105-016 — Table Delete Protection for Draft Orders
Before a table is removed the system counts any draft orders assigned to that table and raises an error if the count is above zero. This applies both to the backend administration and to the in-session delete flow initiated from the floor editor.

### NR-U105-017 — Table Merge Cycle Prevention
When a waiter links one table to another by dragging the server validates the proposed parent assignment for circular references. If accepting the parent would create a cycle the assignment is reverted to the previous parent value, preserving a valid tree structure.

### NR-U105-018 — Order to Table Foreign Key
The core order model is extended with a nullable table reference. The index is a partial non-null index, meaning only orders that have a table assigned are indexed, avoiding index bloat from the majority of standard retail orders that have no table.

### NR-U105-019 — Order Guest Count
The order model stores the number of guests served, which is populated automatically from the table seat count when the order is created. The guest count is displayed as a per-guest amount in the number pad feedback and drives the amount-per-guest calculation.

### NR-U105-020 — Order Course Collection
Orders in the restaurant extension carry a collection of course records. These are loaded as part of the order read response rather than independently, so an order's courses are always available alongside the order data.

### NR-U105-021 — Concurrent Waiter Order Resolution on Server
When two waiters on separate devices submit changes for the same table simultaneously the server-side order lookup expands its match criteria. Instead of matching only the order UUID it also accepts any draft order with the same table and terminal, ensuring both device submissions land on a single canonical order record rather than creating duplicates.

### NR-U105-022 — Course Fired State and Timestamp
Each course has a boolean state that transitions irreversibly from unfired to fired when the waiter dispatches it to the kitchen. At the moment of firing the current date and time is stamped on the record automatically, whether the fired flag is set at creation or through a later write.

### NR-U105-023 — Course UUID for Offline Stability
Courses carry a universally unique identifier generated at creation. This allows the client to reference a course before it has been persisted to the server and to reconcile local and server representations without relying on the database integer primary key.

### NR-U105-024 — Course Sequence Index
The display and processing order of courses within an order is determined by an integer index. The index starts at zero and is incremented by the client when new courses are added. Before displaying courses to the operator the client sorts them by this index.

### NR-U105-025 — Course to Line Membership
Order lines are members of at most one course at a time. Membership is stored as a nullable reference on the line pointing back to the course. Deleting a course sets the reference on its former lines to null rather than deleting the lines, preserving the items on the order.

### NR-U105-026 — Automatic Fired Timestamp on Bulk Create
When courses are created in bulk through the multi-create path the fired timestamp is populated automatically for any record that already has the fired flag set in the creation payload, ensuring data integrity without requiring callers to also supply the timestamp.

### NR-U105-027 — Order Line Course Reference with Null on Delete
The order line model stores its course membership as a nullable relation. The deletion behavior is set to null, which means removing a course releases the lines from the course grouping but does not remove the lines from the order.

### NR-U105-028 — Three Additional Models Loaded at Session Start
When the restaurant module is active the session data loader appends the floor plan, table, and course models to the list of models whose data is fetched before the session becomes operational. All three sets of records are available on the client before any waiter interaction.

### NR-U105-029 — Preparation Change Snapshot After Payment
After an order is paid a utility on the session rebuilds the stored preparation snapshot by re-reading all order lines. The snapshot records each line by its UUID with the product reference, displayed name, internal note, quantity, and attribute values, providing a baseline for detecting subsequent changes if the order needs to be reopened.

### NR-U105-030 — Bill Splitting Feature Toggle
A dedicated boolean toggle on the point-of-sale configuration controls whether the bill-splitting workflow is available to waiters. When disabled the split bill screen and its navigation entry points are hidden.

### NR-U105-031 — Floor Assignment on Configuration
The configuration model holds the set of floor plans assigned to the terminal. The copy flag is disabled on this relation so duplicating a configuration does not copy floor assignments, requiring explicit floor assignment for any new terminal.

### NR-U105-032 — Configurable Default Landing Screen
Operators can choose whether opening the session lands on the floor plan view or the register view. This accommodates both full-service table restaurants and counter-service bars that happen to use the restaurant module.

### NR-U105-033 — Automatic Default Floor on Restaurant Setup
Creating a new restaurant configuration that has no floors triggers automatic creation of a default floor named after the company, containing one starter table. This ensures the floor plan editor is immediately operable without additional setup steps.

### NR-U105-034 — Client-Side Table Status Indicators
Each table in the client stores a small state object with the initial position for drag revert, the number of active orders, and the number of pending kitchen changes. These are updated by the device synchronisation layer whenever new order data arrives, driving the colored status indicators on the floor map.

### NR-U105-035 — Recursive Parent Resolution for Merged Tables
When a table is a child of another the client resolves the topmost ancestor by walking the parent chain recursively. The resolved root table is the one used for order lookup, navigation, and display, hiding the intermediate merge relationships from the waiter.

### NR-U105-036 — Derived Pixel Coordinates for Child Tables
The visual coordinates of a child table are not stored directly but computed from the parent position and attachment side each time they are needed. Left attachment places the child immediately to the right of the parent; right attachment places it to the left. This keeps child positions consistent when the parent is moved.

### NR-U105-037 — Order Inclusion During Tipping State
The table order collection includes orders that are in the tipping screen state even after they have been finalised, so the floor map continues to show a table as occupied while the tip is being entered by the customer.

### NR-U105-038 — Grid Snap in Edit Mode
When the floor editor is active and no background image is present table positions are snapped to a ten-pixel grid during drag and resize operations. The snap is applied by rounding the computed coordinate modulo the grid size before storing, not during rendering.

### NR-U105-039 — Order Merge Triggered by Table Drag-Link
When a waiter drags one table onto another after holding for the link delay threshold the floor screen triggers an order merge from the source table to the destination before recording the parent relationship on the server. This ensures the orders are consolidated before the tables are visually joined.

### NR-U105-040 — Direct Background Image Write on Upload
Uploading a floor background image writes the base64 binary content directly to the server floor record through the standard ORM write path, then reads the record back to synchronise the client with the server-confirmed image, avoiding a stale local copy.

### NR-U105-041 — Split Order Alphabetic Suffix Naming
When a bill is split the new order receives a name derived from the original by appending a letter suffix. The first split produces suffix B, and each subsequent split of the same original increments the trailing letter. Splitting is limited to twenty-six parts before the naming algorithm raises an error.

### NR-U105-042 — Course Continuity Through Bill Split
During a bill split the system preserves course groupings for transferred lines. Lines that belong to a course are moved to a course in the new order that matches by course index. When no matching index exists in the destination a new course is created there with the same index.

### NR-U105-043 — Single-Execution Guard on Split
A device-local flag on the order prevents the split operation from being triggered twice concurrently on the same order. The flag is set at entry and cleared in a finalisation block regardless of success or failure.

### NR-U105-044 — Auto-Fire First Course on Send to Kitchen
When a waiter submits an order for preparation the system identifies the first unfired course and marks it as fired before invoking the parent send logic. This ensures the course state accurately reflects that the items have been dispatched to the kitchen.

### NR-U105-045 — Retroactive Line Assignment on First Course Creation
When the first course is created on an order that already has lines those existing lines are all assigned to the new first course. A second empty course is created immediately and becomes the selected course, ensuring lines added after course creation flow into a fresh course rather than the one already containing existing items.

### NR-U105-046 — Course Fire Workflow
Firing a course marks it as fired and immediately triggers a preparation send with a reference to the fired course, prints a course ticket whose title identifies the course number, and deselects the course so the interface moves focus to the next pending course.

### NR-U105-047 — Course Reconciliation During Order Merge
When two table orders are merged the course records are reconciled by index. Where both orders have a course with the same index all lines from the source course are reassigned to the destination course. A restoration map is stored in the destination order UI state recording the original course assignments so the merge can be undone if the tables are later unlinked.

### NR-U105-048 — Concurrent Waiter Conflict Resolution on Client
After each real-time data synchronisation the client device checks whether any table has more than one non-finalised unsynced order. When a collision is detected all lines from the duplicate orders are migrated into a single canonical order, and the duplicates are deleted to return the table to a single-order state.

### NR-U105-049 — Table Selection and Order Reuse
Selecting a table first fetches fresh server data, then looks for an existing open order on the table to resume. If none exists the system searches for an empty local order without a table or floating name and assigns it to the table rather than always creating a new record.

### NR-U105-050 — Per-Category Kitchen Notification
When an order is sent to the kitchen the restaurant extension tallies the changes by preparation category and shows a confirmation notification listing each category with its item count. This gives the waiter immediate feedback confirming which kitchen stations received items.

### NR-U105-051 — Course Cleanup Before Preparation Send
Before transmitting an order to preparation all empty courses that have not been fired are removed from the order. The remaining courses are then re-numbered from one in sequence to keep the index contiguous.

### NR-U105-052 — Stable Course Sort for Display
The courses on an order are sorted by index on every access through the courses computed property. This means that regardless of the order in which courses were created or merged, the waiter always sees them in ascending course number order.

### NR-U105-053 — Course-Based Grouping on Preparation Ticket
The preparation ticket grouping logic is extended so that when an order line belongs to a course, the course index and name are used as the group header rather than the product category. This causes the printed or displayed preparation ticket to be organised by course sequence rather than by product type.

### NR-U105-054 — Guest Count Prompt via Preset
The order preset model gains a guest flag that when set causes the guest count dialog to appear automatically when a waiter selects a table under that preset. This ensures guest counts are captured at the start of service rather than optionally later.

### NR-U105-055 — Floor Field Protected During Open Session
The floor assignment field on the point-of-sale configuration is added to the forbidden-change list alongside other structural fields. Any attempt to reassign floors while a session is open is blocked by the existing session guard mechanism rather than a floor-specific check.

---

*End of Neutral Knowledge Layer — U105*
