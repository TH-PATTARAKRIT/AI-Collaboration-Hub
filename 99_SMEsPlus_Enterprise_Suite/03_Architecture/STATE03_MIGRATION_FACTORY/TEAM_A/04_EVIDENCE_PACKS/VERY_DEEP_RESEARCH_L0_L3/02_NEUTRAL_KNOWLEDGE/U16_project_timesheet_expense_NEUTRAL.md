# U16 - Project, timesheet and expense accounting flows - Neutral Knowledge

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source family: Odoo 19 Community. Date: 2026-10-02.
> Plain business and process statements only. Each statement carries an identifier that links to the restricted evidence layer.
> No coverage, level, gate or approval claim is made.

## CAP-U16-01 Employee expense capture and categories

### WHAT

- [N-U16-001] Employees record a business expense as a single record that carries a category, an amount, a date, a currency, receipts, optional taxes and an optional cost allocation. There is no separate report or batch object that groups expenses before approval.
- [N-U16-002] An expense can be created by typing it in, by uploading a receipt file, or by sending an email whose subject carries a category code and an amount; the system reads the sender, the category code and the price from the subject.

### WHY

- [N-U16-003] Capturing each expense as its own record with its receipt keeps the evidence next to the amount and lets each expense follow its own approval and accounting path.

### BUSINESS RULE

- [N-U16-004] Only categories flagged as expensable can be chosen; such a category must be usable on purchases, and the flag is cleared automatically for categories that are neither goods nor services.
- [N-U16-005] When the category has a non-zero cost, the amount is quantity times the category cost with taxes included; otherwise the employee types the total and the unit price is derived from it.
- [N-U16-006] Taxes on an expense are always treated as included in the amount that the employee typed or that the category cost represents, whether the tax is configured as included or excluded; the tax portion is carved out of the total, not added on top.
- [N-U16-007] Taxes and the expense account are taken from the category (purchase taxes of the same company only), and the account falls back to the company expense account when no category is set.
- [N-U16-008] An expense in a foreign currency is converted to company currency at the rate of the expense date; the employee may overwrite the converted total, which then defines a custom rate.
- [N-U16-009] Two expenses for the same employee, category, date, amount, company and currency are flagged as possible duplicates, and two expenses sharing the same receipt file are flagged as sharing a receipt; both are warnings, not blocks.
- [N-U16-010] An expense may be split into several expenses whose amounts must add up exactly to the original; each part may take a different category, tax and cost allocation, and every part receives a copy of the receipts.
- [N-U16-011] Receipts can be added or removed only while the expense is still a draft or submitted; after approval attachments are frozen.
- [N-U16-012] An approved, posted or paid expense cannot be deleted; drafts, submitted and refused expenses can.
- [N-U16-013] Changing the cost of a category updates the unit price of all draft expenses that use it, and the category form warns when unsubmitted expenses exist.

### STATE

- [N-U16-014] A newly captured expense starts as a draft; from capture to submission nothing is written to the ledger.

### OPTIONALITY

- [N-U16-015] Capture by email depends on a company setting that is switched on by default, on an alias name, and on the sender matching an employee work email or user email; when the sender is unknown the message becomes an ordinary record without employee data.
- [N-U16-016] Six expense categories are delivered ready-made: meals, travel and accommodation, mileage, gifts, communication and a generic one with no cost; mileage carries a per-kilometre cost.

### DEPENDENCY

- [N-U16-017] The category list, taxes, accounts and units of measure come from the product, accounting and unit-of-measure capabilities; the employee list and its filtering come from the human-resources capability.

### CONSTRAINT

- [N-U16-018] An expense that is no longer a draft may not have a zero total.
- [N-U16-019] Creating an expense requires that the current user be linked to an employee, unless the user holds an approver role.
- [N-U16-020] Every employee has full rights (read, change, create and delete) on expenses at the access-list level; record rules then narrow what each person sees and may change.

### RISK

- [N-U16-021] Because duplicates and shared receipts are warnings only, the same receipt can be reimbursed twice if the approver dismisses the warning.
- [N-U16-022] Email capture reads a price and category from free text in the subject, so a mistyped subject produces a wrong amount or no category.

### UNKNOWN

- [N-U16-023] Automatic receipt reading by an external recognition service and card-feed expenses are offered as settings but belong to modules that are not part of the community edition studied; their behaviour is not documented here.
- [N-U16-024] Delivery of the confirmation email after an email capture, and the real-time behaviour of the mail gateway, were not executed and are unverified.

## CAP-U16-02 Expense approval workflow

### WHAT

- [N-U16-025] An expense moves from draft to submitted, then to approved or refused, under the control of the employee's manager chain; approval is a status on the expense itself and is independent of any accounting entry.
- [N-U16-026] Approvers receive a task on submission and a weekly reminder email listing what is waiting; the task is closed when the expense is approved and removed when it is refused or reset.

