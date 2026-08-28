> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 03 — CAPABILITY MAP

| ID | Capability | Observed shape | Evidence |
|---|---|---|---|
| CAP-01 | Chart of accounts | Flat coded list; code Char(64); typed by 19-value enum; grouped by `internal_group`; per-account `reconcile` flag; deprecation supported | SE-17..SE-21 |
| CAP-02 | Account grouping / tagging | `account_account_tag` (10 cols) for reporting classification | DB inventory |
| CAP-03 | Journals | Journal master (35 cols) classifying entries and controlling numbering and hash mode | SE-22, DB |
| CAP-04 | Journal entry (header) | One generic header (96 cols) serving all financial document types via `move_type` | SE-02 |
| CAP-05 | Journal item (line) | Posting atom (76 cols): debit, credit, balance, amount_currency, account, journal, date | SE-15..16, DB |
| CAP-06 | Posting lifecycle | draft → posted → cancel, with reset-to-draft | SE-01, SE-10..12 |
| CAP-07 | Entry numbering | Computed name with prefix/number split; separate no-gap `secure_sequence_number` for hashed journals | SE-13 |
| CAP-08 | Reversal / correction | New opposing entry linked by `reversed_entry_id`, auto-reconciled | SE-07..09 |
| CAP-09 | Reconciliation | Partial (17 cols) accumulating into full (5 cols); enabled per account | CAP-01, DB |
| CAP-10 | Period control | Six company lock dates + time-boxed lock exceptions | SE-24..26 |
| CAP-11 | Multi-company boundary | company_id on journal, account, move; company currency related onto lines | SE-15, DB |
| CAP-12 | Multi-currency boundary | `amount_currency` alongside company-currency debit/credit | SE-15..16 |
| CAP-13 | Analytic coupling | `account_analytic_line` (36 cols) coupled to postings | DB |
| CAP-14 | Audit trail / tamper evidence | Opt-in hash chain per journal; company restrictive audit trail; message-based trail | SE-22..23, SE-26 |
| CAP-15 | Payment status tracking | `payment_state` maintained separately from `state` | SE-14 |

Deferred (dependency only): tax computation, payment execution, asset depreciation,
inventory valuation, statutory reporting.
