# P09_ONE_PROMPT_OWNER_CLOSURE_RECORD.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` — Part B
**Control branch:** `control/account-one-prompt-final-closure-2026-09-08-001` · prompt commit `a06f5d9c69e020bf8e7749108b892b73c6b31e62`
**Owner:** P09 Plan-to-Analyze · **Baseline:** `2079a2594a6a76eb91bdb528f22eaf928d42c0d6`
**Parent verifier result:** `RC-01 = FAIL` (`01_RC01_P09_CHALLENGE.md`)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P09-C1` — the `M-1` rationale, withdrawn and re-grounded

**File:** `OWNER_QUEUE_2026_09_07/Q_P09_01_L4_AUTHORITY_RESOLUTION.md`

`QR-01` claimed the reference relation is *"a fourth relation, disjoint from all three **by construction**"*. **The denominator table four sections above it, in the same file, reports partition A = 23 files that are inside the K-1 population *and* in the reference relation.** A relation sharing 23 members with `declaration ∪ inheritance` is not disjoint from it.

**`QR-01` is struck and restated at the boundary that is actually proven:**

> **B2 is outside K-1 because partition B is *defined* as the complement of K-1 inside the 192-file denominator, and `B2 ⊂ B`.**

```
DENOMINATOR                            192  / 52 modules
  A  ∩ K-1                              23  / 14
  B  ∖ K-1                             169  / 52      A + B = 192  ✓
  B1  planning                          10  /  3
  B2  analytic dimension only          159  / 51      B1 + B2 = 169 ✓
```

**What the withdrawn wording bought, and could not.** Disjointness-of-relation would have made the K-1 measurements permanently immune to any reference finding. Partition membership buys only *these 159 files are not in K-1*. **Partition A is the standing disproof of the stronger claim.**

**`QR-01a`, the defect class:** the document was written to withdraw a universal negative about the package's own contents (the `L-4` exclusion authority) — **and replaced it with another universal negative, refuted by an executed table on the same page.** Two rows that were *also* worded as disjointness (`ownership`, `extension counts`) are narrower and defensible; both are annotated to say they describe **what the test reads**, not that the file sets are disjoint.

## 2. `P09-C2` — the stale `CO-02b` carrier, superseded at the carrier

**File:** `FINAL_BOUNDED_COMPLETION_2026_09_06/P09_FINAL_BOUNDED_COMPLETION_REGISTER.md` §6

The `L-6` correction asserted the earlier rows *"are marked superseded by this register"*. **They were not marked.** `RC01-F2` found the row live, present-tense, at the frozen surface. A supersession banner is now applied at the row itself, and the deployment wording **"already shipped"** is **withdrawn**: source presence is not deployment, and the supportable statement is *present in the source of the declared root, source generation 18.0 Enterprise*.

## 3. `P09-C3` — `CH-09` tombstoned at its source carrier

**File:** `PHASE_S_DOMAIN_PURE_CLOSURE_2026_09_06/P09_CANDIDATE_HANDOFF_REGISTER.md`:35

Marked **`TOMBSTONE / WITHDRAWN`** with successors **`CO-01`, `CO-02a`, `CO-03`**, the identifier retired and not reusable, historical wording preserved. **A tombstone published in a later register is not a tombstone at the row a reader will actually find.**

## 4. `P09-C4` — the false P11-publication negatives: RC-01 named three; a variant-tolerant sweep found **six**

The prompt requires a variant-tolerant search rather than exact-phrase. Running one changed the answer.

| # | Carrier | Wording found *(all WITHDRAWN — quoted for identification only)* | Named by RC-01? |
|---|---|---|---|
| 1 | `P09_04_…/P09_AUTO_RESUME_STATE.md`:25 | *"P11 no branch published"* — **WITHDRAWN** | **yes** |
| 2 | `SUPPLEMENT_…/S13_P09_ASSET_CONTRADICTION_REFRESH.md`:24 | *"no branch published"* — **WITHDRAWN** | **yes** |
| 3 | `SUPPLEMENT_…/P09_AUTO_RESUME_STATE.md`:18 | *"no branch published"* — **WITHDRAWN** | **yes** |
| 4 | `P09_04_…/D23_P09_P11_DENOMINATOR_SIGN_PLATFORM_SUPPLEMENT.md`:4 | *"P11 has **no published branch**"* — **WITHDRAWN** | **NO** |
| 5 | `SUPPLEMENT_…/S18_P09_P11_SUPPLEMENTAL_CRITICAL_EVIDENCE_HANDOFF.md`:4 | *"P11 has **no published branch** at time of writing"* — **WITHDRAWN** | **NO** |
| 6 | `SUPPLEMENT_…/S20_P09_AAS_PLUS_SUPPLEMENTAL_CONSOLIDATION.md`:28 | *"P11 has **no published branch**"* — **WITHDRAWN** | **NO** |

**All six are corrected.** The earlier P09 round reported *"withdrawn in 3 files"*; `RC-01` independently reported **three carriers**; the sweep finds **six**.

> **Three instruments agreed on three, and all three were searching the same phrase shape** — *"P11 has published no branch"*. The three they missed all say **"no published branch"** — **WITHDRAWN wording, quoted** — a word-order variant. **Agreement between an owner and an independent verifier is not independence when both inherited the same pattern.** RC-01 reproduced the owner's blind spot because it reproduced the owner's query.

**The correction is grounded in an executed check, not in a peer's statement:** `git branch -r` and `git log` at this commit return `research/account-core-reconciliation-2026-09-04-001` (head `002748d`), `corr/p11-phase-s-remediation-2026-09-07-001` and `corr/p11-phase-s-final-2026-09-07-001`. **P11 has published three branches.**

**Scope note.** In carriers 4 and 5 the surrounding `HOLD — PEER PROCESS RECONCILIATION REQUIRED` disposition is **retained** — the disposition may be defensible on other grounds. **Only its publication premise is withdrawn.** A false premise is removed; a conclusion is not silently rescued or silently destroyed.

## 5. `P09-C5` — self-caught: the `CH-09` tombstone's own two stale statements

Found while proving *one current authority per concept*, not named by RC-01, same claim class, repaired in this loop.

| Stale statement at the carrier | Corrected to | Corrected where, earlier |
|---|---|---|
| *"Withdrawn text, **preserved verbatim**"* | **RECONSTRUCTED** — `LC-02` searched and found **no committed original**; the row was overwritten in place before its first commit | `L1_L8` §8.1 |
| *"`MISSING EVIDENCE` — a citation enumeration is required"* | **DISCHARGED** — 21 occurrences / 11 files / 4 outside the package | `L1_L8` §8.3 |

**Both corrections existed. Neither had been applied to the text carrying the claim.** That is the identical shape as `P09-C2` and `P09-C3`, and it is the package's recurring defect: **a revision log is not a correction.**

## 6. Mandatory self-test

### 6.1 `q1` re-executed on the same declared source root — unchanged

```
q1.py sha256 350d6dffb09703444a351b48f6c5589e892af6875032b6843124c253f0f3cc7d
source root  /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons   (1,279 entries, present)
k1_population.json                                                        (8,055 bytes, present)

  denominator                       192  / 52 modules
    A — inside K-1                   23  / 14
    B — outside K-1                 169  / 52     A + B = 192   checks: True
    B1 — planning                    10  /  3     (6 test, 4 non-test)
    B2 — analytic only              159  / 51     B1 + B2 = 169 checks: True
