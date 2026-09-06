# 70 — P05 CANDIDATE EVENT AND STATE REGISTER

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-03` · **PHASE S CANDIDATE — NOT A FINAL CONTRACT**

## 1. P05-Owned Events

Only events whose **truth P05 owns**. Events belonging to another process appear as boundaries, not
as P05 events.

| ID | Event | Owner | Creates obligation? | Creates accounting effect? | Scope | Evidence |
|---|---|---|---|---|---|---|
| `EV-01` | Cost incurred and evidenced | P05 | No | No | COMPANY | FACT VERIFIED |
| `EV-02` | Costs grouped into a claim | P05 | No | No | COMPANY | FACT VERIFIED |
| `EV-03` | Claim submitted for authorisation | P05 | No | No | COMPANY | FACT VERIFIED |
| `EV-04` | **Claim authorised** | P05 | **Yes** | **Yes — in draft** | COMPANY | FACT VERIFIED |
| `EV-05` | Obligation recorded (posted) | P05 | — | Yes | COMPANY | FACT VERIFIED |
| `EV-06` | Obligation settled | **P06 consumes**; P05 observes | — | Yes | COMPANY | FACT VERIFIED |
| `EV-07` | Tax withheld at settlement | P05 emits; **P07 statutory** | reduces cash vs obligation | Yes | COMPANY | FACT VERIFIED |
| `EV-08` | Claim refused after authorisation | P05 | withdraws | **destroys the draft artefact** | COMPANY | FACT VERIFIED |
| `EV-09` | Claim reset to draft after recording | P05 | withdraws | reverses, then **severs lineage** | COMPANY | FACT VERIFIED |
| `EV-10` | Float replenished | P05 | Yes (to the holder) | Yes | COMPANY | FACT VERIFIED |
| `EV-11` | Float drawn down by a claim | P05 | — | Yes | COMPANY | **SUPPORTED INTERPRETATION** — see `45`: no live-posted instance exists in evidence |
| `EV-12` | Funds advanced against a future cost | P05 | Yes | Yes (incorrectly, as expense) | COMPANY | FACT VERIFIED (source + shipped data); **installed nowhere** |
| `EV-13` | Advance liquidated | P05 | reduces | Yes | COMPANY | FACT VERIFIED (source); **installed nowhere** |

## 2. The Three-State Separation — `PSC-01`

| State | Question it answers | Who should own it | Reference behaviour |
|---|---|---|---|
| **Authorised** | *May this cost be incurred / claimed?* | operational management | conflated |
| **Recognised** | *Does this obligation exist in the books, at what date, for which company?* | accounting | **emitted by the authorisation transition, elevated** |
| **Settlement-ready** | *May this be paid?* | accounting/treasury control | **a genuinely separate act** — a distinct method, on a different state gate, behind a different permission group |

> **Correction after AAS-03 Expert 4 (`RE-45`).** The heading calls this a three-state separation, and
> the requirement below is unchanged — but **only two of the three are conflated in the reference.**
> Authorisation emits the accounting entry, in draft; **posting is separate**, and the reference gets
> that part right. `69 §B` carried the stronger, wrong wording *"these three collapse into one"* while
> its own table said otherwise; that wording is corrected there. This table was already accurate and is
> sharpened here only to remove *"downstream of the same transition"*, which understated the separation.
>
> **The correction narrows the defect without weakening it.** The conflated pair is the one that
> matters: an operational approver emits a ledger fact.

> **`SR-01` CANDIDATE REQUIREMENT.** SMEsPlus must make these three **separately observable and
> separately authorised**. An operational approver must not be able to emit a ledger fact as a
> side-effect of approving. **The binding half of this requirement is the authorisation/recognition
> pair**; the recognition/settlement-readiness boundary already exists in the reference and needs to be
> preserved rather than created.

## 3. State Model

`captured` → `claimed` → `submitted` → **`authorised`** → `recorded` → `settled`
Branches: `refused` (from submitted/authorised) · `reset` (from recorded) · `cancelled`.

| Property | Finding |
|---|---|
| Is state stored or derived? | **Derived** from the accounting artefacts, then stored. The document follows the ledger rather than driving it. |
| Can a state be reached without its precondition? | **Yes** — the authorisation marker is a plain stored value with no server-side guard, so `authorised` is reachable by writing the field. |
| Is there a terminal immutable state? | **No.** `recorded` is mutable; `settled` is reversible; lineage is severable. |
| Is there a `corrected` state? | **No.** Correction is by mutation or by reversal-and-detach. See `74`. |

## 4. Events P05 Does **Not** Own — boundaries only

| Event | Owner | P05's only interest |
|---|---|---|
| Payment executed / cleared / reconciled | **P06** | that the obligation became settled |
| Period opened / closed / locked | **P08** | whether P05 may record at a date |
| Statutory return filed | **P07** | that P05 supplied a withheld-tax event |
| Asset capitalised / depreciated | **P04** | **none** — `CH-08`, declaration only |
| Recognition schedule built | **P10** | that P05 could not decide it — `CH-09` |
| Cost re-invoiced to a customer | **P02** | that a flag was set |
| Budget / plan consumption | **P09** | that an attribution was published |

**No internal behaviour of any of the above was researched.**
