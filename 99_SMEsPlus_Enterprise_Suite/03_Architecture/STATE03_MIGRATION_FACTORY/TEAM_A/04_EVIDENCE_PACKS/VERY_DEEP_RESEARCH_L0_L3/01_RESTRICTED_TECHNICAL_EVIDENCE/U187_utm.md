# U187 — UTM Campaign/Source/Medium Tracking: Technical Evidence
**Unit:** U187 | **Group:** G15 | **Priority:** P3 | **Status:** NOT_STUDIED → STUDIED  
**Source Base:** Odoo Community 19.0.post20260921  
**Evidence Level:** L3 (Deep — all model files read)  
**Date:** 2026-10-02

---

## 1. Module Structure

**Path:** `odoo/addons/utm/`  
**Manifest:** `utm/__manifest__.py`  
- Depends on: `base`, `web`  
- Category: Marketing  
- License: LGPL-3  
- Version: 1.1

**Model files:**
```
utm/models/utm_campaign.py
utm/models/utm_medium.py
utm/models/utm_mixin.py
utm/models/utm_source.py
utm/models/utm_stage.py
utm/models/utm_tag.py
utm/models/ir_http.py
```

---

## 2. Core Models

### 2.1 `utm.campaign` — `utm/models/utm_campaign.py`

```python
class UtmCampaign(models.Model):
    _name = 'utm.campaign'
    _description = 'UTM Campaign'
    _rec_name = 'title'

    active = fields.Boolean('Active', default=True)
    name = fields.Char(string='Campaign Identifier', required=True,
                       compute='_compute_name', store=True, readonly=False,
                       precompute=True, translate=False)
    title = fields.Char(string='Campaign Name', required=True, translate=True)
    user_id = fields.Many2one('res.users', string='Responsible', required=True,
                               default=lambda self: self.env.uid)
    stage_id = fields.Many2one('utm.stage', string='Stage', ondelete='restrict',
                                required=True, copy=False,
                                group_expand='_group_expand_stage_ids')
    tag_ids = fields.Many2many('utm.tag', 'utm_tag_rel', 'tag_id', 'campaign_id',
                                string='Tags')
    is_auto_campaign = fields.Boolean(default=False,
                                       string="Automatically Generated Campaign")
    color = fields.Integer(string='Color Index')
```

**Key constraint:** `UNIQUE(name)` — the campaign identifier slug must be unique.

**`_compute_name()`:** Derives a URL-safe unique identifier from `title` using `utm.mixin._get_unique_names()`. On title "Black Friday" → name "Black Friday"; on collision → "Black Friday [2]".

**`is_auto_campaign`:** Flag set by `utm.mixin._find_or_create_record()` when a campaign is auto-created from a URL param.

**No `company_id` field** — campaigns are shared across all companies.

---

### 2.2 `utm.source` — `utm/models/utm_source.py`

```python
class UtmSource(models.Model):
    _name = 'utm.source'
    _description = 'UTM Source'

    name = fields.Char(string='Source Name', required=True)
    # UNIQUE(name) constraint
```

**Seeded records (noupdate=1):** Search engine, Lead Recall, Newsletter, Facebook, X, LinkedIn, Monster, Glassdoor, Craigslist, Referral.

**Referral is protected** — `_unlink_except_referral` raises `ValidationError` on delete attempt.

**`_generate_name(record, content)`:** Utility to produce a source name from content snippet: truncates to 20 chars + "...", appends model description and creation date. Used by `utm.source.mixin`.

**`UtmSourceMixin`** (abstract) — adds `name` (related to source_id.name) and `source_id` (required Many2one). Handles auto-creation of utm.source on record create (used by mass_mailing, social posts, etc.).

---

### 2.3 `utm.medium` — `utm/models/utm_medium.py`

```python
class UtmMedium(models.Model):
    _name = 'utm.medium'
    _description = 'UTM Medium'
    _order = 'name'

    name = fields.Char(string='Medium Name', required=True, translate=False)
    active = fields.Boolean(default=True)
    # UNIQUE(name) constraint
```

**Seeded records (noupdate=1):** Website, Phone, Direct, Email, Banner, X, Facebook, LinkedIn, Television, Google Adwords.

**Protected mediums:** Email, Direct, Website, X, Facebook, LinkedIn — cannot be deleted (`_unlink_except_utm_medium_record`).