```

**Every figure identical to the baseline `q1_results.json`, verified by JSON diff, not by eye.** No material source delta.

### 6.2 One current authority per concept — proven by enumeration

| Concept | Current authority | Every other carrier |
|---|---|---|
| **`CO-02b`** | `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_L1_L8_CORRECTION_REGISTER.md` **§7** | `CORRECTION_EVIDENCE_INTEGRITY_…/P09_CANDIDATE_IPO_HANDOFF_PACK_CORRECTED.md`:61 **marked SUPERSEDED, pointing to §7** · `FINAL_BOUNDED_COMPLETION_…` §6 **marked SUPERSEDED by `P09-C2`** |
| **`CH-09`** | `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_L1_L8_CORRECTION_REGISTER.md` **§8** | source carrier **tombstoned by `P09-C3`** · `CORRECTION_EVIDENCE_INTEGRITY_…`:83 **marked SUPERSEDED** · `FINAL_BOUNDED_COMPLETION_…` §6 tombstone **marked SUPERSEDED by `P09-C5`** |

**Exactly one current authority each. Every other occurrence is either a marked pointer to it, or a challenge/checkpoint row that references the identifier without asserting a disposition.**

### 6.3 Variant-tolerant sweep — with its controls

The declared predicate is `(publication-negative variant) AND (\bP11\b)` on the same line, run in Python over **136 markdown files**, recursive.

**Why not `grep -E`.** The first attempt used a bounded-repetition ERE over UTF-8 text and the engine rejected it: *"exceeds complexity limits"*. **That is `VER-E-04` from P06's instrument register — a search that errors rather than returning empty. Had it exited 0 with no output, it would have read as a clean sweep.** The exit status was checked; the tool was replaced.

```
positive control  "P11 has no branch published anywhere"  -> predicate fires   True   # synthetic, WITHDRAWN-equivalent
negative control  "P09 has no branch published"           -> predicate fires   False
```

## 7. Self-test exit

```
P09 OWNER CLOSURE COMPLETE — RC01 DELTA SELF-TEST PASS
```

**Owner self-test only. Not independent certification.** RC-01's fresh delta challenge is reserved for the single final independent gate.

## 7.1 One note on this file's own text

**Every withdrawn wording quoted above is marked `WITHDRAWN` on its own line.** Without that, a future variant sweep would return this closure record as six new current-looking carriers — **the correction would register as the defect it corrected.** P06's `VER-E-07` is the same phenomenon on a counted population, where it moved a published total from 67 to 69. Here it would only have added noise, because a residue sweep has no denominator to corrupt. **The habit is worth keeping in both cases: an audit artefact must not be indistinguishable from its own subject.**

---

## 8. What is NOT claimed

- `M-2` remains as `RC-01` left it. **`AAS+-VETO-04` is NOT discharged**, and is not dischargeable by owner execution.
- `L-1`…`L-8` not restarted · no new root · no widened denominator · `BD-01` untouched · no peer package mutated · no adjacent-domain research.
- Not a PASS, not a freeze, not a merge, not an implementation authorisation.
