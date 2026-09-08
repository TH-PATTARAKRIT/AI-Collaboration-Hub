# P09_FINAL_DELTA_EVIDENCE.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part B · deliverable **4 of 12**
**Owner SHA:** **`ab8c0131c46e8154ad7efae18de2a54af2f17362`** · baseline `2079a2594a6a76eb91bdb528f22eaf928d42c0d6`
**Parent verifier result:** `RC-01 = FAIL`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. `P09-C1` — the `M-1` rationale was false, and its counterexample was on the same page

`QR-01` claimed the reference relation is *"a fourth relation, disjoint from all three **by construction**"*.

**The denominator table four sections above it, in the same file, reports partition A = 23 files that are inside the K-1 population *and* in the reference relation.** A relation sharing 23 members with `declaration ∪ inheritance` is not disjoint from it, by construction or otherwise.

**Struck, and re-grounded on the only boundary that is proven:**

```
DENOMINATOR   files referencing a P09 model              192  / 52 modules
  A   ∩ K-1                                               23  / 14
  B   ∖ K-1                                              169  / 52      A + B = 192  ✓
  B1    planning                                          10  /  3
  B2    analytic dimension only                          159  / 51      B1 + B2 = 169 ✓
```

> **B2 is outside K-1 because partition B is *defined* as the complement of K-1 inside the 192-file denominator, and `B2 ⊂ B`.**

**What the withdrawn wording bought and could not.** Disjointness-of-relation would have made the K-1 measurements permanently immune to any reference finding. **Partition membership buys only *these 159 files are not in K-1*.** Partition A is the standing disproof of the stronger claim.

**`QR-01a`, the defect class:** the document was written to withdraw a universal negative about the package's own contents — and **replaced it with another universal negative, refuted by an executed table on the same page.** Two adjacent rows that were also worded as disjointness are annotated to say they describe **what the test reads**, not that the file sets are disjoint.

## 2. `P09-C2` / `P09-C3` — supersession applied at the carriers, not announced elsewhere

| Item | Defect | Repair |
|---|---|---|
| `CO-02b` in `FINAL_BOUNDED_COMPLETION_…` §6 | the `L-6` correction **asserted** the earlier rows *"are marked superseded"*. **They were not.** | banner at the row; **"already shipped" WITHDRAWN** — source presence is not deployment |
| `CH-09` in `PHASE_S_DOMAIN_PURE_CLOSURE_…`:35 | a later authority read `TOMBSTONE / WITHDRAWN`; **the source carrier was never marked** | **`TOMBSTONE / WITHDRAWN`**, successors `CO-01`, `CO-02a`, `CO-03`, identifier retired |

## 3. `P09-C4` — `RC-01` named three stale P11-publication negatives. A variant-tolerant sweep found **six**.

| # | Carrier | Wording — **all WITHDRAWN** | Named by `RC-01`? |
|---|---|---|---|
| 1 | `P09_04_…/P09_AUTO_RESUME_STATE.md`:25 | *"P11 no branch published"* | **yes** |
| 2 | `SUPPLEMENT_…/S13_…`:24 | *"no branch published"* | **yes** |
| 3 | `SUPPLEMENT_…/P09_AUTO_RESUME_STATE.md`:18 | *"no branch published"* | **yes** |
| 4 | `P09_04_…/D23_…`:4 | *"P11 has **no published branch**"* | **NO** |
| 5 | `SUPPLEMENT_…/S18_…`:4 | *"…**no published branch** at time of writing"* | **NO** |
| 6 | `SUPPLEMENT_…/S20_…`:28 | *"P11 has **no published branch**"* | **NO** |

> **The owner's earlier round reported "withdrawn in 3 files". `RC-01` independently reported three carriers. The sweep finds six — and the three both missed are the same word-order variant.**
>
> **Agreement between an owner and an independent verifier is not independence when both inherited the same query.** `RC-01` reproduced the owner's blind spot because it reproduced the owner's phrase.

**Grounded in an executed check, not a peer's statement.** `git branch -r` / `git log` at this commit return `research/account-core-reconciliation-2026-09-04-001` (head `002748d`), `corr/p11-phase-s-remediation-2026-09-07-001`, `corr/p11-phase-s-final-2026-09-07-001`. **P11 has published three branches.**

**Scope discipline:** in carriers 4 and 5 the surrounding `HOLD — PEER PROCESS RECONCILIATION REQUIRED` disposition is **retained**. **Only its publication premise is withdrawn.** A false premise is removed; a conclusion is neither silently rescued nor silently destroyed.

## 4. `P09-C5` — self-caught: the `CH-09` tombstone's own two stale statements

| Stale at the carrier | Corrected to | Already corrected, elsewhere |
|---|---|---|
| *"Withdrawn text, **preserved verbatim**"* | **RECONSTRUCTED** — `LC-02` found **no committed original**; the row was overwritten in place before its first commit | `L1_L8` §8.1 |
| *"`MISSING EVIDENCE` — a citation enumeration is required"* | **DISCHARGED** — 21 occurrences / 11 files / 4 outside the package | `L1_L8` §8.3 |

**Both corrections existed. Neither had been applied to the text carrying the claim.** Identical shape to `P09-C2` and `P09-C3`: **a revision log is not a correction.**

## 5. Mandatory self-test

### `q1` re-executed on the unchanged declared source root
```
q1.py sha256   350d6dffb09703444a351b48f6c5589e892af6875032b6843124c253f0f3cc7d
source root    /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons   1,279 entries, present
k1_population  8,055 bytes, present

denominator 192 / 52 · A 23 / 14 · B 169 / 52 · B1 10 / 3 (6 test, 4 non-test) · B2 159 / 51
A + B = 192 checks True     B1 + B2 = 169 checks True
```
**Every figure identical to the baseline results file, verified by JSON diff and by the file being byte-identical after re-run. No material source delta.**

### One current authority per concept — proven by enumeration
| Concept | Current authority | Every other carrier |
|---|---|---|
| `CO-02b` | `L1_L8_…/P09_L1_L8_CORRECTION_REGISTER.md` **§7** | two carriers, **both marked SUPERSEDED pointing to §7** |
| `CH-09` | same file **§8** | three carriers, **all marked**, source tombstoned by `P09-C3` |

### The sweep's own controls, and the tool that failed
```
positive control  "P11 has no branch published anywhere"  → fires   True
negative control  "P09 has no branch published"           → fires   False
```
**`grep -E` was abandoned mid-run: the engine rejected the bounded-repetition pattern as *"exceeds complexity limits"*.** That is `VER-E-04` from P06's instrument register. **The exit status was checked. Had it exited 0 with no output, it would have read as a clean sweep.**

## 6. Self-test exit and standing limits

```
P09 OWNER CLOSURE COMPLETE — RC01 DELTA SELF-TEST PASS
```

**Owner self-test. Not independent certification.**

- **`M-2` remains as `RC-01` left it.** `AAS+-VETO-04` is **NOT DISCHARGED**, and is not dischargeable by owner execution.
- `L-1`…`L-8` not restarted · no new root · no widened denominator · `BD-01` untouched · no peer package mutated.
