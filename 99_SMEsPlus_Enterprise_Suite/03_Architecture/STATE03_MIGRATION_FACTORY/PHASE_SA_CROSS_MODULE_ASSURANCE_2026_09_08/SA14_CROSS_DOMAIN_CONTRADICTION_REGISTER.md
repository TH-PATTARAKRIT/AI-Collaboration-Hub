# SA14 — CROSS-DOMAIN CONTRADICTION REGISTER
## CP-SA-80 — CROSS-DOMAIN CONTRADICTION GATE

Status: **HOLD** — 6 contradictions registered, 0 resolved in this session, 2 require Boss authority.

---

## 1. What counts as a contradiction here

Not every open item is a contradiction. A contradiction is recorded only where **two verified
positions cannot both be acted on**, or where **one programme's published position is
inconsistent with another programme's published position on the same subject**.

Gaps, thin evidence and undetermined designs are recorded elsewhere (`SA01`, `SA16`). Mixing
them into this register would inflate it and hide the items that genuinely block.

---

## 2. Register

### XD-01 — Sell-side cancellation gate: an input recorded as missing in one programme and established in another

| Field | Value |
|---|---|
| Parties | Group A (Sales/Inventory/Purchase backbone) ↔ Account Phase S programme |
| Group A position | `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY` since 2026-08-31, terminal at `77e93d44`; three interface questions posed and unanswered; Group A explicitly declines to invent AR semantics |
| Account position | P02 Order-to-Cash and P08 Record-to-Report executed and Phase S closed conditionally at `CP-SC-15`; customer-invoice lifecycle semantics are within their established scope |
| Measured fact | Instrument in `SA00` §9: the subject appears in 28 blobs, of which **`ACCOUNT_REOPEN` = 0**; the same instrument's positive control fires 17/17 |
| Effect | Group A's Pre-Development Gate stands at `HOLD` on this item; `SA04` R-20, `SA07` AR-23, `SA15` E2E-01 all carry the break |
| Class | Cross-programme handoff failure — neither programme is internally wrong; **no party owned the boundary** |
| Resolution authority | **Boss** — Group A itself records the two options: *(a)* require a symmetric sell-side gate once Accounting supplies the answers, or *(b)* accept the current asymmetry as a disclosed risk trade-off |
| Status | **`OPEN — BOSS AUTHORITY REQUIRED`** |

### XD-02 — Two commercial sides, two different control floors

| Field | Value |
|---|---|
| Parties | Sales ↔ Purchase (within the Group A backbone) |
| Position A | The buy side carries a hard, test-confirmed amount-threshold approval gate, and a hard demand-approval gate before conversion |
| Position B | The sell side's two candidate gates — credit limit and stock availability — are both evidenced as **advisory only**; confirmation is not blocked by either |
| Why a contradiction and not merely an asymmetry | `SA03-F-02`: the sell side can **create** a buy-side commitment directly, with no human demand step. A document therefore enters the buy side *below the control floor the buy side enforces on itself*. The two positions cannot both hold |
| Class | Control-integrity contradiction |
| Resolution authority | SMEs Core design position, then Boss confirmation — see `SA13` |
| Status | **`OPEN — SMEs CORE POSITION STATED`** |

### XD-03 — An approval control whose evidence half was never exercised

| Field | Value |
|---|---|
| Parties | Approval/Workflow domain ↔ Audit/Evidence domain |
| Position A | Approval is a hard gate on the buy side; approver assignment is populated on 98.5% of commitment rows |
| Position B | The fields recording that an approval **actually occurred** are populated on **0 of 27,874 rows** |
| Contradiction | A control asserted to be operative produces no evidence that it operated. Under `SA11`, an audit requirement that cannot be evidenced is not a control |
| Related | Group A **A2**, status `EVIDENCE MISSING / BOSS DECISION REQUIRED` — the internal logic of the three identified approval modules is unavailable |
| Resolution authority | Boss election per A2: commission source acquisition, or accept the vendor-neutral shape as final |
| Status | **`OPEN — BOSS AUTHORITY REQUIRED`** |

### XD-04 — A published register that is stale against its own programme's corrections

