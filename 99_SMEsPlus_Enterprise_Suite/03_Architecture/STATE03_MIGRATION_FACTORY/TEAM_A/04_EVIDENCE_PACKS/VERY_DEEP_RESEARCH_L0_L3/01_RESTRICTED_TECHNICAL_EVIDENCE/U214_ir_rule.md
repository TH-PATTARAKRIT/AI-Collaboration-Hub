# U214 — ir.rule: Security Rule Model, Domain Evaluation, Groups, Global Rules, sudo Bypass

**Research Unit:** U214  
**Module:** `base` — `odoo/addons/base/models/ir_rule.py`  
**Source SHA256:** `bab57d9acc6c06cb3b6b3fbdd8932864dafe860a9bfba877dd33ddd59eb99b1c`  
**Odoo version:** 19.0.post20260921  
**Status:** GREEN  

---

## 1. Model Definition and Fields

**File:** `odoo/addons/base/models/ir_rule.py`

```
_name = 'ir.rule'
_description = 'Record Rule'
_order = 'model_id DESC,id'
_MODES = ('read', 'write', 'create', 'unlink')
_allow_sudo_commands = False     # line 20
```

### Field inventory (lines 22–31)

| Field | Type | Default | Notes |
|---|---|---|---|
| `name` | Char | — | Rule label |
| `active` | Boolean | True | Soft-disable without deletion |
| `model_id` | Many2one `ir.model` | required | ondelete cascade; indexed |
| `groups` | Many2many `res.groups` | — | via `rule_group_rel`; ondelete restrict |
| `domain_force` | Text | — | Python domain expression evaluated by `safe_eval` |
| `perm_read` | Boolean | True | Controls read-mode applicability |
| `perm_write` | Boolean | True | Controls write-mode applicability |
| `perm_create` | Boolean | True | Controls create-mode applicability |
| `perm_unlink` | Boolean | True | Controls delete-mode applicability |
| `global` | Boolean (computed, stored) | — | True when `groups` is empty; set via `setattr` because `global` is a Python keyword |

**Constraint** (lines 32–35): At least one `perm_*` field must be True.

**`global` field special syntax** (lines 276–279):

```python
global_ = fields.Boolean(compute='_compute_global', store=True, ...)
setattr(IrRule, 'global', global_)
global_.__set_name__(IrRule, 'global')
```

Because `global` is a reserved Python keyword, the field is added via `setattr` after class definition.

---

## 2. `_eval_context()` — Domain Evaluation Variables

**Lines 37–51**

```python
@api.model
def _eval_context(self):
    return {
        'user': self.env.user.with_context({}),
        'company_ids': self.env.companies.ids,
        'company_id': self.env.company.id,
    }
```

- `user`: the browsed user record, but with **empty context** (`with_context({})`) to make domain evaluation context-independent and reproducible.
- `company_ids`: list of IDs of all **activated companies** in the multi-company switcher (`self.env.companies.ids`).
- `company_id`: ID of the **primary/current company** (`self.env.company.id`).

These three variables are the only ones available to domain expressions at runtime. No other context keys are injected here.

---

## 3. `_compute_global()` — Global Rule Detection

**Lines 53–56**

```python
@api.depends('groups')
def _compute_global(self):
    for rule in self:
        rule['global'] = not rule.groups
```

A rule is **global** (applies to all users) when it has **no groups assigned**. Global rules are AND-ed together across all ORM queries for the model.

---

## 4. `_check_domain()` — Domain Validation Constraint

**Lines 64–74**

```python
@api.constrains('active', 'domain_force', 'model_id')
def _check_domain(self):
    eval_context = self._eval_context()
    for rule in self:
        if rule.active and rule.domain_force:
            try:
                domain = safe_eval(rule.domain_force, eval_context)
                model = self.env[rule.model_id.model].sudo()
                Domain(domain).validate(model)
            except Exception as e:
                raise ValidationError(_('Invalid domain: %s', e))
```

On save, every active rule with a `domain_force` is validated via `safe_eval` + `Domain.validate`. Raises `ValidationError` on failure.

---

## 5. `_compute_domain_keys()` — Cache Key Declaration

**Lines 76–78**

```python
def _compute_domain_keys(self):
    return ['allowed_company_ids']
```

The only context key used for cache segmentation is `allowed_company_ids`. This allows the domain cache to vary per activated company set. Consumed by `_compute_domain_context_values()`.

---

## 6. `_get_rules()` — Rule Selection per User

**Lines 113–133**