### WHY

- [N-U16-027] Separating approval from accounting lets managers confirm that an expense is a legitimate business cost before any ledger entry exists, and lets accountants act only on approved items.

### BUSINESS RULE

- [N-U16-028] An employee may submit only their own expense, and an expense cannot be submitted without a category; other people may submit on behalf only if they hold approval rights over that employee.
- [N-U16-029] The responsible approver is, in order of preference, the employee's designated expense approver, the manager of the employee's department if that person holds an approver role, or the employee's direct manager; the employee never counts as their own approver.
- [N-U16-030] If no approver exists, or the only approver is the employee, the expense is approved automatically at submission without a duplicate check.
- [N-U16-031] A user may approve only expenses of people they manage, expenses within their company scope, and never their own, unless they are an expense administrator.
- [N-U16-032] Before an expense is approved, the cost allocation is checked against the mandatory allocation plans configured for expenses.
- [N-U16-033] When approving an expense that has possible duplicates already submitted, approved, posted or paid, the approver must confirm in a dialog that each is legitimate or refuse the duplicate with a fixed reason.
- [N-U16-034] Refusal requires a written reason and is allowed from submitted and approved; it is blocked when a posted accounting entry exists, and draft entries are deleted.
- [N-U16-035] Reset to draft clears the approval and the link to the accounting entry; it is refused when the linked entry is already posted.

### STATE

- [N-U16-036] Draft goes to submitted on submission, submitted goes to approved or refused, approved goes to posted on accounting entry creation (see later capabilities), and reset returns an approved, submitted or refused expense to draft.

### OPTIONALITY

- [N-U16-037] Approval routing can be set per employee, by department head, or by direct manager, and the weekly reminder job can be disabled or rescheduled by an administrator.

### DEPENDENCY

- [N-U16-038] Approval routing uses the employee hierarchy and departments; reminders use the activity and outbound email facilities.

### CONSTRAINT

- [N-U16-039] Three expense roles exist: team approver, all approver and administrator, each implying the previous one; accounting roles act on posting rather than approval.
- [N-U16-040] A plain employee can create, read and edit only their own drafts; after submission the employee can read but no longer edit; approvers can edit submitted and approved expenses of their reports.
- [N-U16-041] Editing taxes, cost allocation, account or approver on an expense is allowed only to users who can edit that expense.
- [N-U16-042] Expense records are visible only within the user's allowed companies.

### RISK

- [N-U16-043] Automatic approval when no approver exists means an employee without a manager or approver can have expenses approved with no review at all.
- [N-U16-044] Approval is enforced in the server method and in the form buttons, but a user whose employee record is also their own approver bypasses review through the auto-approval rule.
- [N-U16-045] The reset-to-draft method contains a branch that reverses posted entries, but a prior check refuses posted entries, so that branch cannot be reached through normal use.
- [N-U16-046] A notification branch refers to a status that an expense can never have, so the message intended for that case is never sent; refusal is notified through its own status change instead.

### UNKNOWN

- [N-U16-047] How record visibility behaves for users who hold only a billing accounting role (and not an expense role) when they need to see other employees' approved expenses is not settled by the declared rules; it needs a runtime check with such a user.
- [N-U16-048] Whether the weekly reminder email actually leaves the server depends on mail server configuration and was not executed.

## CAP-U16-03 Expense accounting entry creation (employee-paid and company-paid)

### WHAT

- [N-U16-049] Accountants turn approved expenses into accounting entries. For an expense the employee paid out of pocket, the system creates a vendor receipt addressed to the employee that credits an amount owed to the employee; for an expense paid by the company it creates an outgoing payment together with its entry so the already-made payment can be matched to the bank.
- [N-U16-050] Several approved employee-paid expenses of the same employee are combined into one receipt with one line per expense; each company-paid expense always gets its own entry.

### WHY

- [N-U16-051] The expense cost, input tax and the liability to the employee (or the settled outgoing payment) must be recorded in the ledger as soon as the expense is accepted, regardless of when cash moves.

### BUSINESS RULE

- [N-U16-052] Only approved expenses can be turned into entries, and the payer (employee or company) must be specified.
- [N-U16-053] Employee-paid expenses of different companies cannot be posted in one action.
- [N-U16-054] The receipt is dated with the accounting date chosen in the posting dialog, is held in the employee's work contact, carries the employee's primary bank account, and is posted immediately; the original receipt files are copied onto the entry.
- [N-U16-055] The journal for employee-paid entries defaults to the company's expense journal, then the nearest parent company's, then the first purchase journal; the first time a journal is chosen it is stored as the company default.
- [N-U16-056] Each expense line is booked to the expense account of the expense, falling back to the category account, then the company expense account, then the default account of the purchase journal; if none exists, posting fails with an explanation.
- [N-U16-057] For employee-paid expenses the credit side goes to the employee contact's payable account; for company-paid expenses it goes to the payment method's outstanding account, or an outstanding account that is created on the fly if absent.
- [N-U16-058] Taxes on posted expense lines are extracted from the total as if included, and the tax lines are created from the expense tax settings; the cost allocation of the expense is carried onto the entry lines.
- [N-U16-059] A company-paid expense produces an outgoing supplier payment of the expense amount in the expense currency, using the selected payment method of the journal; the entry and the payment are posted together.
- [N-U16-060] When the chosen payment method is a bank credit transfer file type, the vendor must be filled in, because the file needs a creditor name.

