# P11_ONE_PROMPT_OWNER_CLOSURE_RECORD.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` — Part D
**Control branch:** `control/account-one-prompt-final-closure-2026-09-08-001` · prompt commit `a06f5d9c69e020bf8e7749108b892b73c6b31e62`
**Owner:** P11 Central Core Reconciliation · **Baseline:** `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
**Parent verifier results:** `RC-06 = FAIL` · `RC-02 = PASS` (not reopened)
**Consumed owner SHAs:** P06 `a533fe92d6f6855e0b362179403476520cc9aafa` · P08 **`ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`** *(moved twice inside this prompt: `f0cf287` → `82df5f3` → `ca577be`; neither move touches a claim P11 consumes)* · P09 `ab8c0131c46e8154ad7efae18de2a54af2f17362` · P07 `ee2be30ebf155e241510b3c7133c69419eb060a0` **READ-ONLY**
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P11-C6-01` — the withdrawn tolerance rule, removed from its last live carriers

`RC06-F1`: axis 9 still read *"Arithmetic sound **at a declared tolerance** (`F-02`)"* — **the practical residue of the rule the same file had just withdrawn.**

Superseded in two places, both current-tense at the frozen surface:

| Carrier | Was | Now |
|---|---|---|
| `P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md` axis 9 | *"sound at a declared tolerance"* | **sound at EXACT EQUALITY and at every tested tolerance** |
| `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md` | *"0 holds at tolerance ≥ 0.005"* | **0 at exact equality and at every tested tolerance** |

**Restated, not re-grounded.** This instance supports no requirement that soundness be stated only at a declared tolerance, **because there is no tolerance at which the count is non-zero.** The rule stays **WITHDRAWN**; P11 does not resurrect it because it sounds plausible.

**The `"complete"` withdrawal is untouched** — it rests on a raw-SQL deletion path, not on arithmetic, and is unaffected by anything in this correction.

## 2. `P11-C6-02` — the balance premise, re-pointed to P08's final owner SHA

`RC06-F2`: P11 was closing on P08's **three-database** premise after RC-05 established a fourth.

| | |
|---|---|
| **New premise** | **0 unbalanced posted entries at exact equality and at `1e-7`, `1e-4`, `0.005`, on both the computed and the stored column, across the FOUR FROZEN RC-05 DATABASE EXTRACTS** — `DB-SM` 169,143 · `DB-BK` 16 · `DB-EV` 6 · **`DB-T2` 5** posted entries with lines |
| **Owner evidence** | P08 `f0cf287ac9f4ad37b0c19145df4a0e396af84c13` |
| **Re-pointed at** | `F-02` · `CI-01` (both the pin row and the `Q-P11-04` restatement) |
| **Preserved as lineage** | the three-DB premise — **it was never wrong, it was incomplete against the frozen population** |

**Two uncertainties carried forward rather than resolved by consumption:**

1. **Four frozen extracts are NOT an established deployment census.** P08 does not claim it and **P11 does not upgrade it.** Every restated carrier says *four frozen RC-05 database extracts*.
2. **A tool-version precondition travels with the figure.** `DB-T2` is archive format 1.16 and `pg_restore` 16.15 refuses it; P08's instrument then **fails closed at exit 3** rather than reporting a fourth zero. **Reproducing the four-input result requires `pg_restore` ≥ 18.**

**P11 has not re-executed P08's instrument and has not re-derived a single balance figure.** It consumed published owner evidence, which is what `RC-06` authorises and all it authorises.

## 3. `P11-C6-03` — `B-38` refreshed against P09's final owner SHA

**`M-1` is RESOLVED** at `ab8c013`: P09 withdrew the universal that reference is disjoint from declaration/inheritance/K-1 *"by construction"* — its own executed denominator puts **23 files inside K-1 and in the reference relation** — and re-grounded on the proven partition boundary `B2 ⊂ B`, `B = 192 ∖ K-1`.

**`M-2` is NOT resolved.** It is the challenge that must run on the corrected surface, and **an owner cannot run it on itself.**

**Therefore `AAS+-VETO-04` remains NOT DISCHARGED and `B-38` remains OPEN.** P11 read P09's register and status field, not a summary of it.

