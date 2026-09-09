# SA_CORR3_00 — DECISION RECLASSIFICATION AND DECLARED FRAME
## CP-SA-C3-00 — DECISIONS RECLASSIFIED BEFORE ESCALATION

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `architecture/phase-sa-corr3-proof-verification-2026-09-09-001`
Master prompt commit: `5953ce26` · Parent CORR2 publication commit: `990f915e`
Boss: **SOLE FINAL APPROVER**

---

## 1. What this register does

Master prompt §3 orders every requested decision and blocker in the CORR2 Boss pack to be
re-classified **without preserving the previous Boss-decision classification by default**, into
exactly one of:

`A` SMEs Core can resolve — study/proof required · `B` Governance correction — no Boss decision
required · `C` Structural independence action required · `D` Genuine Boss policy/authority decision
after proof.

**Result: of CORR2's four requested decisions and seven blockers, `0` survive in the form they were
put. Two Boss elections survive on new, narrower grounds, and four items previously carried as
research or design are now closed.**

---

## 2. `CORR3-FRAME` — the declared measurement frame, cited by every artifact in this package

| Clause | Declaration |
|---|---|
| **POPULATION** | Every branch on remote `origin` at fetch 2026-09-09. **n = 184.** Three command shapes agree: `for-each-ref` filtered `^origin/.`, `ls-remote --heads`, `branch -r`. *(CORR2 measured 183; the delta is the control branch created for this round.)* |
| **PATH SET** | **Every path in the tree of every branch head, union the `origin/SMEsPlus` tree.** A **superset** of CORR2's v2 frame — see `C3-I-01` |
| **UNIT** | **U1** = **3,900** unique text blobs. **U2** = **3,579** unique text paths. Never conflated; every count states which |
| **EXTRACTION COVERAGE** | requested 3,900 / written 3,900 / **missing 0** / **zero-byte 0** |
| **POSITIVE CONTROLS** | `BD-ACC-01` → **55** blobs · `clean.room` (-i) → **1,266** blobs. Both fire |
| **NEGATIVE CONTROL** | `qxvz7481_no_such_token` → **0** — a token never previously written into the corpus (`C3-I-02`) |
| **INJECTION CONTROL** | one matching blob injected, re-queried, removed: **0 → 1 → 0**. The predicate can fire, not merely the extractor |
| **COMPLEMENT, stated** | Blobs reachable **only from non-head history commits**, and **all non-`.md`/`.txt`/`.csv` files.** Runtime artefacts on the execution host are outside this frame and are **not asserted absent** — `SA_CORR3_02` reaches four of them under its own declared instrument |

### 2.1 `C3-I-01` — CORR2's corrected frame still had a non-empty complement, and it was governance

CORR2's `C2-I-02` corrected the parent's PATH SET by adding the mainline tree, and stated the rule it
had paid for: **a population is only declared when its complement is stated.** Applying that rule to
CORR2's own v2 declaration:

```
v2 PATH SET  = per-branch merge-base diff  UNION  origin/SMEsPlus tree
complement   = a blob a branch inherited UNCHANGED from a merge-base that
               mainline later revised or deleted
               -> invisible to clause (a) by construction, absent from clause (b)
measured     = 81 text blobs / 57 distinct paths
```

**All 57 are governance artefacts** — including `PROJECT_CONSTITUTION.md`, `APPROVAL_AUTHORITY_MATRIX.md`,
`AI_ROLE_AND_RESPONSIBILITY.md`, `GLOBAL_CHALLENGE_CONTINUITY_LEDGER.md` and the core-team charter.

> **This is the same defect class as `C2-I-02`, one rung further out**, and it is the reason `C3-G-06`
> (a constitution existing in two versions across the population) was invisible to every prior round.
> **CORR3 therefore adopts the full head-tree union and states its own complement above.**

### 2.2 Instrument defects found in this round's own frame, published

| id | Defect | How it was caught |
|---|---|---|
| — | **`git diff --raw` abbreviates blob SHAs to 8 characters** while `ls-tree` gives 40. A union of the two **deduplicates across incompatible key widths** | **The set difference disagreed with the arithmetic** (`comm` returned 2,859 where subtraction demanded 79). Not by inspection. **Always cross-check a set operation against its own subtraction** |
| `C3-I-02` | **A published negative-control token is single-use.** CORR2's token returns **3** in this frame, and all three hits are the registers **documenting the control** | Re-running the inherited control instead of assuming it |
| — | The query tool is **case-insensitive unless forced**: `COSO` returns **7** case-sensitive, **32** case-insensitive | Reproducing CORR2's recorded warning rather than trusting it |
| — | `grep` here is **ugrep**: bounded-repetition context patterns over UTF-8 **fail loudly but partially** | A context extraction errored while the blob list was correct |

---

