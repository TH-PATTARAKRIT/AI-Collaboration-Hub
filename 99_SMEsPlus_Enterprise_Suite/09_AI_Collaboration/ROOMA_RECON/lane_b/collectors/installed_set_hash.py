#!/usr/bin/env python3
"""
INSTALLED SET HASH — Lane B collector  v1.00
SMEsPlus Enterprise Suite · ROOM A

Reproduces the frozen installed-set hash from the LIVE study instance, using the
ORIGINAL formula. Do not rewrite the formula. Per Project Instructions V2.0 §15:
a re-derived value that disagrees is an error in the derivation until proven otherwise.

    sha256( "\n".join(sorted(installed_module_names)) + "\n" )

Credentials are read from a file OUTSIDE this workspace and are never printed.
Set ROOMB_CREDENTIALS to override the default path.

    python3 collectors/installed_set_hash.py
"""
import os, re, ssl, sys, hashlib, xmlrpc.client

EXPECTED = "706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89"
URL      = "https://t9c.smeplus.asia"
CRED     = os.environ.get("ROOMB_CREDENTIALS", os.path.expanduser("~/ROOMB_CREDENTIALS.txt"))


def grab(txt, *keys):
    for k in keys:
        m = re.search(rf'^\s*{k}\s*[:=]\s*(\S+)', txt, re.I | re.M)
        if m:
            return m.group(1)
    return None


def main():
    if not os.path.exists(CRED):
        print(f"BLOCKED — credentials file not found at {CRED}")
        print("Ask Boss for the path. Never paste credentials into a chat, a log or a record.")
        return 2

    txt = open(CRED).read()
    db  = grab(txt, 'database', 'db') or 'iTest19C'
    usr = grab(txt, 'odoo_user', 'user', 'login') or 'roomb_observer'
    pwd = grab(txt, 'odoo_password', 'password', 'pwd')
    if not pwd:
        print("BLOCKED — no password found in the credentials file.")
        return 2

    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except Exception:
        ctx = ssl.create_default_context()

    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common", context=ctx)
    uid = common.authenticate(db, usr, pwd, {})
    if not uid:
        print(f"BLOCKED — authentication failed for {usr} on {db}.")
        return 2

    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object", context=ctx)
    names = models.execute_kw(db, uid, pwd, 'ir.module.module', 'search_read',
                              [[('state', '=', 'installed')]], {'fields': ['name']})
    mods = sorted(m['name'] for m in names)
    digest = hashlib.sha256(("\n".join(mods) + "\n").encode()).hexdigest()

    print(f"DB                : {db}")
    print(f"USER              : {usr}  (uid {uid})")
    print(f"INSTALLED MODULES : {len(mods)}")
    print(f"INSTALLED SET HASH: {digest}")
    print(f"EXPECTED          : {EXPECTED}")
    if digest == EXPECTED:
        print("RESULT            : MATCH — the frozen baseline is intact.")
        return 0
    print("RESULT            : MISMATCH")
    print("Do NOT file any record. Report this as a control finding and stop.")
    print("The runtime has changed, or the formula was altered. Either way, stop.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
