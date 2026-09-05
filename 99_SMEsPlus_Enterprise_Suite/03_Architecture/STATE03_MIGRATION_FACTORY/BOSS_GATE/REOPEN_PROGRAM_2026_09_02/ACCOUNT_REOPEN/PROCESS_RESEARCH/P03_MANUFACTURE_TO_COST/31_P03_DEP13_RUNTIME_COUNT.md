# 31 — P03 DEP-13 RUNTIME COUNT

**LAYER 2 — AUDIT QUARANTINE.** READ-ONLY. No database server was started; no write of
any kind was performed.

---

## 1. What was asked

`DEP-13` / P04 `P04-B-35`: close the work-centre scope defect with **one runtime count of
work centres with no company**.

## 2. Declared enumeration

| Element | Declaration |
|---|---|
| **POPULATION** | Every row of the work-centre table in every readable deployed database dump |
| **PATTERN** | `pg_restore --data-only -t mrp_workcenter <dump>`, parse the `COPY` block, test `company_id` against the null marker `\N` |
| **PATH SET** | Dumps ≥1 MB under `/Volumes/iMacSys` and `~/Downloads` |
| **UNIT** | One work-centre row |
| **METHOD** | Read-only stream to stdout. Reproducible: `evidence/P03T_db_rowcounts.py` |

## 3. Executed result

| Database | Work-centre rows | With no company | With a company |
|---|---|---|---|
| `iSMEs` | **0** | 0 | 0 |
| `BK12MAY26` | **0** | 0 | 0 |
| `iEVING` | **0** | 0 | 0 |
| `iTEST02` | **UNREADABLE** — `pg_restore: unsupported version (1.16) in file header` | — | — |
| **TOTAL** | **0** | **0** | **0** |

## 4. Verification of the zero — three forms and a positive control

A zero result is not accepted on one query — `smeplus-independent-review-ratio-p05`.

1. **Form 1** — parser over the `COPY` block: 0 rows.
2. **Form 2** — direct inspection of the emitted SQL: the `COPY public.mrp_workcenter (…)
   FROM stdin;` statement is immediately followed by the `\.` terminator on the next line.
3. **Form 3** — a corrected parser re-run across eight tables at once: 0 for
   `mrp_workcenter`.
4. **Positive control** — the *same* parser on the *same* dumps returns `account_asset` 36,
   `res_company` 44, `iSMEs account_asset` 685, `account_analytic_account` 27. The parser
   finds data when data exists.

An earlier `awk` counter returned a uniform `9` for every table. It was **wrong** and was
discarded rather than reported; the discrepancy is what prompted forms 2 and 3. Recorded
because a count that was nearly published is worth recording — `22` §6, `RE-P03-13`.

## 5. Disposition — the count is executed and **vacuous**

> **`DEP-13` — EXECUTED. RESULT: 0 of 0.**
>
> The query P04 specified is runnable and was run. It returns an **empty population**, so
> it yields **no evidence either way** about whether work centres are configured without a
> company.

**`P04-B-35` is NOT closed.** The closing evidence P04 named is necessary but not
sufficient: it presumes a deployment in which work centres exist. None of the three
readable deployments has a single one.

## 6. What would actually close it

| Requirement | Status |
|---|---|
| A deployment with ≥1 work-centre row | **None found** in the declared PATH SET |
| `iTEST02` made readable — needs `pg_restore` ≥ the version that wrote dump format 1.16 | **`UNR-P03-07`** — a tooling gap, not an evidence gap. Cheap to close |
| Live read against a running system | **HOLD — RUNTIME EVIDENCE REQUIRED**; no such access in this session |

**The cheapest next step is upgrading the local PostgreSQL client tools**, which converts
`UNR-P03-07` into a fourth data point. P03 records it and does not perform it: it is an
environment change, and §12 of the directive confines this session to read-only evidence.

## 7. A second finding, produced by the same count

The zero is not only a failed closure. It is itself evidence:

> **`P03T-F-03`. Across three readable deployments — including one with 9,807 completed
> manufacturing orders — not one work centre, routing operation, work order or time log
> exists.** The work-centre cost object on which the entire conversion-cost apparatus
> depends has never been created. `FACT VERIFIED`, scope §2.

That finding is developed in `26` §3 and `40`.