| Field | Value |
|---|---|
| Parties | Group A exception matrix ↔ Group A invariant and gap registers (same programme) |
| Fact | The exception matrix is the only one of the programme's six registers with no corrective-update section. It still publishes `EVIDENCE_MISSING` for two items that sibling registers record as closed, and its own cross-cutting note still names one of them the highest-value follow-up |
| Effect | Any consumer reading that register alone inherits two closed items as open |
| Class | Revision-log defect — the correction was made in the programme and never edited into the register that publishes the claim |
| Disposition | Phase SA does **not** inherit the stale rows; `SA09` records them as `ESTABLISHED — via correction`, sourced from the registers carrying the correction and the independent re-verification confirming it |
| Resolution authority | PMO / owning programme |
| Status | **`OPEN — RECORDED, NOT INHERITED`** |

### XD-05 — Cross-module evidence unreachable from the lineage that depends on it

| Field | Value |
|---|---|
| Fact | The nine Group A cross-module artefacts (capability models, E2E map, event/dependency map, ownership matrix, exception matrix, invariant register, gap register) exist **only** on `claude/group-a-sales-inventory-purchase-dr002` `8b0993d8`. Verified by tree listing across all five Group A branches: dr002 carries the full set; the corrective, review and both re-verification branches carry only session-prompt files in that directory |
| Effect | The terminal verified state of Group A cannot cite its own foundational evidence without a cross-branch read |
| Already registered by the owning programme | **C4**, `EVIDENCE MISSING (in-lineage)`; and **C5**, `GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE` |
| Phase SA aggravation | This is a large part of why the Phase SA entry baseline omitted the programme entirely (`SA00-F-02`). Evidence that is only reachable by archaeology gets left out by the next executor — and it was |
| Resolution authority | PMO |
| Status | **`OPEN — PMO ACTIONABLE`** |

### XD-06 — A ruling without a contract behind it

| Field | Value |
|---|---|
| Parties | BD-ACC-01 (Accounting Event Identity ownership) ↔ every source module |
| Position A | BD-ACC-01 rules that the Source Module owns the Business Fact, Accounting Core owns the canonical Accounting Event Identity, and the Posting Engine owns posting |
| Position B | `SA04` R-20 shows a source module requiring an accounting lifecycle fact that no published interface supplies. `SA03` shows two round-trip dependencies where a source module derives its own state by reading Accounting's result back |
| Contradiction | Ownership is ruled but not contracted. A round-trip read is the shape ownership rules exist to prevent, and it is currently the evidenced mechanism on both commercial sides |
| Resolution authority | SMEs Core — publish the cross-domain contract; Boss confirms at the Functional Design gate |
| Status | **`OPEN — DESIGN OBLIGATION RECORDED`** |

---

## 3. Summary

| Status | Count | Items |
|---|---|---|
| `OPEN — BOSS AUTHORITY REQUIRED` | 2 | XD-01, XD-03 |
| `OPEN — SMEs CORE POSITION STATED` | 1 | XD-02 |
| `OPEN — DESIGN OBLIGATION RECORDED` | 1 | XD-06 |
| `OPEN — RECORDED, NOT INHERITED` | 1 | XD-04 |
| `OPEN — PMO ACTIONABLE` | 1 | XD-05 |
| `RESOLVED` | **0** | — |

**No contradiction was resolved in this session.** Registering a contradiction is not resolving
it, and this register does not present it as such.

## 4. SA14-F-01 — five of six contradictions are boundary defects, not domain defects

XD-01, XD-03, XD-04, XD-05 and XD-06 all sit **between** parties. Not one is an error inside a
domain's own reasoning. Each programme was internally coherent and independently verified; the
defects live in the seams, and every control that scoped itself to a single programme was
structurally incapable of seeing them.

This is the empirical justification for Phase SA existing as a phase. It is also the reason
the `CP-SA-80` gate cannot be closed by any amount of additional work *inside* the domains.

## 5. SMEs Core first-detector status

| Contradiction | First detected by | Boss first detector? |
|---|---|---|
| XD-01 | SMEs Core cross-module review, this session | No |
| XD-02 | SMEs Core cross-module review, this session | No |
| XD-03 | SMEs Core, from Group A's own published figures | No |
| XD-04 | SMEs Core cross-file consistency check | No |
| XD-05 | Group A's own independent verifier (C4/C5), re-raised here | No |
| XD-06 | SMEs Core, this session | No |

**Boss is not the first detector of any item in this register.**

---

`CP-SA-80 — HOLD`. Six contradictions are registered and none is resolved. Two require Boss
authority and are carried to `SA19`.

Boss remains the sole Final Approver.
