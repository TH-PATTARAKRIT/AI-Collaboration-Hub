# 03 — `RC-02` (P11) — INDEPENDENT CHALLENGE

**Verifier session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]` · branch `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Executing model:** Claude Opus 5 · **Appointed verifier:** ChatGPT GPT-5.6 Sol

## 1. Exact scope restated before testing (§4.A)

Bounded to `corr/p11-phase-s-remediation-2026-09-07-001` @ `9d4ecdc` (base `002748d`):
`P11_CO_F_01_…md`, `P11_CO_F_02_…md`, `intake_derivations_pinned.py`, `union_214_pinned.txt`
and the re-stated registers. Inputs: **repository only, no external input.**
Scope covers `CO-F-01`, `CO-F-02` **and** `Q-P11-01`/`-02`/`-03`.

## 2. Result

```
RC-02 = RC-HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN
```

**Reason:** `Q-BOSS-02` §1 controls 1 and 2 fail for this executor. The repair at `9d4ecdc` carries
`Co-Authored-By: Claude Opus 5`. Per `Q-BOSS-01` §2, a challenge run by the model that authored the
repair does not satisfy `RC-*`. **No falsification attempted; see `00_` §3.**

## 3. Readiness verified (does NOT certify this RC)

| Check | Result |
|---|---|
| Frozen ref head == asserted SHA | `corr/p11-phase-s-remediation-2026-09-07-001` = `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c` — **MATCH** |
| Base ref present | `corr/p11-phase-s-final-2026-09-07-001` = `002748d153b878274bf1e57f79d6070127de1ea2` — present, **not rewritten** |
| `CO-F-01` / `CO-F-02` corrections included at this SHA | **YES** — the remediation commit message states both were repaired at `9d4ecdc`; this satisfies the §3 sequencing precondition that `RC-02` run only after those corrections land |
| External inputs required | **none** — the surface is repository-only, so no host-evidence blocker applies |
| Owner-published controls | **8** claimed: 6 fail-closed classes, pin-sensitivity, behaviour-preservation, plus 2 clean-run determinism. **Count read from the matrix; not re-derived** |

### 3.1 Declared surface ≠ changed surface — `IV-R-01/RC-02`, **MATERIAL**

The matrix declares four named files *"+ re-stated registers"* — an **open-ended phrase, not a set**.
`git show --name-only 9d4ecdc` changes **ten**.

| Named (4) | Covered only by "+ re-stated registers" (6) |
|---|---|
| `P11_CO_F_01_PIN_INSTRUMENT_REPAIR.md` | `00_README_PACKAGE_INDEX.md` |
| `P11_CO_F_02_STALE_INBOUND_REPAIR.md` | `P11_AUTO_RESUME_STATE.md` |
| `LAYER2_P11_EVIDENCE/corr3_instrument/intake_derivations_pinned.py` | `P11_CHECKPOINT_REGISTER.md` |
| `LAYER2_P11_EVIDENCE/corr3_instrument/union_214_pinned.txt` | `P11_EVIDENCE_MANIFEST.md` |
| | `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md` |
| | `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` |

**Only 2 of the 6 are named `*REGISTER*`.** The other four — a package index, a resume state, an
**evidence manifest**, and a **revision log** — are not registers on any reading, so the phrase does
not in fact cover the set it is standing in for.

**Why it is material here specifically:** `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` is a revision log,
and **a revision log is not a correction** — a corrected register and a log saying it was corrected
are two different claims, and this programme has already shipped accepted findings that were logged
and never edited in. `P11_EVIDENCE_MANIFEST.md` is the artefact `P11-E-49` was raised against.
**Both changed at this SHA and neither is named.**

**One instance of `IV-R-01`, measured in all five lanes in `07_` §3.** The check **fires in all five**,
including `RC-05`, so it has **no passing control** and is weak as a discriminator; `07_` §3 therefore
ranks the lanes **by magnitude** rather than treating them alike. This session does not call
`RC-05`'s single-file miss material.

## 4. Findings

**None issued.** Absence of findings is absence of testing. Under §2.10 it may not be read as a
discharge of anything.

## 5. What the appointed verifier must still do

Test the **repair**, not only the original defect — the handoff row says so in terms. Prove the
repaired instrument **consumes the immutable pins** and **can fail when a pin or control is changed**;
the owner's own claim is that the pin's non-reading was proven by changing it and getting byte-identical
output, so the mirror test is the one that matters. Reproduce `CO-F-01`'s **one-out/one-in** claim
independently: both unions hold 214 members but are **different sets**, so the equal cardinality
concealed a substitution — **member identity, not count**. Note also that the owner's control set is
owner-selected here, which `AASP-P11-C3-VETO-04` (*no control set drawn by the party it controls*)
directly engages: **draw an independent control set.**