```python
def _get_rules(self, model_name, mode='read'):
    if mode not in self._MODES:
        raise ValueError('Invalid mode: %r' % (mode,))

    if self.env.su:
        return self.browse(())     # <-- SUDO BYPASS: returns empty recordset

    sql = SQL("""
        SELECT r.id FROM ir_rule r
        JOIN ir_model m ON (r.model_id=m.id)
        WHERE m.model = %s AND r.active AND r.perm_%s
            AND (r.global OR r.id IN (
                SELECT rule_group_id FROM rule_group_rel rg
                WHERE rg.group_id IN %s
            ))
        ORDER BY r.id
    """, model_name, SQL(mode), tuple(self.env.user._get_group_ids()) or (None,))
    return self.browse(v for v, in self.env.execute_query(sql))
```

**Critical findings:**
- **`self.env.su` check at line 120–121**: when in sudo context, `_get_rules` immediately returns an empty recordset — no rules are applied. This is the complete sudo bypass for `ir.rule`.
- The SQL filters rules by: `active`, correct `perm_<mode>`, AND either `r.global = True` OR the rule belongs to a group the current user is in (via `rule_group_rel`).
- Uses `self.env.user._get_group_ids()` for the group membership check.

---

## 7. `_compute_domain()` — ORM Domain Assembly

**Lines 135–173**

```python
@api.model
@tools.conditional(
    'xml' not in config['dev_mode'],
    tools.ormcache('self.env.uid', 'self.env.su', 'model_name', 'mode',
                   'tuple(self._compute_domain_context_values())'),
)
def _compute_domain(self, model_name: str, mode: str = "read") -> Domain:
    model = self.env[model_name]

    # add rules for parent models (_inherits)
    global_domains: list[Domain] = []
    for parent_model_name, parent_field_name in model._inherits.items():
        if not model._fields[parent_field_name].store:
            continue
        if domain := self._compute_domain(parent_model_name, mode):
            global_domains.append(Domain(parent_field_name, 'any', domain))

    rules = self._get_rules(model_name, mode=mode)
    if not rules:
        return Domain.AND(global_domains).optimize(model)

    eval_context = self._eval_context()
    user_groups = self.env.user.all_group_ids
    group_domains: list[Domain] = []
    for rule in rules.sudo():
        if rule.groups and not (rule.groups & user_groups):
            continue
        dom = Domain(safe_eval(rule.domain_force, eval_context)) if rule.domain_force else Domain.TRUE
        if rule.groups:
            group_domains.append(dom)
        else:
            global_domains.append(dom)

    # combine: group_domains → OR; then AND with global_domains
    if group_domains:
        global_domains.append(Domain.OR(group_domains))
    return Domain.AND(global_domains).optimize(model)
```

**Rule combination logic:**
- **Global rules** (no groups): each domain appended to `global_domains` → combined with **AND**.
- **Group rules** (has groups, user in that group): each domain appended to `group_domains` → combined with **OR** internally → result AND-ed with global domains.
- **Inherits**: parent model rules are applied via `Domain(parent_field_name, 'any', parent_domain)` — each treated as a global domain for the child model.
- **Final**: `Domain.AND(global_domains).optimize(model)`.

**Caching:**
- Cache key: `(uid, su, model_name, mode, tuple(context_values))`.
- Disabled in `xml` dev mode to allow live reload.
- Context values from `_compute_domain_context_values()` which yields `allowed_company_ids` as a tuple.

---

## 8. `_compute_domain_context_values()` — Cache Context Values

**Lines 175–183**

```python
def _compute_domain_context_values(self):
    for k in self._compute_domain_keys():
        v = self.env.context.get(k)
        if isinstance(v, list):
            v = tuple(v)
        yield v
```

Converts list values (like `allowed_company_ids`) to tuples so they are hashable for the `ormcache` decorator.

---

## 9. `_get_failing()` — Failing Rules for Error Reporting

**Lines 80–111**

```python
def _get_failing(self, for_records, mode='read'):
    Model = for_records.browse(()).sudo().with_context(active_test=False)
    eval_context = self._eval_context()
    all_rules = self._get_rules(Model._name, mode=mode).sudo()

    # Group rules: OR-ed; if all records pass combined group domain → group_rules = empty
    group_rules = all_rules.filtered(lambda r: r.groups and r.groups & self.env.user.all_group_ids)
    group_domains = Domain.OR(
        safe_eval(r.domain_force, eval_context) if r.domain_force else []
        for r in group_rules
    )
    if Model.search_count(group_domains & Domain('id', 'in', for_records.ids)) == len(for_records):
        group_rules = self.browse(())

    # Global rules: AND-ed; each checked individually
    def is_failing(r, ids=for_records.ids):
        dom = Domain(safe_eval(r.domain_force, eval_context) if r.domain_force else [])
        return Model.search_count(dom & Domain('id', 'in', ids)) < len(ids)

    return all_rules.filtered(lambda r: r in group_rules or (not r.groups and is_failing(r))).with_user(self.env.user)
```

