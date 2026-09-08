# ACCOUNT_FINAL_CROSS_PACKAGE_DELTA_RECONCILIATION.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part E · deliverable **7 of 12**
**Scope:** **exactly one** Account cross-package reconciliation over the final owner SHAs. **No package was re-researched.**
**Surfaces:** P06 `a533fe9` · P08 `ca577be` · P09 `ab8c013` · P11 `79e1369` · P07 `ee2be30` **READ-ONLY**
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 0. What this reconciliation is, and what it deliberately is not

It runs the **seven checks the prompt names** across the four final owner surfaces, **by executed query**, and it fixes what it finds **inside the owning package in this same prompt**. It does **not** re-open a research question, re-derive a peer measurement, or create a new correction queue.

**Six issues were found. Five were fixed in this prompt. One is a governance act that is not the Account team's to perform.**

---

## 1. CHECK 1 & 5 — stale peer SHA references, and claims whose peer premise was withdrawn

**Method.** Every `*.md` at each of the four final surfaces, scanned for citations of any superseded owner head, each hit classified as *marked lineage* or *unmarked current claim*.

**Result: 34 marked as lineage · 62 unmarked.** The 62 are overwhelmingly **legitimate historical records** — checkpoint rows recording what was consumed at a named round, control-test records, intake-integrity tables whose whole purpose is to fix a moment. **A citation of a superseded SHA is not automatically stale; a *current claim* pinned to one is.**

**Two were current claims, and both were fixed:**

| id | Finding | Owner | Disposition |
|---|---|---|---|
| **`XR-01`** | `P11_AUTO_RESUME_STATE.md` §2 — P11's own control artefact — pointed a successor at **CORR3 heads**, three of which had moved. This is `B-37`'s defect | P11 | **FIXED** — current pin table published, CORR3 snapshot struck and retained, **intake effect measured: UNION 817 → 825, +8, −0**, and a per-claim statement of what moved and what did not. **`B-37` NOT closed** — the repair is evidenced and reserved to the gate |
| **`XR-02`** | `CI-11` / `CI-12` pinned to superseded peer heads in P11's candidate I/P/O pack | P11 | **FIXED** — re-pointed; `CI-11`'s substance did not move, `CI-12`'s did |

## 2. CHECK 3 — current denominator / population contradictions

**Method.** Every `*.md` at the four surfaces, scanned for *"all three deployed databases"* wording and for *"four frozen RC-05"* wording, each classified marked / unmarked.

> ### **`XR-03` — the single largest finding of this reconciliation.**
>
> `P08-C1` and `P08-C4` are **one correction with two limbs.** The frozen population moved from **three databases to four**, and that moves **both** the balance claim **and** the deletion-path install-state claim.
>
> **The owner pass corrected the balance limb at `58_` and left the install-state limb standing in four further carriers across two packages** — `P08` `54_`, `P08` `56_` (×2), and three P11 carriers. **`RC-05` and `RC-06` named the balance premise. Nothing pointed at the install-state premise, which rested on the identical population.**

| Carrier | Owner | Disposition |
|---|---|---|
| `54_P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` `P08-CONTRA-55` | P08 | **FIXED** — `P08-C4b` |
| `56_P08_POSTING_FINALITY_AND_CORRECTION_REGISTER.md` ×2 | P08 | **FIXED** — `P08-C4d`. **The THIRD carrier of the same claim**, found after two had already been corrected in this same prompt |
| `43_P08_DOUBLE_ENTRY_ENFORCEMENT_MATRIX.md` §3 | P08 | **FIXED by re-measurement, not re-scoping** — `P08-C4c`. The external balance-check control is **uninstalled in all four** extracts, and `NOT PRESENT` was not returned for it anywhere. **The finding is unchanged over a larger population, which is the only honest way a three-DB claim becomes a four-DB one** |
| `P11` `B-21`/`T0-14`, `CI-12`, CORR3 intake dispositions | P11 | **FIXED** — `P11-C6-04` |

**`XR-04` — the rows that were NOT re-measured are now a declared set, not a silent carry.** `P08-C4e` names, individually, the two current `FACT VERIFIED` rows still measured on three extracts, and states the blind spot as **`DB-T2` × {those two rows}**. They are not re-measured because **a state enumeration is not made false by a fourth extract, only narrower than it looks** — re-measuring it would be new research on an unchanged claim.

**Residual after fixes:** unmarked *"installed in all three deployed databases"* — **P06 0 · P08 0 · P09 0 · P11 0.**

## 3. CHECK 4 — handoff identifiers with more than one live meaning

### 3.1 `HO` — resolved
| Namespace | State at the final surfaces |
|---|---|
| **P08 live** | `P08-HO-01`…`P08-HO-14` — 14 distinct, contiguous, **one defining row each** |
| **P08 retired** | bare `HO-01`…`HO-06` in `25_` — **struck, banner at §0**, withdrawn from citation, not renumbered |
| **P06** | its own `HO-01`…`HO-06` — **untouched.** Not P08's to renumber, and **no longer colliding** once P08's ids are producer-qualified |

