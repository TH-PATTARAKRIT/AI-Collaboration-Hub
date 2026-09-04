# 02 — ACCOUNT WAVE A — ENUMERATION UNIVERSE REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room · cites `MCE-0NN`
Standard `SMEPLUS-DR-MC-001` §4

---

## 1. Rule of construction

A population enters this register only if it can be **named**, **located in a declared search path**,
and **counted by a single-pass mechanical command**. Where that is impossible the population is
recorded `UNBOUNDED / NOT YET ENUMERABLE` and **no percentage is stated for it**.

Two denominator kinds are distinguished throughout:

- **`D-SRC` — source-derived.** Produced mechanically from the primary source surface. Falsifiable
  by re-running one command.
- **`D-AUTH` — author-derived.** A list a researcher wrote down. It can be complete only by luck; it
  cannot be *shown* complete, because nothing outside it is visible to it.

**The parent package had exactly one enumerated population, and it was `D-AUTH`.** That single fact
is the root of `GB-04` (file `04`).

---

## 2. The universe

`P-01` … `P-27` follow the populations required by the round instruction. `Kind` is `D-SRC` or
`D-AUTH`. `Denominator` is verified unless marked otherwise.

### Group I — Wave A domain concepts (the parent taxonomy)

| ID | Population | Kind | Denominator | Evidence | Status |
|---|---|---|---|---|---|
| `P-01` | Chart-of-account concepts | `D-AUTH` | 26 rows | `MCE-010` | `HOLD` — see §3 |
| `P-02` | Journal concepts | `D-AUTH` | 19 rows | `MCE-010` | `HOLD` |
| `P-03` | Journal-entry concepts | `D-AUTH` | 25 rows | `MCE-010` | `HOLD` |
| `P-04` | Journal-item concepts | `D-AUTH` | 18 rows | `MCE-010` | `HOLD` |
| `P-05` | Reconciliation concepts | `D-AUTH` | 18 rows | `MCE-010` | `HOLD` |
| `P-06` | Lock-date concepts | `D-AUTH` | 17 rows | `MCE-010` | `HOLD` |
| `P-07` | Fiscal-year / close concepts | `D-AUTH` | 15 rows | `MCE-010` | `HOLD` |
| `P-08` | Currency / FX concepts | `D-AUTH` | 17 rows | `MCE-010` | `HOLD` |

`P-01`…`P-08` sum to the parent's **155**. They are retained because they carry the semantic work of
three rounds. They are **not** evidence of coverage of the system: they are a description of what the
research chose to describe. Status `HOLD` for all eight, for two reasons —
the denominator is `D-AUTH`, and the register's own arithmetic does not reconcile (`MCE-010`).

### Group II — Source structure (newly enumerated this round)

| ID | Population | Kind | Verified denominator | Evidence | Status |
|---|---|---|---|---|---|
| `P-13` | Wave A models / entities | `D-SRC` | **21** of 59 declared in the addon | `MCE-001` | `ENUMERATED` |
| `P-14` | Wave A source files | `D-SRC` | **18** files / **16,044** lines | `MCE-001` | `ENUMERATED` |
| `P-14a` | Wave A method definitions | `D-SRC` | **750** | `MCE-001` | `BOUNDED` — counted, not individually assessed |
| `P-10` | Wave A field declarations | `D-SRC` | **397** | `MCE-001` | `BOUNDED` |
| `P-09a` | Menu items (addon) | `D-SRC` | **52** | `MCE-002` | `ENUMERATED` |
| `P-09b` | View records (addon) | `D-SRC` | **126**, of which **46** name a Wave A model | `MCE-002`, `MCE-003` | `ENUMERATED` |
| `P-11` | Window actions | `D-SRC` | **59** | `MCE-002` | `ENUMERATED` |
| `P-11a` | Object buttons in views | `D-SRC` | **55** | `MCE-002` | `BOUNDED` |
| `P-12` | Declared states | `D-SRC` | **3** entry states · **3** lock-exception states | `MCE-002` | `ENUMERATED` |
| `P-12a` | State **transitions** | `D-AUTH` | parent register `10` | — | **`UNBOUNDED / NOT YET ENUMERABLE`** — no transition table is derivable mechanically from the source; the parent list is author-derived and unverified against the 750 methods |
| `P-15` | Storage-level constraints | `D-SRC` | **11** tuples in **6** blocks | `MCE-002` | `ENUMERATED` |
| `P-15a` | Application-level constraint hooks | `D-SRC` | **32** | `MCE-002` | `ENUMERATED` |
| `P-16` | Access-control rows (addon) | `D-SRC` | **132**, of which **35** target Wave A models | `MCE-002` | `ENUMERATED` |
| `P-16a` | Record-scoping rules (addon) | `D-SRC` | **31** records over **20** distinct models | `MCE-004` | `ENUMERATED` |
| `P-16b` | Record-scoping rules (framework) | `D-SRC` | **31** | `MCE-002` | `BOUNDED` |
| `P-23` | Explicit failure/exception paths | `D-SRC` | **153** raise sites | `MCE-002` | `ENUMERATED` |

### Group III — Mechanism populations (the ones the findings came from)

