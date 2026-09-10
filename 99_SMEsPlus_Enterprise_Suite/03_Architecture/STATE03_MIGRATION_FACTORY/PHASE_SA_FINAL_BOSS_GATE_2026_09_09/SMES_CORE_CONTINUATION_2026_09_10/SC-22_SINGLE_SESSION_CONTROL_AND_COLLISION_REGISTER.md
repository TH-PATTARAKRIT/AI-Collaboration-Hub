# SC-22 — SINGLE-SESSION CONTROL AND COLLISION REGISTER

## CP-SA-SC-160 — SINGLE-SESSION CONTROL LOCKED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` — **the only active Phase SA execution session**
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · head consumed **`2cfb57eb`**
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

---

## 1. The lock

> **This session is the ONLY active Phase SA execution session.** All other Phase SA sessions, branches,
> prompts and packages are **`READ-ONLY EVIDENCE / AUDIT LINEAGE / PRIOR AUTHORITY RECORDS`** unless Boss
> explicitly reactivates one.

**All eight mandatory controls are in force and are testable:**

| # | Control | How this session complies, verifiably |
|---:|---|---|
| 1 | No other Phase SA execution session opened | **0** opened. No `Agent`/subagent write track exists |
| 2 | No parallel Phase SA write track | All writes land on this branch only |
| 3 | No peer historical branch modified | The AR branch and every peer branch opened **read-only**; `0` writes |
| 4 | A later peer record is not automatically controlling | §4 — applied to `SC-BD-01` vs `SC-CONTRA-01` and **explicitly refused** as a tiebreaker |
| 5 | Reconcile by primary text, intent, scope, chronology, supersession — never timestamp alone | `SC-24` |
| 6 | New artefacts only on this execution branch | this commit |
| 7 | Scan for post-baseline Boss authority records before every checkpoint | §3 — **executed, and it found two** |
| 8 | Durable collision register | §2 |

---

## 2. Collision register — the concurrency defect, recorded so it cannot recur silently

### 2.1 What happened

**Two executions of one session identifier ran concurrently on one branch for roughly six hours.**

| Time (+0700) | Commit | Actor | Event |
|---|---|---|---|
| 02:18:06 | `6d08bcc5` | Boss | `03_` gate prompt added — `REQUIRED STOP #1` at `FG-F-06` |
| 02:24:53 | `7eeb5d8e` | **Executor 2** | `SC-ADDENDUM-A` — first discovery of the concurrency, **found only by a rejected push** |
| ~02:25 | — | **Boss → Executor 2** | **`FG-F-06 = READING A`** (issuance head `7eeb5d8e`) |
| 07:53:13 | `e113258f` | **Executor 1** | `SC-BD-01` — **`FG-F-06 = READING B`** (issuance head **`6d08bcc5`**) |
| 08:14:26 | `89ba9c7d` | Executor 1 | `SC-BD-02`…`SC-BD-10` — **16 of 23 ruled** — `SC-11`, `SC-12`, `TERMINAL D` |
| 08:21:29 | `a8c7054f` | Boss | `04_` gap-remediation prompt (Reading B path) |
| 08:23:35 | `ce987553` | **Executor 2** | `SC-CONTRA-01` — the contradiction surfaced |
| 08:37:13 | `dfea73b7` | Executor 1 | `SC-13`…`SC-21` — gap closed, **`TERMINAL D`, `EC-05` open, contradiction acknowledged by both** |
| 08:49:43 | `2cfb57eb` | **Boss** | **`05_` — single-session lock. The defect is closed at source** |

### 2.2 Defect classes recorded

