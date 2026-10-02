# U157 — account_bank_statement_import — OFX/CSV/CAMT Import Chain L3

**Unit:** U157 | **G Group:** G01 | **Priority:** P1 | **Gap:** GAP-021  
**Verdict:** ABSENT — The `account_bank_statement_import` module and all format-specific sub-modules (OFX, CSV, CAMT) are NOT present in the Odoo 19.0 Community addons tree.  
**Research date:** 2026-10-02  
**Source tree (READ-ONLY):** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons`

---

## 1. Presence Check Results

| Module | Path Checked | Verdict |
|---|---|---|
| `account_bank_statement_import` | `.../addons/account_bank_statement_import` | ABSENT |
| `account_bank_statement_import_ofx` | `.../addons/account_bank_statement_import_ofx` | ABSENT |
| `account_bank_statement_import_csv` | `.../addons/account_bank_statement_import_csv` | ABSENT |
| `account_bank_statement_import_camt` | `.../addons/account_bank_statement_import_camt` | ABSENT |

No module matching `*bank_statement_import*` was found in the addons listing. No module matching `*ofx*`, `*camt*` was found anywhere in Community addons. No `_parse_file`, `_import_file`, or `import_statement` method was found in any account-related Python file.

---

## 2. VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U157-C001 | PRESENCE-CHECK | `.../addons/account_bank_statement_import` | directory | ABSENT | module not installed | GAP | `account_bank_statement_import` directory does not exist under Community addons root | The dedicated file-format import module is not present in this Community edition installation |
| U157-C002 | PRESENCE-CHECK | `.../addons/account_bank_statement_import_ofx` | directory | ABSENT | module not installed | GAP | `account_bank_statement_import_ofx` directory does not exist | The OFX-specific sub-module is absent from Community addons |
| U157-C003 | PRESENCE-CHECK | `.../addons/account_bank_statement_import_csv` | directory | ABSENT | module not installed | GAP | `account_bank_statement_import_csv` directory does not exist | The CSV-specific sub-module is absent from Community addons |
| U157-C004 | PRESENCE-CHECK | `.../addons/account_bank_statement_import_camt` | directory | ABSENT | module not installed | GAP | `account_bank_statement_import_camt` directory does not exist | The CAMT/ISO-20022 sub-module is absent from Community addons |
| U157-C005 | PARSER-DISPATCH | `.../addons/account/models/account_document_import_mixin.py` | n/a | ABSENT | no bank-import dispatch | GAP | No `_parse_file()` or format-dispatch method exists in any Community account module for bank statements | No bank statement file-format dispatcher is present in the Community codebase |
| U157-C006 | BASE-MODEL | `.../addons/account/models/account_bank_statement.py:10` | `class AccountBankStatement` | C1 | always | C1 | `account.bank.statement` model exists in core account module with `_name = 'account.bank.statement'` | The bank statement header model is defined in the core accounting module |
| U157-C007 | BASE-MODEL | `.../addons/account/models/account_bank_statement.py:74` | `line_ids = fields.One2many(...)` | C1 | always | C1 | `account.bank.statement.line_ids` is a One2many relation to `account.bank.statement.line` | A statement can hold many transaction lines via a one-to-many relationship |
| U157-C008 | BASE-MODEL | `.../addons/account/models/account_bank_statement.py:23` | `reference = fields.Char(...)` | C1 | always | C1 | `reference` field on `account.bank.statement` stores the name of the imported file or external sync reference | The statement stores a reference to its external origin such as an imported filename |
| U157-C009 | LINE-MODEL | `.../addons/account/models/account_bank_statement_line.py:11` | `class AccountBankStatementLine` | C1 | always | C1 | `account.bank.statement.line` uses `_inherits = {'account.move': 'move_id'}` — every statement line is a journal entry | Bank statement lines are implemented as journal entries through model inheritance |
| U157-C010 | LINE-MODEL | `.../addons/account/models/account_bank_statement_line.py:71` | `partner_name = fields.Char(...)` | C1 | always | C1 | `partner_name` field holds the third-party name from an imported file when no partner record exists | An unmatched counterparty name from an electronic import is stored in this field |
| U157-C011 | LINE-MODEL | `.../addons/account/models/account_bank_statement_line.py:74` | `transaction_type = fields.Char()` | C1 | always | C1 | `transaction_type` field records the transaction type code from an electronic import file | The transaction category code sourced from an electronic file is stored on the line |
| U157-C012 | LINE-MODEL | `.../addons/account/models/account_bank_statement_line.py:67` | `account_number = fields.Char(...)` | C1 | always | C1 | `account_number` field stores the raw bank account number before `res.partner.bank` creation during line processing | The counterparty bank account number is held here before a partner bank record is created |
| U157-C013 | LINE-MODEL | `.../addons/account/models/account_bank_statement_line.py:149` | `transaction_details = fields.Json(...)` | C1 | always | C1 | `transaction_details` JSON field stores additional details about the bank statement line | Extended transaction metadata is persisted as a structured JSON value on each line |
| U157-C014 | RECONCILIATION | `.../addons/account/models/account_bank_statement_line.py:129` | `is_reconciled = fields.Boolean(...)` | C1 | always | C1 | `is_reconciled` is a computed stored Boolean on `account.bank.statement.line` driven by `_compute_is_reconciled` | Each statement line carries a computed flag indicating whether reconciliation is complete |
| U157-C015 | RECONCILIATION | `.../addons/account/models/account_bank_statement_line.py:287` | `def _compute_is_reconciled(self):` | C1 | always | C1 | `_compute_is_reconciled` inspects suspense account lines; if suspense balance is zero the line is marked reconciled | The system determines reconciliation status by checking whether amounts remain unmatched on the suspense account |
| U157-C016 | RECONCILIATION | `.../addons/account/models/account_bank_statement_line.py:460` | `def action_undo_reconciliation(self):` | C1 | always | C1 | `action_undo_reconciliation` calls `line_ids.remove_move_reconcile()` and resets lines to default values | Undoing reconciliation removes matching credits/debits and restores the line to its unprocessed state |
| U157-C017 | RECONCILIATION | `.../addons/account/models/account_bank_statement_line.py:488` | `def _find_or_create_bank_account(self):` | C1 | conditional | C1 | `_find_or_create_bank_account` creates a `res.partner.bank` record during reconciliation if `account_number` is set and the system parameter `account.skip_create_bank_account_on_reconcile` is false | Reconciliation can automatically register a new partner bank account when one is first encountered |
| U157-C018 | RECONCILIATION | `.../addons/account/models/account_bank_statement_line.py:504` | `def _get_default_amls_matching_domain(self):` | C1 | always | C1 | `_get_default_amls_matching_domain` builds the domain for finding matching journal entry lines; restricts to posted state, reconcilable accounts, and excludes already-reconciled items | The system constructs a matching domain that restricts candidate journal lines to posted, unreconciled, reconcilable-account entries |
| U157-C019 | DOC-IMPORT-MIXIN | `.../addons/account/models/account_document_import_mixin.py:126` | `class AccountDocumentImportMixin` | C1 | always | C1 | `account.document.import.mixin` is an abstract model providing a generic document import framework with `_get_edi_decoder`, `_extend_with_attachments`, and file-type detection via `_get_import_file_type` | A generic attachment-based import framework exists in the core accounting module but is not wired to bank statement file parsing |
| U157-C020 | DOC-IMPORT-MIXIN | `.../addons/account/models/account_document_import_mixin.py:370` | `def _get_edi_decoder(self, file_data, new=False):` | C1 | always | C1 | `_get_edi_decoder` returns `None` in the base mixin — subclasses or extension modules must override it to provide format-specific decoders | The base import decoder hook returns nothing; bank statement format handling must be contributed by an extension module not present in this Community build |
| U157-C021 | THAI-FORMAT | n/a | n/a | ABSENT | n/a | GAP | No Thai-specific bank statement import module (`*thai*`, `*l10n_th*` import) was found in Community addons | No Thailand-localised bank statement file-import module is present |

---

## 3. Summary

**ABSENT status confirmed.** The `account_bank_statement_import` wizard-based import chain and all format sub-modules (OFX, CSV, CAMT, Thai) are absent from Odoo 19.0 Community. The core `account` module contains the `account.bank.statement` / `account.bank.statement.line` data models and a generic `account.document.import.mixin` infrastructure, but no file-upload wizard, no parser dispatch (`_parse_file`), no format detectors for OFX/CSV/CAMT, and no reconciliation trigger wired to an import event.

**Migration implication:** The import chain must be sourced from Odoo Enterprise, OCA (`account_statement_import` family), or a custom implementation. This is a GAP for the SMEsPlus migration where bank statement file import is expected functionality.
