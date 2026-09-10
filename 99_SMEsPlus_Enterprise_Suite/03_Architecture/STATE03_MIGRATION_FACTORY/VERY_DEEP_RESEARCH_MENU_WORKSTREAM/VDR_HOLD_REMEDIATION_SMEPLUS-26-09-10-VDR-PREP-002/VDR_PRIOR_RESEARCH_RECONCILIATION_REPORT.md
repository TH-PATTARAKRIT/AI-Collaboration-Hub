# VDR_PRIOR_RESEARCH_RECONCILIATION_REPORT.md
# Prior Research Reconciliation — result

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. Corpus reconciled

The prior Inventory deep research — 26 files, **5,193 lines**, registers L1 through L12, covering
**29 menus and 41 functions** and closed as *"29 of 29 traced, 0 deferred"* — plus the 14-file
ruling-conformance corpus that followed it.

**Nothing in that work is withdrawn.** What follows measures its **scope** against a derived
population and its **dimensions** against a standard that has since acquired a third mandatory axis.

## 2. Scope result

| | Menus |
|---|---:|
| Prior scope | 29 |
| Derived population | **62** |
| Mapped to a prior menu | 32 |
| `NOT APPLICABLE` — grouping containers | 14 |
| **`MISSING` — action-bearing, never in prior scope** | **16** |
| — **of which live on an observed deployment** | **10** |
| `OUTDATED` — prior menu with no counterpart in the target generation | 1 |

**Ten live functions were never researched**, and they include **batch transfers, wave transfers,
packages and the operational Overview dashboard** — three of which the commissioning prompt's own
Inventory scope list names explicitly, and the fourth of which is the application's default landing
screen.

## 3. Dimension result — measured with positive controls

| Dimension | Occurrences | Positive control | Verdict |
|-----------|------------:|------------------|---------|
| PROCESS | 278 | *trigger* fires 57× | **covered — and covered well** |
| CONFIGURATION | 363 | *configuration* fires 148× | **covered** |
| **OPTIONAL FUNCTION** | **0** | *toggle* fires **0×** | **absent — complete blind spot** |
| RUNTIME REACHABILITY | 21 weak | *installed* fires **0×** | **absent** |
| INPUT | 74 | fires | covered |
| OUTPUT | 232 | fires | covered |

### The premise, corrected
The commissioning prompt states prior research emphasised **input and output** over **process**.

**Measured: the output:input ratio is 3.1 : 1 — the asymmetry is real and larger than stated. But
PROCESS (278) and CONFIGURATION (363) both exceed OUTPUT (232).** The prior corpus is **not**
process-thin: its L3 register alone carries 230 process-signal occurrences across eight declared
dimensions per function.

> **The gaps are optional function and runtime reachability — not process.** A delta programme aimed
> at "process internals" would target the dimension prior research covered best, and would leave the
> two genuine blind spots untouched.

This is offered as a **correction to the premise, with its measurement attached**, not as a
disagreement with the concern behind it — the concern was right that something was missing.

## 4. Classification roll-up

| Status | Count | Meaning |
|--------|------:|---------|
| `COMPLETE` | **0** | no menu satisfies PROCESS + CONFIGURATION + OPTIONAL FUNCTION |
| `PARTIAL` | 32 | prior L1–L12 coverage; optional-function and runtime dimensions absent |
| `MISSING` | 16 | never in prior scope |
| `NOT APPLICABLE` | 14 | containers |
| `OUTDATED` | 1 | the valuation report menu |
| `CONTRADICTED` | **0** | **no prior conclusion is contradicted by current evidence** |
| `UNVERIFIED` | see §5 | the valuation conclusions, in the target generation |

**Zero contradictions is a substantive result.** Two independent research programmes, different
methods, different instruments, one year apart in generation — and no prior conclusion is falsified.
Two are **independently corroborated** (`P-07` and `P-02`/`IV-05`).

## 5. Valuation / COGS — §17 classification, preserved as lineage

| Prior conclusion | Class | Why |
|---|---|---|
| `P-07` Inventory emits facts; Accounting decides postings | **VALID** | corroborated by ownership evidence |
| `P-02` / `IV-05` completed movement facts are immutable | **VALID** | corroborated by the terminal write-off and teardown documents |
| The COGS dependency lock on 19 menus, `JT-01`…`JT-12` | **PARTIAL** | the dependency is unchanged; the object it reasons about is gone |
| The valuation ledger is the per-movement valuation record | **SUPERSEDED** | absent from the target generation in source, schema and data |
| Conclusions derived from per-movement ledger behaviour | **UNVERIFIED in the target generation** | true of series 16; unestablished for series 19 |

**No conclusion is marked CONTRADICTED and none is silently replaced.** Each is preserved with its
original scope and a generation label.

### The evidence that makes this classification safe
Measured across two generations of real deployment data:
**series 16 — 74,982 valuation rows, 98% bound to a stock movement, 77% to an accounting entry.
Series 19 — that table does not exist; its replacement holds 85,832 rows, 0% bound to a movement.**

`BOSS-DEC-01` now has row-level evidence on both sides of the change.

## 6. Status

| Control | Status |
|---------|--------|
| Prior corpus located, declared and read | **COMPLETE** — 26 files, 5,193 lines, cited by branch |
| Every applicable item classified | **COMPLETE** — 62 of 62 |
| Dimension measurement instrument-controlled | **COMPLETE** — three passes, two corrected, positive controls on all six classes |
| Prior conclusions preserved as lineage | **COMPLETE** |
| Required delta identified | **COMPLETE** — 10 live `MISSING` items, researched; 32 `PARTIAL` items, gap sized and left open |
