# SA_CORR4_09 — FINAL EVIDENCE INTEGRITY

## CP-SA-C4-90 — FINAL EVIDENCE INTEGRITY VERIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. Content freeze

**Content is frozen at this file's publication.** The manifest is generated **after** the freeze and
covers **all 12 files including this one**. `SA_CORR4_09` and `PACKAGE_MANIFEST_SHA256.txt` are the
last two objects written.

> **`C4-08-F-01` is recorded against this round and is not repaired by this freeze.** The freeze that
> mattered was the one **before independent challenge opened**, and it did not happen — §7.

---

## 2. The eleven checks master prompt §11 requires

| # | Check | Result |
|---:|---|---|
| 1 | **Manifests regenerated only after content freeze** | **YES** — §1; the manifest is the final write |
| 2 | **Every file hash verified** | **12 of 12** — §3 |
| 3 | **Every cited commit SHA resolves** | **21 of 21 cited objects resolve** — §4 |
| 4 | **Every branch count reproducible** | **YES**, three shapes — §5 |
| 5 | **No empty or corrupt artefact** | **0 of 12** zero-byte; all parse as Markdown |
| 6 | **No stale CORR3 denominator copied without re-measurement** | **YES** — §6 |
| 7 | **No unsupported compliance/certification claim in the corrected population** | **YES** — §6 |
| 8 | **No false `PASS` used as Boss approval** | **YES** — §6 |
| 9 | **Every remaining `HOLD` is exact and material** | **YES** — §6 |
| 10 | **Every Boss decision request is authority-only** | **YES** — `SA_CORR4_10` §8: **no new Boss decision is requested** |
| 11 | *(added by this round)* **Every tally re-derived from its own rows** | **YES** — §6, after this failed twice |

---

## 3. Package and hashes

**12 files.** `0` empty, `0` zero-byte, `0` unreadable.

| File | Checkpoint |
|---|---|
| `PHASE_SA_CORR4_AUTO_RESUME_STATE.md` | maintained under §13 |
| `SA_CORR4_00_CORR3_BASELINE_REPRODUCTION.md` | `CP-SA-C4-00` |
| `SA_CORR4_01_PRIVILEGED_BYPASS_PATH_ENUMERATION.md` | `CP-SA-C4-10` |
| `SA_CORR4_02_XMC_C_D1_TENANT_COMPANY_HANDOFF_CONTRACT.md` | `CP-SA-C4-20` |
| `SA_CORR4_03_CF_I_03_AUTHORIZATION_CONFORMANCE_CONTROL.md` | `CP-SA-C4-30` |
| `SA_CORR4_04_COMPLIANCE_RETRACTION_PROPAGATION.md` | `CP-SA-C4-40` |
| `SA_CORR4_05_FOUR_CONDITION_CLOSURE_MATRIX.md` | `CP-SA-C4-50` |
| `SA_CORR4_06_AFFECTED_INVARIANT_RECLASSIFICATION.md` | `CP-SA-C4-60` |
| `SA_CORR4_07_22_SCENARIO_TARGETED_CROSS_PROOF.md` | `CP-SA-C4-70` |
| `SA_CORR4_08_SMES_CORE_FINAL_RECHALLENGE.md` | `CP-SA-C4-80` |
| `SA_CORR4_09_FINAL_EVIDENCE_INTEGRITY.md` | `CP-SA-C4-90` |
| `SA_CORR4_10_BOSS_FINAL_GATE_PACK.md` | `CP-SA-C4-FINAL` |

