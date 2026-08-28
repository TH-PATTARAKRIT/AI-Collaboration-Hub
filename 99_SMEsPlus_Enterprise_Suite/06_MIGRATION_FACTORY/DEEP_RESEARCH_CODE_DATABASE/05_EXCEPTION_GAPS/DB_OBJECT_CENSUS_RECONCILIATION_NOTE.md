# Database Object Census — Reconciliation Note

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Reviewer: ChatGPT L99 / Evidence Gate Review  
Status: **PASS WITH CONTROL FOR DIRECT CENSUS / HOLD FOR HISTORICAL COUNT-DEFINITION RECONCILIATION**

## 1. Direct Structural Evidence

DOMAIN_01 corrective evidence executed direct `pg_restore -l` observation against the identified database dump and recorded the following object census:

| Object class | Direct count |
|---|---:|
| FK CONSTRAINT | 5,141 |
| SEQUENCE | 2,871 |
| TABLE | 2,763 |
| CONSTRAINT | 1,860 |
| INDEX | 1,808 |
| TABLE DATA | 1,395 |
| DEFAULT | 888 |
| VIEW | 36 |
| RULE | 9 |
| EXTENSION | 6 |
| TRIGGER | 0 |

The evidence pack also reports four CHECK constraints on the principal accounting-line table.

## 2. Historical Headline Comparison

Historical Phase B evidence reported:

- constraints: 6,682;
- FK: 5,141;
- indexes: 1,714;
- tables: 1,395 in the data/table inventory context.

The direct census does not use an identical taxonomy to those historical headlines.

### 2.1 Index drift

```text
Direct pg_restore census INDEX = 1,808
Historical headline indexes     = 1,714
Difference                      = +94
```

The +94 difference is evidence of a count-definition / extraction-version / artifact-version issue until reconciled. It is not automatically treated as database growth.

### 2.2 Constraint taxonomy

```text
Direct CONSTRAINT       = 1,860
Direct FK CONSTRAINT    = 5,141
Simple sum              = 7,001
Historical constraints  = 6,682
```

The direct categories and historical headline cannot be equated without determining whether the historical figure included/excluded FK, PK, UNIQUE, CHECK, duplicated objects or other filtered categories.

### 2.3 Table terminology

Direct `TABLE = 2,763` and `TABLE DATA = 1,395` are not contradictory by themselves. `TABLE DATA` represents relations with data TOC entries, while the broader TABLE census includes structural relations. Historical `1,395 tables` therefore requires taxonomy confirmation before being compared directly to `TABLE=2,763`.

## 3. Gate Position

| Test | Result |
|---|---|
| Direct pg_restore object census inspectable | PASS WITH CONTROL |
| FK 5,141 independently reproduced | PASS |
| Direct index count inspectable | PASS WITH CONTROL |
| Direct-vs-historical index difference explained | HOLD |
| Historical constraints taxonomy reconciled | HOLD |
| Historical `table=1,395` terminology reconciled with TABLE / TABLE DATA | HOLD |

## 4. Required Closure Evidence

To close the count-definition control, produce one reconciliation register with:

- object class;
- historical extraction rule/query/tool;
- direct pg_restore object class;
- historical count;
- current direct count;
- inclusion/exclusion rule;
- duplicate/filter policy;
- artifact timestamp/version;
- reviewer;
- final disposition (`SAME_SCOPE`, `DIFFERENT_SCOPE`, `VERSION_DELTA`, `EXTRACTION_ERROR`, `UNRESOLVED`).

## 5. Gate Impact

`DR-GAP-007 = REDUCED / STILL OPEN`

Direct structural evidence is stronger than the old fallback evidence, but `No Evidence = No Progress` prevents closure until the count definitions are reconciled.
