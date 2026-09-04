# MCC_H — FIXED-POINT CONVERGENCE PROOF

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Applies the three-pass fixed-point protocol of the round instruction §11.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Protocol as executed

| Pass | Constitution | Assignment | Independent of the author? |
|---|---|---|---|
| **Pass 1** — primary deterministic enumeration | this session | Corrected enumeration rules over the bounded populations: rate-table surface, scoping rules, config keys, shipped data, bypass paths, gating unknowns, denominators | — (is the author) |
| **Pass 2** — fresh independent re-enumeration | reviewer `MCCR-A` | Same bounded universe, re-derived from primary source. Instructed to take **no** prior package statement as true | **Yes.** Not an author of this or any prior round |
| **Pass 3** — fresh adversarial delta search | reviewer `MCCR-B` | Specifically: find a missing population · a new material finding class · an unbounded negative claim · an incorrectly closed gating unknown · a denominator defect · an eighth tolerance-zero boundary | **Yes.** Disjoint assignment from Pass 2 |

Both reviewers were given the enumeration universe, the denominator definitions, the rules, the
material-delta criteria and the evidence manifest, per the standard. Both were told the allowed
verdicts exclude `PASS`, that "no evidence found" is not "does not exist", and that every negative
must declare its scope. **Both complied and both closed with an explicit statement of what they did
not search.**

**Governing rule, applied without exception:**
> `Independent Review ≠ Truth.` `Verified Evidence = Truth Basis.`
> **Every reviewer claim accepted below was re-verified against primary source by this session before
> acceptance.** Claims reduced or rejected on verification are at `MCC_E01` §3.

---

## 2. Pass 1 result (author)

| Output | Value |
|---|---|
| Rate-table surface bounded, pattern declared, path set proven | 20 files |
| Company-scoping expressions over that surface | 14 sites |
| Bypass paths enumerated | 12 · 11 closed with declared scope · 1 residual |
| Gating unknowns closed | 8 of 17 |
| Denominators recounted | 15 of 15 reproduced |
| New tolerance-zero boundary | 1 (`T0-10`) |
| Blocker movement | `GB-03` re-opened → **`PARTIAL`**, split into a closed branch axis and an open null axis |

---

## 3. Pass 2 result — and what it did to Pass 1

| Measure | Result |
|---|---|
| Verdict | **`PARTIALLY VERIFIED`** on boundedness |
| Pass 1 claims **independently reproduced** | the resolver precedence rule · the latent context-company divergence · the absence of raw-SQL writes (by a **second, line-wrap-tolerant** method across **four** version trees) · the absence of a constraint-skip flag · the migration-script absence · the hierarchy-immutability block · the currency root-delegation · the `data`-vs-`demo` shipped-data split · the access matrix |
| Pass 1 claims **INVALIDATED** | **2** — the demo rows are **root-company**, not company-less (the loader applies the model default); and the cross-version model is **NOT stable** (a branch-preference clause exists in a later v18 point release and in neither v19 tree) |
| Pass 1 claims **corrected upward** | **2** — the unsearched tree is **962 manifested modules**, not 961 directories; the localisation surface is **2 in the searched tree, 904 in the unsearched one** |
| **New material class** returned | **1** — a **v19 ORM-core** rate resolver, in raw SQL, outside every record rule, converting at *today*, with a **fourth** fallback semantic |
| Veto | **1 partial, ACCEPTED**: no convergence claim may rest on the branch-rate constraint alone — it is create-time only with no database-level constraint behind it |

---

## 4. Pass 3 result — and what it did to Passes 1 and 2

| Measure | Result |
|---|---|
| Verdict | **`PARTIALLY VERIFIED` / `NOT CONVERGED`** |
| Missing population found | **1** — the company-consistency **enforcement** surface. 9 of 22 Wave A models enable automatic checking; 36 of 139 relational fields opt in; **16 declared guards on the company model are inert** |
| New material finding class found | **1 of tolerance-zero severity** — cross-branch reconciliation, exchange-difference posting and raw-SQL settlement admitted because the sole guard tests the **root** rather than the company. Plus 2 lesser classes |
| Unbounded negative claims found in the parent MC package | **9**, two of which are corrections that round itself accepted and never propagated |
| Misclassified gating unknowns found | **4 reclassified into gating · 2 reverted from out-of-scope to unknown · 1 double-count** |
| Denominator defects found | **3 that do not reproduce**, one of which is published as source-derived while being author-derived; **1 population misdefined by 962 modules** |
| Eighth tolerance-zero boundary found | **Yes** — entry identity — plus a candidate ninth, declared-but-inert control |
| Veto | **None issued** |

---

## 5. Delta record — every material change, by pass

