# 03 — ACCOUNT WAVE A — ENUMERATION COVERAGE MATRIX

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room · cites `MCE-0NN`
Canonical matrix required by `SMEPLUS-DR-MC-001` §5.

Columns per the standard. `Owner` is the round that established the row.
Status vocabulary is the standard's and is not extended:
`NOT STARTED` · `IN PROGRESS` · `BOUNDED` · `ENUMERATED` · `REVIEWED` · `CONVERGED` · `HOLD`.

> **Reading rule.** `Enumerated` = members individually identified. `Evidence` = members carrying a
> primary-source citation. A row where `Enumerated` < `Denominator` is **not** a failure; it is an
> honest statement of where the traverse stopped. Percentages appear **only** where the denominator
> is source-derived (`D-SRC`).

---

## 1. Matrix

| ID | Population | Verified denominator | Enumerated | Evidence | Gap | Unknown | Last material delta | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| `P-01` | COA concepts | 26 `D-AUTH` | 26 | 23 | 3 | 3 | GAPCLOSE | Core | `HOLD` |
| `P-02` | Journal concepts | 19 `D-AUTH` | 19 | 19 | 0 | 1 | **MC — `B-18` unreconciled** | Core | `HOLD` |
| `P-03` | Entry concepts | 25 `D-AUTH` | 25 | 24 | 1 | 1 | GAPCLOSE | Core | `HOLD` |
| `P-04` | Item concepts | 18 `D-AUTH` | 18 | 18 | 0 | 1 | GAPCLOSE | Core | `HOLD` |
| `P-05` | Reconciliation concepts | 18 `D-AUTH` | 18 | 18 | 0 | 2 | **MC — `MCE-004`** | Core | `HOLD` |
| `P-06` | Lock-date concepts | 17 `D-AUTH` | 17 | 17 | 0 | 0 | CORR1 | Core | `HOLD` |
| `P-07` | Fiscal-year / close concepts | 15 `D-AUTH` | 15 | 15 | 0 | 1 | **MC — `G-14` unreconciled** | Core | `HOLD` |
| `P-08` | Currency / FX concepts | 17 `D-AUTH` | 17 | 14 | 3 | 3 | **MC — `H-17` unreconciled** | Core | `HOLD` |
| `P-08a` | Rate-table scoping rules | **6** `D-SRC` | 6 (100%) | 6 | 0 | 0 | **MC — +2 rules** | **MC** | `ENUMERATED` |
| `P-09a` | Menu items | **52** `D-SRC` | 52 (100%) | 52 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-09b` | View records | **126** `D-SRC` (46 Wave A) | 126 (100%) | 46 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-10` | Field declarations | **397** `D-SRC` | 397 (100%) | ~90 cited in parent | 307 | 0 | MC | **MC** | `BOUNDED` |
| `P-10a` | Database-wide config keys | **5** `D-SRC` | 5 (100%) | 5 | 0 | **0** | **MC — `AC-06` closed** | **MC** | **`CONVERGED`** |
| `P-11` | Window actions | **59** `D-SRC` | 59 (100%) | 0 | 59 | 0 | MC | **MC** | `ENUMERATED` |
| `P-11a` | Object buttons | **55** `D-SRC` | 55 (100%) | 0 | 55 | 0 | MC | **MC** | `BOUNDED` |
| `P-12` | Declared states | **6** `D-SRC` | 6 (100%) | 6 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-12a` | State transitions | **`UNBOUNDED`** | parent list only | — | not computable | ≥1 | Core | Core | `HOLD` |
| `P-13` | Wave A models | **21** `D-SRC` of 59 | 21 (100%) | 21 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-14` | Wave A source files / lines | **18 / 16,044** `D-SRC` | 18 (100%) | 18 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-14a` | Method definitions | **750** `D-SRC` | 750 (100%) | ~60 cited in parent | 690 | 0 | MC | **MC** | `BOUNDED` |
| `P-15` | Storage-level constraints | **11** `D-SRC` | 11 (100%) | 11 | 0 | 0 | MC | **MC** | `ENUMERATED` |
| `P-15a` | Application constraint hooks | **32** `D-SRC` | 32 (100%) | 6 | 26 | 0 | MC | **MC** | `ENUMERATED` |
| `P-16` | Access-control rows | **132** `D-SRC` (35 Wave A) | 132 (100%) | 4 | 31 | 0 | **MC — `AC-01` re-verified** | **MC** | `ENUMERATED` |
| `P-16a` | Record-scoping rules (addon) | **31 / 20 models** `D-SRC` | 31 (100%) | 31 | 0 | 0 | **MC — `MCE-004`** | **MC** | `ENUMERATED` |
| `P-16b` | Record-scoping rules (framework) | **31** `D-SRC` | 31 (100%) | 2 | 29 | 0 | MC | **MC** | `BOUNDED` |
| `P-17` | Business events | **`UNBOUNDED`** | parent list | — | not computable | ≥1 | Core | Core | `HOLD` |
| `P-18` | Accounting events | **`UNBOUNDED` by construction** | parent list | — | not computable | ≥1 | Core | Core | `HOLD` |
| `P-19` | Dependent reports | **`UNBOUNDED`** | — | — | — | ≥1 | — | — | `HOLD` → Wave G |
| `P-20` | Cross-module ledger producers | **38** `D-SRC` | 38 (100%) | ~7 families in parent `05` | 31 | 0 | **MC** | **MC** | `ENUMERATED` |
| `P-20a` | Scheduled jobs | **2** `D-SRC` | 2 (100%) | 0 | 2 | 0 | MC | **MC** | `ENUMERATED` |
| `P-21a` | Company-scoping overrides | **11** `D-SRC` | 11 (100%) | 11 | 0 | 0 | **MC — `AC-03` mechanism** | **MC** | `ENUMERATED` |
| `P-21b` | Privilege-elevation sites | **93** `D-SRC` | 93 (100%) | 3 | **90** | **90** | **MC** | **MC** | `BOUNDED` |
| `P-21c` | Root-vs-company divergence | **37** `D-SRC` | 37 (100%) | 4 | **33** | **33** | **MC** | **MC** | `BOUNDED` |
| `P-21d` | Raw-SQL scoping-bypass sites | **62** `D-SRC` | 62 (100%) | 2 | **60** | **60** | **MC** | **MC** | `BOUNDED` |
| `P-21e` | Named control-bypass tokens | **8** `D-SRC` | 8 (100%) | 5 | 3 | 3 | **MC** | **MC** | `ENUMERATED` |
| `P-22` | Migration paths | **`UNBOUNDED`** | parent `17` | — | — | ≥1 | Core | Core | `HOLD` |
| `P-23` | Failure / exception paths | **153** `D-SRC` | 153 (100%) | ~25 in parent `19` | **128** | 0 | **MC** | **MC** | `ENUMERATED` |
| `P-24` | Negative claims | **577 hits / 64 files** `D-SRC` | 200 hits triaged (41.9% of package by line) | 17 rescoped | **377 hits untriaged** | ≥17 | **MC — `MCE-011`** | **MC** | `HOLD` |
| `P-25` | Unknowns | 41 `D-AUTH` | see file `06` | — | — | 41 | GAPCLOSE | GAPCLOSE | `HOLD` |
| `P-26` | Contradictions | 16 `D-AUTH` | 16 | 16 | 0 | 0 | GAPCLOSE | GAPCLOSE | `HOLD` |
| `P-27` | Balanced-but-wrong | 27 `D-AUTH`, a floor | see file `08` | 27 | floor | ≥1 | GAPCLOSE | GAPCLOSE | `HOLD` |

---

## 2. The three numbers that matter

**1. Populations with a source-derived denominator: 0 before this round, 24 after.**
Three rounds of deep research, nine independent reviewers, and one gate report were produced without
a single verified denominator over the system being researched. `P-01`…`P-08` are a description of
the research, not a measure of the system.

**2. Four `BOUNDED` mechanism rows carry 243 unassessed members.**
`P-21b` 93 privilege-elevation sites · `P-21c` 37 root-vs-company sites · `P-21d` 62 raw-SQL sites ·
`P-23` 153 failure paths, of which ~128 uncited. Every verified cross-boundary defect found in three
rounds — `SB-05`, `FX-07`, `FX-08`, `B-05`, `X-04`, `X-05`, `X-06` — is a member of one of these
four populations. They are now **bounded and counted**, which is new; they are **not traversed**,
which is `GB-04`'s residue stated as a number instead of as a worry.

> `GB-04` previously read: *"the full extent of cross-boundary exposure is not characterised."*
> It can now be stated exactly: **the exposure surface is 192 sites in three populations
> (`P-21b`, `P-21c`, `P-21d`), of which 9 have been assessed.**

**3. One population converged.**
`P-10a`, database-wide configuration keys, is closed at **5 members, 2 material** (`MCE-006`). It was
`AC-06`'s open-ended class — *"`SB-01` is a class, not an instance"*. A class with an unstated size
became a bounded set of five by one command. This is the shape every remaining row needs.

## 3. Coverage statements this round is entitled to make

- Wave A source surface is **18 files, 16,044 lines, 21 models, 397 fields, 750 methods** — verified.
- Wave A control surface is **11 storage constraints, 32 application hooks, 31 record-scoping rules
  over 20 models, 132 access rows, 153 failure paths** — verified.
- Reconciliation models `account.full.reconcile` and `account.partial.reconcile` hold **zero**
  record-scoping rules anywhere in a 797-module tree while holding full write rights for ordinary
  accounting roles — verified absence within a fully enumerated bounded scope (`MCE-004`).
- Company-scoping rules over the rate table number **six**, not four (`MCE-007`).

## 4. Coverage statements this round is NOT entitled to make

- **No overall Wave A coverage percentage.** The `D-SRC` populations are bounded but only partly
  traversed; the `D-AUTH` populations have no verifiable denominator. Any single headline percentage
  would be `D-AUTH` arithmetic wearing a `D-SRC` costume — which is exactly what `67.1%` was.
- **No claim that the finding set is complete.** `P-21b`/`P-21c`/`P-21d` are 192 sites with 9
  assessed. The honest statement is that the *space* is now measured, not that it is cleared.
- **No claim of negative-claim compliance for the package.** It holds for 41.9% of it (`MCE-011`).
