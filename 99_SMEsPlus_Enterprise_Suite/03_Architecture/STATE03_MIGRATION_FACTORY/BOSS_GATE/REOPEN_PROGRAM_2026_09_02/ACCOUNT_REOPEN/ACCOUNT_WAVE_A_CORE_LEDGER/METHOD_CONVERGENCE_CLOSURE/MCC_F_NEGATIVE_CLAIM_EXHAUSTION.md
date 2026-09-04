# MCC_F — NEGATIVE CLAIM EXHAUSTION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Applies `DR-NC-01` … `DR-NC-06`. Governs `MC-05`.

> **Recommendation only. Boss is the sole Final Approver.**
> `DR-NC-05` is treated as load-bearing: this scan was run as a **named, separately-tasked step**, by
> the author over their own package **and independently by a fresh reviewer over the parent's**.

---

## 1. Scope, declared

| Corpus | Files | Lines | Scanned |
|---|---|---|---|
| This round's package (`METHOD_CONVERGENCE_CLOSURE/*`) | **7** | **1,934** | **100%** |
| Parent MC package (`METHOD_CONVERGENCE/*`) | 15 | 2,507 | **100%**, by the adversarial pass |
| 64-file canonical baseline | 64 | 14,575 | **NOT scanned by this round.** `MCU-12` stands. Class `C` |

**Pattern.** Case-insensitive, over full lines, in two families:
*hard negatives* — `does not exist` · `there is no` · `there is none` · `no <noun>` · `never` ·
`nowhere` · `none exists` · `impossible` · `cannot` · `unreachable` · `unsupported` · `zero … in/anywhere`;
*completeness assertions*, which `DR-NC-02` treats identically — `complete` · `exhaustive` ·
`the only` · `in every case` · `bounded` · `closed` · `all of` · `every` · `fully` · `entire` ·
`the population is N`.

**Declared false-negative modes of this pattern:** a negative expressed as a table cell (`0`, `—`,
`none`) with no sentence; a negative expressed only as a count; a negative implied by a status word
(`ENUMERATED`, `CONVERGED`) rather than stated. **All three occur in this programme and two of them
carried the parent round's two false closures.** They were therefore triaged by reading the status
columns as well, not only by the token scan.

---

## 2. Token load

| Token | Parent MC (15 files) | This round (7 files) |
|---|---|---|
| `never` | 58 | 20 |
| `zero` | 43 | 19 |
| `anywhere` | 21 | 6 |
| `cannot` | 17 | 26 |
| `does not exist` | 9 | 2 |
| `there is no` | 9 | 3 |
| `always` | 5 | 10 |
| `impossible` | 5 | 0 |
| `no control` / `no validation` / `no rule` | 10 | 0 |
| `no such` | 4 | 1 |
| `unreachable` | 0 | 2 |

**A higher token density is not a worse result.** This round asserts more negatives *per line* than
its parent and asserts almost all of them **with a declared boundary attached in the same sentence**.
Density is not the metric; **unbounded** density is.

---

## 3. This round's own material negatives — every one triaged

| # | Claim | Search boundary | Class | Disposition |
|---|---|---|---|---|
| `F-01` | **No raw-SQL write to the rate table exists in the source root** | pattern + path set declared in `MCC_E00 §MCC-E-001`; `.py`, 1,752 dirs; re-tested by a fresh reviewer across **four** version trees with a line-wrap-tolerant second method | **`A`** | **STANDS** — the strongest negative this round makes |
| `F-02` | **No context flag skips Python constraint validation** | the ORM core validation routine, its five call sites, and an override search across every root | **`A`** | **STANDS**, independently reproduced |
| `F-03` | **No migration script touches the rate table** | the migration and upgrade directories of every root | **`A`** | **STANDS**, independently reproduced |
| `F-04` | **No custom module in the three project addon sets touches the rate table** | three declared copies, `.py`/`.xml`/`.csv` | **`B`** — deliberately **not** upgraded: which copy deploys is unknown | **STANDS as `B`** |
| `F-05` | **No `ir.rule` targets either reconciliation model anywhere in the tree** | inherited class `A`; **re-tested by this round over the archive tree, and again by a fresh reviewer over the 962 modules outside the primary tree** | **`A`, scope widened** | **STANDS and STRENGTHENED** |
| `F-06` | **A null-company tax-repartition row is not reachable** | the repartition model, the tax model's requiredness, the record rule | **`A` within the declared scope** | **STANDS** — one reviewer records it as unsearched by them, so it rests on this round alone |
| `F-07` | **No round has searched the archive tree** | the 64 baseline files + the 15 parent MC files | **`A`** | **STANDS** |
| `F-08` | **`_check_company_id` appears in 0 of the 64 baseline files** | token search **plus** semantic-variant search over all 64 | **`A`** | **STANDS** |
| `F-09` | *"The rate-table surface is complete at 14 files"* | this round's **first pass**, bounded to the primary tree | **`E` — CONTRADICTED, by its own author, same round** | **WITHDRAWN.** Corrected to 20 |
| `F-10` | *"The rate-table scoping model is stable across the v18 and v19 lines"* | a **token list**, not the files | **`E` — CONTRADICTED** by a fresh reviewer | **WITHDRAWN.** `MCC_E01 MCCX-02` |
| `F-11` | *"162 rows, every one NULL-company"* | the **data file**, not the loaded record | **`E` — CONTRADICTED** by a fresh reviewer | **WITHDRAWN.** `MCC_E01 MCCX-01` |
| `F-12` | **No mapping between the two unknown id schemes exists in any file** | all 79 package files | **`A`** | **STANDS** |
| `F-13` | **The pre-v18 framework core is not present in the searched roots** | every root named in `MCC_E00 §MCC-E-000` | **`C` — NOT SEARCHED, explicitly not `A`** | **STANDS as `C`** |
| `F-14` | **No tenant entity exists in the accounting or company model** | inherited from the parent, where **no pattern and no path set is stated** | **`B` — DOWNGRADED from the parent's implied `A`** | **RECLASSIFIED.** See §5 |