### STATE

- [N-U16-061] Posting moves an approved expense to posted for employee-paid expenses, and directly to paid for company-paid expenses because the money has already left.

### OPTIONALITY

- [N-U16-062] The set of payment methods offered for company-paid expenses can be restricted in company settings; otherwise every active outgoing method of the company's journals is offered.
- [N-U16-063] The default expense journal can be configured per company; this database already has one purchase-type journal set as the company default.
- [N-U16-064] Payments created for expenses never require a bank account of the payee to be present.
- [N-U16-065] A second posting path that skips the dialog exists for special flows only; it dates the receipt today and uses the default expense journal or the first purchase journal.

### DEPENDENCY

- [N-U16-067] Posting relies on the vendor-bill engine, the tax engine, the payment engine, analytic plans and the employee's work contact; an employee without a work contact cannot be posted.

### CONSTRAINT

- [N-U16-068] An expense paid by the company must have its own dedicated entry, and a payment may be linked to at most one expense.
- [N-U16-069] Once a payment is linked to an expense its date, amount, type, partner, journal, method and memo cannot be edited.
- [N-U16-070] The posting dialog requires the right to create accounting entries; entries are created with elevated rights on behalf of the accountant.
- [N-U16-071] The journal-type check that normally forces vendor receipts into purchase journals is waived for expense entries.

### RISK

- [N-U16-072] The receipt is created in company currency with prices converted at the expense rate, so any foreign-currency information of the original expense lives only on the expense record, not on the entry.
- [N-U16-073] Creating missing outstanding accounts on the fly during posting means a chart-of-accounts change can happen as a side effect of posting a company-paid expense.
- [N-U16-074] A company-paid expense without a vendor produces an entry with no partner on both lines, which weakens vendor-level reporting and reconciliation.

### UNKNOWN

- [N-U16-066] A numbering series for expense invoices is delivered with the module but is not used by the entry creation code that was read; entry numbers come from the journal.
- [N-U16-075] Local withholding or special tax treatment for the Thai chart on expense lines is not determined by this capability and was not traced; it depends on the tax configuration chosen on the category.
- [N-U16-076] The behaviour of the automatic creation of outstanding accounts for a company with a non-standard chart prefix was not executed.

## CAP-U16-04 Employee reimbursement and expense settlement status

### WHAT

- [N-U16-077] After an employee-paid expense is posted, the amount owed to the employee is settled by registering a payment against the receipt; the expense status then follows the payment status of that receipt.
- [N-U16-078] An expense can go back from posted or paid to approved when its entry is reversed, cancelled or set back to draft, so it can be re-posted; refused and draft expenses can be reset.
- [N-U16-088] From an expense the user can open the receipt for an employee-paid expense or the payment for a company-paid expense.

### WHY

- [N-U16-079] Employees must see whether they have been reimbursed, and finance must be able to correct a wrong entry without losing the approval.

### BUSINESS RULE

- [N-U16-080] Status posted means the receipt exists and is unpaid or still in draft; paid means the receipt is fully or partially settled in a way that leaves no residual, or the expense was paid by the company.
- [N-U16-081] A fully paid, reversed or cancelled receipt is shown as paid; in the community edition the intermediate in-payment status does not exist and fully paid receipts are reported as paid.
- [N-U16-082] The reimbursement payment defaults to the employee's primary bank account, or the first bank account of the contact if the receipt has none.
- [N-U16-083] When a payment is registered on an expense receipt, the payment's entry lines are tagged with the expense, so the payment can be traced back.
- [N-U16-084] Reversing a receipt or cancelling it removes the link between the expense and the entry, which returns the expense to approved so it can be posted again; the original entry stays as an audit trail.
- [N-U16-085] The expense dashboard counts draft and submitted expenses plus approved and posted expenses paid by employees as waiting items, with posted expenses reported under waiting reimbursement.
- [N-U16-093] A bundled automated test, read but not executed here, expects that cancelling, deleting or reversing the receipt returns each expense to approved with no entry link, so the receipt can be posted again.

### STATE

- [N-U16-086] Approved goes to posted when a receipt exists; posted goes to paid on full payment; paid or posted goes back to approved when the receipt is reversed, cancelled or its link is cleared.

