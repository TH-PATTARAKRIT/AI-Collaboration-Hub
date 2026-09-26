#!/usr/bin/env python3
"""
LANE B CENSUS - FEASIBILITY PROBE
Answers one question before any charter is written:

    can the Lane B observer account actually enumerate the result surface
    (menus, screens, actions, feature switches, states) on this server?

Reads only. Creates nothing. Changes nothing.
Run BEFORE committing to the census model - control tested before it is specified.
"""
import os, ssl, json, sys, datetime, xmlrpc.client

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(W, "credentials/roomb_observer.env")
env = {}
for line in open(CRED):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); env[k.strip()] = v.strip()
url, db, usr, pwd = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]
ctx = ssl.create_default_context()
uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx).authenticate(db, usr, pwd, {})
m = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
print(f"observer uid={uid}  {db}\n")

SURFACES = [
    ("menus shown to the user",      "ir.ui.menu",              ["name", "parent_id", "action", "sequence"]),
    ("screens / windows",            "ir.actions.act_window",   ["name", "res_model", "view_mode"]),
    ("server actions",               "ir.actions.server",       ["name", "model_id"]),
    ("report outputs",               "ir.actions.report",       ["name", "model", "report_type"]),
    ("view layouts",                 "ir.ui.view",              ["name", "model", "type"]),
    ("feature switches (settings)",  "res.config.settings",     []),
    ("field-level selections",       "ir.model.fields",         ["name", "model", "ttype"]),
    ("record-level states",          "ir.model.fields.selection", ["name", "value"]),
    ("groups the user may see",      "res.groups",              ["name"]),
    ("modules as the user sees them","ir.module.module",        ["name", "shortdesc", "state"]),
]

ok = fail = 0
rows = []
for label, model, fields in SURFACES:
    try:
        n = m.execute_kw(db, uid, pwd, model, "search_count", [[]])
        sample = None
        if fields:
            s = m.execute_kw(db, uid, pwd, model, "search_read", [[]], {"fields": fields, "limit": 1})
            sample = "yes" if s else "empty"
        else:
            m.execute_kw(db, uid, pwd, model, "fields_get", [], {"attributes": ["string"]})
            sample = "metadata only"
        rows.append((label, model, "REACHABLE", n, sample)); ok += 1
    except Exception as e:
        msg = (getattr(e, "faultString", None) or str(e)).strip().splitlines()[0][:70]
        rows.append((label, model, "REFUSED", None, msg)); fail += 1

w = max(len(r[0]) for r in rows)
for label, model, st, n, note in rows:
    cnt = f"{n:>7}" if n is not None else "      -"
    print(f"  {label:<{w}}  {st:<9} {cnt}   {note}")

print(f"\nreachable {ok} / {len(SURFACES)}   refused {fail}")
print("\nVERDICT: " + ("CENSUS FEASIBLE with this account"
                       if fail == 0 else
                       f"CENSUS PARTIAL - {fail} surface(s) need a scoped read grant"))
out = os.path.join(W, "ops", "census_feasibility_result.json")
json.dump({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "uid": uid, "reachable": ok, "refused": fail,
           "rows": [{"surface": a, "model": b, "status": c, "count": d, "note": e} for a, b, c, d, e in rows]},
          open(out, "w"), indent=2, ensure_ascii=False)
print(f"written: {out}")