## 3. Reclassification of CORR2's four requested decisions

| CORR2 item | CORR2 class | **CORR3 class after proof** | Basis |
|---|---|---|---|
| **Decision 1 — `XD-01`** with its durability precondition | `D` | **`A` — RESOLVED** | `SA_CORR3_01`. The precondition's second clause is **already answered by a published SMEsPlus baseline neither Phase SA nor CORR2 opened** (`0 of 38` files, positive control **28**). CORR2's own package says three times out of four that this is **not a Boss question**. **One residual policy election survives on a new ground** — `XD1-P1`, §5 |
| **Decision 2 — `C2-D-03`** kit vs component category | `D` | **`A` — RESOLVED. 0 Boss decisions** | `SA_CORR3_02`. **12 of 16 cases resolve by quoting the existing ruling; 3 cannot arise; 0 genuine policy gaps.** CORR2's *"no research resolves it"* is **falsified** — and was itself an unevidenced claim about the evidence base |
| **Decision 3(a) — compliance overclaim** | `D` | **`B` — EXECUTED** | `SA_CORR3_05`. The remedy is **prescribed by two standing Boss decisions**; executing a prescribed remedy is not a new decision. **Corrected on this branch** |
| **Decision 3(b) — verdict-vocabulary contradiction** | `D` | **`B` — DISSOLVED. No contradiction exists** | `SA_CORR3_05` §4. The Enterprise Constitution holds *"AI must not approve itself"* and *"AI must return PASS / HOLD / FAIL / FROZEN"* as **items 4 and 7 of one enumerated list.** And CORR2's second horn **conflated two senses of "certification"** |
| **Decision 4 — `BLK-07`** normal capacity, gating two absent mechanisms | `D` | **`A` mostly; `D` for a narrow residue** | `SA_CORR3_03`, `SA_CORR3_04`. The **destination** of unabsorbed overhead is **already CLOSED by `BD-02`**; the **basis** is settled in the owning register, **which rejects the alternative by name in its own *Rejected* table**; the **existence of a mechanism** was never a policy question. **11 of 12 maintenance routes do not need it**, and the part that is gated is gated by **`BLK-08`, which Decision 4 does not name** |

---

## 4. Reclassification of CORR2's seven blockers

| # | CORR2 blocker | CORR2 owner | **CORR3 disposition** |
|---|---|---|---|
| 1 | Handoff element 10 as a *guarantee* — *"blocks all 22 on its own"* | Development / Pre-Test | **PARTIALLY FALSIFIED.** Element 10 is **sufficient but not necessary**: element 15 is **equally unconditional in both Boss controls** and has equal reach, so **`(b)` — scenarios blocked by element 10 alone — is `0 of 22`**, and discharging element 10 moves `0 of 22` → `0 of 22` (`SA_CORR3_06`). **A second, independent cause was also found: element 10 is absent from the producing party's own published payload** (`SA_CORR3_08`) |
| 2 | The deterministic accounting-event identity — *"owned by neither"* while `BD-ACC-01` assigns it | SMEs Core | **CORRECTED and ACTED ON.** *"Owned by neither"* is **wrong**: `BD-ACC-01`'s primary text names three owners explicitly. **The contract is specified** in this package under the ruling's express grant (`SA_CORR3_08` §3). **And the claim that publishing it closes six items is falsified — it closes none** (`XMC-F-05`) |
| 3 | Price and credit determination undefined — *"research can close it: **Yes**"* | Research | **EXECUTED, not carried** (`SA_CORR3_13`). Blocker 3 is **upheld in one clause and corrected in three.** The inherited zeros are **vocabulary artefacts** |
| 4 | *"The Quality object does not exist"* — *"research can close it: **Yes**"* | Research | **EXECUTED and FALSIFIED** (`SA_CORR3_14`). The object **exists**: named in **two Layer-1 clean-room blueprints**, materialised in **18 deployed tables**, and *"quality check"* returns **10 blobs, not 0.** **It is named and never specified — a design act, not a research act** |
| 5 | Fixed production overhead and maintenance cost | **Boss** (`BLK-07`) | **NARROWED FROM 12 ROUTES TO 1.** Boss residue is **six items and none is "normal capacity or actual hours"**; the genuinely gated maintenance part is **`BLK-08`** |
| 6 | The unqualified compliance claim | **Boss** (governance act) | **`B` — EXECUTED.** Not a Boss decision |
| 7 | *"No structurally independent challenge exists. `PHASE-S/Q-BOSS-02` open"* | **Boss** | **FALSIFIED AS STATED.** `Q-BOSS-02` was **APPROVED 2026-09-07** at commit `2930723` with **ten named controls**, and a verifier **is appointed** at `6cb9946`. **The open residue is an appointment act scoped to Phase SA — a one-line governance act, not a research question** (`SA_CORR3_10`) |