### OPTIONALITY

- [N-U16-087] Reimbursement through payroll deduction or card-feed reconciliation is offered by settings that belong to modules outside the community edition.

### DEPENDENCY

- [N-U16-089] Settlement depends on the vendor payment, reconciliation and payment-status capabilities of the accounting engine.

### CONSTRAINT

- [N-U16-090] Receipts of employee-paid expenses are held in the employee's work contact; partner and commercial partner are forced from the receipt on every line, so payments cannot be misrouted to another bank account.

### RISK

- [N-U16-091] A receipt that is cancelled is read as paid by the status computation before the link is cleared; the code relies on the cancel handler clearing the link to avoid a false paid status.
- [N-U16-092] Reversal does not reverse the receipt's reimbursement payment; if a payment already exists the corrected expense can be posted again and the employee may be paid twice.

### UNKNOWN

- [N-U16-094] The effect of clearing the entry link through the relation command is stated by a source comment and asserted by a bundled test, but it was not executed here.

## CAP-U16-05 Re-invoicing expenses to customers

### WHAT

- [N-U16-095] An employee expense can be tied to a confirmed customer order so that its cost is billed back to that customer. When the expense is posted, the order receives a new line for the expense, at cost or at the product's sales price depending on the category's re-invoice policy.
- [N-U16-096] If the expense carries no order but its cost allocation points to a project that belongs to an order, the order is found through the project; an order chosen explicitly on the expense always wins.

### WHY

- [N-U16-097] Costs incurred on behalf of a customer (travel, communication, mileage) should be passed on without retyping them into the order or the customer invoice.

### BUSINESS RULE

- [N-U16-098] Re-invoicing applies only when the category's policy is at cost or at sales price and an order is set on the expense; for other categories the order field is cleared automatically.
- [N-U16-099] Re-invoicing works through cost allocation: posting the expense creates analytic entries, and the order line is created from the product line of the entry; if the expense has an order but no allocation, a new allocation account is created for the order.
- [N-U16-100] The target order must be confirmed, not cancelled and not locked; otherwise posting the expense is refused with a message naming the order.
- [N-U16-101] At cost, the price per unit is the posted expense amount divided by the quantity (converted to the order currency); at sales price, it is the price from the order's price list for one unit of the category.
- [N-U16-102] Each re-invoiced expense gets its own order line flagged as an expense line; the line copies the entry's description, cost allocation and, for sales-price categories with a cost, the expense quantity.
- [N-U16-103] Delivered quantity of an expense line is the sum of the analytic quantities from cost entries (amount of zero or less), which is what makes the line billable on the next customer invoice according to the product's invoicing policy.
- [N-U16-104] Reversing, resetting to draft or deleting the expense entry resets the related order line quantity and delivered quantity to zero and detaches the expense.
- [N-U16-105] A credit-side or reversal entry is never re-invoiced, and only lines that carry a cost allocation can create analytic entries.

### STATE

- [N-U16-106] The order shows the expense once it is posted, in payment or paid; expenses still in draft, submitted or approved do not appear on the order.

### OPTIONALITY

- [N-U16-107] Re-invoice policy is set per category; the delivered defaults are meals at sales price, mileage at sales price on delivered quantity, travel and accommodation at cost on delivered quantity, communication at cost and gifts not re-invoiced.
- [N-U16-108] The re-invoice policy field is shown on the category only to users with the all-approver expense role.

### DEPENDENCY

- [N-U16-109] This capability needs sales orders, price lists, cost allocation (analytic) and, for project-based mapping, projects linked to orders.

### CONSTRAINT

- [N-U16-110] Salespeople without access to all orders can still pick any confirmed order of their companies when recording an expense, but only see its name.

### RISK

- [N-U16-111] The order line is created from the category's customer taxes, not from the tax configured on the expense, so the tax billed to the customer can differ from the input tax recovered on the expense.
- [N-U16-112] If reimbursement of the employee has already happened and the entry is reversed to correct the customer billing, the order line resets to zero but the payment stays, so the corrected expense can be billed and reimbursed again.

### UNKNOWN

- [N-U16-113] The runtime effect of reversing an expense whose order line was already invoiced to the customer (quantity reset on an invoiced line) was not executed.

## CAP-U16-06 Timesheet recording, cost valuation and analytic linkage

### WHAT

- [N-U16-114] Employees record time worked against a project (and optionally a task) as a time entry; each entry is a cost-allocation record whose amount is the employee's hourly cost times the time, shown as a negative amount, and it belongs to the project's cost-allocation account.
- [N-U16-115] The time entries are an internal management record: they do not create any ledger entry and only feed project profitability, billing and analysis reports.

### WHY

- [N-U16-116] Knowing what each project costs in labour, and what share of the time is billable, supports pricing, billing and margin decisions without involving payroll.

### BUSINESS RULE

