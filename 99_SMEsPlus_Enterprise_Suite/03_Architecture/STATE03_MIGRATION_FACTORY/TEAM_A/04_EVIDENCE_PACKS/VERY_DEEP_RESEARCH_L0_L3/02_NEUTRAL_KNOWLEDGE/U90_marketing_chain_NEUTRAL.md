# U90 Neutral Knowledge — Marketing Chain
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U90-001 | The mass mailing entity is a core Community model that combines thread communication, activity tracking, email rendering, and UTM attribution capabilities through multiple inheritance. |
| NR-U90-002 | The UTM attribution mixin grants mass mailing access to source, medium, and campaign tracking fields through a shared inheritance chain. |
| NR-U90-003 | The mailing lifecycle has four states: Draft (not yet scheduled), In Queue (scheduled and waiting for the cron), Sending (actively being dispatched by cron), and Sent (completed); the default is Draft. |
| NR-U90-004 | In Community edition, the mailing type only supports Email. Additional mailing types such as SMS exist in separate add-on modules that may require Enterprise licensing. |
| NR-U90-005 | A mass mailing may be directed at one or more mailing lists, which are linked through a many-to-many relationship. |
| NR-U90-006 | Each mailing holds a one-to-many collection of delivery trace records that capture per-recipient send outcomes; the trace records reference back to their parent mailing. |
| NR-U90-007 | A mailing carries three UTM attribution references — campaign, medium, and source — enabling attribution of engagement back to a specific marketing initiative. |
| NR-U90-008 | Placing a mailing in the send queue sets its state to In Queue and triggers the mass mailing cron job to process it at the configured schedule date, or immediately if no date is set. |
| NR-U90-009 | Cancelling a mailing from the In Queue state resets it to Draft and clears all scheduling information. |
| NR-U90-010 | The public send action is a thin wrapper over the internal send logic and is the entry point used by the user interface and external callers. |
| NR-U90-011 | After the underlying mail composition finishes sending, the mailing record is updated to Sent status with the current timestamp recorded as the sent date. |
| NR-U90-012 | A scheduled cron job processes all mailings in the In Queue or Sending states whose schedule date has passed; it transitions each to Sending before dispatching and marks them Sent when complete. |
| NR-U90-013 | During cron processing, if recipients remain the mailing transitions to Sending before dispatch; if no recipients remain it is marked Sent directly without sending. |
| NR-U90-014 | Delivery trace records are stored in a separate model from the mail records themselves in order to preserve statistics even after the individual email records are deleted. |
| NR-U90-015 | A trace record can be in one of nine states: Outgoing, Processing, Sent (pending delivery confirmation), Delivered, Opened, Replied, Bounced, Exception, or Cancelled. |
| NR-U90-016 | Trace records inherit UTM attribution (medium, source, campaign) as related fields from their parent mailing, enabling campaign-level aggregation of delivery metrics. |
| NR-U90-017 | Each trace record links to click tracking records; the most recent click timestamp is stored directly on the trace for quick reporting without joining the click table. |
| NR-U90-018 | The event entity is a Community model combining thread communication and activity tracking; events are ordered by start date. |
| NR-U90-019 | Event status in Community is managed through a combination of a stage reference (configurable by administrators) and a kanban progress indicator (In Progress, Ready, Blocked, Cancelled), rather than a single fixed status field. |
| NR-U90-020 | An event registration links an attendee to a specific event, ticket type, and optionally a slot; it inherits thread communication and activity tracking. |
| NR-U90-021 | Registration status has four values: Unconfirmed (pending), Registered (confirmed), Attended (post-event), and Cancelled; the default on creation is Registered. |
| NR-U90-022 | Event registrations capture UTM attribution (campaign, source, medium) via default values taken from the UTM session context at the time of registration. |
| NR-U90-023 | Event tickets belong to a specific event and inherit from a ticket-type template; they track reserved, available, and sold-out seat counts and have optional sale window dates. |
| NR-U90-024 | When the event-CRM integration module is installed, each event registration gains a many-to-many relationship to sales leads, making it possible to trace which registrations contributed to which leads. |
| NR-U90-025 | Lead generation from event registrations is skipped during data import operations to avoid creating spurious leads when bootstrapping a database. |
| NR-U90-026 | When a registration is confirmed (status set to Registered), the system automatically runs all active lead generation rules configured to trigger on attendee confirmation. |
| NR-U90-027 | When a registration is marked as Attended, the system runs all active lead generation rules configured to trigger on attendance completion. |
| NR-U90-028 | Lead generation rules are a configuration entity that defines when and how sales leads are automatically created from event attendees. |
| NR-U90-029 | Rules operate in one of two modes: per-attendee (creates one lead for each individual registration) or per-order (creates one lead for a batch of registrations from the same booking session). |
| NR-U90-030 | A rule's trigger point determines whether it fires at attendee creation, at registration confirmation, or after event attendance is confirmed. |
| NR-U90-031 | The lead creation engine collects all lead value dictionaries and issues a single batch create call, returning only the newly created leads (updates to existing leads are not returned). |
| NR-U90-032 | When leads are created from event registrations, they are linked back to the originating rule, event, and source registrations for full traceability. |
| NR-U90-033 | UTM attribution travels from registration to lead: the campaign, source, and medium values on the registration are copied onto the created sales lead, preserving end-to-end marketing attribution. |
| NR-U90-034 | When a mass mailing has email type and no medium is assigned, the system automatically sets the medium to the standard email UTM medium value, ensuring consistent attribution without manual configuration. |
| NR-U90-035 | The marketing automation module (rule-based drip campaign engine) is not present in the Community edition source tree; it is an Enterprise-only capability and therefore unavailable in a Community deployment. |
