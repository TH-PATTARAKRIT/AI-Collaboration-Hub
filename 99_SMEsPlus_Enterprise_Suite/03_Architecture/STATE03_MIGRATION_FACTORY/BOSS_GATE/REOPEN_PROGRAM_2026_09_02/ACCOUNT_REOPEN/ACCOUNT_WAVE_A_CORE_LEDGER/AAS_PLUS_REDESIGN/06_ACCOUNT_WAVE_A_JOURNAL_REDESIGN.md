# 06 — CANDIDATE JOURNAL REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. What a journal is, in the candidate model

The reference journal carries four unrelated responsibilities at once: it is a **classification of
purpose**, a **numbering authority**, a **company boundary**, and a **control scope** (secure/hashed).
Wave A evidence shows the second and fourth causing damage through the first.

> ### `D-26` — Numbering is a presentation concern and must never influence period attribution. `PROVISIONAL`
>
> `VF-07`: period attribution — an accounting fact — is derived from a **numbering format**, which is
> itself deduced from the highest existing number already in the journal (`C07` consequence **C**).
>
> `L5`/`C07` name this the wrong dependency direction, and it is: **a presentation artefact derived
> from existing data is determining which period a fact belongs to.**

| Candidate rule | Statement | Status |
|---|---|---|
| `JR-01` | A journal classifies **purpose**. It is not the numbering authority, not the identity authority, and not the sole control scope | `PROVISIONAL` |
| `JR-02` | Numbering is a **presentation service**; no accounting attribute is ever derived from a number or a numbering pattern | `PROVISIONAL` `D-26` |
| `JR-03` | A journal belongs to exactly one company, within exactly one tenant | `EVIDENCE-DEPENDENT` — tenant clause blocked on `GB-01` |
| `JR-04` | Posting authority is a property of the **event type and the actor**, not of the journal alone | `PROVISIONAL` |
| `JR-05` | Tamper-evidence is a **ledger-wide guarantee**, not a per-journal opt-in | `EVIDENCE-DEPENDENT` — blocked on `T0-08` |

`JR-05` is the direct consequence of `VF-02`: today the hash is one of only two unconditional
immutabilities, **and it is opt-in per journal**. A guarantee that must be switched on is a setting.

---

## 2. Journal responsibilities — decomposed

| Reference responsibility | Candidate owner | Status |
|---|---|---|
| Purpose classification (sale / purchase / bank / cash / general) | **the journal** | `PROVISIONAL` |
| Source eligibility — which producers may post here | **the journal**, declared | `PROVISIONAL` |
| Entry numbering and reset pattern | **numbering service**, no accounting effect | `PROVISIONAL` `JR-02` |
| Entry identity / uniqueness | **the event and the entry**, tenant-scoped | `EVIDENCE-DEPENDENT` `T0-08` |
| Company boundary | **the company on the event** | `PROVISIONAL` |
| Currency context | journal currency must agree with its default account currency (`EV-019`) — keep | `PROVISIONAL` |
| Secure/hash scope | **ledger-wide** | `EVIDENCE-DEPENDENT` `JR-05` |
| Lock behaviour | sale/purchase locks raise the effective lock by journal type (`VF-08`) — **keep as policy, reject as re-dating** | `PROVISIONAL` |

---

## 3. Default, suspense and interim behaviour

| Concern | Reference | Candidate | Status |
|---|---|---|---|
| Suspense account on a journal | exists | keep — but every suspense posting is an **open item with an owner and an age** | `PROVISIONAL` |
| Interim accounts | exist for outstanding payments | keep | `PROVISIONAL` |
| Default account | per journal | keep | `PROVISIONAL` |
| Liquidity journal → one company, sharing refused | `EV-019` | **keep unchanged** — `BS-10`, a bank account belongs to one legal entity | `PROVISIONAL` |

---

## 4. `T0-08` — why journal-scoped identity is the open wound

`VF-02` and `T0-08` together. The parent characterised entry identity as:

| Element | Finding |
|---|---|
| Declared uniqueness constraint | empty definition string — **not a defect** per `G-C6`; a delegation idiom that registers a post-init assertion. The defect is the index **scope** |
| Real control | a raw-DDL index scoped by **journal, not company** |
| Lock | conditional |
| Missing index | degrades to a **log line**, not a refusal |
| Escape hatch | a wizard that **blanks the number** to escape the index |
| Global switch | a database-wide key disabling number/date alignment |

**Consequence for this file.** `JR-05` and `D-14` (tamper-evidence on business identity) cannot be
settled while identity is journal-scoped and conditionally enforced. **`T0-08` is unresolved and this
design is blocked behind it.** Registered at `D-14`, `D-26`.
