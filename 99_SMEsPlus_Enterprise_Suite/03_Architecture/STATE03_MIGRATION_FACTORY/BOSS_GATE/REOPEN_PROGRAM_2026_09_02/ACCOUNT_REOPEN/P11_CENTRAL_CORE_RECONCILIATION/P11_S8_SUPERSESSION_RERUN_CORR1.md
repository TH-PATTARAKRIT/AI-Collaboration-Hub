# P11 — `S8` SUPERSESSION RE-RUN ACROSS ALL TEN PEERS

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · `CP-P11C13` · Layer 1 clean-room

> **Why this exists.** `P11-E-31`: P11 built the round's headline on `25_P08_CORE_RECON_HANDOFF_PACK.md`
> while `52_P08_CORE_RECON_HANDOFF_PACK_V2.md` existed at the same SHA and withdrew the claim. The
> AAS-03 challenge named the ordering surface `S8` — *a peer publishing more than one handoff artefact* —
> and P11 then checked **two** peers. `AASP-C1-R-02` recorded the remaining **eight as unbounded**.
> **This is that check, executed over all ten.**

---

## 1. Declared denominator — before anything was opened

| Element | Declaration |
|---|---|
| **POPULATION** | The **10** peer branches at the **exact SHAs `P11_PEER_DELTA_INTAKE_CORR1.md` consumed** — not their current heads. A later head is a different question (`P11-F-08`); this asks whether P11 mis-read the SHA it *had*. |
| **PATTERN** | `git ls-tree -r --name-only <SHA> \| grep -Ei 'HANDOFF\|CORE_RECON'` — **published verbatim, and executed, not quoted** |
| **PATH SET** | The **whole tree** at each SHA. Not the peer's own directory — that assumption is what produced `S8` |
| **UNIT** | **one path = one artefact.** Not "one peer = one handoff" — the unit conflation that caused the defect |
| **POSITIVE CONTROL** | The scan **must** return `52_P08_…_V2` and `71_P10_…`. If either is missing the scan is inert and its zeros mean nothing |
| **NEGATIVE CONTROL** | The generic programme-wide templates (`SMEPLUS_NEXT_STATE_HANDOFF_TEMPLATE_L99.md`, `STATE_HANDOFF_RULE.md`, …) appear in **all ten** trees and are **excluded by inspection**, not by pattern — they are a constant, so a peer differing from them is a real difference |

### 1.1 The instrument failed first, and the control caught it — **before publication this time**

The first execution returned **`(no name-pattern match)` for all ten peers, including P08 and P10.**
Cause: `for pair in "P01 49d0fe3" …; do set -- $pair` — **zsh does not word-split unquoted parameters**,
so `$2` was empty and every `git ls-tree` ran against an empty ref.

> **A `0` from a broken loop is indistinguishable from a `0` meaning "no supersession anywhere",** and
> that second reading would have *confirmed the comfortable answer* — that only P08 and P10 had the
> problem. **The positive control is the only reason this file says six and not zero.**
>
> **Fifth instance of the inert-pattern class in this package.** It is the first caught **before** a
> conclusion was drawn rather than after. That is the rule finally operating as designed, not the rule
> ceasing to be needed.

---

## 2. Result — **6 of 10 peers carry a later artefact P11 did not consume**

