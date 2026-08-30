> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 8 of 10 — Persona / User Fitness Observation Matrix
> IMPORTANT SCOPE CAVEAT: this is a source-code-only research pass. No user interviews, job-shadowing, or usage
> telemetry were available. Personas below are RECONSTRUCTED from field help-text, security-group names, and
> actor/maintainer/consumer language already documented in Phases 1-4 — they are role labels the source code
> implies, not confirmed real-world job functions. Every row is classified `Unknown / Requires Real-User
> Validation` for anything beyond "the source code names or implies this role" per governance §17's rule that AI
> synthesis does not replace real-user validation.

# 12 — PERSONA / USER FITNESS OBSERVATION MATRIX

## 00 — Method

Column meaning: **Persona (as implied by source)** = the role a security group, field help-text, or docstring
names. **Evidence** = where this role is named. **What they touch** = the capability from Phases 1-4 this role is
associated with. **Fitness observation** = anything about the interface/workflow that the source itself reveals
as friction, a manual workaround, or a real-user-facing decision point. **Validation status** = whether this is
confirmed by anything beyond the source code itself (in every row: no).

## 01 — Personas implied by source evidence

| Persona (as implied by source) | Evidence | What they touch | Fitness observation (source-evidenced only) | Validation status |
|---|---|---|---|---|
| Sales quotation preparer | `sale.order` state machine, quotation-focused fields (`validity_date`, `partner_credit_warning`) | Creates/edits quotations pre-confirmation | Confirmation gate is minimal (state + product presence only) — no credit or approval friction is imposed on this persona by the base system (Sales SO-14) | Unknown / Requires Real-User Validation |
| Sales order confirmer / account manager | `action_confirm()`, credit-warning display (advisory only) | Converts quotation to committed order | The credit-limit warning is visible but never blocking (Sales SO-32/36) — a real design choice whose lived experience (does staff trust/ignore the warning?) cannot be assessed from source alone | Unknown / Requires Real-User Validation |
| Purchasing buyer / procurement officer | `purchase.order` RFQ workflow, `_add_supplier_to_product()` (Purchase PO-04) | Creates RFQs, manages vendor selection, approves under the amount threshold if authorized | The approval-threshold gate (`po_double_validation`) silently no-ops a `button_approve()` click for an unauthorized user rather than explaining why (Purchase PO-07) — a real UX friction point: the buyer sees no error, just no state change | Unknown / Requires Real-User Validation |
| Purchasing manager / approver | `purchase.group_purchase_manager` security group | Approves orders above the threshold | Purchase's real approval mechanism is a single amount-threshold gate, not the elaborate two-level "level 1/level 2 approver" schema the DB schema suggests once existed or was intended (Purchase §03) — if staff were trained on a two-level process, the live system does not implement it | Unknown / Requires Real-User Validation — this is the single highest-value gap for a real-user interview to resolve |
| Warehouse operator (receiving) | `stock.picking.type.code=='incoming'`, `use_create_lots` default (Phase 2 LOT-06) | Validates receipts, creates lots/serials at receipt time | Backorder policy (`ask`/`always`/`never`) is configured per picking type, not per-transaction — an operator cannot choose case-by-case whether to backorder unless the type is set to `ask` (Phase 2 BO-03) | Unknown / Requires Real-User Validation |
| Warehouse operator (delivery) | `stock.picking.type.code=='outgoing'`, `use_existing_lots` default | Validates deliveries, picks against reservations | Sale confirmation never gates on availability (Sales/Phase 2 finding) — meaning a salesperson can promise a delivery date the warehouse cannot meet, and the warehouse operator is the first to discover a shortfall at pick time, not the salesperson at order time | Unknown / Requires Real-User Validation — a real fit-gap candidate for user-experience review |
| Requesting employee (internal demand) | `purchase.request.requested_by` | Raises a Purchase Request before any vendor is chosen | Approver is derived automatically from `hr.employee.pr_approver` (Purchase PREQ-04) — the requester has no way to choose or escalate to a different approver from within the request itself, per the fields read | Unknown / Requires Real-User Validation |
| Purchase Request approver | `assigned_to`, `button_approved()` | Approves/rejects a Purchase Request | The module's own code comments say its native approve/reject buttons are meant to be "superseded" by an external multi-level approval engine (Purchase PREQ-07/08) — but that engine's connection to this model could not be confirmed as live (Purchase §03/§05). **A real approver may be using a different screen/flow than the one the base module implements, and source code alone cannot say which.** | Unknown / Requires Real-User Validation — flagged as the second-highest-value gap for a real-user interview |
| Finance / credit-control admin | `account.payment.term`, `res.partner.credit_limit` | Maintains payment terms and credit limits | Same "visible but non-blocking" pattern as the Sales credit warning (Phase 1/Sales) | Unknown / Requires Real-User Validation |
| Inventory / warehouse manager | `stock.warehouse`, `stock.location`, `stock.putaway.rule`, `stock.warehouse.orderpoint` | Configures warehouse structure, reorder rules, put-away logic | Put-away rule specificity ordering (package-type > product > category) is expressed only as a sort-key, not documented anywhere as a named policy a manager could review in plain language (Phase 2 PA synthesis) | Unknown / Requires Real-User Validation |
| Vendor / customer (external party) | `res.partner`, portal-facing fields (`partner_credit_warning`, quotation email templates) | Receives quotations, RFQs, invoices, WHT certificates | Whether external parties interact via a portal, email-only, or a completely separate channel (phone/LINE/Excel, explicitly named as a possibility in governance §17) was **not evidenced anywhere in this source-code-only pass** | Unknown / Requires Real-User Validation — explicitly a governance-flagged blind spot this research cannot fill |

