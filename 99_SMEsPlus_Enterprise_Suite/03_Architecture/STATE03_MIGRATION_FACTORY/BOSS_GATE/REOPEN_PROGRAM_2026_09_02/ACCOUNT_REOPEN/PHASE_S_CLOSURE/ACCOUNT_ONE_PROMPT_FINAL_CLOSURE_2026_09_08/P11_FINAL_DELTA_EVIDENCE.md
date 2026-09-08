# P11_FINAL_DELTA_EVIDENCE.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part D · deliverable **6 of 12**
**Owner SHA:** **`79e1369156ca052ad77c8f589842f5e99b25f800`** · baseline `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
**Parent verifier results:** `RC-06 = FAIL` · `RC-02 = PASS` (not reopened)
**Consumed:** P06 `a533fe9` · P08 `ca577be` · P09 `ab8c013` · **P07 `ee2be30` READ-ONLY**
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P11-C6-01` — the withdrawn tolerance rule, removed from its last live carriers

| Carrier | Was | Now |
|---|---|---|
| `P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md` axis 9 | *"sound **at a declared tolerance**"* | **sound at EXACT EQUALITY and at every tested tolerance** |
| `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md` | *"0 holds **at tolerance ≥ 0.005**"* | **0 at exact equality and at every tested tolerance** |

**Both were the practical residue of the rule the same package had already withdrawn.** Restated, **not re-grounded** — this instance supports no requirement that soundness be stated only at a declared tolerance, **because there is no tolerance at which the count is non-zero.** The `"complete"` withdrawal is untouched: it rests on a raw-SQL deletion path, not on arithmetic.

## 2. `P11-C6-02` / `C6-04` — the peer premise moved, and it had **two limbs**

`P08-C1` and `P08-C4` are **one correction with two limbs**: the frozen population went from three databases to four, which changes the **balance** claim **and** the **deletion-path install-state** claim.

**The first P11 pass re-pointed the balance limb and left the install-state limb on the three-database premise in three live carriers.** The cross-package reconciliation returned it; all three are corrected.

| Limb | Carriers re-pointed |
|---|---|
| balance | `F-02` · `CI-01` (pin row and the `Q-P11-04` restatement) |
| install state | `B-21`/`T0-14` · `CI-12` · CORR3 intake dispositions |

> **A peer correction that moves a *population* moves every claim resting on that population, not the one the challenge happened to name.** `RC-06` named the balance premise. **The install-state premise had the same premise and no challenge pointed at it.**

**Two uncertainties carried forward rather than resolved by consumption:**
1. **Four frozen extracts are NOT a deployment census.** P08 does not claim it; **P11 does not upgrade it.**
2. **Reproducing the four-input figure requires the 18.x restore client or newer** — `DB-T2`'s archive format is refused by 16.x, whereupon P08's instrument fails closed rather than reporting a fourth zero.

**P11 has not re-executed P08's instrument and has not re-derived a single balance figure.**

## 3. `P11-C6-03` — `B-38` refreshed against P09's final SHA

**`M-1` is RESOLVED** at `ab8c013`. **`M-2` is NOT** — it is the challenge that must run on the corrected surface, **and an owner cannot run it on itself.**

**`AAS+-VETO-04` remains NOT DISCHARGED. `B-38` remains OPEN.** P11 read P09's register and status field, not a summary of it.

## 4. `P11-CORR4-C1` — `B-35`: the intake instrument rebuilt. **`B-35` stays OPEN.**

| # | `B-35` defect | Repair | **Measured consequence** |
|---|---|---|---|
| 1 | lexical tail | order by **last-commit author time**, printed | — |
| 2 | generation-discarding key | key = **(peer, FULL PATH)** | **294** basenames carry more than one path — members the old key collapsed |
| 3 | raw substring membership | **bounded peer token** | **70** files admitted only by the loose rule — names containing `STEP01`/`STEP02`/`STEP03`, which contain `P01`/`P02`/`P03` |
| 4 | tautological blind-spot table | **measured complement** | **9,650 of 10,475** paths selected by **no** derivation |
| 5 | fitted `TAIL=5` | **bound removed**, curve published | `1→94 · 2→102 · 3→108 · 5→126 · 8→152 · 13→200 · 21→270 · unbounded→825`. **The fitted bound discarded 84.7 %** |
| 6 | vacuous failure control | **four controls that can fail** | all four ran, all four behaved as expected |
| 7 | frozen peer SHAs | every tree resolves the **declared pin**, validated fail-closed | 10 pins resolved, substantive, ancestors of their branch |

### An eighth defect, found by the rebuild and by no challenge
**The derivation was dependent on the working directory it was invoked from.** `git grep <ref> -- "*.md"` and `git log <ref> -- <path>` resolve their pathspec **relative to the current directory**. Run from inside the package — where an owner naturally runs it — **`D2` returned 0 and every commit time returned 0.** Run from the repository root, **`D2` = 51**.

**A zero produced by a mis-scoped path set is indistinguishable from a zero produced by an empty population.** It was caught only because the zero was re-run in a second command shape before being believed. The instrument now anchors every pathspec to the toplevel, and a **run-location control** executes the whole derivation from two directories and requires identical output — **825 from both.**