| Peer | Consumed by C8 | Also present at the same SHA | Verdict |
|---|---|---|---|
| `P01` | `P01_CORE_RECON_HANDOFF_PACK.md` | *(`P01_SUBCONTRACT_PURCHASE_HANDOFF.md` — different subject)* | **CLEAN** |
| `P02` | `19_P02_CORE_RECON_HANDOFF_PACK.md` | — | **CLEAN** |
| `P03` | `24_P03_CORE_RECON_HANDOFF_PACK.md` | **`37_P03_SCOPE02_P11_HANDOFF.md`** | **MISSED — addressed to P11 by name** |
| `P04` | `19_P04_CORE_RECON_HANDOFF_PACK.md` | *(`06_P04_DEPRECIATION_COST_HANDOFF.md` — earlier, different subject)* | **CLEAN** |
| `P05` | `19_P05_CORE_RECON_HANDOFF_PACK.md` | **`57_P05_HANDOFF_COMPLETENESS_V2.md`** *(supersedes `28_`)* | **MISSED** |
| `P06` | `18_P06_CORE_RECON_HANDOFF_PACK.md` | **`70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md`** | **MISSED — `CRITICAL`, addressed to P11 by name** |
| `P07` | `19_P07_CORE_RECON_HANDOFF_PACK.md` | — | **CLEAN** |
| `P08` | `25_P08_CORE_RECON_HANDOFF_PACK.md` | **`52_…_V2`** *(supersedes `25_`)* | **MISSED — known, `P11-E-31`** |
| `P09` | `18_P09_CORE_RECON_HANDOFF_PACK.md` | **`S18_P09_P11_SUPPLEMENTAL_CRITICAL_EVIDENCE_HANDOFF.md`** **and `S23_P09_POST_PUBLICATION_CORRECTION.md`** | **MISSED — two deep** |
| `P10` | `18_P10_CORE_RECON_HANDOFF_PACK.md` | **`37_…_V2`**, **`71_…`** *(`71_` supersedes both)* | **MISSED — known** |

> ### `P11-F-14` — the defect was never a two-peer defect. **It is 6 of 10, and P11 stopped at the two it was told about.**
>
> `P11-E-28` says *rank the population before choosing*. P11 applied it to database dumps and **not to
> the peer artefacts the whole round is built from** — the largest population in the package. The
> command that produced this table is **one line** and could have run before the first peer was opened.

### 2.1 A supersession chain runs **two deep**, which no version-check for "a V2" would find

`P09`'s `S18_` is itself corrected by `S23_`, and `S18_` **says so in its own header**. A check asking
*"is there a `_V2`?"* returns **NO** for P09 — both filenames are `S`-prefixed sequence numbers.
**`P11-G-04` v2 binds at artefact level and is still insufficient**: it must bind at
**claim** level — *read every artefact of the peer, in sequence order, and take the last statement of
each claim.* Issued as **`P11-G-04` v3**.

---

## 3. What the six missed artefacts actually change

### 3.1 `P06` `70_` — a `CRITICAL` that changes the package's risk headline

> **`om_data_remove` is INSTALLED on a real Odoo 19 database in this programme's estate.** It deletes
> bank statements, payments, journal entries, journal items, reconciliations **and the audit trail** by
> unfiltered `DELETE FROM`, committing per table and swallowing errors. **17 copies**, three rebranded
> *SMEsPlus Remove Data*, one locally extended for this project's Thai withholding-tax certificates.

P06 classifies it **`DESTRUCTIVE PATH VERIFIED`** / **`NO SERVER-SIDE AUTHORIZATION VERIFIED`** /
**`REACHABLE — DEPLOYMENT VERIFIED`**, and **answers the question `P08` left open** (`P08-T0-08`:
*"whether the underlying methods are reachable by a lower-privileged direct call is `D UNKNOWN`"*).
A first-party remediation module states the destructive path **has already been run**.

**Registered `P11-B-21` (`CRITICAL`) and tolerance-zero `T0-14`.** *(Deployment is on a v19 database
**not confirmed to be the SMEsPlus target** — the `D-1` dependency again, recorded, not elided.)*

### 3.2 `P09` `S23` — P11 carries a withdrawn figure, and the correction is the wrong way

`P11_PEER_INTAKE_DELTA_01.md:72` states the cost-centre attribution route **"nets to zero"**.
**`S23` withdraws it**, re-measured by the author before acceptance:

> **The net is `+3,595,851.11` — a sign-inverted CREDIT, not zero. Depreciation makes the cost centre
> look *more profitable*.** *"Materially worse than zero, and no document in the package said it."*

`TH-F-02` likewise is not a depreciation-pair effect but a **277 M swing** across **169,954** additional
records, on **one of four** v19 builds — and P09 names its own cause as *"an asset-derived subset, not
the population — **the programme's own denominator rule, missed again**."*

**`P11_PEER_INTAKE_DELTA_01.md` corrected in place. Registered `P11-B-22`.**

### 3.3 `P09` `S18` — a version-basis `CRITICAL` that bounds every P09 claim P11 holds

> *"P09's mechanism claims are read from a platform version that no deployment runs. One deployment runs
> version 16; three run version 19; the source is version 18."*

