# U222 — ir.model.access: Access Control List Model, Group-Based Access, Security Enforcement

**Research Unit**: U222  
**Module**: `ir_model_access` (class `IrModelAccess`)  
**Primary Source**: `odoo/addons/base/models/ir_model.py` (lines 2080–2223)  
**Secondary Source**: `odoo/orm/models.py` (lines 4106–4199)  
**Supporting Source**: `odoo/addons/base/models/ir_rule.py` (lines 15–280)  
**SHA (ir_model.py)**: `1f5bdf77a7e1953e4a6e7470add7dab96dab3514`  
**Odoo Version**: 19.0.post20260921 (Community)

---

## 1. Class Definition and Fields

**Source**: `ir_model.py:2080–2093`

```python
class IrModelAccess(models.Model):
    _name = 'ir.model.access'
    _description = 'Model Access'
    _order = 'model_id,group_id,name,id'
    _allow_sudo_commands = False

    name = fields.Char(required=True, index=True)
    active = fields.Boolean(default=True, ...)
    model_id = fields.Many2one('ir.model', ..., required=True, index=True, ondelete='cascade')
    group_id = fields.Many2one('res.groups', ..., ondelete='restrict', index=True)
    perm_read = fields.Boolean(string='Read Access')
    perm_write = fields.Boolean(string='Write Access')
    perm_create = fields.Boolean(string='Create Access')
    perm_unlink = fields.Boolean(string='Delete Access')
```

Key properties:
- `_allow_sudo_commands = False` (line 2084): The `IrModelAccess` model itself rejects sudo-elevated commands, preventing privilege escalation on the ACL table.
- `group_id` is optional (no `required=True`): A NULL `group_id` denotes a **global ACL** (applies to all users). In v19, creating a global ACL record emits a deprecation warning.

---

## 2. `group_names_with_access(model_name, access_mode)` — Line 2096

Returns the human-readable names of groups with a given permission on a model. Uses a raw SQL query joining `ir_model_access` → `ir_model` → `res_groups` → `res_groups_privilege` (left join for privilege/category).

```sql
SELECT COALESCE(c.name->>%s, c.name->>'en_US'), COALESCE(g.name->>%s, g.name->>'en_US')
  FROM ir_model_access a
  JOIN ir_model m ON (a.model_id = m.id)
  JOIN res_groups g ON (a.group_id = g.id)
 LEFT JOIN res_groups_privilege c ON (c.id = g.privilege_id)
 WHERE m.model = %s AND a.active = TRUE AND a.perm_{access_mode} = TRUE
 ORDER BY c.name, g.name NULLS LAST
```

Note: `res_groups_privilege` is a v19 addition representing privilege categories. The output format is `Privilege/Group` or just `Group` if no privilege.

---

## 3. `_get_access_groups(model_name, access_mode='read')` — Lines 2117–2134

Decorated with `@tools.ormcache('model_name', 'access_mode', cache='stable')`.

Returns a `SetDefinitions` group expression object:
- **No ACL records exist** for this model/mode → returns `group_definitions.empty` (nobody has access)
- **At least one ACL has no `group_id`** (global ACL) → returns `group_definitions.universe` (all users have access)
- **All ACLs have a group** → returns `group_definitions.from_ids(accesses.group_id.ids)`

This method uses `self.sudo().search(...)` to retrieve ACL records regardless of the caller's own permissions.

```python
if not accesses:
    return group_definitions.empty
if not all(access.group_id for access in accesses):  # there is some global access
    return group_definitions.universe
return group_definitions.from_ids(accesses.group_id.ids)
```

---

## 4. `_get_allowed_models(mode='read')` — Lines 2141–2160

Decorated with `@tools.ormcache('self.env.uid', 'mode')`.

Performs a SQL query to return the frozenset of model names accessible to the current user (`self.env.uid`) for the given mode:

```sql
SELECT m.model
  FROM ir_model_access a
  JOIN ir_model m ON (m.id = a.model_id)
 WHERE a.perm_{mode}
   AND a.active
   AND (a.group_id IS NULL OR a.group_id IN {user_group_ids})
 GROUP BY m.model
```

The `GROUP BY m.model` means: a model is accessible if **at least one** ACL record grants it — OR logic across all matching ACL entries. User group IDs come from `self.env.user._get_group_ids()` (itself cached per user id, line 1098–1104 of res_users.py).

---

## 5. `check(model, mode='read', raise_exception=True)` — Lines 2162–2176

**Primary ACL enforcement entry point** called from `orm/models.py:_check_access()`.

```python
@api.model
def check(self, model, mode='read', raise_exception=True):
    if self.env.su:
        # User root have all accesses
        return True

    assert isinstance(model, str), ...
    if model not in self.env:
        _logger.error('Missing model %s', model)

    has_access = model in self._get_allowed_models(mode)
    if not has_access and raise_exception:
        raise self._make_access_error(model, mode) from None
    return has_access
```

**Superuser bypass** (line 2164): If `self.env.su` is True (sudo environment), the check is unconditionally bypassed and `True` is returned. This is different from `ir.rule` bypass behaviour — both use `env.su`.

