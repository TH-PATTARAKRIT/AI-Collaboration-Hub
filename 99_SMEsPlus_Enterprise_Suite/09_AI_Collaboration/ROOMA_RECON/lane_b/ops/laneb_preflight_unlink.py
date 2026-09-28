#!/usr/bin/env python3
"""
LANE B PRE-FLIGHT - LIVE UNLINK CHECK   V1.00   (RED TEAM finding RT-LANEB-016)
SMEsPlus Enterprise Suite / ROOM A / Lane B

Asks the SERVER, as the observer, whether the observer may unlink its own test
records RIGHT NOW. Replaces the RUN_ALL.sh step-4 gate that grepped the grant
script's output: that grep tested what the odoo shell saw, not what the HTTP
workers enforce - and on 26 Sep the two disagreed for 6.5 hours.

Reads only. Creates nothing. Deletes nothing.
Exit 0  -> prints  UNLINK_RIGHT: LIVE     (collector may run)
Exit 1  -> prints  UNLINK_RIGHT: ABSENT   (collector must NOT run)
Exit 2  -> prints  UNLINK_RIGHT: UNKNOWN  (no usable check method; treat as ABSENT)

The access-check method differs across Odoo versions. Discovered at runtime,
never assumed: has_access(operation) first, check_access_rights second.
"""
import os, re, ssl, sys, xmlrpc.client

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(W, "credentials/roomb_observer.env")
SRC = re.compile(r"(Traceback|site-packages|/opt/odoo|File \"/)", re.I)

def scrub(t):
    t = str(t)
    if SRC.search(t):
        return "SOURCE_SCRUBBED"
    return t.strip().splitlines()[0][:160] if t.strip() else ""

def main():
    env = {}
    for line in open(CRED):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1); env[k.strip()] = v.strip()
    url, db, usr, pwd = env["ODOO_URL"], env["ODOO_DB"], env["ODOO_USER"], env["ODOO_PASSWORD"]
    ctx = ssl.create_default_context()
    uid = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", context=ctx).authenticate(db, usr, pwd, {})
    if not uid:
        print("UNLINK_RIGHT: UNKNOWN   (authentication failed)"); return 2
    M = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", context=ctx)
    def call(model, method, args, kw=None):
        try:
            return True, M.execute_kw(db, uid, pwd, model, method, args, kw or {})
        except Exception as e:
            return False, scrub(getattr(e, "faultString", None) or str(e))

    ok, ids = call("res.partner", "search",
                   [[["name", "like", "ROOMB_TEST_OBS_PARTNER"]]], {"context": {"active_test": False}})
    ids = ids if ok else []
    print(f"observer uid={uid}  {db}")
    print(f"test records present: {len(ids)}  {ids}")

    # method 1 - Odoo 18/19: has_access(operation) on the concrete records (model + record rules)
    ok, res = call("res.partner", "has_access", [ids, "unlink"])
    if ok and isinstance(res, bool):
        print(f"method: has_access(records, 'unlink') -> {res}")
        print("UNLINK_RIGHT: LIVE" if res else "UNLINK_RIGHT: ABSENT"); return 0 if res else 1
    print(f"method has_access: not usable ({res})")

    # method 2 - Odoo <= 17: check_access_rights(operation, raise_exception=False), model level only
    ok, res = call("res.partner", "check_access_rights", ["unlink"], {"raise_exception": False})
    if ok and isinstance(res, bool):
        print(f"method: check_access_rights('unlink') -> {res}   (model level only)")
        print("UNLINK_RIGHT: LIVE" if res else "UNLINK_RIGHT: ABSENT"); return 0 if res else 1
    print(f"method check_access_rights: not usable ({res})")

    print("UNLINK_RIGHT: UNKNOWN   (no usable check method on this server - treat as ABSENT)")
    return 2

if __name__ == "__main__":
    sys.exit(main())
