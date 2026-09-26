#!/usr/bin/env python3
"""
RT-SEC-003 - MENU-TREE IMPACT ESTIMATE PER RIGHTS PROFILE   V1.00   (RED TEAM, Lane B)
SMEsPlus Enterprise Suite / ROOM A

Question for Boss: if the observer's 7 shared group memberships are cut, how much of the
census denominator (681 menus / 492 leaf screens) disappears?

Reads only. Changes nothing. Does NOT touch the observer's groups.
Method: menu visibility = (menu has no group restriction OR menu.groups ∩ user's effective
groups ≠ ∅) AND parent visible. Effective groups = direct groups + implied closure, read from
res.groups. Field names are discovered with fields_get, never assumed.

LIMIT (stated, not hidden): Odoo also hides a menu whose action model the user cannot read.
That second filter needs ir.model.access, which the observer cannot read, so every number
below is an UPPER BOUND of what a reduced profile would still see. Exact numbers need a test
account per profile (OPTION D in the decision package).
"""
import os, ssl, json, sys, datetime, xmlrpc.client

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(W, "reports", "RT-SEC-003_menu_impact_estimate.json")
env = {}
for line in open(os.path.join(W, "credentials/roomb_observer.env")):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); env[k.strip()] = v.strip()
url, db, usr, pwd = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]
ctx = ssl.create_default_context()
uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx).authenticate(db, usr, pwd, {})
M = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
def rpc(model, method, args, kw=None):
    return M.execute_kw(db, uid, pwd, model, method, args, kw or {})

def pick(model, candidates):
    f = rpc(model, "fields_get", [], {"attributes": ["type"]})
    for c in candidates:
        if c in f:
            return c
    sys.exit(f"ABORT: none of {candidates} on {model} - fields seen: {[k for k in f if 'group' in k or 'impl' in k]}")

MENU_G = pick("ir.ui.menu", ["group_ids", "groups_id"])
USER_G = pick("res.users", ["group_ids", "groups_id"])
GRP_IMPL = pick("res.groups", ["all_implied_ids", "implied_ids"])
print(f"observer uid={uid}  {db}")
print(f"fields: ir.ui.menu.{MENU_G}  res.users.{USER_G}  res.groups.{GRP_IMPL}")

me = rpc("res.users", "read", [[uid]], {"fields": [USER_G]})[0]
direct = sorted(me[USER_G])
groups = {g["id"]: g for g in rpc("res.groups", "search_read", [[]], {"fields": ["id", "name", GRP_IMPL]})}
name = lambda gid: groups.get(gid, {}).get("name", f"<group {gid} not readable>")
print(f"direct groups ({len(direct)}): " + ", ".join(f"{g}={name(g)}" for g in direct))

def closure(gids):
    seen, todo = set(), list(gids)
    while todo:
        g = todo.pop()
        if g in seen: continue
        seen.add(g)
        todo += groups.get(g, {}).get(GRP_IMPL, [])
    return seen

menus = rpc("ir.ui.menu", "search_read", [[]],
            {"fields": ["id", "name", "parent_id", "action", MENU_G],
             "context": {"ir.ui.menu.full_list": True}})
by_id = {m["id"]: m for m in menus}
kids = {}
for m in menus:
    if m["parent_id"]:
        kids.setdefault(m["parent_id"][0], []).append(m["id"])

def top_of(m):
    seen = set()
    while m.get("parent_id") and m["id"] not in seen:
        seen.add(m["id"]); m = by_id.get(m["parent_id"][0], m)
        if m["id"] in seen: break
    return m["name"]

def visible_set(effective):
    vis = {}
    def v(mid):
        if mid in vis: return vis[mid]
        m = by_id[mid]
        own = (not m[MENU_G]) or bool(set(m[MENU_G]) & effective)
        par = True if not m["parent_id"] else (m["parent_id"][0] in by_id and v(m["parent_id"][0]))
        vis[mid] = own and par
        return vis[mid]
    return {mid for mid in by_id if v(mid)}

def measure(label, direct_ids):
    eff = closure(direct_ids)
    vis = visible_set(eff)
    leaves = [mid for mid in vis if not kids.get(mid) and by_id[mid]["action"]]
    tops = sorted({top_of(by_id[mid]) for mid in vis})
    return {"profile": label, "direct_groups": sorted(direct_ids),
            "direct_names": [name(g) for g in sorted(direct_ids)],
            "effective_groups": len(eff), "menus_visible_est": len(vis),
            "leaf_screens_est": len(leaves), "top_level_sections": tops}

NAMED = {name(g).lower(): g for g in direct}
def gid(substr):
    return next((g for n, g in NAMED.items() if substr.lower() in n), None)
G_USER, G_OBS = gid("role / user"), gid("room b observer")
G_HR, G_FULLACC = gid("manage all employees"), gid("full accounting")

scenarios = [
    ("A  current 8 groups (as-is)",               set(direct)),
    ("B  minimal: Role/User + Lane B group only", {g for g in (G_USER, G_OBS) if g}),
    ("C  business user: drop HR-Officer + Full-Accounting", set(direct) - {g for g in (G_HR, G_FULLACC) if g}),
    ("D  drop Full-Accounting only",              set(direct) - ({G_FULLACC} if G_FULLACC else set())),
]
results = [measure(l, s) for l, s in scenarios]
base = results[0]
print()
print(f"{'profile':<56} {'groups':>6} {'eff':>4} {'menus':>6} {'leaves':>7}   sections")
for r in results:
    print(f"{r['profile']:<56} {len(r['direct_groups']):>6} {r['effective_groups']:>4} "
          f"{r['menus_visible_est']:>6} {r['leaf_screens_est']:>7}   {len(r['top_level_sections'])}")
print()
for r in results[1:]:
    lost = sorted(set(base["top_level_sections"]) - set(r["top_level_sections"]))
    print(f"{r['profile'][:2]} loses sections: {', '.join(lost) if lost else '(none)'}")
print()
print("NOTE: estimates are UPPER BOUNDS - action-model access filtering is not modelled (needs ir.model.access).")
json.dump({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(), "observer_uid": uid, "db": db,
           "fields": {"menu_groups": MENU_G, "user_groups": USER_G, "group_implied": GRP_IMPL},
           "actual_now": {"menus": len(menus)},
           "method_limit": "upper bound; action-model access not modelled",
           "scenarios": results},
          open(OUT, "w"), indent=2, ensure_ascii=False)
print(f"written: {OUT}")
