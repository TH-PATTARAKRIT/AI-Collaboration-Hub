# 14 — BALANCED-BUT-WRONG DESIGN CHALLENGE

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> A `BALANCED BUT WRONG` case is one where **every equation the ledger can check is satisfied and the
> accounting fact is nonetheless untrue.** A design that merely preserves `Debit = Credit` is
> insufficient — this file exists to prove the candidate design does more than that.

---

## 0. Two blocking caveats on this file

### `MCD-01` — the taxonomy carries an id collision and must be renumbered before use as design input

The parent recorded it plainly: **`BW-16` is a branch-scoped rate; `NBW-16` is a period sourced from
another company.** Any downstream reference to "case 16" is ambiguous, and the parent stated
*"renumbering is required before this register is used as design input."*

**This file is exactly that downstream use.** The collision is therefore carried, not silently
corrected, and every reference below uses the full id. **`MCD-01` is an open defect of the input to
this file.**

### `BW-16` is withdrawn

`MCU-13` withdrew `BW-16` — the branch-scoped rate case is **not reproducible** on this build (see
`D-10a`). Its residual content is absorbed by `BW-01` and `BW-29`. Any design defended by reference to
`BW-16` is defended against nothing.

---

## 1. Coverage position

| Metric | Value |
|---|---|
| Classes in the taxonomy | **19** (15 supplied + 3 added by necessity + 1 split) |
| Classes searched | **19 of 19 (100%)** |
| Known instance floor | **claimed 35/36 — ESTABLISHED 32.** `G-C8`: the establishment test was applied to only 3 of 7 new cases, yet all were counted. 4 are re-classified `NOT YET ESTABLISHED` |
| Classes that stood empty and were then searched | **2** — `T-14` wrong opening provenance, `T-15` wrong reversal lineage |
| Result of searching them | **both produced a verified defect on first search** (`BW-34`-adjacent, `BW-35`) |

> **`ER-CORE-4` — an empty taxonomy cell means UNSEARCHED, never ABSENT — now has a 2-of-2 record.**
> This is the strongest single methodological result in the parent programme and it is why no class
> below is marked "no exposure".

---

## 2. Design challenge, class by class

For each class: the instances, the candidate design response, and whether the response **prevents**,
**detects**, or merely **controls**.

