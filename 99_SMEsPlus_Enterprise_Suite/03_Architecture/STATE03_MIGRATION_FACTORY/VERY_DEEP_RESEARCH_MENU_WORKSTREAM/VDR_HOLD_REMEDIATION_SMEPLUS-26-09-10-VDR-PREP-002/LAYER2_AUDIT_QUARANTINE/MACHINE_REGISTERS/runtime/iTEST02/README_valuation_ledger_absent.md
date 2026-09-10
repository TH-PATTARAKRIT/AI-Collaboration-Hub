# Valuation-ledger table — ABSENT from this deployment

`LAYER 2`. Extraction of the series-18 valuation-ledger table from this **series-19** deployment
returns **no COPY block**: the table does not exist in the database.

This is recorded as a file rather than as a zero-byte extract, because **a zero-byte file is
indistinguishable from a failed extraction**. The absence is the finding — see
`00C_RUNTIME_REACHABILITY_MATRIX.md` `RR-F-06`.

Reproduce:
```
pg_restore --data-only -t <valuation ledger table> -f - <this deployment's dump>
# -> produces no COPY block
```
The same command against the series-16 deployment returns **74,982 rows**.
