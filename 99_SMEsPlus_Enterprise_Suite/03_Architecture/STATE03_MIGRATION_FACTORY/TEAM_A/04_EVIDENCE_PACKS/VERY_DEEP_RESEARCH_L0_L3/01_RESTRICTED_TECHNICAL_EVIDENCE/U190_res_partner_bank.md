# U190 — res.partner.bank: Bank Account Model, IBAN Validation, BIC, Thai L3
**Unit:** U190 | **Group:** G03 | **Priority:** P1 | **Status:** STUDIED  
**Researcher:** DeepSeek STATE03 VDR Worker  
**Date:** 2026-10-02  
**Source Base:** Odoo Community 19.0.post20260921

---

## CLAIMS TABLE (19 claims)

| # | Claim ID | Layer | Source File (relative to addons/) | Symbol / Line | Claim Statement | Evidence Quote / Key Line | Confidence | Arch Impact | Notes |
|---|----------|-------|----------------------------------|---------------|-----------------|--------------------------|-----------|-------------|-------|
| 1 | U190-C01 | L0 | base/models/res_bank.py:16 | `ResBank._name` | Model `res.bank` is the bank-institution registry, separate from partner bank accounts. Fields: name (required), bic, country, active, email, phone, street, city, state. | `_name = 'res.bank'` | HIGH | Schema | res.bank is institution-level; res.partner.bank is account-level. |
| 2 | U190-C02 | L0 | base/models/res_bank.py:33 | `ResBank.bic` | BIC is stored on `res.bank`, indexed, and auto-uppercased on create and write. It is optional. | `bic = fields.Char('Bank Identifier Code', index=True` … `vals['bic'] = vals['bic'].upper()` | HIGH | Schema | BIC/SWIFT stored at institution level, not account level. |
| 3 | U190-C03 | L0 | base/models/res_bank.py:88 | `ResPartnerBank.acc_number` | `res.partner.bank` stores acc_number (required Char), bank_id (FK to res.bank), partner_id (FK to res.partner, required), and company_id (computed from partner). | `acc_number = fields.Char('Account Number', required=True` | HIGH | Schema | Core fields of the bank-account entity. |
| 4 | U190-C04 | L0 | base/models/res_bank.py:92 | `sanitized_acc_number` | `sanitized_acc_number` is a stored computed field derived from `acc_number` by stripping all non-alphanumeric characters and uppercasing via `sanitize_account_number()`. | `sanitized_acc_number = fields.Char(compute='_compute_sanitized_acc_number', store=True)` | HIGH | Schema | Used for uniqueness constraint and searching. |
| 5 | U190-C05 | L1 | base/models/res_bank.py:10–13 | `sanitize_account_number()` | Sanitization strips all `\W+` characters (non-word chars including spaces, dashes, dots) and uppercases the result. Applies to both reads (`_search_acc_number`) and writes. | `return re.sub(r'\W+', '', acc_number).upper()` | HIGH | Behavior | Ensures consistent comparison regardless of formatting input. |
| 6 | U190-C06 | L1 | base/models/res_bank.py:106–109 | `_unique_number` constraint | A SQL UNIQUE constraint enforces `unique(sanitized_acc_number, partner_id)`, preventing the same sanitized account number from being stored twice for the same partner. | `_unique_number = models.Constraint('unique(sanitized_acc_number, partner_id)', ...)` | HIGH | Integrity | Constraint is per-partner, not global; the same number can exist for different partners. |
| 7 | U190-C07 | L1 | base/models/res_bank.py:123–126 | `_compute_acc_type` | `acc_type` is a computed (not stored) Selection field whose value is determined by calling `retrieve_acc_type(acc_number)`. Base returns `'bank'` always; `base_iban` overrides to return `'iban'` when valid. | `bank.acc_type = self.retrieve_acc_type(bank.acc_number)` | HIGH | Behavior | acc_type is inferred, not user-set. |
| 8 | U190-C08 | L2 | base_iban/models/res_partner_bank.py:68–85 | `validate_iban()` | IBAN validation performs three checks: (1) country code prefix must be in `_map_iban_template` dict, (2) length and alphanumeric regex must match the country template, (3) mod-97 check on rearranged digits must equal 1. | `if digits % 97 != 1: raise ValidationError(...)` | HIGH | Validation | Thailand (TH) is NOT in `_map_iban_template`, so Thai accounts cannot be IBAN type. |
| 9 | U190-C09 | L2 | base_iban/models/res_partner_bank.py:110–128 | IBAN auto-format on create/write | When `acc_number` is provided and passes IBAN validation during create or write, it is automatically reformatted to grouped-4 format (e.g. `GB29 NWBK 6016 1331 9268 19`) via `pretty_iban()`. | `vals['acc_number'] = pretty_iban(normalize_iban(vals['acc_number']))` | HIGH | Behavior | Reformatting happens silently; raw input is not preserved. |
| 10 | U190-C10 | L2 | base_iban/models/res_partner_bank.py:92–95 | `_get_supported_account_types()` | When `base_iban` is installed, the supported account types list is extended to include `('iban', 'IBAN')` in addition to the base `('bank', 'Normal')`. | `rslt.append(('iban', self.env._('IBAN')))` | HIGH | Config | acc_type selection list is additive via super() chain. |
| 11 | U190-C11 | L1 | base/models/res_bank.py:101 | `company_id` derivation | `company_id` on `res.partner.bank` is derived as a stored related field from `partner_id.company_id`. It is read-only and not directly writable. | `company_id = fields.Many2one('res.company', related='partner_id.company_id', store=True, readonly=True)` | HIGH | Multi-company | Bank accounts inherit company scope from their partner, not from a direct company_id field. |
| 12 | U190-C12 | L2 | account/models/res_partner_bank.py:17–20 | `journal_id` one2many | The `account` module adds a `journal_id` One2many from `account.journal` to res.partner.bank, constrained so each bank account may belong to at most one journal. | `if len(bank.journal_id) > 1: raise ValidationError(...)` | HIGH | Accounting | One bank account : one journal maximum. |
| 13 | U190-C13 | L2 | account/models/account_journal.py:247 | `account_journal.bank_account_id` | `account.journal` stores `bank_account_id` as a Many2one to `res.partner.bank`. A constraint checks that the bank account's company matches the journal's company, and that the bank account's partner is the journal's company partner. | `bank_account_id = fields.Many2one('res.partner.bank', ...)` | HIGH | Accounting | Journal-to-bank-account link enforces company and partner alignment. |
| 14 | U190-C14 | L1 | base/models/res_bank.py:165–172 | Soft-delete pattern | `unlink()` is overridden to call `action_archive()` instead of hard-deleting, returning a reload action. The `active` field (default True) drives the archive/restore pattern. | `def unlink(self): self.action_archive(); return True` | HIGH | Data lifecycle | Bank accounts are never truly deleted; they are archived. |
| 15 | U190-C15 | L2 | account/models/res_partner_bank.py:288–307 | Archive guard on create | The `account` module's create override raises a UserError if an archived bank account already exists with the same acc_number + partner_id, preventing silent shadow records. | `raise UserError(_("A bank account ... already exists ... but is archived. Please unarchive it instead."))` | HIGH | Integrity | Prevents duplicate-key errors from archived records. |
| 16 | U190-C16 | L2 | account/models/res_partner_bank.py:273–283 | `allow_out_payment` trust gate | The `allow_out_payment` flag gates outgoing payment usage. Enabling it requires the `account.group_validate_bank_account` group or system admin. Trusted accounts lock acc_number and partner_id from further edits. | `lock_fields = {'acc_number', 'sanitized_acc_number', 'partner_id', 'acc_type'}` | HIGH | Security | Anti-fraud: account details frozen once trusted. |
| 17 | U190-C17 | L3 | account_qr_code_emv/models/res_bank.py:15 | `proxy_type` base field | The `account_qr_code_emv` module defines `proxy_type` (Selection, default 'none') and `proxy_value` (Char) on `res.partner.bank` as the EMV QR base extension. | `proxy_type = fields.Selection([('none', 'None')], ...)` | HIGH | Localization | Required dependency for any EMV QR (PromptPay / PayNow) implementation. |
| 18 | U190-C18 | L3 | l10n_th/models/res_bank.py:11–14 | Thai proxy_type extension | `l10n_th` adds three proxy types to the EMV QR selection: `ewallet_id` (Ewallet ID), `merchant_tax_id` (Merchant Tax ID), and `mobile` (Mobile Number), implementing Thailand PromptPay via EMV QR method code 29 with AID `A000000677010111`. | `proxy_type = fields.Selection(selection_add=[('ewallet_id', ...), ('merchant_tax_id', ...), ('mobile', ...)])` | HIGH | Localization | `_get_merchant_account_info()` encodes PromptPay payload per Thai BOT spec. |
| 19 | U190-C19 | L3 | l10n_th/models/res_bank.py:16–26 | Thai proxy validation rules | Thai accounts with `proxy_type='merchant_tax_id'` must have a 13-digit value; `proxy_type='mobile'` must have a 10-digit value. QR generation requires THB currency. Mobile numbers are converted: leading `0` → `66` (international prefix), zero-padded to 13 chars. | `tax_id_re = re.compile(r'^[0-9]{13}$')` / `mobile_re = re.compile(r'^[0-9]{10}$')` | HIGH | Localization | Validation fires on both create and write via `@api.constrains`. |

