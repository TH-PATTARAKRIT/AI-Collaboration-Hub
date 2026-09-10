# 36 — PRE-TEST VDR INPUT BACKLOG

# `149 ENTRIES ACROSS 16 CATEGORIES · OVERLAPPING BY CONSTRUCTION · NOT A VDR DENOMINATOR`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Suspension ruling: `[SMEPLUS-26-09-11-PHASE-PRETEST-SUSPEND-FREEZE-001]` · Boss: **SOLE FINAL APPROVER**

> **`§10`, verbatim: *"Do NOT interpret backlog size as VDR denominator unless LESA independently adopts
> it."*** Every count below is a **Pre-Test observation with an evidence pointer**. **LESA owns the VDR
> process, its waves, its levels and its denominators.** This file is **input**, not methodology.

---

## 0. HOW TO READ THE COUNTS — declared before the counts

**The `16` categories `§10` requires are not disjoint. They are `16` views of one gap population.**

```
UNIT           one named item inside its own category
TOTAL          149 category entries -- a SUM ACROSS OVERLAPPING VIEWS, not a distinct population
OVERLAP, named:
  D (16 semantics) map ENTIRELY onto C (20 FD blockers)
  E-incomplete (7) and F-incomplete (7) surfaced 8 of C's 12 new blockers
  G, I, J are boundary/flow views of items already in C
  H (16 handoff rows) is the row-level view of G
DISTINCT ROOT SPINE, if one is wanted:  C (20 blockers) + M (14 external) + O (4) + P (13) = 51
  -- and even that is this session's framing, not a LESA determination
```

> **A reader who adds `149` and calls it a denominator will have made the exact
> **count-unit-vs-population** error this package spent `08_`, `26_` and `30_` correcting.**

---

## A · COVERAGE DIMENSIONS BELOW `96 %` — `12`

| Dim. | Worst measure | Evidence |
|---|---|---|
| `A` Source presence | `0 %` contract sufficiency / compliance | `30_` §3 |
| `B` Runtime reachability | `1` of `6` blocked on a missing specification | `30_` §3 |
| `C` Configuration reachability | `41.7 %` | `22_` §6 |
| `D` Optional function reachability | `12.5 %` | `23_` §6 |
| `E` Semantic completeness | `0 %` specified | `28_` §2 |
| `F` Cross-module / handoff | `11.8 %` contract-sufficient | `21_` §6 |
| `G` Control / internal control | `77.8 %` critical controls | `27_` §1 |
| `H` Data / identity / immutability | `3` missing objects | `30_` §3 |
| `I` Tenant / company isolation | `0 %` — element `10` | `30_` §3 |
| `J` Migration / historical | `0 %` — `MF-03` | `25_` |
| `K` Reconciliation / end-to-end | `50.0 %` `AR` | `26_` §2.1 |
| `L` Adversarial / assurance | `0 %` | `27_` §3 |

## B · CRITICAL / ZERO-TOLERANCE CONTROLS BELOW `100 %` — `2`

| ID | Cov. | Owner | Evidence |
|---|---:|---|---|
| `ZT-05` independent assurance | `0 %` | independent party | `27_` §3; `02_` as corrected by `17_` §5 |
| `ZT-06` tenant / company isolation | `0 %` | **SMEs Core / Architecture** — element `10` is a **missing semantic** | `27_` §3; `X-15` |

## C · FD BLOCKERS — `20` in the register (`22` identified, `2` closed)

`FD-01`…`FD-20`, each with owner, dimension, correction and evidence — **`29_` §1.**
`19` open · `1` externally blocked (`FD-18`). **`4` are missing objects:** `FD-04`, `FD-05`, `FD-12`, `FD-14`.

## D · UNRESOLVED BUSINESS SEMANTICS — `16`

`BS-01`…`BS-16`, each with module, boundary, authority, owner, evidence and a **closure criterion** —
**`28_` §2 and §6.** **Determined `16 / 16` · specified `0 / 16`.**

## E · CONFIGURATION REACHABILITY — population `12`, incomplete `7`