- [N-U16-117] A time entry needs a project (or a task that belongs to a project); time cannot be recorded on a private task, and the entry's company is taken from the task or project.
- [N-U16-118] The entry's employee must be an active employee in the selected companies; when only a user is known, the user's employee in the entry's company is used.
- [N-U16-119] The unit of measure of an entry defaults to the company's project time unit; the encoding unit (hours or days) is a company setting.
- [N-U16-120] The cost of an entry is minus quantity times the employee's hourly cost, converted from the employee's currency into the cost-allocation account's currency at the entry date; it is recomputed when quantity, employee or account changes.
- [N-U16-121] When a project uses employee-based rates, the hourly cost for that employee on that project can be overridden in the project's rate table and then overrides the employee's own cost.
- [N-U16-122] A project that allows time entries must have a cost-allocation account; it is created automatically when the project is created or when time entries are enabled, named after the project and placed in the project plan.
- [N-U16-123] The project, the task and the cost-allocation accounts of an entry must belong to the same company, and the account must be active.
- [N-U16-124] Any other mandatory allocation plan configured for time entries must be present on the project; otherwise the entry is refused.
- [N-U16-125] A project with time entries cannot be deleted until those entries are removed; its cost-allocation account is deleted with it only when empty, and the project's company cannot change once the account has lines.
- [N-U16-126] An internal project with Training, Meeting and Time Off tasks is created for each company and is used for time off and as a default project.

### STATE

- [N-U16-127] A time entry has no approval or locking status in this edition; it can be edited by its owner or an all-timesheet user until it is invoiced or linked to time off.

### OPTIONALITY

- [N-U16-128] Hours or days encoding, the company project time unit, employee reminders and approver reminders are settings; the hourly cost on the employee is optional and defaults to zero.

### DEPENDENCY

- [N-U16-129] Time entries depend on the project, human-resources hourly cost, cost-allocation accounting and unit-of-measure capabilities.

### CONSTRAINT

- [N-U16-130] Users with the own-timesheets role see and change only their own entries on projects visible to employees or shared with them; the all-timesheets role sees all entries on visible projects; the administrator and project managers see all entries on any project.
- [N-U16-131] Employees with time entries cannot be deleted by users without the all-timesheets role unless an active employee also exists.
- [N-U16-132] Hourly cost is visible only to human-resources officers.

### RISK

- [N-U16-133] Because the cost is stored on the entry at the time of recording, later changes in the employee's hourly cost do not restate earlier entries, and the margin of old periods stays on the old rate.
- [N-U16-134] The accountant roles lose visibility of project time entries in the cost-allocation lists because two accounting rules are narrowed to entries without a project, so finance must hold a timesheet role to audit time cost.
- [N-U16-135] Timesheet cost is an analytic figure and is not reconciled to payroll expense; any difference between timesheet cost and real labour cost is not recorded by this capability.

### UNKNOWN

- [N-U16-136] A manager approval or period lock for time entries is not present in this edition; whether it exists in another edition cannot be determined here.
- [N-U16-137] Behaviour of the calendar batch entry with employees working different days, and of the portal timesheet rule (declared inactive), was not executed.

## CAP-U16-07 Billing services and timesheets from sales orders

### WHAT

- [N-U16-138] Service products can be sold under four billing styles: prepaid or fixed price, billed on the time recorded, billed on a manually entered delivered quantity, or billed on milestones reached. The style sets the invoicing basis and the way delivered quantity is measured.
- [N-U16-139] For services billed on time, each time entry is linked to an order line; the delivered quantity of the line is the sum of linked time, and the next customer invoice bills it. Invoicing records which invoice took which time entries.
- [N-U16-140] Prepaid time lines show remaining hours and raise an upsell task for the salesperson when the delivered time passes a threshold of the prepaid quantity.

### WHY

- [N-U16-141] Customers are billed for services in the way agreed (fixed fee, time, milestone, manual) while the company keeps an audit trail of exactly which time was billed and can protect billed time from later edits.

### BUSINESS RULE

