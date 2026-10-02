# U205 — res.partner: Commercial Partner Hierarchy, Address Types, VAT, bank_ids, company_type
## STATE03 VDR — Restricted Technical Evidence
**Research Unit**: U205  
**Module**: res_partner  
**Addons scoped**: base, account, base_vat  
**Date**: 2026-10-02  
**Gate**: GREEN

---

## 1. Model Definition

**File**: `base/models/res_partner.py`  
**Line**: 184  
**Class**: `ResPartner`  
**Inherits**: `['format.address.mixin', 'format.vat.label.mixin', 'avatar.mixin', 'properties.base.definition.mixin']`  
**Order**: `complete_name ASC, id DESC` (line 188)  
**rec_names_search**: `['complete_name', 'email', 'ref', 'vat', 'company_registry']` (line 189)  
**_check_company_domain**: `models.check_company_domain_parent_of` (line 192)

---

## 2. Key Field Definitions

### 2.1 Hierarchy Fields
| Field | Type | Line | Notes |
|---|---|---|---|
| `parent_id` | Many2one('res.partner') | 215 | index=True, string='Related Company' |
| `parent_name` | Char (related) | 216 | related='parent_id.name', readonly |
| `child_ids` | One2many('res.partner', 'parent_id') | 217 | domain=[('active','=',True)], context={'active_test': False} |
| `commercial_partner_id` | Many2one('res.partner') | 302–305 | computed, stored, recursive=True, index=True |

### 2.2 Company Type / is_company
| Field | Type | Line | Notes |
|---|---|---|---|
| `is_company` | Boolean | 277 | default=False; actual storage field |
| `company_type` | Selection([('person','Person'),('company','Company')]) | 282–284 | compute='_compute_company_type', inverse='_write_company_type'; **interface only — do NOT use in business logic** (comment line 281) |
| `company_id` | Many2one('res.company') | 285 | index=True; multi-company scoping |

### 2.3 Address Type Field
| Field | Type | Line | Selection values |
|---|---|---|---|
| `type` | Selection | 254–259 | `('contact','Contact'), ('invoice','Invoice'), ('delivery','Delivery'), ('other','Other')` |

> **MIGRATION FLAG**: The `'private'` type option (present in v16/v17) is **absent** from the v19 selection list. There are exactly 4 values: contact, invoice, delivery, other.

> **NOTE**: `_complete_name_displayed_types = ('invoice', 'delivery', 'other')` at line 195 — 'contact' type does NOT get a type label appended to the complete name.

### 2.4 VAT Field
| Field | Type | Line | Notes |
|---|---|---|---|
| `vat` | Char | 237 | index=True, string='Tax ID'; `'/'` means explicitly no valid VAT |
| `same_vat_partner_id` | Many2one | 239 | computed, store=False; duplicate VAT detection |

### 2.5 Bank Relationship
| Field | Type | Line | Notes |
|---|---|---|---|
| `bank_ids` | One2many('res.partner.bank', 'partner_id') | 245 | Direct relational — no _compute method; account addon adds `bank_account_count` (partner.py:573) |

### 2.6 Address Display
| Field | Type | Line | Notes |
|---|---|---|---|
| `contact_address` | Char (computed) | 299 | compute='_compute_contact_address'; calls `_display_address()` |

### 2.7 Commercial Company Name
| Field | Type | Line | Notes |
|---|---|---|---|
| `commercial_company_name` | Char (computed, stored) | 306–307 | depends on company_name, parent_id.is_company, commercial_partner_id.name |
| `company_name` | Char | 308 | Raw company name for non-company partners that belong to a company |

---

## 3. commercial_partner_id Computation

**Method**: `_compute_commercial_partner()`  
**File**: `base/models/res_partner.py`  
**Lines**: 514–520  

```python
@api.depends('is_company', 'parent_id.commercial_partner_id')
def _compute_commercial_partner(self):
    for partner in self:
        if partner.is_company or not partner.parent_id:
            partner.commercial_partner_id = partner
        else:
            partner.commercial_partner_id = partner.parent_id.commercial_partner_id
```

