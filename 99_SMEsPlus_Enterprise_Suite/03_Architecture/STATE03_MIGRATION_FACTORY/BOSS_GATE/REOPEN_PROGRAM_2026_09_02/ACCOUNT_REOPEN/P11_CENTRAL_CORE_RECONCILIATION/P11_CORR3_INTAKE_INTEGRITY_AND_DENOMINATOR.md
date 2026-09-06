# P11 — CORR3 ACCOUNTING INTAKE INTEGRITY AND DENOMINATOR

`[SMEPLUS-26-09-06-ACC-P11-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-01`/`-02`/`-03` · **PHASE S** · AI EOS **OFF**

> **Intake before convergence.** Nothing in this round claims convergence until P11 can state what it
> **received, enumerated, opened, interpreted and superseded**, and prove the instrument that found it
> could have failed.

---

## 1. `CORR3 PEER SNAPSHOT` — resolved once, frozen

| Peer | Frozen SHA | vs CORR2 | `.md` in tree |
|---|---|---|---|
| `P01` | `b820b29` | unchanged | 1,094 |
| `P02` | `7cb1c27` | unchanged | 1,019 |
| `P03` | `bc767a8` | unchanged | 1,054 |
| `P04` | `65b8841` | unchanged | 1,007 |
| `P05` | `205e0ac` | unchanged | 1,046 |
| **`P06`** | **`1b018c1`** | **MOVED** | 1,050 |
| `P07` | `ee2be30` | unchanged | 998 |
| **`P08`** | **`00ccd66`** | **MOVED** | 1,033 |
| **`P09`** | **`92de8a1`** | **MOVED** | 1,091 |
| `P10` | `1fea562` | unchanged | 1,063 |

**3 of 10 moved**, and they are the three Accounting-House concurrency peers. **The snapshot is frozen
here. Later peer commits are `POST-SNAPSHOT MATERIAL DELTA CANDIDATE` and are not consumed.**

> **A published branch is not proof P11 received or read an artefact, and a written handoff is not
> proof of delivery.** Both are tracked separately in §4.

---

## 2. The intake instrument — rebuilt, because the old one was not repairable

**CORR2's instrument matched `basename contains peer-id AND one of six tokens`. CORR3 does not fix that
pattern; it replaces it with three derivations and takes their union**, because the prompt forbids
using filename as semantic truth and because **no single derivation is complete** (proved in §3).

| id | Derivation | Semantics | Finds |
|---|---|---|---|
| **`D1`** | basename carries peer-id **AND** a token | CORR2's instrument, retained **only** as one input | **55** |
| **`D2`** | **file CONTENT carries a markdown heading naming P11** (`^#{1,4} .*P11`) | *"this artefact addresses P11"* — semantic, not lexical | **48** |
| **`D3`** | the **last 5 members of every (directory, series) group** whose basenames carry the peer id | *"this is the owner's current statement"* — currentness, independent of whether P11 is named | **155** |

> ### **`UNION = 212`. That is the CORR3 intake denominator.**

### 2.1 The finding that justifies three derivations

**`D1` and `D2` answer a different question from `D3`, and CORR2 conflated them.**

- *"Which artefacts address P11?"* → `D1`, `D2`
- *"Which artefacts are current for a claim P11 already holds?"* → `D3`

**`P09`'s `D26` names P11 nowhere, carries no token, and is not the terminal member of its series — and
it partially withdraws the position P11's `B-23` asserts against.** No P11-addressing instrument of any
kind could find it. **That is not a pattern defect. It is a category error**, and it is the reason
CORR2's diagnosis (*"the pattern was a conjunction"*) was itself incomplete.

## 3. Instrument controls — union/intersection test, blind-spot measurement, and four failures

### 3.1 Union / intersection test *(the test CORR2 never ran)*

| | Count |
|---|---|
| `D1 ∩ D2` — both instruments agree | **19** |
| `D1 \ D2` — token but no P11 heading | **36** |
| **`D2 \ D1` — P11 heading, filename instrument blind** | **29**, spanning **all ten peers** |

**`D1` and `D2` agree on 19 of 55.** Two instruments purporting to answer *"does this address P11?"*
overlap on barely a third.

### 3.2 Blind-spot measurement — executed, not declared

| Instrument alone | Misses, of the 212-artefact union |
|---|---|
| `D1` | **157** |
| `D2` | **164** |
| `D3` | **57** |

**No single derivation exceeds 73 % coverage. Every one of the three is load-bearing.**

### 3.3 The instrument failed four times and every failure was caught by a control

