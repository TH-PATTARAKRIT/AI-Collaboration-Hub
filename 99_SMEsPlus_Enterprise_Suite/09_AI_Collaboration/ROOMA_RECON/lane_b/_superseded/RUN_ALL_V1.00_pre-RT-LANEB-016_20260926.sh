#!/usr/bin/env bash
# ONE COMMAND. Runs the whole Lane B chain, survives its own failures,
# and writes a single report at the end. Re-runnable - nothing is done twice.
W=~/ROOMB_WORKSPACE
SRV=root@103.253.74.217
R=$W/RUN_REPORT.txt
: > "$R"
say(){ echo "$@" | tee -a "$R"; }
step(){ say ""; say "──────── $1"; }

say "LANE B RUN   $(date '+%F %H:%M')"

step "1/5  grant scoped access (server)"
if ssh -o BatchMode=yes -o ConnectTimeout=15 $SRV 'bash -s' < "$W/ops/grant_laneb_via_odoo_shell.sh" >>"$R" 2>&1; then
  say "     ok"; else say "     FAILED - see detail above; chain continues"; fi

step "2/5  verify what the observer can now reach"
python3 "$W/ops/census_feasibility_probe.py" 2>&1 | tee -a "$R" | tail -4

step "3/5  menu tree census  (needs no grant)"
python3 "$W/collectors/census_menu_tree.py" 2>&1 | tee -a "$R" | grep -E "menus|leaves|tree hash" 

step "4/5  standard batch + test-record cleanup"
# GATE: this collector CREATES 2 test records per run. Running it before the
# observer can delete them turns an unattended loop into a record generator.
# Only run it once the unlink right is actually in place.
if grep -qE "res\.partner .*d1|roomb_observer_res_partner_.*unlink" "$R" 2>/dev/null; then
  python3 "$W/collectors/stage1a_collector_V2.py" 2>&1 | tee -a "$R" | grep -E "baseline|cleanup|done"
else
  say "     SKIPPED - unlink right not in place yet."
  say "     Running it now would create 2 test records this cycle and every cycle,"
  say "     with no way to remove them. Waiting for the grant instead."
  python3 - <<'PYCHK' 2>&1 | tee -a "$R"
import os,ssl,xmlrpc.client
W=os.path.expanduser("~/ROOMB_WORKSPACE")
e={}
for l in open(W+"/credentials/roomb_observer.env"):
    l=l.strip()
    if l and not l.startswith("#") and "=" in l:
        k,v=l.split("=",1); e[k.strip()]=v.strip()
c=ssl.create_default_context()
u=xmlrpc.client.ServerProxy(e["ODOO_URL"]+"/xmlrpc/2/common",context=c).authenticate(e["ODOO_DB"],e["ODOO_USER"],e["ODOO_PASSWORD"],{})
M=xmlrpc.client.ServerProxy(e["ODOO_URL"]+"/xmlrpc/2/object",context=c)
ids=M.execute_kw(e["ODOO_DB"],u,e["ODOO_PASSWORD"],"res.partner","search",
                 [[["name","like","ROOMB_TEST_OBS_PARTNER"]]],{"context":{"active_test":False}})
print(f"     test records still in the study database: {len(ids)}  {ids}")
PYCHK
fi

step "5/5  clean room check"
if grep -rl "site-packages\|/opt/odoo\|Traceback" "$W/batches" "$W/artifacts" 2>/dev/null; then
  say "     SOURCE LEAK FOUND in the files listed above"
else say "     CLEAN - no source path in any artifact"; fi

say ""
say "════════ SUMMARY"
say "reachable surfaces : $(grep -o 'reachable [0-9]* / 10' "$R" | tail -1)"
say "menus              : $(grep -o 'menus *[0-9]*' "$R" | tail -1)"
say "screens to capture : $(grep -o 'leaves *[0-9]*' "$R" | tail -1)"
say "baseline           : $(grep -o 'baseline *[A-Z]*' "$R" | tail -1)"
say "test records       : $(grep -o 'cleanup *[A-Z_]*' "$R" | tail -1)"
say ""
say "full log: $R"
say "next: open Gemini and send one line ->  อ่าน ~/ROOMB_WORKSPACE/GEMINI_TASK.md แล้วทำตาม"
