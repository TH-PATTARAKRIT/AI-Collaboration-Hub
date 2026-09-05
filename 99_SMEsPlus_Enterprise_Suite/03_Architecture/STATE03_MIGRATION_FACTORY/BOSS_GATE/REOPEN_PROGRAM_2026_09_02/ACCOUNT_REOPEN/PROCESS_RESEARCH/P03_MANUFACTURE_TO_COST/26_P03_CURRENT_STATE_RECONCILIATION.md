# 26 — P03 CURRENT STATE RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

Continuation `SMEPLUS-26-09-05-ACC-P03-M2C-CROSS-PROCESS-EVIDENCE-CLOSURE-001`.
**TARGETED CONTINUATION — NO RESET.** Files `00`–`25` stand as prior evidence.

---

## 1. Baseline carried forward, unchanged

| Round | Commit | Content |
|---|---|---|
| P03#01 | `812cc5c` | Files `00`–`24`. 13 `DC-*`, 6 contradictions, 8 tolerance-zero boundaries, CORR1 scope matrix |
| P03#02 | `259dd2e` | File `25`. P04 intake: `DC-14`, `DC-15`, denominator correction, scope downgrade `REV-S-05` |
| **P03#03** | this round | Files `26`–`47`. Runtime evidence, dispositions, peer reconciliation |

Nothing from `00`–`25` is discarded, reset or re-derived. Where this round changes a
classification it says so and preserves the superseded wording.

## 2. The material delta of this round

**Runtime and database evidence became available for the first time.** Prior rounds were
bounded by `DEP-04` — the installed-module list was unknown, and that bound capped every
negative finding in the package.

**`DEP-04` is now executed.** Four deployed database dumps exist; three are readable. The
executed output is `evidence/P03T_EXECUTED_OUTPUT.txt`, reproducible with
`evidence/P03T_db_rowcounts.py`.

## 3. The single finding that reorganises the package

> **`P03T-F-01`. In the only available deployment where manufacturing has ever executed,
> finished-goods cost is direct materials and nothing else. Conversion cost is zero — not
> merely missing its fixed-overhead component, but missing labour and machine cost
> entirely — because no work centre, no routing operation, no work order and no time log
> exists at all.**
>
> Enumerated, not sampled: 10,764 manufacturing orders (9,807 `done`), 983 bills of
> material, 2,789 component lines, 103,949 stock moves, 74,982 valuation layers —
> against **0** work centres, **0** routing operations, **0** work orders, **0** time
> logs, and `extra_cost` non-zero on **0** of 10,764 rows.
>
> Class: **FACT VERIFIED** for the `iSMEs` database as dumped 2026-07-11.

Applying `03` §3's own formula with the measured inputs:

```
total_cost = -Σ(consumed valuation layers) + work_centre_cost + extra_cost
           = -Σ(consumed valuation layers) + 0                + 0
```

And `_post_labour` reaches `if mo.company_id.currency_id.is_zero(workcenter_cost): continue`
on every order, so **the labour relief entry is never created.**

## 4. What this does to the prior findings — reachability, not correctness

**No prior finding is withdrawn.** Every code defect in `05` remains verified *as code*.
What changes is whether it can fire in the deployments that exist.

| Finding | Code status | Reachability in `iSMEs` | Basis |
|---|---|---|---|
| `DC-01` machine cost on overlapping logs | `FACT VERIFIED` | **UNREACHABLE** | `mrp_workorder` not installed; 0 work orders; 0 time logs |
| `DC-02` two rates on one interval | `FACT VERIFIED` | **UNREACHABLE** | `mrp_workorder_hr_account` not installed |
| `DC-03` `extra_cost` residue | `FACT VERIFIED` | **UNREACHABLE — enumerated** | `extra_cost` non-zero on 0 of 10,764 |
| `DC-04` standard-cost mismatch | `FACT VERIFIED` | **UNREACHABLE** | requires non-zero work-centre cost |
| `DC-05` analytic ≠ GL | `FACT VERIFIED` | **UNREACHABLE** | no work-centre analytic is ever written |
| `DC-06` inert rate snapshot | `FACT VERIFIED` | **UNREACHABLE** | no work orders |
| `DC-07` relief credits COGS | `FACT VERIFIED` | **UNREACHABLE** | relief entry never created |
| `DC-08` expected cost as actual | `FACT VERIFIED` | **UNREACHABLE** | no work orders to force a duration on |
| `DC-09` labour entry dated today | `FACT VERIFIED` | **UNREACHABLE** | entry never created |
| `DC-10` employee analytic inert | `FACT VERIFIED` | **CONFIRMED INERT — the strongest confirmation available** | `project_mrp_workorder_account` not installed in any readable dump |
| `DC-11` wrong-company accounts | `FACT VERIFIED` | **UNREACHABLE** via this path; `iSMEs` has 1 company | `_post_labour` never runs |
| `DC-12` rate-squared in report | `FACT VERIFIED` | **UNREACHABLE** | report has no employee times to read |
| `DC-13` unbuild first-layer cost | `FACT VERIFIED` | **LIVE — the only reachable `DC-*` in the package** | 987 unbuild orders, 4,132 unbuild moves, measured |
| `DC-14` analytic double distribution | `FACT VERIFIED` (mechanism) | **UNREACHABLE** | `project_mrp_account` not installed in any readable dump |
| `DC-15` no idempotence marker | `FACT VERIFIED` (absence) | **second post unreachable** | relief entry never created |
| `CC-07`…`CC-14` fixed overhead | `FACT VERIFIED` | **CONFIRMED, and now stronger** | not only is there no overhead path, there is no work-centre rate either |

**The honest reading.** P03#01 and P03#02 dissected a cost apparatus with real defects.
The runtime evidence shows that apparatus **has never been switched on**. That does not
make the analysis wrong; it makes it a specification of what will go wrong the day a work
centre is configured — which is precisely what a clean-room design study is for.

**It also makes the practical defect far larger than any `DC-*`.** A subtle
double-count in an unused mechanism matters less than 9,807 completed manufacturing
orders valued at material cost alone.

## 5. Scope of the runtime claim — mandatory bound

- **POPULATION:** database dumps ≥1 MB reachable under `/Volumes/iMacSys` and `~/Downloads`.
- **PATTERN:** `find … \( -name "*.dump" -o -name "*.sql.gz" -o -name "*.backup" \) -size +1M`.
- **PATH SET:** those two roots.
- **UNIT:** one database dump file.
- **RESULT:** 4 distinct databases; **3 readable**, 1 refused (`iTEST02`, dump format
  version 1.16 exceeds the local `pg_restore`).

**This is not a claim about "the production system".** It is a claim about the three
readable databases. `iTEST02` is unread and is carried as `UNR-P03-07`. Whether any of
these is the system SMEsPlus must migrate is **not** established here and is not P03's to
decide.

## 6. What `DEP-04` now is

`DEP-04` was: *the running system's installed-module list is unknown, and caps every
negative claim.* It is now **executed for three databases** and is downgraded from a cap
on the whole package to a bounded residual:

> **`DEP-04` — PARTIALLY CLOSED.** Installed-module lists obtained for `BK12MAY26` (251
> modules) and `iSMEs` (190). Not obtained for `iTEST02` (unreadable) or for any system
> not represented by these dumps.

This is reported to the Asset track as evidence toward its priority-1 query `Q-04`.
**P03 does not close `Q-04`** — that register is Asset-owned, and `Q-04` was framed
against the *running* system, which is not the same object as a dump.
