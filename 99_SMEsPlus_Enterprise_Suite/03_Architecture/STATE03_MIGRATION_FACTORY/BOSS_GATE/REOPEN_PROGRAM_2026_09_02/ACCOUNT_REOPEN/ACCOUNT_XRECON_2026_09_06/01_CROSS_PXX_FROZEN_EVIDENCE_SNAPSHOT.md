# 01_CROSS_PXX_FROZEN_EVIDENCE_SNAPSHOT

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`
**Baseline** `origin/SMEsPlus` @ `41f3b32` · **Classification** LAYER 2 — RECONCILIATION QUARANTINE

> Everything below is **read-only evidence**. No artefact named here was edited by this session.

---

## 1. Snapshot method — declared before results

**POPULATION** — the artefact sets of P06 (source + IEV), P08 (source + IEV), P09 (L1–L8), P11 (CORR3), each
at its frozen SHA.
**PATH SET** — derived by `git diff --name-only $(git merge-base origin/SMEsPlus <SHA>) <SHA>`, **not** by
author-supplied file lists. This is what separates each package from the 1,100+ file shared baseline.
**PATTERN** — declared per query at point of use; every zero carries a positive control.
**UNIT** — declared per count; file, occurrence and distinct-identifier are never interchanged.

**Merge-base for all four branches:** `88f52cd`. Branch-added/changed file counts against it:
P06 **100** · P08 **82** · P09 **146** · P11 **87**.

## 2. Frozen surfaces and their package roots

All paths below are relative to `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/`.

| Pxx | Frozen SHA | Package root | Files |
|---|---|---|---|
| **P06 source** | `1b018c1` | `PROCESS_DEEP_RESEARCH_2026_09_04/P06_BANK_TO_RECONCILE_EXECUTION/` | **87** |
| **P06 IEV** | `b423eff` | `INDEPENDENT_REVIEW/P06_BANK_TO_RECONCILE/IEV_006/` | **9** |
| **P08 source** | `00ccd66` | `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_P08_RECORD_TO_REPORT/` | 63 numbered + `LAYER2_EVIDENCE_QUARANTINE/` |
| **P08 IEV** | `bd95d1d` (terminal `3ea9195`) | `…/ACCOUNT_REOPEN/P08_INDEPENDENT_VERIFICATION_2026_09_06/` | **8** |
| **P09** | `4778792` (HEAD `ec4d3d2` bookkeeping) | `…/ACCOUNT_REOPEN/ACCOUNT_P09_PLAN_TO_ANALYZE/L1_L8_BOUNDED_CORRECTION_2026_09_06/` | **11** |
| **P11** | `dc4cc4a` (challenge surface `9356557`) | `…/ACCOUNT_REOPEN/P11_CENTRAL_CORE_RECONCILIATION/` | **87** |

### 2.1 P06 IEV artefact set (9)
`P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` · `P06_INDEPENDENT_VERIFICATION_ADDENDUM_E2.md` ·
`P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md` · `P06_INDEPENDENT_AAS03_CHALLENGE.md` ·
`P06_INDEPENDENT_AUTO_RESUME_STATE.md` · `P06_INDEPENDENT_CHECKPOINT_REGISTER.md` ·
`P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md` · `P06_CLAIM_CLASS_POPULATION_REGISTER.md` ·
`P06_CORRECTION_PROPAGATION_AUDIT.md`

### 2.2 P08 IEV artefact set (8)
`P08_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` · `P08_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md` ·
`P08_HANDOFF_PROPAGATION_AUDIT.md` · `P08_INDEPENDENT_AAS03_CHALLENGE.md` ·
`P08_INDEPENDENT_AUTO_RESUME_STATE.md` · `P08_INDEPENDENT_CHECKPOINT_REGISTER.md` ·
`P08_CLAIM_CLASS_POPULATION_REGISTER.md` · `P08_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`

### 2.3 P09 L1–L8 artefact set (11)
`P09_L1_L8_CORRECTION_REGISTER.md` · `P09_AAS03_L1_L8_CHALLENGE_RECORD.md` · `P09_AUTO_RESUME_STATE.md` ·
`P09_CHECKPOINT_REGISTER.md` · `E05_L1_L8_EVIDENCE.md` · `INSTRUMENTS_MANIFEST_SHA256.md` ·
instruments `L1_L2_L8.py`, `L2_k3_control.py`, `L4_L5.py` · results `L_results.json`, `k1_population.json`

## 3. Evidence measured directly by this session

These are **XRECON's own re-executions**, not quotations of a peer's result.

### `XS-01` — P06's true blocker population is **67**, and it is contiguous

| Field | Value |
|---|---|
| **POPULATION** | distinct `P06-B-nn` identifiers in the P06 source package |
| **PATTERN** | `P06-B-[0-9]+` |
| **PATH SET** | `PROCESS_DEEP_RESEARCH_2026_09_04/P06_BANK_TO_RECONCILE_EXECUTION/` — **all 87 files**, no exclusion |
| **UNIT** | distinct identifier |
| **SHA** | `1b018c1` (the surface P06 published and P11 consumed) |
| **Form 1** | `git grep -hoE 'P06-B-[0-9]+' 1b018c1 -- <root>` → **67**, max `P06-B-67` |
| **Form 2** | `git archive 1b018c1 <root> \| tar -x` (**87 files extracted**) then `grep -rhoE` → **67**, max `P06-B-67` |
| **Agreement** | identifier sets **`diff`-identical** |
| **Contiguity** | `P06-B-01`…`P06-B-67` — **zero missing** |
| **Positive control** | synthetic `P06-B-99` injected → instrument moved **67 → 68**; control removed |
| **Result** | **The published figure of 65 is wrong. 67 is confirmed by two instruments of different shape.** |

This independently confirms the P06 IEV's repair requirement 1 and its `IEV-D-20`, and it is the basis for
`XRD-002` and `XRD-003`.

### `XS-02` — P11's decision population is **19**, and the `D-` namespace carries three families

A naive distinct-identifier count of `` `D-nn` `` over the P11 package returns **23**. That figure is an
artefact of **two zero-padding conventions plus two foreign families**, not a population.

| Family | Members | What it is |
|---|---|---|
| `D-1` … `D-18` **+ `D-3b`** | **19** | **P11's own Boss decisions** — reconciles with `P11_RESEARCH_ERROR_AND_REVISION_LOG.md`:1008, *"18 Boss decisions → **19** — `D-3b` dropped from a total while carried as a row"* |
| `D-01` … `D-07` | 7 | **AAS-03 CORR1 challenge finding-class ids** (decision-authority / cross-process boundary) — `P11_AAS03_CORR1_CHALLENGE.md`:82 |
| `D-01` (`MTI-D-01`) | 1 | an **external Boss ruling** from the Inventory MTI track — `P11_AAS03_FINAL_CHALLENGE.md`:43, :180 |

Occurrence counts: padded `` `D-0n` `` **25**, unpadded `` `D-n`/`D-nn` `` **189**.
**P11's total of 19 is correct.** The hazard is that the namespace is not producer-qualified — and it has
already produced one material defect: `X1-F01`/`X3-F06`/`P11-E-05`, *a Boss ruling inverted and the inversion
attributed to the ruling*, detected **three** times. That instance was corrected; the namespace was not.

### `XS-03` — P08's Boss-decision population is enumerated, not asserted

`P08-BD-01` … `P08-BD-19` — **19 distinct, contiguous**. `18_P08_DEPENDENCY_REGISTER.md`:85 states the total
is *"enumerated from the identifiers present in the package, not asserted"*. P08's own `CP-S11` self-audit
caught it published as 18 in three files (`P08-CONTRA-45`). **Confirmed distinct from P11's 19.**

### `XS-04` — the P08→P11 outbound row population is **14**, and the apparent 13 is a different artefact

The P08 IEV requires *"re-issue all 14 outbound rows"*. `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md`
carries **5 supplied + 8 not-supplied = 13** rows, which reads as a contradiction. It is not.

| Artefact @ `00ccd66` | `HO-` identifiers | Population |
|---|---|---|
| `54_P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` | `HO-01`…`HO-14` | **14** — this is the verifier's population |
| `25_P08_CORE_RECON_HANDOFF_PACK.md` | `HO-01`…`HO-06` | 6 — **a different set under the same ids** (`IVR-F-13`) |
| `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` | `HO-13`, `HO-14` | 13 boundary rows, 2 `HO-` cited |

**No discrepancy. The verifier's 14 is sound.** Recorded because the apparent conflict would otherwise be
published as a false finding by a successor reading only `58_`.

### `XS-05` — P11's live outbound registers cite CORR2 heads for exactly the three peers that moved

**PATTERN** CORR2 peer heads `249b7c2` (P06) · `194efcb` (P08) · `5441f8d` (P09).
**PATH SET** the entire P11 package @ `dc4cc4a`. **UNIT** occurrence.

| Carrier | P06 | P08 | P09 | Nature |
|---|---|---|---|---|
| `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` | `:29` | `:18` | `:28` | **LIVE OUTBOUND** |
| `P11_ACCOUNTING_CONVERGENCE_QUESTION_REGISTER.md` | `:28` | `:29` | `:30` | **LIVE OUTBOUND** |
| `P11_AAS03_CORR3_CHALLENGE.md`:66 | ✓ | ✓ | ✓ | historical — this is finding `X4-C8` *about* the staleness |
| `P11_CORR2_PEER_CLAIM_SNAPSHOT.md`, `P11_CORR2_SUPERSESSION_…`, `P11_B17_SCOPE_REPAIR_CORR2.md` | ✓ | ✓ | ✓ | historical — CORR2-labelled by filename |
| `P11_CORR3_POPULATION_REGISTERS.md`:83 | ✓ | ✓ | ✓ | historical — this is blocker `B-37` recording the staleness |

**In the same two live registers the seven peers that did NOT move are cited at CORR3 heads correctly**
(`P01 b820b29` · `P03 bc767a8` · `P04 65b8841` · `P05 205e0ac` · `P10 1fea562`).

> **The only three peers whose heads moved are the only three still cited at superseded heads.**
> Basis for `XRD-005`.

### `XS-06` — P11 consumed P08's no-referent figure, and built a falsification on it

**PATTERN** `1e-7`; **PATH SET** P11 package @ `dc4cc4a`; **UNIT** occurrence.
**Positive control** `169,143`, the companion figure from the same P08 sentence — returns 4 occurrences,
confirming the region is reachable by the instrument.

| P11 carrier | What it does with the figure |
|---|---|
| `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md`:124 | restates `CI-01` as *"at 1e-7 the count is 3"* — **live outbound** |
| `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md`:106 | quotes it as the received P08 position |
| `P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md`:15 (`F-02`) | **uses it as the falsifier** — asks *"a tolerance at which the count is non-zero"*, answers **YES**, re-states P08's claim on that basis, and derives the method rule *"a soundness claim without a tolerance is not a claim"* |

**Against `IVR-F-16`, re-derived by the P08 verifier in exact Decimal: 0 unbalanced at 0.005, 1e-4, 1e-7 and
exact equality, on both computed and stored balance.** The correct answer to `F-02`'s own question is **NO**.
Basis for `XRD-011`.

## 4. What the frozen evidence affirms

Recorded because a reconciliation that reports only defects misrepresents the state as much as one that
reports none.

- **P06:** every claim re-executed against the ERP source held — the `is_matched` structure, every sampled
  v18/v19 line number, the `account_move` SQL quotation, all eight enumerative version counts. Of 84
  published per-file hashes, **63 match and all 21 that differ are files the round edited** — no unaccounted
  change. The evidence-base denominators (791/961/904/1752) have **no rival value anywhere**.
- **P08:** **21 of 21** extracted tables byte-identical to the original dumps. Arithmetic sound across four
  independent re-derivations. Clean-room separation holds with **zero vendor tokens** across Layer-1.
  Identifier families contiguous, no gaps or orphans.
- **P09:** instruments packaged, paths package-relative, **checksummed**; the ephemeral-locator defect
  **fixed, not asserted**; `L-1`…`L-8` closed with `L-4` honestly **split** rather than force-closed.
- **P11:** the CORR3 intake instrument **reproduces exactly** (`D1` 55 · `D2` 48 · `D3` 155 · union 212) and
  is **published as runnable code**; its positive control caught an inert loop **before** publication.

**Across all four, the research is in materially better condition than the record of the research.**