---

## 5. What survives the §18 qualification test

Every candidate was put to all seven questions. **Two survive**, plus a third that is an authority act
rather than a decision.

| Item | Q1 studied? | Q2 evidence consumed? | Q3 cross-module proven/challenged? | Q4 specialists? | Q5 dissent resolved/bounded? | Q6 existing Boss ruling checked? | Q7 genuinely policy, not missing research/design/proof? | **Verdict** |
|---|---|---|---|---|---|---|---|---|
| `XD1-P1` gate-severity default | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — **Group A's own session reserved this election to Boss in writing and the reservation is undischarged** | ✔ — **a risk-appetite election; both surviving options are architecturally sound and equally auditable** | **READY** |
| `TV6-BOSS-01` confirmation-gate default | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — **an explicitly deferred item, open since the Group A round and re-reported "undefined" three times** | ✔ | **READY** |
| `TV6-BOSS-02` base sell-price scope | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — a **scoping election with a stated consequence**, not a research gap | **READY** |
| `XMC-D-01` dropship valuation facts | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — **both readings are consistent with every fact in the corpus** | **READY** |
| `XMC-D-02` extend the 16-element contract's scope? | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — a **scope question about a Boss-approved control**; its scope is unambiguous at primary text, so **there is nothing to research and something to decide** | **READY** |
| `POH-D-01`, `-02`, `-06` · `MNT-B-01`, `-02` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — **`POH-D-01` amends a standing Boss decision; `-02` is an accounting-policy election with unresearched tax consequences; `-06`/`MNT-B` are governance restatements of Boss-owned blockers** | **READY** |
| Independence appointment for Phase SA | ✔ | ✔ | n/a | ✔ | ✔ | ✔ | **an authority act, not a decision** — `Q-BOSS-02` control 2 reserves appointment to Boss and **forbids this session selecting its own** | **READY as an act** |
| `POH-D-03`, `-04`, `-05` | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ — **small, genuine management-meaning and control-ownership policy** | **READY (minor)** |
| **Everything else** | — | — | — | — | — | — | **NO** | **`NOT READY FOR BOSS — RETURNED TO SMEs CORE`, and executed in this package** |

### 5.1 One convergence worth naming

**`XD1-P1` and `TV6-BOSS-01` were reached by two independent studies and are the same *shape* of
question** — *what does a commercial control default to when the business has not said?* They are
**distinct gates** (cancellation vs confirmation) and are **not merged**, because merging two
separately-evidenced elections into one would be exactly the conflation this round convicts CORR2 of
elsewhere. **But Boss may wish to rule once on the principle and let both follow**, and that option is
stated rather than assumed.

---

## 6. Findings raised by this register

| id | Finding |
|---|---|
| `C3-I-01` | CORR2's corrected v2 PATH SET **still had a non-empty complement — 81 text blobs / 57 paths, all governance artefacts.** Same defect class as `C2-I-02`, one rung out |
| `C3-I-02` | **A published negative-control token is single-use.** Regenerate per round |
| `C3-G-01`…`C3-G-06` | Governance corrections and the two-version constitution — `SA_CORR3_05` |
| `C3-IND-01`…`C3-IND-04` | Independence status, blocker 7 falsified, and the Phase-S closure sequence verified — `SA_CORR3_10` |
| **`C3-M-01`** | **Four of CORR2's eleven Boss-facing items rest on a negative that a re-run falsifies, and in three cases the instrument, not the reasoning, was at fault** — a spaced pattern that could not reach run-together identifiers; a clean-room scrub that removed the tokens the pattern needed; a diff-based clause that could not reach an inherited blob. **The reasoning in all three was sound. The instrument's blind spot and the evidence base were the same set** |
| **`C3-M-02`** | **A round's most dangerous output is a negative it produced with a control that fired.** Every falsified negative in this package had a **passing positive control** — the control proved the instrument reached *something*, never that it reached *the thing*. **A positive control must be chosen to sit inside the blind spot the pattern is suspected of having**, not merely inside the corpus |

---

## 7. Checkpoint

# `CP-SA-C3-00 — DECISIONS RECLASSIFIED BEFORE ESCALATION`

`CLOSED (execution status)`. **Checkpoint completion is NOT Boss approval.**

| | Count |
|---|---|
| CORR2 requested decisions surviving in the form they were put | **0 of 4** |
| CORR2 blockers surviving in the form they were put | **0 of 7** |
| Reclassified to `A` and **resolved in this package** | **4** |
| Reclassified to `B` and **executed or dissolved** | **2** |
| Reclassified to `C` — structural independence **act** | **1** |
| Genuine `D` decisions surviving the qualification test | **5 material + 3 minor**, all on **new, narrower grounds** |

Boss remains the sole Final Approver.
