# 03 — CANDIDATE ACCOUNTING EVENT MODEL

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01` · every statement carries a status label

---

## 1. The position

> ### `D-01` — The accounting event is separated from the journal entry that represents it. `PROVISIONAL`

**Evidence class** `INFERENCE` built on `VF-01` (`VERIFIED FACT`) and `BS-03` (`VERIFIED BUSINESS SEMANTIC`).

The reference model has no accounting-event object. The entry is both the representation *and* the
only durable record (`BS-03`). Four consequences follow in evidence, not in theory:

| Consequence | Evidence |
|---|---|
| A **partial** duplicate control exists (`NC-13`, class `E — CONTRADICTED`): a duplicated-reference field matches sale and purchase documents on the reference across draft and posted states and **suppresses auto-posting with a thread message**. It does not block manual posting, does not key on an accounting-event identity, and was **not found to extend to machine-generated entries** | `NC-13`, `XM-01`, `MCU-34` |
| "Correcting the event" and "editing its representation" collapse into one operation — which is why the destructive correction path exists | `EV-012` |
| A producing module's business event has no identity once posted | `GAP-B02` |
| Period re-attribution, migration provenance and the audit question *what did we recognise, as distinct from how we wrote it down* are all unanswerable | `L5 §2` |

**One separation resolves five otherwise independent problems.** That is the reason to make it, and
it is the reason the parent's own `L5` called it *the single most consequential design position in
this Wave*.

**Invalidation trigger.** A carrier **is** found — most plausibly in the **962 manifested modules
never searched** (`GB-07`, `MCU-18`). The negative is class `B`, not `A`. Registered at `D-01`.

---

## 2. Candidate event structure

`DESIGN CHOICE` throughout. No reference to adapt — this is invention against a proven absence.

| Element | Content | Status | Rationale |
|---|---|---|---|
| **Event identity** | Independent of any storage identifier, and of the entry that presents it | `PROVISIONAL` | `VF-17` — storage-keyed identity cannot survive migration, which is when it is most needed |
| **Source reference** | Producing domain + that domain's own event identity | `PROVISIONAL` | `GAP-B02` |
| **Idempotency key** | Deterministic over the source fact, not over the posting attempt | `PROVISIONAL` `D-24` | `XM-01` — the duplicate is undetectable today |
| **Recognition basis** | The rule under which the ledger asserts this | `PROVISIONAL` | needed for `VF-05`'s missing recognition date |
| **Actor** | Human, schedule, or **the system itself** | `PROVISIONAL` | `CR-08` — `VF-19`: seven system-emitted events, four invisible |
| **Reason** | Why this event exists, including for system-emitted events | `PROVISIONAL` | `CR-08` |
| **Provenance chain** | Source system → extraction → event, permanent | `PROVISIONAL` `D-04` | `F7` is not implemented at all (`BS-02`) |
| **Correction relation** | `corrects` / `corrected-by`, constrained | `PROVISIONAL` `D-03` | `VF-22` — today's pointer has **no constraint of any kind** |

---

## 3. Event taxonomy — candidate, derived from the 21 events found

The parent enumerated `AE-01`…`AE-21`. Reclassified here by **who initiates** and **whether the
operator can see it**, because that is the cut that produced the finding.

| Class | Members (parent ids) | Candidate SMEsPlus rule | Status |
|---|---|---|---|
| **Operator-initiated, explicit** | `AE-01` post · `AE-06` reverse · `AE-10` match · `AE-15` finalise · `AE-21` measure | Permitted. Recorded with actor and reason | `PROVISIONAL` |
| **Operator-initiated, destructive** | `AE-05` un-post · `AE-07` cancel · `AE-08` delete · `AE-20` merge | **Rejected as a general path.** Replaced by additive equivalents | `PROVISIONAL` — `VF-13`, `VF-14` |
| **System-emitted, visible** | `AE-11` exchange difference · `AE-12` exchange reversal · `AE-18` tax lock set | Permitted, with actor `system` and a stated reason | `PROVISIONAL` |
| **System-emitted, invisible** | `AE-02` re-date on posting · `AE-03` re-date on document-date change · `AE-13` cash-basis tax dated today · `AE-20` merge | **Rejected.** An invisible accounting event is the concrete list of what naive adoption imports | `PROVISIONAL` — `VF-19` |
| **Governance** | `AE-15` finalise · `AE-16` reopen · `AE-17` lock exception | Each becomes a first-class governed event with its own authority | `PROVISIONAL` — `D-08`/`D-27` blocked on `T0-10` |
| **Absent, must be designed** | period close · year-end transfer · revaluation · event recognition · approval | See `15` | mixed |

### The four invisible events, restated as the design agenda

`AE-02`, `AE-03`, `AE-13`, `AE-20`. **`AE-03` is the worst**: it changes period attribution with **no
lock configured** and no accounting justification (`VF-04`), and under `VF-06` it fires on routine
same-month entry, not only on late entry.

---

## 4. Event lifecycle — candidate

```
recognised → asserted → [ superseded-by-correction ]
                     ↘ [ settled ] (a separate fact, not a state of the event)
```

| Rule | Statement | Status |
|---|---|---|
| `EL-01` | An event, once asserted, is **never** amended or withdrawn — only superseded by a further event | `PROVISIONAL` — `BS-01` `F2` |
| `EL-02` | Supersession is explicit and bidirectional: the corrector names what it corrects, and the corrected names its corrector | `PROVISIONAL` — `VF-22` |
| `EL-03` | Immutability is **unconditional** — not a journal setting, not a company flag, not dependent on the calling module. *If it can be switched off, it is not immutability* | `PROVISIONAL` `D-02` — `VF-02` |
| `EL-04` | Settlement is **not** a state of the event. It is a separate fact class (`F4`) | `PROVISIONAL` — `BS-05` |
| `EL-05` | Every event carries the period it was **recognised into** and the period it was **asserted in**, and these may differ | `PROVISIONAL` — depends on `D-06` period object |
| `EL-06` | No event may be created by a path that bypasses event construction — **including raw data paths** | `EVIDENCE-DEPENDENT` — 62 raw-SQL sites, **0 assessed**; `MCU-16` |

---

## 5. Duplicate and missing event detection — candidate

| Concern | Candidate mechanism | Status |
|---|---|---|
| Duplicate | Idempotency key unique **within tenant**, refusal on collision, with the prior event returned | `PROVISIONAL` `D-24` |
| Missing | Producing domains declare expected event counts per period; close preconditions test them | `PROVISIONAL` — extends `BS-08` |
| Out-of-order | Recognition date is the event's own, never the arrival order | `PROVISIONAL` |
| Concurrency | **Open.** `MCU-33`/`MCU-35` were reclassified **into** gating: the reference's own documentation records that when the governing uniqueness condition is unmet *"sequence numbers may not be unique"*, and a missing index degrades to a **logged warning** | `EVIDENCE-DEPENDENT` — blocked on `T0-08` |

---

## 6. What this model does not settle

| Question | Why open | Decider |
|---|---|---|
| Does an event span companies? | `GB-01` unresolved; `GB-02` widened twice | **Boss** |
| Is the event or the entry the unit of tamper-evidence? | `T0-08` unresolved; `VF-17` says storage-keyed fails | research → Boss |
| Does a producing domain own recognition, or does the ledger? | `MCU-56` split — bank path holds the **only** production consumers of the immutability suppression flag, writing to **posted** moves | research |
| Approval before assertion — engine or design? | `MCU-08` rescoped to the module-baseline decision | **Boss** |