## 4. `P11-CORR4-C1` — `B-35`: the intake instrument rebuilt. **`B-35` stays OPEN.**

Successor: `LAYER2_P11_EVIDENCE/corr4_instrument/intake_derivations_v3.py`. Both predecessors retained as lineage.

| # | `B-35` defect | Repair | **Measured consequence** |
|---|---|---|---|
| 1 | lexical tail — filename order is not evidence order | order by **last-commit author time** at the pinned tree, printed | — |
| 2 | generation-discarding key | key is **(peer, FULL PATH)** | **294 basenames carry more than one path** — members the old key collapsed |
| 3 | raw substring membership | **bounded peer token**, delimited both sides | **70 files** selected only by the loose rule — names containing `STEP01`/`STEP02`/`STEP03`, which contain `P01`/`P02`/`P03` |
| 4 | tautological blind-spot table | **measured complement** | **9,649 of 10,474** `*.md` paths selected by **no** derivation |
| 5 | fitted `TAIL=5` | **bound removed**; curve published instead | `1→94 · 2→102 · 3→108 · 5→126 · 8→152 · 13→200 · 21→270 · unbounded→825`. **The fitted bound discarded 84.7 % of the population** |
| 6 | vacuous failure control | **four controls that can fail** | all four ran; all four behaved as expected |
| 7 | frozen peer SHAs | every tree resolves the **declared pin**, validated fail-closed | 10 pins resolved, substantive, ancestors of their declared branch |

### 4.1 An eighth defect, found by the rebuild and not by any challenge

**The derivation was dependent on the working directory it was invoked from.**

`git grep <ref> -- "*.md"` and `git log <ref> -- <path>` resolve their pathspec **relative to the current directory**. Invoked from inside the P11 package — which is where an owner naturally runs it — **`D2` returned 0 and every commit time returned 0**. Invoked from the repository root, **`D2` = 51**.

```
git grep -l -E '^#{1,4} .*P11' ee2be30 -- "*.md"     run from the package  ->  (nothing)
                                                      run from the root     ->  hits
```

**A zero produced by a mis-scoped path set is indistinguishable from a zero produced by an empty population.** It was caught only because the zero was re-run in a second command shape before being believed. The instrument now `chdir`s to the toplevel, every pathspec is `:(top)`-anchored, and a **run-location control** executes the whole derivation from two different directories and requires identical output — **`825` from both**.

### 4.2 The four controls, expected printed before observed

| Control | Expected | Observed |
|---|---|---|
| `NEG` unresolvable pin | exit 3, `pin UNRESOLVED` | **exit 3**, `pin UNRESOLVED or not a commit: 0000000` |
| `NEG2` prompt commit (`P11-G-10`) | exit 3, `NON-SUBSTANTIVE` | **exit 3**, `pin NON-SUBSTANTIVE under P11-G-10 (prompt commit): 92de8a1` |
| `NEG3` pin not an ancestor of its branch | exit 3, `NOT AN ANCESTOR` | **exit 3**, `pin NOT AN ANCESTOR of declared branch …` |
| `POS` injected synthetic path | union **+1**, and the new member is the injected path | **825 → 826**, delta exactly the injected path |

Each `NEG` re-invokes the instrument as a subprocess with one pin overridden, so it **exercises the real validation path rather than a copy of it**. The override prints itself whenever it fires and is unset in every real run.

### 4.3 The pin delta, measured rather than swapped silently

| Pin set | UNION | `D1` | `D2` | `D3` |
|---|---:|---:|---:|---:|
| CORR3 pins | **817** | 55 | 48 | 815 |
| 2026-09-08 final owner pins | **825** | 57 | 51 | 823 |

**+8 members, 0 removed**, and all eight are the owner-closure artefacts published in this same prompt by P06, P08 and P09. **Re-run at P08's final `ca577be`: UNION unchanged at 825**, with the measured complement moving `9,649 → 9,650` as P08's package gained one file. **All four controls re-run and behaved as expected at the final pins.** **Re-pinning was published as a delta, not applied silently.**

### 4.4 A bound of the selector, disclosed rather than left for a challenger