**No P09 mechanism claim may be treated as describing a running system.** The *measurements* are
unaffected. **Registered `P11-B-23`**, and it compounds `P11-B-20` (`P01`: the v19 databases have no
GRNI account) — **two peers, independently, say P11's matrix is written against an undeclared
generation.**

### 3.4 `P03` `37_` — three more decisions routed to P11 by name

| Routed | Question |
|---|---|
| `P11-D-1` | May a scope narrowing established for one object be read across to a related object? |
| `P11-D-2` | What closes a scope defect whose specified closing evidence returns an **empty population**? (`0 of 0` across three databases) |
| `P11-D-3` | Is `MA-11` (`P09`) binding on `P01`–`P10`? |

**Decision population 13 → 16, and still a declared floor.** P03 also states what P11 must **not** be
asked: *"To adjudicate the monetisation count. Four units are declared and all four counts are
published."* **P11 declines it, as asked.**

### 3.5 `P05` `57_` — supersedes `28_`; one element moved **backwards**

**2 COMPLETE · 4 PARTIAL — EXACT GAP · 4 BLOCKED.** `HE-08` moved from `NOT APPLICABLE — EVIDENCE
VERIFIED` to **`PARTIAL — RE-OPENED`** because the corrected population contradicted its closure —
*"the honest direction of travel"*. `HE-09` needs **the platform event-identity primitive — P11**, and
is therefore a fifth peer requiring `D-5`.

### 3.6 `P08` `52_V2` and `P10` `71_` — already folded

Recorded at `P11-E-31` and in `ACCOUNTING_BOSS_FINAL_GATE_PACK.md` §1a. No further delta.

---

## 4. The one convergence this round actually produced

> ### `P11-C-09` — three peers independently require the same three things of a settlement event
>
> **An identity, a date, and a reversal link.** `P06` (`P07-R-01`/`R-03`), `P07` (`X-07`/`X-09`),
> `P08` (`XP-05`/`KRN-INV-01`) — reached separately, with separate evidence. `P06` states the
> instruction plainly: **P11 should carry it as one requirement, not three.**

**This is the first genuine cross-process convergence in the package** — three independent processes
converging on one object. It is **the same object as `D-5`**, approached from the settlement side
rather than the identity side, which **raises `D-5` from five dependent processes to eight** and is the
strongest available argument that `D-5` is the programme's single highest-leverage decision.

**It does not close `D-5`.** Convergent peer requirement is not evidence that the object is absent;
that remains class `C`, per `P11-E-31`.

---

## 5. Two peer vetoes now bind **P11's own method**, not P11's conclusions

| Veto | Binds |
|---|---|
| **`P06 AASP-VETO-04`** | *"VETO on P11 aggregating negatives across processes until each declares its addons-path population"* — P06 searched **791**; the full v18 distribution is **1752**. **P06 raises this against its own contribution to P11's registers** |
| **`P09 AAS+-VETO-04`** | No P09 mechanism claim may be relied on as describing a running system until version-matched |

**Both accepted without dispute, and both are honoured by construction in this file** — no negative is
aggregated across processes anywhere in `P11_S8_SUPERSESSION_RERUN_CORR1.md`, and every P09 item above
is labelled measurement or mechanism. **Registered `P11-B-24`** so the constraint survives into CORR2,
where the aggregate registers live.

`P06` additionally instructs that its two severity axes — **impact** (`B-50` leads) and **reachability**
(`B-10` leads) — **must not be collapsed**. P11 carries both.

---

## 6. Net effect on the package

| | Before `S8` re-run | **After** |
|---|---|---|
| Peers consumed | 10 of 10 | **10 of 10, now at their last artefact** |
| Peer artefacts consumed | 10 | **16** |
| Blockers | 20 registered · 18 open | **24 registered · 22 open** |
| Tolerance-zero | 13 | **14** (`T0-14`) |
| Boss decisions | 13 (floor) | **16 (floor)** |
| Cross-process convergences | 0 | **1** (`P11-C-09`) |
| Withdrawn P11 claims | 1 (`D-5` upgrade) | **2** (+ *"nets to zero"*) |

> **This re-run made the package larger, later and worse — and it is the most valuable hour of the
> round.** Every item above was reachable at the SHAs P11 had already consumed, by a one-line command
> P11 could have run first.

**`CP-P11C13` — COMPLETE.**