**`PACKAGE_MANIFEST_SHA256.txt` carries 12 hashes.** *(It does not hash itself — 12 hashes over a
12-file package plus the manifest is correct, not short. `SA_CORR4_00` §7 records the same arithmetic
for CORR3's 16-over-17.)*

---

## 4. Cited objects

**21 distinct commit and blob identifiers are cited across the package. All 21 resolve.**

| Class | Verified |
|---|---|
| Parent CORR3 publication `604398c3` — abbreviated and full form | **resolves**, both |
| CORR3's own self-declared publication `c7f42ce0` | **resolves** — it is the **parent** of `604398c3`. Recorded at `SA_CORR4_00` §7, immaterial |
| Master prompt `5931d7ef` | **resolves** |
| Boss act `eb3d7dbb` — Phase SA entry authorization | **resolves.** *Inherited from CORR3 and independently verified here for the first time* |
| The seven 2026-09-09 mainline Boss decisions | **all 7 resolve** |
| The stranded architecture branch head `098798f7` | **resolves** |
| Blobs `111bfc41` uncorrected · `827b5906` corrected · `9569ceb7` mainline register · `90351835` branch register | **all 4 resolve** |
| This session's own commits | **resolve** |

**Every CORR3 manifest hash was independently recomputed at `SA_CORR4_00` §7: 16 of 16 match.**

---

## 5. Reproducible counts

| Figure | Shapes | Result |
|---|---|---|
| Branch population | `for-each-ref` · `branch -r` · `ls-remote --heads` | **185**, three shapes agree — **and independently re-derived by a challenger** |
| `U1` text blobs · `U2` text paths | full `ls-tree` sweep of all 185 heads | **3,926 · 3,604** — **independently re-derived from scratch by a challenger** |
| Compliance split | `rev-parse -q --verify` per branch · `ls-tree` per branch | **185 present · 0 absent · 183 uncorrected · 2 corrected** — **independently re-derived** |
| 58 invariants | id extraction, two instruments, **plus reading** | **50 `MTI` + 8 `CF-I`**. `C4-I-02`: both instruments returned **51** on a shared wrong pattern; **reading corrected it** |
| 30 `FINAL_SOLUTION` paths · 0 outside `INVENTORY` · `V1_0`=18 / `V2_0`=12 | direct | **reproduced exactly** |
| Positive controls | `BD-ACC-01`=58 · `MTI-50`=17 · `MTI-18`=17 · `privileged`=89 · `compliance`=557 | **all fire** |
| Negative control | `zqw94713_corr4_no_such_token` | **0** — a **fresh** token; `C3-I-02` records they are single-use |

---

## 6. The five substantive verifications

### 6.1 No stale denominator copied without re-measurement

**Four were corrected** — `C4-B-01` … `C4-B-04`. **The one that matters most:** CORR3's remaining count
of `183` and CORR4's are the same number **from different arithmetic** — `184 − 1` against `185 − 2`.
**A round that inherited rather than re-measured would have carried a wrong denominator and a wrong
corrected-count and never noticed, because the number it cared about was unchanged.**

### 6.2 No unsupported compliance claim in the corrected population

**The corrected blob `827b5906` was read directly and audited on all four required tests: it passes
all four.** `0` unqualified claims remain; nothing evidence-backed was removed; no new contradictory
variant; the Thailand line carries **both** required qualifiers.

**The claim class is one file**, established on four instruments, **re-run independently and extended
into Thai** — a language every prior instrument in this chain was blind to. **The negative survived
being widened, which is the only way a negative earns confidence.**

**`183 of 185` branches including `origin/SMEsPlus` remain uncorrected, and the repository is public.**
That is stated as an open exposure, not as a corrected one.

### 6.3 No false `PASS` used as Boss approval

Swept for `PASS`, `APPROVED`, `VERIFIED`, `CERTIFIED`, `BUILD READY`, `RELEASE READY`,
`PRODUCTION READY`, `COMPLETE`, **and every occurrence read in context** — by the orchestrator and
independently by a challenger.

**Every instance is one of:** a negation (`SPECIFIED — NOT BUILT — NOT VERIFIED`, *"no other wording"*);
a quotation of a prohibition; a defined classification name (`SA CONTRACT COMPLETE`,
`MTI-43 CONTROL REFERENCE CLOSED` — **explicitly scoped in the same sentence**); or a reference to the
sweep itself. **No self-declared affirmative verdict. `0` findings.**

### 6.4 Every remaining `HOLD` is exact and material

| `HOLD` | Exact blocker | Owner |
|---|---|---|
| `C4-04` `PROPAGATION HOLD` | Named to the clause; **and one of its three cited instruments was found to be a single undefined assertion** (`C4-04-F-06`), so the disposition now rests on two | PMO |
| Element 10 | `specified, not built, not verified` | Development / Pre-Test |
| Element 15 | The object is undesigned; **an architectural position exists, stranded and unreviewed** | SMEs Core |
| `22 of 22 SA MATERIAL GAP` | Element 15 on all 22, plus each row's own named `(c)` | mixed |
| `G1`–`G5` | Each named, each with an owner | SMEs Core / PMO |
| 6 vetoes | **In force, `0` discharged, none asked to be** | Boss / issuers |

### 6.5 Every tally re-derived from its own rows — after this control failed twice

| Tally | Re-derived |
|---|---|
| `SA_CORR4_01` — 14 path classes; `5 SPEC · 4 PROP · 1 NAME · 4 mixed`; `3+5+2+3+1` | ✓ |
| `SA_CORR4_02` — 13 elements `10 ✔ · 2 ◐ · 1 ✎`; 9 rules `6+3+0`; **10 flows `2 / 8`** | ✓ |
| `SA_CORR4_03` — 25 test classes `5+8+8+4` | ✓ |
| `SA_CORR4_06` — 25 rows; `18 · 5 · 1 · 1`; **8 `Δ` marks = 6 forward + 2 backward** | ✓ |
| `SA_CORR4_07` — 22 rows, 22 `SA MATERIAL GAP` | ✓ |

> **This control failed twice before it worked.** `C4-02-F-06` (self-caught), `C4-06-F-01` and
> `C4-04-F-05` (both challenger-caught) are **three instances of one defect: a total that sums while
> its distribution is wrong.** In every case the total was right, which is why they survived reading.
> **A stated total is a claim about the rows beneath it and must be re-derived, not checked.**

---

## 7. Integrity findings against this round

**Three, and they are published rather than left for a reader.**

| ID | Finding |
|---|---|
| **`C4-08-F-01`** | **The package was not frozen while independent challenge ran.** Four commits landed and three files grew mid-review; a challenger watched a defect corrected underneath its own audit |
| **withdrawn claim** | `SA_CORR4_02`'s `C4-02-F-06` asserted *"every count in `SA_CORR4_06` was re-derived the same way after it."* **Untrue when written.** A challenger found the defect it missed. **The claim is withdrawn at `C4-06-F-01`** |
| **`C4-04-F-07`** | This package cited *"the supersession rule"* as forbidding the correction of historical branches. **That rule governs which document version to read and has never covered this subject.** The extension is withdrawn, and **the recommendation it supported — the one that minimises this session's own work — now stands with no cited authority** |

---

## 8. Clean-room

| Check | Result |
|---|---|
| Vendor / reference-ERP token count, per file, against the CORR3 baseline | **`0` genuine tokens on all 12 files** |
| Apparent hits inspected | **all false positives** — the English words *quantity*, *quantify*, and `ir.` inside *"repair. Its"* |
| One genuine token removed pre-commit | A reference-estate elevation token used as a **search token** in a control table. **Layer 2 vocabulary on a Layer 1 surface is a leak however true the sentence** |
| Thai statutory claims | **None made.** Every statutory item `HOLD / EVIDENCE REQUIRED`, `candidate / UNVALIDATED` |

**Identifier sweep:** 11 families, **`0` sequence gaps**, `0` collisions with another package's namespace.

---

## 9. What integrity verification cannot establish

1. **That the conclusions are right.** Every check here is on *form*: hashes, counts, wording, tallies,
   citations. **The one finding that most changed this package — `5/5` → `2/8` — would have passed
   every check in §2**, because a wrong classification hashes and tallies exactly like a right one.
2. **That the evidence base is complete.** `~12%` of the 1,061-path compliance population is read;
   16 stranded architecture deliverables are unread; the corpus is **documentary**, and a path can
   exist in a built system and in no document.
3. **That this round is independent.** It is not. `EXTERNAL INDEPENDENT CHALLENGE — PENDING`.

## 10. Checkpoint

> ## `CP-SA-C4-90 — FINAL EVIDENCE INTEGRITY VERIFIED`
> **12 files · 12 hashes · 21 of 21 cited objects resolve · 0 empty · 0 clean-room leaks ·
> 0 false `PASS` · 0 stale denominators · 5 of 5 tallies re-derived · 11 of 11 §11 checks ·
> 3 integrity findings published against this round.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
