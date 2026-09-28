#!/usr/bin/env python3
"""
LANE B CENSUS - MENU TREE  V1.00
Builds the navigation map: every menu the observer can see, its full path,
and the destination it opens. Needs ONLY ir.ui.menu, which is already
reachable - no pending grant required.

Output: batches/W1-SCREENS/MENU_TREE.tsv  (one row per leaf menu = one screen to capture)
        batches/W1-SCREENS/MENU_TREE.json
        stable tree hash, so a second run proves the census is reproducible.

Records what is there. Attributes nothing to a module - a screen is composed of
many modules and knowing which part came from where would require reading source.
"""
import os, ssl, json, hashlib, datetime, xmlrpc.client

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(W, "batches", "W1-SCREENS")
os.makedirs(OUT, exist_ok=True)

env = {}
_CRED = os.path.join(W, "credentials/roomb_census.env")          # BOSSDEC-003 A: census account
if not os.path.exists(_CRED):
    _CRED = os.path.join(W, "credentials/roomb_observer.env")
    print("WARNING: roomb_census.env not found - falling back to roomb_observer (narrow reach)")
print(f"account    {os.path.basename(_CRED)}")
for line in open(_CRED):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); env[k.strip()] = v.strip()
url, db, usr, pwd = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]
ctx = ssl.create_default_context()
uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx).authenticate(db, usr, pwd, {})
M = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
print(f"connected  {url} ({db}) uid={uid}")

menus = M.execute_kw(db, uid, pwd, "ir.ui.menu", "search_read", [[]],
                     {"fields": ["id", "name", "parent_id", "action", "sequence", "web_icon"],
                      "context": {"ir.ui.menu.full_list": True}})
by_id = {m["id"]: m for m in menus}
print(f"menus      {len(menus)} in the system  (full list - NOT filtered by this account's rights; RT-LANEB-017)")

def path_of(m):
    parts, seen = [], set()
    while m and m["id"] not in seen:
        seen.add(m["id"]); parts.append(m["name"])
        p = m.get("parent_id")
        m = by_id.get(p[0]) if p else None
    return " / ".join(reversed(parts))

rows = []
for m in menus:
    kids = [c for c in menus if c.get("parent_id") and c["parent_id"][0] == m["id"]]
    rows.append({
        "menu_id": m["id"],
        "path": path_of(m),
        "depth": path_of(m).count(" / ") + 1,
        "is_leaf": not kids,
        "opens": m.get("action") or "",          # e.g. ir.actions.act_window,123
        "sequence": m.get("sequence"),
        "children": len(kids),
    })
rows.sort(key=lambda r: r["path"])

leaves = [r for r in rows if r["is_leaf"] and r["opens"]]
no_dest = [r for r in rows if r["is_leaf"] and not r["opens"]]
dests = sorted({r["opens"] for r in leaves})

tsv = os.path.join(OUT, "MENU_TREE.tsv")
with open(tsv, "w", encoding="utf-8") as f:
    f.write("menu_id\tdepth\tis_leaf\tchildren\topens\tpath\n")
    for r in rows:
        f.write(f"{r['menu_id']}\t{r['depth']}\t{int(r['is_leaf'])}\t{r['children']}\t{r['opens']}\t{r['path']}\n")

# reproducibility proof: same tree -> same hash, on any later run
canon = "\n".join(f"{r['menu_id']}|{r['path']}|{r['opens']}" for r in rows) + "\n"
tree_hash = hashlib.sha256(canon.encode()).hexdigest()

meta = {"collected_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "server": url, "db": db, "observer_uid": uid,
        "menus_total": len(rows), "leaf_screens": len(leaves),
        "leaves_without_destination": len(no_dest),
        "distinct_destinations": len(dests),
        "max_depth": max(r["depth"] for r in rows) if rows else 0,
        "tree_sha256": tree_hash,
        "note": "No menu element is attributed to a module. One screen is composed "
                "of several modules and that attribution would require reading source. "
                "menus_total is the FULL system menu list (ir.ui.menu.full_list) - the census "
                "denominator - not the set visible to this account (RT-LANEB-017, 26 Sep).",
        "rows": rows}
json.dump(meta, open(os.path.join(OUT, "MENU_TREE.json"), "w"), indent=2, ensure_ascii=False)

print(f"leaves     {len(leaves)} screens to capture   ({len(no_dest)} leaf menus open nothing)")
print(f"distinct   {len(dests)} destinations   max depth {meta['max_depth']}")
print(f"tree hash  {tree_hash}")
print(f"written    {tsv}")
print("\ntop-level sections:")
for r in rows:
    if r["depth"] == 1:
        print(f"   {r['children']:>3} children   {r['path']}")
