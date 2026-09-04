# 09 — CANDIDATE DATE / PERIOD REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. Eight date concepts, explicitly separated

`VF-05`: three of seven Boss-named concepts **have no carrier**. `C07` also found an eighth date the
Boss list did not name.

| # | Concept | Reference carrier | Candidate owner | Status |
|---|---|---|---|---|
| 1 | **Source document date** | exists, user-owned | the source document | `PROVISIONAL` |
| 2 | **Accounting date** | exists — **system-derived** (`VF-04`) | the **event**, user-owned, never system-moved | `PROVISIONAL` `D-05` |
| 3 | **Recognition date** | **none — collapsed into the accounting date** | the event, explicit | `PROVISIONAL` |
| 4 | **Tax date / tax point** | **none** | `WAVE-D TAX` owns content; **Wave A must carry the field** | `EVIDENCE-DEPENDENT` |
| 5 | **Statutory filing date** | none in the ledger — belongs to the return | the return | `PROVISIONAL` |
| 6 | **Due date** | exists | the item | `PROVISIONAL` |
| 7 | **Posting timestamp** | **none** — only generic record-audit fields; *there is no accounting fact recording when a posting occurred* | the event, as an accounting fact | `PROVISIONAL` |
| 8 | **Delivery / supply date** | exists; **not found to drive any ledger, tax or reporting behaviour** (class `B`, boundary stated) | carried, and **wired to the tax point** where a regime makes supply the tax point | `PROVISIONAL` |

> ### The load-bearing result, carried verbatim from `C07`
>
> **Three of the seven concepts have no carrier, and the missing one with the greatest consequence is
> the tax date.** Because there is no tax point, the tax lock, the tax return population and the
> statutory extracts all fall back on the accounting date — **the one date in the system that the user
> does not control and that the system silently moves.**

For a Thai-statutory deployment this is the sharpest point in Wave A: VAT tax-point rules are not the
same as posting-date rules, and the ledger has no field to hold the difference. Content is
`WAVE-D TAX`; **the carrier is a Wave A obligation** and is registered as such.

---

## 2. The derivation rule is removed

`VF-04`, `VF-06`, `VF-07`. The reference derives the accounting date from the document date, the
violated locks, **and the journal's numbering pattern**. Three consequences:

| # | Consequence | Candidate |
|---|---|---|
| **A** | A past-month bill takes that month's **last day**, with no lock configured | **removed** — the date is what the user asserts |
| **B** | A **current-month** bill takes **today**, not its document date. *For non-sale documents the accounting date is, in the ordinary case, never the document date* | **removed** |
| **C** | The branch taken depends on a numbering pattern deduced from existing data | **removed** — `D-26`, `JR-02` |

| Rule | Statement | Status |
|---|---|---|
| `DP-01` | The accounting date is **asserted, never derived**. If it is invalid the assertion is **refused**, not silently moved | `PROVISIONAL` |
| `DP-02` | A lock violation is an **error with a named cause**, never a re-dating | `PROVISIONAL` — `VF-08`: *being locked does not mean refused, it means re-dated* |
| `DP-03` | No accounting attribute is derived from any presentation artefact | `PROVISIONAL` `D-26` |
| `DP-04` | Where the system must choose a date it cannot derive, it **stops and asks** | `PROVISIONAL` |

---

## 3. The period object

> ### `D-06` — A period is a first-class object carrying state. `PROVISIONAL`

`VF-08` + `12 §2`: there is **no period object**. Two integers on the company derive boundaries; an
optional, **fully mutable** fiscal-year record may override them, with *"no state, no close, no link
to any entry"* (`COR-01`). What is locked is a **range of accounting dates**, per company, per lock
kind.

| Candidate element | Content | Status |
|---|---|---|
| Identity | tenant + company + period key, permanent | `EVIDENCE-DEPENDENT` — tenant clause on `GB-01` |
| Boundaries | explicit, immutable once the period has facts | `PROVISIONAL` |
| State | `open → closing → closed → final` | `PROVISIONAL` |
| Link to facts | every event names the period it was recognised into | `PROVISIONAL` `EL-05` |
| Close artefact | who, when, on what basis, against which preconditions | `PROVISIONAL` — `GAP-G01`: today there is **no artefact**, only a tracked field change |
| Reopen artefact | who, under what authority, why | `PROVISIONAL` `D-08` — blocked on `T0-10` |

**`GAP-G01` is an orphan unclassified id.** The question *"who closed, when, and on what basis?"* has
never been classified in the unknown register. Flagged at `D-21`/`15`.

---

## 4. Period attribution and re-attribution

| Rule | Statement | Status |
|---|---|---|
| `DP-05` | An event's period is fixed at recognition and **never silently moves** | `PROVISIONAL` |
| `DP-06` | Re-attribution is an explicit event with actor, reason and record — never a side effect of an edit | `PROVISIONAL` — closes `AE-03`, the worst of the four invisible events |
| `DP-07` | A correction lands in an **open** period and **names the period it corrects** | `PROVISIONAL` — today *"the correction lands in an open period, not the original one"*, with no link back |
| `DP-08` | Comparative reporting across a chart change is supported | `PROVISIONAL` `D-21` — rests on `GAP-A03`, an orphan id |
