# U56 neutral knowledge — sale bridges, SMS messaging, postal mail integration, social media, spreadsheet dashboards

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> No technical identifiers, no code syntax, no file paths. Plain English only.

---

## Sale profitability and cost bridges

[N-U56-001] A margin reporting bridge links sales order lines to their associated expense records so that the actual cost recorded in the expense system is used as the purchase price for margin computation rather than a static product cost price. The expense amount is divided by the expense quantity to obtain a per-unit cost, which is then converted to the sale order's currency before being stored.

[N-U56-002] A separate bridge connects sales order lines to timesheet data. When a service product's cost is not pre-set and the delivery method is based on recorded hours, the system aggregates the monetary amounts and hours from all analytic time entries linked to that sale line and computes an effective average hourly cost. Lines for ordered, manual-delivery, or milestone services that already have a purchase price are excluded from this recalculation to prevent overwriting previously computed values.

[N-U56-003] A bridge for print-on-demand fulfilment through an external provider bypasses the standard warehouse stock rules for products belonging to that provider, since the provider handles fulfilment directly and no internal picking should be created.

[N-U56-004] A bridge connecting sales, projects, and inventory accounting excludes certain re-invoiceable products from generating duplicate accounting analysis entries when the company uses a specific costing method for accounting. Only products that are not flagged for re-invoicing are allowed to generate these entries.

[N-U56-005] A bridge between sales orders and purchase orders preserves the analytic distribution defined on the linked project when creating purchase order lines for service products. It also copies the project reference to the generated purchase order, so financial analysis remains consistent across both documents.

[N-U56-006] A module marks each sale order line as either a service or a physical product, storing this flag in the database for fast filtering. A database-level partial index accelerates searches that target only service lines, and an optimised name-search path is provided for user interface lookups on service lines.

[N-U56-007] The manufacturing margin bridge has no standalone model code; it only contributes additional automated tests verifying that kit and bill-of-materials cost calculations produce correct per-unit values when nested structures or multi-quantity bills are involved.

---

## SMS messaging infrastructure

[N-U56-008] The SMS subsystem maintains an outgoing message queue where each record carries a unique identifier, a destination number, the message body, an optional link to the sending partner, and a status indicator. New entries in the queue automatically wake a background scheduler to process them. Messages are sent in configurable batches, with separate batch sizes available for different providers.

[N-U56-009] The default SMS provider routes outgoing messages through the Odoo in-app-purchase service at a dedicated endpoint. Batch messages are grouped by content to minimise API calls. The same service supports account registration, phone verification, sender name management, and credit purchase through associated endpoints.

[N-U56-010] SMS messages pass through a state lifecycle: queued, in processing, sent to carrier, delivered to handset, errored, or cancelled. Delivery confirmations and error codes arrive via a public web callback. After processing, message records are flagged for deletion and removed by an automated garbage-collection routine.

[N-U56-011] A tracker model bridges the SMS queue record and the notification record. Because SMS records are deleted after sending, the tracker persists the unique message identifier so that later delivery reports — arriving via callback — can still locate and update the corresponding notification. State transitions in the tracker respect a forward-only rule: a message already confirmed as delivered cannot be moved back to a pending state.

[N-U56-012] All document models that support messaging can send SMS notifications. The system resolves a phone number by checking the document's own phone fields first, then falling back to the linked contact's phone fields if no valid number is found on the document itself.

[N-U56-013] A wizard supports three sending modes: sending to an explicit list of phone numbers, posting a note on a single document, and sending in bulk to a filtered set of records. In bulk mode, records are pre-screened against a phone blacklist, an opt-out list, and a duplicate detector; matched records receive a cancelled status rather than an attempted send.

[N-U56-014] SMS templates are attached to specific document types. Only document types that support messaging and have phone number fields are eligible. Templates can be exposed as actions in the document's action menu, allowing users to trigger an SMS send from any record of the template's target type.

[N-U56-015] Server automation rules can include an SMS step that sends a template message to the records matched by the rule. Three sub-options exist: send the SMS without creating a log note, send it and create a log note, or create only a note without sending.

[N-U56-016] Each mail notification record can now represent an SMS notification as well as an email notification. SMS-specific fields store the destination number, a reference to the originating SMS record, links to tracker records, and a set of SMS-specific failure codes covering missing numbers, wrong formats, provider errors, credit shortfall, blacklisting, delivery failures, and country restrictions.

[N-U56-017] When a batch of SMS messages is sent, the system converts the plain-text body to a message record by making URLs clickable and preserving line breaks as HTML breaks. The original plain-text content is kept separately so that the SMS carrier receives unformatted text.

---

## Twilio SMS provider integration

[N-U56-018] The Twilio provider module replaces the default in-app-purchase SMS gateway at the company level. Each company can independently select between the default provider and Twilio. When Twilio is selected, credentials include an account identifier and an authentication token. A pool of Twilio phone numbers is maintained per company, with country codes assigned to each number so that the sender number is chosen based on the destination country.

[N-U56-019] Twilio messages are sent one at a time (not in a content-grouped batch), using a smaller batch size than the default provider. The Twilio message identifier returned by the carrier is stored on the tracker record for later reference.

