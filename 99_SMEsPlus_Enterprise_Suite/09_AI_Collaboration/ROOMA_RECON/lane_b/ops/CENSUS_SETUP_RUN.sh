#!/usr/bin/env bash
# ONE COMMAND - BOSSDEC-003 implementation chain (RED TEAM, Lane B, 26 Sep 2026)
# Creates roomb_census on the study server (odoo shell over SSH), fetches its credentials to a 0600
# file, verifies the account from the observer side, checks the server error log window and the
# frozen baseline. Survives step failures and writes one report. Re-runnable: the server script
# ABORTs if the login already exists, so a second run changes nothing.
#   run  :  bash ~/ROOMB_WORKSPACE/ops/CENSUS_SETUP_RUN.sh
W=~/ROOMB_WORKSPACE
SRV=root@103.253.74.217
TS=$(date +%Y%m%d_%H%M%S)
R=$W/reports/CENSUS_SETUP_RUN_${TS}.txt
: > "$R"
say(){ echo "$@" | tee -a "$R"; }
step(){ say ""; say "──────── $1"; }
say "CENSUS SETUP RUN   $(date '+%F %H:%M')   (BOSSDEC-003 A/B/C/D - Boss approved 26 Sep)"

step "0/6  pre-conditions"
say "remote script sha256 : $(shasum -a 256 "$W/ops/create_census_account_via_odoo_shell.sh" | cut -c1-16)"
if [ -f "$W/credentials/roomb_census.env" ]; then
  say "     credentials/roomb_census.env already exists - account setup was done before. STOP (nothing run)."; exit 0; fi
ROOMB_CREDENTIALS=$W/credentials/roomb_observer.env python3 "$W/collectors/installed_set_hash.py" 2>&1 | grep -E "INSTALLED|RESULT" | tee -a "$R"

step "1/6  create roomb_census (server, odoo shell)  - §21.2 backup/before/apply inside the script"
ssh -o BatchMode=yes -o ConnectTimeout=15 $SRV 'bash -s' < "$W/ops/create_census_account_via_odoo_shell.sh" 2>&1 \
  | grep -vE "ODOO_PASSWORD" | tee -a "$R" | grep -E "launcher|ABORT|CREATED|closure|forbidden|ROLLBACK|credentials|full log|ok |match"
CREATED=$(grep -c "^CREATED user" "$R")

step "2/6  fetch credentials (0600, never printed)"
if [ "$CREATED" -ge 1 ]; then
  mkdir -p "$W/credentials"
  if scp -o BatchMode=yes -q $SRV:/root/ROOMA_BACKUP/roomb_census.env "$W/credentials/roomb_census.env"; then
    chmod 600 "$W/credentials/roomb_census.env"; say "     fetched -> credentials/roomb_census.env (mode $(stat -f '%Lp' "$W/credentials/roomb_census.env"))"
  else say "     FAILED - scp; credentials remain on the server at /root/ROOMA_BACKUP/roomb_census.env"; fi
else say "     SKIPPED - account not created (see step 1)"; fi

step "3/6  server error-log window (read-only)"
ssh -o BatchMode=yes -o ConnectTimeout=15 $SRV 'LOGF=$(grep -E "^\s*logfile" /etc/odoo19.conf | awk -F= "{print \$2}" | tr -d " "); { journalctl -u odoo19 --since "5 min ago" --no-pager 2>/dev/null; [ -n "$LOGF" ] && tail -n 400 "$LOGF" 2>/dev/null; } | grep -iE "error|traceback|critical" | grep -v "Mute this logger" | tail -10; echo "     log-window-check done"' 2>&1 | tee -a "$R"

step "4/6  verify roomb_census from the observer side (read-only)"
if [ -f "$W/credentials/roomb_census.env" ]; then
  python3 "$W/ops/census_account_verify.py" "$W/credentials/roomb_census.env" 2>&1 | tee -a "$R" | grep -E "account|groups|forbidden|ui reach|baseline|write-audit|VERIFY|written"
else say "     SKIPPED - no credentials file"; fi

step "5/6  baseline regression as roomb_observer (reference script)"
ROOMB_CREDENTIALS=$W/credentials/roomb_observer.env python3 "$W/collectors/installed_set_hash.py" 2>&1 | grep -E "INSTALLED|RESULT" | tee -a "$R"

step "6/6  clean-room scan of this report"
if grep -qE "site-packages|/opt/odoo|Traceback" "$R"; then
  python3 - "$R" <<'PY'
import re,sys; p=sys.argv[1]; t=open(p).read()
t=re.sub(r'/opt/[\w/\.\-]*','<REDACTED_PATH>',t); t=re.sub(r'[\w/\.\-]*site-packages[\w/\.\-]*','<REDACTED_PATH>',t); t=t.replace("Traceback","<REDACTED_TRACE>")
open(p,"w").write(t); print("     report scrubbed of install/source paths")
PY
else say "     CLEAN"; fi
say ""; say "════════ SUMMARY"
say "created            : $CREATED"
say "verify             : $(grep -o 'VERIFY: [A-Z].*' "$R" | tail -1)"
say "ui reach (census)  : $(grep -o 'ui reach .*' "$R" | tail -1)"
say "baseline           : $(grep -o 'RESULT *: [A-Z]*' "$R" | tail -1)"
say "rollback           : archive the user via odoo shell (non-destructive) - see ROLLBACK line above"
say "report             : $R"