- [N-U16-142] The order line for a time entry is found from the task if the task is billable, then from the project; with employee-based pricing it comes from the project's employee-to-line table, falling back to the task and then project lines. The line can be overridden by hand and then stays unless the time is invoiced.
- [N-U16-143] Each time entry has a billable type: billed on time, fixed price, milestones, manual, non-billable, or revenue and cost types for entries without a project; it follows the product's policy and the project's billing mode.
- [N-U16-144] When invoices are created from an order, time entries on lines billed on time are linked to the new draft invoice, optionally limited to a date range chosen in the invoicing dialog, and only entries not yet billed, or whose invoice was cancelled or reversed, are taken.
- [N-U16-145] Time entries linked to an invoice that is not cancelled cannot be edited in quantity, employee, project, task, order line or date on lines billed on time, and cannot be deleted once the invoice is posted.
- [N-U16-146] Posting a credit note that reverses an invoice releases the credited time entries so they become billable again; deleting a draft invoice line releases its time entries without changing what was delivered.
- [N-U16-147] When invoicing a date range, the quantity to invoice for each timesheet line is recomputed from entries in that range, never above delivered minus already billed when credit notes exist.
- [N-U16-148] For milestone-billed lines, delivered quantity is the sum of the percentages of reached milestones times the ordered quantity; milestone billing is only offered when the milestone feature is switched on.
- [N-U16-149] A billable project or task can be linked only to a service order line that is not an expense line; project and task customers must match the order's customer.
- [N-U16-150] The system keeps a mandatory service product for time billing; it cannot be archived, deleted or tied to one company.
- [N-U16-151] Margin on a time-billed order line uses the average actual timesheet cost per unit when the product has no cost of its own; otherwise the product cost applies.

### STATE

- [N-U16-152] A time entry is open until a draft invoice takes it; it becomes locked when that invoice is not cancelled, and open again when the invoice is cancelled, reversed by a credit note, or deleted.

### OPTIONALITY

- [N-U16-153] Employee-based pricing, task-based pricing and project-based pricing are chosen by project configuration; the upsell threshold is per product and defaults to the full prepaid quantity.

### DEPENDENCY

- [N-U16-154] Billing from time depends on sales orders and customer invoicing, time entries, projects and tasks, and optionally on the margin capability.

### CONSTRAINT

- [N-U16-155] Only service products can be linked to billable projects; one employee can appear only once in a project's employee-to-line table.
- [N-U16-156] Project managers can read confirmed service order lines that have a project or task, with no right to change them.

### RISK

- [N-U16-157] A time entry's billed status depends on its invoice state at the time of reading, so cancelling an invoice silently makes billed time editable and re-billable.
- [N-U16-158] A guard intended to stop edits to billable time evaluates a method reference rather than calling it, so the extra not-billed condition never restricts anything and the edit lock relies only on the other checks.
- [N-U16-159] Billing a date range recomputes quantity to invoice directly, which can overwrite a quantity computed from the order line and produce billing that differs from the order status shown before the range was applied.

### UNKNOWN

- [N-U16-160] The effect of partial credit notes on multi-line time invoices and of the legacy invoice status on re-billing was not executed.
- [N-U16-161] How the delivered quantity behaves when timesheet units differ between hours and days on mixed lines was not executed; conversion is by unit factor.

## CAP-U16-08 Sale-to-project generation and project analytic distribution

### WHAT

- [N-U16-162] When an order containing service products is confirmed, the system can automatically create a task in an existing project, a new empty project, or a new project with a task per line; the generated project or task is linked to the order line so time and costs can be tracked against the sale.
- [N-U16-163] A project can also be created from a confirmed order by a button, and a project or task created first can be tied to an order line afterwards; ties made to a draft order confirm that order.
- [N-U16-164] Cost-allocation accounts follow the sale: the project's account is added to the order lines, to customer invoice lines and to vendor bill and purchase lines coded to the project, so revenue and cost can be matched later.

### WHY

- [N-U16-165] Linking each sold service to the work that delivers it lets operations plan hours from the sale and lets finance read profitability per project from one cost-allocation key.

### BUSINESS RULE

- [N-U16-166] Product setting decides what is generated: nothing, a task in a chosen project, an empty project, or a project plus tasks; templates for the project and the task can be configured, and a product that generates a task in a given project cannot also name a project template.
- [N-U16-167] Without templates, one project is created per order and shared by all lines of that order that generate projects; with templates, one project per order and per template.
- [N-U16-168] Re-confirming an order that was cancelled and set back to draft reuses projects and tasks already linked to its lines instead of creating new ones.
- [N-U16-169] The new project takes the order name (with the customer reference when present), the customer, billable status and company; its cost-allocation account is the order's project account if the order already points to a project, otherwise a new account named like the order.
- [N-U16-170] The task is named after the order line or product, carries allocated hours equal to the ordered quantity converted to the company time unit (zero for milestone products), and is unassigned.
- [N-U16-171] Changing the ordered quantity of a line later updates the allocated hours of its task, unless explicitly suppressed.
- [N-U16-172] When products require a task in a global project and neither the order nor the product names one, confirmation fails with a message naming the product.
- [N-U16-173] A project created from an order for a prepaid time product is allocated the sum of ordered hours of all lines that share it, converted by unit factor; units sold as 'unit' are treated as hours.
- [N-U16-174] Cancelling an order detaches its lines from every project that referenced them; the projects themselves are kept.
- [N-U16-175] Order lines receive the project's cost-allocation account on top of any existing distribution, as long as the project's plan is not already used on the line.
- [N-U16-176] A customer invoice line takes the allocation of the project or task linked to its order line when the order line has none, falling back to the single project account found for the line.
- [N-U16-177] A project is billable only if it has a customer; clearing the customer or changing it to one that does not match removes the linked order line.

