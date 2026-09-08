# 05_RC05_P08_CHALLENGE

RC: `RC-05` · Owner: P08 · Frozen surface: `e368d11da6f7e4973469ff5608d676ec2d13811c`
Result: **`RC-FAIL — MATERIAL DEFECT FOUND`**

## Independent balance reproduction — computation itself survives
Four frozen PGDMP inputs were opened read-only with `pg_restore 18.6`.

| DB | Posted moves with lines | Posted lines | COMPUTED/STORED unbalanced at exact / 1e-7 / 1e-4 / 0.005 |
|---|---:|---:|---|
| DB-SM | 169,143 | 417,700 | 0 / 0 / 0 / 0 |
| DB-BK | 16 | 563 | 0 / 0 / 0 / 0 |
| DB-EV | 6 | 15 | 0 / 0 / 0 / 0 |
| DB-T2 | 5 | 14 | 0 / 0 / 0 / 0 |

Controls independently executed:
- 0.01 injection => +1 at all four tolerances;
- 0.001 injection => +1 below 0.005 and 0 at 0.005;
- missing input => fail-closed exit 2;
- missing required column/table => fail-closed exit 3;
- no `pg_restore` => fail-closed exit 2;
- two clean four-DB runs => byte-identical;
- shared three-DB outputs under pg_restore 16.15 vs 18.6 => normalized outputs identical.

## Material findings
### RC05-F1 — three-DB claim remains live after four-DB population correction
`58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` §1 item 1 and §8 still state the balance result over **all three deployed databases** (`169,143 + 16 + 6`). RC-05 preparation establishes and independently reproduces a fourth frozen dump, DB-T2, with 5 posted entries and the same zero result. `e368d11` did not update `58_`.

### RC05-F2 — Q-P08-02 retirement was not applied to the old carrier
`54_P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` says the old `25_` `HO-01…HO-06` family is retired and the live P08 family is producer-qualified `P08-HO-01…P08-HO-14`.

But `25_P08_CORE_RECON_HANDOFF_PACK.md` itself was not edited by the correction commit and still presents bare `HO-01…HO-06` as live “six things that must be reconciled”. This leaves two live-looking P08 namespaces despite the claimed retirement.

### RC05-F3 — pre-execution prediction immutability is not independently provable from Git lineage
The package asserts `EXPECTED_CONTROL_BEHAVIOUR.md` was hashed before first execution at `2026-09-07T11:40:26+0700`. In repository history, the expected-behaviour file, instrument, owner run outputs, manifest, the hash, and that timestamp first appear together in commit `e368d11` at `11:45:05+0700`.

The final contents are internally consistent, but Git alone does **not** establish that the prediction was immutably frozen before the run. This is a control-provenance defect, not a defect in the reproduced balance result.

### RC05-F4 — four-DB propagation scope must be bounded
P08 still carries multiple “three deployed databases” statements. At minimum the balance claim in `58_` must move to the four frozen DBs. `DB-T2` independently shows `om_data_remove` installed, so current “installed in all three” destructive-path carriers require a bounded re-check against the fourth DB rather than silent carry-forward.

## Scope limit
The arithmetic result passes independent reproduction. RC-05 fails because the frozen evidence package has stale population/namespace/provenance carriers. No whole-package reset is justified.