## 02 — Manual workaround / Excel-adjacent risk signals found in source (not confirmed as real practice)

The following are places where the source code's OWN design suggests a manual step or discretionary human
judgment is required — these are **candidate** signals for "does staff use Excel/manual tracking here," not
confirmed instances of it:

| Signal | Evidence | Why it's a candidate manual-workaround risk |
|---|---|---|
| No automated linkage between the two independent Thai "branch" fields (`l10n_th_partner.branch` vs `bm_thai_rd_vat_company_search.office_type`) | Phase 1 CO-15..24 | If both are meant to describe the same real-world fact (a company's Revenue-Department branch registration), someone must be manually keeping them consistent, or one is simply unused/stale in practice — cannot be determined from source alone |
| Purchase's real approval gate is a single amount threshold, but the DB schema implies a two-level approver workflow was once intended or configured | Purchase §03 | If staff believe there is a two-level sign-off process, they may be tracking that second level outside the system entirely (e.g., an email chain or a spreadsheet) — plausible, not confirmed |
| Over-receipt on Purchase lines is completely unguarded | Purchase POL-24 | A discrepancy between ordered and received quantity, if it occurs, produces no system flag — any reconciliation would have to happen through a manual review process not evidenced in source |
| Sale confirmation is never gated by inventory availability | Sales/Phase 2 finding | A sales team promising delivery dates without a hard stock check plausibly relies on informal communication with warehouse staff to avoid overpromising — plausible, not confirmed |
| Two byte-identical "amount to text" modules exist with no indication either was deliberately chosen over the other | Phase 8 TXT-01 | Suggests two different implementers (possibly at different times) solved the same problem without checking for an existing solution — a process/governance signal about how customizations get added to this codebase, not a live user workaround |

## 03 — Explicit statement per governance §17

No claim in this document should be read as confirming a persona's actual behavior, workflow, or reliance on
non-system tools. Every entry is a hypothesis generated from source-code structure, explicitly awaiting real-user
validation. The two items flagged as "highest-value gap for a real-user interview" (the Purchase approval-process
discrepancy and the Purchase-Request approval-screen discrepancy) are prioritized because they involve a
**structural mismatch between what the database schema implies was intended and what the live code actually
does** — precisely the kind of question source code alone cannot resolve, and precisely the kind of question this
governance framework requires be marked UNKNOWN rather than assumed.
