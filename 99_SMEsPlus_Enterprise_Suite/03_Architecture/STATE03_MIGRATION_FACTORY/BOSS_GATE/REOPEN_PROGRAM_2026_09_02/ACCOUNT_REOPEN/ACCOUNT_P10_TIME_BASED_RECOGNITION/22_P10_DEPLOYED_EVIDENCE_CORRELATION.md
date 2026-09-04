# P10 — DEPLOYED EVIDENCE CORRELATION (STAGE E)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
**Added after the rest of the package was written and pushed.** See `14_P10_REVISION_LOG.md` `P10-R-08` for why, and what it corrects.

Stage E of the canonical acquisition flow requires material facts to be correlated across evidence layers. The package originally declared that only one layer was available. **That declaration was wrong.** Deployed database evidence existed on the execution host and was readable. This document is the correlation the package should have contained from the start.

---

## 1. Population and Method

| Element | Declaration |
|---------|-------------|
| POPULATION | Every deployed database archive available on the execution host |
| PATH SET | The host's download directory, enumerated — not assumed |
| PATTERN | Schema extraction from the archive without a running server, then targeted per-table data extraction for the small recognition tables |
| UNIT | One deployed database |
| SCRIPT | `p10_scripts/p10_enum_03_deployed_schema.sh`, shipped and re-runnable |
| CONTROL | **Every zero is printed next to the byte size of the artefact it was counted from**, so an empty extraction cannot be mistaken for an empty table |

Four archives found. **Three readable; one written in an archive format the host's tooling cannot open** — that one is class `C`, NOT SEARCHED, and nothing below applies to it.

## 2. What the Deployed Databases Show

| Fact | Database A | Database B | Database C |
|------|------------|------------|------------|
| Deferral window fields on journal items | present | present | **absent** |
| Deferral relation structure | present | present | **absent** |
| Company-level deferral configuration | all eight settings present | all eight present | **absent** |
| Asset structures | present | present | present |
| Loan structures | present | present | **absent** |
| Periodic transfer structures | **absent** | **absent** | present |
| Chart-of-accounts shape | many-to-many across companies; **no scalar company column at all** | same | **scalar company column, mandatory** |
| Companies in the tenant | 44 | 44 | not examined |
| Companies with deferral accounts or journals provisioned | 43 of 44 | 43 of 44 | n/a |
| Accounts belonging to more than one company | **1** of 544 | **0** of 544 | n/a — structurally impossible |
| Deferral entries ever generated | **0** | **0** | n/a |
| Generation method configured | `on validation` — **all 44 companies** | same | n/a |
| Allocation method configured | 30/360 month basis — **all 44 companies** | same | n/a |
| Companies with asymmetric expense/revenue settings | **0** | **0** | n/a |

## 3. What This Changes

### `P10-F-37` — the deferral function is not present in every deployed database

Database C has no deferral structure of any kind. Any SMEsPlus design, migration plan or reconciliation that assumes the function exists across the estate is wrong for at least one deployed database. Class `A`, scope = that database. This is the same class of finding as the P2P process's discovery that the goods-received-clearing bridge has no physical structure in the deployed databases.

Database C does carry the **periodic transfer** structures that A and B lack. The estate is not on one line of the product; it is on at least two, with **different sets of time-based mechanisms available**.

### The live configuration is the fragile one

All 44 companies in both databases are configured to generate on source-document validation. That is precisely the path that:
- performs **no lock-date check** before generating, so a locked-period recognition entry is silently re-dated (`P10-F-05`);
- has **no catch-up mechanism** (`P10-C-01`, and the correction that scoped it to this path);
- produces a per-document journal shape that the grouped path does not (`P10-F-06`).

**The path the estate actually uses is the one with the weakest period-close and correction behaviour.** The resilient grouped path is used by zero companies. This inverts the practical priority: the grouped-path defects (`P10-F-21`, `P10-S-02`, the cache defect, the duplicate-control defeats) are **latent**, while the validation-path defects are **live**.

### The realised exposure today is nil, and the defects are intact

- Zero deferral entries have ever been generated in either database, so no wrong recognition exists to correct and there is no deferral data to migrate.
- All 44 companies share one identical configuration, so the allocation-policy scope defect (`P10-S-01`) **cannot currently produce a divergence** — every company would supply the same answer. The defect is intact; its realised risk is zero **until the first company changes a setting**.
- The chart of accounts is effectively unshared — one account in one database, zero in the other, belong to more than one company. So the multi-company grouped-generation defect (`P10-S-02`) would, on today's data, most likely **fail loudly** rather than post silently. That is the safer branch of `P10-C-02` — and it remains, as that entry says, an accident of configuration rather than a control. One shared account already exists.

### Two structural facts that are *not* softened

1. Database A and B have **no scalar company column on accounts at all**. The old, strong guarantee that an account belongs to exactly one company is gone at the schema level; what remains is a relation whose current contents happen to be almost one-to-one.
2. All eight per-direction deferral settings are physically present and independently writable in every one of the 44 companies. The asymmetric-configuration risk (`P10-F-17`) is one settings change away in any of them.

## 4. Effect on the Gate

| Criterion | Before | After |
|-----------|--------|-------|
| `EC-01` Scope Bounded | Four surfaces declared unbounded, including database | Database surface **now bounded** for three of four archives; one archive is class `C` |
| `EC-04` Tolerance-Zero Closed | NOT SATISFIED — defects unreproduced | **Still NOT SATISFIED.** The deployed evidence bounds the *realised* exposure to nil today; it does not reproduce or refute the defects, because reproduction requires executing the code, not reading the data |
| `EC-08` Package Complete | "Cross-layer correlation could not be performed at all" | **Corrected.** Stage E performed across source and deployed-database layers; runtime and UI layers remain absent |

`P10-U-01` and `P10-U-02` move from `UNKNOWN` to **partially dispositioned**: the deployment context that decides their severity is now known; the code behaviour still needs an executing reproduction.

## 5. What This Evidence Cannot Do

It is **schema and stored data**, not behaviour. It cannot show what the code does when it runs. Every finding in `01`–`09` that describes a code path remains source-verified and unreproduced. Reading a database is a layer above reading source; it is still a layer below running the system.