**Logic**:
- If `is_company=True` OR no `parent_id` → `commercial_partner_id = self`
- Otherwise → recursively delegates to `parent_id.commercial_partner_id`
- Field is `recursive=True` enabling chain traversal via stored computed field

---

## 4. _fields_sync() — Bidirectional Propagation

**Method**: `_fields_sync()`  
**File**: `base/models/res_partner.py`  
**Lines**: 770–814  

Three-direction synchronization:

**Direction 1 — FROM UPSTREAM (parent → this partner)**:
- If `parent_id` changed: call `_commercial_sync_from_company()` (lines 780–783)
- If `parent_id` set AND `type == 'contact'`: copy parent address fields (lines 785–787)

**Direction 2 — TO UPSTREAM (this partner → parent)**:
- If `type == 'contact'` AND address fields changed: push address to parent (lines 790–800)
- If synced commercial fields (vat) changed AND different from parent: push to parent (lines 801–811)

**Direction 3 — TO DOWNSTREAM (this → children)**:
- `_children_sync(values)` at lines 816–827:
  - If `commercial_partner_id == self`: sync commercial fields to non-company children
  - Sync address fields to `contact`-type children

### _synced_commercial_fields()
**File**: `base/models/res_partner.py:700`  
Returns: `['vat']`  
VAT is the only field propagated bidirectionally (child → parent and parent → children).

### _commercial_fields()
**File**: `base/models/res_partner.py:693`  
Returns: `_synced_commercial_fields() + ['company_registry', 'industry_id']`  
**Extended in account** (partner.py:715–718):
Adds: `property_account_payable_id`, `property_account_receivable_id`, `property_account_position_id`, `property_payment_term_id`, `property_supplier_payment_term_id`, `credit_limit`

### _commercial_sync_to_descendants()
**File**: `base/models/res_partner.py:751–768`  
Iterates `child_ids` filtered to non-company; writes commercial values; recurses.

---

## 5. address_get() — Address Resolution by Type

**Method**: `address_get(adr_pref=None)`  
**File**: `base/models/res_partner.py:1121–1158`  

Algorithm: Depth-first-search through descendant tree, stopping at `is_company` boundaries, then walking up ancestor chain. Returns dict `{type: partner_id}`.  
Default fallback: type 'contact' or the partner itself.

---

## 6. VAT Validation

### Base Account Stub (_run_vat_checks)
**File**: `account/models/partner.py:857–873`  
Base stub: returns `(vat, country.code or '')` with no validation logic.

### _check_vat() in account
**File**: `account/models/partner.py:849–854`  
Calls `_run_vat_checks(partner.commercial_partner_id.country_id, partner.vat, ...)`.  
Uses **commercial partner's country** for VAT country resolution.

### base_vat Override of _run_vat_checks
**File**: `base_vat/models/res_partner.py:107–164`  
Full validation with stdnum integration. Splits VAT prefix, resolves EU cross-country checks.

### _check_vat_number() dispatch
**File**: `base_vat/models/res_partner.py:346–350`  
```python
check_func_name = 'check_vat_' + country_code.lower()
check_func = getattr(self, check_func_name, None) or getattr(stdnum.util.get_cc_module(country_code, 'vat'), 'is_valid', None)
return check_func(vat_number) if check_func else True
```

### Thai VAT (TIN) Validator
**File**: `base_vat/models/res_partner.py:894–896`  
```python
def check_vat_th(self, vat):
    check_func = stdnum.util.get_cc_module('th', 'tin').is_valid
    return check_func(vat)
```
**Reference format** (line 80): `'th': '1234545678781'` — **13-digit TIN**  
Uses Python stdnum library `th.tin` which validates 13-digit Thai Tax Identification Numbers.

### can_edit_vat()
**File**: `account/models/partner.py:751–754`  
Blocked if posted out_invoice/out_refund exists for `commercial_partner_id`.

---

## 7. _find_accounting_partner()

**File**: `account/models/partner.py:710–712`  
```python
def _find_accounting_partner(self, partner):
    ''' Find the partner for which the accounting entries will be created '''
    return partner.commercial_partner_id
```
Account entries always land on the **commercial entity** (root company or individual without parent).

---

