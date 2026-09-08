# P11 — CORR3 POPULATION REGISTERS (blockers · tolerance-zero · decisions · errors)

`[SMEPLUS-26-09-06-…-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-07` · **PHASE S**

> Re-derived by execution. **No item closes because wording improved. No Boss item is decided by P11.**

---

## 1. Blockers — movement

| id | CORR2 | **CORR3** | Basis |
|---|---|---|---|
| `B-23` | withdrawn as worded | **stays withdrawn** | `P09` `D26`. Confirmed at the new head `4778792` |
| `B-26` | bounded to 2 valuation-layer zeros | **bounded holds, and widens by mechanism** | `P08` `P08-HO-13` — the same class of raw-SQL deletion reaches the **settlement table** as well |
| `B-28` | *"largest unrecognised accounting position"* | **RE-WORDED — `CANDIDATE INPUT — NOT PROMOTED`** | The owner classifies it a **timing position expected under periodic valuation**, *"P08's judgement and the Boss's decision"*. **The defect was P11's non-intake, not the position** |
| `B-29` | `P08 AAS+-VETO-01` unrecorded | **RECORDED · conditions UNDISCHARGED** | `62_` confirms `AAS+-PS-VETO-01` *"does not lift"* it. **P11 does not discharge a peer veto** |
| `B-21` / `T0-14` | one v19 non-target database | ~~**STRENGTHENED — installed in ALL THREE deployed databases**~~ → **installed in ALL FOUR FROZEN RC-05 EXTRACTS** **[`P11-C6-04`, 2026-09-08 — population premise re-pointed to P08 `82df5f3df8faec484a27146eb1f1d8b652424293`.** The deletion module records an **installed** state in **all FOUR frozen RC-05 extracts**, read from each extract's own module registry. **Four frozen extracts are NOT an established deployment census** and P11 does not upgrade them into one. **`exercised` remains NOT ESTABLISHED** — install state is capability, not act.]** | `P08` `P08-HO-13`. Scope corrected across two generations. **`exercised` still NOT ESTABLISHED** |

## 2. Blockers — new

| id | Blocker | Class |
|---|---|---|
| **`B-31`** | ~~Handoff delivery is unevidenced programme-wide~~ **FALSIFIED AND RE-WORDED.** `23_P10_PEER_INTAKE_REGISTER.md` records receipt of **four P11-origin items** (`IN-10`…`IN-13`) with a verification column and a **reasoned refusal** (`RF-02`); `P06_AUTO_RESUME_STATE` L16-17 is a working receipt record. **And `P06` already carries this as a standing veto — `AASP-VETO-06`, *"a handoff is not delivered by being written"* — which appears nowhere in P11's tree.** P11 cited the weaker `REV-E-23` because the stronger sits in the instrument's blind zone. **Surviving claim: no artefact records a RECIPIENT ACKNOWLEDGING a specific handoff back to its sender; consumption records exist on both sides and are unpaired and self-attested** | **MEDIUM** (downgraded) · **and it broke P11's own §5 absence rule** |
| **`B-32`** | **Five claims P11 carried for a round were corrected by their owner at the new frozen head** — *"complete"* withdrawn, 447,384 unit-noted (posted population **417,700**), origin pointers **96.1 % → 78.03 %**, the period absence **re-scoped to 18.0**, the settlement chronology **withdrawn as containing no defect**. **P11 published a non-defect as a finding** | **HIGH** |
| **`B-33`** | **REGISTERED, NOT APPLIED (`X4-C5`) — and it receives the absolute it forbids (`X4-C4`).** The 18.0 qualifier reaches **2** rows (`T0-15`, `P11-C-12`); **nine** P08-sourced rows are published unqualified. And `IC-01`'s accrual control (*0 of 15,522*) is **sourced from a deployed series-18 database** while this blocker registers `CRITICAL` that no deployed database runs 18.0. **`P08`'s scope is *every kernel claim in that handoff*, not P08's deployed counts** — the 169,143 / 417,700 / 5,228 measurements are 16.0/19.0. Original wording: **`P08` instructs that every row of its handoff to P11 is an 18.0 statement and *"no deployed database runs it"***. `DB-SM` — **99.987 % of the estate's posted entries** — runs **16.0**, whose core source *"is not on this host at all"*. **Every P08-sourced row in P11's registers is a source-line statement, including `P11-C-12`** | **`CRITICAL`** |
| **`B-34`** | **A new duplicate mechanism.** `P08-HO-13`'s deletion path **resets the entry-number sequence to 1**, so *"previously-issued numbers [may] be re-issued"* — a duplicate-identity risk on the one field the ledger uses as a human-facing key | **HIGH** |

## 3. Position

| | CORR2 | **CORR3** |
|---|---|---|
| Registered | 30 | **34** |
| Open | 26 | **30** |
| `CRITICAL` open | 3 | **4** (`B-21`, `B-26`, `B-27`, `B-33`) |
| Closed by completed work | 1 | **1** (`B-18`) |
| Contradicted-corrected | 2 | **3** (`B-22`, `B-23`, **`B-28` re-worded**) |

## 4. Tolerance-zero

| id | Movement |
|---|---|
| `T0-14` | **strengthened** — installed in **three** deployed databases (`P08-HO-13`) |
| **`T0-15`** | **RE-SCOPED — 18.0 source line only.** `P08-CONTRA-68`: the 19.0 line carries a dated recurring return object and both 19.0 databases carry its linking column. ***"P11 must not receive the absolute."*** **This is the first tolerance-zero boundary this package has ever narrowed** |
| **`T0-16`** *(new)* | **A settlement graph offered as reconcilable is deletable outside the object layer, and the entry-number sequence can be reset to 1.** `P08` withdraws its own control: *"`56` §2 ranked settlement referential integrity as the one control that **holds** — it does not"* |

**`16` boundaries · `0` resolved · `1` re-scoped (first ever) · `CONDITIONAL PASS` unavailable by rule.**

## 5. Boss decisions

**`19` — unchanged in population, `0` decided by P11.**

`D-1` context is **materially better evidenced and still undecided**:
- `P09`: the **source** generation of its declared root is established — **18.0 Enterprise** — *"a
  discharge in P09's favour, found by a challenger and not by the author"*; **`installed`,
  `configured`, `exercised`, `economically correct` all remain `NOT ESTABLISHED`**.
- `P08`: **`DB-SM` runs 16.0 and holds 99.987 % of the estate's posted entries; its core source is not
  on this host.** The two 19.0 databases' source **is** on the host and *"was never searched"*.
- **Consequence for the Boss:** `D-1` now bounds **`B-20`, `B-21`, `B-23a`, `B-33`** — four blockers,
  one of them `CRITICAL`. **P11 writes no decision and infers no approval from silence.**

## 6. Errors

**`41` ids.** New: **`P11-E-41`** — *P11 promoted a peer's timing position to "the largest unrecognised
accounting position" without carrying the owner's own classification of it.* CORR2 registered `B-28`
from a heading (*"THE NUMBER P11 AND P08 BOTH NEED"*) and from the figure, **without reading the two
paragraphs beneath it** that classify it as a timing position expected under periodic valuation and
route the judgement to `P08` and the Boss. **The same defect class as quoting a superseded claim: the
evidence was open on the page and the reader stopped early.**

**`CP-P11C3-07` — COMPLETE — EVIDENCE VERIFIED.**


---

## 7. CORR3 CHALLENGE ADDENDUM — `2026-09-06` · after `CP-P11C3-09`

### 7.1 New blockers

| id | Blocker | Class |
|---|---|---|
| **`B-35`** | **The intake instrument is not certifiable, and CORR3 certified it.** Six confirmed defects: lexical tail; generation-discarding key; substring membership; tautological blind-spot table; fitted `TAIL`; vacuous failure control. **And the control set was truncated** — P11's own log names 12 lost artefacts, P11 tested 10, and `S06` (one of the two dropped) **fails**. `S06` carries **`NC-8`**: *"No `head`, `tail`, sampling, `limit`, or first-N command may bound a population"* — **`D3` is a tail bounding this denominator**. **OWNER REBUILD PUBLISHED `2026-09-08` (`P11-CORR4-C1`) — `B-35` REMAINS OPEN.** The successor `LAYER2_P11_EVIDENCE/corr4_instrument/intake_derivations_v3.py` repairs all six and one more the rebuild itself uncovered: **chronological ordering** by last-commit author time (printed); **full-path identity key** (the basename key would have collapsed **294** basenames carrying more than one path); **bounded peer token** (the raw-substring rule admitted **70** files whose names merely contain `STEP01`/`STEP02`/`STEP03`, matching `P01`/`P02`/`P03`); **measured complement instead of a defined blind-spot table** (**9,649 of 10,474** `*.md` paths selected by no derivation); **bound removed** — the sensitivity curve is `tail 1→94 · 2→102 · 3→108 · 5→126 · 8→152 · 13→200 · 21→270 · unbounded→825`, so the fitted `TAIL=5` discarded **84.7 %** of the population; and **four controls that can fail**, all four run and behaving as expected. **Newly found in the rebuild: the derivation was cwd-dependent** — `git grep <ref> -- "*.md"` and `git log <ref> -- <path>` resolve their pathspec against the working directory, so run from inside the package `D2` returned **0** and every commit time returned **0**. Run from the repository root `D2` = **51**. **A zero that is a scope error is indistinguishable from a zero that is a result**, and it was caught only by re-running the query in a second form. **`B-35` may close only on independent certification of the rebuilt instrument against the full twelve-control set including `S06`. That certification has NOT occurred and P11 does not self-certify.** | **`CRITICAL` — OPEN** |
| **`B-36`** | **`19_P07_CORE_RECON_HANDOFF_PACK.md` — inside the union, inside `ADDRESSED`, never opened.** Titled *"CORE ACCOUNTING RECONCILIATION HANDOFF PACK"*, terminal state *"READY FOR CORE ACCOUNTING RECONCILIATION"*, carrying a company-spanning tax-grouping scope ruling **routed to P11**. ~~**P11 has not opened P07 at any SHA across three rounds**~~ **CONSUMED `2026-09-08` (`P11-CORR4-C3`), READ-ONLY, at the declared frozen SHA `ee2be30ebf155e241510b3c7133c69419eb060a0`.** File `…/P07_TH_TAX_TO_COMPLIANCE_EXECUTION/19_P07_CORE_RECON_HANDOFF_PACK.md`, content SHA-256 `482fc987e86a758b74936ae6f18175dcb5e49485da4244bd29eb1cac95efb56c`. **P07 was not mutated and no P07 file was written.** The routed question, transcribed from §6: **"A ruling on whether a tax-reporting grouping may span companies, and within what security boundary."** **P11 registers it and does NOT answer it.** It is a **downstream Account/Tax interface decision reserved to Boss**, not a Phase S finding: the evidence does not determine it, and answering a design question in Phase S is outside P11's authority. **It is not a reason to block Account closure** — see `ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md`, where the Thailand Tax interface is classified `ACCOUNT-HANDOFF-EXTERNAL-DECISION-PENDING` on exactly this item. **The intake defect `B-36` names — an in-denominator artefact left unopened for three rounds — is CLOSED. The routed question it carried is OPEN and owned by Boss.** | **HIGH — intake limb CLOSED, routed decision OPEN** |
| **`B-37`** | **`P11_AUTO_RESUME_STATE.md` instructs the successor to use superseded heads.** At the frozen SHA it reads *"Frozen Peer Snapshot — **DO NOT RE-RESOLVE**"* over `P06 1b018c1 · P08 00ccd66 · P09 4778792` — the **CORR2** heads — and reports 40 errors against 41. **P11's own control artefact would rebuild CORR3's denominator on the wrong snapshot** | **HIGH** |
| **`B-38`** | **RE-STATED `2026-09-07` against `P09`'s SUBSTANTIVE head `4778792` (`Q-P11-03` / `XRD-008`).** ~~*"an unexecuted L1–L8 correction set"*~~ — **SUPERSEDED, retained as lineage.** At `4778792` the L-series is **executed**: `E05_L1_L8_EVIDENCE.md` carries `L-1`, `L-2`, `L-4`, `L-5`, `L-7`, `L-8` with instrument outputs (`L1_L2_L8.py`, `L2_k3_control.py`, `L4_L5.py`), `L-4` split, corrections applied in place. **P11 read a *prompt* commit (`92de8a1`) and reported its correction set as unexecuted.** **The surviving limb, unchanged and still true: `AAS+-VETO-04` is `NOT DISCHARGED`** — P09's own words: *"Its condition requires the K-2 correction surface complete **and re-tested**"*, and K-2's materiality is withdrawn, so the condition is unmet. **Unlock re-pointed to `P09`'s own named next actions `M-1` and `M-2`** — `M-1` *"resolve `L-4`'s authority"*; `M-2` the challenge that *"has not run"* on the corrected surface. **P11 does not discharge `AAS+-VETO-04` and does not close `B-38`.** **REFRESHED `2026-09-08` (`P11-C6-03`) against P09's final owner SHA `ab8c0131c46e8154ad7efae18de2a54af2f17362`:** **`M-1` is now RESOLVED at that SHA** — P09 withdrew the false universal that reference is disjoint from declaration/inheritance/K-1 *"by construction"* (its own executed denominator puts **23 files inside K-1 and in the reference relation**) and re-grounded the authority on the proven partition boundary `B2 ⊂ B`, `B = 192 ∖ K-1`. **`M-2` is NOT resolved** — it is the challenge that must run on the corrected surface, and an owner cannot run it on itself. **`AAS+-VETO-04` therefore remains NOT DISCHARGED, and `B-38` remains OPEN.** **P11 consumed P09's published state; it did not re-derive P09's denominator and did not adjudicate `M-2`.** | **HIGH — OPEN** |
| **`B-39`** | ~~**`P08-HO-14` vs `P07-F-02`/`F-03` is an unregistered cross-process contradiction**~~ **RE-STATED `2026-09-08` (`P11-CORR4-C4`): `VERSION-SPLIT / NO DIRECT CONTRADICTION`.** The two statements are about **two generations of the system and are both true of theirs**: **`P08-HO-14` is `S16c` / `DB-SM` evidence at generation 16.0** — the statutory register family selecting on two different period bases, 5,228 entries; **`P07-F-02`/`F-03` describe the v19 migration state in which the substitution was removed.** **A mechanism present at 16.0 and removed at 19.0 is not a contradiction; it is a version history.** **Both generations are preserved and are NOT merged into one runtime truth** — the deployed estate contains more than one generation, so *"the system does X"* has no single referent here and neither finding may be restated without its generation. **What remains open is not a contradiction but a scope question:** which generation any given deployment runs, which is a per-deployment fact P11 does not hold. **No statutory determination is made or implied.** | **MEDIUM — RE-CLASSIFIED, contradiction limb CLOSED** |

### 7.2 `B-28` — re-instated, at the right figure

**`X1-5` accepted in substance.** `P01` routes the **judgement** to `P08` and the **decision** to Boss; it
does **not** remove the position from P11's carriage — it hands it to P11 by name. CORR2 over-claimed;
**CORR3 over-conceded, and both errors read the owner's framing instead of the owner's evidence.**

**`B-28` re-instated as a carried candidate**, stated at the figure the evidence supports:
**`฿27,490,865.80` across 1,411 receipted PO lines**, against clearing account `210300`
*"Uninvoiced Receipts"* — **configured, reconcilable, effective on 171 of 504 (category, company) pairs,
carrying `0` journal items** with a 144-account / 6-journal positive control. **`฿1,538,601.86` on 169
service lines is carved out** as operator-typed with no receipt document. **Carrying is not promoting
and is not deciding.**

### 7.3 Position

| | before challenge | **after** |
|---|---|---|
| Registered | 34 | **39** |
| Open | 30 | **35** |
| `CRITICAL` open | 4 | **5** (`B-21`, `B-26`, `B-27`, `B-33`, `B-35`) |
| `B-31` | HIGH | **MEDIUM, re-worded** |
| Errors | 41 | **43** |

> **`B-27` is NOT discharged.** The instrument is published — necessary, not sufficient — and it is
> defective in six named ways. **CORR3 did not repair intake integrity. It measured how far from
> repaired it is, which is a smaller and more honest result.**
