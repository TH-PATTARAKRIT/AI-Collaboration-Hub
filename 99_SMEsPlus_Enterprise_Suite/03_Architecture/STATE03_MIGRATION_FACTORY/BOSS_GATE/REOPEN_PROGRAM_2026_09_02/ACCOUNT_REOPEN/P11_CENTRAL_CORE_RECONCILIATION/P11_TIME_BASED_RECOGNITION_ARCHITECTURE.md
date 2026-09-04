# P11 — UNIFIED TIME-BASED RECOGNITION ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 10 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Position — stated as the near-empty section it is

> ## `P10` is the least-evidenced process in the whole reconciliation.
>
> Wave A recorded the deferred-recognition producer contract as **`UNKNOWN — EVIDENCE REQUIRED`** and
> no later package closed it. `P10` has published nothing. **This architecture therefore consists of
> the contract `P10` must satisfy, and an explicit statement that its content is unknown.**
>
> Writing more than that would be inference presented as architecture.

## 2. What is known

| id | Fact | Evidence | Class |
|---|---|---|---|
| `TB-01` | Deferred revenue / cost release is a **period-run** event producing periodic reclassification entries in a general journal; the items are **not open items**; correction is by ordinary reversal | `SL-01` `05` §1, `08` Part 2 | ledger-interface verified |
| `TB-02` | The **producer contract is not established** — trigger, schedule object, basis, and idempotency are all unspecified | `SL-01` `05` §1 | `UNKNOWN — EVIDENCE REQUIRED` |
| `TB-03` | **No revaluation / unrealised-FX carrier was found in the scope read** (`GAP-H01`) — the adjacent time-based recognition class is also absent | `SL-01` `07` | `NOT FOUND IN SEARCHED SCOPE` |
| `TB-04` | **No prior-period attribution mechanism exists in the reference ERP at all**, so a late cost or a late release has nowhere correct to land — largely **original design work** | `SL-07` `17` §4 `JT-06` | `UAE-32`, new at P11 |
| `TB-05` | **`DC-10`** — with no producer contract, no duplicate-schedule guard can be asserted in either direction | `P11_DOUBLE_COUNTING_REGISTER.md` | `UNKNOWN` |

## 3. The contract `P10` must satisfy

Derived from the ledger side, which **is** established, and therefore statable now without pre-empting
`P10`'s own gate:

| # | Requirement | Why the ledger needs it |
|---|---|---|
| 1 | A **schedule object** with its own identity, distinct from the entries it generates | Otherwise `DC-10` is unguardable and a re-run duplicates the release |
| 2 | An **idempotency key per period release** (element 15) | The release is a machine-generated, repeatable event — the highest-risk class for `DC-01` |
| 3 | The **intended recognition date**, recorded before the lock mechanism can move it | `UAE-04` will otherwise silently re-attribute the release |
| 4 | An explicit **`N/A + reason`** for elements 5, 6, 8, 9 — no goods move | contract discipline: blanks are not acceptable |
| 5 | **Reversal linkage** to the original deferral, and to each prior release | element 13; `SRP-05` |
| 6 | A **remaining-balance reconciliation** to the deferral control account, reconstructible from the schedule alone | `S4` — otherwise it is a derived view, not a subledger |
| 7 | Declared **scope: `COMPANY`** — the release produces a financial effect | `SCP-04` |
| 8 | Behaviour when the target period is **closed** — denied, or routed to a prior-period attribution mechanism that **does not yet exist** | `TB-04`, `UAE-32` |

Requirement 8 is the one `P10` cannot satisfy alone: it depends on `UAE-32`, which is a design decision
shared with `P01` (late vendor bills) and `P03` (late costs) and owned by `P08`.
