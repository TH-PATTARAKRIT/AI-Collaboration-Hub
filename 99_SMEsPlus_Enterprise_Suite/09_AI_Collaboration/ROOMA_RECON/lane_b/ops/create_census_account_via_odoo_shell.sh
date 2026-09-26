#!/usr/bin/env bash
# BOSSDEC-003 A/B/C/D : create the Lane B CENSUS account  roomb_census   (RED TEAM, 26 Sep 2026)
# Runs ON THE STUDY SERVER through Odoo's own shell (no admin login needed).
# V2.0 §21.2 : backup · before · apply · after · rollback.   All-or-nothing: any unresolved
# group, any forbidden group in the resulting closure, or an existing login -> ABORT, nothing committed.
#
# Two-account model (Boss, 26 Sep): roomb_observer = narrow S6 transaction account (unchanged);
# roomb_census = wide read-by-procedure census account, app-level groups only.
# NEVER: Role/Administrator (base.group_system), Access Rights, Technical, or any deferred-section group
# (Website / Live Chat / eLearning / Link Tracker family) - BOSSDEC-003 B + C.
# The password is generated inside the odoo shell, never printed, written to a 0600 file only.
set -uo pipefail
DB=iTest19C
CONF=/etc/odoo19.conf
BK=/root/ROOMA_BACKUP
STAMP=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BK"

LAUNCH=""
for c in /opt/odoo19/venv/bin/odoo /opt/odoo19/venv/bin/odoo-bin /opt/odoo19/odoo-bin /usr/bin/odoo /usr/local/bin/odoo; do
  [ -x "$c" ] && LAUNCH="$c" && break
done
[ -z "$LAUNCH" ] && LAUNCH=$(ps -eo args= | grep -m1 -oE '(/[^ ]*python[0-9.]*) +(/[^ ]*odoo(-bin)?)' | awk '{print $2}')
RUN_CONF=$(ps -eo args= | grep -m1 odoo | grep -oE '\-c +[^ ]+' | awk '{print $2}')
[ -n "$RUN_CONF" ] && [ -f "$RUN_CONF" ] && CONF="$RUN_CONF"
SVC_USER=$(ps -eo user:20,args= | grep -m1 '[o]doo' | awk '{print $1}'); [ -z "$SVC_USER" ] && SVC_USER=odoo
id -u "$SVC_USER" >/dev/null 2>&1 || SVC_USER=root
[ -z "$LAUNCH" ] && { echo "ABORT: could not locate the Odoo launcher. Nothing changed."; exit 1; }
case "$LAUNCH" in
  *venv/bin/odoo|*/bin/odoo) SHELL_CMD=("$LAUNCH") ;;
  *) PY=/opt/odoo19/venv/bin/python; [ -x "$PY" ] || PY=$(command -v python3); SHELL_CMD=("$PY" "$LAUNCH") ;;
esac
TMP_ENV=/tmp/.roomb_census_${STAMP}.env
echo "launcher : ${SHELL_CMD[*]}"; echo "config   : $CONF"; echo "run as   : $SVC_USER"
echo "backup   : $BK/census_account_before_$STAMP.json"; echo

cat > /tmp/_rt_census.py <<'PYEOF'
import json, datetime, secrets, os
LOGIN, NAME, COMPANY = "roomb_census", "ROOM B Census (Lane B)", 2
TMP_ENV = os.environ.get("TMP_ENV", "/tmp/.roomb_census.env")
URL = "https://t9c.smeplus.asia"

# (privilege name or None, group name) - measured on 26 Sep from ir.ui.menu.group_ids gating the hidden
# leaf screens (reports/RT-SEC-003_groups_needed.json). App-level only. BOSSDEC-003 B.
WANT = [
    (None, "Role / User"),                              # internal user - required to log in (probed 26 Sep 11:10: the group's name is literally "Role / User", no privilege)
    ("Sales", "Administrator"),
    ("Accounting", "Administrator"), (None, "Analytic Accounting"),
    ("Expenses", "Administrator"), ("Expenses", "All Approver"),
    ("Inventory", "Administrator"),
    ("Purchase", "Administrator"),
    ("Employees", "Administrator"),
    ("Recruitment", "Interviewer"),                     # Officer/Administrator imply "Website / Restricted Editor" (probed 11:47) -> excluded, BOSSDEC-003 C
    ("Project", "Administrator"),
    ("Fleet", "Administrator"), ("Fleet", "Officer: Manage all vehicles"),
    ("Manufacturing", "Administrator"),
    ("Time Off", "Administrator"), ("Time Off", "Officer: Manage all requests"), (None, "Time Off Responsible"),
    ("Events", "User"),                                 # Administrator implies "Website / Restricted Editor" (probed 11:47) -> excluded, BOSSDEC-003 C
    ("Attendances", "Administrator"), ("Attendances", "Officer: Manage all attendances"), (None, "Officer: Manage attendances"),
    ("Timesheets", "User: all timesheets"), ("Timesheets", "User: own timesheets only"),
    ("Surveys", "User"),
    ("Contact", "Creation"),
    (None, "Show Lead Menu"), (None, "Show Recurring Revenues Menu"),
]
# Forbidden anywhere in the resulting closure. BOSSDEC-003 B (system/technical) + C (deferred sections).
FORBID_EXACT = [("Role", "Administrator"), (None, "Role / Administrator"), (None, "Access Rights"), ("Administration", "Access Rights"),
                ("Administration", "Settings"), (None, "Technical Features"), ("Role", "Technical"), (None, "Role / Technical")]
FORBID_PRIV  = {"Website", "Live Chat", "eLearning", "Link Tracker", "Mail Group"}
FORBID_NAME_SUB = ["Mail Group Administrator", "Website / Editor", "Editor and Designer"]

