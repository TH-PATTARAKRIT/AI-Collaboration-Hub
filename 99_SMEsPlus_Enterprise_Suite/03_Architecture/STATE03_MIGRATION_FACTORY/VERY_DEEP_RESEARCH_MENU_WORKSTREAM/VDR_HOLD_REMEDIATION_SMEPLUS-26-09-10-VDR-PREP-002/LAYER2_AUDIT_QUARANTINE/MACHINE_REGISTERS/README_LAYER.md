# MACHINE_REGISTERS — VDR-PREP-002

**LAYER 2 — AUDIT QUARANTINE.** Reference-ERP and deployment identifiers throughout.
Boss / PMO / AI-Audit only. Nothing here may be transcribed onto a LAYER 1 surface.

## Runtime evidence — how it was obtained, reproducibly

No database server was started. Two extraction routes, both server-free:

```
# plain-SQL dump: parse the COPY block directly
python3 copyx.py <dump.sql> <table>          > <table>.csv

# custom-format archive: extract one table, then parse
pg_restore --data-only -t <table> -f - <dump> > <table>.sql
python3 copyx2.py <table>.sql                 > <table>.csv
```

**A newer archive client was required** for the custom-format artefacts: the older client reports
*"unsupported version (1.16) in file header"*. **That is unreadable-by-this-client, not absent.**

**Coverage assertion is mandatory on every extraction.** `copyx.py` prints rows returned; that figure
must be compared against the block length in the source dump. The first extraction run in this session
was truncated by a pipe that closed early — it returned 584 rows of 34,164 and produced a **0%**
menu-presence result that was entirely false.

## Deployments

| Ref | Generation | Modules installed | Inventory menus present | Stock movements | On-hand rows |
|-----|-----------|------------------:|------------------------:|----------------:|-------------:|
| `iEVING` | 19.0.1.3 | 216 | 46 / 62 | 0 | 0 |
| `iTEST02` | 19.0.1.3 | 486 | 52 / 62 | 48 | 0 |
| `iSMEs` | **16.0.1.3** | 190 | not enumerated | **103,949** | **27,196** |

`database_artefact_census.txt` holds the artefact census: 236 candidates checked, 15 artefacts,
**6 distinct database identities**, 3 examined.

## Files

| File | Contents |
|------|----------|
| `LEARNING_POPULATION.csv` | the population, now carrying a measured `reachability` on every row |
| `ownership_final.json` · `primary_owner.json` | Workstream B — ownership class and dependency-graph-derived primary owner |
| `reach.json` · `reachability_summary.txt` | Workstream C — menu, module and scheduled-job reachability |
| `prior_map.json` · `recon_status.json` · `prior_density3.txt` | Workstream D — scope mapping and the instrument-controlled dimension measurement |
| `delta_evidence.txt` | targeted delta evidence for the ten unresearched live menus |
| `coverage_recalc.txt` | the recalculated populations |
| `runtime/<db>/*.csv` | the extracted deployment tables (files above 3 MB were not committed) |
