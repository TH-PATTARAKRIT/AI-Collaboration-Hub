# 11 — CANDIDATE LOCK / CLOSE / REOPEN REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. What is wrong today, stated once

`VF-08`: **what is locked is a range of accounting dates**, per company, per lock kind. No period
object, no document lock, no entry lock. And decisively:

> **Being "locked" does not mean refused. It means re-dated.**

`VF-09`: soft locks move backward **freely, with no distinct authority and no artefact**.

`12 §3` records the honest summary: the reference gives **one genuinely irreversible control and four
advisory ones — and the four advisory ones are what most users will operate.** A soft lock is best
understood as a **default date policy**, not as a close.

---

## 2. The candidate model — close is a state, lock is its consequence

| Concept | Candidate definition | Status |
|---|---|---|
| **Close** | a **state a period enters** when it has earned it, recorded as an artefact with actor, time and basis | `PROVISIONAL` `D-06`/`D-07` |
| **Lock** | the **consequence** of a close state, not a separate typed date | `PROVISIONAL` |
| **Finality** (`F6`) | governance-declared, permanent once hard | `PROVISIONAL` `BS-01` |
| **Reopen** | a **governed event** with its own authority, artefact and reason | `PROVISIONAL` `D-08` — blocked on `T0-10` |
| **Exception** | a named, time-bounded, separately-authorised derogation | `EVIDENCE-DEPENDENT` `D-27` — blocked on `T0-10` |

| Rule | Statement | Status |
|---|---|---|
| `LC-01` | A posting into a closed period is **refused with a named cause**. It is never silently re-dated | `PROVISIONAL` `DP-02` |
| `LC-02` | Close preconditions are enforced by the ledger, with a route to the offending records | `PROVISIONAL` `BS-08` |
| `LC-03` | Irreversible means irreversible — monotonic, no exception, no removal | `PROVISIONAL` `ST-08` |
| `LC-04` | Every close, reopen and exception produces a **durable artefact inside the tenant's data** | `PROVISIONAL` `CR-04` |
| `LC-05` | Month 12 is procedurally an ordinary month close | `PROVISIONAL` `BS-09` |

---

## 3. The precondition pattern — adopted and generalised

`ST-07` / `12 §4` call this *"the single best control pattern found in Wave A"* and *"the only place
where the reference treats closing as a state the data must earn rather than a date someone types."*

| Precondition | Reference | Candidate | Status |
|---|---|---|---|
| No draft entries in the period | hard lock only | **all closes** | `PROVISIONAL` |
| No unreconciled bank statement lines | blocks any fiscal-effective lock | **keep** | `PROVISIONAL` |
| No unsecured entries where securing is expected | recommended by the parent | **adopt** | `PROVISIONAL` |
| No unresolved suspense items | — | **add** | `PROVISIONAL` — follows `06 §3` |
| No settlement in flight whose dependent tax event cannot post | — | **add** | `PROVISIONAL` — `COR-17` |
| Derived state reconciles to the immutable core | — | **add** | `PROVISIONAL` — `FF-02`, `GAP-E03` |

---

## 4. Hard versus soft — the candidate replacement

The five typed lock dates are replaced by **period state plus scope**.

| Reference | Candidate | Status |
|---|---|---|
| Global lock date | period state `closed` | `PROVISIONAL` |
| Hard lock date | period state `final` — monotonic, no exception | `PROVISIONAL` `LC-03` |
| Sale / purchase lock dates | close **scoped by event class**, not by journal type | `PROVISIONAL` |
| Tax lock date | owned by `WAVE-D TAX`; the ledger carries the **tax point** (`09 §1`) | routed |
| Cascade from parent companies | **`CL-05` — an open Boss decision**, not a technical necessity | `UNKNOWN` — decider **Boss** |

`CL-05` is stated by `16 §5` as: *a parent's irreversible lock cascading to subsidiaries is a policy
choice, and it couples entities a tenant may consider independent.* Left open deliberately.

---

## 5. The exception object — the blocked centre of this design

> ### `D-27` — Granting and revoking a derogation require **different** authority. `EVIDENCE-DEPENDENT`

`T0-10` characterises the lock-exception object — **the control over the control** — as:

| Property | Finding |
|---|---|
| Record-level scoping | **none** |
| Company on creation | **caller-supplied** |
| Revocation authority | **group membership alone**, then a write under elevated privilege |
| Revoker vs granter | `COR-04` — **the same role** |
| Scope | one company, optionally **every user**, optionally **forever** (`EV-021`) |

**`T0-10` is unresolved.** Until it closes, neither `D-08` (reopen governance) nor `D-27` can be
settled, because the evidence does not yet establish whether reopening and exception-granting are one
mechanism or two. Registered in `01 §1.2`.

---

## 6. Year-end

| Item | Finding | Candidate | Status |
|---|---|---|---|
| Year-end closing entry | **not found** within the core accounting and reporting modules — **class `B`** (`NC-04`); localization and third-party modules **not searched** | no reference to adapt | — |
| Retained-earnings transfer | **never posted**; the result is computed at report time | **`UNKNOWN` — Boss decision** | `UNKNOWN` `D-22` |
| Current-year earnings | derived, never stored | keep derived, keep reconstructible | `PROVISIONAL` |
| Carry-forward | a type property at report time | keep the concept, add auditability | `PROVISIONAL` |

`D-22` is a genuine decision, not a research gap: **does SMEsPlus post a year-end result transfer, or
derive the result at report time?** The reference's absence of a year-close event independently
corroborates the Boss baseline that month 12 is ordinary — but that baseline does not by itself settle
whether the transfer is posted. **Decider: Boss.**
