# 15 — RECOVERED CANONICAL BASELINE — FREEZE REGISTER

## `CHECKPOINT I — RECOVERED BASELINE FROZEN`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]` · Boss: **SOLE FINAL APPROVER**

> **This baseline is the ONLY authorized input for B-7 Round 2.**

---

## 1. Freeze evidence

| Field | Value |
|---|---|
| Session ID | `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-NEWSESSION-001]` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| **Canonical branch** | `architecture/account-phase-pretest-new-session-2026-09-10-001` |
| **Commit SHA** | **recorded in `PHASE_PRETEST_AUTO_RESUME_STATE.md` at handoff** — a document cannot contain the hash of the commit containing it (§1.1) |
| Package content freeze | this commit's `RECOVERY_2026_09_10/` tree |
| Recovery package | **`16` artefacts** — `01_`…`15_` + `16_` manifest |
| Manifest | `16_RECOVERY_MANIFEST_SHA256.txt` |
| SHA-256 verification | **executed — see §2** |
| **Competing canonical writers** | **`0`** — corrected instrument (`R-F-01`) |

### 1.1 The SHA self-reference limit, stated not fudged

**Package content is frozen at this commit's tree.** The authoritative SHA is recorded in the resume state
and in the closing report. **A baseline a reader must guess at is not frozen** — so the pointer is
explicit rather than embedded.

---

## 2. Manifest verification

Executed at freeze: `shasum -a 256 -c 16_RECOVERY_MANIFEST_SHA256.txt` → result recorded at §7.

---

## 3. Corrected Pre-Test denominator

| | |
|---|---|
| **Exit conditions** | **`7` satisfied / `13` applicable** |
| Satisfied | `1`, `2`, `5` (qualified) · `6`, `7`, `8`, `14` |
| **Surviving FAIL** | **`6`** — `3`, `4`, `13`, `15`, `16`, `17` |
| Re-placed out of the Pre-Test set | `9` `EC-04` → State · `10` `EC-07` → Module+State · `11` `E2E-04` `D`/`I` → FD Exit / Build · `12` verification → Build/Test |
| **Character** | **INSTRUMENT CORRECTION — NOT A READINESS IMPROVEMENT** |

---

## 4. All surviving blockers

### 4.1 Functional Design blockers — `5`

| # | Blocker | Owner |
|---:|---|---|
| 1 | `2` outputs + `1` orphan input remain `ORPHAN / GAP` | SMEs Core design determination |
| 2 | `O-1` — the corrected-entry link does not exist | SMEs Core |
| 3 | `O-3` — reversal after downstream consumption unrepresented | SMEs Core |
| 4 | **`4` gap-carrying handoffs outside the declared boundary set** (`B7-F-07`) | **`CORE-07`** |
| 5 | **`B4′` × `B9′`** — admitted flows travel on the excluded `XMC-H-18` (`B7-F-08`) | Architecture → Boss |

### 4.2 Obligations re-placed to later gates — `10`, none closed

`EC-04` ×3 → **State Gate** · `EC-07` ×2 → **Module + State** · `48` verification items → **Build/Test** ·
`E2E-04` `D`-limb → **FD Exit** · `E2E-04` `I`-limb → **Build/Test** · **`E2E-04` re-grade act (`G`) →
outstanding at the architecture/Pre-Test control point** (`R-F-03`).

### 4.3 SMEs Core obligations — `4`

| ID | Obligation | Status |
|---|---|---|
| `CORE-04` | map `12 ↔ 18 ↔ 10` | **PARTIAL** — `12↔18` executed; **`12↔10` underived by both parties** |
| `CORE-05` | deterministic refusal rule | **HELD** — Functional Design scope (`03_` §2.3) |
| `CORE-06` | `MF-01` counterpart account | **OPEN** |
| **`CORE-07`** | analyse `XMC-H-13`/`-14`/`-17`/`-18` **before** any `B4′` amendment is put to Boss | **OPEN — precondition ruled by Boss** |

---

## 5. Statutory / external items — `14`

| Authority | n | Note |
|---|---:|---|
| **AAS+** | `4` | incl. **`X-14`** — the `AAS-V-02` issuer discharge act, **OUTSTANDING** (reversed from *"executed"*) |
| **Thai statutory** | `4` | incl. **`POH-D-02`** — **Boss authority shall NOT substitute** |
| Business SME | `2` | — |
| PMO | `4` | incl. the `12↔10` leg |

**Vetoes: `7` canonical · `0` discharged · `AAS-V-02` NOT DISCHARGED.**

---

## 6. Lineage — preserved, nothing overwritten

| Commit | Role | Status |
|---|---|---|
| `c94839e8` | pre-B-7 handoff baseline | **Audit Lineage** |
| **`5bd36d62`** | **B-7 Round-1 immutable evidence**, branch `audit/b7-independent-2026-09-10` | **IMMUTABLE — `0` writes to the canonical path, verified vs merge-base** |
| **`8674f735`** | wrong-session execution | **PROCEDURALLY CONTAMINATED / CONTENT DISPOSITIONED** — purely additive (`2368` insertions, `0` deletions); `15` artefacts classified at `03_` |
| `94f23976` | recovery package `01_`…`13_` | superseded by this freeze |
| **this commit** | **RECOVERED CANONICAL BASELINE** | **B-7 Round-2 input** |

**`0` commits deleted · `0` history rewritten · `0` force-push · `0` evidence overwritten.**

---

## 7. `R-D-01` ruling application

| Applied | Evidence |
|---|---|
| `4` criteria re-placed | `14_` §1 |
| Arithmetic verified `7/13` | `14_` §2 — `0` removed conditions were satisfied |
| `0` evidence waived · `0` criteria satisfied · `0` runtime proof | `14_` §7 |
| Obligations preserved at downstream gates | `14_` §4 |
| **`E2E-04` `G`-limb re-registered** rather than dropped | `14_` §4.1 (`R-F-03`) |
| Non-Boss items carried as ruled | `14_` §6 |

---

## 8. Terminal state at freeze

| | |
|---|---|
| **Pre-Test** | **`HOLD PRE-TEST EXIT`** |
| Exit conditions | **`7 / 13`** — instrument correction |
| §18 answer | **`NO`** — `5` blockers |
| `EC-04` · `EC-07` | **`0/3` · `0/2`** — deferred, not discharged |
| Verification | **`0 PASS · 0 FAIL · 48 HOLD`** |
| `E2E-04` | **`NOT TRAVERSABLE`** |
| Vetoes | **`7` · `0` discharged** |
| B-7 | **Round 1 `HOLD`; Round 2 REQUIRED** |
| **Functional Design** | **NOT AUTHORIZED** |

---

## 9. Checkpoint

> ## `CHECKPOINT I — RECOVERED BASELINE FROZEN`
>
> **`16` artefacts · manifest verified · **`0` competing writers** under the corrected instrument ·
> denominator **`7 / 13`** with its *instrument-correction* character attached · `5` FD blockers ·
> `10` obligations re-placed and **`0` closed** · `4` SMEs Core obligations · `14` external items ·
> **`0` history rewritten, `0` evidence deleted, `0` lineage overwritten** ·
> **this baseline is the ONLY authorized input for B-7 Round 2.**

