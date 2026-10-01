# U14 — Manufacturing Core — Neutral Knowledge (clean-room layer)

> Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`
> Source product basis: Odoo 19 Community (named here once, in the header only).
> This file states what a manufacturing capability must do and why, in business language: recipes (bills of materials) and kits, work centers and operations, manufacturing orders and their lifecycle, component reservation, consumption and completion, backorders, scrap and unbuild, replenishment for manufacturing, and cost inputs. It contains no source paths, object names, field names or code.

Section key: WHAT, WHY, BUSINESS RULE, STATE, OPTIONALITY, DEPENDENCY, CONSTRAINT, RISK, UNKNOWN. Each statement carries an identifier of the form N-U14-nnn that is referenced from the restricted technical evidence file.

## CAP-U14-01 Bill of materials definition, kinds and lookup (neutral)

### WHAT
- [N-U14-001] A bill of materials is the master recipe for a finished product: the components and quantities consumed to make a stated quantity, optionally also operations, residual by-products and planning parameters such as manufacturing lead time. It may be shared by all companies or belong to one.
- [N-U14-002] A bill of materials is either a manufacturing recipe or a kit. A manufacturing recipe is made through a manufacturing order; a kit is a bundle that is never produced and is replaced by its components wherever it is sold, moved or procured. Only manufacturing recipes can be used on a manufacturing order.
- [N-U14-003] The available, incoming, outgoing and forecast quantities of a kit are derived from its components: the number of complete kits the scarcest component allows, in whole kits only; services and non-stocked components are ignored.

### WHY
- [N-U14-004] One master definition lets orders, procurement, cost estimates and availability forecasts use the same component list so that real consumption can be compared with the intended recipe.
- [N-U14-005] Kits let a business sell, buy or move a bundle as one item while stock is tracked only on its components.

### BUSINESS RULE
- [N-U14-006] A bill of materials applies to a goods product. It may be restricted to a single variant; otherwise it applies to every variant of the product. A variant-specific bill of materials cannot be combined with lines limited to chosen attribute values.
- [N-U14-007] To find the bill of materials for a product the system considers only active ones valid for the company or shared across companies; services never have one; if an operation type is given the bill of materials must match it or leave it open. A variant-specific bill of materials wins over one for the whole product, then the sequence number decides.
- [N-U14-008] Expanding a bill of materials multiplies component quantities by the number of recipe repetitions needed, converts units, skips lines that do not apply to the variant, and rounds each component quantity up to a whole unit of measure. Only kit sub-assemblies are expanded further; a sub-assembly that is itself manufactured remains one component line.
- [N-U14-009] A component line may have zero quantity to mark an optional component; component lines may be goods or services, and a line may be tied to the operation in which it is consumed.
- [N-U14-010] By-products carry a cost share percentage of the production cost. A by-product may not be the finished product itself, its share may not be negative, and for any variant the shares of all by-products with a quantity may not total more than one hundred percent.
- [N-U14-011] A bill of materials may not create a cycle in which a product directly or indirectly consumes itself.
- [N-U14-012] When a kit appears on a stock movement, a procurement or a completed movement, it is replaced by one movement or procurement per component scaled by the kit recipe quantity; the kit itself is never reserved.
- [N-U14-013] Stock quantities cannot be adjusted directly on a kit product; the components must be adjusted instead.
- [N-U14-014] Each bill of materials carries a consumption policy (allowed, allowed with warning, blocked) that defaults to allowed with warning, a readiness policy (all components available, or only those of the first operation), a manufacturing lead time and a days-to-prepare delay, all copied or used when orders are created.
- [N-U14-015] A bill of materials may define a batch size; orders generated automatically for the product are then split into batches of that size, and a configured batch size must be positive.

### STATE
- [N-U14-016] When the components, by-products, product or quantity of a bill of materials change, draft and confirmed orders that use it are flagged as outdated so planners can refresh them. Copying a bill of materials re-links its operations, and files attached to a bill of materials are stored on the product.
- [N-U14-017] Archiving or restoring a product archives or restores its bills of materials, and archiving a bill of materials archives its operations. Archiving a product that is still a component of an active bill of materials is allowed with a warning.

### OPTIONALITY
- [N-U14-018] By-products, work-order operations and operation dependencies are optional features enabled by company-wide settings that grant visibility to a group of users. In the reviewed configuration the by-product, work-order, unlocked-order and allocation-report options are switched on for all internal users while operation dependencies are off.
- [N-U14-019] A third kind of bill of materials, subcontracting, exists only when the subcontracting capability is installed; it cannot carry operations or by-products. In the reviewed configuration that capability is installed.

### DEPENDENCY
- [N-U14-020] When the project integration is installed a bill of materials can reference a project, which orders made from it inherit.

### CONSTRAINT
- [N-U14-021] The quantity produced by a bill of materials must be strictly positive.
- [N-U14-022] A product with a kit bill of materials cannot have a reordering rule, and a product with a reordering rule cannot be given a kit bill of materials.
- [N-U14-023] A bill of materials with unfinished manufacturing orders cannot be deleted, and a bill of materials cannot be created by typing a name into a selection box.
- [N-U14-024] Manufacturing users may read bills of materials, their lines and by-products; manufacturing administrators have full control; stock users and project users may only read them.
- [N-U14-025] Users see bills of materials, work centers, operations, orders, work orders and unbuild orders only for the companies they are allowed to work in; bills of materials, operations and work centers that belong to no company are visible to all.

### RISK
- [N-U14-026] A manufactured sub-assembly is not flattened into its parent's order. It is demanded as a component and only produces its own order through replenishment or make-to-order rules, so having a bill of materials for the sub-assembly does not by itself guarantee a cascade of orders, although cost and availability overviews do show the nested structure.
- [N-U14-027] Editing the structure of a kit that has already been used on stock movements can make history inconsistent; the system only warns and recommends archiving and recreating.

### UNKNOWN
- [N-U14-028] How lines limited to never-variant attribute values behave in real orders and procurements has not been exercised.

## CAP-U14-02 Work centers, operations and productivity losses (neutral)

### WHAT
- [N-U14-029] A work center is a machine, line or team that performs operations. It has a working calendar, a time efficiency percentage, setup and cleanup times, an hourly cost, optional capacity per product, optional alternative work centers and live statistics such as equipment effectiveness.
- [N-U14-030] An operation is one step of a bill of materials performed at a work center, with a duration that is either fixed or derived from history, a cost basis, and optional dependencies on other operations of the same bill of materials.
- [N-U14-031] Productivity-loss reasons classify logged time as productive, performance loss, availability loss or quality loss. A standard set of seven reasons is delivered, and only some of them can be chosen manually when blocking a work center.

### WHY
- [N-U14-032] Work centers and operations let the business plan capacity, estimate duration and cost of production steps, and measure how much of the available time is productive.

### BUSINESS RULE
- [N-U14-033] The duration of an operation equals setup plus cleanup plus the number of cycles times the time per cycle, divided by the work center efficiency; the number of cycles is the quantity divided by the capacity, rounded up. Capacity and setup times come from a product-specific capacity entry when one exists, otherwise from the work center. In computed mode the time per cycle is the average of the most recent finished work orders, falling back to the entered value when there is no history.
- [N-U14-034] The cost of an operation is its duration in hours times the hourly cost of the work center. Each operation states whether its cost is based on actual tracked time or on estimated time.
- [N-U14-035] Equipment effectiveness is productive time divided by productive plus non-productive time over the last month, with a configurable target defaulting to ninety percent.
- [N-U14-036] When scheduling, the system looks for the first free slot in the work center calendar in two-week windows, up to a configurable number of windows (fifty by default, about seven hundred days), avoiding time already taken by other work orders, and reports that no slot exists if none is found.
- [N-U14-037] Blocking or lost time on a work center that has a calendar is measured in calendar working hours; productive time is measured in elapsed minutes.

### STATE
- [N-U14-038] A work center is normal when no time is being logged, in progress when productive or performance time is open, and blocked when non-productive time is open; it stays blocked until someone unblocks it, which closes all open time logs.
- [N-U14-039] Changing, adding or archiving an operation flags affected draft and confirmed orders as outdated. Archiving an operation detaches it from the component and by-product lines that referenced it, and archived operations are ignored when orders are built.

### OPTIONALITY
- [N-U14-040] Work-order operations and operation dependencies are optional features. Switching operations off deactivates all of them; switching them on again reactivates the most recently changed ones; switching dependencies off clears the dependency permission on every bill of materials.

### DEPENDENCY
- [N-U14-041] Posting labour cost to accounts and analytic accounts is not part of this capability; it comes from the manufacturing accounting capability, which adds an expense account to the work center.
- [N-U14-042] The community manufacturing capability has no employee-specific costing or permission to work at a work center; any employee-based cost is an extension point only.

### CONSTRAINT
- [N-U14-043] A work center cannot be its own alternative; a capacity entry cannot be negative and must be unique per work center, product and unit; operation dependencies cannot form a cycle; the same user cannot have two open time logs on one work order.
- [N-U14-044] At least one productive reason and one performance reason must exist, otherwise logging time or closing an under-performing time log fails.
- [N-U14-045] Manufacturing users may read work centers, operations, capacities, tags and loss reasons and may freely record time logs; manufacturing administrators have full control of that master data.

### RISK
- [N-U14-046] Archiving a work center that is still referenced by active bills of materials does not stop operations from being planned on it; only a warning is shown.

### UNKNOWN
- [N-U14-047] Computed operation durations and calendar slot search with real history and real leaves have not been exercised because the reviewed environment holds no work orders.

## CAP-U14-03 Manufacturing order creation, confirmation and lifecycle (neutral)

### WHAT
- [N-U14-048] A manufacturing order instructs production of a quantity of a product. It lists the components to consume, the product and any by-products to output, optional work orders, planned dates, a responsible person, locations, a priority and a consumption policy. It is numbered from the sequence of its operation type.
- [N-U14-049] Every manufacturing order belongs to a production group that links it to its backorders and, as parent or child, to other orders that supply or consume its output; each order and its movements also carry a reference record so they can be traced together.

### WHY
- [N-U14-050] The order is the single document where planning, component reservation, execution, consumption and traceability of one production run are tied together.

### BUSINESS RULE
- [N-U14-051] While an order is in draft, its product, quantity, unit, bill of materials, components, by-product lines and operations are derived from the bill of materials, which must be a manufacturing recipe of the order's company; components and operations may still be edited by hand, and an order without a bill of materials has quantity one and free components.
- [N-U14-052] A new order starts now and ends one hour later by default; its end date is the start plus the bill of materials manufacturing lead time, or, when that is zero, the start plus the planned operation minutes, or sixty minutes.
- [N-U14-053] The order reference comes from the number sequence of its operation type and is unique within a company.
- [N-U14-054] Confirming an order checks company consistency, copies the consumption policy from the bill of materials, converts serial-tracked products to their own unit, sets the procurement method of each component, confirms component and product movements and work orders, triggers replenishment for components forecast to be short, confirms linked transfers and marks the order confirmed. An order without a bill of materials keeps the permissive consumption policy. Warehouse manufacturing rules cannot be generated for a company that has no production location.
- [N-U14-055] After draft the product cannot change; the start date cannot be moved once the order is done or cancelled, and moving it un-plans a planned order; changing the operation type issues a new number and re-reserves components; components or operations added after confirmation are confirmed automatically.
- [N-U14-056] The quantity to produce can be changed after confirmation: component quantities are scaled by the ratio of new to old quantity and rounded up, product and by-product quantities are adjusted (as separate extra movements when they already feed downstream documents), operation durations are re-estimated and replenishment is re-run.
- [N-U14-057] A confirmed order whose bill of materials changed is flagged outdated and can be refreshed from it, preserving started or finished operations; a new bill of materials can also be generated from an order by managers and is linked back to it.
- [N-U14-058] By-product quantities on an order scale with the produced quantity; their cost shares may not be negative and may not total more than one hundred percent, and a by-product cannot be the order's own product.
- [N-U14-059] A done order cannot be cancelled. Cancelling cancels unfinished operations and movements and linked transfers that feed nothing else, warns responsible users of affected upstream and downstream documents, and, if the consumption policy is permissive and some components were already consumed, leaves the order done instead of cancelled. Only cancelled orders can be deleted.
- [N-U14-060] New orders are locked unless the user belongs to the unlocked-by-default option; a done order is locked. While locked, quantities cannot be edited freely; unlocking a done order allows corrections of the produced quantity.
- [N-U14-061] Components are reserved first for orders with the highest priority; completing an order resets its priority to normal.
- [N-U14-062] Each state change of an order is recorded in its discussion thread with a dedicated message type, and orders created by replenishment note their origin.
- [N-U14-063] A daily background replenishment run, owned by inventory, is what creates and confirms orders automatically from reordering rules; manufacturing owns no scheduled job of its own and no automation rules exist.

### STATE
- [N-U14-064] An order moves through draft, confirmed, in progress, to close, done and cancelled. It is in progress as soon as anything is produced, consumed or an operation starts; it is to close when all operations are finished or the planned quantity is registered; it is done when all its movements are finished; it is cancelled when all its product movements are cancelled.

### OPTIONALITY
- [N-U14-065] The operation type governs order numbering, default locations, backorder behaviour, creation of new component lots and printing; in the reviewed configuration the single active manufacturing type asks about backorders, reserves at confirmation and does not allow creating component lots.

### DEPENDENCY
- [N-U14-066] With the project integration, bills of materials and orders carry a project; an order made from a sale order or from a bill of materials inherits it through the replenishment values, and project users can see the related counts and read bills of materials.
- [N-U14-067] The sale-project manufacturing module delivers no behaviour of its own; it only installs automatically when projects, sales and manufacturing are all present.

### CONSTRAINT
- [N-U14-068] Order references are unique per company, quantities to produce must be positive, and a lot-tracked product allows only one producing lot per order.
- [N-U14-069] Manufacturing users have full control of orders and may create and read production groups; stock users may read orders; managers inherit the user rights.

### RISK
- [N-U14-070] The lock on an order is not role-protected: anyone with write access can unlock it, so it is a guard against accidents rather than an approval control.
- [N-U14-071] Project inheritance for orders created to supply a parent order relies on a legacy link that is no longer populated, so such child orders may not receive the project of their parent.

### UNKNOWN
- [N-U14-072] The complete order lifecycle was not executed because the reviewed environment holds no orders.

## CAP-U14-04 Component reservation, readiness and multi-step manufacturing (neutral)

### WHAT
- [N-U14-073] Reservation sets aside available stock for the components of a manufacturing order. The order shows a readiness status of waiting, ready, or waiting for another operation, derived from the state of its component movements.
- [N-U14-074] A warehouse can manufacture in one step (consume from stock and produce into stock), two steps (first a transfer that picks components into a pre-production area) or three steps (also a transfer that stores the finished product from a post-production area).

### WHY
- [N-U14-075] Extra steps let a business stage components close to the line and quarantine or inspect output before it enters stock, each stage being its own numbered transfer.

### BUSINESS RULE
- [N-U14-076] An order is ready when every component movement that is not yet consumed and has a demand is fully reserved. When only part of the components is reserved the order is waiting, unless the bill of materials says the order is ready as soon as the components of its first operation are fully reserved. A partly reserved component counts as fully reserved when it covers the quantity still to consume.
- [N-U14-077] Components are reserved at confirmation when the operation type is set to reserve at confirmation, on the planned reservation date for date-based types, or on demand through a check-availability action; any shortfall for components supplied on order triggers a procurement.
- [N-U14-078] Reservations of unfinished component and product movements, except by-products, can be released unless something has already been consumed; the reserve action is offered only while some component with a demand is still unreserved.
- [N-U14-079] The order shows a component forecast: not available when any component's forecast is below its demand, otherwise expected on a date, flagged late when that date is after the planned start. It also shows the quantity that could be produced from the stock on hand.
- [N-U14-080] When finished products are posted, other waiting or partly reserved movements for those products are re-assigned automatically unless automatic reservation is disabled by configuration.
- [N-U14-081] Transfers created for the pick-components and store-product steps are grouped by the order's production group, and component and product movements of an order are not placed in transfers by default.
- [N-U14-082] Choosing the manufacturing steps creates or activates the matching locations, operation types and rules: pre-production location and pick transfer for two steps; additionally post-production location, store transfer and a cancel-propagating manufacture rule for three steps. The manufacturing type takes its default source and destination from those locations. A manufacture route applies to a product only if it has a manufacturing recipe. In three steps the finished product's final destination is the stock location while it first lands in post-production.

### STATE
- [N-U14-083] Readiness is empty for draft, done and cancelled orders; otherwise it mirrors the summarised state of the component movements and is recomputed whenever they change, returning to waiting if reservations are released or demand grows.

### OPTIONALITY
- [N-U14-084] The reviewed warehouse uses one-step manufacturing: pre- and post-production locations, pick and store transfers and the pick make-to-order rule exist but are inactive, and one company-wide production location exists.

### DEPENDENCY
- [N-U14-085] Multi-step manufacturing relies on the warehouse and route engine of the inventory capability: the manufacture route is created globally and linked to each warehouse that is allowed to manufacture.

### CONSTRAINT
- [N-U14-086] A manufacturing operation type cannot have a scrap or inventory-adjustment location as its destination.

### RISK
- [N-U14-087] When readiness is judged on the first operation only, components added by hand to the order and not on the recipe are ignored in that judgement.

### UNKNOWN
- [N-U14-088] Two- and three-step manufacturing, and readiness based on the first operation, have not been exercised because only the one-step configuration and no orders exist.

## CAP-U14-05 Consumption, production recording and completion (neutral)

### WHAT
- [N-U14-089] Recording production means stating the quantity of product being made, which sets the components to consume in proportion, marks by-products as produced, assigns lot or serial numbers to the output and finally posts all movements when the order is completed.

### WHY
- [N-U14-090] Separating the recording of what was really consumed and produced from the planned quantities lets the business compare actuals with the recipe, trace components to finished lots and keep stock accurate.

### BUSINESS RULE
- [N-U14-091] The quantity to consume of each component equals the quantity being produced beyond what was already produced, times the component's planned ratio; for tracked components it is capped by what predecessor transfers actually delivered; for serial products the quantity being produced equals the number of serial numbers.
- [N-U14-092] A component is consumed manually when its recipe line is tied to an operation or when a user types a quantity different from the planned one; manually recorded components are not overwritten when the produced quantity changes.
- [N-U14-093] Consumed components leave their location towards the product's virtual production location, and finished products and by-products arrive from that location into the destination location.
- [N-U14-094] Before completion the system sets missing quantities automatically for simple orders (untracked, single unit, or ready non-serial orders), requires lot or serial numbers for tracked output, marks by-products as produced, then checks the consumption policy and then offers a backorder when less than planned was produced.
- [N-U14-095] The consumption policy is allowed, allowed with warning, or blocked. On completion the consumed quantity of each component is compared with the quantity expected from the recipe for the produced quantity, and extra components are flagged. With a warning the user may confirm; with blocking only a manager button forces completion, but users may instead set quantities to the expected ones and validate.
- [N-U14-096] On completion components with a recorded consumption are consumed and components without one are cancelled; finished products and by-products are posted at the quantity produced beyond what was previously produced; operations are finished and given their expected duration if none was recorded; remaining movements are closed with zero demand; waiting movements are re-assigned; the order becomes done, locked, with end date now and normal priority. A cost calculation hook is called but does nothing unless the manufacturing accounting capability is installed.
- [N-U14-097] A lot-tracked product receives one lot per order and a serial-tracked product one serial number per unit. Numbers can be generated from the product's own sequence or a general serial sequence, typed in, pasted, or used to split the order into one order per serial number.
- [N-U14-098] A completed order that is unlocked may be corrected: the produced quantity can be rewritten and extra component movements added; changes to lots, locations and quantities on completed movements are logged, and extra consumption is linked to the produced lots for traceability.
- [N-U14-099] Journal entries for manufacturing movements are created only when the product uses perpetual valuation and the location involved has a valuation account; in the reviewed configuration valuation is periodic with standard cost and no work-in-process accounts are set, so completing an order would post stock movements but no journal entries.

### STATE
- [N-U14-100] A component counts as consumed once it is marked picked; at completion picked components are posted, unpicked ones are cancelled and already posted ones are left unchanged.

### OPTIONALITY
- [N-U14-101] Creating new lots or serial numbers for components from an order is allowed only if the operation type is configured for it.
- [N-U14-102] Printing of the production order, product labels, lot labels and allocation report on completion is optional per operation type.

### DEPENDENCY
- [N-U14-103] When the product-expiry capability is installed, completing an order that consumes a component lot whose expiration date has passed asks the user to confirm before proceeding.

### CONSTRAINT
- [N-U14-104] A component movement cannot have a negative quantity.
- [N-U14-105] A serial number cannot be produced twice unless the earlier production was reversed or the unit removed, cannot be consumed twice, and a lot or serial name must be obtainable from a sequence or typed; empty serial lists are rejected.

### RISK
- [N-U14-106] The blocked consumption policy is enforced only by which buttons are shown; any manufacturing user can still complete the order by setting quantities to the expected ones, and the confirmation action itself has no role check.
- [N-U14-107] The expiry confirmation has a work-order branch that calls an action not provided by the community edition, so that branch would fail if ever reached.

### UNKNOWN
- [N-U14-108] The full completion flow with lots, serial numbers, consumption and expiry confirmations has not been executed because no orders exist in the reviewed environment.

## CAP-U14-06 Backorders, split and merge of manufacturing orders (neutral)

### WHAT
- [N-U14-109] A backorder is a new manufacturing order for the quantity not produced when an order is completed short. The original and its backorders share a production group, are numbered with a three-digit suffix, and can be listed together.
- [N-U14-110] Splitting divides a draft or confirmed order into several smaller orders, for example by batch size or one order per serial number, each with its own responsible person and date.
- [N-U14-111] Merging combines several draft or confirmed orders for the same product and recipe into one new order and cancels the originals.

### WHY
- [N-U14-112] Backorders let production continue for the remainder instead of losing it, while the completed part is posted and traced on its own order.

### BUSINESS RULE
- [N-U14-113] When an order is completed with less than the planned quantity, the operation type decides: always create a backorder, ask the user, or never offer one, in which case the remainder is closed with zero demand. The backorder is created before the completed quantity is posted.
- [N-U14-114] The original order becomes number one of its chain and its reference gets a dash and a three-digit sequence; each backorder takes the next number.
- [N-U14-115] A backorder keeps the same production group, references, origin, deadline and replenishment source as the original, starts empty of lots, and is confirmed unless the original was still draft; its components and products are copies scaled to its quantity.
- [N-U14-116] Component and product movement quantities are divided in proportion to the order quantities; existing reservations are redistributed between the original and the backorder rather than released and rebuilt; new backorder components are reserved according to the operation type's reservation method, and after the original is done the backorder reserves newly available stock.
- [N-U14-117] Operations of a backorder carry forward the quantity already produced before it; operations with nothing left to do are cancelled.
- [N-U14-118] The default split is the planned quantity divided into batches of the recipe's batch size, or one batch if none; the parts must add up to the planned quantity; each resulting order gets the chosen responsible person and start date.
- [N-U14-119] A merged order has the summed quantity, the combined origin of the sources, their common responsible person (else the current user), the combined references and groups, and keeps links to upstream supply and downstream demand; it is confirmed if any source was confirmed, and each source records that it was merged.

### STATE
- [N-U14-120] An order with no backorder chain has sequence zero; at its first backorder the original becomes number one and each backorder takes the next number in the same group.

### OPTIONALITY
- [N-U14-121] Whether a backorder is always created, asked for, or never offered is configured per operation type; the reviewed manufacturing type asks.

### DEPENDENCY
- [N-U14-122] Backorders depend on the inventory movement chain: component and product movements are copied with their state, reservation date, deadline, origin links and supply method.

### CONSTRAINT
- [N-U14-123] Only draft or confirmed orders that have a recipe can be split or merged, and a split cannot ask for more than the planned quantity.
- [N-U14-124] Orders can be merged only if there are at least two, they share product, recipe, state and operation type, and none has manually added components or by-products.
- [N-U14-125] Manufacturing users can use the backorder, split and serial-number dialogs.

### RISK
- [N-U14-126] References that already end in a dash and digits may be rewritten unexpectedly when long backorder chains are renumbered; this was not exercised.

### UNKNOWN
- [N-U14-127] How reservations, serial numbers and multi-step links behave when splitting and merging has not been exercised because no orders exist.

## CAP-U14-07 Work orders, planning and scheduling (neutral)

### WHAT
- [N-U14-128] A work order is the execution unit of one operation of a manufacturing order. It has a work center, an expected duration, real time logs, a produced quantity, optional predecessors and a status of blocked, to do, in progress, finished or cancelled.

### WHY
- [N-U14-129] Work orders let the business schedule capacity on work-center calendars, track the real time and quantity of each production step, and cost the operations.

### BUSINESS RULE
- [N-U14-130] Work orders are generated from the operations of the order's recipe and of any kit sub-recipes (kit operations first), skipping operations that do not apply to the variant; they are created to do while the order is draft and blocked when added by refreshing a confirmed order; work orders added by hand after confirmation are confirmed automatically.
- [N-U14-131] When the recipe allows operation dependencies each work order waits for the work orders of its prerequisite operations; otherwise each waits for the previous one in sequence. Component and product movements tied to an operation are attached to its work order.
- [N-U14-132] A work order is to do when quantity is available to it, being the quantity its predecessors have completed minus what it has already done; otherwise it is blocked.
- [N-U14-133] Starting a work order is refused if its work center is blocked or the work order is finished or cancelled; it defaults the quantity to the remainder, starts a time log, starts the order and creates its calendar slot. Pausing only stops the user's time log. Finishing picks the remaining components and by-products of the operation proportionally, closes time logs, records the produced quantity and the work center's current hourly cost, and marks the work order finished. Marking done without any logged time sets the real duration to the expected one.
- [N-U14-134] Expected duration is setup plus cleanup plus the number of cycles times the time per cycle, divided by efficiency; real duration is the union of time-log intervals, with overlapping logs counted once, and changing the real duration creates or trims time logs.
- [N-U14-135] Planning works from the last operations backwards through prerequisites: each work order is placed after its predecessors, not before now or the order start, on its own work center or whichever alternative finishes earliest; the order's dates become the earliest start and latest end of its work orders. An order cannot be un-planned once any work order has started or finished; re-planning moves only work orders that are to do or blocked. A planned order whose first or last work order is moved updates the order dates, and overlaps on the same work center are flagged. The start date can also be set from the forecast availability of components.
- [N-U14-136] The recipe overview can simulate scheduling of its operations on work-center calendars to estimate when a product could be made, adding the longest component delay to the larger of the manufacturing lead time and the operations delay; it reports availability of each component as available, expected on a forecast date, estimable through manufacture, or not available, and fails if a work center has no calendar or no slot exists.
- [N-U14-137] A planned work order occupies a time slot on its work center's calendar; a single work order cannot be un-planned on its own, only the whole order.

### STATE
- [N-U14-138] A work order alternates between blocked and to do automatically with quantity availability, becomes in progress when started, finished when completed and cancelled when cancelled; finished or cancelled work orders can be reopened through the status control, via to do, unless the order is done.

### OPTIONALITY
- [N-U14-139] Work orders appear only when the work-order option is enabled, and need work centers with calendars to be planned; start and pause are also available as bulk actions on lists, and in the reviewed configuration the option is enabled.

### DEPENDENCY
- [N-U14-140] Scheduling and expected end dates depend on the working calendar and leave handling of the resource capability; without a calendar the end date is simply start plus expected minutes.

### CONSTRAINT
- [N-U14-141] Work-order dependencies cannot be cyclic; the produced quantity cannot change after a work order is finished or cancelled and cannot be negative; a work order cannot be moved to another order or to another work center after it is finished; its end cannot precede its start.
- [N-U14-142] Manufacturing users and administrators have full control of work orders within their companies.

### RISK
- [N-U14-143] A paused work order keeps the in-progress status, so state alone does not show whether work is actually running; only open time logs do.

### UNKNOWN
- [N-U14-144] Scheduling against real calendars, choosing alternative work centers and time-log splitting have not been exercised because no work orders exist.

## CAP-U14-08 Scrap during production and unbuild (disassembly) (neutral)

### WHAT
- [N-U14-145] Scrap records waste during production: a user scraps a component that was not consumed or a product that was produced, from the manufacturing order or a work order, and the quantity leaves stock to a scrap location.
- [N-U14-146] An unbuild order reverses production: it consumes the finished product, and by-products, from a chosen location and returns the components to a destination location. It can reverse a specific completed order or disassemble a product using its recipe.

### WHY
- [N-U14-147] Scrap is recorded against the order so waste can be traced to it without altering the order's planned component and product lists.
- [N-U14-148] Unbuild allows returning components to stock and removing the finished product when a completed order must be undone, while keeping lots and serial numbers traceable.

### BUSINESS RULE
- [N-U14-149] Scrap is taken from the order's component location while the order is open and from its finished-product location once it is done; a scrapped product that is one of the order's products counts as a product movement, otherwise as a component movement; scrap movements are kept out of the order's component and product lists; scrapping a lot that was consumed releases its consumed marking; kit scraps are split into component scraps.
- [N-U14-150] When unbuilding a completed order, quantities of every consumed and produced movement are scaled by the ratio of the quantity unbuilt to the quantity produced, lots and owners are taken from the original movement lines, produced and consumed lines are linked for traceability, a note is added to the order, and defaults for quantity and locations come from the order. Without an order the recipe is used. If the source location lacks the quantity the user is warned and may proceed. A serial number may be produced again after it was unbuilt.

### STATE
- [N-U14-151] An unbuild order is either draft or done; there is no cancelled state.

### OPTIONALITY
- [N-U14-152] Unbuild needs no feature switch; it can be done against a completed order or directly from a recipe, but tracked products and components require an order.

### DEPENDENCY
- [N-U14-153] Unbuild relies on the inventory capability for stock availability checks, lots and put-away of returned components.

### CONSTRAINT
- [N-U14-154] The quantity to unbuild must be positive; a given order must be completed; tracked products need a lot and tracked components need an order; a completed unbuild cannot be deleted.
- [N-U14-155] Manufacturing users and administrators have full control of unbuild orders within their companies.

### RISK
- [N-U14-156] Doing several unbuilds with lots on the same order may fail, as noted in the source, and unbuilding without an order assumes the recipe quantities rather than the actual consumption.

### UNKNOWN
- [N-U14-157] The accounting and valuation effect of unbuild movements, and unbuild with lots and serial numbers, have not been traced or executed.

## CAP-U14-09 Replenishment for manufacturing: manufacture rule, reordering rules, make-to-order, lead times (neutral)

### WHAT
- [N-U14-158] A manufacture rule turns a need for a product into a manufacturing order. Needs come from sales, component demand of another order, reordering rules or manual replenishment. The warehouse owns the manufacture rule and the make-to-order rules that feed production from stock; in the reviewed configuration no reordering rule exists.

### WHY
- [N-U14-159] Automatic creation, merging and batching of orders lets production follow demand and stock minimums without manual order entry, with lead times used to plan when to start.

### BUSINESS RULE
- [N-U14-160] A need creates a manufacturing order using the recipe named on the need or on the reordering rule, otherwise the manufacturing recipe that matches the rule's operation type, otherwise any manufacturing recipe; the operation type comes from the recipe or the rule; zero or negative needs create nothing.
- [N-U14-161] A new need is added to an existing draft or confirmed order instead of creating another one when it has the same recipe, product, type, company and references, is not yet planned and has no responsible person; for reordering-rule needs the existing order must also fall within the date window.
- [N-U14-162] When the recipe has a batch size, the need is split into orders of exactly that batch size instead of being merged.
- [N-U14-163] Orders created by replenishment are confirmed automatically unless they were requested by a reordering rule and already have components, in which case they are confirmed after all reordering rules have been processed so their component demand does not conflict with the others; orders note their origin.
- [N-U14-164] The start of a generated order is the need date minus the manufacturing lead time, an hour earlier if that lead time is zero, and its deadline is the need deadline or the start plus the lead time; manual replenishment adds the lead time and the days to prepare components to the date.
- [N-U14-165] The lead-time estimate for a product adds the manufacturing lead time, the pre-production step delays for multi-step warehouses and the days to supply components; if no recipe exists it adds a year and flags that no recipe was found. The days to supply components can be computed from the availability delays of the components.
- [N-U14-166] Component movements for products supplied on order generate procurements for the quantity not covered by reservation, never reducing below what upstream movements can give back; the child order or purchase is linked to the parent through the production group.
- [N-U14-167] A reordering rule may name the recipe to use and defaults to the manufacture route when the product has a recipe; its replenishment multiple is the recipe's unit; it counts quantity already in progress from draft orders and confirmed orders overlapping its horizon, and for kits derives the quantity from components; a supply warning shows if a product with the manufacture route has no recipe; the daily scheduler processes automatic reordering rules.

### STATE
- [N-U14-168] An order created by replenishment starts as draft and is confirmed at once, or later by the scheduler pass, according to whether it has components and what requested it.

### OPTIONALITY
- [N-U14-169] Manufacture-based replenishment is optional per warehouse, per product route, per reordering-rule trigger and per recipe batch size.

### DEPENDENCY
- [N-U14-170] A master production schedule is not part of the community edition; the settings only offer to install an additional product, which is absent from the reviewed environment.

### CONSTRAINT
- [N-U14-171] A manufacture rule must use a manufacturing operation type.

### RISK
- [N-U14-172] Orders generated by rules are created with elevated privileges, so the user who triggered the need does not need manufacturing rights and access checks are not applied at creation.
- [N-U14-173] The rule code reserves a special origin for the schedule planner that skips merging; without that planner it has no effect.

### UNKNOWN
- [N-U14-174] The complete replenishment chain with real reordering rules, make-to-order products and batch sizes has not been exercised because no such data exists.

## CAP-U14-10 Manufacturing cost inputs and cost reporting (neutral)

### WHAT
- [N-U14-175] Manufacturing cost inputs are the hourly cost of a work center, the cost basis of each operation, the cost share of by-products and the standard cost of components. The manufacturing capability stores no total order cost; it gives cost estimates and comparisons in the recipe overview and the order overview, and a hook for the accounting capability.

### WHY
- [N-U14-176] Comparing recipe cost, expected order cost and real cost lets managers see where production deviates from plan and how cost is split between the main product and by-products.

### BUSINESS RULE
- [N-U14-177] The cost of an operation is its duration in hours times the hourly cost; for operations on an actual-time basis the duration is the tracked time, for those on an estimated basis it is the expected duration. The cost basis is copied from the operation when the order is confirmed and the hourly cost is frozen when the work order is finished, so later rate changes do not alter finished work.
- [N-U14-178] A by-product receives its stated percentage of the total production cost; the main product carries the remainder.
- [N-U14-179] In the recipe overview, component cost is the component's standard cost converted to the line unit times the quantity, sub-assemblies add their own cost recursively, operation costs are added, and by-products take their share. The order overview shows expected, recipe and real cost: real component cost is consumed quantity times unit cost, and operation cost follows the cost basis.
- [N-U14-180] When the manufacturing accounting capability is installed, the unit cost of the finished product at completion equals the value of consumed components plus work-order cost plus the extra unit cost times the quantity, reduced by the by-product shares, divided by the quantity, for average and first-in-first-out products; products on standard cost keep their standard cost; by-products take their share or their standard cost. This is based on what was actually consumed, not on the recipe quantities.
- [N-U14-181] Journal entries for manufacturing movements and labour are created only for products with perpetual valuation and only when the production location carries a valuation account, which is an expense-type account used to requalify goods sent to that location rather than a dedicated work-in-process account. At completion one labour entry per order debits the work-center expense account, or the product's expense account, and credits the production location account.
- [N-U14-182] A manual work-in-process entry can be posted for orders in progress at a chosen date: component value at standard cost and overhead from work-order cost are credited and the company's work-in-process account debited; the entry must balance and is automatically reversed on a later date.

### STATE
- [N-U14-183] A work order's cost basis is fixed when its order is confirmed and its hourly rate when it is finished, after which rate or basis changes on the work center or operation do not alter it.

### OPTIONALITY
- [N-U14-184] In the reviewed configuration valuation is periodic with standard cost, no company work-in-process accounts are set, no location has a valuation account and no work center exists, so no manufacturing journal entries would arise.

### DEPENDENCY
- [N-U14-185] Accounting for manufacturing exists only through the manufacturing accounting capability, which in turn requires the stock valuation capability.

### CONSTRAINT
- [N-U14-186] A manual work-in-process entry must balance and its reversal date must be after its posting date.

### RISK
- [N-U14-187] The interim work-in-process amount uses standard cost rather than the actual valuation of consumed components, so it can differ from the amount finally posted at completion.

### UNKNOWN
- [N-U14-188] Actual cost calculation, by-product pricing, labour and work-in-process entries have not been exercised, because the reviewed configuration uses periodic valuation and holds no orders.

## CAP-U14-X Cross-cutting: access groups, settings, menus, reports, activation hooks and add-on modules (neutral)

### WHAT
- [N-U14-189] The manufacturing capability seeds two role groups, five optional feature groups, a menu tree, six printable reports, five message types for order state changes, loss reasons and activation hooks. At installation it adds two calculation columns to stock movements and makes every existing warehouse able to manufacture.

### WHY
- [N-U14-190] Optional features are enabled by settings that grant visibility to all internal users, so that simple businesses see a simple application and advanced features are shown only when switched on.

### BUSINESS RULE
- [N-U14-191] At installation every existing warehouse is made able to manufacture, so manufacturing orders can be generated for it without further setup.

### STATE
- [N-U14-192] Changing the unlocked-by-default setting immediately locks or unlocks all open manufacturing orders to match.

### OPTIONALITY
- [N-U14-193] Work-order operations, by-products, unlocked-by-default orders, allocation report and operation dependencies are separate optional features, each granted through a setting.

### DEPENDENCY
- [N-U14-194] Planning schedule, product lifecycle, quality and subcontracting appear in settings as installable add-ons, of which only subcontracting is part of the community edition. The expiry add-on installs automatically when manufacturing and product expiry are both present, the project add-on when manufacturing and projects are both present, and a further technical bridge when project, sales and manufacturing are all present.

### CONSTRAINT
- [N-U14-195] Manufacturing users also gain stock-user rights; manufacturing administrators gain user rights, and only they see the configuration menu; project users may only read bills of materials and lines when the project integration is installed.

### RISK
- [N-U14-196] In the reviewed configuration the unlocked-by-default option is on for all internal users, so the protection of locked orders against accidental edits is not in effect.

### UNKNOWN
- [N-U14-197] Uninstallation behaviour and the browser-side behaviour of the manufacturing application were not read or exercised.

