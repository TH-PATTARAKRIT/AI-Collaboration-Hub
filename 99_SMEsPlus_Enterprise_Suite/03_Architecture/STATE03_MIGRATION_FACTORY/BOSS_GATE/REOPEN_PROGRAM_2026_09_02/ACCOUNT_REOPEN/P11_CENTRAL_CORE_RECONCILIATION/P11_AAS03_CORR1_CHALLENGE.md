# P11 — C9 · AAS-03 CORR1 FOUR-LAYER CHALLENGE

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C09 · Layer 1 clean-room
Panel bounded to commit **`11f473f`**, files timestamped 09:00–09:10 on `2026-09-05`.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Verdict

> # `CONTRADICTED`
>
> *"The round's headline result — the `C`→`A` upgrade of `UAE-29`/`T0-08`/`D-5`, and with it C6 §3,
> C7 §3 and C8 §2–§3 — rests on a `P08` claim that `P08` **withdrew as `CONTRADICTED`** in a
> superseding handoff pack P11 never opened; and the `D-3b` v4 control that was supposed to prevent
> exactly this **omits the population step** and certifies a sample as complete over a host population
> at least twice the size P11 declared."*

**P11 verified the three `CRITICAL` findings at source before accepting any of them.** All three hold.
**18 findings raised · 18 accepted · 0 disputed.**

## 2. The three `CRITICAL` findings, verified by P11 at source

### `C-01` — the headline upgrade is withdrawn

P11 published: *"`A VERIFIED ABSENCE` across all 22 declared roots"*, upgrading `UAE-29`/`T0-08`/`D-5`
from class `C` to class `A`, and called it *"the highest-value change in this matrix"*.

**Verified at `P08` `52_P08_CORE_RECON_HANDOFF_PACK_V2.md`**, which is headed **"Supersedes
`25_P08_CORE_RECON_HANDOFF_PACK.md`"** and is addressed to **"P11 Core Accounting Reconciliation"**:

> | **Event identity** | **The business record, per channel — absent as a platform property** | `FACT VERIFIED`, **base narrowed** |
>
> Break 1: *"No durable event identity **as a platform property**… identity exists on **one inbound
> channel, on a nullable column, 0 of 13,814 rows populated**."*

> ### The upgrade is WITHDRAWN. P11 quoted the superseded pack's headline verbatim.

**What survives, and it is not nothing.** The finding stands on **different and in one respect stronger**
ground: an identity that exists per channel, on a nullable column, **populated in 0 of 13,814 rows**, is
a *measured* deployment fact rather than an inferred source absence. **But it is not a 22-root verified
absence, and `P08`'s own correctly-scoped successor claim — *no accounting-event object with identity
independent of the journal entry* — is `UNTESTED across the root set`.**

### `B-01` — an eighth ordering surface, and it is the cause of `C-01`

P11's own `P11-M-04` audit examined seven ordering surfaces and cleared the peer-artefact question at
the **peer** level. **The eighth is intra-peer artefact version order.**

**Verified by P11:** `P08` publishes **two** handoff packs (`25_`, `52_…_V2`); `P10` publishes
**three** (`18_`, `37_…_V2`, `71_`). **P11 read the earliest of each.** The branch SHA P11 recorded was
correct; the artefact inside it was superseded.

> **`P11-G-04` does not fix this.** Ranking peers by relevance still selects the wrong file inside the
> right peer. **The rule must bind at artefact level — path **and** SHA — not at peer level.**

**`P10` `71_` §1 is titled *"What Changed for P11"*** and P11 had not read it. It carries: the
status-quo option **restored**; **three coupled Boss decisions, not two** (`T0-13` → `D-5` → `P10-D-02`);
**a peer design veto that binds `P10` and had never been read**; and — pointedly — that `T0-13`
*"carries a recorded defect in its own derivation… **the Boss should see that beside it**."*

### `A-01` — the dump population is a floor of 9, not 4, and a third format exists

P11 declared *"4+ dumps"*, ranked 4, opened 2, and certified *"2 of 2 versions ⇒ complete"*.

**The panel re-derived 9 candidate artefacts** including two `.zip` containers holding **plain `dump.sql`**
— **a third format that needs no `pg_restore` version at all** — plus an Oracle DDL file and two
`iTEST02` copies at **65,444,053 B**, *larger than the artefact P11 ranked second*.

> **"2 of 2 ⇒ complete" is false.** And the failure is in the control P11 wrote to prevent it: **`D-3b`
> v4 has no population element** (`B-03`), so coverage was measured against a denominator the control
> never required deriving.

## 3. Findings by layer

| Layer | Ids | Accepted |
|---|---|---|
| **A — evidence population / denominator** | `A-01`…`A-06` | 6 of 6 |
| **B — tooling / extraction / selection** | `B-01`…`B-05` | 5 of 5 |
| **C — finding / accounting semantics** | `C-01`…`C-05` | 5 of 5 |
| **D — decision authority / cross-process boundary** | `D-01`…`D-07` | 7 of 7 |

