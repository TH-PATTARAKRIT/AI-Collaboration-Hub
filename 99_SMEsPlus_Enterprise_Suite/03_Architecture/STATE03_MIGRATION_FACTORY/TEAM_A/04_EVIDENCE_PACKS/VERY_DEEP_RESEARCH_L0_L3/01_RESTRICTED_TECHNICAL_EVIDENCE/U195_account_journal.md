# U195 — account.journal: Journal Type Architecture, Sequence, Lock, Bank/Cash Controls
**Level:** L3 Deep Technical  
**Unit:** U195 | Group: G01 | Priority: P1  
**Source:** `odoo/addons/account/models/account_journal.py` (1331 lines), `account/models/sequence_mixin.py`, `account/models/account_move.py`  
**Odoo Version:** 19.0.post20260921 Community  
**Produced:** 2026-10-02  

---

## 1. Model Definition & Core Identity

**Model name:** `account.journal`  
**Table:** `account_journal`  
**Description:** "Journal"  
**Order:** `sequence, type, code`  
**Mixins inherited:**
- `portal.mixin`
- `mail.alias.mixin.optional`
- `mail.thread`
- `mail.activity.mixin`

**Company check:**
```python
_check_company_auto = True
_check_company_domain = models.check_company_domain_parent_of
```
This means child companies can see parent-company journals. It does NOT mean journals are shared — each journal is still bound to exactly one company_id.

**Record name search:** `['name', 'code']`

---

## 2. `type` Field — Six Values in Odoo 19

```python
type = fields.Selection([
    ('sale', 'Sales'),
    ('purchase', 'Purchase'),
    ('cash', 'Cash'),
    ('bank', 'Bank'),
    ('credit', 'Credit Card'),
    ('general', 'Miscellaneous'),
], required=True)
```

**Odoo 19 adds `credit`** (Credit Card) as a distinct type, absent in Odoo 16/17.

| Type | Default Account Type | Payment Methods | Suspense | Alias | Refund Seq | Payment Seq |
|---|---|---|---|---|---|---|
| sale | income% | No | No | Yes | Yes | No |
| purchase | expense% | No | No | Yes | Yes | No |
| cash | asset_cash | Yes (bank/cash/credit) | Yes | No | No | Yes |
| bank | asset_cash | Yes (bank/cash/credit) | Yes | No | No | Yes |
| credit | liability_credit_card | Yes (bank/cash/credit) | Yes | No | No | Yes |
| general | % (all types) | No | No | No | No | No |

**Default account domain logic** (`_get_default_account_domain`):
- `bank` → `asset_cash` or `liability_credit_card`
- `credit` → `liability_credit_card` only
- `cash` → `asset_cash` only
- `sale` → `income`, `income_other`
- `purchase` → `expense`, `expense_depreciation`, `expense_direct_cost`
- `general` → all account types

---

## 3. `code` Field — Sequence Prefix

```python
code = fields.Char(
    string='Sequence Prefix',
    size=5,
    compute='_compute_code', readonly=False, store=True, required=True, precompute=True,
)
_code_company_uniq = models.Constraint('unique (company_id, code)', 'Journal codes must be unique per company.')
```

**Auto-generation** (`_get_next_journal_default_code`):
```python
prefix_map = {
    'sale': 'INV', 'purchase': 'BILL', 'cash': 'CSH',
    'bank': 'BNK', 'credit': 'CCD', 'general': 'MISC',
}
```
Iterates suffix 1–99 until an unused code is found within the company. Maximum code length = 5 characters.

On type change via form (`_onchange_type`), code is reset to `False` and recomputed.

**Copy semantics:** When copying a journal, `copy_data` finds the next unique code by stripping digits from the prefix and incrementing.

---

## 4. Sequence Architecture — `sequence.mixin`

`account.move` inherits `sequence.mixin` (abstract model at `account/models/sequence_mixin.py`).

### Key fields on account.move
```python
sequence_prefix = fields.Char(compute='_compute_split_sequence', store=True)
sequence_number = fields.Integer(compute='_compute_split_sequence', store=True)
```

### Regex patterns
Five mutually-exclusive patterns, tried in priority order:
1. `_sequence_year_range_monthly_regex` → reset `'year_range_month'`
2. `_sequence_monthly_regex` → reset `'month'`
3. `_sequence_year_range_regex` → reset `'year_range'`
4. `_sequence_yearly_regex` → reset `'year'`
5. `_sequence_fixed_regex` → reset `'never'`

account.move overrides these:
```python
@property
def _sequence_monthly_regex(self):
    return self.journal_id.sequence_override_regex or super()._sequence_monthly_regex
```
(Same for yearly and fixed.) This means `sequence_override_regex` on the journal completely replaces the parsing regex.

