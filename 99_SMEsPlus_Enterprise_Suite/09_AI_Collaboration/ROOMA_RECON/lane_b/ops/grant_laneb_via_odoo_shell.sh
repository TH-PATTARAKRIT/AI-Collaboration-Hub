#!/usr/bin/env bash
# BOSSDEC-002 A : scoped access grant for the Lane B observer
# Runs ON THE STUDY SERVER, through Odoo's own shell - so NO login password is
# needed and no password is reset. V2.0 §21.2 : backup, before, apply, after, rollback.
#
# Why a NEW group: the observer currently sits in 7 SHARED groups (User, Invoicing,
# Show Full Accounting Features, Officer: Manage all employees ...). Attaching a
# right to any of those hands that right to every user in them. A dedicated group
# is the only way to grant to the observer alone.
set -uo pipefail
DB=iTest19C
CONF=/etc/odoo19.conf
BK=/root/ROOMA_BACKUP
STAMP=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BK"

# Odoo 19 here is pip-installed into a venv (evidence: server tracebacks resolve to
# /opt/odoo19/venv/lib/python3.11/site-packages/odoo/...), so the entry point is the
# console script "odoo", not a source-checkout "odoo-bin". Discover, never guess.
LAUNCH=""
for c in /opt/odoo19/venv/bin/odoo /opt/odoo19/venv/bin/odoo-bin \
         /opt/odoo19/odoo-bin /usr/bin/odoo /usr/local/bin/odoo; do
  [ -x "$c" ] && LAUNCH="$c" && break
done
# fall back to whatever the RUNNING process actually uses
if [ -z "$LAUNCH" ]; then
  LAUNCH=$(ps -eo args= | grep -m1 -oE '(/[^ ]*python[0-9.]*) +(/[^ ]*odoo(-bin)?)' | awk '{print $2}')
fi
if [ -z "$LAUNCH" ]; then
  LAUNCH=$(systemctl cat odoo19 2>/dev/null | grep -m1 ExecStart | sed 's/ExecStart=//' | awk '{print $2}')
fi
[ -z "$LAUNCH" ] && LAUNCH=$(find /opt /usr -maxdepth 5 \( -name odoo-bin -o -name odoo \) -type f -perm -u+x 2>/dev/null | head -1)

RUN_CONF=$(ps -eo args= | grep -m1 odoo | grep -oE '\-c +[^ ]+' | awk '{print $2}')
[ -n "$RUN_CONF" ] && [ -f "$RUN_CONF" ] && CONF="$RUN_CONF"

SVC_USER=$(ps -eo user:20,args= | grep -m1 '[o]doo' | awk '{print $1}')
[ -z "$SVC_USER" ] && SVC_USER=odoo
id -u "$SVC_USER" >/dev/null 2>&1 || SVC_USER=root

if [ -z "$LAUNCH" ]; then
  echo "ABORT: could not locate the Odoo launcher. Nothing changed."
  echo "  running process:"; ps -eo user:20,args= | grep '[o]doo' | head -3
  echo "  systemd unit   :"; systemctl cat odoo19 2>/dev/null | grep ExecStart
  exit 1
fi
case "$LAUNCH" in
  *venv/bin/odoo|*/bin/odoo) SHELL_CMD=("$LAUNCH") ;;
  *) PY=/opt/odoo19/venv/bin/python; [ -x "$PY" ] || PY=$(command -v python3); SHELL_CMD=("$PY" "$LAUNCH") ;;
esac
echo "launcher : ${SHELL_CMD[*]}"
echo "config   : $CONF"
echo "run as   : $SVC_USER"
echo "backup   : $BK/laneb_grant_before_$STAMP.json"
echo

cat > /tmp/_rt_grant.py <<'PYEOF'
import json, datetime
GROUP_NAME = "ROOM B Observer (Lane B)"
OBSERVER   = "roomb_observer"
GRANTS = [
    ("res.partner",           dict(perm_read=True,  perm_write=False, perm_create=False, perm_unlink=True)),
    ("ir.actions.act_window", dict(perm_read=True,  perm_write=False, perm_create=False, perm_unlink=False)),
    ("res.config.settings",   dict(perm_read=True,  perm_write=False, perm_create=False, perm_unlink=False)),
]
u = env["res.users"].search([("login", "=", OBSERVER)])
assert len(u) == 1, f"expected 1 {OBSERVER}, found {len(u)}"

# The user -> groups field was renamed across Odoo versions. Discover it at
# runtime from the ORM instead of hard-coding a name for a version we assumed.
GF = next((f for f in ("group_ids", "groups_id", "role_ids")
           if f in env["res.users"]._fields), None)
assert GF, "cannot find the user->groups field on res.users: " + \
           str([f for f in env["res.users"]._fields if "group" in f or "role" in f])
print(f"user->groups field detected: {GF}")
user_groups = u[GF]

before = {"ts": datetime.datetime.now().isoformat(),
          "observer_uid": u.id,
          "groups_field": GF,
          "groups": [{"id": g.id, "name": g.display_name} for g in user_groups],
          "access": []}
