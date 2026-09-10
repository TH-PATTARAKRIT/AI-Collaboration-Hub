# VDR_CERTIFIED_MEASUREMENT_BASELINE.md
# No certified baseline exists — and this file records why, rather than being absent

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 11.

---

## 1. Status

> ## **NO CERTIFIED MEASUREMENT BASELINE IS CREATED BY THIS ROUND.**

§16 permits a freeze **only after instrument validation**. Validation returned **5 of 7 instruments
REJECTED** and the anti-self-reference control **FAILED**. **The precondition is not met.**

This file exists so that its emptiness is explicit. An absent baseline file and an uncreated baseline
are the same fact, and a reader is entitled to see which.

## 2. What would have been frozen, and its state

| Element | Value | Certified? |
|---------|-------|-----------|
| Population version | Hop-0 v1 — 24,553 entities | **NO** — two methods corroborate 49.5% (53.9% on a constant version basis) |
| Measurement specification version | v1 — 16 dimensions, 18 clauses each | **not independently reviewed** |
| Instrument version | v1 — 7 instruments, unchanged since first execution | **2 with limitation, 5 REJECTED** |
| Fixture version | v3 — 24 fixtures, 3 preserved runs | **the result is 24 selections of 168 verdicts** |
| Evidence baseline | 1 source tree (19.0) + 5 deployments (19.0 ×3, 18.0, 16.0) | **no version basis was declared** |
| Commit SHA | — | **withheld: a freeze would assert a certification that does not exist** |

## 3. What IS frozen, and may be relied on within its boundary

| | |
|---|---|
| **The artefacts** | every script, register and result file is committed and hashed. Nothing is unreproducible |
| **The instrument source** | unchanged since first execution, verified by an independent party |
| **The fixture expectations** | fixed before execution, verified byte-identically across three versions |
| **The evidence** | the source tree and five deployment extracts are unmodified |
| **INS-01 and INS-02** | certified **with a stated limitation**, usable only for the narrow question each answers |

**These are frozen as *artefacts*. None of them is frozen as a *certified measurement foundation*, and
the difference is the whole content of this file.**

## 4. The sequencing this round proves is not optional

> **certify the population → certify the instruments → then measure.**

Every retracted figure in this programme came from measuring before one of the first two was true. This
round attempted the second before the first and found the second failing on its own terms.

**The next round starts at step one, and this file will be written again only when both are true.**