[N-U56-020] Twilio notifies the system of delivery status changes through a callback endpoint. The signature of each callback is validated using a keyed hash computed from the callback URL and the sorted POST parameters, ensuring authenticity. A mapped set of Twilio status values and error codes translates to the same internal state and failure vocabulary used by the default provider.

---

## Postal mail integration with accounting

[N-U56-021] The postal mail module extends the invoice sending process with a physical-mail option. When a user selects postal delivery for an invoice, the system checks whether the recipient has a complete valid address. Invoices with invalid addresses are flagged with a warning in the send dialogue. For batch sending, the expected stamp count is displayed.

[N-U56-022] Postal mail letters are created with a reference to the standard invoice report as the document to print. Sending is queued rather than immediate. When an invoice is deleted, any associated postal letters are also removed. In the customer portal, postal mail appears as a selectable invoice delivery method.

---

## Social media account references

[N-U56-023] The company record gains eight fields for storing social media identifiers or profile links covering: a microblogging network, a social networking platform, a code hosting service, a professional networking platform, a video sharing platform, a photo sharing service, a short-video platform, and a community messaging service.

---

## Spreadsheet engine core

[N-U56-024] A shared mixin provides the foundation for all spreadsheet-based features. It stores the spreadsheet content as a binary attachment encoded in a structured format. The mixin validates that all data models and menu references embedded in the spreadsheet definition are still present in the system, raising a validation error if any are missing. This validation runs only in testing environments.

[N-U56-025] An empty spreadsheet is initialised with a default sheet, a revision tracking marker, and the current user's locale settings. The locale controls number formatting, date formatting, time formatting, the decimal separator, the thousands separator, and the formula argument separator.

[N-U56-026] Spreadsheets can be exported as multi-file zip archives in a widely supported office format. Image references within the export are resolved by fetching the binary content from the document attachment store.

[N-U56-027] A batch API allows the frontend to retrieve display names for records across multiple models in a single request, with archived records included via an inactive-record search override.

---

## Spreadsheet currency and locale support

[N-U56-028] The system provides a method that returns the company currency's formatting information — its code, symbol, number of decimal places, and symbol position — for use by the spreadsheet engine's number formatting layer.

[N-U56-029] Currency conversion rates are retrievable by the spreadsheet engine by specifying a source currency code, a target currency code, an optional date, and an optional company. The conversion uses the standard multi-currency rate mechanism.

[N-U56-030] All installed languages can be queried and returned as structured locale objects for the spreadsheet engine. The locale object includes date and time format patterns translated from the system's format tokens, with the formula separator automatically set based on the decimal character.

---

## Spreadsheet accounting formulas

[N-U56-031] The accounting spreadsheet integration exposes several data retrieval endpoints that power built-in financial formulas. These cover: debit and credit amounts, net balance, residual amounts on open items, partner balances filtered by contact, and balances grouped by account tag.

[N-U56-032] All accounting formula endpoints accept date period parameters that can specify a calendar year, fiscal year, calendar month, calendar quarter, or a specific day. Fiscal year boundaries honour the company's configured fiscal year end date and month. Balance-sheet accounts accumulate amounts from the beginning of time to the period end, while income-statement accounts use the period's start and end dates.

[N-U56-033] An audit action is available from spreadsheet accounting cells that opens the underlying journal entry lines filtered to the same domain used to compute the cell value, enabling direct drill-down into source transactions.

[N-U56-034] The accounting integration can report account codes grouped by account type, and can return fiscal year start and end dates for a list of company and date combinations, used by the spreadsheet engine to align its date grouping logic with the company's fiscal calendar.

---

## Spreadsheet dashboards

[N-U56-035] Dashboards are spreadsheet documents published for read-only consumption. Each dashboard belongs to a group, has a display sequence, can be restricted to specific companies, and has access groups controlling who can view it. Users can mark dashboards as favourites.

[N-U56-036] When a dashboard has no data — detected by checking whether its associated data models return any records — and a sample data file is configured, the system substitutes the sample data in the response, so the dashboard displays illustrative content rather than an empty canvas.

[N-U56-037] The dashboard data served to the browser includes the current user's locale settings and the company's default currency injected into the snapshot, so number and currency formatting displays correctly without requiring additional requests.

[N-U56-038] Dashboard groups cannot be deleted if they were installed by a module, preventing breakage of module-installed dashboard configurations.

[N-U56-039] A sharing mechanism creates a copy of a dashboard snapshot accessible via a unique token-bearing URL. The share is publicly accessible to anyone with the link, but the original dashboard must still be readable by the user who created the share. Users with export permission also receive a download link for the spreadsheet file.

[N-U56-040] Dashboard data is served through a dedicated route that reads the company selection from a browser cookie, enabling multi-company users to see data filtered to their active companies without re-authenticating.

---

## Spreadsheet dashboard domain sub-modules

[N-U56-041] Eight domain-specific dashboard packages install pre-built dashboard definitions for accounting, event sales, employee expenses, timesheets, live chat, sales, sales with timesheets, and inventory accounting respectively. Each package activates automatically when both the spreadsheet dashboard module and its corresponding domain module are installed. These packages contribute only dashboard configuration data; they add no additional server-side logic.