| ID | Class | Statement |
|---|---|---|
| **`COL-01`** | **Identifier collision** | Both executions authored `SC-08`/`SC-09`/`SC-10` with different content; `SC-BD-02` was taken for `F4_BOSS_RULING` while Executor 2 was writing `SC-BD-02` for the `FG-F-06` ruling. **Resolved by renaming Executor 2's file to `SC-CONTRA-01` and quarantining its earlier package — never by overwriting** |
| **`COL-02`** | **Authority collision** | **The severe one.** Two opposed Boss rulings on `FG-F-06`, each issued into a context where the other did not exist (`SC-23` claim 6, proven). **16 downstream rulings rest on one of them** |
| **`COL-03`** | **Instruction drift under the executor** | Four Boss prompts (`02_`, `03_`, `04_`, `05_`) landed on the branch *during* execution. **A cited baseline is a floor, not a ceiling** |
| **`COL-04`** | **Late detection** | The concurrency was detected only by a **rejected push**, ~6 hours after both executions began |

### 2.3 Root cause

> **A session identifier names a line of work. It is not a lock on a branch.** Nothing in the prompt chain
> prevented a second executor from taking the same prompt, and nothing surfaced the first executor's
> existence to the second until git refused a write.

### 2.4 Prevention controls — now in force

| # | Control | Status |
|---|---|---|
| P1 | **Boss single-session lock** | **IN FORCE** — `05_` §0. **This is the control that actually closes `COL-04`**, and it is Boss's act, not SMEs Core's |
| P2 | Fetch the branch head **before starting** and **again immediately before every push** | in force this round — it found `dfea73b7` and `2cfb57eb` |
| P3 | List the remote directory before minting any numbered identifier | in force — this file's number checked against the live tree |
| P4 | On collision: **never force, never renumber into a live/reserved series, never modify peer artefacts** | applied at `COL-01` |
| P5 | Scan for Boss authority records newer than the cited baseline before every checkpoint | §3 |
| P6 | Verify byte-identity of every peer artefact before and after each commit, and publish the result | §5 |

---

## 3. Control 7 executed — post-baseline Boss authority scan

**Baseline cited by the `05_` prompt: `dfea73b7`. Live head at ingestion: `2cfb57eb`.**

| Record found after the cited baseline | Author | Classification |
|---|---|---|
| **`2cfb57eb`** — `05_PHASE_SA_SINGLE_SESSION_COLLISION_RESOLUTION_AND_EXIT_PATH_PROMPT` | **Boss** | **CONTROLLING INSTRUCTION for this round.** Ingested; this file executes it |
| `dfea73b7` — `SC-13`…`SC-21` | Executor 1 | **READ-ONLY EVIDENCE.** Ingested and reproduced at `SC-23` |

**Boss authority records selecting an `FG-F-06` reading, created after both alternatives were on the
record: `0`** — measured at `SC-24` §3, with a firing positive control.

---

## 4. Control 4 applied — recency is refused as a tiebreaker

**`SC-CONTRA-01` (Reading A) was issued against a strictly later head than `SC-BD-01` (Reading B)** —
`7eeb5d8e` (02:24:53) vs `6d08bcc5` (02:18:06).

> **This session does not treat that as controlling.** A later issuance head is evidence about **the state
> of the branch when a record was written**, not about **which instruction Boss intends to stand**.
> Control 4 forbids it, and `CF-D-01` reserves the question: *"only Boss may state what a Boss ruling
> covers."* **Reconciliation is performed on primary text, intent, scope and supersession at `SC-24`.**

---

## 5. Peer-artefact integrity — measured, not asserted

**Every artefact authored by Executor 1 is byte-identical between `dfea73b7` and this commit.**
Verified per file by blob id; result published at `SC-31` §2. **`0` peer artefacts modified across this
entire session, including under two rebases and three rejected-push recoveries.**

---

## 6. Checkpoint

> ## `CP-SA-SC-160 — SINGLE-SESSION CONTROL LOCKED`
> **8 of 8 mandatory controls in force and testable · 4 collision classes registered with root cause ·
> 6 prevention controls, the decisive one being Boss's own single-session lock · control 7 executed and it
> found 2 post-baseline records, both ingested and classified · **`0` explicit Boss supersessions of an
> `FG-F-06` reading** · control 4 applied: recency **refused** as a tiebreaker · `0` peer artefacts
> modified.**

No Evidence = No Progress. Never Skip Gate. A session identifier is not a lock.
Boss remains the sole Final Approver.