**`_fetch_or_create_utm_medium(name, module='utm')`:** Finds an existing medium by XML ID `{module}.utm_medium_{slug}` or creates one and registers a new `ir.model.data` record.

**NO `_compute_name()`** on utm.medium — `name` is a plain Char. No slug display; uniqueness enforced at DB level.

---

### 2.4 `utm.stage` — `utm/models/utm_stage.py`

```python
class UtmStage(models.Model):
    _name = 'utm.stage'
    _description = 'Campaign Stage'
    _order = 'sequence'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=1)
```

**Default stage:** "New" at sequence=10 (created at module install in `utm_stage_data.xml`, NOT noupdate — always exists).

**ACL:** Regular users read-only; system users full CRUD.

**`stage_id` in campaign:** `ondelete='restrict'` — stages cannot be deleted while campaigns reference them. Kanban group_expand via `_group_expand_stage_ids` shows all stages even if empty.

---

### 2.5 `utm.tag` — `utm/models/utm_tag.py`

```python
class UtmTag(models.Model):
    _name = 'utm.tag'
    _description = 'UTM Tag'
    _order = 'name'

    name = fields.Char(required=True, translate=True)
    color = fields.Integer(default=lambda self: randint(1, 11))
    # unique (name) constraint
```

**Seeded:** One default tag "Marketing" (color=1).  
**ACL:** Regular users read-only; system users full CRUD.  
**Linked to campaigns** via M2M relation table `utm_tag_rel`.

---

## 3. `utm.mixin` — `utm/models/utm_mixin.py`

**Abstract model** providing UTM fields to any consumer:

```python
class UtmMixin(models.AbstractModel):
    _name = 'utm.mixin'
    _description = 'UTM Mixin'

    campaign_id = fields.Many2one('utm.campaign', 'Campaign',
                                   index='btree_not_null')
    source_id = fields.Many2one('utm.source', 'Source',
                                 index='btree_not_null')
    medium_id = fields.Many2one('utm.medium', 'Medium',
                                 index='btree_not_null')
```

All three are indexed (`btree_not_null`) — queries filtering by UTM fields use the index.

**`tracking_fields()`** — canonical URL param → field → cookie mapping:
```python
[
    ('utm_campaign', 'campaign_id', 'odoo_utm_campaign'),
    ('utm_source',   'source_id',   'odoo_utm_source'),
    ('utm_medium',   'medium_id',   'odoo_utm_medium'),
]
```

**`default_get()`:**
- **Skips salesman users** (`sales_team.group_sale_salesman`) unless superuser.
- Reads each cookie (`odoo_utm_campaign`, `odoo_utm_source`, `odoo_utm_medium`) from the HTTP request.
- For Many2one fields: calls `_find_or_create_record()` to resolve string value to a record ID.

**`_find_or_create_record(model_name, name)`:**
- `search([('name', '=ilike', cleaned_name)], limit=1, active_test=False)` — case-insensitive, includes archived.
- Creates new record if none found; sets `is_auto_campaign=True` if applicable.

**`_get_unique_names(model_name, names)`:**
- Batch-safe: computes unique slug names for a list of inputs.
- Strips existing `[N]` counter suffix, searches existing names, fills holes in counter sequence.
- Used by campaign, source, medium `create()` methods.

**`find_or_create_record(model_name, name)`** (public API):
- Returns `{'id': ..., 'name': ...}` dict.
- For UTM tracking models: delegates to `_find_or_create_record`.
- For other models: plain create.

---

## 4. Website / URL Integration — `utm/models/ir_http.py`

```python
class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _set_utm(cls, response):
        domain = cls.get_utm_domain_cookies()
        for url_parameter, __, cookie_name in request.env['utm.mixin'].tracking_fields():
            if url_parameter in request.params \
               and request.cookies.get(cookie_name) != request.params[url_parameter]:
                response.set_cookie(cookie_name, request.params[url_parameter],
                                    max_age=31 * 24 * 3600,   # 31 days
                                    domain=domain,
                                    cookie_type='optional')

    @classmethod
    def _post_dispatch(cls, response):
        cls._set_utm(response)
        super()._post_dispatch(response)
```

**Flow:**
1. Visitor lands on `https://example.com/shop?utm_campaign=xmas&utm_source=facebook&utm_medium=social`
2. `_post_dispatch` fires after every request; `_set_utm` extracts URL params.
3. Cookies `odoo_utm_campaign=xmas`, `odoo_utm_source=facebook`, `odoo_utm_medium=social` are set with 31-day TTL.
4. When visitor submits a form (lead, order, registration), `utm.mixin.default_get` reads cookies and populates `campaign_id`, `source_id`, `medium_id`.

