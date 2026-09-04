# 08 — CANDIDATE RECONCILIATION REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. Three things, modelled separately

`BS-05` is `VERIFIED BUSINESS SEMANTIC` and is adopted whole.

| Nature | What it is | Candidate treatment | Status |
|---|---|---|---|
| **Matching record** | a stored pairwise fact: this debit item and this credit item, matched for this amount, in three currencies, as at this date | **immutable settlement fact `F4`** | `PROVISIONAL` |
| **Derived settlement state** | residual, reconciled flag, marker, payment state, ageing placement | **derived, reconstructible, never authoritative** | `PROVISIONAL` `FF-02` |
| **Emitted accounting event** | exchange difference, cash-basis tax | **a first-class event with actor `system` and a reason** | `PROVISIONAL` `CR-08` |

> *"The reference model conflates the first two by storing the derived values, and hides the third
> behind an operation users think of as clerical."* (`11 §1`)

> ### `RE-01` — **CORRECTED after `RA-21`.** The first draft prescribed destroying the fact class `D-18` declares undestroyable.
>
> **Rule `RE-01`.** `PROVISIONAL`. *Unreconciling is not an undo, and it is not a deletion.* It
> **asserts a withdrawal fact that supersedes the settlement fact**, and posts the consequent
> reversals. The settlement fact remains. A settlement and its withdrawal are **both** accounting
> events, and both are permanent.
>
> The draft had restated the parent's *description of reference behaviour* (*"it removes matching
> records"*) as a **candidate design rule**, and substituted "settlement facts" for "matching records"
> — the term this model reserves for the immutable `F4` class. Since `07 §5` removes un-posting,
> **unreconcile was left as the surviving destruction path**, defeating `D-18` structurally.

---

## 2. The two structural defects the design must close

> ### `D-17` — A settlement is hard-bounded by the residual it discharges. `PROVISIONAL`

`VF-12` / `COR-09` / `RC-01`: **nothing prevents over-reconciliation, in any currency configuration.**
The matching record is unconstrained against the item it matches. `11 §3` point 6 states it exactly:
the item stays available for further matching and *"nothing bounds the further matches against the
remaining residual."*

Candidate: the bound is enforced **at storage level**, in every currency carried, not in application
code — because `VF-02` shows application guards in this system are bypassable by construction.

> ### `D-18` — Settlement facts are never destroyed by an entry-level operation. `PROVISIONAL`

`VF-13` / `RC-02`: matches are **deleted silently** when an entry is reset to draft. Since `07 §5`
removes un-posting entirely, this closes structurally rather than by a new guard — the preferred
resolution, because it removes the path rather than defending it.

---

## 3. Matching semantics — carried forward

| Aspect | Candidate | Status | Basis |
|---|---|---|---|
| Granularity | pairwise, item to item — never entry to entry | `PROVISIONAL` | `ST-04`: settlement happens between specific obligations, not between totals |
| Amounts carried | **three** — company currency, and each side's transaction currency | `PROVISIONAL` | this is exactly what makes the difference computable |
| Partial match | residual reduced, item remains open, marker is a **relation not a flag** | `PROVISIONAL` | today the marker *"carries no lineage"* |
| Full match | aggregation record; owns the exchange event | `PROVISIONAL` | |
| Ageing placement | driven by latest matched date — **and this is disclosed**, since a partial settlement can move an old item into a younger bucket | `PROVISIONAL` | `11 §3` point 4 |
| Write-off | **`UNKNOWN`** — mechanism exists, policy semantics never established (`GAP-E01`) | `UNKNOWN` | decider: Boss |
| Matching history | **required** — no dedicated history artefact exists today (`GAP-E02`) | `PROVISIONAL` | |
| Account eligibility | receivable/payable forced reconcilable — keep | `PROVISIONAL` | |
| Unreconciled bank items block a fiscal-effective lock | **keep and generalise** | `PROVISIONAL` | `ST-07`, `BS-08` |

---

## 4. FX difference on settlement

| Rule | Statement | Status |
|---|---|---|
| `RE-02` | A difference arising because the two sides were measured differently is **realised** and is an accounting event | `PROVISIONAL` `BS-04` |
| `RE-03` | The emission is automatic; the **visibility is not optional** | `PROVISIONAL` |
| `RE-04` | A match whose measurement cannot be established **fails** — it does not settle at par | `PROVISIONAL` `D-09` |
| `RE-05` | Reversal of a settlement reverses its difference event; the reversal is matched to the original so no residue shows | `PROVISIONAL` |

`RE-04` is the reconciliation face of `VF-11`. The reference converts a missing rate at 1:1 **with no
error**, inside reconciliation (`COR-14`). `11` marks it `REJECT`; this design marks it a hard failure.

---

## 5. Cross-company settlement

> ### `D-31` — Cross-company settlement is refused by default. `EVIDENCE-DEPENDENT`

`BW-32`: **a receivable settled by cash that never entered its company.** `MCU-22`: cross-branch
reconciliation, exchange-difference posting **and a raw-SQL settlement write**, admitted because the
sole guard tests the **root** rather than the company — reachable by an ordinary accounting role in
the normal branch configuration.

**Blocked pending `GB-02`**, which has now **widened twice**. The design rule is stated; the boundary
it must defend is still moving.

---

## 6. Cash-basis tax interaction

`COR-17`: the emitted entries ignore the tax lock in **selection** but the write is then **refused**,
so the reconciliation **hard-fails**. `AE-13` adds that when the natural period is locked the entries
are dated **today** — invisibly, and *"can cross a year boundary."*

| Candidate | Status |
|---|---|
| A settlement that cannot emit its dependent tax event **fails before settling**, naming the tax period as the cause | `PROVISIONAL` — content routed to `WAVE-D TAX`; Wave A owns the failure semantics |
| No dependent event is silently re-dated to today | `PROVISIONAL` — `VF-19` |