### `_get_last_sequence_domain` (account.move extension)
```python
where_string = "WHERE journal_id = %(journal_id)s AND name != '/'"
```
Further conditionals:
- `refund_sequence=True` → separates refund types `('out_refund', 'in_refund')` from non-refund
- `payment_sequence=True` → separates entries by `origin_payment_id IS NULL`
- `is_self_billing=True` → separates by `commercial_partner_id`

**Concurrency safety:** sequence cache (`sequence.mixin`) stored in `cr.cache` keyed by `(seq_format, seq_index)`. Cleared on write of `_sequence_field`. Relies on unique constraint locking at DB level.

### `refund_sequence` (computed)
```python
journal.refund_sequence = journal.type in ('sale', 'purchase')
```
Default True for sale/purchase. When True, credit notes get a completely separate number series (e.g., RINV/2024/00001 vs INV/2024/00001).

### `payment_sequence` (computed)
```python
journal.payment_sequence = journal.type in ('bank', 'cash', 'credit')
```
Default True for bank/cash/credit. Separates payment records from bank transaction entries.

### `is_self_billing`
Boolean field. When True, invoices use a per-commercial-partner sequence.

---

## 5. Hash Chain Lock — `restrict_mode_hash_table`

```python
restrict_mode_hash_table = fields.Boolean(
    string="Secure Posted Entries with Hash",
    help="If ticked, when an entry is posted, we retroactively hash all moves in the sequence from the entry back to the last hashed entry...")
```

### Immutability rule
`write()` validation:
```python
if 'restrict_mode_hash_table' in vals and not vals.get('restrict_mode_hash_table'):
    journal_entry = self.env['account.move'].sudo().search_count(domain, limit=1)
    if journal_entry:
        raise UserError(_("You cannot modify the field %s of a journal that already has accounting entries."))
```
Once hash mode is enabled and entries are hashed, it **cannot be disabled**.

### Hash calculation (`_calculate_hashes`)
Uses SHA-256. Chain: each move hashes `previous_hash + JSON(current_record_values)`.

```python
hash_string = sha256((previous_hash + current_record).encode('utf-8')).hexdigest()
move2hash[move] = f"${hash_version}${hash_string}" if hash_version >= 4 else hash_string
```

**Hash version integrity fields:**
- v1: `['date', 'journal_id', 'company_id']`
- v2/3/4: `['name', 'date', 'journal_id', 'company_id']` + line-level fields

**`inalterable_hash`** on account.move: stored result; blocks field-write if set:
```python
violated_fields = set(vals).intersection(move._get_integrity_hash_fields() + ['inalterable_hash'])
if move.inalterable_hash and violated_fields:
    raise ...
```

**`secured`** computed field:
```python
move.secured = bool(move.inalterable_hash)
```

---

## 6. Bank Journal Controls

```python
bank_account_id = fields.Many2one('res.partner.bank', ondelete='restrict', copy=False, index='btree_not_null')
bank_statements_source = fields.Selection(selection=_get_bank_statements_available_sources, default='undefined')
bank_acc_number = fields.Char(related='bank_account_id.acc_number', readonly=False)
bank_id = fields.Many2one('res.bank', related='bank_account_id.bank_id', readonly=False)
```

**Constraint** (`_check_bank_account`):
1. `bank_account_id.company_id` must match `journal.company_id`
2. `bank_account_id.partner_id` must equal `company_id.partner_id`

**`bank_statements_source`:** Base value is `'undefined'`. Modules (e.g., `account_bank_statement_import`, online sync providers) extend `_get_bank_statements_available_sources()` to add their own sources.

**`_prepare_liquidity_account_vals`**: Auto-creates `asset_cash` account on journal creation.

**On currency change:** `default_account_id.currency_id` is synced to `journal.currency_id`.

**Outstanding payments accounts:** Each `inbound_payment_method_line_id.payment_account_id` stores the outstanding receipts account; `outbound` side stores outstanding payments account.

---

## 7. Cash Journal Controls

**Profit/Loss accounts** (cash difference handling):
```python
profit_account_id = fields.Many2one(..., domain="[('account_type', 'in', ('income', 'income_other'))]", string='Profit Account')
loss_account_id = fields.Many2one(..., domain="[('account_type', '=', 'expense')]", string='Loss Account')
```
Auto-filled from company defaults (`default_cash_difference_income_account_id` / `default_cash_difference_expense_account_id`) for cash/bank journals.