### STATE

- [N-U16-178] A generated project starts active, billable, linked to the order; its task starts unassigned in the first stage; after cancellation of the order the order link is cleared.

### OPTIONALITY

- [N-U16-179] Generation can be switched off for a single confirmation by a context flag used internally by project-created orders; product-level generation settings default to none.

### DEPENDENCY

- [N-U16-180] This capability needs sales orders, products with service settings, projects and tasks, cost-allocation accounts and the allocation plan of the company.

### CONSTRAINT

- [N-U16-181] Only users in the project manager role can create a project from an order.
- [N-U16-182] Project managers receive read-only access to confirmed service lines tied to projects or tasks; salespeople retain their own order rights.

### RISK

- [N-U16-183] Linking a project or task to a draft order line silently confirms the whole order, which can create revenue commitments from a project screen without sales approval.
- [N-U16-184] Generation runs with elevated rights because salespeople may not have project access; any failure in project creation (for example missing company or plan configuration) blocks order confirmation.
- [N-U16-185] Several projects can share one cost-allocation account, and the matching of costs to an order picks the earliest confirmed order, so cross-assigned costs are possible when allocation accounts are reused.

### UNKNOWN

- [N-U16-186] Project-template duplication behaviour when the template contains sub-tasks and recurrence was not traced in full, and mail or portal side effects of the generated task messages were not executed.

## CAP-U16-09 Project profitability and project cost links (purchase, stock, landed cost, expense, time)

### WHAT

- [N-U16-187] The project dashboard shows revenue and cost per project, split into amounts already invoiced or billed and amounts still to invoice or to bill, with a margin and margin percentage; it is built live from the project's cost-allocation account and the linked orders, invoices, bills, purchase orders, expenses, stock transfers and time entries.
- [N-U16-188] Costs of project goods come from three routes: purchase orders and vendor bills coded to the project, goods moved on stock transfers that are marked to generate project costs, and landed costs on those transfers; employee expenses and time are separate cost lines.

### WHY

- [N-U16-189] Project managers and finance need a single page that says whether a project makes or loses money before the books are closed, using the same allocation key that links sales, purchases, payroll-like time and expenses.

### BUSINESS RULE

- [N-U16-190] Revenue is read from confirmed order lines (to invoice and invoiced, split into down payments and per service type), plus customer invoice lines coded to the project that are not already counted through an order line; draft invoices count as to invoice, posted ones as invoiced.
- [N-U16-191] Down payments are shown on their own line: the invoiced amount is positive and an equal negative amount is shown under to invoice, because the advance will be deducted later.
- [N-U16-192] Cost of goods sold lines in customer invoices coded to the project are reported as costs; other customer invoice lines as revenue.
- [N-U16-193] A purchase order contributes its untaxed amount for the share allocated to the project, as to bill until bills exist; posted bills move the amount to billed and the unbilled remainder stays to bill; refund lines are not counted for the unbilled remainder.
- [N-U16-194] Vendor bills coded to the project and not tied to a purchase order or an expense are shown as vendor bill costs; draft counts to bill, posted counts billed.
- [N-U16-195] Employee expenses that are posted, in payment or paid and coded to the project are shown as expense costs using the untaxed amount, and the corresponding bill lines are excluded from vendor bills to avoid double counting; re-invoiced expenses also appear on the revenue side.
- [N-U16-196] Time entries are counted by billable type with their negative cost; costs from vendor bills seen as cost-allocation lines are skipped to avoid duplicates.
- [N-U16-197] Other cost-allocation lines of the project that are neither time nor linked to a journal line, nor from manufacturing or transfers, are totalled as other revenues if positive or other costs if negative, all shown as already invoiced or billed.
- [N-U16-198] Goods moved by a transfer create cost-allocation entries only when the transfer has a project, its operation type is marked to generate analytic costs, and the move is done or picked; the entry is a cost for outgoing moves and carries the transfer name.
- [N-U16-199] The amount of a goods entry is the stock valuation of the move once done, or an estimate from the product cost while the move is only picked.
- [N-U16-200] Landed costs applied to transfers with a project carry the project's allocation on their valuation lines.
- [N-U16-201] A purchase order created from a replenishment rule for a project inherits the project, and matching existing orders is restricted to the same project.
- [N-U16-202] If mandatory allocation plans exist for stock pickings, the project must have all of them before a goods entry is created.

### STATE

- [N-U16-203] Dashboard amounts have no state of their own: draft documents count as to invoice or to bill, posted documents as invoiced or billed, cancelled documents are ignored where the code filters them.

### OPTIONALITY