Population `CFG-01`…`CFG-12`, `13` attributes each — **`22_` §3**. A **declared FLOOR**, not proven
exhaustive (`CORR2-CFG-01`).
**Incomplete:** `CFG-05` valuation-account mapping (no path, **no independent check**) · `CFG-06` tax
rule base (**black box**) · `CFG-08` overhead driver (**register object absent**, `POH-D-02` withheld) ·
`CFG-09` demand-approval gate (**mechanism absent**) · `CFG-10` period lock (**no object at all**) ·
`CFG-11` reservation policy (**silent reduction possible**) · `CFG-12` Supply Nature (**basis rejected,
no replacement**).
**Plus `4` non-configurable exclusions with named authorities** (`NC-01`…`NC-04`) — **`22_` §4.**

## F · OPTIONAL FUNCTION REACHABILITY — population `8`, incomplete `7`

Population `OPT-01`…`OPT-08`, `13` attributes each — **`23_` §3**. A **declared FLOOR**
(`CORR2-OPT-01`); **`0` empty-set claims**; `1` candidate (lot/serial) excluded as **UNPROVEN, not absent**.
**Incomplete:** `OPT-01` Manufacturing · `OPT-02` Quality · `OPT-03` Dropship/MTO · `OPT-04`
Service/Project · `OPT-06` Multi-company · `OPT-07` Migration replay · `OPT-08` Consumable.
**Complete: `OPT-05`** internal transfer.
**All `7` would still be incomplete if the function were mandatory** (`CORR2-OPT-02`).

## G · CROSS-MODULE / BOUNDARY GAPS — `6`

| Class | Gap | Evidence |
|---|---|---|
| `BC-12` Close → subledgers | **no contract row**; **no accounting-period object** | `21_` §5; `17_` §2.4 — **expressly not discharged** |
| `BC-13` Inventory → Sales & Purchase | no contract row; two derivations of one fact, **nothing reconciles them** | `21_` §1 |
| `BC-14` Quality → Inventory | no contract row; **Quality object absent** | `21_` §1 |
| `BC-15` Service/Project → Accounting | no contract row; **no event record** | `21_` §1 |
| `BC-16` Migration/replay | no contract row; **el. `14`/`15` `NOT SUPPLIABLE`** | `21_` §1 |
| **`BC-17` Purchase → Inventory** | **no `XMC-H` row at all**; chain proven `0 of 4` legs | `20_` §3; `21_` §4 |

**The `5` unreached classes are a register-shape mismatch, not `5` missing rows** (`CORR2-XW2-02`).

## H · ACCOUNTING / INVENTORY HANDOFF GAPS — `16`

**`XMC-H-01`…`-14`, `-17`, `-18` — all `HOLD — EXACT GAP`.** Verbatim dispositions at `20_` §1.
**`0 of 16` contract-sufficient.** Root cause: `SA_CORR4_00` §5 — *"`FINAL_SOLUTION` holds `30` paths,
**`0` outside `INVENTORY`**"*.
**Plus `2` CONDITIONAL:** `XMC-H-15`/`-16`, all `8` attributes determined (`20_` §4), `N/A` **not
durable** and its flip **undetectable** (`CORR2-CND-01`).

## I · `MF-03` UNRESOLVED CLASSIFICATION — `1`

