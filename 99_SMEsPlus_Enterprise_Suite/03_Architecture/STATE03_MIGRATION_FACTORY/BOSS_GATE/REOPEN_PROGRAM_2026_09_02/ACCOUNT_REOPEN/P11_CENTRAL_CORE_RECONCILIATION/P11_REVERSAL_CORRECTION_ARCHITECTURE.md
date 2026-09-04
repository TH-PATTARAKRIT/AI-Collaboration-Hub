# P11 — UNIFIED REVERSAL / CORRECTION ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 12 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The resolved principle

> **Once an accounting event exists, it is corrected only by further accounting events.**
>
> The reference model offers a destructive alternative **and makes it the convenient one. That
> convenience is the defect.**

## 2. The three routes, and their verdicts

| Route | What it does | Destroys | Verdict |
|---|---|---|---|
| Edit while draft | changes the entry before it is a fact | nothing | **`ADAPT`** |
| **Un-post, edit, re-post** | retracts the fact, changes it, re-asserts it | **matching history and analytic lines, silently and unrecoverably** | **`REJECT` as a general path** |
| Reverse and re-enter | adds a counter-fact, then a corrected fact | nothing | **`ADAPT` — this must be the default** |

## 3. What the destructive path destroys, per process

| Destroyed | Owner of the loss | Recoverable? |
|---|---|---|
| Analytic lines | `P09` | **no** — regenerated, not restored (`C4-01`) |
| Matching / settlement history | `P06` | **no** |
| Cash-basis tax lineage | `P07` | generated entries can be reversed but **cannot be reset to draft** |
| Reversal lineage itself | `P08` | **a `CLOSED — VERIFIED DEFECT`** (`MCU-15` / `BW-35`) |
| Deletion evidence | assurance | written to the **application log**, outside the tenant's data (`SC-08`) |

## 4. Correction defects that cross processes

| id | Defect | Evidence |
|---|---|---|
| `RC-01` | **Cancellation routes through un-posting**, so it carries the destruction | `AE-07` |
| `RC-02` | **Deletion is possible where the audit-trail flag is off or bypassed**; immutability is **configuration, not a ledger property** | `AE-08`, `EV-011`, `COR-07`; `T0-03` `UNRESOLVED` |
| `RC-03` | **A reversal can be re-dated into a different year from its original** | `M-04`, `PC-02` |
| `RC-04` | **Merging classifications retargets posted items, deletes accounts past the ORM's own guards, and writes no tracking of any kind** | `AE-20`, `COR-08`; `C4-02` |
| `RC-05` | **Reversal-to-original linkage is required by contract elements 12 and 13 and does not exist** — *without it, no correction can be proven to be a correction rather than a second event* | `SL-07` `16` §5 |
| `RC-06` | **Entry reference and narration remain writable when posted** | `EV-022` |
| `RC-07` | **Hashing covers only hashed fields**; tax items are outside coverage; the chain keys on **storage row identifiers** and cannot survive a tenant split, merge, restore or migration | `AE-09`, `COR-06`, `COR-12`, `SC-07` |

`RC-05` is the one that converts a correction problem into a **double-counting** problem: an unlinked
correction and a duplicate are indistinguishable, which is `DC-01` seen from the correction side.

## 5. Positions

| id | Position | Basis |
|---|---|---|
| `RCP-01` | **Un-post does not exist.** A posted fact is corrected by reversal and re-entry only | §2 |
| `RCP-02` | **Immutability is a ledger property, not a configuration flag.** No setting, key or bypass makes a posted fact editable or deletable | `RC-02`, `T0-03` |
| `RCP-03` | **Every correction carries a link to what it corrects** (elements 12, 13), and the link is mandatory, not conditional | `RC-05` |
| `RCP-04` | **A reversal is recognised in the period of the original where that period is open, and otherwise through an explicit prior-period attribution event — never by silent re-dating** | `RC-03`, `PCP-05` |
| `RCP-05` | **Classification merge is an accounting event with an actor, a record and a reversal path, or it is forbidden** | `RC-04` |
| `RCP-06` | **Integrity coverage is complete over the fact — all fields, all dimensions, tax included — and keys on business identity so it survives migration and tenant reshaping** | `RC-07`, `TI-03` |
| `RCP-07` | **Control evidence, including evidence of destructive acts, is stored inside the tenant's own data** | `SC-08`, `SCP-06` |
