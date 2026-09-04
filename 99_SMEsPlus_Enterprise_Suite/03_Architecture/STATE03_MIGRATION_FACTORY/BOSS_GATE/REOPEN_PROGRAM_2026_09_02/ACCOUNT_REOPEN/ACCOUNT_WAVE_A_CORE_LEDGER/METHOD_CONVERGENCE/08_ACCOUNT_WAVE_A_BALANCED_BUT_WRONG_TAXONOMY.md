# 08 — ACCOUNT WAVE A — `BALANCED BUT WRONG` TAXONOMY

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room

**Method, per the round instruction: define the taxonomy first, then enumerate against it.**
The parent register grew 15 → 17 → 27 by accretion — each round appended the cases it happened to
find. A register built that way can never say what is missing, because it has no shape to be missing
from.

---

## 0. Lineage hazard, recorded first

The 27 cases carry **two independent numbering series** that collide:

- `BW-01` … `BW-17` — the `C12`/`G08` series;
- `NBW-16` … `NBW-25` — the `GR2` series.

`BW-16`/`BW-17` and `NBW-16`/`NBW-17` are **four different cases sharing two numbers**.
`BW-16` is a branch-scoped rate; `NBW-16` is a period sourced from another company. Any downstream
reference to "case 16" is ambiguous. **Renumbering is required before this register is used as
design input.** Recorded as `MCD-01` and not silently corrected here.

---

## 1. The taxonomy

A `BALANCED BUT WRONG` case is one where **every equation the ledger can check is satisfied and the
accounting fact is nonetheless untrue.** The classification axis is *what is wrong*, not *how it
happened*.

The round instruction supplies fifteen classes. Enumeration against them showed four Wave A cases
that no class could hold, so the taxonomy is **extended by three** and one class is **split**.
Extensions are marked `+`.

| # | Class | Definition |
|---|---|---|
| `T-01` | Wrong FX | The measurement is made at a rate that is not the correct rate for this fact |
| `T-02` | Wrong date | The fact carries a date other than the one the business event bears |
| `T-03` | Wrong period | The fact lands in a period other than the one it belongs to |
| `T-04` | Wrong tenant | A fact is measured, controlled or reported using another tenant's data |
| `T-05` | Wrong company | As `T-04`, across a company boundary within a tenant |
| `T-06` | Wrong account | The fact names an account other than the one it was posted to |
| `T-07` | Wrong partner | The fact names a counterparty other than the true one |
| `T-08` | Wrong source linkage | The fact cannot be tied back to the event that caused it, or ties to the wrong one |
| `T-09` | Duplicate event | One business event produces more than one accounting fact |
| `T-10` | Omitted event | A business event that should produce an accounting fact produces none |
| `T-11` | Wrong analytic dimension | The fact carries an incorrect management-accounting dimension |
| `T-12` | Wrong tax classification | The fact carries an incorrect tax treatment |
| `T-13` | Wrong reconciliation state | Settlement state misrepresents what is actually settled |
| `T-14` | Wrong opening provenance | An opening balance misstates what it was carried forward from |
| `T-15` | Wrong reversal lineage | A reversal misstates what it reverses, or is not tied to it |
| `T-16` `+` | **Wrong classification** | The fact's *character* — its type or category — is changed after the fact, altering meaning without altering amount. Split out of `T-06`: an account can be right while its classification is wrong |
| `T-17` `+` | **Wrong measurement rule** | The amount is computed correctly *from a shared, unversioned rule object that was silently changed or is owned outside the fact's boundary*. The fact records the result, never the rule |
| `T-18` `+` | **Wrong integrity domain** | Tamper-evidence or identity machinery is correct in itself but scoped to the wrong domain, so it attests something other than what it appears to attest |
| `T-19` `+` | **Wrong report definition** | The ledger is entirely correct; the definition that reads it is wrong or is owned outside the boundary. Nothing in the ledger is wrong and the reported figure still is |

## 2. Enumeration of the 27 known cases against the taxonomy

| Class | Instances | Count |
|---|---|---|
| `T-01` Wrong FX | `BW-01` par valuation · `BW-14` null-company rate re-measures another tenant · `BW-16` branch-scoped rate invisible to resolver · `BW-17` another company's global rate | **4** |
| `T-02` Wrong date | `BW-02` derived accounting date | **1** |
| `T-03` Wrong period | `BW-03` generated consequence relocated · `NBW-16` period sourced from another company | **2** |
| `T-04` Wrong tenant | `BW-12` cross-tenant control state · `BW-14` · `NBW-22` report definition owned by another tenant | **3** |
| `T-05` Wrong company | `BW-17` · `NBW-16` · `NBW-18` cross-company settlement inside one root · `NBW-21` · `NBW-23` · `NBW-25` | **6** |
| `T-06` Wrong account | `BW-04` retroactive merge retargets posted history | **1** |
| `T-07` Wrong partner | `NBW-17` retroactive counterparty rewrite, lock bypassed | **1** |
| `T-08` Wrong source linkage | `BW-08` no general provenance carrier | **1** |
| `T-09` Duplicate event | `BW-06` machine-generated · `BW-13` manual entry, detector never runs · `BW-15` two ingestion routes, disjoint keys · `NBW-23` inter-company document under superuser | **4** |
| `T-10` Omitted event | `NBW-24` FX-difference recognition suppressed database-wide | **1** |
| **`T-11` Wrong analytic dimension** | — | **0** |
| **`T-12` Wrong tax classification** | — | **0** |
| `T-13` Wrong reconciliation state | `BW-07` over-settlement · `NBW-18` · `NBW-19` settlement created with no guard · `NBW-20` state written by raw SQL | **4** |
| **`T-14` Wrong opening provenance** | — | **0** |
| **`T-15` Wrong reversal lineage** | — | **0** |
| `T-16` `+` Wrong classification | `BW-05` retroactive account-type change | **1** |
| `T-17` `+` Wrong measurement rule | `NBW-21` shared rounding/payment-term object, no company field, no version · `NBW-24` | **2** |
| `T-18` `+` Wrong integrity domain | `BW-09` silent tamper on a secured entry · `BW-10` hash collision on rounding precision · `NBW-25` hash chain spanning companies | **3** |
| `T-19` `+` Wrong report definition | `NBW-22` | **1** |

