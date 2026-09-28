#!/usr/bin/env bash
# Runs the Lane B chain unattended, every 10 minutes, for up to 8 hours.
# RED TEAM edits the scripts in this folder while you sleep; each cycle picks
# up whatever is fixed. Stops by itself on a safety trip or when told to.
#
# start :  nohup caffeinate -is bash ~/ROOMB_WORKSPACE/WATCH.sh >/dev/null 2>&1 &
#          caffeinate keeps the Mac awake - without it the loop dies at sleep.
# stop  :  touch ~/ROOMB_WORKSPACE/STOP
W=~/ROOMB_WORKSPACE
LOG=$W/WATCH.log
BASELINE=706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89
rm -f "$W/STOP"
echo "watch started $(date '+%F %H:%M')  pid $$" > "$LOG"

for i in $(seq 1 48); do
  [ -f "$W/STOP" ] && { echo "stopped by STOP file at cycle $i" >> "$LOG"; break; }

  echo "" >> "$LOG"
  echo "═══ cycle $i   $(date '+%F %H:%M') ═══" >> "$LOG"
  bash "$W/RUN_ALL.sh" >> "$LOG" 2>&1
  cp -f "$W/RUN_REPORT.txt" "$W/reports/RUN_$(date +%Y%m%d_%H%M).txt" 2>/dev/null

  # safety trip 1 - the frozen baseline must never move
  if grep -q "INSTALLED SET HASH" "$W/RUN_REPORT.txt" 2>/dev/null; then
    got=$(grep -o '[0-9a-f]\{64\}' "$W/RUN_REPORT.txt" | head -1)
    if [ -n "$got" ] && [ "$got" != "$BASELINE" ]; then
      echo "!! BASELINE MOVED - stopping. expected $BASELINE got $got" >> "$LOG"; break
    fi
  fi
  # safety trip 2 - any source path inside an artifact
  if grep -rq "site-packages\|/opt/odoo\|Traceback" "$W/batches" "$W/artifacts" 2>/dev/null; then
    echo "!! SOURCE LEAK DETECTED - stopping for RED TEAM" >> "$LOG"; break
  fi
  # success - everything green, no need to keep looping
  if grep -q "cleanup *CLEAN" "$W/RUN_REPORT.txt" 2>/dev/null \
     && grep -q "reachable 6 / 10\|reachable 7 / 10\|reachable 8 / 10\|reachable 9 / 10\|reachable 10 / 10" "$W/RUN_REPORT.txt" 2>/dev/null; then
    echo "ALL GREEN at cycle $i - nothing left to retry" >> "$LOG"; break
  fi

  sleep 600
done
echo "" >> "$LOG"
echo "watch finished $(date '+%F %H:%M')" >> "$LOG"