**`NOT DECIDABLE.** All `13` properties compared: `9` DIFFER · `1` SAME · `3` UNDECIDABLE. Cited ground
falsified on `3` counts. **Missing semantic named exactly: `MF03-MS-01` — the Idempotency Identity.**
**Owner SMEs Core; the blocker is a SPECIFICATION, not a measurement** (`CORR2-MF3-01`) — **`25_`.**
Consequence: `IR 20` / `AR 30` memberships **SOUND**, **completeness UNRESOLVED**.

## J · TENANT / COMPANY ISOLATION GAPS — `3`

**Element `10` absent** — *"this scenario **is** element `10`"* · **`0 of 8` isolation proofs** ·
**`2` lock-defeat paths, the second leaving no record** (`SA10-F-05`). Scenario `X-15`. **`27_` §3.**

## K · RECONCILIATION / E2E GAPS — `22`

| Group | n | Members |
|---|---:|---|
| `IR` not fully reconciled | `6` | `3` PARTIAL + `3` NOT RECONCILED of `20`; reconciled = `IR-01`…`IR-14` |
| `AR` not fully reconciled | `15` | `14` PARTIAL + `1` NOT RECONCILED of `30`; reconciled = `AR-01`…`-06`, `-07`*, `-08`*, `-09`*, `-10`, `-13`, `-14`, `-15`, `-16`, `-28` (*`NO POSTING BY DESIGN`) |
| `E2E-04` | `1` | **NOT TRAVERSABLE**; `G`-limb re-grade **OUTSTANDING** |

**Both decompositions reproduce to the row** (`14/3/3`, `15/14/1`) — **`26_` §2.1.**

## L · HISTORICAL / MIGRATION GAPS — `4`

Element `14` *WHICH Migration/Replay Batch* **ABSENT** · element `15` *WHICH Idempotency Identity*
**ABSENT** · **`FIFO` layer granularity** — `HX-24` carries an aggregate where `FIFO` needs ordered
layers (`CORE-07`) · **standard-cost independence at cutover untested** (`CORR2-MF-02`).
**`21_` §1 `BC-16`; `24_` §2; `25_` §8.**

## M · EXTERNAL-AUTHORITY DEPENDENCIES — `14`

Membership **`X-01`…`X-13` + `X-15`** (*not* `X-01`…`X-14`). AAS+ `4` · **Thai statutory `5`** ·
Business SME `2` · PMO `3`. **`36_` §2 of the parent package; `35_` §12.**
**`AAS-V-02` NOT DISCHARGED** — `0` AAS+-authored records, `3` instrument shapes, firing injection.
**Tax substitution rule base `EVIDENCE-INSUFFICIENT`** — *"a black box in this evidence set"*.

## N · CARRIED BOSS OBLIGATIONS — `2` open

| ID | Status | Evidence |
|---|---|---|
| **`POH-D-02`** | **OPEN — NOT ASKABLE.** Thai statutory evidence absent | `05_` §3; `SC-60` |
| **`SC-SMT-01`** | **OPEN — carried, not re-asked.** Gates `X-08`/`X-09` | `05_` §3; `SC-BD-05` §8.1 |

*(`BOSS-CORR1-01` and `BOSS-CORR2-RD01` are **RULED** at `17_`. `B5′` is **asked and deferred**, not open.)*

## O · DROPPED / RESTORED OBLIGATIONS DISCOVERED DURING PRE-TEST — `4`

| Item | Discovery | Status |
|---|---|---|
| **`CORR1-F-02`** `FIFO` layer gap | `5` files → **`0`** in the successor package | **RESTORED** as `CORE-07` |
| **`CORR1-F-03`** idempotency on re-run — *"a re-run can duplicate an opening balance"* | `5` → **`0`** | **RESTORED** |
| **`CORE-03`** veto limb-`2` re-wording | `3` → **`0`** | **RESTORED — BLOCKED** on AAS+ issuer |
| **`CORE-07` identifier collision** | re-used for a second obligation **and announced as *"new"*** | **RESOLVED** — boundary obligation renamed **`CORE-08`** |

**Detected by neither B-7 round.** **`24_`.** **Mechanism:** the successor rebuilt its obligation set from
a post-ruling state rather than from the predecessor's closing state. **No control compared a
successor's open list against its predecessor's** — sweep units `1c`/`1d` were added in response.

## P · MEASUREMENT / INSTRUMENT DEFECTS RELEVANT TO FUTURE VDR — `13`

**Published because a future programme inherits the instruments, not just the findings.**

| # | Defect | Shape | Where |
|---:|---|---|---|
| `1` | path set declared as `NEW_SESSION_2026_09_10/**`; `SA_CORR2_05`/`06` are on the frozen tree — **`4` denominators wrongly called UNSUPPORTED** | **wrong boundary read as absent evidence** | `26_` §2 |
| `2` | identifier detector required severity inside a short bold span — **returned `0` of `14` defined** | broken predicate → clean zero | `12_` §4.1 |
| `3` | same detector, second round — missed headings and long spans | **recurrence of `2`** | `32_` §9.2 |
| `4` | severity vocabulary lacked a **fourth class** (*recorded in the executor's favour*) | vocabulary narrower than the data | `32_` §9.2 |
| `5` | citation check compared **all** `NN_` refs against own files — `7` false unresolved | **unit conflation** (own vs peer) | `12_` §4.1 |
| `6` | same check, second round | **recurrence of `5`** | `32_` §9.2 |
| `7` | status extractor took the **empty trailing field** — `0` verdicts on `18` rows | broken predicate → clean zero | `26_` §2.2 |
| `8` | verdict vocabulary lacked **`NO POSTING BY DESIGN`** — `3` `AR` rows returned `None` | vocabulary narrower than the data | `26_` §2.2 |
| `9` | `AR` **row count `28` ≠ id count `29`** (one row carries two ids) | **row unit ≠ identifier unit** | `26_` §2.2 |
| `10` | `01_` headline `14`/`3` — counted `15`/`2` | headline not re-derived | `12_` §4.1 |
| `11` | `26_` headline `9`/`9` — counted `12`/`6` | headline not re-derived | `32_` §9.1 |
| `12` | `29_` *"new `10`"* and `20`/`18` — counted `12`, and `22`/`19`/`1`/`2` | headline not re-derived | `32_` §9.1 |
| `13` | `30_` *"`4` meet their floor"* — **a dimension meets its floor only when every measure does: `0 of 12`**; `32_` *"PASS `7` / FAIL `5`"* — counted `8`/`4` | **passing sub-measure read as a passing dimension** | `32_` §9.1 |

> **`4` shapes recur, and `2` recur across rounds.** The families are: **broken predicate returning a
> clean zero** (`2`, `3`, `7`), **vocabulary narrower than the data** (`4`, `8`), **unit conflation**
> (`5`, `6`, `9`, `13`), **headline not re-derived from its own list** (`10`–`13`).
> **Every one was caught by the same control: re-deriving a count from the list it summarises, and
> giving each negative instrument a positive control.** **That control is the single most transferable
> output of this programme, and it is offered to VDR as such.**

---

## SUMMARY OF COUNTS

| Cat. | Subject | n |
|---|---|---:|
| `A` | Coverage dimensions below `96 %` | `12` |
| `B` | Critical controls below `100 %` | `2` |
| `C` | FD blockers in the register | `20` |
| `D` | Unresolved business semantics | `16` |
| `E` | Configuration items incomplete | `7` |
| `F` | Optional functions incomplete | `7` |
| `G` | Cross-module / boundary gaps | `6` |
| `H` | Accounting / inventory handoff gaps | `16` |
| `I` | `MF-03` classification | `1` |
| `J` | Tenant / company isolation gaps | `3` |
| `K` | Reconciliation / E2E gaps | `22` |
| `L` | Historical / migration gaps | `4` |
| `M` | External-authority dependencies | `14` |
| `N` | Carried Boss obligations (open) | `2` |
| `O` | Dropped / restored obligations | `4` |
| `P` | Measurement / instrument defects | `13` |
| | **TOTAL CATEGORY ENTRIES** | **`149`** |

```
CHECK 12+2+20+16+7+7+6+16+1+3+22+4+14+2+4+13 = 149   OK
```

> **`149` is a sum across overlapping views (§0). It is NOT a distinct gap population and NOT a VDR
> denominator. LESA determines its own denominators through its own Canonical Process.**

---

## CHECKPOINT

> **`16` categories · `149` category entries · **every entry carries an evidence pointer** ·
> overlap declared **before** the counts, with the distinct-spine estimate published and labelled as
> this session's framing · **`0` interpretation of backlog size as a VDR denominator** ·
> `13` instrument defects published so a future programme inherits the corrections, not the errors ·
> **frozen as VDR INPUT. LESA owns the process.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