| # | Delta | Origin | Material? | Effect |
|---|---|---|---|---|
| 1 | Rate-table surface 14 → 20 files | **Pass 1, against itself** | **YES** — new population members | Path set corrected |
| 2 | Second module tree found; 961 dirs / 962 manifested modules | Pass 1, corrected by Pass 3 | **YES** — bounding denominator for every whole-tree negative in the programme | `MC-01` |
| 3 | 3 module directories directly under the source root | **Pass 3** | **YES** — Pass 1 missed them | `MC-01` |
| 4 | Localisation surface: 2 searched, 904 unsearched | **Pass 2** | **YES** | `MC-01` |
| 5 | Demo rows are root-company, not company-less | **Pass 2** | **YES — invalidates a Pass 1 claim** | `MC-05`, `BW-30` mechanism |
| 6 | Cross-version instability in the rate resolver | **Pass 2** | **YES — invalidates a Pass 1 claim** | `MC-03`, `MC-10` |
| 7 | v19 ORM-core rate resolver, 11th rule, rule-bypassing, fourth fallback | **Pass 2** | **YES — new material class** | `MC-03`, `MC-10`, new `GATING` |
| 8 | Company-consistency enforcement surface; 16 inert guards | **Pass 3** | **YES — new population + new tolerance-zero candidate** | `MC-01`, `MC-08` |
| 9 | Cross-branch reconciliation and FX posting | **Pass 3** | **YES — new tolerance-zero-severity class** | `MC-03`, `MC-08`, `MC-10` |
| 10 | Entry identity as a boundary (`T0-08`) | **Pass 3** | **YES — eighth boundary** | `MC-08` |
| 11 | 9 unbounded negatives in the parent MC package | **Pass 3** | **YES** | `MC-05` |
| 12 | 4 gating reclassifications + 2 reversions | **Pass 3** | **YES** | `MC-06` |
| 13 | `P-13` = 22, not 21, and is author-derived under a source-derived label | **Pass 3** | **YES** | `MC-04` |
| 14 | Elevation-site count is 93 under the declared pattern; the accepted correction to 94 is itself wrong | **Pass 2 + Pass 3 concurring** | **Marginal** — corrects a correction | `MC-04` |
| 15 | Unit-of-count ambiguity: 12 vs 14 over the identical bounded surface | **Pass 1 ∩ Pass 2** | **YES — a new class of denominator defect** | `MC-01`, `MC-04` |
| 16 | The reviewer brief written by this session contained a wrong path | **Pass 2** | **YES, methodologically** | see §7 |
| 17 | Two candidate findings **rejected** on verification | Pass 1 + Pass 2 | Non-material to the gate | discipline evidence |

**Material deltas: 15. Non-material: 2.**

---

## 6. The fixed-point rule, applied

> **Convergence may be considered achieved only when two consecutive independent convergence passes
> produce: no new material population · no new material finding class · no new gating unknown · no
> reopened tolerance-zero issue · no denominator change affecting gate interpretation · no material
> semantic or control contradiction · a materially equivalent gate recommendation.**

| Criterion | Pass 2 | Pass 3 | Met by two consecutive passes? |
|---|---|---|---|
| No new material population | **NO** — 904 unsearched localisations, 962-module tree | **NO** — the enforcement surface | **NO** |
| No new material finding class | **NO** — v19 core resolver | **NO** — cross-branch reconciliation | **NO** |
| No new gating unknown | **NO** — `MCU-20` | **NO** — `MCU-21`, `MCU-22`, plus 4 reclassifications | **NO** |
| No reopened tolerance-zero issue | **NO** — the branch axis veto | **NO** — `T0-08`, `T0-09` | **NO** |
| No denominator change affecting gate interpretation | **NO** — bounding denominator, demo-data characterisation | **NO** — `P-13`, `P-15`, `SRC-F` | **NO** |
| No material semantic/control contradiction | **NO** — 2 Pass-1 claims invalidated | **NO** — 9 unbounded negatives, 6 misclassifications | **NO** |
| Materially equivalent gate recommendation | **YES** — all three passes recommend `HOLD` | **YES** | **YES — the only criterion met** |

> ## `FIXED POINT NOT REACHED`
>
> **Six of seven criteria fail, on both consecutive passes.** Only the gate recommendation is stable,
> and a stable recommendation reached by three passes that keep finding new material is evidence of
> the recommendation, not of convergence.

---

## 7. What the protocol proved about itself — the transferable result

Three facts, and they point the same way.

**1. The discovery asymmetry is now five rounds old and it did not break this time either.**
Every material correction in Wave A's history came from an independent reviewer and none from the
author — *including in the round convened to diagnose that pattern, and including in this round,
which was convened to close that round.* Pass 1 caught **one** of its own errors (the 14→20 surface).
It did not catch the other three; Passes 2 and 3 did.

**2. The author injected a defect into the control itself.**
The reviewer brief written by this session named the ORM core one directory too deep. A reviewer who
searched the literal path would have found nothing and scored a class-`B` result as class `A`.
`MCCR-A` found the real path, used it, and **reported the brief as defective**. The instrument was
mis-calibrated by the round administering the test, and only an independent operator noticed.
**A control designed by the author is not independent of the author.**

**3. Every remaining defect is one defect, wearing six costumes.**
The rate-table surface, the module tree, the localisation surface, the demo data, the version
comparison, the unit of count — six failures in this round alone, all the same shape:
**a proxy was substituted for the source, and the proxy was chosen by the person whose claim it
bounded.** A path stands in for a tree; a token list stands in for a file; an XML element stands in
for a loaded record; a regex stands in for a population; a count stands in for a definition.

> **The programme has now learned the complete form of the rule, one clause per round:**
>
> ### A denominator is `POPULATION` + `PATTERN` + `PATH SET` + `UNIT`, and none of the four may be chosen by the author of the claim it bounds.
>
> `GB-04` learned *population*. `GB-07` and `ER-CORE` learned *pattern*. This round learned *path set*
> — twice, once against itself — and *unit*. **The final clause is the one that has never been
> implemented, and it is the reason the other three keep failing.**

---

## 8. Verdict

> ## `NOT CONVERGED`
>
> **15 material deltas across two independent passes. Six of seven fixed-point criteria fail on both.
> Three of this round's own claims were invalidated, and the author caught none of them.**
>
> **This is not a failure of the round's evidence.** Fifteen of fifteen denominators reproduced under
> a third and fourth independent recount; the rate-table surface is the first fully-evidenced
> population in the programme's history; and eight gating unknowns closed against a prior record of
> zero.
>
> **It is a failure of the round's — and the method's — ability to bound its own search.** Which is
> the same finding the last two rounds returned, now stated precisely enough to be fixed.
