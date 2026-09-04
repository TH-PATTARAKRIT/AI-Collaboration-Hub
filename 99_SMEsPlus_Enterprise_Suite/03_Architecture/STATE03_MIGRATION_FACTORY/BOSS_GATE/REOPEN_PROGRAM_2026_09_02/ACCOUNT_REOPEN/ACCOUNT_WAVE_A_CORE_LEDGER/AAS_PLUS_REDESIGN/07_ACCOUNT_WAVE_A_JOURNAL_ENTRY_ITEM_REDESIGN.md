# 07 — CANDIDATE JOURNAL ENTRY / JOURNAL ITEM REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. Three layers, not one

The reference fuses **document**, **event** and **ledger representation** into one object
(`BS-03`, `VF-01`). The candidate separates them.

| Layer | Owns | Immutable? | Status |
|---|---|---|---|
| **Source document** | what the counterparty and the business agreed; the document date | its own domain | `PROVISIONAL` |
| **Accounting event** | recognition, identity, provenance, idempotency, correction lineage | **yes, unconditionally** | `PROVISIONAL` `D-01` |
| **Journal entry** | presentation: number, journal placement, narration | number immutable once assigned; narration mutable | `PROVISIONAL` |
| **Journal item** | the financial facts (`F3`) | **yes** — the immutable core of `04 §2` | `PROVISIONAL` |

**Why the separation earns its cost.** `L5 §2` lists it: duplicate detection, correction semantics,
period re-attribution, migration provenance, and *"what did we recognise, as distinct from how we
wrote it down."* Five problems, one separation.

---

## 2. Header versus line — ownership

| Attribute | Candidate owner | Reference position | Status |
|---|---|---|---|
| Recognition / accounting date | **event** | on the entry, **system-derived** (`VF-04`) | `PROVISIONAL` |
| Document date | **source document** | on the entry, user-owned — *the only date the user actually owns* | `PROVISIONAL` |
| Company | **event** | via the journal | `PROVISIONAL` |
| Tenant | **event** | **no tenant concept found in the primary tree** — class `A` *in that scope* (`VF-15`) | `EVIDENCE-DEPENDENT` `GB-01` |
| Number | **entry** | on the entry | `PROVISIONAL` |
| Classification (account) | **item** | on the item, DB-enforced | `PROVISIONAL` |
| Signed company amount | **item** | the canonical stored amount | `PROVISIONAL` `FF-01` |
| Transaction currency + amount | **item** | required always; **magnitude unprotected** | `PROVISIONAL` |
| Counterparty | **item** | item-level, hash-covered | `PROVISIONAL` |
| Due date | **item** | item-level; **not frozen, outside hash coverage** | `PROVISIONAL` |
| Analytic | **item** | a distribution expanded into a destructible subledger | `UNKNOWN` `D-28` |
| Tax | **item** | outside hash coverage (`COR-06`) | routed `WAVE-D` |
| Residual / reconciled / payment state | **derived, never stored authoritatively** | stored computed | `PROVISIONAL` `FF-02` |

---

## 3. Debit/credit invariants

| Rule | Statement | Status |
|---|---|---|
| `JE-01` | One signed company-currency amount per item; debit and credit are **presentation** | `PROVISIONAL` `ST-03` |
| `JE-02` | The sum of signed amounts over an event is zero — **unconditionally** | `PROVISIONAL` |
| `JE-03` | Sign agreement between company and transaction amounts is enforced **at storage level** | `PROVISIONAL` — `COR-06`, one of only four storage-level guarantees found |
| `JE-04` | **Magnitude** agreement is enforced too — `CONTRA-01b` shows magnitude neither write-guarded nor hash-detected | `PROVISIONAL` |
| `JE-05` | `Debit = Credit` is **necessary and grossly insufficient** — see file `14` | `PROVISIONAL` |

> `CONTRA-05` recorded that the entry balance invariant is **switchable** in the reference. `JE-02`'s
> word *unconditionally* is doing deliberate work: `VF-02` is the pattern, and a switchable invariant
> is not an invariant.

---

## 4. Hash and tamper-evidence

| Finding | Candidate | Status |
|---|---|---|
| Hash keyed on **storage row identifiers** (`VF-17`) | key on **business identity** | `EVIDENCE-DEPENDENT` `D-14` / `T0-08` |
| Company amounts serialised at the **transaction** currency's decimal places — a collision vector (`COR-11`, `CONTRA-06`) | serialise at the amount's own precision | `PROVISIONAL` |
| Five fields pass both the write guard and the hash guard | the immutable core is **wholly covered**, with no exceptions | `PROVISIONAL` |
| Hash is opt-in per journal | ledger-wide (`JR-05`) | `EVIDENCE-DEPENDENT` |
| Hashing cannot be undone (`AE-09`) | keep | `PROVISIONAL` |

---

## 5. Correction and reversal at entry level

| Operation | Candidate | Status |
|---|---|---|
| Edit draft | permitted | `PROVISIONAL` |
| **Un-post** | **removed.** It destroys matching history and analytic lines silently and unrecoverably (`VF-13`) | `PROVISIONAL` |
| **Delete** | **removed** once asserted. Today it is available wherever the audit-trail flag is off or bypassed, and is **invisible afterwards** (`AE-08`) | `PROVISIONAL` |
| Cancel | routed through additive reversal, never through un-posting | `PROVISIONAL` |
| Reverse | permitted; **the lineage link is constrained** — unique, non-severable, with a declared delete behaviour | `PROVISIONAL` — `BW-35`/`VF-22` |
| Re-enter | permitted; **linked to what it corrects** | `PROVISIONAL` `FF-03` |
| Suppression flags | **no production path may suppress posted-fact immutability** | `EVIDENCE-DEPENDENT` — `MCU-01` gating; `MCU-56`: the bank path holds the **only** production consumers, writing to **posted** moves |

---

## 6. Residual and reconciliation state on the item

Derived, never authoritative (`FF-02`). Reconstruction is mandatory, and today whether *any*
mechanism reconstructs after drift is `GAP-E03` — **an orphan unclassified id**, which is itself the
finding: the question of whether the ledger can rebuild its own derived state has never been
classified.