The peer-token rule reads the **basename**. P08's `RC05_CONFIRMATION_2026_09_08/00_PRE_RUN_PREDICTION.md` and `01_RUN_RESULTS_AND_PREDICTION_SCORING.md` carry no `P08` token in their filenames and are therefore **not selected**, although they are exactly the artefacts the pin refresh was made for. **This is a real limitation of a filename-based selector and it is stated here rather than discovered later.** It is not repaired in this round because repairing it would move the population for a second, unrelated reason and make the pin delta unreadable — **the same discipline `CO-F-01` applied, and for the same reason.**

### 4.5 Why `B-35` does not close

**`B-35` may close only on independent certification of the rebuilt instrument against the full published twelve-control set including `S06`.** That has not happened.

**No structurally independent actor exists inside this execution.** A subagent in this same session is not an independent challenger: it shares this context, this prompt and this author's framing. **Per prompt §9, P11 does not stop and does not open a new prompt.** It runs the strongest available owner adversarial QA and records:

```
B-35 OWNER REBUILD COMPLETE — INTERNAL ADVERSARIAL QA PASS — FINAL EXTERNAL CERTIFICATION PENDING
```

**This internal review is NOT independent and is not labelled as such.** `B-35` remains **`CRITICAL` — OPEN**. `B-27` is not reconsidered, because its precondition is a certified `B-35`.

## 5. `P11-CORR4-C3` — `B-36`: P07 consumed, read-only

| | |
|---|---|
| **File** | `…/P07_TH_TAX_TO_COMPLIANCE_EXECUTION/19_P07_CORE_RECON_HANDOFF_PACK.md` |
| **At** | `ee2be30ebf155e241510b3c7133c69419eb060a0` — the SHA the prompt declares |
| **Content SHA-256** | `482fc987e86a758b74936ae6f18175dcb5e49485da4244bd29eb1cac95efb56c` |
| **P07 mutated?** | **No. No P07 file was written, at any SHA, on any branch.** |

**The routed question, transcribed from §6 rather than paraphrased:**

> *"A ruling on whether a tax-reporting grouping may span companies, and within what security boundary."*

**P11 registers it and does not answer it.** The evidence does not determine it; it is a **design decision reserved to Boss**, and answering a Phase-SA design question inside Phase S is outside P11's authority — a boundary this programme has crossed before by promoting an open peer item into a rule.

**It is not a reason to block Account closure.** It is carried into `ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md` as the single named item behind the Thailand Tax interface's `ACCOUNT-HANDOFF-EXTERNAL-DECISION-PENDING`.

**`B-36`'s intake limb — an in-denominator artefact left unopened across three rounds — is CLOSED. The question it carried is OPEN and owned by Boss.**

## 6. `P11-CORR4-C4` — `B-39`: `VERSION-SPLIT / NO DIRECT CONTRADICTION`

| Statement | Generation | Status |
|---|---|---|
| `P08-HO-14` — the statutory register family selects on two different period bases; 5,228 entries can appear in one register and not the other | **`S16c` / `DB-SM`, 16.0** | true of 16.0 |
| `P07-F-02` / `-03` — the tax-point substitution *"was removed in the v19 migration"* | **v19 migration state** | true of v19 |

**A mechanism present at 16.0 and removed at 19.0 is a version history, not a contradiction.** Both generations are **preserved and are not merged into one runtime truth**: the estate contains more than one generation, so *"the system does X"* has no single referent and neither finding may be restated without its generation.

**What is still open is not a contradiction but a scope question** — which generation a given deployment runs, a per-deployment fact P11 does not hold. **No statutory determination is made or implied.**

## 7. `P11-CORR4-C5` — P06 count correction acknowledged, not re-derived

Received at P06 `a533fe9`: **seven vetoes, 0 discharged · 67 blockers `P06-B-01`…`P06-B-67` contiguous · 21 author errors** (unit: author error, not identifier) · open items **68 root-only / 75 three-root**, two figures for one concept separated only by path set, which P06 registers as `VER-E-06`.

**P11 records receipt and re-derives nothing.** No P06 finding was withdrawn or added; `AASP-VETO-06` still binds (`HO-03`/`HO-04` **WRITTEN, NOT DELIVERED**); `P06-B-34`/`P06-B-35` remain **flagged, not disposed**; `AASP-VETO-07` remains **PRESERVED**.

## 8. `P11-CORR4-C6` — manifest wording