**Key behaviors:**
- Uses `active_test=False` to evaluate rules against inactive records too.
- Group rules fail as a unit (OR-ed): if the combined OR domain passes all records, no group rule is blamed.
- Global rules fail individually: each checked with `search_count`.
- Returns rules with `with_user(self.env.user)` so they display with user context.

---

## 10. `_make_access_error()` — Access Error Generation

**Lines 208–268**

Key behaviors:
- Logs `Access Denied` at INFO level with operation, record IDs (first 6), uid, model.
- Calls `_get_failing(records, mode=operation)` to collect failing rule names.
- **Debug mode only** (`base.group_no_one` AND internal user): shows failing rule names (`rule.name`) and record details.
- Multi-company detection: checks `'company_id' in (r.domain_force or '')` string-match on domain text.
- Uses `records._get_redirect_suggested_company()` for company switch suggestions.
- Returns `AccessError` with optional `.context` dict containing `suggested_company`.

---

## 11. Cache Invalidation on Mutations

**Lines 185–206**

```python
def unlink(self):
    res = super().unlink()
    self.env.registry.clear_cache()
    return res

def create(self, vals_list):
    res = super().create(vals_list)
    self.env.flush_all()
    self.env.registry.clear_cache()
    return res

def write(self, vals):
    res = super().write(vals)
    self.env.flush_all()
    self.env.registry.clear_cache()
    return res
```

All three mutating operations flush the ORM and clear the registry-level cache to ensure `_compute_domain` cache is invalidated.

---

## 12. `_check_model_name()` — Self-Reference Protection

**Lines 58–62**

```python
@api.constrains('model_id')
def _check_model_name(self):
    if any(rule.model_id.model == self._name for rule in self):
        raise ValidationError(_('Rules can not be applied on the Record Rules model.'))
```

No rule can target `ir.rule` itself. Prevents recursive access control loops.

---

## 13. sudo() Bypass — Definitive Analysis

`_allow_sudo_commands = False` (line 20) is a class attribute that prevents ORM commands on `ir.rule` records themselves from being called via sudo (protecting the rule records from being modified through sudo in some contexts).

However, the actual **enforcement bypass** is in `_get_rules()` (lines 120–121):

```python
if self.env.su:
    return self.browse(())
```

When `env.su` is True (any `sudo()` call on any model), `_get_rules` returns an empty recordset for all models, meaning **no domain rules are applied** to any query executed under sudo. This is unconditional and applies to all rule types (global and group-based).

---

## 14. Multi-Company Domain Pattern

The `_eval_context()` provides `company_ids` (list of activated company IDs) and `company_id` (current company ID). The standard multi-company rule domain pattern used in practice across Odoo modules is:

```python
['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]
```

This restricts records to those belonging to no company OR belonging to one of the user's activated companies. The `_make_access_error` method detects multi-company issues by string-searching `'company_id'` in `domain_force` text (line 233).

---

## 15. Migration Flags (v16/v17 → v19)

| Flag | Description |
|---|---|
| `Domain` class usage | v19 uses the `odoo.fields.Domain` object class (imported from `odoo.fields`) for all domain manipulation, replacing raw list-based domains. `Domain.AND`, `Domain.OR`, `Domain.TRUE`, `domain.optimize(model)` are v19 idioms. |
| `Domain.optimize()` | New in v19: final domain is optimized per-model before return, potentially simplifying or short-circuiting the domain. |
| `Domain('field', 'any', sub_domain)` | v19 inherits handling uses `'any'` operator in Domain for parent model rules — this is a newer domain operator. |
| `SQL()` object in `_get_rules` | Uses `odoo.tools.SQL` object for parameterized queries (line 8, 123), not raw string interpolation. |
| `_allow_sudo_commands = False` | Class attribute on `ir.rule` itself — may be v19-specific pattern for protecting rule meta-records. |
| `tools.conditional` on cache | Cache decorator is conditionally applied based on `'xml' not in config['dev_mode']` — same pattern as earlier versions but explicit conditional wrapping. |
| `env.registry.clear_cache()` | Used instead of older `self.pool.clear_caches()` — v17+ ORM style. |

---

## 16. Summary of Logic Flow

```
ORM query (read/write/create/unlink)
  └─► _compute_domain(model_name, mode)
        ├─ [cache hit] → return cached Domain
        └─ [cache miss]
             ├─ handle _inherits (parent model domains via 'any' operator)
             ├─ _get_rules(model_name, mode)
             │    ├─ self.env.su → return empty (SUDO BYPASS)
             │    └─ SQL: active + perm_<mode> + (global OR user_in_group)
             ├─ for each rule:
             │    ├─ global rule → append to global_domains (AND logic)
             │    └─ group rule → append to group_domains (OR logic)
             ├─ combine: AND(global_domains + OR(group_domains))
             └─ optimize(model) → return Domain
```
