# 04 — `RC-01` … `RC-06` INDEPENDENT VERIFIER HANDOFF MATRIX

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]` — **Claude Opus 5, disqualified from
every lane below** under `XRECON/Q-BOSS-01` (`XRD-009`).
**Verifier appointed by Boss:** ChatGPT GPT-5.6 Sol, eligibility conditional per repair/challenge pair.

> **No `RC` was run, selected or self-satisfied by this session. No disposition is issued. Every row
> is a surface to be challenged, not a result to be adopted.**

---

## 1. The matrix

| RC | Owner | Repair / correction SHA | Files / surface | Inputs | Controls published | Expected challenge action | Dependency | Status |
|---|---|---|---|---|---|---|---|---|
| **`RC-01`** | P09 | `corr/p09-phase-s-final-2026-09-07-001` @ **`2079a25`** | `OWNER_QUEUE_2026_09_07/` — `Q_P09_01_L4_AUTHORITY_RESOLUTION.md`, `Q_P09_02_CHALLENGE_SCOPE_PREPARED_NOT_RUN.md`, `LAYER2_AUDIT_QUARANTINE/q1.py`, `q1_results.json` | source root `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` **EXISTS, 13,515 `.py`**; `k1_population.json` **present, and identical in-repo** (§2) | owner-published; **not re-derived here** | Re-execute `q1.py`; **establish the deployed generation before relying on an Odoo 18 root** | none | **READY** |
| **`RC-02`** | P11 | `corr/p11-phase-s-remediation-2026-09-07-001` @ **`9d4ecdc`** *(base `002748d`)* | `P11_CO_F_01_…md`, `P11_CO_F_02_…md`, `intake_derivations_pinned.py`, `union_214_pinned.txt`, + re-stated registers | repository only — **no external input** | **8**: 6 fail-closed classes, pin-sensitivity, behaviour-preservation; 2 clean-run determinism | Test `CO-F-01`/`CO-F-02` **and** `Q-P11-01/02/03`. **Test the repair too, not only the original defect** | none | **READY** |
| **`RC-03`** | P06 IEV | `corr/p06-iev-phase-s-final-2026-09-07-001` @ **`692ea27`** | `IEV_006/P06_Q_P06_01_02_EXECUTION_RECORD.md` + 4 registers | repository only | owner-published | Test the **26** adjudication. **The naive count returns 27** — the extra member is the documented negative-control token matching its own documentation. **Validate with a second command shape** | none | **READY** |
| **`RC-04`** | P06 source | `corr/p06-source-phase-s-final-2026-09-07-001` @ **`b5f5a21`** | `G02_OWNER_CORRECTION_2026_09_07/`, incl. `P06_TO_P11_COUNT_CORRECTION_NOTICE.md` | repository only | owner-published | Test `Q-P06-03`/`-04` and the re-issued `Q-P06-02`. **The `:45` row is unrepaired at this SHA by design** and contradicts `:54` | none | **READY** |
| **`RC-05`** | P08 | `corr/p08-phase-s-rc05-prep-2026-09-07-001` @ **`e368d11`** *(base `c7cfd8a`)* | `RC05_REPRODUCIBILITY/` — instrument, prediction, 4 run logs, manifest | **4 dumps, SHA-256 published**, `/Users/admin/Downloads/`. **`pg_restore` 18.x required for `DB-T2`** | positive · negative · **graded injection** · 4 fail-closed · discriminating set · cross-version · determinism; **prediction hashed pre-execution** | Re-execute independently. **Population is FOUR databases** | **was blocked; now unblocked** | **READY** |
| **`RC-06`** | P11 | `corr/p11-phase-s-remediation-2026-09-07-001` @ **`9d4ecdc`** | `Q-P11-04` limb: `F-02` withdrawal + method-rule withdrawal | the P08 notification @ `c7cfd8a`, now **registered as received** | — | Certify the `F-02` withdrawal **after** `RC-05` establishes the P08 premise | **`RC-05`** | **BLOCKED ON `RC-05` — dependency unchanged, but `RC-05` is now executable** |
| `RC-07` | P08 IEV | `corr/p08-iev-phase-s-final-2026-09-07-001` @ `d685176` | `Q-P08-03` | — | — | **none — pointer-only** | — | **NOT REQUIRED** |

## 2. Packaging/provenance defects found and repaired — §6 of the dispatch

| Lane | Defect | Action |
|---|---|---|
| **`RC-05`** | surface carried **no executable file at all**; inputs unlocated | **repaired** — instrument, frozen inputs, SHA-256, controls published at `e368d11` |
| **`RC-05`** | population understated: `P08-U-22`'s fourth dump declared unreadable | **repaired** — readable under `pg_restore` 18.6; population is **four** databases |
| **`RC-01`** | `q1.py` reads `k1_population.json` from a **local peer session clone** — a path outside the repository that a verifier need not have | **provenance note, not a mutation.** The same file is tracked in-repo at `2079a25` under `L1_L8_BOUNDED_CORRECTION_2026_09_06/LAYER2_AUDIT_QUARANTINE/INSTRUMENTS/`, and the two are **byte-identical** (`sha256 54edc214…bbbdc569`). **The verifier should source it from the frozen ref.** P09's package was **not edited** — that would be peer-owner mutation |
| **`RC-02`** | base surface's manifest coverage assertion false (`P11-E-49`) | **repaired at the packaging level**, registered, reported |

**No moving-branch dependency remains in any lane.** Every input is either a frozen SHA or a host
file with a published SHA-256.

## 3. Leads — offered to be tested, never adopted

**Produced by the disqualified model. Each may be wrong.**

- **`CO-F-01`** — highest value. The pin is never read; the published `214` and the pin-honoured `214`
  are **different sets**. **Reproduce the one-out/one-in independently before believing it.**
- **`P11-E-47`** — its verification sentence is false at the head it names. **The defect it reported
  still stands**; do not let the withdrawal swallow the finding.
- **`P11-E-49`** — the manifest coverage assertion was carried forward. **Check whether any other
  package in this programme carries the same shape.** Not swept here — outside the remit.
- **`RC-03`'s 26 vs 27** — the naive count is wrong for a documented reason. **Use a second command
  shape**; this session lost a whole search to a `git grep` `\b` that silently matched nothing.
- **`B-29`** — P11's claim that P08's `AAS+-VETO-01` is absent from the package is **CORR2-era and
  untested here**. Adjacent to `CO-F-02`'s claim class and worth its own check.

## 4. The boundary this session kept

Verified the exact frozen SHA · reproduced with controls capable of failing · **published the two
controls that fired for the wrong reason** · preserved every superseded claim as lineage · mutated no
peer package · discharged no veto · answered no domain Boss decision · **declared no `RC` result and
no Phase S closure**.
