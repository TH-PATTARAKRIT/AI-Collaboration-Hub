# 04 — CANDIDATE FINANCIAL FACT MODEL

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. The seven-fact frame, carried forward

`BS-01` is adopted as the frame. It is `VERIFIED BUSINESS SEMANTIC`, multi-round, uncontradicted.

| Fact | Reference implements? | Candidate SMEsPlus position | Status |
|---|---|---|---|
| `F1` classification identity | yes | keep identity; **version the labels** (`D-21`) | `PROVISIONAL` |
| `F2` accounting event | **no — fused into the entry** | **separate it** (`D-01`) | `PROVISIONAL` |
| `F3` financial fact (the item) | yes, inside the entry | keep, bound to the event not the entry | `PROVISIONAL` |
| `F4` settlement fact | yes | keep; **bound it** (`D-17`); make it undestroyable (`D-18`) | `PROVISIONAL` |
| `F5` measurement fact | yes — the cleanest identity in Wave A | keep; **remove every fallback** (`D-09`); re-scope it (`D-10`) | mixed |
| `F6` finality declaration | **as a bare date, no object** | **make it an object** (`D-06`) | `PROVISIONAL` |
| `F7` provenance | **not at all** | **introduce it** (`D-04`) | `PROVISIONAL` |

> **The two absences — `F2` and `F7` — are the largest structural findings of the Wave, and they are
> the same absence twice: the ledger records *what was written down*, never *what happened and where
> it came from*.**

---

## 2. The immutable core of a financial fact

`CONTROL REQUIREMENT`. Derived from `VF-02` — today exactly **two** things are unconditionally
immutable, and neither is a financial fact.

| Element | In the immutable core? | Rationale | Status |
|---|---|---|---|
| Owning event identity | **yes** | the fact cannot outlive or migrate away from what recognised it | `PROVISIONAL` |
| Classification (account) | **yes** | the only dimension the reference protects at storage level (`COR-07`) | `PROVISIONAL` |
| Signed company-currency amount | **yes** | `ST-03` — one stored amount cannot disagree with itself; a stored debit/credit pair can | `PROVISIONAL` |
| Transaction currency | **yes** | `ST-02` — required always, even when equal to company currency; removes the "is this already converted?" class entirely | `PROVISIONAL` |
| Transaction-currency amount | **yes** | today the **magnitude is unprotected** — sign is DB-checked, magnitude is neither write-guarded nor hash-detected (`CONTRA-01b`) | `PROVISIONAL` |
| Measurement applied | **yes** | pins the rate to the fact — `13` records **no mechanism to pin a rate to a fact** exists | `PROVISIONAL` |
| Counterparty | **conditional** | relational, required only where a subledger is involved | `PROVISIONAL` |
| Analytic attribution | **decision required** | see §4 | `UNKNOWN` |
| Tax attribution | out of Wave A | `WAVE-D TAX`; today **outside hash coverage** (`COR-06`) | routed |
| Due date | **no — mutable metadata** | but today it is **not in the frozen-field list and outside hash coverage** at item level | `PROVISIONAL` |
| Narration, reference | **no — mutable metadata** | writable even when posted today | `PROVISIONAL` |

**Rule `FF-01`.** `PROVISIONAL`. *Debit and credit are presentation of a single signed amount,
never two stored values.* (`ST-03`)

**Rule `FF-02`.** `PROVISIONAL`. *Every derived value is reconstructible from the immutable core
alone, and no derived value is ever authoritative.* (`D-19`) The reference stores residual, reconciled
flag, matching marker, payment state, ageing placement and analytic lines as computed-and-stored —
**every one is a drift risk**, and whether any mechanism reconstructs them after drift is `GAP-E03`,
one of five **orphan unclassified ids**.

---

## 3. Temporal validity

`VF-03`: no temporal validity model was found anywhere **in the searched scope** (negative class `B`; boundary at `02 §6`). The consequence is stated exactly in `L5 §4`:

> *"What did this account mean on that date?" is unanswerable. A chart reorganisation, a type change,
> or a merge applies retroactively to all history.*