> **Three of this round's own negatives were contradicted — all three by a fresh independent pass, none
> by the author. That is the fourth consecutive round with that signature and it is reported as such.**

---

## 4. Parent-package negatives, triaged by the adversarial pass and verified here

| # | Claim | Class | Disposition |
|---|---|---|---|
| `F-20` | *"No `ir.rule` anywhere in the tree"* — scoped to the primary tree, stated as the system | **`B` as written** → **`A`** after the reviewer extended the search | **CONCLUSION SURVIVES; SCOPE STATEMENT WAS WRONG** |
| `F-21` | *"Populations with a source-derived denominator: **0** before this round"* | **`B`** — no pattern declared, and the same round records that 19 of the 64 files were never read by its own scan | **STANDS AS `B`** |
| `F-22` | *"The reference system has **no accounting-event object** — positively established"* | **`B` presented as `A`.** No pattern, no path set, no command in any of the 15 files | **RECLASSIFIED `B`.** It is load-bearing: it is the sole basis for one out-of-scope classification and for calling a population "unbounded by construction, not by omission" — **circular** |
| `F-23` | *"**No** tenant entity exists in the accounting domain or the company model"* | **`B`** — no boundary stated | **RECLASSIFIED `B`** |
| `F-24` | Rate-table scoping rules *"**6**, complete"*; config keys *"**5**, complete, `CONVERGED`"* | **`E`** — contradicted **inside the same package** | **STILL PUBLISHED AS `ENUMERATED`/`CONVERGED` IN THE LAYER-1 REGISTERS AT THE GATE BASELINE.** `GB-06` operating on `GB-06`'s own round |
| `F-25` | Storage constraints *"**11** · `ENUMERATED`"* | **`E`** — the true figure is 9 in 6 blocks, one of them empty | **STILL PUBLISHED AS 11** in two registers **and in the repeatability artefact itself** |
| `F-26` | *"**No Wave A blocker is routed.** Each item was checked … all answer no"* | **`B`** — no per-item evidence in the table | **PARTLY CONTRADICTED:** the bank-flow item's *mechanism* is a Wave A rewrite path on a posted fact and was routed with its semantics |
| `F-27` | The repeatability artefact's own command note: *"→ **only** access files. No `ir.rule` record anywhere in 797 addons"* | **`E`, minor** | The declared command, run verbatim, returns **five** files — the fourth is a translation catalogue the filter does not exclude. **The artefact whose purpose is repeatability misstates its own output, and cites a module count its own package had already corrected** |

---

## 5. The reclassifications that matter

> `MCU-60` and `MCU-61` were classified **`OUT OF SCOPE WITH EVIDENCE`**. Neither carries a search
> pattern or a path set in **any** file of the parent package. Under `DR-NC-01` and `DR-NC-03` they are
> **class `B` — not found in searched scope — and B is never converted to A.**
>
> **They are reclassified `UNKNOWN`.** This matters beyond bookkeeping: `MCU-60` is the sole support
> for declaring the accounting-event population *"unbounded by construction, not by omission"*. If the
> negative is class `B`, the population is unbounded **by omission until searched**, and the parent's
> distinction collapses.

---

## 6. `MCU-12` — 58.1% of the package still unscanned

| Position | Status |
|---|---|
| The parent's negative-claim scan covered 45 of 64 canonical files, 41.9% by volume | inherited, verified |
| The unscanned 19 files carry **377** raw negative-token hits, **1.9×** the load that was triaged | inherited, verified |
| **This round did not scan them either** | **stated plainly.** The round instruction confines scope to the targeted closure chain; extending to 14,575 lines of baseline would broaden it |
| **This round DID scan its own package in full, and the parent MC package was scanned in full by the adversarial pass** | **new — the first time any round's own output has been fully scanned** |

> **`MCU-12` REMAINS GATING. `MC-05` cannot be `MET`.** The control now exists as a demonstrated,
> separately-tasked step with a declared pattern and declared false-negative modes; it has been run
> over **22 files and 4,441 lines** across two rounds. It has **not** been run over the baseline.

---

## 7. Verdict

> ## `PARTIALLY VERIFIED`
>
> **What improved.** Every material negative in this round carries a declared pattern, a declared path
> set, a class letter, and — new — a declared **false-negative mode**. Three unbounded negatives were
> caught and withdrawn *within the round that made them*. Two class-`B` claims wearing class-`A`
> clothing were found in the parent and reclassified. The scan was run as a separately-tasked step in
> both directions.
>
> **What did not.** The author caught **none** of their own three. All three were caught by fresh
> independent passes — the fourth consecutive round with that result. `DR-NC-05`'s conclusion is
> therefore reinforced, not relieved: **the negative-claim control works only when it is executed by
> someone who did not write the claim.** No authoring rule has ever caught one of these in this
> programme.
>
> **`MC-05` NOT MET.**

---

> ### FIGURE-GOVERNANCE NOTICE — appended mechanically, package-wide
>
> **`MCC_00_CANONICAL_FIGURES_REGISTER.md` governs every published figure and disposition in this
> package.** Where a figure in this file differs from a row in `MCC_00`, **`MCC_00` governs**; the text
> here stands unedited so the lineage is visible (`DR-NC-06`).
>
> This notice was appended to **every** Layer-1 file by one command, after the independent audit panel
> found that this round had failed to propagate its own last correction to three of its own files
> (`MCC_J` `J-16`). It is the mechanism, not the intention, that `ER-CORE-3` requires.