Cookie domain = `request.httprequest.host` — single-host, not cross-subdomain by default.

---

## 5. Models Inheriting `utm.mixin` in Community

| Model | Addon | Notes |
|---|---|---|
| `sale.order` | `sale` | Direct `_inherit`; overrides fields with `ondelete='set null'` |
| `account.move` | `sale` (`sale/models/account_move.py`) | Added by sale addon; UTM propagated from sale.order at invoice creation |
| `crm.lead` | `crm` | Direct `_inherit`; overrides fields with `ondelete='set null'` |
| `hr.applicant` | `hr_recruitment` | Direct `_inherit` |
| `link.tracker` | `link_tracker` | Direct `_inherit`; overrides fields with `ondelete='set null'` |

**`account.move` is NOT in the core `account` addon** — UTM on invoices is installed by the `sale` addon only.

---

## 6. `sale.order` ↔ UTM Linkage (L3)

**File:** `sale/models/sale_order.py` lines 284–286, 1428–1435

```python
# Field overrides (ondelete behaviour)
campaign_id = fields.Many2one(ondelete='set null')
medium_id = fields.Many2one(ondelete='set null')
source_id = fields.Many2one(ondelete='set null')

# Invoice preparation — UTM propagated to account.move
values = {
    ...
    'campaign_id': self.campaign_id.id,
    'medium_id': self.medium_id.id,
    'source_id': self.source_id.id,
    ...
}
```

**Propagation chain:** URL params → browser cookies (31 days) → `utm.mixin.default_get` → `sale.order.campaign_id/source_id/medium_id` → `_prepare_invoice()` copies to `account.move`.

**`_reverse_moves()` in account.move (sale addon):** Preserves UTM fields on credit notes.

---

## 7. Revenue Tracking Fields

**Core UTM module has NO revenue fields.** No `utm.campaign.revenue`, no turnover aggregation.

Revenue attribution is indirect:
- `account.move` carries UTM fields (via sale addon).
- Reporting/BI tools must join `account.move` or `sale.order` with UTM fields.
- No computed revenue field on `utm.campaign` in Community.

---

## 8. Company Scope

**None of the UTM models have `company_id`:**
- `utm.campaign` — no company_id
- `utm.source` — no company_id
- `utm.medium` — no company_id
- `utm.stage` — no company_id
- `utm.tag` — no company_id

**All UTM records are cross-company shared.** In multi-company setups, all companies see the same campaigns, sources, mediums, and stages. This is a deliberate design — marketing taxonomy is global.

---

## 9. ACL Summary

| Model | Group User | Group System |
|---|---|---|
| utm.campaign | R/W/C | R/W/C/D |
| utm.medium | R/W/C | R/W/C/D |
| utm.source | R/W/C | R/W/C/D |
| utm.stage | R only | R/W/C/D |
| utm.tag | R only | R/W/C/D |

Regular users cannot delete campaigns, mediums, or sources — only system admins can.

---

## 10. Key Files

| File | Content |
|---|---|
| `utm/models/utm_campaign.py` | `utm.campaign` model |
| `utm/models/utm_medium.py` | `utm.medium` model + `_fetch_or_create_utm_medium` |
| `utm/models/utm_source.py` | `utm.source` + `UtmSourceMixin` |
| `utm/models/utm_mixin.py` | `utm.mixin` abstract + `utm.source.mixin` |
| `utm/models/utm_stage.py` | `utm.stage` |
| `utm/models/utm_tag.py` | `utm.tag` |
| `utm/models/ir_http.py` | Cookie capture in `_post_dispatch` |
| `utm/security/ir.model.access.csv` | ACL rules |
| `utm/data/utm_medium_data.xml` | 10 seeded mediums |
| `utm/data/utm_source_data.xml` | 10 seeded sources |
| `utm/data/utm_stage_data.xml` | Default "New" stage |
| `sale/models/sale_order.py` | UTM fields on sale.order + invoice propagation |
| `sale/models/account_move.py` | UTM fields on account.move via sale addon |
| `crm/models/crm_lead.py` | UTM fields on crm.lead |
| `hr_recruitment/models/hr_applicant.py` | UTM fields on hr.applicant |
| `link_tracker/models/link_tracker.py` | UTM fields on link.tracker |