---

## KEY ARCHITECTURE FINDINGS

### Model Hierarchy
```
res.bank                         (institution registry: name, BIC, country)
  └── res.partner.bank           (account record: acc_number, partner_id, bank_id)
        ├── base_iban extension  (adds IBAN type detection and mod-97 validation)
        ├── account extension    (adds journal link, QR, trust/fraud controls)
        └── l10n_th extension    (adds PromptPay proxy_type/value via account_qr_code_emv)
```

### Uniqueness Scope
The UNIQUE constraint is `(sanitized_acc_number, partner_id)` — NOT globally unique. The same account number may exist for two different partners (e.g., a vendor and a company). Multi-company isolation is enforced at the journal level via `bank_account_id.company_id == journal.company_id`.

### Thai L3 Dependencies
l10n_th requires `account_qr_code_emv` (for base `proxy_type`/`proxy_value` fields). The Thai EMV QR payload is encoded as tag-29 with AID `A000000677010111`, compliant with Thailand BOT PromptPay specification. No separate `res.partner.bank` model exists for Thai — all extensions are mixin-based inheritance (`_inherit`).

### payment.provider separation
`payment.provider` (v19 successor to `payment.acquirer`) is a completely separate model in the `payment` module with no direct FK to `res.partner.bank`. Online payment providers are not stored as bank accounts.

---

## SOURCE FILES VERIFIED
- `/addons/base/models/res_bank.py` — lines 1–225
- `/addons/base_iban/models/res_partner_bank.py` — lines 1–218
- `/addons/account/models/res_partner_bank.py` — lines 1–398
- `/addons/account/models/account_journal.py` — lines 247–255, 586–594, 773–783
- `/addons/account_qr_code_emv/models/res_bank.py` — line 15–17
- `/addons/l10n_th/models/res_bank.py` — lines 1–68
