#!/usr/bin/env python3
"""
BOSSDEC 2026-09-26 : scoped access grant for the Lane B observer
Supersedes ops/grant_unlink_roomb_observer.py (which covered grant 1 only).

Grants, read-only except where stated, bound ONLY to the observer's own group:
   1  res.partner             unlink   - remove test records instead of accumulating them
   2  ir.actions.act_window   read     - know which screen each of the 681 menus opens
   3  res.config.settings     read     - enumerate the feature on/off switches

Runs ON THE STUDY SERVER. Change to a running system -> V2.0 §21.2 is followed:
backup, before-state, apply, after-state, rollback command.

NEVER modifies an existing shared access rule: a shared rule would hand the same
right to every user of the system. Each grant is a NEW rule on the Lane B group.
Record rules still confine the observer to its own company - proven on 2026-09-26
when a cross-company create was refused by the server.
"""
import json, os, sys, datetime, xmlrpc.client

URL, DB, LOGIN = "http://127.0.0.1:8069", "iTest19C", "admin"
PWD_FILE, BACKUP_DIR = "/root/ODOO_ADMIN_PASSWD.txt", "/root/ROOMA_BACKUP"
OBSERVER_LOGIN = "roomb_observer"

GRANTS = [
    ("res.partner",           {"perm_read": True, "perm_write": False, "perm_create": False, "perm_unlink": True}),
    ("ir.actions.act_window", {"perm_read": True, "perm_write": False, "perm_create": False, "perm_unlink": False}),
    ("res.config.settings",   {"perm_read": True, "perm_write": False, "perm_create": False, "perm_unlink": False}),
]

if not os.path.exists(PWD_FILE):
    sys.exit(f"ABORT: {PWD_FILE} not found")
pwd = open(PWD_FILE).read().strip()
uid = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common").authenticate(DB, LOGIN, pwd, {})
if not uid:
    sys.exit(f"ABORT: could not authenticate as '{LOGIN}'.\n"
             f"  {PWD_FILE} is evidently NOT the login password for '{LOGIN}'.\n"
             f"  NOTHING WAS CHANGED. Tell RED TEAM what that file binds to.")
M = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
def x(model, method, args, kw=None):
    return M.execute_kw(DB, uid, pwd, model, method, args, kw or {})
print(f"authenticated as {LOGIN} (uid {uid})\n")

obs = x("res.users", "search_read", [[["login", "=", OBSERVER_LOGIN]]],
        {"fields": ["id", "name", "groups_id"]})
if len(obs) != 1:
    sys.exit(f"ABORT: expected exactly 1 user '{OBSERVER_LOGIN}', found {len(obs)}")
obs = obs[0]
groups = x("res.groups", "read", [obs["groups_id"]], {"fields": ["id", "name", "full_name"]})
cand = [g for g in groups if any(k in (g.get("full_name") or g["name"]).upper()
                                 for k in ("ROOM B", "ROOMB", "LANE B", "LANEB", "OBSERVER"))]
if len(cand) != 1:
    print("Could not identify one dedicated Lane B group. Groups on this user:")
    for g in groups:
        print(f"   id={g['id']:4}  {g.get('full_name') or g['name']}")
    sys.exit("ABORT: NOTHING WAS CHANGED. Tell RED TEAM which group id is the Lane B group.")
grp = cand[0]
print(f"observer uid={obs['id']}   group id={grp['id']}  {grp.get('full_name') or grp['name']}\n")

# ---------- BEFORE ------------------------------------------------------
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(BACKUP_DIR, exist_ok=True)
before = {}
for model, _ in GRANTS:
    before[model] = x("ir.model.access", "search_read",
                      [[["model_id.model", "=", model], ["group_id", "in", obs["groups_id"]]]],
                      {"fields": ["id", "name", "group_id", "perm_read", "perm_write",
                                  "perm_create", "perm_unlink"]})
bpath = f"{BACKUP_DIR}/laneb_access_before_{stamp}.json"
json.dump(before, open(bpath, "w"), indent=2)
print(f"backup   {bpath}\n")

def probe(model):
    try:
        if model == "res.config.settings":
            x(model, "fields_get", [], {"attributes": ["string"]})
        else:
            x(model, "search_count", [[]])
        return "reachable"
    except Exception:
        return "refused"

# before-state measured AS THE OBSERVER, not as admin
opwd = None
cf = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "credentials/roomb_observer.env")
def as_observer(model):
    return "not measured (observer credentials not on this host)"
print("before (admin view of existing rules):")
for model, _ in GRANTS:
    rows = before[model]
    flags = ", ".join(f"id{r['id']}:r{int(r['perm_read'])}w{int(r['perm_write'])}"
                      f"c{int(r['perm_create'])}d{int(r['perm_unlink'])}" for r in rows) or "no rule on this group set"
    print(f"   {model:<24} {flags}")

# ---------- APPLY -------------------------------------------------------
created = []
print("\napply:")
for model, perms in GRANTS:
    existing = [r for r in before[model]
                if r["group_id"] and r["group_id"][0] == grp["id"]
                and all(r.get(k) for k, v in perms.items() if v)]
    if existing:
        print(f"   {model:<24} already granted (rule id {existing[0]['id']}) - skipped")
        continue
    mid = x("ir.model", "search", [[["model", "=", model]]])
    if not mid:
        print(f"   {model:<24} MODEL NOT FOUND - skipped")
        continue
    rid = x("ir.model.access", "create", [dict(
        name=f"roomb_observer_{model.replace('.', '_')}_"
             + "_".join(k.replace("perm_", "") for k, v in perms.items() if v),
        model_id=mid[0], group_id=grp["id"], **perms)])
    created.append((model, rid))
    got = ",".join(k.replace("perm_", "") for k, v in perms.items() if v)
    print(f"   {model:<24} CREATED rule id={rid}  ({got})")

# ---------- AFTER -------------------------------------------------------
print("\nafter (rule state):")
for model, _ in GRANTS:
    rows = x("ir.model.access", "search_read",
             [[["model_id.model", "=", model], ["group_id", "=", grp["id"]]]],
             {"fields": ["id", "perm_read", "perm_write", "perm_create", "perm_unlink"]})
    print(f"   {model:<24} " + (", ".join(
        f"id{r['id']}:r{int(r['perm_read'])}w{int(r['perm_write'])}"
        f"c{int(r['perm_create'])}d{int(r['perm_unlink'])}" for r in rows) or "none"))

ids = [r for _, r in created]
print(f"""
BEFORE-STATE BACKUP : {bpath}
CREATED RULE IDS    : {ids or 'none - everything was already in place'}

ROLLBACK (run on this server):
  python3 -c "import xmlrpc.client as x;p=open('{PWD_FILE}').read().strip();\\
u=x.ServerProxy('{URL}/xmlrpc/2/common').authenticate('{DB}','{LOGIN}',p,{{}});\\
x.ServerProxy('{URL}/xmlrpc/2/object').execute_kw('{DB}',u,p,'ir.model.access','unlink',[{ids}])"

NEXT (on the Mac, verifies the grant as the observer):
  python3 ~/ROOMB_WORKSPACE/ops/census_feasibility_probe.py
  python3 ~/ROOMB_WORKSPACE/collectors/stage1a_collector_V2.py     # must print: cleanup CLEAN

This is an execution result only. It is not Boss Final Approval of any gate.
""")