| ID | Population | Kind | Verified denominator | Evidence | Status |
|---|---|---|---|---|---|
| `P-21a` | Company-scoping domain overrides | `D-SRC` | **11**, all parent-inclusive variants | `MCE-005` | `ENUMERATED` |
| `P-21b` | Privilege-elevation sites (addon models) | `D-SRC` | **93** | `MCE-005` | `BOUNDED` — counted; **not individually assessed** |
| `P-21c` | Root-vs-company divergence sites | `D-SRC` | **37** across **11** files | `MCE-005` | `BOUNDED` — **not individually assessed** |
| `P-21d` | Raw-SQL sites bypassing record scoping | `D-SRC` | **62** | `MCE-005` | `BOUNDED` — **not individually assessed** |
| `P-21e` | Named control-bypass tokens | `D-SRC` | **8** sites over 4 distinct tokens (+48 generic skip flags) | `MCE-005` | `ENUMERATED` |
| `P-10a` | Database-wide configuration keys | `D-SRC` | **5**, of which **2** material | `MCE-006` | **`CONVERGED`** — closes `AC-06`/`SB-01` |
| `P-08a` | Company-scoping rules over the rate table | `D-SRC` | **6** (parent recorded 4) | `MCE-007` | **`ENUMERATED`** — closes residual `FX08-R2` |
| `P-20` | Cross-module producers of ledger entries | `D-SRC` | **38** modules outside the accounting addon | `MCE-015` | `ENUMERATED` — parent map `05` names ~7 families |
| `P-20a` | Scheduled jobs in the accounting addon | `D-SRC` | **2** | `MCE-015` | `ENUMERATED` |

### Group IV — Semantic and governance populations

| ID | Population | Kind | Denominator | Evidence | Status |
|---|---|---|---|---|---|
| `P-17` | Business events | `D-AUTH` | parent register `07` | — | **`UNBOUNDED / NOT YET ENUMERABLE`** |
| `P-18` | Accounting events | `D-AUTH` | parent registers `07`, `08` | — | **`UNBOUNDED / NOT YET ENUMERABLE`** — the parent established that no event object exists in the reference system, so no `D-SRC` denominator is available *by construction*; this is a genuine unbounded remainder, not an omission |
| `P-19` | Reports depending on Wave A facts | `D-AUTH` | not established | — | **`UNBOUNDED`** — routed to Wave G |
| `P-21` | Tenant / company boundaries | mixed | see `P-21a`…`P-21e` | `MCE-004`, `MCE-005`, `MCE-007` | `HOLD` — the mechanism populations are bounded; the **boundary model itself** is a Boss decision (`TI-07`) |
| `P-22` | Migration / historical continuity paths | `D-AUTH` | parent register `17` | — | **`UNBOUNDED / NOT YET ENUMERABLE`** |
| `P-24` | Negative claims in the package | `D-SRC` | **577** raw token hits over **64** files / **14,575** lines | `MCE-011` | `HOLD` — only **41.9%** of the package by volume has been triaged |
| `P-25` | Unknowns | `D-AUTH` | parent states **41** | file `06` | `HOLD` |
| `P-26` | Contradictions | `D-AUTH` | parent states **16** | file `10` | `HOLD` pending independent verification |
| `P-27` | Balanced-but-wrong scenarios | `D-AUTH` | parent states **27**, explicitly a floor | file `08` | `HOLD` — taxonomy first |

---

## 3. Why every Group I population is `HOLD`

The 155-row taxonomy is not wrong; it is **not a denominator**. Three properties are missing:

1. **It is not falsifiable.** Nothing in the source can tell you a row is missing, because the list
   was not derived from the source.
2. **It has no cell for a mechanism.** "Multi-company isolation" is a row; *"a database-wide search
   under elevated privilege that rewrites a posted counterparty and passes an explicit lock bypass"*
   is not a value that row can hold. Every material finding of rounds 2 and 3 is of the second kind
   (`MCE-013`).
3. **Its own arithmetic does not reconcile.** Row cells give 108 `SC`; the summary gives 104
   (`MCE-010`). The published `67.1%` cannot be reproduced from the register that published it,
   and the four unreconciled rows are precisely those whose affirmative claims later rounds
   contradicted.

## 4. What is genuinely unbounded, and why that is acceptable

Four populations are `UNBOUNDED / NOT YET ENUMERABLE` and **no percentage is claimed** for any of
them: `P-12a` state transitions · `P-17`/`P-18` business and accounting events · `P-19` reports ·
`P-22` migration paths.

`P-18` deserves the record: the parent research established, positively, that the reference system
has **no accounting-event object**. A population that does not exist as a structure in the source
cannot acquire a source-derived denominator. Its unboundedness is a **finding about the reference
system**, not a gap in this round's method. `P-19` and `P-22` are unbounded because their content
belongs to Wave G and to the migration programme respectively; both are routed, not hidden
(file `06`).

`P-12a` is the one unbounded population that is a genuine **method** gap: transitions are derivable
in principle by tracing the 750 methods for writes to the three declared states, and that trace has
not been done. Enumeration rule `ER-12` (file `05`) specifies it. It is recorded as a named
enumeration defect, not as coverage.

## 5. Summary of the universe

| | Populations | Note |
|---|---|---|
| `D-SRC`, denominator verified this round | **24** | Group II and III |
| `D-AUTH`, retained from the parent | **14** | Group I and IV |
| `UNBOUNDED / NOT YET ENUMERABLE`, declared | **5** | `P-12a`, `P-17`, `P-18`, `P-19`, `P-22` |
| Populations reaching `CONVERGED` | **1** | `P-10a` |
| Populations enumerated for the first time in three rounds | **24** | every `D-SRC` row |
