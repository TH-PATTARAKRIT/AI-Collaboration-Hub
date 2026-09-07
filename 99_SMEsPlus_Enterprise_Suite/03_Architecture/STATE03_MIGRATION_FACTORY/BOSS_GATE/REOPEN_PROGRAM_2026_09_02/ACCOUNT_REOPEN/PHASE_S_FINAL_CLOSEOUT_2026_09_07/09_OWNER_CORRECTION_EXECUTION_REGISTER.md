# 09_OWNER_CORRECTION_EXECUTION_REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**Authority** `PHASE-S/Q-BOSS-01 = APPROVED` @ `1bf9b40` — 13 owner-bounded items
**Classification** LAYER 2 — AUDIT QUARANTINE

> **Terminal disposition vocabulary.** `EXECUTED — GATED` means the repair is published and its
> completion condition names an RC that has not run. It is **not** a pass and **not** a discharge.
> `CLOSED` is never used as a synonym for `DISCHARGED`.

## 1. The 13 authorized items — terminal disposition

| # | Item | Track / freeze branch | Disposition | Gate |
|---|---|---|---|---|
| 1 | `Q-P06-01` totals re-enumeration | P06 IEV · `corr/p06-iev-…` `692ea27` | **EXECUTED — GATED** | `RC-03` |
| 2 | `Q-P06-02` 65-row contradiction | P06 IEV (as scoped) | **NOT EXECUTABLE AS SCOPED — RE-ISSUED** (§3) | `RC-04` after re-issue |
| 3 | `Q-P06-03` count families + `P06-B-58` re-scale | P06 source · `corr/p06-source-…` `b5f5a21` | **EXECUTED — GATED** | `RC-04` |
| 4 | `Q-P06-04` archive negative re-run | P06 source · `b5f5a21` | **EXECUTED — GATED** | `RC-04` |
| 5 | `Q-P08-01` no-referent figure | P08 source · `corr/p08-…` `c7cfd8a` | **EXECUTED — GATED** | `RC-05` |
| 6 | `Q-P08-02` `HO-` namespace | P08 source · `c7cfd8a` | **EXECUTED — GATED** | `RC-05` |
| 7 | `Q-P08-03` FX cause-clause | P08 IEV · `corr/p08-iev-…` `d685176` | **EXECUTED — POINTER-ONLY** | `RC-07` pointer-only; no fresh challenge required |
| 8 | `Q-P09-01` `M-1` / `L-4` authority | P09 · `corr/p09-…` `2079a25` | **EXECUTED — GATED** | `RC-01` |
| 9 | `Q-P09-02` challenge scope | P09 · `2079a25` | **SCOPE PUBLISHED, CHALLENGE CORRECTLY NOT RUN BY AUTHOR** | `RC-01` |
| 10 | `Q-P11-01` re-pin moved peers | P11 · `corr/p11-…` `002748d` | **EXECUTED — GATED, AND MATERIALLY DEFECTIVE** (§4) | `RC-02` |
| 11 | `Q-P11-02` producer-qualify `HO-` | P11 · `002748d` | **EXECUTED — GATED**; declared residue `UNRESOLVED — NAMESPACE` | `RC-02` |
| 12 | `Q-P11-03` re-state `B-38` | P11 · `002748d` | **EXECUTED — GATED** | `RC-02` |
| 13 | `Q-P11-04` withdraw `F-02` + method rule | P11 · `002748d` | **EXECUTED — GATED** | `RC-06` |

**13 of 13 have a terminal disposition. 0 are complete**, because completion requires an RC that no
eligible party has run.

## 2. `XQ-R-02` ADJUDICATED — the P06 material-defect denominator is **26**

The dispatch (§4B) makes the enumeration authoritative and forbids forcing 25. **Re-executed
independently here, not adopted from P06's record.**

```
POPULATION  distinct IEV-D-nn identifiers in every file under IEV_006/ at 692ea27  (10 files)
UNIT        one distinct identifier   (NOT one occurrence, NOT one file)

FORM 1  git grep -oh -E 'IEV-D-[0-9]+' 692ea27 -- 'IEV_006/*' | sort -u -V | wc -l    → 27
FORM 2  python re.findall(r'IEV-D-\d+') over each file's bytes                        → 27
        SET IDENTITY between the two forms: IDENTICAL
```

**Both forms returned 27, not 26. The extra member is `IEV-D-99` — the documented negative-control
token, matching its own documentation** at `P06_Q_P06_01_02_EXECUTION_RECORD.md:66`
(`NEGATIVE CONTROL  IEV-D-99 → 0`). This is P06's own standing rule firing against P06's own register:
*a grep for a literal token will match its own documentation.*

```
POPULATION corrected: distinct IEV-D-nn ids EXCLUDING the self-documented control token
COUNT        → 26
CONTIGUITY   min 1 · max 26 · distinct 26 · gaps NONE
POSITIVE CONTROL  IEV-D-01 → 10 occurrences
NEGATIVE CONTROL  IEV-D-99 → occurs ONCE, and only as control documentation (line cited above)
```