| # | Attempt | Failure | Caught by |
|---|---|---|---|
| 1 | `D3` = global `tail -4` per peer | returned `X1`…`X4` alphabetically; **`D27` absent** | positive control naming `D27` |
| 2 | `D3` grouped by series prefix, one directory per peer | **`D27` absent** — the `D`-series lives in a *subdirectory* | same control |
| 3 | `D3` grouped by `(directory, series)`, **terminal member only** | **`D26` absent** — an intermediate member carrying a withdrawal the terminal never restates | control extended to name `D26` |
| 4 | `D3` = last **5** of each `(directory, series)` | **PASS** | — |

> **Attempt 3 is the one that matters.** *Terminal-member-only is insufficient for supersession.* A
> chain's intermediate member can carry a withdrawal that the terminal statement does not repeat, so
> **currentness must be read over the series tail, not the series end.** `P11-G-07`.

### 3.4 Certification

**POSITIVE CONTROL — every artefact CORR2 was shown to have missed must return:**

`43_G02_P02_FINAL_CLEANROOM_HANDOFF` ✔ · `D23_P09_P11` ✔ · `D25_P09_CHALLENGE` ✔ · **`D26_P09_V18` ✔** ·
`D27_P09_EVIDENCE` ✔ · `S18_P09_P11` ✔ · `S23_P09_POST` ✔ · `37_P03_SCOPE02` ✔ · `71_P10_CORE_RECON` ✔ ·
`P01_S16_P11_HANDOFF` ✔ — **10 of 10.**

**FAILURE CONTROL — must return zero:** P11's own package inside a peer tree → **0** · generic
programme template → **0**.

> **The control set is constructed so that it *can* fail: three of its ten members were absent on
> earlier attempts and the instrument was rejected each time.** A control that has never failed is not
> evidence that it works.

**`INSTRUMENT CERTIFIED` for enumeration. It is not certified for *absence*** — see §5.

---

## 4. Read / address status — the four statuses kept apart

| Status | Count | Definition |
|---|---|---|
| **ENUMERATED** | **212** | in the union denominator |
| **ADDRESSED** | **77** (`D1 ∪ D2`) | names P11 in a filename token or a section heading |
| **OPENED / READ by P11** | **21** | listed in `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md` |
| **CURRENT-CRITICAL** | **155** (`D3`) | owner's recent statements; **opened only where they bear on a claim P11 holds** |
| **HANDOFF WRITTEN** | **≥ 14** | a peer states it hands something to P11 |
| **HANDOFF DELIVERED / RECEIVED** | **0 evidenced** | **no peer artefact evidences receipt by P11, and P11 evidences none** |
| **EXCLUDED, with reason** | **191** | enumerated, not opened — reason per §5 |

### 4.1 `WRITTEN ≠ DELIVERED` — a standing gap, now measured

**P11 can evidence that peers *wrote* handoffs. Neither P11 nor any peer can evidence that any handoff
was *delivered to and received by* P11.** The programme has no receipt artefact. Every *"handed to
P11"* in a peer package is a **statement of intent by the sender**, and P11's own consumption records
are **P11's assertion about itself**.

**`P11-B-31` — `HANDOFF DELIVERY IS UNEVIDENCED PROGRAMME-WIDE.`** Not a defect of any one peer. The
correct disposition is a **receipt record** owned by the consumer, and P11 does not have one.
`P06`'s own delta says the same thing from the other side — a *"stale current claim … invisible to the
pattern declared for its class"* (`REV-E-23`).

---

## 5. Exclusions — declared with authority, per `D-3b` v5 `E5`

| Excluded | Count | Authority | Reversal |
|---|---|---|---|
| Enumerated, not P11-addressed, not bearing on a held claim | **191** | §3 of the controlling prompt — *"more research width is not authorised"* | any claim P11 holds that traces to one |
| Peer internals (lifecycle, module, model, runtime) | all | §3 domain purity | route to owner |
| Peer source trees and databases | all | §15 no mutation; §3 purity | Boss |

> **Consequence, stated plainly: this instrument is certified for *what P11 has*, and is NOT certified
> for *what P11 lacks*.** 191 artefacts are enumerated and unopened. **No absence claim in this round
> may rest on the intake denominator**, and none does.

---

## 6. Intake integrity verdict

> ### `INTAKE INTEGRITY: REPAIRED FOR ENUMERATION AND CURRENTNESS · NOT ESTABLISHED FOR DELIVERY`
>
> **Repaired:** the denominator is reproducible from three declared derivations with a control set that
> has demonstrably failed and been fixed; the CORR2 blind spot is **measured at 29 artefacts across all
> ten peers**; every artefact CORR2 was shown to have missed is now inside the denominator.
>
> **Not established:** delivery/receipt (`P11-B-31`), and absence of anything (§5).

**`CP-P11C3-01`/`-02`/`-03` — COMPLETE — EVIDENCE VERIFIED.**
