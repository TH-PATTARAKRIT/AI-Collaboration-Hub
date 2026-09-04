# 13 — CANDIDATE EVENT → FINANCIAL FACT MAP

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. The chain

```
Source Fact → Business Event → Accounting Event → Recognition Rule → Journal
   → Journal Entry → Journal Item → GL Fact → Reconciliation State
   → Reporting Fact → Close State
```

**Two links have no carrier found in the searched scope** (`BS-02`; negative class `B`, boundary: the primary module tree — **962 manifested modules unsearched**, `GB-07`/`MCU-18`, independently re-derived at `18A §5`): the *Accounting Event* as an object, and
*Provenance* across every link. Everything the reference does is compressed into
`Journal Entry / Journal Item`, which is why the parent's `L5` called the entry both the
representation and the only durable record.

---

## 2. Link-by-link

### `L-1` Source Fact → Business Event

| Field | Content |
|---|---|
| Owner | the producing domain |
| Source of truth | the source document |
| Trigger | a business act |
| Invariant | the source fact has an identity in its own domain |
| Failure mode | `T-08` wrong source linkage · `T-10` omitted event |
| Correction | in the producing domain |
| Evidence | `GAP-B02` — *a producing module's business event has no identity of its own once posted* |
| Status | `PROVISIONAL` |

### `L-2` Business Event → Accounting Event

| Field | Content |
|---|---|
| Owner | **the ledger** |
| Source of truth | the accounting event (`D-01`) |
| Trigger | recognition, under a stated rule |
| Invariant | **one business event → at most one accounting event**, enforced by idempotency key (`D-24`) |
| Failure mode | `T-09` duplicate event — **`BW-06`, `BW-13`, `BW-15`, `NBW-23`: four instances** |
| Correction | supersession only (`EL-01`) |
| Evidence | `XM-01`, `MCU-34` |
| Status | `PROVISIONAL` · **the link with no carrier found in the searched scope** (class `B`) |

### `L-3` Accounting Event → Recognition Rule

| Field | Content |
|---|---|
| Owner | configuration, **versioned** |
| Invariant | the rule that produced a fact is **identifiable from the fact** |
| Failure mode | **`T-17` wrong measurement rule** — *the fact records the result, never the rule* |
| Evidence | `T-17` is one of the three classes the parent had to **add** because Wave A cases existed that no supplied class could hold |
| Status | `PROVISIONAL` — the rule-versioning design is not evidenced, only required |

### `L-4` Accounting Event → Journal

| Field | Content |
|---|---|
| Owner | the journal (purpose classification only — `JR-01`) |
| Invariant | placement carries **no** accounting consequence; numbering carries none either (`JR-02`, `D-26`) |
| Failure mode | `T-03` wrong period, via `VF-07` numbering-derived attribution |
| Evidence | `C07` consequence **C** |
| Status | `PROVISIONAL` |

### `L-5` Journal → Journal Entry

| Field | Content |
|---|---|
| Owner | the entry — presentation |
| Invariant | number immutable once assigned; **tenant-scoped**, not journal-scoped |
| Failure mode | `T-18` wrong integrity domain |
| Evidence | `T0-08` — index scoped by **journal, not company**; a wizard that **blanks the number** to escape it; missing index degrades to a **log line** |
| Status | `EVIDENCE-DEPENDENT` — blocked on `T0-08` |

### `L-6` Journal Entry → Journal Item

| Field | Content |
|---|---|
| Owner | the item — the financial fact `F3` |
| Invariant | signed amounts sum to zero **unconditionally** (`JE-02`); sign **and magnitude** agreement enforced at storage (`JE-03`, `JE-04`) |
| Failure mode | `T-06` wrong account · `T-07` wrong partner · `T-11` wrong analytic |
| Evidence | `CONTRA-05` balance invariant **switchable**; `CONTRA-01b` magnitude unprotected; `NBW-17` retroactive counterparty rewrite with the lock bypassed |
| Status | `PROVISIONAL` |

### `L-7` Journal Item → GL Fact

| Field | Content |
|---|---|
| Owner | the item; the GL is a **projection**, not a second store |
| Invariant | the GL is reconstructible from items alone |
| Failure mode | `T-16` wrong classification — *character changed after the fact, meaning altered without amount altering* |
| Evidence | `BW-33` control-account attribute **silently flipped by imported data**; `EV-016` type change is retroactive |
| Status | `EVIDENCE-DEPENDENT` — `D-32` blocked on `T0-09` |

### `L-8` GL Fact → Reconciliation State

| Field | Content |
|---|---|
| Owner | the settlement fact `F4`; the state is **derived** |
| Invariant | settlement ≤ residual, at storage level (`D-17`); settlement facts undestroyable (`D-18`) |
| Failure mode | `T-13` wrong reconciliation state |
| Evidence | `COR-09` no bound in any currency configuration; `VF-13` silent destruction; `BW-32` receivable settled by cash that never entered its company |
| Status | `PROVISIONAL` · cross-company clause `EVIDENCE-DEPENDENT` on `GB-02` |

### `L-9` Reconciliation State → Reporting Fact

| Field | Content |
|---|---|
| Owner | the report definition — **and this is the exposure** |
| Invariant | a report definition is **tenant-owned and company-scoped** |
| Failure mode | **`T-19` wrong report definition** — *nothing in the ledger is wrong and the reported figure still is* |
| Evidence | `MCU-04` report definitions **carry no company dimension**; `MCU-11` report company scope is a **caller-supplied parameter with no defence in depth**; `NBW-22` definition owned by another tenant; `BW-31`/`MCU-20` v19 aggregates at **today's** rate outside every record rule |
| Status | `EVIDENCE-DEPENDENT` — `MCU-04`+`MCU-11` merged and **`REMAINS GATING`** |

### `L-10` Reporting Fact → Close State

| Field | Content |
|---|---|
| Owner | the period object (`D-06`) |
| Invariant | close is earned, recorded, and its reversal is governed (`LC-01`…`LC-04`) |
| Failure mode | `T-03` wrong period · `T-14` wrong opening provenance |
| Evidence | `GAP-G01` **no close artefact of any kind**, only a tracked field change — and `GAP-G01` is an **orphan unclassified id** |
| Status | `PROVISIONAL` · reopen clause blocked on `T0-10` |

---

## 3. Where the chain breaks today — summary

| Break | Link | Class |
|---|---|---|
| No accounting-event object | `L-2` | `VERIFIED FACT` (negative class `B`) |
| No provenance on any link | all | `VERIFIED FACT` (negative class `B`) |
| No rule versioning | `L-3` | `T-17`, class added by necessity |
| Numbering determines period | `L-4` | `VF-07` |
| Identity scoped to journal, not tenant | `L-5` | `T0-08` |
| Settlement unbounded | `L-8` | `VF-12` |
| Report definitions unscoped | `L-9` | `MCU-04`/`MCU-11` gating |
| No close artefact | `L-10` | `GAP-G01`, unclassified |

**Eight breaks across ten links.** Three are blocked behind unresolved tolerance-zero boundaries and
two behind gating unknowns.