| Class | Instances | Candidate response | Rule | Effect | Status |
|---|---|---|---|---|---|
| `T-01` **Wrong FX** | `BW-01` par · `BW-14` null-company rate re-measures another tenant · `BW-17` another company's global rate · `BW-29` undated earliest-ever · `BW-30` opening at a 2010 rate · `BW-31` v19 today-rate aggregation | Remove every fallback; refuse on missing measurement; pin the rate to the fact; scope measurement to tenant+company | `FXD-02` `FXD-03` `FXD-04` `D-10` | **prevents** `BW-01`/`BW-29`/`BW-30`; **`BW-14`/`BW-17`/`BW-31` NOT ADDRESSED — blocked on `GB-03`/`GB-01`/`MCU-20`** | `EVIDENCE-DEPENDENT` |
| `T-02` **Wrong date** | `BW-02` derived accounting date | Date is asserted, never derived; refusal replaces re-dating | `DP-01` `DP-02` | **prevents** | `PROVISIONAL` |
| `T-03` **Wrong period** | `BW-03` generated consequence relocated · `NBW-16` period sourced from another company | Period is an object; attribution fixed at recognition; re-attribution is an explicit event | `D-06` `DP-05` `DP-06` | **prevents** `BW-03`; **`NBW-16` blocked on `GB-01`** | mixed |
| `T-04` **Wrong tenant** | `BW-12` cross-tenant control state · `BW-14` · `NBW-22` report definition owned by another tenant | Tenant dimension on every control config; tenant identity above company | `CR-01` `D-12` `D-33` | **prevents `BW-12`**; `BW-14`/`NBW-22` **blocked** on `GB-01` and `MCU-04`/`MCU-11` | `EVIDENCE-DEPENDENT` |
| `T-05` **Wrong company** | `BW-17` · `NBW-16` · `NBW-18` cross-company settlement inside one root · `NBW-21` · `NBW-23` · `NBW-25` · `BW-32` · `MCU-22` | Cross-company settlement refused by default; no posted fact rewritten across a company boundary | `D-31` `CB-05` | **NOT PROVEN — `GB-02` has widened twice.** Design stated; boundary still moving | `EVIDENCE-DEPENDENT` |
| `T-06` **Wrong account** | `BW-04` retroactive merge retargets posted history | Classification never deleted; replacement is succession; every retargeting is an event with a record | `CA-02` `CA-03` `CA-05` | **prevents** | `PROVISIONAL` |
| `T-07` **Wrong partner** | `NBW-17` retroactive counterparty rewrite, lock bypassed | Counterparty in the immutable core; no suppression path on a posted fact | `04 §2` `07 §5` | **prevents**, *conditional on* `MCU-01` | `EVIDENCE-DEPENDENT` |
| `T-08` **Wrong source linkage** | `BW-08` no general provenance carrier | Provenance is part of the fact; source reference on the event | `FF-04` `D-04` | **prevents** | `PROVISIONAL` |
| `T-09` **Duplicate event** | `BW-06` machine-generated · `BW-13` manual, detector never runs · `BW-15` two ingestion routes with **disjoint keys** · `NBW-23` inter-company document under elevated privilege | Idempotency key on the accounting event, unique within tenant, refusal on collision | `D-24` | **prevents `BW-06`/`BW-13`**; **`BW-15` only if the key is single and canonical** — two routes with disjoint keys is precisely the failure a per-route key reproduces; `NBW-23` blocked on `GB-02` | `PROVISIONAL` |
| `T-10` **Omitted event** | — | Producing domains declare expected counts; close preconditions test them | `03 §5` | **detects only** | `PROVISIONAL` |
| `T-11` **Wrong analytic** | analytic subledger destroyed by ordinary correction | Un-post removed; analytic classed as fact or attribution | `07 §5` `D-28` | **prevents the destruction**; **the classification is `UNKNOWN`, decider Boss** | `UNKNOWN` |
| `T-12` **Wrong tax** | routed | `WAVE-D TAX` owns content; Wave A carries the tax point | `09 §1` | **not addressed in Wave A** | routed |
| `T-13` **Wrong reconciliation state** | over-reconciliation; silent match destruction | Hard bound at storage level; settlement facts undestroyable; derived state reconstructible | `D-17` `D-18` `FF-02` | **prevents** | `PROVISIONAL` |
| `T-14` **Wrong opening provenance** | found on first search of an empty class | Opening carries provenance to origin; opening measurement refuses fallback | `D-29` `FXD-03` | **prevents** | `PROVISIONAL` |
| `T-15` **Wrong reversal lineage** | `BW-35` — pointer **not unique, severable, no delete behaviour, server-written**; auto-match only in the cancel case | Correction relation constrained, unique, non-severable, bidirectional | `FF-03` `EL-02` | **prevents** | `PROVISIONAL` |
| `T-16` **Wrong classification** | `BW-33` control-account attribute silently flipped by import | Control status governed, not importable | `D-32` | **blocked on `T0-09`** — control present in the view layer, absent at write; `T0-09` **not bounded** | `EVIDENCE-DEPENDENT` |
| `T-17` **Wrong measurement rule** | *the fact records the result, never the rule* | Recognition rule versioned and identifiable from the fact | `L-3` | **PARTIAL — design stated, not evidenced.** The weakest response in this file | `PROVISIONAL` |
| `T-18` **Wrong integrity domain** | hash keyed on storage identity; index scoped by journal; number-blanking wizard | Tamper-evidence on business identity; identity tenant-scoped; ledger-wide securing | `D-14` `JR-05` `L-5` | **blocked on `T0-08`** | `EVIDENCE-DEPENDENT` |
| `T-19` **Wrong report definition** | `MCU-04` no company dimension · `MCU-11` caller-supplied scope, no defence in depth · `NBW-22` | Report definitions tenant-owned, company-scoped, defence in depth | `L-9` | **blocked — `MCU-04`+`MCU-11` merged and `REMAINS GATING`** | `EVIDENCE-DEPENDENT` |

---

## 3. Honest score

| Response quality | Classes | Ids |
|---|---|---|
| **Prevents, and not blocked** | **6** | `T-02` `T-06` `T-13` `T-14` `T-15` — and `T-08` **only conditionally**: it rests on the class-`B` provenance negative the register lists as blocked (`RB-23`) |
| **Partially answered** | **2** | `T-03` (prevents `BW-03`; `NBW-16` blocked on `GB-01`) · `T-15` (link constrained **and** content-validated only after `FF-03a`, `RA-14`) |
| **Prevents, conditional on an open item** | 2 | `T-07` `T-09` — and `T-09` only for machine-originated events: `RA-03` shows a deterministic key over a source fact **does not exist for a manual entry**, which is `BW-13` |
| **Detects only** | 1 | `T-10` — **and §4 re-grades `BW-33` into this class, making it load-bearing** |
| **Blocked behind an unresolved boundary or gating unknown** | **6** | `T-01` `T-04` `T-05` `T-16` `T-18` `T-19` |
| **Design stated but unevidenced** | 1 | `T-17` |
| **Open decision** | 1 | `T-11` |
| **Routed out of Wave A** | 1 | `T-12` |

