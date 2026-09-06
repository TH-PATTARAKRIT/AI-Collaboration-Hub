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
| **`B-31`** | **Handoff delivery is unevidenced programme-wide.** Peers evidence that they *wrote* handoffs; **no artefact anywhere evidences delivery to or receipt by P11**, and P11's consumption records are P11's assertions about itself. `P06` names the same class from the other side (`REV-E-23`) | **HIGH** |
| **`B-32`** | **Five claims P11 carried for a round were corrected by their owner at the new frozen head** — *"complete"* withdrawn, 447,384 unit-noted (posted population **417,700**), origin pointers **96.1 % → 78.03 %**, the period absence **re-scoped to 18.0**, the settlement chronology **withdrawn as containing no defect**. **P11 published a non-defect as a finding** | **HIGH** |
| **`B-33`** | **`P08` instructs that every row of its handoff to P11 is an 18.0 statement and *"no deployed database runs it"***. `DB-SM` — **99.987 % of the estate's posted entries** — runs **16.0**, whose core source *"is not on this host at all"*. **Every P08-sourced row in P11's registers is a source-line statement, including `P11-C-12`** | **`CRITICAL`** |
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
