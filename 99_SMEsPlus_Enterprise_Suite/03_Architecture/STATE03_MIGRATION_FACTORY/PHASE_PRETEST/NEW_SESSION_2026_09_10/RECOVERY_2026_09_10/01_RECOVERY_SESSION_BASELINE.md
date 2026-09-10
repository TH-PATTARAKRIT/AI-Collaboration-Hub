# 01 — RECOVERY SESSION BASELINE

## `CHECKPOINT A — CANONICAL INPUTS AND LINEAGE VERIFIED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]`
Canonical session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`0` Phase SA restarts · `0` research restarts · `0` evidence deleted · `0` history rewritten.**

---

## 1. Lineage — verified, not assumed

| Commit | Type | Session | Verified |
|---|---|---|---|
| `c94839e8` | commit | `BOSS-RESOLUTION-001` — my handoff baseline | **RESOLVES** |
| **`5bd36d62`** | commit | **`B7-INDEPENDENT-001`** — independent verdict | **RESOLVES**, on `origin/audit/b7-independent-2026-09-10` |
| **`8674f735`** | commit | **`B7-RETURN-CORR1-001`** — wrong-session execution | **RESOLVES**, canonical branch head |
| `172d7b9c`, `88003079`, `8af573f2` | commits | prior baselines | **ALL RESOLVE — none overwritten** |

**History integrity:** the canonical branch is **strictly linear** `c94839e8 → 8674f735`. **`0` force-push,
`0` rebase, `0` deletion.**

---

## 2. The two governance facts that decide how `8674f735` is treated

### 2.1 It is purely additive

```
$ git show --stat --format='' 8674f735
  16 files changed, 2368 insertions(+)
```

**`0` deletions. `0` modifications to pre-existing evidence** except `PHASE_PRETEST_AUTO_RESUME_STATE.md`,
which gained `57` lines and lost none.

> **The procedural contamination is in WHERE it was executed, not in WHAT it did to the record.**
> Nothing was overwritten, so nothing needs undoing — only verifying.

### 2.2 B-7 respected read-only, exactly

```
$ git show --stat --format='' 5bd36d62
  .../B7_INDEPENDENT_CHALLENGE_VERDICT.md | 429 +++++++++++++++++++++
  1 file changed, 429 insertions(+)
$ git show --stat --format='' 5bd36d62 -- '.../PHASE_PRETEST'   →   0 lines
```

**`1` file, `429` insertions, published to `INDEPENDENT_REVIEW/B7_PHASE_PRETEST_2026_09_10/` — its own
channel. `0` writes to the challenged tree.** B-7 also ran a **positive control on my manifest checker**
(appended one byte to `01_`, confirmed `FAILED`, restored, `24 OK`).

> **The independence controls held. The procedural failure is downstream of B-7, not inside it.**

---

## 3. Classification of `8674f735`

| | |
|---|---|
| **Status** | **`PROCEDURALLY CONTAMINATED · CONTENT PENDING INDEPENDENT CANONICAL RE-VERIFICATION`** |
| Preserved as | **PROCEDURAL AUDIT LINEAGE** |
| Deleted / reset / amended | **`0`** |
| Auto-accepted | **NO** |
| Auto-rejected | **NO** |
| Disposition method | **per-artefact**, `03_` |

**Why contamination matters even though the content may be sound:** the corrective round was executed
**inside the B-7 conversation**, so its author held the challenger's context. **A corrective round that
can see the challenger's reasoning is not independent of it** — and its conclusions may be shaped by that
context in ways neither party can detect from the artefacts alone. **This is why every conclusion is
re-verified here rather than adopted.**

---

## 4. Evidence hierarchy used by this session

| Rank | Source | Use |
|---:|---|---|
| 1 | **Primary Phase SA evidence** (`SC-*`, `SA_*`) | authoritative |
| 2 | **Boss rulings** | authoritative |
| 3 | **B-7 Round-1 immutable evidence** (`5bd36d62`) | independent finding — **verified before adoption** |
| 4 | Original Pre-Test package (`PT-00`…`25_`) | prior conclusion — **not evidence about itself** |
| 5 | **Wrong-session artefacts (`26_`…`39_`)** | **CANDIDATE CONCLUSIONS ONLY** |
| — | chat-only reasoning, wrong-session memory, executor self-certification | **NOT USED** |

---

## 5. Intake state — reproduced

| Control | Value |
|---|---|
| Pre-Test posture | **`HOLD PRE-TEST EXIT`** |
| B-7 Round 1 | **executed · verdict `HOLD` · `12/12` targets · `6` successful falsifications · `18` findings** |
| `EC-04` · `EC-07` | **`0/3` · `0/2`** |
| Verification | **`0 PASS · 0 FAIL · 48 HOLD`** |
| `E2E-04` | **`NOT TRAVERSABLE`** |
| Vetoes | **`7` canonical · `0` discharged** |
| Writer collision | **`1` of `193` branches** |

---

## 6. Checkpoint

> ## `CHECKPOINT A — LINEAGE VERIFIED`
>
> **`6` commits resolve · history **strictly linear**, `0` rewrites · `8674f735` is **purely additive**
> (`2368` insertions, `0` deletions) and is classified **PROCEDURALLY CONTAMINATED / CONTENT PENDING** ·
> B-7 wrote `0` bytes to the challenged tree and ran a positive control on my own manifest checker ·
> **`5`-rank evidence hierarchy declared, with wrong-session artefacts admitted as CANDIDATES ONLY.**