**Algorithm**:
1. Superuser → skip (return True)
2. Delegate to `_get_allowed_models(mode)` (cached per uid+mode)
3. Model in result → access granted
4. Model not in result → raise `AccessError` (if `raise_exception=True`)

---

## 6. `_make_access_error(model, mode)` — Lines 2178–2195

Creates a formatted `AccessError` with:
1. Header identifying the model name and operation
2. List of groups that would grant access (via `group_names_with_access`)
3. If no groups → "No group currently allows this operation"
4. Resolution info: "Contact your administrator"

Error is logged at INFO level with uid, model, operation.

---

## 7. `call_cache_clearing_methods()` — Lines 2198–2200

```python
def call_cache_clearing_methods(self):
    self.env.invalidate_all()
    self.env.registry.clear_cache('stable')  # mainly _get_allowed_models
```

Called in `create`, `write`, `unlink`. Clears:
- Per-request environment cache (`invalidate_all`)
- Registry-level `'stable'` cache (which contains `_get_allowed_models`, `_get_access_groups`, and others)

---

## 8. Global ACL Deprecation Warning — Lines 2208–2214

In v19, creating an `ir.model.access` record with no `group_id` (global access) triggers a deprecation warning:

```python
if "group_id" in ima and not ima["group_id"] and any([...]):
    _logger.warning("Rule %s has no group, this is a deprecated feature. ...")
```

This indicates a **v19 migration flag**: global ACL records (no group) are officially deprecated. All access-granting ACL records should specify a group.

---

## 9. `check_access()` / `_check_access()` in orm/models.py — Lines 4106–4164

**v19 unified access check** replaces the older `check_access_rights()` + `check_access_rule()` pattern.

```python
def check_access(self, operation: str) -> None:
    if not self.env.su and (result := self._check_access(operation)):
        raise result[1]()

def _check_access(self, operation: str) -> tuple[Self, Callable] | None:
    Access = self.env['ir.model.access']
    if not Access.check(self._name, operation, raise_exception=False):
        return self, functools.partial(Access._make_access_error, self._name, operation)

    # record-level check (ir.rule) only for real records
    if any(self._ids):
        Rule = self.env['ir.rule']
        domain = Rule._compute_domain(self._name, operation)
        if domain and (forbidden := self - self.sudo().with_context(active_test=False).filtered_domain(domain)):
            return forbidden, functools.partial(Rule._make_access_error, operation, forbidden)

    return None
```

**Two-stage check**:
1. **Model-level (ACL)**: `IrModelAccess.check()` — does the user have permission on this model at all?
2. **Record-level (rules)**: `IrRule._compute_domain()` — does the user have permission on these specific records?

ACL must pass first. If ACL fails, rule check is never reached.

---

## 10. Deprecated Methods — Lines 4167–4198

All deprecated since **Odoo 18.0**:

| Old Method | Replacement | Note |
|---|---|---|
| `check_access_rights(operation, raise_exception=True)` | `check_access(operation)` or `has_access(operation)` | line 4167 |
| `check_access_rule(operation)` | `check_access(operation)` | line 4181 |
| `_filter_access_rules(operation)` | `_filtered_access(operation)` | line 4191 |
| `_filter_access_rules_python(operation)` | `_filtered_access(operation)` | line 4196 |

---

## 11. ir.rule: Superuser Bypass and Domain Combination — ir_rule.py:113–173

`_get_rules(model_name, mode)` at line 113:
```python
if self.env.su:
    return self.browse(())  # empty — superuser bypasses all rules
```

`_compute_domain()` at lines 141–173:
- Global rules (no `groups`): AND-ed together
- Group rules (user in group): OR-ed together within the group set; result AND-ed with global domains
- Returns `Domain.AND(global_domains).optimize(model)`

---

## 12. ACL vs Rule Distinction

| Property | ir.model.access (ACL) | ir.rule (Record Rule) |
|---|---|---|
| Scope | Model-level (all records) | Record-level (specific records via domain) |
| Logic | OR (any ACL grants access) | AND global + OR group rules |
| Superuser bypass | `env.su` check in `check()` | `env.su` returns empty ruleset |
| Caching | `ormcache` per uid+mode | `ormcache` per uid+su+mode+context |
| Default when no rule | Access depends on ACL | All records accessible (no restriction) |

---

## 13. Migration Flags Summary

1. **`check_access_rights()` deprecated since 18.0** — still present in v19 but emits deprecation; use `check_access()`.
2. **`check_access_rule()` deprecated since 18.0** — delegates to `check_access()`.
3. **Global ACL (no group_id) is deprecated in v19** — `create()` emits `_logger.warning`. Any existing global ACLs should be migrated to group-specific ACLs.
4. **`res_groups_privilege`** join in `group_names_with_access` — new table in v19 representing group categories/privileges (not present in older versions).
5. **`_allow_sudo_commands = False`** on `IrModelAccess` — prevents commands run under sudo from operating on the ACL table, a security hardening feature.
6. **`cache='stable'` for `_get_access_groups`** — stable cache is cleared only on ACL create/write/unlink, not on every request; older versions may have used default cache.
