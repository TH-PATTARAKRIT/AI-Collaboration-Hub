# 16_PHASE_S_BRANCH_LINEAGE_RECOVERY_REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**Branch** `audit/account-phase-s-final-closeout-2026-09-07-001`
**Authority** `PHASE-S/Q-BOSS-01` @ `1bf9b40` · `PHASE-S/Q-BOSS-02` @ `2930723`
**Classification** LAYER 2 — AUDIT QUARANTINE · Boss is Sole Final Approver

> **No history was rewritten.** No branch was force-reset, deleted or amended. Every commit named below
> still exists at the ref it was published on. The recovery is **additive**: a new immutable ref now
> names each corrected surface, so an RC challenge can be frozen against a compliant branch without
> touching the branch on which the control failure occurred.

## 1. The control conflict being recovered from

Master Phase S instructions told owners to keep owner lineage; the XRECON child prompts told each owner
`Create a NEW branch. Never push to the branch above.` **Owners followed the master instruction and
published in place**, onto the very branches named as frozen evidence surfaces. The independent verifier
recorded this as `IV-F-01 — MATERIAL CONTROL FAILURE: BRANCH ISOLATION WAS NOT OBSERVED`
(`audit/account-phase-s-independent-verification-2026-09-07-001` @ `5db35eb`).

**Attribution recorded, because it bears on culpability:** the owners were obeying a live instruction
that contradicted the child prompt. This is a **control-design defect**, not owner non-compliance. It is
contained here and is not charged against any owner.

## 2. Lineage map — old frozen SHA → in-place correction SHA → new compliant freeze

| Track | Original frozen SHA | In-place correction (preserved, not erased) | **New compliant freeze branch** | Freeze SHA |
|---|---|---|---|---|
| P06 IEV | `b423eff340cc86bbf52d2a97271f167ad9096bba` | `692ea27e11533bc72ef0123fa4d1e3524179bf6e` | `corr/p06-iev-phase-s-final-2026-09-07-001` | `692ea27e11533bc72ef0123fa4d1e3524179bf6e` |
| P06 source | `1b018c104001eb4683166518a6161a8cd8ab5cee` | `b5f5a211763568a4212d08954c835412f7728a0a` | `corr/p06-source-phase-s-final-2026-09-07-001` | `b5f5a211763568a4212d08954c835412f7728a0a` |
| P08 source | `00ccd663d55d72830c8e0db46e4cc1aa345d0af1` | `c7cfd8ae369e8c4d76dd94c64b41aab92001a9c6` | `corr/p08-phase-s-final-2026-09-07-001` | `c7cfd8ae369e8c4d76dd94c64b41aab92001a9c6` |
| P08 IEV | `bd95d1d16009a7a7d293de53848f983403e87070` | `d685176c2416210dfb67c01d862a911741530949` | `corr/p08-iev-phase-s-final-2026-09-07-001` | `d685176c2416210dfb67c01d862a911741530949` |
| P09 | `4778792196371c460d3e6ca87bf8d9adee760f47` | `2079a2594a6a76eb91bdb528f22eaf928d42c0d6` (substantive) | `corr/p09-phase-s-final-2026-09-07-001` | `2079a2594a6a76eb91bdb528f22eaf928d42c0d6` |
| P11 | `dc4cc4a6bb1ea2fac071925f5eb1c01c44072c4b` | `ce0cc2b44faf989c0a6262cf8475b4feb3a3e64f` → `002748d153b878274bf1e57f79d6070127de1ea2` | `corr/p11-phase-s-final-2026-09-07-001` | `002748d153b878274bf1e57f79d6070127de1ea2` |

**Six branches, not four.** The prompt named four. **P06 and P08 each have two distinct correction
surfaces on two different tracks (source and IEV), and `RC-03`/`RC-04` and `RC-05` challenge different
ones.** Collapsing each pair into a single branch would have left one surface of each pair unfrozen.
The deviation from the prompt's naming is recorded here rather than taken silently.

Remote read-back, executed after push:

```
692ea27e11533bc72ef0123fa4d1e3524179bf6e	corr/p06-iev-phase-s-final-2026-09-07-001
b5f5a211763568a4212d08954c835412f7728a0a	corr/p06-source-phase-s-final-2026-09-07-001
d685176c2416210dfb67c01d862a911741530949	corr/p08-iev-phase-s-final-2026-09-07-001
c7cfd8ae369e8c4d76dd94c64b41aab92001a9c6	corr/p08-phase-s-final-2026-09-07-001
2079a2594a6a76eb91bdb528f22eaf928d42c0d6	corr/p09-phase-s-final-2026-09-07-001
002748d153b878274bf1e57f79d6070127de1ea2	corr/p11-phase-s-final-2026-09-07-001
```

## 3. Two SHAs the dispatching prompt asserted were current, and are not

The prompt's §2 "VERIFIED CURRENT CONTROL SURFACES" was stale in three places. **Measured against the
remote at the start of this session, not taken on the prompt's word:**

| Prompt asserted | Remote head measured | Ancestor? | Delta |
|---|---|---|---|
| P06 source @ `1b018c1` | **`b5f5a21`** | `1b018c1` is an ancestor of `b5f5a21` | **`Q-P06-03` and `Q-P06-04` executed** — the prompt says both "remain to be completed" |
| P11 @ `ce0cc2b` | **`002748d`** | `ce0cc2b` is an ancestor of `002748d` | `Q-P11-01` sweep extended to non-`.md` carriers; **denominator moved 212 → 214** |
| P09 head `150a033` | `150a033` confirmed | `2079a25` is an ancestor | **bookkeeping only** — 2 files, manifest + resume pointer. The prompt's instruction to "treat bookkeeping-only movement separately" is **confirmed correct by measurement** |

**No prompt assertion was adopted without a remote read-back.** The two stale rows changed what work
remained: §4C and §4D of the dispatch ask for work that was already published.

## 4. Publication-time ordering — why the independent verifier's negatives are false

The IV gate report (`5db35eb`, committed `2026-09-07T09:13:13+07:00`) records:

> *"`Q-P06-03` / `Q-P06-04`: **NO EXECUTION EVIDENCE FOUND**; the P06 source branch remains at the frozen SHA."*
> and, in its §2 table, *P06 source … `1b018c1` … **UNCHANGED***.

Commit timestamps, read from the repository:

| Commit | Committed | Content |
|---|---|---|
| `002748d` P11 denominator move | `09:09:56 +07:00` | — |
| `b5f5a21` P06 `Q-P06-03`/`Q-P06-04` | **`09:11:29 +07:00`** | the evidence the IV reports as absent |
| `5db35eb` IV gate report | `09:13:13 +07:00` | asserts that evidence does not exist |

**`b5f5a21` was committed 1 minute 44 seconds before the report that says it does not exist.**

**Stated precisely, and not overstated:** a commit timestamp records when a commit was *created*, not when
it was *pushed*. Git does not record push time, so this session **cannot** prove the IV verifier could
have seen `b5f5a21` at its read moment. What is proven is narrower and sufficient:

> **Against the current remote, the IV report's two negative claims about P06 are false, and the
> remediation it derives from them (`P06-RQ-03`, `P06-RQ-04`) asks for work that is already published.**

Classified `IV-STALE-01`. **This is a `NO EVIDENCE FOUND ≠ DOES NOT EXIST` instance in the control layer
itself** — the same defect class the programme has been correcting inside the owner packages. It does not
impeach the IV verifier's independence and does not vacate `IV-F-01`, which this register acts on.

## 5. Forward rule, now binding

1. All further remediation goes on the `corr/*` branches above, or a numbered successor.
2. A surface under active RC challenge is **immutable**; its SHA must not move while the challenge runs.
3. The independent verifier publishes only on its own audit branch and mutates no owner branch.
4. **Every SHA a prompt asserts is re-read from the remote before it is relied on.** Three of this
   prompt's own assertions failed that check.