> ### The result, stated plainly
>
> **The candidate design fully answers 6 of 20 known classes — and §4 establishes the taxonomy itself is incomplete. Six are blocked behind items the parent has
> not closed, and every one of those six is a cross-boundary class — tenant, company, integrity
> domain, or report definition.**
>
> That is not a coincidence and it is the most useful thing this file says: **the classes the design
> cannot yet defend are exactly the classes `GB-01`, `GB-02`, `GB-03`, `GB-04`, `T0-08` and `T0-09`
> govern.** The redesign is not blocked in many places for many reasons; it is blocked in one place —
> **the boundary model** — for one reason: the exposure is 9 of 192 assessed, over a path set known to
> be short by 962 modules.

---

## 4. `T-20` — the class this taxonomy has no cell for

> ### `UNBALANCED AND POSTED IS REACHABLE.`

`VERIFIED FACT`, from the parent's own fresh challenge (`MCC_G §7`). Two tolerance-zero boundaries
were returned that **no numbered `T0-` id covers**, because they are **recorded only in `MCC_J`, which
does not exist**:

| # | Boundary |
|---|---|
| 1 | The entry-balance invariant is enforced in **one currency dimension only** |
| 2 | The balance assertion itself is **suppressible by context on three shipped production paths** |

The parent stated the consequence and this file adopts it verbatim as a design obligation:

> **`unbalanced-and-posted` is reachable. That is a worse state than balanced-but-wrong, and this
> taxonomy has no cell for it.**

### Why this changes the frame, not just the score

Every one of the 19 classes assumes the ledger's own equations hold and asks what is *nonetheless*
untrue. `T-20` is the case where **the equation itself does not hold and the fact posts anyway**. A
design tested only against `T-01`…`T-19` would never be asked to defend it.

| Candidate response | Rule | Status |
|---|---|---|
| `Σ signed amounts = 0` is enforced **unconditionally**, at storage level, with **no context able to suppress it** | `JE-02` + `ADR-02` `B1` | `PROVISIONAL` |
| The invariant is enforced in **every currency dimension carried**, not one | `JE-03`, `JE-04` extended | `PROVISIONAL` |
| No production path may assert a fact through a route that bypasses the invariant | `EL-06` | `EVIDENCE-DEPENDENT` — 62 raw-SQL sites, **0 assessed** |

**`ADR-02`'s recommendation of storage-level enforcement was argued on testability before this class
was known. `T-20` is the case that makes it decisive**: an application-level invariant with three
shipped suppression contexts is not an invariant, and `VF-02` predicted exactly this shape.

### Register correction

| Item | As carried in §1–§3 | Corrected |
|---|---|---|
| Taxonomy classes | 19 searched | **19 searched, and the taxonomy is now known to be incomplete** |
| Established floor | claimed 35/36 | **32** (`G-C8`) |
| Tolerance-zero boundaries | 10 | **10 registered · 12 known**; 2 exist by reference only |
| `BW-28` | *"no detecting control"* | **WITHDRAWN** (`G-C2` — a class-`A` absence asserted where a class-`B` search finds a user-overridable revaluation control). Replaced by **`BW-28a`** |
| `BW-28a` | — | **`VERIFIED DEFECT`, more severe than what it replaces.** Where the consolidating root holds no rate row for a subsidiary's functional currency, that subsidiary's **entire balance sheet and income statement** translate at **1.0**, silently, with no warning and no reconciling item — **a whole-entity consolidation failure**, now `T0-07`'s headline instance |
| `BW-33` | *"minor severity"* | **UNDERSTATED → re-graded MEDIUM** (`G-C4`). The same lines that flip the reconcile attribute then reconcile with **exchange-difference and cash-basis generation both switched off** — so realised FX is **not recognised** and cash-basis tax entries are **not generated**, automatically, with only an informational log. Cross-listed under `T-10` **omitted event** |

**`BW-28a` strengthens `D-09` further**: the fallback's worst realisation is not a wrong line on one
posting — it is an entire subsidiary consolidated at par with nothing on the face of the statements to
show it.

**`BW-33`'s re-grading moves it out of `T-16` alone.** It is now also a `T-10` omitted-event case, and
`T-10` was the one class this design could only **detect**, never prevent. That gap is now
load-bearing and is recorded as such.