| Candidate rule | Statement | Status |
|---|---|---|
| `TV-01` | A financial fact is valid **as at** its event's recognition date, permanently | `PROVISIONAL` |
| `TV-02` | Classification **labels** carry effective dating; classification **identity** does not change | `PROVISIONAL` `D-21` — rests on `GAP-A03`, an **orphan id** |
| `TV-03` | A report over a past period resolves labels **as they stood in that period** | `PROVISIONAL` — follows `TV-02` |
| `TV-04` | No configuration change may retroactively alter the meaning of an asserted fact | `PROVISIONAL` — the design obligation created by `VF-03` |

---

## 4. Dimensional semantics — the open decision

`L5 §5` found three dimensions of three different kinds, and **only the first protected at storage
level**:

| Dimension | Kind | Today | Candidate |
|---|---|---|---|
| Classification | **structural** — the fact cannot exist without it | DB-enforced | keep, in the immutable core |
| Counterparty | **relational** | hash-covered at item level | conditional core member |
| Analytic | **derived from intent** — a distribution expanded into a subledger | **the subledger is destroyed by an ordinary correction** (`EV-012`) | see below |

> ### `D-28` — Per dimension, decide whether it is a **fact** (immutable, part of the event) or an **attribution** (restatable). `UNKNOWN`
>
> `INFERENCE` from `L5 §5`: *the reference model never makes that distinction explicit, which is why
> analytic attribution can be silently destroyed while the account cannot.* The decision is a business
> one — does management reporting restate, or is attribution part of what was recognised? **Decider:
> Boss.** Not a research gap.

---

## 5. Correction semantics

`ST-09` + `VF-13`. Three routes exist; the reference makes the destructive one the convenient one.

| Route | Effect | Destroys | Candidate | Status |
|---|---|---|---|---|
| Amend before assertion | changes a draft | nothing | **permitted** | `PROVISIONAL` |
| Retract, amend, re-assert | un-post / edit / re-post | **matching history and analytic lines, silently and unrecoverably** | **rejected as a general path** | `PROVISIONAL` |
| Counter-fact then corrected fact | reversal + re-entry | nothing | **the only correction path** | `PROVISIONAL` |

**Rule `FF-03`.** *Once an accounting event exists, it is corrected only by further accounting events —
and the correction relation is recorded, constrained, bidirectional, **and validated against the
content it claims to correct**.*

> ### The last clause was added after `RA-14`, and it is the load-bearing one.
>
> The first draft constrained only the **link** — unique, non-severable, declared delete behaviour.
> `BW-35`'s **first** finding is not about the link: *"**nothing checks that the entry a reversal
> points at is the entry it actually reverses — not the amounts, not the signs, not the accounts, not
> the period.**"* The wizard's only pre-check on the target is that the **journal type** matches.
>
> **A reversal pointing at the wrong original, carried on a perfect bidirectional link, still balances
> and is still wrong lineage.** The design claimed to *prevent* `T-15` while leaving the primary defect
> open.
>
> **Rule `FF-03a`.** `PROVISIONAL`. *A correction relation is admitted only where the corrector's
> amounts, signs, classifications and period stand in the declared relation to the corrected fact.*

---

## 6. Provenance — `F7`

`PROVISIONAL` `D-04`. The reference implements none of this; `15 §4` records **five of seven
lineages unrecorded**.

| Lineage | Reference | Candidate |
|---|---|---|
| reversal → original | **recorded** | keep, **and constrain it** (`BW-35`) |
| exchange entry → causing match | **recorded** | keep |
| cash-basis entry → origin document | **recorded**, survives unmatching | keep |
| corrected → corrector | **absent** | **required** (`FF-03`) |
| fact → source document | **no general carrier** | **required** (`D-01` source reference) |
| classification → predecessor | **absent — the predecessor is deleted** | **required** (`D-20` succession) |
| migrated balance → origin | **absent** | **required** (`D-29`) |

**Rule `FF-04`.** `PROVISIONAL`. *Provenance is part of the fact, not metadata attached to it.*
Source system, source event identity, extraction lineage and idempotency key travel with the event
permanently — and **tamper-evidence keys on business identity, not storage identity**, or it cannot
survive the migration it is most needed for (`VF-17`, `COR-12`).
