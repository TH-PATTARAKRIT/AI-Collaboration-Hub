# 19 — AAS+ PROVISIONAL SYNTHESIS REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-AASR-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` — **IN PROGRESS, NOT TERMINATED**
Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001` · Depth `L99999.99999` · Model `Claude Opus 5 (Extra)`

---

## TERMINAL STATE

> # `ACCOUNT WAVE A — PROVISIONAL PARALLEL SYNTHESIS · AAS+ OUTPUT IS NOT CANONICAL`
> # `AWAITING PARENT CONVERGENCE, REGISTER CLOSURE AND DELTA REVALIDATION`

**Not declared:** architecture frozen · semantic model final · Deep Research Standard final, effective
or candidate · findings complete · parent package superseded · implementation recommended · Wave A
closed · Wave B started · gate movement · Boss approval · convergence · `CONDITIONAL PASS`.

**Gate recommendation: none is issued.** The mandate's four allowed recommendations
(`ACCEPTANCE` / `ACCEPTANCE WITH CARRY-FORWARD` / `HOLD` / `FAIL`) all presuppose a terminated parent
round. **Issuing any of them against an unfinished parent would itself be a completeness claim** — the
defect this programme exists to prevent. Boss is the sole Final Approver.

---

## 1. Why the mandate's §2 precondition was not met

| # | Ground | Class |
|---|---|---|
| `PC-01` | Parent self-reports **`METHOD NOT CONVERGED`**. `MC-01`…`MC-10`: **8 not met · 2 partially met · 0 met**. Fixed point **not reached** — six of seven criteria fail on **both** consecutive passes | `VERIFIED FACT` |
| `PC-02` | **Ten tolerance-zero boundaries recorded, zero resolved — and two further returned by the parent's own challenge, recorded only in `MCC_J`. Twelve known, ten documented** | `VERIFIED FACT` |
| `PC-03` | **`AASR-F-01`** — the parent package is **untracked in git and unpushed**; no `mcc` remote branch exists; **`MCC_J`, the MCC gate report and the MCC evidence manifest do not exist**. `MCC_J` is cited as the *governing record* of the parent's own §7 challenge | `VERIFIED FACT` |

The Boss containment directive received mid-session independently confirmed `PC-03`'s cause. This
session therefore produced a **parallel provisional synthesis**, not a gate recommendation.

---

## 2. What was produced

**23 files.** Evidence reconstructed from **93 parent artefacts across six rounds**, plus **20 rescued
files** preserved by parallel-copy and hash-fixed at consumption time (`01A` / `DEP-00`).

| Deliverable | Content |
|---|---|
| `01` + `01A` | Controlling dependency register — **38 design rows**, each with evidence, parent dependency, assumption, invalidation trigger, status, required revalidation; §5 records the closure forced by the veto |
| `02` | Verified semantic baseline by evidence class, with negative-claim classes attached |
| `03`–`12` | Candidate models: event · financial fact · COA · journal · entry/item · reconciliation · date/period · FX · lock/close/reopen · SaaS boundary |
| `13` | Event → financial fact chain, **8 breaks across 10 links** |
| `14` | Balanced-but-wrong design challenge, 19 classes **+ `T-20`** |
| `15` | Unknown → design impact register |
| `16` | **8 architectural decisions, ≥2 alternatives each, 5 recommendations and 3 deliberate non-recommendations** |
| `17` | Ten AAS+ perspectives, **5 disagreements preserved undispositioned** |
| `18` + `18A` | Independent veto (**68 findings**) and self-scan (**13 findings**) |
| `20` | Standard-candidate eligibility — **NOT GENERATED**, per-criterion |

---

## 3. Design position

**Every design is `PROVISIONAL`, `EVIDENCE-DEPENDENT`, `UNKNOWN` or `INVALIDATED`. None is
`STABLE-CANDIDATE`** — the label is **unused in this package** (`AASR-C-01`, §6 below).

| Class | Count |
|---|---|
| `PROVISIONAL` | **19** |
| `EVIDENCE-DEPENDENT` — blocked on a named parent finding | **11** |
| `UNKNOWN` — decider **Boss** | **6** |
| `INVALIDATED` | **2** |
| **Total** | **38** |

### The design positions that survived adversarial challenge

Two independent reviewers on disjoint assignments **could not disprove a single design position**:

separate the accounting event from the entry · unconditional immutability enforced below the
application · additive correction with a **content-validated** relation · permanent classification
identity with succession, never rewrite · provenance as part of the fact · a hard-bounded,
undestroyable settlement fact · the accounting date asserted, never derived · the period as an object
with state · **no measurement fallback of any kind** · and **no tenant-isolation claim**.

### The two `INVALIDATED` designs

| id | Why it matters |
|---|---|
| `D-10a` | The `FX-08` framing, carried as a `VERIFIED DEFECT` through **two parent gate reports**, describes a state that **cannot be constructed**. A redesign run before `MCU-13` would have re-architected rate scoping around nothing |
| `D-23` | *"SMEsPlus must design revaluation"* — **`NC-19`: a post-and-reverse revaluation mechanism exists**, and `G-C2` shows it is user-overridable per currency with a warning, making it a *detecting control* a separate finding claimed did not exist. **Two absence claims rested on not having read one file** |

---

## 4. The six Boss decisions

Stated once, here, because the first draft carried three different counts in three files. **None is
answerable by more research.**

| # | Decision | Governs |
|---|---|---|
| 1 | **`GB-01` / `TI-07`** — the SMEsPlus boundary model: does every writer and every reader apply the same scoping rule, and where is the tenant? | `D-33`, `D-10`, `D-31`, all of `12` |
| 2 | **`MCU-02` / `MCU-03`** — accounting-event identity and idempotency. Parent: *"cannot be closed by any amount of further research. It is `GB-01`-class"* | `D-01`, `D-24` |
| 3 | **`CL-01`** — is a closed period a record with a closer, a timestamp and a basis, or a date? | `D-06` |
| 4 | **`CL-04`** — does a late document post to its own period (reopening) or the current one (restatement)? The reference silently chooses the second | `DP-07` |
| 5 | **`D-22`** — is a year-end result transfer posted, or the result derived at report time? | `11 §6` |
| 6 | **`D-28`** — is each dimension a *fact* (immutable, part of the event) or an *attribution* (restatable)? | membership of the immutable core |

Plus `CL-05` (does a parent's irreversible lock cascade to subsidiaries?) — a policy choice the parent
declined to settle.

---

## 5. Blocking position

**11 designs are blocked behind items the parent has not closed.** They are not scattered:

| Blocking item | Designs |
|---|---|
| `GB-01` boundary model | `D-33`, `D-10` |
| `GB-02` cross-company rewrite — **widened twice** | `D-31`, `CB-05` |
| `GB-03` null-company rate row — open half | `D-10` |
| `GB-04` exposure **9 of 192**, over a path set short by 962 modules | `D-34`, every isolation claim |
| `GB-07`/`MCU-18` unsearched module tree | `D-01`, `D-04`, `D-29` |
| `GB-08`/`MCU-20` v19 instability | `D-30`, **all of file `10`** |
| `T0-01`…`T0-06` | `D-02`, `D-12`, `D-13`, `D-17`, `D-18`, `D-20` |
| `T0-07`…`T0-10` | `D-09`, `D-14`, `D-26`, `D-32`, `D-08`, `D-27` |
| `MCU-04`/`MCU-11` report scope | `L-9`, `T-19` |
| `MCU-19` migrated rate rows | `D-35` |
| `MCU-60`/`MCU-61` tenancy, reverted to class `B` | `D-33` foundation |

> **`14 §3` states the consequence exactly: the design fully answers 6 of 20 known failure classes,
> and every one of the six it cannot defend is a cross-boundary class — tenant, company, integrity
> domain, or report definition. The redesign is not blocked in many places for many reasons. It is
> blocked in one place — the boundary model — for one reason: the exposure is 9 of 192 assessed, over
> a path set known to be short by 962 modules.**

---

## 6. Independent review — and what it cost

| | Value |
|---|---|
| Self-caught, before review returned | **13** (`NCS-01`…`NCS-07`, `EFC-01`…`EFC-06`) |
| Independent reviewers | **2**, disjoint assignments, neither authored |
| Reviewer findings | **68** — **46 `MATERIAL`** |
| Design positions disproved | **0** |
| Evidence citations disproved | **46** |
| Clean-room leaks (both reviewers, independently) | **0** |
| Prohibited verdict wording (both, independently) | **0** |

### `AASR-C-01` — the label correction

`STABLE-CANDIDATE` was applied to **20** designs. Both reviewers independently found it did not mean
what `00 §4` defines: at least nine designs carried it while their own register cell named an open
gating unknown, and the bar could not have been tested at all because **`T0-01`…`T0-06` appeared zero
times in the package**. **All 20 demoted. The label is now unused.**

### `AASR-VETO-01` — upheld

> **`01` was not a usable delta-revalidation worklist**, because it omitted twenty live parent ids —
> `T0-01`…`T0-06`, `GB-05`, `GB-06`, `MCU-60`, `MCU-61`, `CL-01`…`CL-04`, `TI-07`, `TI-08`, `BW-28a`,
> `D-28`. These are **backward** contradictions: parent text that already exists and was already in
> this session's evidence base. **Delta revalidation would never have surfaced them.**

Closed at `01 §5`. **The veto is lifted only by that closure, not by the parent finishing.**

### The method finding

This session ran the negative-claim scan as a separately-tasked step specifically to break the
programme's five-round pattern of *"every material correction from a reviewer, none from the author"*.
It caught **13**. The reviewers then returned **68 more**.

> **Self-review moved the ratio from 0-in-N to 13-in-81. It did not come close to replacing
> independent review.**
>
> `ER-AASR-1` — *take design input from a source's adversarial section, not its summary* — was
> authored by this session after finding six such errors, and was **then found insufficient by its own
> author's reviewers**: they located a *second* correction notice (`MCC_G §8`) below the one it had
> learned to read, and a governing register (`CORR1/C04`, 11 claims class `E — CONTRADICTED`) an
> entire round below that.
>
> **The rule was correct and under-applied by its author inside the same session that wrote it.** That
> is `MCC_K`'s fifth clause — independence — demonstrated at close range: **a control designed by the
> author is not independent of the author.**

---

## 7. Scope limitations, stated

| Limitation | Note |
|---|---|
| **Source-level design verification was not performed** | A deliberate containment choice, **not an access limitation**. Reference source trees exist and were used once, to re-derive the 962-module boundary on this package's own claims (`18A §5`). Re-stated explicitly because a prior programme session concluded *"no source or database access exists"* after searching only its working tree |
| `MCC_J` has never been read | It does not exist. **No design here has been tested against the parent's own expert and audit challenge** |
| Register closure is complete against ids **found**; not proven exhaustive | The reviewers found twenty in one pass. A third pass may find more |
| `GB-05` exposure not established | Seven contradicted affirmative claims still stand live in the canonical registers `02` was reconstructed from. **Which `VF-*` rows are exposed is not yet known** |

---

## 8. Continuation — in order

1. **Close the register further** against the parent evidence **that already exists** — `01 §5` closed twenty ids; `GB-05`'s seven live contradicted claims are the next target. **Cheap, and not on the parent worklist.**
2. **Read `MCC_J` when it exists.** It governs the parent's §7 challenge and holds two tolerance-zero boundaries nobody has read.
3. **On parent termination:** stop synthesis · ingest · byte-diff against `01A` · re-test all 38 rows · re-run the negative-claim scan · **only then** restart synthesis from the converged baseline.
4. **Put the six Boss decisions to Boss.** Four gate design components directly and none can be closed by research.
5. **Do not begin Wave B.** Do not implement. Do not declare any standard effective.

---

## 9. Declaration

Nothing in this package is canonical, converged, final, approved, or authorised for implementation.
No SMEsPlus or reference source code was modified. Nothing was merged or deployed. Wave A is not
closed and Wave B has not started.

**Boss is the sole Final Approver. No Evidence = No Progress. Never Skip Gate.**
