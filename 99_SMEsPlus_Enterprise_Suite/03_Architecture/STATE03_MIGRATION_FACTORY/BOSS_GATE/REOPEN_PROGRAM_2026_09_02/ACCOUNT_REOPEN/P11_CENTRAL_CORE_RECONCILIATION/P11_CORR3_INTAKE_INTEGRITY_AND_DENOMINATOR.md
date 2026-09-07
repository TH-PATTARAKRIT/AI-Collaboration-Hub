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
| **`P09`** | **`4778792`** | **MOVED** | 1,091 |
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

> ### **`UNION = 212`. That is the CORR3 intake denominator — and the instrument that produced it is NOT CERTIFIED.**
>
> **CORRECTED `2026-09-06` by the CORR3 challenge.** The figures reproduce exactly from the now-published
> code (`LAYER2_P11_EVIDENCE/corr3_instrument/intake_derivations.py`, with `union_212.txt`), but the
> instrument carries **six confirmed defects** recorded inline in that file and in §3.5. **The numbers
> were right and the certification was not.**

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

### 3.4 Certification — **WITHDRAWN**

> ### `INSTRUMENT NOT CERTIFIED.`
>
> **The control set was truncated.** P11's own error log names **twelve** artefacts CORR2's instrument
> lost — `D26`, `D27`, **`S06`**, `S22`, **`D24`** of P09, plus the others. **P11 listed twelve and
> tested ten.** Re-run on the full twelve: **11 pass, `S06` fails — union hit 0.**
>
> **And `S06` carries the standard this instrument violates.** `S06_P09_NEGATIVE_CLAIM_CONTROL_STANDARD.md`,
> issued *"for adoption across all SMEsPlus Deep Research processes"*, line 21:
> **`NC-8` — "No `head`, `tail`, sampling, `limit`, or first-N command may bound a population."**
> **`D3` is a `tail` and it bounds this denominator.** `P11-E-42`.

### 3.5 The six confirmed instrument defects

| # | Defect | Consequence |
|---|---|---|
| 1 | **`D3`'s "last 5" is LEXICAL** — `git ls-tree` has no timestamps | `CURRENT-CRITICAL` is unestablished for every un-numbered group. P01's `P`-series returns `S,V,V,V,W,W` — **the alphabet**. *The defect that got attempt 1 rejected survives into attempt 4: the partition changed, the order never did* |
| 2 | **`PEER\|basename` discards generations** | `P09_CHECKPOINT_REGISTER.md` at **5** paths and `P09_AUTO_RESUME_STATE.md` at **5** collapse to **2 keys**; the directory is the only discriminator between the `09-05` and `09-06` generations |
| 3 | **Raw substring membership** | `P04` ⊂ `STEP0401`; **26** State-02 migration artefacts entered under P04 alone |
| 4 | **§3.2's blind-spot table is `UNION − \|Di\|`** | a tautology. **It cannot fail.** Titled *"executed, not declared"* |
| 5 | **`TAIL = 5` is fitted** | `D26` sits at **−2**; `TAIL=2` would pass. The control returns **10/10 at TAIL 2,3,4,5** while `D3` moves **117 → 207** |
| 6 | **The failure control is vacuous** | its subject is not in the scanned population — **the identical defect CORR2 condemned as `X2-R1`** |

### 3.4-old Certification *(superseded, preserved)*

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
| **ADDRESSED** | ~~77~~ **84** (`D1 ∪ D2`) | **CORRECTED (`X2-C3`)** — §3.1's own cells give `55 + 48 − 19 = 84`. P11 published a figure contradicted three lines earlier in the same file |
| **OPENED / READ by P11** | **21** | listed in `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md` |
| **CURRENT-CRITICAL** | **155** (`D3`) | owner's recent statements; **opened only where they bear on a claim P11 holds** |
| **HANDOFF WRITTEN** | **≥ 14** | a peer states it hands something to P11 |
| **HANDOFF DELIVERED / RECEIVED** | ~~0 evidenced~~ **FALSIFIED** | **`X1-3`/`X3-C1`/`X4-C6`.** `23_P10_PEER_INTAKE_REGISTER.md` records receipt of **four P11-origin items** with a verification column and a reasoned refusal (`RF-02`); `P06_AUTO_RESUME_STATE` L16-17 is a working receipt record. **And the artefact that falsifies this is in none of D1/D2/D3** |
| **EXCLUDED, not opened** | **191** | `212 − 21`. **This is a partition by READ STATUS and may not be added to `ADDRESSED`** (`X2-C4`, self-flagged) |
| **NOT ADDRESSED** | **128** | `212 − 84`. A **different** partition, by addressing. **§5's single exclusion reason is false for the 63 artefacts that are addressed AND unopened** |

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

> ### `INTAKE INTEGRITY: NOT ESTABLISHED.`
>
> **What holds:** the peer snapshot (10/10 file counts exact, verified by three experts); `D1`=55,
> `D2`=48 and the union/intersection test **19/36/29**, reproduced independently by three experts; the
> `D26` diagnosis and `P11-G-07`; and **the instrument is now published and re-executes exactly**.
>
> **What does not:** the certification (§3.4), `CURRENT-CRITICAL` for un-numbered groups, the
> generation-discarding key, the `ADDRESSED` count, the exclusion authority, and the claim that *every
> artefact CORR2 missed is now inside the denominator* — **`S06` is not**.
>
> **`B-27` is NOT discharged.** Publishing the instrument was necessary and is not sufficient; the
> instrument it publishes is defective in six named ways.

**`CP-P11C3-01`/`-02`/`-03` — COMPLETE — EVIDENCE VERIFIED.**
