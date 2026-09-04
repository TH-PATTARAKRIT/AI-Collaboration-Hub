# 10 — CANDIDATE FX REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`
**Every FX conclusion in this file is additionally blocked by `D-30` / `MCU-20` — see §6.**

---

## 1. The chain, adopted

`13 §1` establishes all five links exist. This is **the cleanest chain in Wave A** and is adopted.

`Transaction fact → Currency fact → Valuation fact → Settlement fact → Reporting fact`

**Rule `FXD-01`.** `PROVISIONAL`. *Measurement is stored once per date; valuation bases are
derived per reporting purpose.* Closing, historical, average and current are **selection rules over
one dated series**, not four stored measurements (`BS-06`, `COR-10`, `ST-05`).

This is the one place the reference model's design is better than it first appeared, and the parent
found it **only after the challenge unit corrected the round's own claim**. It is retained with that
lineage attached.

---

## 2. The fallback is removed entirely

> ### `D-09` — A missing measurement halts the posting. There is no fallback of any kind. `PROVISIONAL`

The evidence strengthened at every round:

| Round | Finding |
|---|---|
| Core | *"Missing rate: silently converts at par, producing a valid-looking entry"* (`CONTRA-08`) |
| `CORR1` | Resolution is: latest rate on or before the date; **else the earliest rate ever**; else **1.0** (`COR-14`) |
| MCC | `T0-07` characterised **worse than registered** — 8 raw-SQL reads, three modules, **four distinct fallback semantics** |
| MCC | `BW-29` the **undated earliest-rate-ever** fallback — *"more dangerous than par"* |
| MCC | `BW-30` **opening and onboarding valued at a 2010 rate** |
| MCC | `BW-31` v19 aggregates monetary columns **at today's rate, outside every record rule** |

**Why "more dangerous than par" is right.** Par is obviously wrong and shows up as an implausible
number. An undated historical rate produces a *plausible* number — it survives review. `BW-30` is that
class realised: a migration opening balance measured at a rate from 2010.

| Rule | Statement | Status |
|---|---|---|
| `FXD-02` | No implicit rate. No par. No nearest. No earliest. No latest-ever | `PROVISIONAL` |
| `FXD-03` | A missing measurement is a **refusal with a named cause**, at posting and at settlement | `PROVISIONAL` |
| `FXD-04` | Every conversion records **which measurement it used** — the rate is pinned to the fact | `PROVISIONAL` — `13` records **no mechanism to pin a rate to a fact** exists today |
| `FXD-05` | No reporting path converts at a date other than the fact's own, unless the basis is explicitly a reporting basis and is labelled as such | `EVIDENCE-DEPENDENT` — `BW-31`/`MCU-20` |

---

## 3. Measurement scope

> ### `D-10` — Measurement is scoped to tenant + company, never to a group root, and never nullable. `EVIDENCE-DEPENDENT`

`EV-018`: rates are held per company **group root** (`VF-15`). `GB-03` bounded the surface for the
first time — **20 of 20 files (100%)** — and the site/expression figure is a **denominator defect, not a statistic**: `MCC_B` `B-3` records two disciplined enumerations of the same surface returning **12** and **14** because **the unit was never defined**. *"A bounded population with an undefined unit is not yet a denominator."* Only the file count survives as coverage — and split it in two:

| Axis | Position |
|---|---|
| **Branch-scoped rate row** | research-complete with one residual. The `FX-08` composite defect is **`NOT REPRODUCIBLE`** — see `D-10a` |
| **Company-less (null) rate row** | **an unclosed verified defect.** Admitted by an explicit disjunct in the record rule, **creatable by a routine accounting role**, resolved by **6** paths and refused by **6** others — and **widened again on the version SMEsPlus is targeting** |

**Blocked pending `GB-03`'s open half and `GB-01`.**

### `D-10a` — `INVALIDATED`, retained for lineage