### The four controls
| Control | Expected | Observed |
|---|---|---|
| `NEG` unresolvable pin | exit 3, `pin UNRESOLVED` | **exit 3**, matched |
| `NEG2` prompt commit (`P11-G-10`) | exit 3, `NON-SUBSTANTIVE` | **exit 3**, matched |
| `NEG3` pin not an ancestor | exit 3, `NOT AN ANCESTOR` | **exit 3**, matched |
| `POS` injected synthetic path | union +1, and the new member **is** the injected path | **825 → 826**, delta exactly the injected path |

Each `NEG` re-invokes the instrument as a subprocess with one pin overridden, so it **exercises the real validation path rather than a copy of it**.

### A bound of the selector, disclosed rather than left for a challenger
The peer-token rule reads the **basename**. P08's own RC-05 confirmation artefacts carry no `P08` token in their filenames and are therefore **not selected**, although they are exactly the artefacts the pin refresh was made for. **A real limitation, stated here rather than discovered later**, and not repaired in this round because repairing it would move the population for a second unrelated reason and make the pin delta unreadable.

### Why `B-35` does not close
**No structurally independent actor exists inside this execution.** A subagent in this session shares this context, this prompt and this author's framing. Per prompt §9, P11 does not stop and does not open a new prompt:

```
B-35 OWNER REBUILD COMPLETE — INTERNAL ADVERSARIAL QA PASS — FINAL EXTERNAL CERTIFICATION PENDING
```

**This internal review is NOT independent and is not labelled as such.** `B-35` remains **`CRITICAL` — OPEN**. `B-27` is not reconsidered; its precondition is a certified `B-35`.

## 5. `P11-CORR4-C3` — `B-36`: P07 consumed, read-only

| | |
|---|---|
| File | `…/P07_TH_TAX_TO_COMPLIANCE_EXECUTION/19_P07_CORE_RECON_HANDOFF_PACK.md` |
| At | `ee2be30ebf155e241510b3c7133c69419eb060a0` |
| Content SHA-256 | `482fc987e86a758b74936ae6f18175dcb5e49485da4244bd29eb1cac95efb56c` |
| P07 mutated? | **No. No P07 file was written, at any SHA, on any branch.** |

**The routed question, transcribed rather than paraphrased:**
> *"A ruling on whether a tax-reporting grouping may span companies, and within what security boundary."*

**Registered, not answered.** The evidence does not determine it; it is a **design decision reserved to Boss**, and answering a Phase-SA design question inside Phase S is outside P11's authority — a boundary this programme has crossed before by promoting an open peer item into a rule.

**Intake limb CLOSED. The routed question OPEN and Boss-owned.** It is **not** a reason to block Account closure.

## 6. `P11-CORR4-C4` — `B-39`: `VERSION-SPLIT / NO DIRECT CONTRADICTION`

| Statement | Generation |
|---|---|
| `P08-HO-14` — the statutory register family selects on two different period bases; **5,228 entries** can appear in one register and not the other | **16.0** |
| `P07-F-02`/`-03` — the tax-point substitution *"was removed in the v19 migration"* | **v19** |

**A mechanism present at 16.0 and removed at 19.0 is a version history, not a contradiction.** Both generations preserved, **not merged into one runtime truth**: the estate contains more than one generation, so *"the system does X"* has no single referent here.

**What is still open is a scope question** — which generation a given deployment runs — **not a contradiction.** No statutory determination is made or implied.

## 7. `P11-CORR4-C5` / `C6-05` / `C6` — dependent deltas

- **P06 count correction acknowledged** at `a533fe9` — 7 vetoes / 67 blockers / 21 author errors / 68 root-only vs 75 three-root open items — **received, not re-derived.** No P06 finding changed; `AASP-VETO-06` still binds; `P06-B-34`/`B-35` still flagged, not disposed.
- **Peer snapshot refreshed** at the artefact a successor actually reads. `B-37`'s defect is **REPAIRED and evidenced**; **`B-37` is not closed by P11** — closing a registered blocker on the owner's own say-so is the practice this programme has ruled against.
- **P08's pin moved three times inside this prompt** (`f0cf287` → `82df5f3` → `ca577be`). Re-pinned each time with the delta measured: **UNION 817 → 825 → 825.** The last re-pin moved no claim and **was applied anyway** — *a pin that is right for the wrong reason is not a control.*
- **`P08-F-NEW-01` received, not re-derived.** P11 claims nothing about the access-rights module's behaviour and nothing about what `DB-T2` is. Carried to the Boss Decision Matrix **open**.
- **Manifest self-exclusion stated. `P11-E-49` NOT re-opened** — no new mismatch was measured.

## 8. Owner exit and the blockers that stay open

```
P11 OWNER PHASE S CLOSURE COMPLETE — INTERNAL DELTA QA PASS
```

| Item | Status |
|---|---|
| `B-35` | **`CRITICAL` — OPEN.** Rebuilt, internally QA'd, **not independently certified** |
| `B-27` | **OPEN** — gated on a certified `B-35` |
| `B-37` | **OPEN** — defect repaired and evidenced, closure reserved to the gate |
| `B-38` | **OPEN** — `M-2` unresolved |
| `AAS+-VETO-04` | **NOT DISCHARGED** |
| `B-36` routed question | **OPEN — Boss-owned**; intake limb closed |
| `B-39` | **RE-CLASSIFIED**; contradiction limb closed, generation scope open |
| **Terminal state** | **`TERMINAL B` unchanged — intake integrity is NOT established** |

**Not a PASS, not a freeze, not a merge, not an implementation authorisation. No Veto self-discharged. No peer package mutated. P07 untouched.**
