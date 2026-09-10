# SC-36 — SINGLE-SESSION CANONICAL RECOVERY REGISTER

## CP-SA-SC-270 — SINGLE SESSION RECOVERY CONTROL LOCKED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` — **the only active Phase SA execution session**
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · head consumed **`e2e3f3dc`**
Prompt: `06_…CANONICAL_RECOVERY_AND_CONSTITUTIONAL_HARMONIZATION_PROMPT` (`e2e3f3dc`)
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

---

## 1. The ten mandatory controls — in force and testable

| # | Control | Compliance, verifiable |
|---:|---|---|
| 1 | No new Phase SA session | **`0`** opened |
| 2 | No parallel write track | all writes on this branch only |
| 3 | No second executor on this branch | **verified at §3** — no commits by another executor since `093585d0` |
| 4 | No peer historical branch mutation | peer branches opened **read-only**; `0` writes |
| 5 | **No force-push to hide collision lineage** | **`0` force-pushes this session.** Three rejected pushes were resolved by rebase, never by force |
| 6 | No recency-as-authority shortcut | applied and **refused** at `SC-39` |
| 7 | No stricter-reading-is-better shortcut | applied and **refused** at `SC-39` |
| 8 | No gate-opening-is-better shortcut | **the sharpest control this round** — `SC-40`'s harmonization lands in the gate-opening direction and is therefore routed to Boss, not adopted |
| 9 | Scan for new Boss instruction before every checkpoint | executed — §3 |
| 10 | All corrections land only on this branch | this commit |

---

## 2. Procedural quarantine authorized, substantive choice withheld

**`06_` §0 authorizes *procedural quarantine* of collision-tainted authority records. It expressly does not
authorize SMEs Core to choose Boss's substantive policy.**

**Both are honoured, and the distinction is applied literally:**

| Act | Authorized? | Done? |
|---|---|---|
| Mark `SC-BD-01` and `SC-CONTRA-01` as collision-tainted, unsafe as prospective tiebreakers | **YES — procedural** | **YES**, `SC-38` |
| Preserve both records intact | **required** | **YES** — byte-identical, verified |
| Classify the 16 downstream rulings as *substantive ruling exists / gate-precondition pending* | **YES — procedural** | **YES**, `SC-38` |
| **Choose Reading A or Reading B** | **NO — substantive** | **NOT DONE** |
| **Declare the 16 void, or safe** | **NO — substantive** | **NOT DONE** |
| Re-derive `FG-F-06` from primary text and recommend | **YES** | **YES**, `SC-39`, `SC-40` — **and routed to Boss as `SC-AUTH-02`** |

---

## 3. Control 9 executed — new-instruction scan

| Record after the previous baseline `093585d0` | Author | Classification |
|---|---|---|
| **`e2e3f3dc`** — the `06_` recovery prompt | **Boss** | **CONTROLLING INSTRUCTION.** Ingested; this round executes it |

**Commits by any other executor since `093585d0`: `0`.** The single-session lock is holding in practice, not
only on paper — this is the first round in this session with **no** concurrent writer.

---

## 4. Collision-recovery status carried forward

| Class | Status |
|---|---|
| `COL-01` identifier collision | **CLOSED** — the collided package is quarantined at `PARALLEL_EXECUTION_SUPERSEDED_2026_09_10/`; `0` renames into live series |
| `COL-02` **authority collision** | **OPEN — the subject of this round.** Quarantined `SC-38`; re-derived `SC-39`; routed `SC-AUTH-02` |
| `COL-03` instruction drift | **CLOSED by the lock** — `1` Boss instruction this round, `0` mid-execution arrivals |
| `COL-04` late detection | **CLOSED at source** by Boss's lock |

**Prevention controls `P1`–`P6` remain in force.** `P2` (fetch before start **and** immediately before every
push) is executed twice per round and is what detected `e2e3f3dc`.

---

## 5. Peer-artefact integrity

**Every pre-existing artefact byte-identical**, verified per blob before and after this commit; result
published at `SC-46` §2. **`0` modified across the entire session, through three rebases and three rejected
pushes.**

---

## 6. Checkpoint

> ## `CP-SA-SC-270 — SINGLE SESSION RECOVERY CONTROL LOCKED`
> **10 of 10 controls in force and testable · **`0` force-pushes**, `0` peer mutations, `0` concurrent
> writers this round — the first clean round of the session · procedural quarantine authorized and
> exercised; **substantive choice withheld** · control 9 found `1` new Boss instruction, ingested ·
> 4 collision classes tracked, `3` closed, `1` open and being worked.**

No Evidence = No Progress. Never Skip Gate. Procedural quarantine is not a substantive ruling.
Boss remains the sole Final Approver.
