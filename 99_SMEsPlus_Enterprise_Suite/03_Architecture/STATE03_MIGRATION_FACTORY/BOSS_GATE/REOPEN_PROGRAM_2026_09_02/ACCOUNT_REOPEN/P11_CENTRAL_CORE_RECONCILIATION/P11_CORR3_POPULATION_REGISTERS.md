# P11 — CORR3 POPULATION REGISTERS (blockers · tolerance-zero · decisions · errors)

`[SMEPLUS-26-09-06-…-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-07` · **PHASE S**

> Re-derived by execution. **No item closes because wording improved. No Boss item is decided by P11.**

---

## 1. Blockers — movement

| id | CORR2 | **CORR3** | Basis |
|---|---|---|---|
| `B-23` | withdrawn as worded | **stays withdrawn** | `P09` `D26`. Confirmed at the new head `92de8a1` |
| `B-26` | bounded to 2 valuation-layer zeros | **bounded holds, and widens by mechanism** | `P08` `HO-13` — the same class of raw-SQL deletion reaches the **settlement table** as well |
| `B-28` | *"largest unrecognised accounting position"* | **RE-WORDED — `CANDIDATE INPUT — NOT PROMOTED`** | The owner classifies it a **timing position expected under periodic valuation**, *"P08's judgement and the Boss's decision"*. **The defect was P11's non-intake, not the position** |
| `B-29` | `P08 AAS+-VETO-01` unrecorded | **RECORDED · conditions UNDISCHARGED** | `62_` confirms `AAS+-PS-VETO-01` *"does not lift"* it. **P11 does not discharge a peer veto** |
| `B-21` / `T0-14` | one v19 non-target database | **STRENGTHENED — installed in ALL THREE deployed databases** | `P08` `HO-13`. Scope corrected across two generations. **`exercised` still NOT ESTABLISHED** |

## 2. Blockers — new

| id | Blocker | Class |
|---|---|---|
| **`B-31`** | ~~Handoff delivery is unevidenced programme-wide~~ **FALSIFIED AND RE-WORDED.** `23_P10_PEER_INTAKE_REGISTER.md` records receipt of **four P11-origin items** (`IN-10`…`IN-13`) with a verification column and a **reasoned refusal** (`RF-02`); `P06_AUTO_RESUME_STATE` L16-17 is a working receipt record. **And `P06` already carries this as a standing veto — `AASP-VETO-06`, *"a handoff is not delivered by being written"* — which appears nowhere in P11's tree.** P11 cited the weaker `REV-E-23` because the stronger sits in the instrument's blind zone. **Surviving claim: no artefact records a RECIPIENT ACKNOWLEDGING a specific handoff back to its sender; consumption records exist on both sides and are unpaired and self-attested** | **MEDIUM** (downgraded) · **and it broke P11's own §5 absence rule** |
| **`B-32`** | **Five claims P11 carried for a round were corrected by their owner at the new frozen head** — *"complete"* withdrawn, 447,384 unit-noted (posted population **417,700**), origin pointers **96.1 % → 78.03 %**, the period absence **re-scoped to 18.0**, the settlement chronology **withdrawn as containing no defect**. **P11 published a non-defect as a finding** | **HIGH** |
| **`B-33`** | **REGISTERED, NOT APPLIED (`X4-C5`) — and it receives the absolute it forbids (`X4-C4`).** The 18.0 qualifier reaches **2** rows (`T0-15`, `P11-C-12`); **nine** P08-sourced rows are published unqualified. And `IC-01`'s accrual control (*0 of 15,522*) is **sourced from a deployed series-18 database** while this blocker registers `CRITICAL` that no deployed database runs 18.0. **`P08`'s scope is *every kernel claim in that handoff*, not P08's deployed counts** — the 169,143 / 417,700 / 5,228 measurements are 16.0/19.0. Original wording: **`P08` instructs that every row of its handoff to P11 is an 18.0 statement and *"no deployed database runs it"***. `DB-SM` — **99.987 % of the estate's posted entries** — runs **16.0**, whose core source *"is not on this host at all"*. **Every P08-sourced row in P11's registers is a source-line statement, including `P11-C-12`** | **`CRITICAL`** |
| **`B-34`** | **A new duplicate mechanism.** `HO-13`'s deletion path **resets the entry-number sequence to 1**, so *"previously-issued numbers [may] be re-issued"* — a duplicate-identity risk on the one field the ledger uses as a human-facing key | **HIGH** |

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
| `T0-14` | **strengthened** — installed in **three** deployed databases (`HO-13`) |
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
| **`B-35`** | **The intake instrument is not certifiable, and CORR3 certified it.** Six confirmed defects: lexical tail; generation-discarding key; substring membership; tautological blind-spot table; fitted `TAIL`; vacuous failure control. **And the control set was truncated** — P11's own log names 12 lost artefacts, P11 tested 10, and `S06` (one of the two dropped) **fails**. `S06` carries **`NC-8`**: *"No `head`, `tail`, sampling, `limit`, or first-N command may bound a population"* — **`D3` is a tail bounding this denominator** | **`CRITICAL`** |
| **`B-36`** | **`19_P07_CORE_RECON_HANDOFF_PACK.md` — inside the union, inside `ADDRESSED`, never opened.** Titled *"CORE ACCOUNTING RECONCILIATION HANDOFF PACK"*, terminal state *"READY FOR CORE ACCOUNTING RECONCILIATION"*, carrying a company-spanning tax-grouping scope ruling **routed to P11**. **P11 has not opened P07 at any SHA across three rounds** | **HIGH** |
| **`B-37`** | **`P11_AUTO_RESUME_STATE.md` instructs the successor to use superseded heads.** At the frozen SHA it reads *"Frozen Peer Snapshot — **DO NOT RE-RESOLVE**"* over `P06 249b7c2 · P08 194efcb · P09 5441f8d` — the **CORR2** heads — and reports 40 errors against 41. **P11's own control artefact would rebuild CORR3's denominator on the wrong snapshot** | **HIGH** |
| **`B-38`** | **`P09` declares its own package internally contradictory at the head P11 dispositioned as `CONSUMED`.** `P09_..._L1_L8_FINAL_BOUNDED_CORRECTION_NEXT_PROMPT` (inside `D1`, unopened): *"P09 carried a fact and its negation in the same package"*; `AAS+-VETO-04` **NOT DISCHARGED**; an unexecuted L1–L8 correction set. §5's own reversal trigger fires here and was not applied | **HIGH** |
| **`B-39`** | **`HO-14` vs `P07-F-02`/`F-03` is an unregistered cross-process contradiction**, and the two statements may be true of **different generations** — `P07` says the tax-point substitution *"was removed in the v19 migration"*; `HO-14`'s 5,228 is a **`DB-SM` 16.0** count | **MEDIUM** |

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
