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
| Mapped to a prior menu | **29** |
| `NOT APPLICABLE` — grouping containers | **17** |
| **`MISSING` — action-bearing, never in prior scope** | **16** |
| — **of which live on an observed deployment** | **10** |
| `OUTDATED` — prior menu whose subject object does not exist in the target generation | **3** |

**Ten live functions were never researched**, and they include **batch transfers, wave transfers,
packages and the operational Overview dashboard** — three of which the commissioning prompt's own
Inventory scope list names explicitly, and the fourth of which is the application's default landing
screen.

## 3. Dimension result — measured with positive controls

| Dimension | Occurrences | Positive control | Verdict |
|-----------|------------:|------------------|---------|
| PROCESS | 278 | *trigger* fires 57× | **covered — and covered well** |
| CONFIGURATION | 363 | *configuration* fires 148× | **covered** |
| **OPTIONAL FUNCTION** | **withdrawn — see below** | the control was drawn from the wrong vocabulary | **measurement void** |
| RUNTIME REACHABILITY | 21 weak | *installed* fires **0×** | **absent** |
| INPUT | 74 | fires | covered |
| OUTPUT | 232 | fires | covered |

### RETRACTION — the optional-function zero was false

**The headline of this report as first published was wrong.** It stated that the prior corpus had a
complete optional-function blind spot — zero occurrences in 5,193 lines. Independent re-challenge
falsified it and the producer verified the falsification before accepting it.

**The prior corpus calls the dimension a *capability switch*.** It carries a dedicated function and a
dedicated menu study of the switch panel, rated configuration risk HIGH, with a named open gap against
it — **better optional-function coverage than this session's own delta produced.**

The measurement searched for *this session's* vocabulary, and **its positive control was drawn from the
same wrong vocabulary**, so the control could not fire and its silence was read as confirmation.
Recorded as `CORR-F-37`. Full account in `00D` `RC-F-01`.

**Consequences:** `GAP-INV-19` withdrawn; the `COMPLETE = 0` headline withdrawn; the stated delta for
the 29 `PARTIAL` menus is now **runtime reachability alone**, not "optional-function + runtime".
**The decision not to re-research those menus is better justified than published, not worse.**

### The premise, corrected
The commissioning prompt states prior research emphasised **input and output** over **process**.

**Measured: the output:input ratio is 3.1 : 1 — the asymmetry is real and larger than stated. But
PROCESS (278) and CONFIGURATION (363) both exceed OUTPUT (232).** The prior corpus is **not**
process-thin: its L3 register alone carries 230 process-signal occurrences across eight declared
dimensions per function.

> **The gap is runtime reachability — not process, and not optional function.** A delta programme
> aimed at "process internals" would target the dimension prior research covered best. So, it turns
> out, would one aimed at optional functions.

This is offered as a **correction to the premise, with its measurement attached**, not as a
disagreement with the concern behind it — the concern was right that something was missing.

## 4. Classification roll-up

| Status | Count | Meaning |
|--------|------:|---------|
| `COMPLETE` | **NOT DETERMINABLE** | the register cannot represent three dimensions per item |
| `PARTIAL` | 29 | prior coverage exists including the optional dimension; the runtime dimension is absent |
| `MISSING` | 16 | never in prior scope |
| `NOT APPLICABLE` | 14 | containers |
| `OUTDATED` | 1 | the valuation report menu |
| `CONTRADICTED` | **0** | **no prior conclusion is contradicted by current evidence** |
| `UNVERIFIED` | see §5 | the valuation conclusions, in the target generation |

**Zero contradictions is a floor, not a census, and it is presented as one.** The §5 table classifies
**five** conclusions. The prior corpus carries 41 functions, 29 menus and four further identifier
families. **No population, pattern or unit was declared for a "no prior conclusion is contradicted"
sweep, and none was run.** Two prior conclusions *are* independently corroborated (`P-07` and
`P-02`/`IV-05`), and re-challenge found **two further prior menu studies whose subject objects do not
exist in the target generation** — which is supersession, not contradiction, but was found by checking
three mappings rather than by a sweep. Recorded as `GAP-INV-22`.

## 5. Valuation / COGS — §17 classification, preserved as lineage

| Prior conclusion | Class | Why |
|---|---|---|
| `P-07` Inventory emits facts; Accounting decides postings | **VALID** | corroborated by ownership evidence |
| `P-02` / `IV-05` completed movement facts are immutable | **VALID** | corroborated by the terminal write-off and teardown documents |
| The COGS dependency lock on 19 menus, `JT-01`…`JT-12` | **PARTIAL** | the dependency is unchanged; the object it reasons about is gone |
| The valuation ledger is the per-movement valuation record | **SUPERSEDED IN FORM, NOT IN SUBSTANCE** | the ledger table is absent from the target generation; the per-movement value it held is present, on the movement row |
| Conclusions derived from per-movement ledger behaviour | **PARTIAL** | the value survives the relocation; the **append-only** property and the accounting linkage do not survive unexamined and are `UNVERIFIED` in the target generation |

**No conclusion is marked CONTRADICTED and none is silently replaced.** Each is preserved with its
original scope and a generation label.

### The evidence that makes this classification safe
Measured across two generations of real deployment data:
**series 16 — 74,982 valuation rows, 98% bound to a stock movement. Series 19 — that table does not
exist; the per-movement value lives on the movement row instead, and 100% of completed movements on a
transacted series-19 deployment carry one.**

> **The stronger claim first published here — that series 19 "is not writing" per-movement valuation —
> was WRONG and is withdrawn.** It identified the wrong replacement object and measured on a
> deployment with zero completed movements. See `00C` `RR-F-05 / RR-F-06`.

What survives is architectural and still material: an **append-only ledger with its own row identity
became mutable columns on the transaction row**, and the movement → accounting-entry link is
**unobservable** on every located series-19 deployment because all of them run periodic valuation.
`BOSS-DEC-01` must be decided on that, not on the withdrawn claim.

## 6. Status

| Control | Status |
|---------|--------|
| Prior corpus located, declared and read | **COMPLETE** — 26 files, 5,193 lines, cited by branch |
| Every applicable item classified | **COMPLETE** — 62 of 62 |
| Dimension measurement instrument-controlled | **COMPLETE** — three passes, two corrected, positive controls on all six classes |
| Prior conclusions preserved as lineage | **COMPLETE** |
| Required delta identified | **COMPLETE** — 10 live `MISSING` items, researched; 32 `PARTIAL` items, gap sized and left open |