G = env["res.groups"]
def find(priv, name):
    dom = [("name", "=", name)]
    dom += [("privilege_id.name", "=", priv)] if priv else [("privilege_id", "=", False)]
    return G.search(dom)
def label(g):
    p = g.privilege_id.name if g.privilege_id else None
    return f"{p} / {g.name}" if p else g.name

resolved, problems = [], []
for priv, name in WANT:
    r = find(priv, name)
    if len(r) != 1:
        problems.append(f"  {priv} / {name}: {len(r)} match(es)")
    else:
        resolved.append(r)
print("RESOLUTION")
for r in resolved:
    print(f"  ok   id={r.id:<4} {label(r)}")
if problems:
    print("ABORT: unresolved group(s) - nothing created:"); print("\n".join(problems)); raise SystemExit(2)

GF = next((f for f in ("group_ids", "groups_id") if f in env["res.users"]._fields), None)
assert GF, "cannot find the user->groups field on res.users"
if env["res.users"].with_context(active_test=False).search([("login", "=", LOGIN)]):
    print(f"ABORT: login '{LOGIN}' already exists - nothing created. Inspect it first."); raise SystemExit(3)

# closure check BEFORE creating: what would the user end up holding?
direct = G.browse([r.id for r in resolved])
closure = direct
for _ in range(10):
    nxt = closure | closure.mapped("all_implied_ids") if "all_implied_ids" in G._fields else closure | closure.mapped("implied_ids")
    if nxt == closure: break
    closure = nxt
bad = []
for g in closure:
    p = g.privilege_id.name if g.privilege_id else None
    if (p, g.name) in FORBID_EXACT or (p in FORBID_PRIV) or any(s in label(g) for s in FORBID_NAME_SUB):
        bad.append(label(g))
    if not p and g.name == "Access Rights": bad.append(label(g))
print(f"closure: {len(closure)} groups after implication")
if bad:
    print("ABORT: forbidden group(s) would be implied - nothing created:"); print("\n".join("  " + b for b in sorted(set(bad)))); raise SystemExit(4)

before = {"ts": datetime.datetime.now().isoformat(), "login": LOGIN, "groups_field": GF,
          "direct_groups": [{"id": g.id, "name": label(g)} for g in direct],
          "closure_count": len(closure), "closure": [label(g) for g in closure],
          "users_count_before": env["res.users"].with_context(active_test=False).search_count([])}
print("BEFORE_JSON_START"); print(json.dumps(before, indent=2, default=str)); print("BEFORE_JSON_END")

pwd = secrets.token_urlsafe(24)
u = env["res.users"].with_context(no_reset_password=True).create({
    "name": NAME, "login": LOGIN, "password": pwd,
    "company_id": COMPANY, "company_ids": [(6, 0, [COMPANY])],
    GF: [(6, 0, direct.ids)],
})
u.invalidate_recordset()
allg = u.all_group_ids if "all_group_ids" in u._fields else u[GF]
post_bad = [label(g) for g in allg if (g.privilege_id.name if g.privilege_id else None, g.name) in FORBID_EXACT
            or (g.privilege_id and g.privilege_id.name in FORBID_PRIV) or any(s in label(g) for s in FORBID_NAME_SUB)]
if post_bad:
    env.cr.rollback(); print("ABORT after create: forbidden group present -> ROLLED BACK, nothing committed:"); print("\n".join("  " + b for b in post_bad)); raise SystemExit(5)

fd = os.open(TMP_ENV, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)   # 0600 from the first byte
os.write(fd, f"ODOO_URL={URL}\nODOO_DB={env.cr.dbname}\nODOO_USER={LOGIN}\nODOO_PASSWORD={pwd}\n".encode())
os.close(fd)
del pwd
env.cr.commit()
for fn in ("clear_cache", "signal_changes"):
    try: getattr(env.registry, fn)(); print(f"registry.{fn}() ok")
    except Exception as ex: print(f"registry.{fn}() n/a ({type(ex).__name__})")
env.cr.commit()
print(f"\nCREATED user uid={u.id} login={LOGIN} company={COMPANY} direct_groups={len(direct)} all_groups={len(allg)}")
print("AFTER_GROUPS_START"); print("\n".join("  " + label(g) for g in allg)); print("AFTER_GROUPS_END")
print(f"ROLLBACK: env['res.users'].browse({u.id}).write({{'active': False}}); env.cr.commit()   # archive, non-destructive")
PYEOF

TMP_ENV="$TMP_ENV" sudo -E -u "$SVC_USER" "${SHELL_CMD[@]}" shell -c "$CONF" -d "$DB" --no-http < /tmp/_rt_census.py 2>&1 \
  | tee "$BK/census_account_${STAMP}.log" \
  | grep -vE "ODOO_PASSWORD|token" \
  | sed -n '/RESOLUTION/,/BEFORE_JSON_START/p;/BEFORE_JSON_END/,$p'
sed -n '/BEFORE_JSON_START/,/BEFORE_JSON_END/p' "$BK/census_account_${STAMP}.log" | sed '1d;$d' > "$BK/census_account_before_${STAMP}.json" 2>/dev/null
rm -f /tmp/_rt_census.py
if [ -f "$TMP_ENV" ]; then
  mv "$TMP_ENV" "$BK/roomb_census.env" && chmod 600 "$BK/roomb_census.env" && chown root:root "$BK/roomb_census.env"
  echo "credentials: $BK/roomb_census.env (0600 root) - fetch with scp, never cat into a chat"
else
  echo "no credentials file produced - the account was NOT created (see ABORT above)"
fi
echo "full log : $BK/census_account_${STAMP}.log"