- [N-U16-204] The profitability section is shown only for billable projects; each extension (purchase, stock, expense, time) appears only when its module is installed, and action links appear only for users with the matching sales, purchase or accounting role.

### DEPENDENCY

- [N-U16-205] Profitability depends on cost-allocation accounts, customer invoices, vendor bills, purchase orders, stock valuation and transfers, employee expenses and time entries; all of them must carry the project's allocation key.

### CONSTRAINT

- [N-U16-206] Only project users see the panel data, only project managers get profitability values, and only users with sales, purchase or accounting roles get links to the source documents.

### RISK

- [N-U16-207] Figures depend on the allocation key being present on every document; a bill, invoice or transfer with no project allocation is invisible, and one allocated to several accounts counts only its percentage share.
- [N-U16-208] Two extensions use the same section name for different content (materials from time entries without a project and materials from transfers), and one extension reads the sequence of another section, so ordering or merging of those lines may not match the labels.
- [N-U16-209] A purchase order filter compares the order state to a text value with a membership test, so it matches by substring rather than by equality; with the current state names this still selects confirmed orders but is fragile.
- [N-U16-210] The dashboard is a management view, not an accounting statement: amounts are converted at the document date to the project currency and do not tie to ledger balances.

### UNKNOWN

- [N-U16-211] Foreign-currency conversion differences between document dates and report date and the effect of manufacturing cost entries (excluded here) on project margin were not executed.

## CAP-U16-10 Time-off, attendance comparison and project collaboration extensions

### WHAT

- [N-U16-212] Approved time off automatically creates time entries on the company's internal project, so hours of absence are counted as worked-equivalent time in project and attendance analysis; public holidays do the same for every employee on the affected calendar.
- [N-U16-213] A report compares, per employee and day, the hours of attendance with the hours of time entries, with the cost of each at the employee's hourly cost and the difference between them.
- [N-U16-214] Projects and tasks can send a text message to the customer when they reach a stage that has a message template; a mail-client add-in can search projects and create tasks and projects from an email; employee skills are shown on tasks; and a personal to-do list is kept as private tasks of the user.

### WHY

- [N-U16-215] These small extensions keep absence, attendance, customer communication and personal tasks consistent with the project and time data without separate entry.

### BUSINESS RULE

- [N-U16-216] A validated time-off request creates one time entry per working day (or per half-day or hours for flexible calendars) on the company's internal project and time-off task, only if both are configured and the leave type counts as time.
- [N-U16-217] Time entries made from time off cannot be edited or deleted by hand; refusing, cancelling or deleting the request, or setting its duration to zero, removes them, and regenerated entries replace the old ones.
- [N-U16-218] Public holidays create entries for each employee of the affected working calendar, skipping days already covered by validated personal leave, and are regenerated when the holiday is edited or removed; entries of public holidays cannot be modified.
- [N-U16-219] Nobody can record time on the time-off task by hand.
- [N-U16-220] A stage text message is sent only if the project or task has a customer and the stage has a template; it is sent when the record is created in that stage or moved into it.
- [N-U16-221] From the mail add-in, a task is created with the email subject and body for a chosen project and partner, assigned to the calling user; a project can be created by name only.
- [N-U16-222] A to-do is a task with no project and no parent; its name is taken from the first line of its description or defaults to Untitled to-do; it can later be converted to a project task.
- [N-U16-223] To-do access is limited by a rule to private tasks the user is assigned to; every employee has full rights on their own to-dos.

### STATE

- [N-U16-224] Time off entries live as long as the approved request; they disappear when the request leaves the approved state.

### OPTIONALITY

- [N-U16-225] Time off entries need the internal project and a time-off task on the company; the attendance comparison needs the attendance capability; SMS sending needs the text-message module and a template on the stage; the add-in needs the mail plug-in module.

### DEPENDENCY

- [N-U16-226] This capability depends on time off, attendance, human-resources skills, text messaging, the mail add-in framework, projects and the time entry capability.

### CONSTRAINT

- [N-U16-227] The attendance comparison report respects company rules; employees see only their own rows, all-timesheet users see all.
- [N-U16-228] Project managers get create, change and delete rights on text-message templates that target projects or tasks only.

### RISK

- [N-U16-229] Time-off entries carry the employee's hourly cost into project cost, so absences inflate the internal project cost; finance should not read the internal project cost as productive labour cost.
- [N-U16-230] The add-in endpoints accept requests from any origin with a separate authentication mode, so they rely entirely on that mode and on record rules of the calling user.
- [N-U16-231] Customer text messages are sent automatically on stage change with elevated rights, so a mis-set template or stage can message customers without any review.

### UNKNOWN

- [N-U16-232] Delivery of text messages depends on an external gateway and credits and was not executed; failure behaviour (queued, failed or lost) is runtime.
- [N-U16-233] Authentication and rate limits of the mail add-in endpoints depend on the platform's add-in authentication, which was not traced here.
