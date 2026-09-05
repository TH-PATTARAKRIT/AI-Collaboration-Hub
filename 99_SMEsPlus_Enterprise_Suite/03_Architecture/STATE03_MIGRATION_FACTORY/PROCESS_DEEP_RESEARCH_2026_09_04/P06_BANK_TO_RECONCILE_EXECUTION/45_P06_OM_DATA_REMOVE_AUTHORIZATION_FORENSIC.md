# P06_OM_DATA_REMOVE_AUTHORIZATION_FORENSIC.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S04)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Question:** what, on the server, prevents an unauthorised caller from executing the destructive operation?

> **The prior round answered this correctly and reasoned it wrongly.** The conclusion survives; the argument is replaced. §3 records the correction in full.

---

## 1. The full dispatch chain, traced end to end

Every link read first-hand in `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo`.

**Link 1 — the HTTP route is open to any authenticated user.**
`addons/web/controllers/dataset.py:32-36`:
```
@http.route(['/web/dataset/call_kw', '/web/dataset/call_kw/<path:path>'], type='json', auth="user", readonly=_call_kw_readonly)
def call_kw(self, model, method, args, kwargs, path=None):
    Model = request.env[model]
    get_public_method(Model, method)
    return call_kw(request.env[model], method, args, kwargs)
```
`auth="user"` — **any logged-in user**, no group requirement. `call_button` at `:38-40` is identical.
The XML-RPC path reaches the same guard: `service/model.py` `execute_cr` → `get_public_method(recs, method)` → `call_kw`.

**Link 2 — the only dispatch guard blocks private methods, nothing else.**
`service/model.py:28-46`:
```
def get_public_method(model, name):
    """ ... Accessible methods are public (in sense that python defined it:
    not prefixed with "_") and are not decorated with `@api.private`. """
    ...
        if name.startswith('_') or getattr(cla_method, '_api_private', False):
            raise AccessError(f"Private methods (such as '{model._name}.{name}') cannot be called remotely.")
    return method
```
`remove_all`, `remove_account`, `remove_account_chart`, `remove_message` are **public** and carry **no `@api.private` decorator**. They pass.

**Link 3 — `call_kw` performs no access check at all.**
`api.py:512-540`:
```
def call_kw(model, name, args, kwargs):
    method = getattr(model, name, None)
    ...
    api = getattr(method, '_api', None)
    if api:
        recs = model
    else:
        ids, args = args[0], args[1:]
        recs = model.browse(ids)
    ...
    result = getattr(recs, name)(*args, **kwargs)
```
**PATTERN `check_access` over `api.py:512-540`: 0 hits.** `browse()` does not check access — it constructs a recordset. With `args[0] = []` the result is an **empty recordset**, and the method is then invoked on it.

**Link 4 — the method body never performs an ORM operation on its own model.**
`remove_all` → `remove_account` → `remove_data` → `self._cr.execute(sql)`. **`self` is never read, written, searched or iterated.** It is only a handle for `self._cr` and `self.env`.

**AUTH-F-01 — Therefore no access-control check occurs on any link of the chain. FACT VERIFIED.**

---

## 2. The ACL that exists, and why it is not on this path

**AUTH-F-02 — `res.config.settings` IS restricted, and to the strictest group available.**
`addons/base/security/ir.model.access.csv:129`:
```
"access_res_config_settings","access.res.config.settings","model_res_config_settings","base.group_system",1,1,1,0
```
**DENOMINATOR:** POPULATION: all `security/ir.model.access.csv` files under `$V18E`. PATTERN: `model_res_config_settings`. UNIT: granting row. **RESULT: 1 — the base row above, `base.group_system` only, and `unlink` is 0.**

**AUTH-F-03 — And it is irrelevant here, because `ir.model.access` is enforced by ORM operations and this path performs none.**
The ACL fires on `search`, `read`, `write`, `create`, `unlink`. `remove_data` executes raw SQL. `browse()` in `call_kw` triggers nothing. **The strictest possible model ACL sits directly on the model and is bypassed not by defeating it but by never invoking it.**

---

## 3. CORRECTION TO THE PRIOR ROUND

`20_` Appendix A, CMD-F-18, argued:
> *"The methods are plain `type="object"` handlers on `res.config.settings`, a `TransientModel` with a broad default ACL."*

**That premise is FALSE.** The default ACL is `base.group_system` only — the narrowest grant in the system, and it does not even grant `unlink`. The prior round asserted a broad ACL without reading `ir.model.access.csv`.

**The conclusion is unchanged and the reasoning is now stronger.** The correct statement:

> **The destructive path is unauthorised not because the model is permissive, but because the path never touches the ORM layer where the model's permissions are enforced.**