**`IEV-D-26` is substantive, not a paper item:** it is the root defect of `Q-P06-04` (`XRD-004`) — the
archive pattern that cannot fire — defined in `P06_INDEPENDENT_VERIFICATION_ADDENDUM_E2.md` §4 in prose,
outside the §3 table over which the 25 was summed.

> **ADJUDICATION: the P06 IEV material-defect denominator is `26`. The adopted 25 is superseded.
> Both 18 and 25 are retained as lineage on the P06 IEV surface.** Every dependent total must be
> re-derived from 26. **This adjudication is a controller finding and is itself subject to `RC-03`.**

**A second-order note that must not be lost:** this session's own first count returned **27** and would
have been published as 27 had the second command shape not been run. The rule that saved it is the one
P06 wrote one round earlier.

## 3. `XQ-R-01` RESOLVED — `Q-P06-02` re-issued against the correct artefact

Published as a **bounded queue correction**, not a silent edit of the adopted row.

| | |
|---|---|
| **Original pointer** | `IEV_006/P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45 (contradicted by `:54`), on `audit/p06-independent-verifier-2026-09-06-001` |
| **Evidence the pointer is wrong** | `git show 692ea27:…/P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md \| grep -n '65'` → **one line, `:5`, the frozen SHA**. The file has no validation table and no `:45` row |
| **Corrected pointer** | `…/P06_BANK_TO_RECONCILE_EXECUTION/G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:45, on `corr/p06-source-phase-s-final-2026-09-07-001` @ `b5f5a21` |
| **Evidence the corrected pointer is right** | `:45` reads `\| 65 \`P06-B-*\` \| grep -oh … \| max id = 65 and contiguous \| **YES** \|` — and `:54` of the same file raises `P06-B-66` and `P06-B-67`. The self-contradiction is intact and verified at `b5f5a21` |
| **Why scope is unchanged** | Same defect, same claim, same two lines, same round. Only the file identity changes. **The defect class, the unit and the Re-test are untouched** |
| **Origin of the error** | P06's own `IEV-D-20` mis-attributed the row to the verifier's own file; the queue inherited the wrong name in good faith. Corrected on the IEV surface as `XQ-F-02`, superseded wording retained |

**Track consequence:** the row lives on the **source** track, so re-issued `Q-P06-02` is a natural member
of `Q-P06-03`'s count families and **its challenge belongs to `RC-04`, not `RC-03`.**

**Not repaired here.** `:45` still reads 65 at `b5f5a21`. Repairing it is owner work on the source track
under the re-issued item; this session re-issues the item and does not execute it.

## 3a. `XQ-R-03` — DISPOSED, no action required here

P06 routed three items back. `XQ-R-01` and `XQ-R-02` are resolved above. **`XQ-R-03` — the wrong file
attribution inside `IEV-D-20`, which the queue inherited in good faith — was already corrected by P06 on
its own IEV surface at `692ea27`, with the superseded wording retained as lineage.**

**Disposition: RESOLVED BY THE OWNER, verified present on the frozen surface. No controller action.**
It is recorded here so the routed set is complete: **three routed, three disposed.** Its correctness is
`RC-03`'s to test.

## 4. `CO-F-01` — MATERIAL: P11's re-pin repair is behaviourally inert, and its denominator is non-deterministic

**Discovered and reproduced by this session while freezing the `RC-02` surface.**

### 4.1 The instrument never reads the pin it declares

`LAYER2_P11_EVIDENCE/corr3_instrument/intake_derivations.py` declares a `PEERS` table of ten
`(peer, sha, branch)` rows. Both places it resolves a tree use **`"origin/"+br`** — the floating branch
head. **The `sha` field is never read.**

```
RUN A  instrument exactly as published at 002748d      (P09 pinned 4778792)
RUN B  identical file, one character class changed:    (P09 pinned 92de8a1)
       diff(union_A, union_B)  →  IDENTICAL, byte for byte
```

> **`Q-P11-01`'s repair — and `P11-E-47`'s follow-up correction of that same `.py` — change a value the
> program never reads. Both are behaviourally inert.**

### 4.2 The published denominator is a floating-head artefact

All runs below are `python3 intake_derivations.py` from the repository root, with a positive control
confirming the instrument can see the tree (`git ls-tree` over the P08 branch → 1034 `.md` files).

| Run | Refs resolved | D1 | D2 | D3 | UNION | D1∩D2 / D1\D2 / D2\D1 |
|---|---|---|---|---|---|---|
| **P11 published "before"** | claimed at `92de8a1` | 55 | 48 | 155 | **212** | 19 / 36 / 29 |
| **P11 published "after"** | claimed at `4778792` | 57 | 49 | 157 | **214** | 20 / 37 / 29 |
| **RUN D** — pins honoured, P09 `92de8a1` | pinned | **55** | **48** | **155** | **212** | **19 / 36 / 29** |
| **RUN C** — pins honoured, P09 `4778792` | pinned | **56** | **48** | **157** | **214** | **19 / 37 / 29** |
| **RUN E** — floating heads as at `002748d`'s commit time | `P06 1b018c1 · P08 c7cfd8a · P09 150a033` | **57** | **49** | **157** | **214** | **20 / 37 / 29** |
| **RUN A** — floating heads, today | current `origin/*` | **58** | **50** | **159** | **216** | 21 / 37 / 29 |

