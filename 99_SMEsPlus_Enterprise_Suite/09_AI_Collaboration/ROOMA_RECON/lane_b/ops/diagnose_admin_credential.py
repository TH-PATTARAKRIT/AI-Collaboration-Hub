#!/usr/bin/env python3
"""
RED TEAM DIAGNOSTIC - which credential opens which door?
Runs ON THE STUDY SERVER. READ ONLY. Changes nothing.

Prints NO password. Only: file sizes, sha256 prefixes, and MATCH / NO MATCH.
V2.0 §21.4 - a secret is never printed to a chat, a log or a screenshot.
"""
import os, glob, hashlib, datetime, xmlrpc.client, configparser, io

URL, DB = "http://127.0.0.1:8069", "iTest19C"
print(f"diagnostic {datetime.datetime.now().isoformat(timespec='seconds')}  db={DB}\n")

# ---- 1. what credential files exist -----------------------------------
print("1. credential files on this server")
cands = {}
for p in sorted(glob.glob("/root/*PASSWD*") + glob.glob("/root/*passwd*")):
    try:
        v = open(p).read().strip()
    except Exception as e:
        print(f"   {p:<36} unreadable ({e})"); continue
    st = os.stat(p)
    h = hashlib.sha256(v.encode()).hexdigest()
    cands[p] = v
    print(f"   {p:<36} {st.st_size:>4}B  mode {oct(st.st_mode)[-3:]}  "
          f"mtime {datetime.datetime.fromtimestamp(st.st_mtime):%Y-%m-%d %H:%M}  "
          f"len {len(v)}  sha256 {h[:12]}")

# ---- 2. what odoo.conf holds ------------------------------------------
print("\n2. odoo.conf master password (admin_passwd)")
conf_val = None
for cf in ("/etc/odoo19.conf", "/etc/odoo.conf", "/opt/odoo19/odoo.conf"):
    if os.path.exists(cf):
        cp = configparser.ConfigParser()
        cp.read_string("[options]\n" + "\n".join(
            l for l in open(cf) if not l.strip().startswith("[")))
        conf_val = cp.get("options", "admin_passwd", fallback=None)
        print(f"   {cf}: admin_passwd " + ("present" if conf_val else "ABSENT"))
        if conf_val:
            print(f"      len {len(conf_val)}  sha256 {hashlib.sha256(conf_val.encode()).hexdigest()[:12]}")
            for p, v in cands.items():
                print(f"      vs {os.path.basename(p):<28} "
                      + ("MATCH  <- this file IS the master password"
                         if v == conf_val else "no match"))
        break
else:
    print("   no odoo conf file found at the usual paths")

# ---- 3. which file is a LOGIN password, and for which login -----------
print("\n3. login test (xmlrpc authenticate) - no value is printed")
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
logins = ["admin", "Admin", "administrator", "root", "smesplus", "boss"]
works = []
for p, v in cands.items():
    for lg in logins:
        try:
            uid = common.authenticate(DB, lg, v, {})
        except Exception:
            uid = None
        if uid:
            works.append((lg, p, uid))
            print(f"   OPENS  login '{lg}'  uid={uid}  <- {os.path.basename(p)}")
if not works:
    print("   none of these files is a login password for any of the tried logins")
    print(f"   logins tried: {', '.join(logins)}")

# ---- 4. what admin-capable logins exist (needs one working login) -----
print("\n4. admin-capable logins on this database")
if works:
    lg, p, uid = works[0]
    pw = cands[p]
    M = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
    try:
        us = M.execute_kw(DB, uid, pw, "res.users", "search_read",
                          [[["active", "in", [True, False]]]],
                          {"fields": ["id", "login", "share"]})
        for u in us:
            print(f"   uid {u['id']:<4} login '{u['login']}'")
    except Exception as e:
        print("   could not list users:", str(e).splitlines()[0][:80])
else:
    print("   SKIPPED - no working login, cannot list users")

print("""
CONCLUSION
  If section 2 shows MATCH, that file is the DATABASE MASTER password
  (used for backup/restore/create), not a user login - authenticating with
  it will always fail, which is what the grant script reported.
  If section 3 shows nothing at all, the admin LOGIN password is not on
  this server in any file, and it must be reset before the grant can run.
  Nothing on this server was modified by this diagnostic.
""")