This matters for the target design. Under the wrong reasoning, the remedy would be "tighten the ACL on the settings model" — which would achieve **nothing**. Under the correct reasoning, the remedy is that **a destructive financial operation must perform its own explicit server-side authorisation check**, because the framework's declarative layer cannot protect a method that bypasses the framework.

**Recorded as author error REV-E-09.**

---

## 4. Each candidate control, tested

| Control | Present? | Does it stop the RPC? |
|---|---|---|
| Menu `groups="base.group_system"` | yes, `views/view.xml:113-119` | **NO** — governs menu rendering only |
| `confirm=` on every button | yes | **NO** — a client-side dialog |
| `groups` on the `ir.actions.act_window` | **NOT FOUND** (`:104-111`) | n/a |
| `ir.model.access` on `res.config.settings` | yes, `base.group_system` | **NO** — never invoked on this path (AUTH-F-03) |
| Module-supplied `security/` directory or ACL file | **NOT FOUND in all 4 copies** — `find <root>/om_data_remove -iname "*.csv" -o -iname "security*"` → nothing in any copy | n/a |
| Record rules on `res.config.settings` | **NOT FOUND** in the module; base rules govern the model, not raw SQL | **NO** |
| `has_group` / `_is_admin` / `check_access` inside the module | **NOT FOUND** — PATTERN `has_group\|_is_admin\|check_access\|AccessError` over `$CUST18/om_data_remove/models/model.py`, 368 lines read in full → 0 hits | n/a |
| `@api.private` on the destructive methods | **NOT FOUND** | **NO** |
| `sudo()` needed to escalate | **not needed** — the SQL runs on the caller's cursor regardless of `uid` | n/a |
| Postgres role separation | **NOT ASSESSED** — see §6 | unknown |

---

## 5. Scope filtering on the destructive path

| Element | Company filter | Tenant filter | Ownership check |
|---|---|---|---|
| `delete from <table>` | **none** | **none** | **none** |
| Sequence reset, `remove_account` | **yes** — `('company_id','=',self.env.company.id)` | none | none |
| Sequence reset, generic `remove_data` | **none**, and `.sudo()`-ed | none | none |
| `ir_default` / `account_journal` SQL in `remove_account_chart` | **yes** — `company_id=%d` | none | none |
| MIGR18 WHT-cert cleanup | **yes** | none | none |

**AUTH-F-04 — The destructive primitive is the one element with no scoping, in a module whose author applied scoping everywhere else.** See `44_` OMD-F-09.

---

## 6. What this forensic does NOT establish

Stated before the classification, because the classification depends on it.

1. **No execution was performed.** This is a source call-graph analysis. Per the directive's §10 vocabulary the reachability class is **SOURCE-REACHABLE / RUNTIME UNVERIFIED**, and that is recorded in `46_`.
2. **Whether the module is installed on any target is unknown** (`P06-OQ-98`). An uninstalled module's methods are not on the registry and cannot be dispatched.
3. **Database-role separation was not assessed.** If the Odoo database user lacked `DELETE` on those tables, Postgres would refuse — and the exception would be **swallowed to a warning** in the v18 copies. Whether such separation exists is **HOLD — DEPLOYMENT EVIDENCE REQUIRED**. It is uncommon in Odoo deployments, which is why this is a real mitigation to check rather than to assume.
4. **Whether a base record rule on `res.config.settings` would block `browse([])`** — it would not; record rules apply to `search`/`read`, and no read occurs.

---

## 7. Classification

**SERVER-SIDE AUTHORIZATION: `NO SERVER-SIDE AUTHORIZATION VERIFIED`.**

Precisely: across the full dispatch chain — HTTP route (`auth="user"`), `get_public_method` (blocks only private/`@api.private`), `call_kw` (no access check), and the method body (no ORM operation on its own model, no `has_group`, no explicit check) — **no authorisation control was found that would prevent an authenticated non-administrator from invoking the destructive methods over RPC.**

The only controls present are **UI-ONLY**: a menu `groups=` attribute and a client-side `confirm=` string.

**This classification is bounded by §6.** It is a source-level conclusion about the code path. It is **not** a claim that any deployed system is exposed — that requires the module to be installed, and requires database-role separation to be absent.

---

## 8. Requirement for the target

| ID | Requirement |
|---|---|
| `AUTH-R-01` | A destructive financial operation must perform an **explicit server-side authorisation check inside the method**, and must not rely on declarative ACLs, record rules, menu groups or client confirmations. |
| `AUTH-R-02` | Any operation that bypasses the data-access layer must be treated as **outside the security model** and must therefore carry its own. |
| `AUTH-R-03` | Bulk deletion of financial records must not exist as a callable operation at all. Where data must be cleared, it must be scoped, logged, authorised, reversible, and must refuse inside a closed period. |
| `AUTH-R-04` | UI visibility must never be recorded as an authorisation control in any design document. |
