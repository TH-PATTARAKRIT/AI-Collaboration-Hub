# MCC enumeration and verification scripts

Retained for `MC-04` repeatability. Each is a single-pass `grep`/`find`/`wc` over a declared path
set; none depends on judgement. Run from any working directory — absolute source paths are embedded.

| Script | Purpose |
|---|---|
| `recount.sh` | Independent recount of 15 source-derived Wave A denominators |
| `v3.sh` | Wave A model count, `_check_company_auto` / `check_company=True` enforcement surface |
| `xver.sh` | Cross-version matrix of rate-model company scoping |
| `ncscan.sh` | Negative-claim token load across the MC and MCC packages |
| `compliance.sh` | Prohibited-wording scan (self-declared PASS / approval / gate movement) |

**Known false-positive mode of `compliance.sh`:** a case-insensitive scan for the token `PASS`
collides with the fixed-point protocol's own pass numbering (`Pass 1`, `PASSES 2 AND 3`,
`FIRST PASS`). The retained script is case-sensitive on the uppercase token and excludes the
legitimate verdict forms. Declared here because a compliance scan's own error rate is part of its
declaration.