for model, _ in GRANTS:
    for a in env["ir.model.access"].search(["&", ("model_id.model", "=", model),
                                            "|", ("group_id", "in", user_groups.ids),
                                                 ("group_id", "=", False)]):
        before["access"].append(dict(id=a.id, model=model,
                                     group=a.group_id.display_name if a.group_id else "GLOBAL (all users)",
                                     r=a.perm_read, w=a.perm_write, c=a.perm_create, d=a.perm_unlink))
print("BEFORE_JSON_START"); print(json.dumps(before, indent=2, default=str)); print("BEFORE_JSON_END")

grp = env["res.groups"].search([("name", "=", GROUP_NAME)], limit=1)
created_group = False
if not grp:
    # build the payload only from fields this Odoo version actually has -
    # res.groups lost category_id in 19. Ask the ORM, never assume.
    vals = {"name": GROUP_NAME}
    gf = env["res.groups"]._fields
    for cand in ("category_id", "comment"):
        if cand == "comment" and "comment" in gf:
            vals["comment"] = "Dedicated Lane B observer group - RED TEAM / BOSSDEC-002 A"
        elif cand == "category_id" and "category_id" in gf:
            cat = env["ir.module.category"].search([("name", "=", "Extra Rights")], limit=1)
            if cat:
                vals["category_id"] = cat.id
    grp = env["res.groups"].create(vals)
    created_group = True
    print(f"CREATED group id={grp.id}  '{GROUP_NAME}'")
else:
    print(f"group already exists id={grp.id}  '{GROUP_NAME}'")

if grp.id not in u[GF].ids:
    u.write({GF: [(4, grp.id)]})
    print(f"observer uid={u.id} added to group {grp.id}")
else:
    print(f"observer uid={u.id} already in group {grp.id}")

new_rules = []
for model, perms in GRANTS:
    mid = env["ir.model"].search([("model", "=", model)], limit=1)
    if not mid:
        print(f"  {model:<24} MODEL NOT FOUND - skipped"); continue
    ex = env["ir.model.access"].search([("model_id", "=", mid.id), ("group_id", "=", grp.id)], limit=1)
    if ex:
        print(f"  {model:<24} rule already exists id={ex.id} - skipped"); continue
    flags = "_".join(k[5:] for k, v in perms.items() if v)
    a = env["ir.model.access"].create(dict(
        name=f"roomb_observer_{model.replace('.', '_')}_{flags}",
        model_id=mid.id, group_id=grp.id, **perms))
    new_rules.append(a.id)
    print(f"  {model:<24} CREATED rule id={a.id}  ({flags})")

env.cr.commit()

# The HTTP workers cache access rights in their own registry. A change committed
# from this separate shell process is invisible to them until the registry is
# signalled. Without this the grant is in the database but the observer still
# gets "you are not allowed". Run it every time, not only when rules are created.
for fn in ("clear_cache", "signal_changes", "clear_caches"):
    try:
        getattr(env.registry, fn)()
        print(f"registry.{fn}() ok")
    except Exception as ex:
        print(f"registry.{fn}() n/a ({type(ex).__name__})")
try:
    env["ir.model.access"].call_cache_clearing_methods()
    print("ir.model.access cache cleared")
except Exception as ex:
    print(f"ir.model.access cache clear n/a ({type(ex).__name__})")
env.cr.commit()

print("\nAFTER")
u.invalidate_recordset()
for a in env["ir.model.access"].search([("group_id", "=", grp.id)]):
    print(f"  {a.model_id.model:<24} id={a.id} r{int(a.perm_read)}w{int(a.perm_write)}"
          f"c{int(a.perm_create)}d{int(a.perm_unlink)}")
print(f"\nROLLBACK_RULE_IDS={new_rules}")
print(f"ROLLBACK_GROUP_ID={grp.id if created_group else 'pre-existing, do not delete'}")
PYEOF

sudo -u "$SVC_USER" "${SHELL_CMD[@]}" shell -c "$CONF" -d "$DB" --no-http < /tmp/_rt_grant.py 2>&1 \
  | tee "$BK/laneb_grant_${STAMP}.log" \
  | sed -n '/BEFORE_JSON_START/,/BEFORE_JSON_END/p;/detected\|CREATED\|already\|AFTER\|ROLLBACK\|ABORT\|Error\|error\|Assertion\|Traceback/,+6p'

sed -n '/BEFORE_JSON_START/,/BEFORE_JSON_END/p' "$BK/laneb_grant_${STAMP}.log" \
  | sed '1d;$d' > "$BK/laneb_grant_before_${STAMP}.json" 2>/dev/null
rm -f /tmp/_rt_grant.py
echo
echo "full log : $BK/laneb_grant_${STAMP}.log"
echo "ROLLBACK : delete the rule ids printed above via the same odoo shell:"
echo "           env['ir.model.access'].browse([...]).unlink(); env.cr.commit()"