**`P11_EVIDENCE_MANIFEST.md` is excluded from its own substantive population by definition** — a manifest cannot carry its own digest. **`P11-E-49` is NOT re-opened**: no new mismatch was measured, and stating an exclusion is not an admission of an omission.

## 9. Owner exit

```
P11 OWNER PHASE S CLOSURE COMPLETE — INTERNAL DELTA QA PASS
```

## 10. What is NOT claimed — the blockers that stay open

| Item | Status after this round |
|---|---|
| `B-35` | **`CRITICAL` — OPEN.** Rebuilt, internally QA'd, **not independently certified** |
| `B-27` | **OPEN** — gated on a certified `B-35` |
| `B-37` | **OPEN** — not in this round's authorised surface |
| `B-38` | **OPEN** — `M-2` unresolved |
| `AAS+-VETO-04` | **NOT DISCHARGED** |
| `B-36` routed question | **OPEN — Boss-owned**, intake limb closed |
| `B-39` | **RE-CLASSIFIED**, contradiction limb closed, generation scope open |
| Terminal state | **`TERMINAL B` unchanged — intake integrity is NOT established** |

**Not a PASS, not a freeze, not a merge, not an implementation authorisation. No Veto self-discharged. No peer package mutated. P07 untouched.**

---

## 11. Second pass — items the cross-package reconciliation returned to P11

Published after the first P11 owner commit, on the same branch, from the **single** Account cross-package delta reconciliation over the four final owner SHAs. **These are corrections to P11's own package, not a new round.**

### `P11-C6-04` — the install-state premise moved with the balance premise, and the first pass moved only one of them

`P08-C1` and `P08-C4` are **one correction with two limbs**: the frozen population went from three databases to four, which changes **both** the balance claim **and** the deletion-path install-state claim. **The first P11 pass re-pointed the balance limb and left the install-state limb on the three-database premise in three live carriers.**

| Carrier | Was *(all WITHDRAWN — quoted for identification only)* | Now |
|---|---|---|
| `P11_CORR3_POPULATION_REGISTERS.md` `B-21`/`T0-14` | *"installed in ALL THREE deployed databases"* — **WITHDRAWN** | **all FOUR frozen RC-05 extracts** |
| `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` `CI-12` | *"installed in all three deployed databases"* — **WITHDRAWN** | **all FOUR frozen RC-05 extracts** |
| `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md` | *"installed in all three deployed databases"* — **WITHDRAWN** | **all FOUR frozen RC-05 extracts** |

**`exercised` remains NOT ESTABLISHED.** Install state is capability, not act. **Four frozen extracts are not a deployment census.**

> **The lesson is the shape, not the miss.** A peer correction that moves a *population* moves **every** claim resting on that population, not the one the challenge happened to name. `RC-06` named the balance premise; **the install-state premise had the same premise and no challenge pointed at it.**

### `P11-C6-05` — the peer snapshot, refreshed at the artefact a successor actually reads

`B-37`'s defect is that `P11_AUTO_RESUME_STATE.md` — P11's own control artefact — **points a successor at superseded heads.** §2 now carries a **current** table with the three moved pins, the CORR3 snapshot struck and retained as lineage, the measured intake effect (**UNION 817 → 825, +8, 0 removed**), and a per-claim statement of **which consumed claims moved and which did not**.

**`B-37` is not closed.** The defect is repaired and evidenced; **closing a registered blocker on the owner's own say-so is the practice this programme has ruled against**, so it goes to the final independent gate with the repair attached.

### `P08-F-NEW-01` — received, not re-derived

P08's four-input refresh reports **`scgl_special_access_rights` installed in `DB-T2` alone** — uninstalled in two extracts, **no row at all** in a third. **P11 records receipt and does not re-derive it.**

**P11's position, bounded:** this is an **access-rights** module, and P11's scope register carries tenant- and company-isolation as tolerance-zero. **P11 makes no claim about the module's behaviour** — nobody has read its source — and **no claim about whether `DB-T2` is a deployment, a test restore or a clone.** What is established is that **the extracts are not homogeneous in their custom access-rights layer**, and that is carried to the Boss Decision Matrix as an open item rather than resolved here.

**It does not change any P11 finding**, and it is **not** used to strengthen one.
