#!/usr/bin/env bash
# RED TEAM DIAGNOSTIC - who is the administrator on this database?
# Runs ON THE STUDY SERVER. READ ONLY. No password, no hash is ever printed.
set -uo pipefail
DB=iTest19C
echo "diagnostic $(date -Is)  db=$DB"
echo

PSQL=""
if sudo -u postgres psql -d "$DB" -tAc "select 1" >/dev/null 2>&1; then
  PSQL="sudo -u postgres psql -d $DB -tAc"
elif psql -U odoo -d "$DB" -tAc "select 1" >/dev/null 2>&1; then
  PSQL="psql -U odoo -d $DB -tAc"
fi
if [ -z "$PSQL" ]; then
  echo "cannot open a read-only psql session as postgres or odoo"
  echo "run manually:  sudo -u postgres psql -d $DB"
  exit 1
fi

echo "1. every login on this database"
printf "   %-5s %-28s %-7s %-7s %s\n" uid login active share "password set"
$PSQL "select u.id, u.login, u.active, u.share, (u.password is not null and u.password <> '')
       from res_users u order by u.id" |
while IFS='|' read -r id login active share haspw; do
  printf "   %-5s %-28s %-7s %-7s %s\n" "$id" "$login" "$active" "$share" "$haspw"
done

echo
echo "2. who holds Settings / Administration rights"
$PSQL "select u.id, u.login, g.name->>'en_US'
       from res_users u
       join res_groups_users_rel r on r.uid = u.id
       join res_groups g on g.id = r.gid
       where g.name::text ilike '%Settings%' or g.name::text ilike '%Admin%'
       order by u.id" |
while IFS='|' read -r id login grp; do
  printf "   uid %-5s %-28s %s\n" "$id" "$login" "$grp"
done

echo
echo "3. the Lane B observer's groups (for the grant script)"
$PSQL "select g.id, g.name->>'en_US'
       from res_users u
       join res_groups_users_rel r on r.uid = u.id
       join res_groups g on g.id = r.gid
       where u.login = 'roomb_observer' order by g.id" |
while IFS='|' read -r gid gname; do
  printf "   group %-6s %s\n" "$gid" "$gname"
done

echo
echo "4. menu count visible in the database (census scope check)"
$PSQL "select count(*) from ir_ui_menu" | sed 's/^/   ir_ui_menu rows: /'

echo
echo "READ ONLY - nothing on this server was modified."