## 8. bank_ids → res.partner.bank

### Base Model (res.partner.bank)
**File**: `base/models/res_bank.py:73`  
Key fields:
- `partner_id` Many2one('res.partner') — domain `['|', ('is_company','=',True), ('parent_id','=',False)]` (line 94). Only company partners or root individuals can own bank accounts.
- `acc_number` required, indexed (line 90)
- `sanitized_acc_number` computed+stored (line 92)
- `company_id` related from `partner_id.company_id` (line 101)

### Account Extension (res.partner.bank)
**File**: `account/models/res_partner_bank.py:13`  
Adds:
- `journal_id` One2many('account.journal', 'bank_account_id') (line 17)
- `allow_out_payment` Boolean (line 45) — must be trusted before payments can be sent
- `duplicate_bank_partner_ids` Many2many computed (line 53) — detects same acc_number across partners
- Adds `mail.thread`, `mail.activity.mixin` for tracking

---

## 9. Multi-Company: company_id on res.partner

**Field**: `company_id` Many2one('res.company') at `base/models/res_partner.py:285`  
- Partners with `company_id=False` are shared across all companies
- `_check_company_auto = True` (line 191) enforces company domain checks
- `_check_company_domain = models.check_company_domain_parent_of` (line 192)
- `write()` propagates `company_id` change to all `child_ids` (line 911)
- Constraint `_check_partner_company()` (lines 551–562): if partner `is_company` and is linked to a `res.company`, the `company_id` must match

---

## 10. contact_address / _display_address

**Field**: `contact_address` Char (computed) — `base/models/res_partner.py:299`  
**Compute**: `_compute_contact_address()` at lines 506–508, calls `partner._display_address()`

**_display_address()** at lines 1196–1207:
- Calls `_prepare_display_address()` which builds format args including company_name
- Uses `country_id.address_format` or default `%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s`
- `without_company=False` prepends `%(company_name)s\n` when commercial_company_name is set (line 1193)

---

## 11. Migration Flags (v19 vs v16/v17)

| Flag | Change | Evidence |
|---|---|---|
| `type='private'` REMOVED | v16/v17 had 5 types including 'private'; v19 has only 4 types: contact, invoice, delivery, other | `base/models/res_partner.py:254–259` |
| `title` field REMOVED | No `title` field (res.partner.title, Mr/Ms/Dr) found anywhere in `base/models/res_partner.py`; confirmed absent from grep | Full file scan returned 0 matches |
| `mobile` field REMOVED from base | No `mobile` field in `base/models/res_partner.py`; confirmed absent | Full file scan returned 0 matches |
| `credit`/`debit` in account only | These monetary fields are defined only in `account/models/partner.py:516–540`; NOT in base res.partner | `account/models/partner.py:516, 537` |
| `barcode` company_dependent | `barcode` field is `company_dependent=True` in v19 | `base/models/res_partner.py:309` |
| `website` field PRESENT | `website = fields.Char('Website Link')` at line 246 — still present in v19 base | `base/models/res_partner.py:246` |
| `complete_name` stored + indexed | `complete_name` is now `store=True, index=True` (line 214) — used for default ordering | `base/models/res_partner.py:214` |

---

## 12. Other Notable Fields (account extension)

**File**: `account/models/partner.py`

| Field | Line | Type | Notes |
|---|---|---|---|
| `property_account_payable_id` | 545 | Many2one('account.account'), company_dependent | Liability payable account |
| `property_account_receivable_id` | 550 | Many2one('account.account'), company_dependent | Asset receivable account |
| `property_account_position_id` | 555 | Many2one('account.fiscal.position'), company_dependent | Fiscal position |
| `property_payment_term_id` | 559 | Many2one, company_dependent | Customer payment terms |
| `property_supplier_payment_term_id` | 563 | Many2one, company_dependent | Vendor payment terms |
| `supplier_rank` | 608 | Integer | Incremented on PO/bill creation |
| `customer_rank` | 609 | Integer | Incremented on SO/invoice creation |
| `trust` | 574 | Selection, company_dependent | Debtor trust level |
| `credit_limit` | 523 | Float, company_dependent | Partner-level credit limit |
