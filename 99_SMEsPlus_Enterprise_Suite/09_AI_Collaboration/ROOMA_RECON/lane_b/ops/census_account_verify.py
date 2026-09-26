#!/usr/bin/env python3
"""
CENSUS ACCOUNT VERIFY   V1.00   (RED TEAM, Lane B) - BOSSDEC-003 after-state
Reads only. Creates nothing. Changes nothing.

Usage:  python3 ops/census_account_verify.py [credentials/roomb_census.env]

Proves, from the observer side (XML-RPC/JSON-RPC as the account itself):
  1. the account authenticates and which uid it is
  2. its effective groups contain NONE of the forbidden groups (BOSSDEC-003 B + C)
  3. what it sees in the UI (load_menus): menus, root sections, leaf screens - the honest census reach
  4. the frozen installed-set hash is unchanged (reference formula, rule R2)
  5. detective-audit baseline: records created/modified by this uid across key models (expected 0)
Writes:  reports/CENSUS_ACCOUNT_VERIFY_<ts>.json   (no credentials inside)
"""
import os, re, sys, ssl, json, hashlib, datetime, urllib.request, xmlrpc.client

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = sys.argv[1] if len(sys.argv) > 1 else os.path.join(W, "credentials/roomb_census.env")
EXPECTED_HASH = "706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89"
FORBID_LABELS = {"Role / Administrator", "Administration / Access Rights", "Access Rights",
                 "Administration / Settings", "Role / Technical"}
FORBID_PRIV = {"Website", "Live Chat", "eLearning", "Link Tracker", "Mail Group"}
AUDIT_MODELS = ["res.partner", "res.users", "res.company", "ir.attachment", "mail.message",
                "sale.order", "purchase.order", "account.move", "stock.picking", "product.template",
                "hr.employee", "project.task", "crm.lead", "ir.ui.menu", "ir.actions.act_window",
                "res.config.settings", "ir.model.access", "res.groups"]

def scrub(t):
    t = str(t)
    if re.search(r"(Traceback|site-packages|/opt/odoo|File \"/)", t):
        return "SOURCE_SCRUBBED"
    return t.strip().splitlines()[0][:160] if t.strip() else ""

env = {}
for line in open(CRED):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); env[k.strip()] = v.strip()
url, db, usr, pwd = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]
ctx = ssl.create_default_context()
uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx).authenticate(db, usr, pwd, {})
out = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(), "login": usr, "db": db, "uid": uid}
if not uid:
    print("VERIFY: FAIL - authentication failed"); sys.exit(2)
M = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
def R(model, method, args, kw=None):
    try:
        return True, M.execute_kw(db, uid, pwd, model, method, args, kw or {})
    except Exception as e:
        return False, scrub(getattr(e, "faultString", None) or str(e))
def J(model, method, args, kw=None):
    payload = {"jsonrpc": "2.0", "method": "call", "id": 1,
               "params": {"service": "object", "method": "execute_kw", "args": [db, uid, pwd, model, method, args, kw or {}]}}
    req = urllib.request.Request(url + "/jsonrpc", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, context=ctx, timeout=90))
    if "error" in r:
        return False, scrub((r["error"].get("data", {}) or {}).get("message") or r["error"].get("message") or "error")
    return True, r["result"]
print(f"account   {usr}  uid={uid}  {db}")

# 2. groups
ok, me = R("res.users", "read", [[uid]], {"fields": ["group_ids", "all_group_ids", "company_id", "company_ids"]})
fails = []
if ok:
    me = me[0]
    ok2, grp = R("res.groups", "search_read", [[["id", "in", me["all_group_ids"]]]], {"fields": ["id", "name", "privilege_id"]})
    labels = sorted((f"{g['privilege_id'][1]} / {g['name']}" if g["privilege_id"] else g["name"]) for g in grp) if ok2 else []
    bad = [l for l in labels if l in FORBID_LABELS or l.split(" / ")[0] in FORBID_PRIV or "Editor and Designer" in l or "Mail Group Administrator" in l]
    out.update({"direct_groups": len(me["group_ids"]), "all_groups": len(me["all_group_ids"]), "all_group_labels": labels,
                "company_id": me["company_id"], "company_ids": me["company_ids"], "forbidden_groups_present": bad})
    print(f"groups    direct={len(me['group_ids'])}  effective={len(me['all_group_ids'])}  company={me['company_id']}")
    print("forbidden " + ("NONE - PASS" if not bad else "PRESENT - FAIL: " + ", ".join(bad)))
    if bad: fails.append("forbidden groups present")
else:
    fails.append("cannot read own user: " + me); print("groups    cannot read own user:", me)

# 3. UI reach
ok, menus = J("ir.ui.menu", "load_menus", [False])
if ok and isinstance(menus, dict):
    ids = {int(k) for k in menus if str(k).lstrip("-").isdigit()}
    root = menus.get("root") or {}
    kids = root.get("children", []) if isinstance(root, dict) else []
    sections = [menus.get(str(i), menus.get(i, {})).get("name", "?") for i in kids]
    leaves = [k for k in ids if not menus[str(k)].get("children") and menus[str(k)].get("action_id")]
    out.update({"ui_visible_menus": len(ids), "ui_root_sections": sections, "ui_visible_leaf_with_action": len(leaves),
                "ui_visible_menu_ids": sorted(ids)})
    print(f"ui reach  menus={len(ids)}  sections={len(sections)}  leaf screens with action={len(leaves)}")
    print("sections  " + ", ".join(sections))
else:
    fails.append("load_menus failed"); print("ui reach  load_menus failed:", menus)

# 4. installed-set hash (reference formula, R2)
ok, mods = R("ir.module.module", "search_read", [[["state", "=", "installed"]]], {"fields": ["name"]})
if ok:
    names = sorted(m["name"] for m in mods)
    digest = hashlib.sha256(("\n".join(names) + "\n").encode()).hexdigest()
    out.update({"installed_modules": len(names), "installed_set_hash": digest, "baseline": "MATCH" if digest == EXPECTED_HASH else "MISMATCH"})
    print(f"baseline  {out['baseline']}  ({len(names)} modules)  {digest[:16]}…")
    if digest != EXPECTED_HASH: fails.append("baseline moved")
else:
    fails.append("cannot read module set"); print("baseline  cannot read module set:", mods)

# 5. detective-audit baseline: anything created or modified by this uid?
audit = {}
for m in AUDIT_MODELS:
    ok, n = R(m, "search_count", [["|", ["create_uid", "=", uid], ["write_uid", "=", uid]]], {"context": {"active_test": False}})
    audit[m] = n if ok else f"n/a ({n})"
touched = {m: n for m, n in audit.items() if isinstance(n, int) and n > 0}
out["write_audit"] = audit
print("write-audit " + ("0 records created/modified by this uid - PASS" if not touched else "TOUCHED: " + json.dumps(touched)))
# res.users itself: the account's own row is created by the shell (uid 1), so 0 is expected here too.
if touched: fails.append("write-audit non-zero")

out["result"] = "PASS" if not fails else "FAIL: " + "; ".join(fails)
os.makedirs(os.path.join(W, "reports"), exist_ok=True)
p = os.path.join(W, "reports", f"CENSUS_ACCOUNT_VERIFY_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
json.dump(out, open(p, "w"), indent=2, ensure_ascii=False)
print(f"\nVERIFY: {out['result']}")
print(f"written: {p}")
sys.exit(0 if not fails else 1)
