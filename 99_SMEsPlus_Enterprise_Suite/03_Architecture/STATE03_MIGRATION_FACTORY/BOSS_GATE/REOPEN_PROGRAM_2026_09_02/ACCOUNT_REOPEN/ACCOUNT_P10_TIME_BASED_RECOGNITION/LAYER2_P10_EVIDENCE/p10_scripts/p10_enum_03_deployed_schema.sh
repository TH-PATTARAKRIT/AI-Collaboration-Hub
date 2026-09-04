#!/bin/bash
# P10-ENUM-03 : DEPLOYED-DATABASE CORRELATION (Stage E cross-layer)
# POPULATION : every database dump available on the execution host
# PATTERN    : schema-only extraction via pg_restore -s, then targeted data-only
#              extraction (pg_restore -a -t <table>) for the small P10 tables
# UNIT       : one deployed database
# PATH SET   : $HOME/Downloads/*.dump  -- declared, enumerated, not assumed
# NOTE       : every zero below is printed together with the byte size of the
#              artefact it was counted from, so an empty extraction cannot be
#              mistaken for an empty table.
set -u
OUT="${1:-.}"
for d in "$HOME"/Downloads/*.dump; do
  n=$(basename "$d" .dump)
  echo "=== $n ==="
  if ! pg_restore -s -f "$OUT/schema_$n.sql" "$d" 2>"$OUT/err_$n.txt"; then
    echo "  SCHEMA EXTRACTION FAILED: $(head -1 "$OUT/err_$n.txt")"; continue
  fi
  echo "  schema bytes: $(wc -c < "$OUT/schema_$n.sql")"
  for probe in deferred_start_date deferred_end_date account_move_deferred_rel \
               generate_deferred_expense_entries_method \
               "CREATE TABLE public.account_asset " \
               "CREATE TABLE public.account_loan" \
               "CREATE TABLE public.account_transfer_model" \
               "CREATE TABLE public.account_account_res_company_rel"; do
    echo "  hits[$probe] = $(grep -c "$probe" "$OUT/schema_$n.sql")"
  done
  for t in account_account_res_company_rel res_company account_move_deferred_rel; do
    if pg_restore -a -t "$t" -f "$OUT/${t}_$n.txt" "$d" 2>/dev/null; then
      echo "  data[$t] artefact bytes: $(wc -c < "$OUT/${t}_$n.txt")"
    fi
  done
done