**`cash_control`:** This field does NOT exist on `account.journal` in Odoo 19 Community. Cash register session management is handled through `account.payment` and `pos.session` (POS addon), not via a `cash_control` boolean on the journal. The `outbound_payment_method_line_ids` field lists allowed outbound payment methods.

---

## 8. Suspense Account

```python
suspense_account_id = fields.Many2one(
    comodel_name='account.account',
    domain="[('account_type', '=', 'asset_current')]",
    compute='_compute_suspense_account_id', readonly=False, store=True,
)
```

**Only for:** `type in ('bank', 'cash', 'credit')` — others set to False.

**Default resolution chain:**
1. Keep existing value if already set
2. Fall back to `company_id.account_journal_suspense_account_id`
3. Otherwise False

Bank statement lines are posted to the suspense account until final reconciliation assigns the correct account.

---

## 9. `account_control_ids` — Status in Odoo 19 Community

**This field is NOT present as a native field on `account.journal` in Odoo 19 Community.** 

Evidence: the field name `account_control_ids` appears in:
- i18n translation files (legacy from older versions)
- Test helper code at `account/tests/common.py` where it is **dynamically created** as `x_account_control_ids` (custom field prefix) specifically to test the account-merge wizard's many2many reference tracking

In prior Odoo versions (≤16) `account_control_ids` was a Many2many on `account.journal` restricting which `account.account` records could be used in journal entries. **This restriction mechanism was removed from Odoo 19 Community core.**

---

## 10. Mail Alias — Incoming Document Creation

```python
alias_name = fields.Char(help="Send one separate email for each invoice.\nAny file extension will be accepted.\nOnly PDF and XML files will be interpreted by Odoo")
```

**`_alias_get_creation_values()`:**
```python
values['alias_model_id'] = self.env['ir.model']._get_id('account.move')
defaults['move_type'] = {
    'purchase': 'in_invoice',
    'sale': 'out_invoice',
}.get(self.type, 'entry')
```

- Aliases only created for `sale` and `purchase` journals.
- Incoming email → creates `account.move` with appropriate `move_type` and `journal_id`.
- `_alias_prepare_alias_name`: falls back through `alias_name → name → code → type` to find an ASCII-safe name; appends company identifier for non-main companies.

---

## 11. Company Isolation

```python
company_id = fields.Many2one('res.company', required=True, readonly=True, index=True, default=lambda self: self.env.company)
```

**Rules:**
- `company_id` is readonly (cannot be changed via UI once set)
- `_check_company_consistency`: raises `UserError` if you attempt to change `company_id` when journal entries exist linked to a different company
- `_check_company_domain = models.check_company_domain_parent_of`: child companies can see parent journals (multi-company / branch structure)
- Journal code must be unique per company (`_code_company_uniq`)
- Bank account must belong to company's partner (`_check_bank_account`)

---

## 12. `AccountJournalGroup`

```python
_name = 'account.journal.group'
_check_company_domain = models.check_company_domain_parent_of
```
- `company_id`: optional; if None, visible to all companies
- `excluded_journal_ids`: Many2many of journals to exclude from a ledger group in reports
- `_uniq_name`: unique per company

---

## 13. Payment Method Lines

- `inbound_payment_method_line_ids` / `outbound_payment_method_line_ids`: only available for `type in ('bank', 'cash', 'credit')`
- `_compute_inbound_payment_method_line_ids` clears and rebuilds when type or currency changes
- Methods can be `unique` (one journal per company), `electronic` (one per company+provider), or `multi` (unlimited)
- `_check_payment_method_line_ids_multiplicity` enforces uniqueness constraints

---

## 14. Non-Deductible Account

```python
non_deductible_account_id = fields.Many2one(
    comodel_name='account.account',
    string='Private Share Account',
    help="Account used to register the private part of mixed expenses.",
)
```
Used by purchase journals for splitting business/private expense portions.

---

## 15. Archiving Constraint

```python
@api.constrains('active')
def _check_auto_post_draft_entries(self):
    for journal in self.filtered(lambda j: not j.active):
        pending_moves = self.env['account.move'].search([
            ('journal_id', '=', journal.id), ('state', '=', 'draft')
        ], limit=1)
        if pending_moves:
            raise ValidationError(...)
```
Cannot archive a journal with draft entries.

---

## Source File References

| File | Lines | Key Content |
|---|---|---|
| `account/models/account_journal.py` | 1–1331 | Full AccountJournal model |
| `account/models/sequence_mixin.py` | 1–300+ | SequenceMixin abstract |
| `account/models/account_move.py` | ~80–100, 4201–4260, 4590–4804 | Hash chain, sequence domain |
| `account/tests/common.py` | 2329–2336 | account_control_ids as test-only custom field |
