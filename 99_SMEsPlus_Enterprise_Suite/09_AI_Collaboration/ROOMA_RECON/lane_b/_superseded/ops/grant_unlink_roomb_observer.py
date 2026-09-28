#!/usr/bin/env python3
"""
BOSSDEC — Option A : grant scoped delete to the Lane B observer
Runs ON THE STUDY SERVER. Change to a running system -> follows V2.0 §21.2.

Safety design:
  * NEVER modifies an existing shared access rule (that would grant delete to
    every user of the system). Creates a NEW rule bound only to the observer's
    own dedicated group.
  * Aborts if the dedicated group cannot be identified unambiguously.
  * Record rules already restrict the observer to its own company - proven:
    a cross-company create was refused by the server.
  * Prints the exact rollback command before finishing.
"""
import json, os, sys, datetime, xmlrpc.client

URL = "http://127.0.0.1:8069"
DB  = "iTest19C"
LOGIN = "admin"
PWD_FILE = "/root/ODOO_ADMIN_PASSWD.txt"
BACKUP_DIR = "/root/ROOMA_BACKUP"
OBSERVER_LOGIN = "roomb_observer"
MODEL = "res.partner"

if not os.path.exists(PWD_FILE):
    sys.exit(f"ABORT: {PWD_FILE} not found")
pwd = open(PWD_FILE).read().strip()

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid = common.authenticate(DB, LOGIN, pwd, {})
if not uid:
    sys.exit(f"ABORT: could not authenticate as '{LOGIN}'.\n"
             f"  {PWD_FILE} is evidently NOT the login password for user '{LOGIN}'.\n"
             f"  Nothing was changed. Tell RED TEAM what that file binds to.")
m = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, pwd, model, method, args, kw or {})

print(f"authenticated as {LOGIN} (uid {uid})")

obs = x("res.users", "search_read", [[["login", "=", OBSERVER_LOGIN]]],
        {"fields": ["id", "name", "groups_id", "company_id"]})
if len(obs) != 1:
    sys.exit(f"ABORT: expected exactly 1 user '{OBSERVER_LOGIN}', found {len(obs)}")
obs = obs[0]
print(f"observer   uid={obs['id']}  company={obs['company_id']}")

groups = x("res.groups", "read", [obs["groups_id"]], {"fields": ["id", "name", "full_name"]})
cand = [g for g in groups if any(k in (g.get("full_name") or g["name"]).upper()
                                 for k in ("ROOM B", "ROOMB", "LANE B", "LANEB", "OBSERVER"))]
if len(cand) != 1:
    print("\nCould not identify one dedicated group. Groups on this user:")
    for g in groups:
        print(f"  id={g['id']:4}  {g.get('full_name') or g['name']}")
    sys.exit("ABORT: nothing changed. Tell RED TEAM which group id is the Lane B group.")
grp = cand[0]
print(f"group      id={grp['id']}  {grp.get('full_name') or grp['name']}")

# ---- BEFORE state -----------------------------------------------------
before = x("ir.model.access", "search_read",
           [[["model_id.model", "=", MODEL], ["group_id", "in", obs["groups_id"]]]],
           {"fields": ["id", "name", "group_id", "perm_read", "perm_write",
                       "perm_create", "perm_unlink"]})
os.makedirs(BACKUP_DIR, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
bpath = f"{BACKUP_DIR}/ir_model_access_{MODEL.replace('.','_')}_before_{stamp}.json"
open(bpath, "w").write(json.dumps(before, indent=2))
print(f"backup     {bpath}")
for r in before:
    print(f"  before   id={r['id']:5} r{int(r['perm_read'])} w{int(r['perm_write'])} "
          f"c{int(r['perm_create'])} d{int(r['perm_unlink'])}  {r['name']}")

existing = [r for r in before if r["group_id"] and r["group_id"][0] == grp["id"] and r["perm_unlink"]]
if existing:
    print(f"\nALREADY GRANTED (rule id {existing[0]['id']}) - nothing to do")
    sys.exit(0)

# ---- APPLY : new rule only, never touch a shared one -------------------
model_id = x("ir.model", "search", [[["model", "=", MODEL]]])[0]
new_id = x("ir.model.access", "create", [{
    "name": f"roomb_observer_{MODEL.replace('.','_')}_unlink",
    "model_id": model_id,
    "group_id": grp["id"],
    "perm_read": True, "perm_write": False,
    "perm_create": False, "perm_unlink": True,
}])
print(f"\nCREATED    ir.model.access id={new_id}  (unlink only, group {grp['id']})")

after = x("ir.model.access", "read", [[new_id]],
          {"fields": ["id", "name", "perm_read", "perm_write", "perm_create", "perm_unlink"]})
print(f"after      {after}")

print(f"""
ROLLBACK (run on this server):
  python3 -c "import xmlrpc.client as x;p=open('{PWD_FILE}').read().strip();\\
u=x.ServerProxy('{URL}/xmlrpc/2/common').authenticate('{DB}','{LOGIN}',p,{{}});\\
x.ServerProxy('{URL}/xmlrpc/2/object').execute_kw('{DB}',u,p,'ir.model.access','unlink',[[{new_id}]])"

BEFORE-STATE BACKUP: {bpath}
""")