### 3.2 `XR-05` — **an unresolved collision, on the Veto namespace**

> **`AAS+-VETO-01` carries at least two different meanings across Account, in an unprefixed namespace.**
>
> | Owner | What `AAS+-VETO-01` means there |
> |---|---|
> | **P08** | *"`C-1` — every measurement must be re-issued with its predicate in executable form."* A **method** veto over P08's measurements |
> | **P09** | *"No implementation of the P09 management-accounting model may begin while the financial-event identity is undefined."* A **scope** veto over P09 implementation |
>
> **P11 already writes `P08 AAS+-VETO-01` with a producer qualifier in one place**, which shows the ambiguity was felt without being registered.

**Why this matters more than an ordinary namespace collision.** The Boss non-degradation ruling requires that **no Veto is silently discharged**. **A discharge recorded against a bare `AAS+-VETO-01` does not say which veto was discharged** — the exact failure mode the ruling forbids, made possible by an identifier rather than by anyone's intent.

**Disposition: NOT FIXED HERE, and deliberately so.**
- **Renaming another package's veto identifier is a governance act, not a reconciliation act.** An identifier belongs to the register that defines it, and Account has ruled before that a peer's identifiers are not the reconciler's to renumber.
- **Interim control, applied in this package's own text and recommended programme-wide:** every Account citation of this identifier must be **producer-qualified** — `P08/AAS+-VETO-01`, `P09/AAS+-VETO-01`.
- **Routed to the Boss Decision Matrix as `BD-ACC-04`.**

## 4. CHECK 2 — stale current claims superseded by a final correction

**The withdrawn tolerance rule and the `1e-7 = 3` figure.** Residual unmarked current carriers after the P11 correction: **P06 0 · P09 0.** In **P08** the surviving mentions are the **correction records themselves** (`17_` `P08-CONTRA-75`, `58_` §8.1, `64_` the delivered notification), each of which quotes the withdrawn wording and immediately withdraws it. **These are the record of the correction and are correct as written.** In **P11** they are the correction record plus this round's own disposition table, whose quoted wordings are now marked `WITHDRAWN` on their own lines.

> **`XR-06` — an artefact must not be indistinguishable from its own subject.** Three times in this prompt a correction's own text matched the sweep that found the defect: in P06 it moved a **published total from 67 to 69**; in P09 and P11 it would have returned the correction as new current-looking carriers. **In P06 it corrupted a count; elsewhere it only added noise — but the habit is the same and is now applied in all three.**

## 5. CHECK 6 — P07 read-only dependency consumption

| | |
|---|---|
| Opened | `19_P07_CORE_RECON_HANDOFF_PACK.md` at `ee2be30`, content SHA-256 `482fc987…` |
| Mutated | **No P07 file was written at any SHA on any branch in this prompt.** Verified: P07 appears in no diff |
| Routed question | *"whether a tax-reporting grouping may span companies, and within what security boundary"* — **registered verbatim, not answered** |
| Where it goes | Thailand Tax interface = **`ACCOUNT-HANDOFF-EXTERNAL-DECISION-PENDING`**; Boss Decision Matrix `BD-ACC-02` |

**`B-36`'s intake limb — an in-denominator artefact unopened for three rounds — is CLOSED.**

## 6. CHECK 7 — cross-package Input/Output consistency for Phase SA

Delivered as `ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md`. **Eleven interfaces classified, no global Account HOLD.**

## 7. The clean-room check this reconciliation added on its own initiative

**Not one of the seven, and it found a defect this session had itself created.**

A **mechanical vendor-token count delta against each baseline commit** showed `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` moving from **0 tokens at baseline to 5** — a module technical name, a registry table name and a restore-tool name, written by this prompt's own `P08-C1`/`P08-C4` edits into **the file that goes to P11**.

**Scrubbed to zero.** The identifiers live in the Layer 2 quarantine, which is now explicitly marked. **It was found by counting, not by reading**, and no challenge had run yet.

## 8. Disposition summary

| id | Finding | Owner | Status |
|---|---|---|---|
| `XR-01` | P11's resume state pointed a successor at superseded heads | P11 | **FIXED**; `B-37` open at the gate |
| `XR-02` | `CI-11`/`CI-12` pinned to superseded peer heads | P11 | **FIXED** |
| `XR-03` | the install-state limb of a two-limb peer correction, live in 5 carriers across 2 packages | P08, P11 | **FIXED** |
| `XR-04` | rows measured on three extracts, carried without a stated boundary | P08 | **FIXED — declared as a set** |
| `XR-05` | **`AAS+-VETO-01` has two live meanings across Account** | Boss | **OPEN — `BD-ACC-04`.** Interim: producer-qualified citation |
| `XR-06` | a correction's text matching its own sweep | all | **FIXED in three packages** |
| clean-room | 5 vendor tokens introduced into a Layer 1 handoff by this prompt | P08 | **FIXED** |

**Five fixed inside this prompt. One routed to Boss because it is a governance act. No new correction queue was created.**