**Selected, beyond the three criticals:**

| id | Finding | Disposition |
|---|---|---|
| `A-02` | `P08` phrases its class-A negatives as **"21 of 21 roots"**, not 22; and `P08-CONTRA-34` records **7 distinct contents by hash**, so *"apparent strength is overstated by roughly threefold"* | **ACCEPTED** — every inherited root-set claim now carries the independence limit |
| `A-03` | **C8 is the only CORR1 register with no declared denominator** — and it is the one that read the wrong artefact | **ACCEPTED** — the causal link is exact |
| `A-05` | C6 says *"5 strengthened"*; its own table marks **6** | **ACCEPTED** — the `P11-E-01` class, recurring inside the correction round |
| `C-02` | `B-17` closed using a `P08` **source-line (18.0)** statement across a boundary `P08` forbids: *"**No deployed database matches the source line.** Any peer combining the two as one fact must re-read it as two facts with two scopes"* | **ACCEPTED** — `B-17` **re-opened**, see §4 |
| `C-03` | `KRN-INV-00` is marked **`CONTESTED`** by `P08-BD-18` and **"must not be inherited downstream"**; P11 inherited it as *"strengthened to its maximum available form"* | **ACCEPTED** — embargo stamped |
| `C-05` | `B-12` discharged on *publication*; its condition was **contract establishment**, and `B-10` (**0 of 10 compliant**) is carried unchanged in the same table | **ACCEPTED** — `B-12` **re-opened** |
| `D-01` | **≈7 decisions routed to P11 by peers never reached §31** — `P08-BD-09/11/16/17/18`, entry-vs-item finality, `P10-D-01`…`D-06` | **ACCEPTED** — decision population re-declared |
| `D-03` | The gate pack's own `TERMINAL STATE` says *"ten named decisions"* while §31 has 13 — **C7's row-pattern structurally could not see prose** | **ACCEPTED** — pattern-boundedness inside the register created to fix counting by class |
| `D-05` | `D-10` recorded *"DISCHARGED — this run is it"* in a matrix whose footer says *"0 decided by P11"* | **ACCEPTED** → `EXECUTED UNDER PROMPT — RATIFICATION OUTSTANDING` |
| **`D-07`** | **P11 mutated the package while the challenge it commissioned was running** — `B-17` moved from *"deliberately not repaired"* to `CLOSED` mid-review | **ACCEPTED — P11's process error, §5** |

## 4. What P11 re-opens as a result

| Item | Was | Now |
|---|---|---|
| `C`→`A` upgrade of `UAE-29`/`T0-08`/`D-5` | the round's headline | **WITHDRAWN.** Restated on the measured per-channel basis |
| `B-17` | `CLOSED` | **RE-OPENED** — its `S3` input crossed a scope its source forbids (`C-02`) |
| `B-12` | discharged | **RE-OPENED** — publication ≠ contract establishment (`C-05`) |
| `B-18` | `CLOSED` | **stands** — but its audit population excludes CORR1's own supersessions (`B-05`) |
| `D-3b` v4 | 5 elements | **v5 required** — add `E0` population and `E6` independent denominator challenge |
| `P11-G-04` | binds at peer level | **must bind at artefact level: path + SHA** |

## 5. `P11-E-30` — P11 broke freeze-before-review, and it is P11's error not the panel's

`D-07` is upheld. P11 commissioned an independent challenge and then **continued editing the package
under review**, closing the round's only `CRITICAL` mid-review. The panel had to bound its findings to
`11f473f` and say so.

> **P11's own memory of this programme records that freezing the package before review opens is the
> precondition for the review meaning anything. P11 violated it in the round convened to repair its
> method.** The panel's findings are valid; **their coverage of `B-17`'s closure and the four files
> created at 09:08 is not, and cannot be, complete.**

**Consequence:** `B-17`'s re-opening rests on `C-02`, which the panel *could* evaluate. **Anything
created after `11f473f` is unreviewed** and is marked so in the checkpoint register.

## 6. Claims the panel attacked and could not break

18 blockers at `43195fd` (exact); 29 error ids; **13 inherited tolerance-zero** — *"I expected 10 and
was wrong"*; all ten peer SHAs accurate; all ten peers do publish a handoff pack; C1's blast-radius scan
**sound in method**; `2.4×` arithmetically correct within P11's population; `B-18`'s closure evidenced
with declared controls; `B-17`'s re-run **honest in direction** — *"it makes the headline worse and says
so"*; and **C7's citation of `P08`'s refusal to take the favourable reading is exactly right** — which
the panel notes *"sharpens `C-01`: P11 quotes `P08`'s refusal to take the favourable reading, then takes
it."*