The `FX-08` framing — *"the writer stores a branch company, the resolver looks for root-or-null, the
two do not intersect"* — was carried as a `VERIFIED DEFECT` through **two gate reports** and is
**wrong**. `MCU-13` contradicted the writer half at three independent layers, the composite defect is
not constructible, and `BW-16` was withdrawn.

> **A design synthesised before `MCU-13` would have re-architected rate scoping around a state that
> cannot exist.** This is the package's concrete proof that delta revalidation is mandatory.

---

## 4. Realised versus unrealised

`BS-04` adopted: **realisation is caused by an event; revaluation is caused by a date.**

| | Realised | Unrealised |
|---|---|---|
| Trigger | settlement | passage of a reporting date with the obligation open |
| Nature | an accounting event — a posted fact | a valuation restatement |
| Reference | emitted automatically by matching | **A post-and-reverse revaluation mechanism EXISTS** in the reporting module — `NC-19`, class **`E — CONTRADICTED`**. `GAP-H01`'s negative held only for the core accounting module |
| Candidate | `ADAPT` — keep the emission, make the visibility non-optional | **`ADAPT` + `EXTEND`, not invent** — `D-23` is `INVALIDATED` in its original form; the mechanism exists and must be assessed before anything is designed |

> `P-13 §3` notes the reference *avoids the classic error of conflating them — by not implementing the
> second at all.* **That framing is now contradicted** (`NC-19`). The candidate must still implement
> revaluation without importing the conflation — reversed or restated at the next period boundary,
> never a settlement fact — but it does so by **assessing an existing mechanism, not by inventing one**.

> ### `D-23` — `INVALIDATED`. `NC-19` contradicts it.
>
> This design said *"SMEsPlus must design revaluation."* **A post-and-reverse unrealised-FX
> revaluation mechanism exists in the reporting module**, verified by the parent's research team.
> `GAP-H01` was class `B`, bounded to the core accounting module, and this package restated it as a
> design obligation **without reading `NC-19`** — the register that recorded the contradiction.
>
> **Successor `D-23a`** — assess the existing mechanism, then decide `ADAPT` / `EXTEND` / `REJECT`.
> `PROVISIONAL`.
>
> **And it compounds.** `G-C2` records that this same revaluation report computes the retranslation
> difference per line and per account and is **user-overridable per currency with a warning** — making
> it a *detecting control* for par-valued balances, which `BW-28` had asserted did not exist. **Two
> separate absence claims in this package rested on not having read one file.**

---

## 5. Correction of a measurement

`GAP-H02`: one rate per day is replaceable, and *"effect on already-posted entries not traced."*

| Rule | Statement | Status |
|---|---|---|
| `FXD-06` | A measurement correction is **itself dated** and never silently retroactive (`BS-01` `F5`) | `PROVISIONAL` |
| `FX-07` | Facts measured under a superseded rate are **enumerable** — the ledger can answer "what did this correction touch?" | `PROVISIONAL` — closes `GAP-H02` |
| `FXD-07` | A migrated or restored rate row is **revalidated against its company at import** | `EVIDENCE-DEPENDENT` `D-35` / `MCU-19` — *"one `SELECT` answers it"*, and it is unrun |

---

## 6. The version-stability blocker — governs this whole file

> ### `D-30` — No FX conclusion carries into v19 until `MCU-20` closes. `EVIDENCE-DEPENDENT`

`GB-08` / `MCU-20`: the v19 ORM **core** adds an **eleventh** read-side rate resolver, in raw SQL,
**outside every record rule**, converting at **today** rather than at the record's date, with a
**fourth** fallback semantic, reachable from **any grouped monetary aggregation in any list or pivot
view**. Zero occurrences in either v18 core.

**SMEsPlus targets the v19 line.** So:

> **A v18 → v19 migration *widens* the rate-scoping control surface rather than converging it.**

This is the **second independent confirmation of reference-version instability in this programme, in a
second domain** — the first was the COGS Perpetual pattern. It is a programme-level property, not an
FX quirk, and it is the strongest single argument in the evidence for **not** deriving SMEsPlus
measurement semantics from reference behaviour at all.
