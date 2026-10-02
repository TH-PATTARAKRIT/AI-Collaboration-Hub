# U238 Journal entry header model, posting and payment status

Odoo 19 Community — DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

## CAP-U238-01 Journal entry header, posting pipeline and payment status

### WHAT
- Every journal entry has one of seven types: general entry, customer invoice, customer refund, vendor bill, vendor refund, customer receipt and vendor receipt, and the default is a general entry. [N-U238-001]
- Every entry has one of three states: draft, posted or cancelled; an entry cannot be created directly in the posted state. [N-U238-002]
- The payment status has seven values and the same list is reused by a separate display-only status. [N-U238-003]
- The payment status is derived from how receivable or payable lines are matched with payments; one legacy value has no producer in the community code and a separate flag marks documents blocked for payment. [N-U238-004]
- A combined display-only status has eleven values, is not stored, and merges the state with the payment status. [N-U238-005]
- Untaxed, tax, total and residual amounts are computed in the document currency and in the company currency by classifying the lines according to their kind. [N-U238-006]
- A direction sign of plus one or minus one converts the amounts into signed amounts: general entries and money-out types use plus one, all other types use minus one. [N-U238-007]
- The tax totals structure shown on documents is built from the base and tax lines through the shared tax summary engine, and edits to it are written back to the tax amounts. [N-U238-008]
- Posting needs membership of the invoicing group unless the system user acts, and invoice-level problems are collected and reported together in one message. [N-U238-009]
- When the entry date falls in a locked period, posting replaces the accounting date by the first allowed date instead of failing at that step; the hard lock is included in the check. [N-U238-010]
- The official number is assigned as a side effect of leaving the draft state, not by an explicit step in posting. [N-U238-011]
- Posting marks the entry as posted before, then reconciles reversed entries, updates customer and supplier ranks and handles zero-total documents. [N-U238-012]
- Eight installed modules extend posting to add cost lines, payment transaction reconciliation, electronic documents, fleet logs, inter-company checks, email sending and approval responses. [N-U238-013]
- Resetting to draft keeps the reconciliations, while cancelling removes them and cancels linked payments; locked entries cannot be reset to draft. [N-U238-014]
- Integrity hashing is part of the community edition, chains entries together, and runs at posting only for journals in restricted mode. [N-U238-015]
- On a posted entry nine fields are blocked from editing while other header fields stay editable unless the hash protects them. [N-U238-016]
- Deleting an entry is refused when it was posted before in an audit-trail journal and when it is not the last of its chain, except for privileged cases. [N-U238-017]
- The accounting date follows the invoice date, the due date is the latest term maturity, and delivery date and taxable supply date are empty hooks in the base model. [N-U238-018]
- Duplicate detection compares company, partner, type, currency and either the amount and date or the vendor reference, and it only warns. [N-U238-019]
- The commercial partner, delivery address, fiscal position and recipient bank are computed from the partner, and inbound documents prefer the bank of the payment method journal. [N-U238-020]
- A foreign-currency invoice needs a strictly positive currency rate that defaults to the expected rate at the invoice date. [N-U238-021]
- Sale and purchase documents require a journal of matching type, and company and journal are kept consistent by computed defaults. [N-U238-022]
- A scheduled job posts due draft entries in batches with a one-by-one fallback, recurring entries copy themselves, and vendor bill auto-posting depends on company and partner settings. [N-U238-023]
- Reversal copies the entry with the mapped refund type, can cancel by reconciling and posting, and maps both receipt types to refund types. [N-U238-024]
- Header changes drive an ordered synchronisation of payment term, rounding, discount, tax and invoice lines, and invoice lines are only a subset of all lines. [N-U238-025]
- The Thai localisation adds only a report template choice on the entry and provides no tax invoice number, branch or withholding field on the header in the community edition. [N-U238-026]

### WHY
- A single header model lets invoices, refunds, receipts and general entries share one accounting lifecycle.
- Locking, hashing and numbering protect the integrity and chronology of posted records.
- Automatic computation of dates, parties, banks and currency rates reduces manual encoding.

### BUSINESS RULE
- Only drafts can be posted; posted entries cannot be created directly.
- Vendor documents need a bill date; customer documents default to today when no date is given.
- Customer and vendor invoices need a partner; negative totals are refused.
- Posted entries keep their lines, partner, dates, terms, currency, fiscal position and rounding method frozen.

### STATE
- Draft moves to posted by posting, and posted or cancelled moves return to draft by resetting.
- Draft moves to cancelled by cancelling; posted moves are first reset and then cancelled.
- Future-dated draft entries with automatic posting wait for the scheduled job.

### OPTIONALITY
- Hashing applies only to journals in restricted mode or on explicit request.
- Vendor bill auto-posting is switched on by company and partner settings.
- Delivery date, taxable supply date and the Thai header concepts are optional hooks or absent.

