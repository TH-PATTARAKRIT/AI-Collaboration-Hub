# 63 — P05 AAS+ SUPPLEMENTAL VETO RECHECK

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E25`
AAS+ output is a **recommendation**. It is **not** Boss approval.

## 1. Authoritative Wording

**`AASV-01`** (`17 §4`): *"AAS+ vetoes any implementation start on P05."*
**`AASV-02`** (`17 §5`): *"AAS+ additionally vetoes citing any uncorrected section of this package as
settled input to design without a further independent pass over it. The corrected sections may be
relied on at their stated classes."*

## 2. Re-evaluation Against This Round's Evidence

### `AASV-01` — **VETO STRENGTHENED**

| Ground | Movement |
|---|---|
| Tolerance-zero boundaries | **13 of 13 open, 0 closed** — an interim closure of `TZ-01` was **withdrawn within the round** |
| Evidence base | A whole target-platform database was missing from two prior rounds (`RE-20`) |
| Finding stability | `TZ-01` now has **four positions in three rounds**, three of them published |
| Population discipline | **Nine of twenty-two** research errors are population defects; the class recurred a **third** time |
| Source-vs-deployed | `U-16` open: no source-only finding is demonstrably about deployed code |

**Strengthened, not merely upheld.** Round 2 could argue the evidence was thin. This round shows the
evidence base itself was **wrong**, twice, and that a large, correct, reproducible measurement was
taken over a population that could not answer the question asked of it. Implementing against this
package would be implementing against conclusions that have not stopped moving.

### `AASV-02` — **VETO STRENGTHENED AND WIDENED**

Round 2 drew the line at *uncorrected* sections. This round shows **corrected sections can also be
wrong** — `45` was written, corrected, and corrected again inside one round.

> **`AASV-02'` (widened):** no section of this package may be cited as settled design input unless it
> carries an **explicit evidence class** and, where it rests on database evidence, an explicit
> statement of **provenance** — who created the rows, when, and by what process. `45`'s original text
> satisfied neither and was wrong twice.

### `AASV-03` — **NEW**

> **AAS+ vetoes any reclassification of a finding's exposure that rests on a population whose
> provenance has not been established.** The controlling instance: 712 correctly-counted journal
> entries, all migration output, used to contradict a claim about live application behaviour.
> Provenance is a **precondition** of reclassification, not a footnote.

## 3. Veto Status

| Veto | Status |
|---|---|
| `AASV-01` no implementation start | **VETO STRENGTHENED** |
| `AASV-02` no uncorrected section as design input | **VETO STRENGTHENED AND WIDENED** (`AASV-02'`) |
| `AASV-03` no reclassification without provenance | **NEW — IN FORCE** |

**None closed. None narrowed. None superseded.**

## 4. What Is Safe to Rely On

| Reliance | Status |
|---|---|
| **`TX-01`** — screen/CSV divergence | **Reliable.** Predicted from source, proven structurally overdetermined by the ORM field definition, measured at 92.55% (v16) and **100.00% (v18)**, independently reproduced. The best-evidenced finding in the package. |
| Module install states across 7 registries | **Reliable** — class A within those registries, independently re-extracted |
| The source-level defect catalogue (`10`, `05`, `07`) | **Reliable as statements about the analysed source copy**; bounded by `U-16` |
| Any exposure/reach reclassification | **NOT reliable without provenance** — `AASV-03` |
| `TZ-01` in any direction | **NOT decidable** on current evidence |
| Layer 1 design input (`17 §6`) | **Reliable and Boss-decidable now** — it does not depend on any reach classification |