Cases appear under every class they belong to; the column is not a partition. **All 27 cases map.**

`BW-11` — *unbalanced entry stored, externally reachable* — is **excluded from this taxonomy** and
recorded separately. It is not "balanced but wrong": it is **not balanced**. It is the only case in
the register detectable by a proof over stored data, which is precisely because it violates the
equation set rather than satisfying it. Filing it here has flattered the register's detectability
profile by one.

## 3. Answers to the three questions asked

### (a) Which classes have at least one instance — **15 of 19**

`T-01` … `T-10`, `T-13`, `T-16` … `T-19`.

### (b) Which classes have zero instances — **4**, and they are not equivalent

| Class | Zero because | Disposition |
|---|---|---|
| `T-11` Wrong analytic dimension | Management accounting is **Wave E** | **Legitimately empty for Wave A.** Routed |
| `T-12` Wrong tax classification | Tax is **Wave D** | **Legitimately empty for Wave A.** Routed |
| **`T-14` Wrong opening provenance** | **Not searched** | **UNENUMERATED SPACE INSIDE WAVE A** |
| **`T-15` Wrong reversal lineage** | **Not searched** | **UNENUMERATED SPACE INSIDE WAVE A** |

`T-14` and `T-15` are the material result of this file. Both are squarely Wave A — opening balances
are scope `G` (`G-07`), reversal is scope `B`/`C` (`B-10`, `C-04`) — and both sit on ground the
package has already found weak:

- **`T-14`.** The parent established that the opening-balance mechanism exists but that **provenance
  does not survive it**, and that an account merge **deletes records and retargets posted history**
  (`BW-04`). An opening balance carried forward across a merge would misstate what it was carried
  from, and no case in the register tests this.
- **`T-15`.** The parent established that a reversal is **a new dated entry, optionally auto-matched**
  to its origin, and that no general source-event identity exists (`BW-08`). A reversal whose link to
  its origin is absent, wrong, or severed by a later master-data rewrite (`NBW-17` rewrites posted
  items across every company) would misstate lineage, and no case in the register tests this.

Both are recorded as **`GATING` unknowns** in file `06` — `MCU-14` and `MCU-15`. They are not new
findings; they are **named empty cells**, which is the whole point of building the taxonomy first.

### (c) Is the taxonomy itself complete for Wave A — **No, as supplied; extended here to 19**

Four of the 27 known cases could not be held by any of the fifteen supplied classes. The four
extensions each name a distinct failure mode that Wave A demonstrably contains:

| Extension | Why the supplied fifteen could not hold it |
|---|---|
| `T-16` Wrong classification | `T-06` is about *which account*; `BW-05` changes the account's *type* while the account is unchanged |
| `T-17` Wrong measurement rule | Every supplied class describes a wrong **value on the fact**. `NBW-21` has a correct value derived from a shared rule object that is unversioned, company-blind, and not recorded on the fact |
| `T-18` Wrong integrity domain | No supplied class is about the **control machinery** being scoped wrongly rather than the fact being wrong |
| `T-19` Wrong report definition | Every supplied class assumes the wrongness is **in the ledger**. `NBW-22` is a wrong figure with a wholly correct ledger |

`T-17`, `T-18` and `T-19` share one structure worth stating plainly:

> **The fact is correct and the thing that gives it meaning is not.** A rule object, a hash domain, a
> report definition — none is a journal entry, none is checked by any of the seven equations, and all
> three are company-blind or boundary-crossing in the reference system.

The equation set can never detect this family. That is a design input for SMEsPlus, not merely an
audit observation.

## 4. Is 27 still a floor?

**Yes, and the taxonomy now says where.**

| Source of further instances | Bounded? | Size |
|---|---|---|
| `T-14`, `T-15` — never searched | yes, by scope | unknown, ≥0 |
| `P-21b` privilege-elevation sites unassessed | yes | **90 of 93** |
| `P-21c` root-vs-company sites unassessed | yes | **33 of 37** |
| `P-21d` raw-SQL sites unassessed | yes | **60 of 62** — `NBW-20` is one of the 2 assessed |
| `P-23` failure paths unassessed | yes | **~128 of 153** |
| `T-17` shared rule objects — only 2 found, population never enumerated | **no** | `UNBOUNDED / NOT YET ENUMERABLE` |

The difference from the parent position is not the number. It is that "floor" now has a **named,
mostly-bounded remainder** instead of being an honest shrug. Ten cases were found in one independent
round against 4 assessed sites in these populations; 211 remain.

## 5. Effect on the gate

The taxonomy does not change any finding, severity, or blocker. It changes what can be *said*:

- `27` is a floor over a **19-class** taxonomy, of which **2 classes inside Wave A have never been
  searched** and **4 populations totalling 211 sites are bounded but untraversed**.
- The most severe cases cluster in `T-05` (6), `T-01` (4), `T-09` (4) and `T-13` (4) — company
  boundary, measurement, duplication, settlement. That is the same cluster as `GB-01` … `GB-03`, and
  it is consistent with the tolerance-zero position in file `09`.