### DEPENDENCY
- Sales, purchasing, stock valuation, electronic documents, fleet, inter-company and email modules extend posting.
- Payment terms, taxes and line synchronisation are covered by other research units.

### CONSTRAINT
- The hard lock date and other lock dates limit dates of posted entries.
- The strictly positive currency rate and journal type matching are enforced on save.
- A vendor bill in automatic posting must carry a bill date.

### RISK
- A date adjusted by the lock check can still fall in a lock and fail later when saved.
- Resetting a reconciled entry to draft behaves differently from earlier versions.
- Receipt reversal mapping differs from what an earlier unit documented.

### UNKNOWN
- Runtime behaviour of payment status with real reconciliations.
- Hash chain behaviour when restricted mode is enabled.
- Scheduling details of the posting job and cash-basis multi-entry posting.
- Comparison with earlier versions is pending verification because no migration scripts are present.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U238-C01 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:143 | move_type | FACT | always | — | The move type selection has seven values with default entry | N-U238-001 |
| U238-C02 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:134 | Cancelled | FACT | always | — | The state selection has three values and creation as posted is refused | N-U238-002 |
| U238-C03 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:49 | PAYMENT_STATE_SELECTION | FACT | always | — | The payment state selection has seven values reused by the display status | N-U238-003 |
| U238-C04 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1234 | def _compute_payment_state | INFERENCE | invoice-like moves with reconciled lines | RT | Payment state is derived from reconciliation of receivable and payable lines | N-U238-004 |
| U238-C05 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1329 | def _compute_status_in_payment | FACT | always | — | The status in payment field is non-stored with eleven values | N-U238-005 |
| U238-C06 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1180 | def _compute_amount | FACT | always | — | Amounts are derived by classifying lines by display type | N-U238-006 |
| U238-C07 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1158 | def _compute_direction_sign | FACT | always | — | The direction sign drives the signed amount fields | N-U238-007 |
| U238-C08 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1836 | def _compute_tax_totals | FACT | always | — | The tax totals structure comes from the tax-totals summary engine | N-U238-008 |
| U238-C09 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5584 | access rights to post an invoice | FACT | posting | — | Posting requires the invoice group and aggregates validation errors | N-U238-009 |
| U238-C10 | PCO-F01 | account/models/account_move.py:5704 | _get_violated_lock_dates | FACT | date violates a lock date | RT | Posting replaces the date through the lock-date adjustment without raising | N-U238-010 |
| U238-C11 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:966 | _set_next_sequence | FACT | posted state with a date and no real name | — | Sequence assignment is triggered by the name compute | N-U238-011 |
| U238-C12 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5759 | posted_before | FACT | posting | RT | Posting writes state and posted-before flag then runs the post-hooks | N-U238-012 |
| U238-C13 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:124 | posted = super()._post(soft) | FACT | extension modules installed | — | Eight module extensions wrap posting | N-U238-013 |
| U238-C14 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6269 | def button_draft | INFERENCE | reset or cancel | RT | Reset keeps reconciliations while cancel removes them | N-U238-014 |
| U238-C15 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4625 | def _hash_moves | FACT | restricted hash mode or explicit hashing | RT | Integrity hashing is present and chains entries | N-U238-015 |
| U238-C16 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3960 | unmodifiable_fields | FACT | writing a posted move | — | Nine fields are blocked on posted moves | N-U238-016 |
| U238-C17 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4069 | _unlink_account_audit_trail_except_once_post | FACT | deleting a move | RT | Deletion is refused for audit-trail journals and chain members | N-U238-017 |
| U238-C18 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:862 | def _compute_date | FACT | always | — | Accounting date, due date and hook stubs for delivery and supply dates | N-U238-018 |
| U238-C19 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2085 | def _fetch_duplicate_reference | FACT | sale and purchase documents | RT | Duplicate detection only warns | N-U238-019 |
| U238-C20 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1053 | def _compute_partner_bank_id | FACT | always | — | Partner-derived fields and recipient bank selection | N-U238-020 |
| U238-C21 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2873 | _check_invoice_currency_rate | FACT | invoice-like with foreign currency | — | The currency rate must be strictly positive | N-U238-021 |
| U238-C22 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:2850 | _check_journal_move_type | FACT | always | — | Journal type must match the document type | N-U238-022 |
| U238-C23 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6460 | def _autopost_draft_entries | FACT | scheduled run | RT | Scheduled posting with per-move fallback | N-U238-023 |
| U238-C24 | SDV-F07 | account/models/account_move.py:5495 | def _reverse_moves | FACT | reversal | CONTRA | Reversal maps both receipt types to refund types | N-U238-024 |
| U238-C25 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3722 | def _get_sync_stack | FACT | line changes on invoice-like moves | — | Ordered synchronisation stack for generated lines | N-U238-025 |
| U238-C26 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:7 | def _get_name_invoice_report | INFERENCE | Thai company | — | Only a report template override exists for Thailand | N-U238-026 |
