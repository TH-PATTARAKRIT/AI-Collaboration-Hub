# 10_FRESH_CHALLENGE_RESULT_REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**Governing authority** `PHASE-S/Q-BOSS-02 = APPROVED` @ `2930723` — structural independence defined
**Prior ruling** `XRECON/Q-BOSS-01` (`XRD-009`) = **NOT SATISFIED** — same-model verification of a repair
is not structural independence

## 1. Result: **NO RC IS COMPLETE. NO RC WAS RUN BY THIS SESSION.**

`PHASE-S/Q-BOSS-02` requires a qualifying verifier to satisfy **all** of: model/agent separation,
appointment independence, isolated session, frozen evidence surface, read-only boundary, independent
reproduction, independent publication, no owner mutation, no self-discharge, no self-pass.

**This session is Claude Opus 5. The P06/P08/P09/P11 owner corrections under challenge were authored and
executed by the same model.** The first criterion — model/agent separation — fails at the outset. Under
dispatch §5 this session therefore **stopped the RC execution lane only** and continued every other
non-blocked task.

> **This session issues no `SUPPORTED` / `CONTRADICTED` / `NARROWED` / `MISSING EVIDENCE` disposition on
> any owner finding.** Doing so would be the self-pass that `XRD-009` already ruled out.

## 2. RC status — six lanes

| RC | Surface, frozen and immutable | Status | Blocking reason |
|---|---|---|---|
| `RC-01` | P09 six-correction surface · `corr/p09-phase-s-final-2026-09-07-001` @ `2079a25` | **READY — AWAITING INDEPENDENT VERIFIER** | No eligible verifier has run it. **Inputs confirmed present on host (§4)** |
| `RC-02` | P11 `Q-P11-01/02/03` · `corr/p11-phase-s-final-2026-09-07-001` @ `002748d` | **READY — AWAITING VERIFIER; CARRIES A MATERIAL LEAD** | `CO-F-01` must be tested by `RC-02`, not accepted from this session |
| `RC-03` | P06 IEV totals · `corr/p06-iev-phase-s-final-2026-09-07-001` @ `692ea27` | **READY — AWAITING VERIFIER** | The IV's prior `BLOCKED` reason (25-vs-26 unstable) **is now resolved: adjudicated 26**, `09_` §2 |
| `RC-04` | P06 source · `corr/p06-source-phase-s-final-2026-09-07-001` @ `b5f5a21` | **READY — AWAITING VERIFIER** | The IV's prior `NOT READY` reason (*"surface does not exist"*) **is false against the remote** — `16_` §4. Surface exists and is frozen |
| `RC-05` | P08 source · `corr/p08-phase-s-final-2026-09-07-001` @ `c7cfd8a` | **HOLD — REQUIRED PRIMARY EVIDENCE NOT ESTABLISHED** | §3 |
| `RC-06` | P11 `Q-P11-04` · `corr/p11-phase-s-final-2026-09-07-001` @ `002748d` | **BLOCKED ON `RC-05`** | Its subject is the withdrawal of a falsification built on P08's figure; certifying it requires the P08 premise established under `RC-05` |
| `RC-07` | P08 IEV `Q-P08-03` · `corr/p08-iev-…` @ `d685176` | **NOT REQUIRED** | Pointer-only under the queue; no fresh challenge mandated |

**Four of six lanes are ready and unblocked** — `RC-01`, `RC-02`, `RC-03`, `RC-04`. Two prior blockers
(`RC-03`'s and `RC-04`'s) were cleared by this session's work and by remote read-back respectively.

## 3. `RC-05` — the one genuine evidence unavailability

The IV verifier recorded that it *"cannot independently re-execute the exact-arithmetic database result
from the currently accessible evidence"*, having no authorized Remote Desktop device.

**What `RC-05` requires and what has not been established:**

| Required by `PHASE-S/Q-BOSS-02` §6 (independent reproduction) | Established? |
|---|---|
| An independently executable exact-arithmetic instrument | **NOT ESTABLISHED** — no script published on the P08 correction surface |
| Frozen input/extract location for the balance measurement | **NOT ESTABLISHED** |
| Population identity for `DB-SM` / `DB-BK` / `DB-EV` | **NOT ESTABLISHED** on the frozen surface |
| Outputs at exact / `1e-7` / `1e-4` / `0.005`, computed **and** stored balance | published as **prose figures**, not as a re-executable result |
| A discriminating positive control | **NOT ESTABLISHED** |

**This session did not attempt to close this gap by locating the databases itself.** Doing so would be
independent reproduction — `RC-05` work — barred by §5. **The requirement is specified in `17_` so the
appointed verifier can execute it.**

**Recorded against this session's own standing rule** (`evidence-at-rest`, `PATH SET for runtime
evidence`): *"required primary evidence unavailable" is a claim about the evidence base and needs its own
authority.* **This session asserts only that the P08 correction surface does not carry the instrument and
inputs `RC-05` needs. It does NOT assert that the underlying database evidence is absent from the host** —
that negative has not been tested here and must not be inferred from this row.

## 4. `RC-01` reproducibility — a narrow positive finding

P09's `Q-P09-01` instrument `OWNER_QUEUE_2026_09_07/LAYER2_AUDIT_QUARANTINE/q1.py` reads two host paths
outside the repository. Both were checked for **existence only**:

```
source root  /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons
             EXISTS · 13,515 .py files (excluding __pycache__)
input        …/L1_L8_BOUNDED_CORRECTION_2026_09_06/LAYER2_AUDIT_QUARANTINE/INSTRUMENTS/
             EXISTS · k1_population.json PRESENT
```

**Deliberately not done: the instrument was not executed and its numbers were not reproduced.** That is
`RC-01`'s work. This row establishes only that **`RC-01` is not evidence-blocked** — unlike `RC-05` — so
the appointed verifier can begin it immediately.

**A version-basis caveat the verifier must resolve, not inherit:** `q1.py` reads an **Odoo 18** tree. This
programme has previously recorded P09 deployments running other generations. **`RC-01` must establish the
deployed version before relying on that root.** This session does not decide it.

## 5. Findings produced by this session, and their correct standing

| Id | Finding | Standing |
|---|---|---|
| `CO-F-01` | P11's re-pin is behaviourally inert; the CORR3 denominator is floating-head, non-deterministic, and its published `D1`/`D2`/`D1∩D2` are wrong by one | **CONTROLLER FINDING — a lead for `RC-02`. NOT independent challenge evidence** |
| `CO-F-02` | P11 carries two stale inbound negatives (P08 notification, P06 count notice) | **CONTROLLER FINDING — routed to P11** |
| `XQ-R-02` | P06 material-defect denominator adjudicated at **26** | **CONTROLLER ADJUDICATION — subject to `RC-03`** |
| `XQ-R-01` | `Q-P06-02` re-issued against the correct source-track artefact | **QUEUE CORRECTION — its challenge is `RC-04`** |
| `IV-STALE-01` | Two IV negative claims about P06 are false against the remote | **CONTROLLER FINDING — does not impeach IV independence; `IV-F-01` stands and was acted on** |

**None of these is an RC disposition, and none may be counted toward one.** Each was produced by a
model that is disqualified from challenging these repairs. They are published so the independent
verifier can test them — including the possibility that they are wrong.