**RUN D reproduces the published "before" column exactly.** **RUN E reproduces the published "after"
column exactly, and its union file is byte-identical to P11's published `union_212.txt` at `002748d`.**

> **Therefore P11's published denominator was computed against floating branch heads, while the package
> declares it computed against pins.**

### 4.3 The declared pin and the executed membership contradict each other

P11 declares P08 pinned at `00ccd66`. Its published union contains
`P08|64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` — **a file that does not exist at `00ccd66`.** It exists
only at `c7cfd8a`. Conversely the union **drops** `P08|59_P08_METHOD_AND_REQUIREMENT_REGISTER.md`, which
exists at *both* heads.

Mechanism, verified: `D3` takes the last `TAIL=5` members of each numbered series. P08's series is
`50…63` at `00ccd66` (tail = 59,60,61,62,63) and `50…64` at `c7cfd8a` (tail = 60,61,62,63,64). **A P08
correction commit silently pushed `59_` out of P11's denominator and pulled `64_` in.**

**The two 214s are different sets.** RUN C (pins honoured) and P11's published run agree on the
cardinality 214 and disagree on membership by exactly this one-out/one-in swap — which is why the
headline total looked stable while `D1`, `D2` and `D1∩D2` were each wrong by one.

### 4.4 The revision log contradicts the correction record inside the same commit

`P11_RESEARCH_ERROR_AND_REVISION_LOG.md` `P11-E-47` states the corrected instrument

> *"re-runs at `4778792` and reproduces `D1 55 · D2 48 · D3 155 · union 212` unchanged."*

**All four figures are wrong at the head it names.** They are the figures for `92de8a1` (RUN D) — the
*pre*-correction pin. The same commit's `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md` publishes
`D1 57 · D2 49 · D3 157 · union 214`, and the regenerated `union_212.txt` contains **214** lines.

> **One commit publishes a fact and its negation in two files.**

### 4.5 Disposition

| | |
|---|---|
| **Severity** | **MATERIAL.** The CORR3 intake denominator is not reproducible: it returns **216** today and changes whenever any of ten peer branches moves. Every count derived from it inherits this |
| **Cause attribution** | P11 attributes the 212→214 move to the P09 re-pin. **That attribution is false.** The move is caused by peer branches drifting under a floating reference, of which the P09 change is one contributor |
| **Scope** | **NOT REPAIRED HERE.** The dispatch's P11 lane (§4 P11 A–E) authorises preserve, incorporate, freeze, and forbids self-discharge. It does **not** authorise re-executing P11 research, and repairing this re-opens the CORR3 `ADDRESSED`/`EXCLUDED` partitions |
| **Routed to** | **P11 owner**, as a bounded completion defect within `Q-P11-01`'s existing authority — the item's stated objective (*re-pin the moved peers*) is objectively unmet while the instrument ignores pins |
| **Independence** | **This is a controller finding, NOT `RC-02` evidence.** It was produced by the same model family that authored the repair. It is offered to `RC-02` as a lead to test, and **must not be counted as the independent challenge of `Q-P11-01`** |
| **`B-35`** | unaffected and standing — the instrument was already NOT CERTIFIED. This adds a sixth instrument defect to that record |

## 5. `CO-F-02` — P11 carries two stale inbound negatives

At `002748d`, P11 states in **two** files that P08's `Q-P08-01` notification is *"Not received"* /
*"Not yet received"*:

- `P11_AUTO_RESUME_STATE.md`:101
- `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md`:112

**P08 published `64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` at `c7cfd8a`, committed `09:05:24`** — 2 minutes
before P11's first correction commit and 4½ minutes before `002748d`.

A **second** inbound is also unconsumed: `P06_TO_P11_COUNT_CORRECTION_NOTICE.md`, published at `b5f5a21`
(`09:11:29`), after P11's last commit. P11's P06-derived figures are therefore stale by construction.

**Disposition: ROUTED to P11.** Both are receipt-side freshness defects, correctable without re-opening
research. **Neither is repaired here** — editing P11 from this session is peer-owner mutation.

## 6. What this session did NOT do

- **Ran no RC.** See `10_`. This session is Claude Opus 5; the owner corrections were authored by the
  same model. `PHASE-S/Q-BOSS-02` disqualifies it from every RC lane.
- **Discharged no veto.** All 17 stand. See `12_`.
- **Answered no Boss decision.** All 51 domain decisions stand open. See `13_`.
- **Edited no owner branch.** The six `corr/*` refs are new refs at existing commits; no owner file was
  modified from here.
- **Did not repair `CO-F-01` or `CO-F-02`**, for the scope reasons stated in §4.5 and §5.
