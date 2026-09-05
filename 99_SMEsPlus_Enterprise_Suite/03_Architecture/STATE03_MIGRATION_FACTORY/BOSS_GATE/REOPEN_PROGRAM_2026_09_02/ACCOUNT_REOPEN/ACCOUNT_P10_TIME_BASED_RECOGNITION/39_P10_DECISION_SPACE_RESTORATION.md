# P10 — DECISION SPACE RESTORATION

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D02`.

**Every option eliminated solely because `T0-13` was treated as resolved is restored here.**

---

## 1. What Was Eliminated, and On What Authority

| Eliminated | Where | Sole ground | Authority |
|-----------|-------|-------------|-----------|
| **Option A — permit the silent re-date (status quo)** | `28` revision 1 §4 | *"not among the options that satisfy `T0-13` … a consequence of a boundary two peers have already adopted"* | **NONE.** `T0-13` is `HOLD — BOSS DECISION REQUIRED` |

No other option was eliminated. Options B, C and D were carried; E and F were **not yet discovered**, which is a completeness defect and not an elimination.

## 2. Restoration

> **Option A is RESTORED to the decision space, unconditionally.**

It is restored not because P10 favours it — P10 does not — but because **P10 had no authority to remove it**, and because the only ground offered for removing it is an open Boss decision.

Its standing is now stated correctly:

> Option A is **conditionally excluded**: it is excluded **if and only if** the Boss adopts `T0-13`. Until that ruling, it is a live option with evidence for and against, like every other.

## 3. The Restored Option Set — full statement

Six options, each with the fields the directive requires.

### `OPT-A` — permit the silent re-date (status quo)

| Field | Content |
|-------|---------|
| Description | A posting constraint may move an entry's date; the recognition period is not recorded and the movement is not traced |
| Evidence for | The product's specified behaviour, recorded by an executed test on the asset mechanism. Never blocks a close. No change to any layer |
| Evidence against | The amount is misstated by period while every total remains correct, so no reconciliation detects it. The landing period is selected by the journal's **sequence numbering format** — a year-reset sequence lands at 31 December, a month-reset at that month's end. A convention whose answer changes with a numbering format is not a convention |
| Dependency | None |
| **`T0-13` dependency** | **TOTAL.** Excluded if and only if the Boss adopts `T0-13` |
| Accounting consequence | Period allocation misstated; totals correct |
| Period consequence | Recognition period silently replaced by a posting date |
| Scope consequence | COMPANY-scoped financial effect altered without record |
| Audit consequence | No trace. The mutation is undetectable after the fact |

### `OPT-B` — refuse

| Field | Content |
|-------|---------|
| Description | An entry that cannot post into its own period is rejected |
| Evidence for | Precedent exists and is tested: asset disposal hard-refuses, grouped generation refuses. Satisfies the **lock-triggered** half of `T0-13` |
| Evidence against | **Insufficient on its own under the refined close condition.** A second mutation path fires with **no lock configured**, so there is nothing to refuse and refusal cannot reach it. Converts a silent misstatement into a visible failure at close |
| Dependency | None technical |
| `T0-13` dependency | Partial — satisfies half the refined condition |
| Accounting consequence | No misstatement on the lock path; the lock-free path is untouched |
| Period consequence | Preserved where a lock exists |
| Scope consequence | COMPANY |
| Audit consequence | The refusal is the record |

### `OPT-C` — permit, and record an attributable trace

| Field | Content |
|-------|---------|
| Description | Entry posts at the permissible date; the recognition period is recorded and the divergence is reportable |
| Evidence for | Satisfies the refined close condition on **both** paths, because a trace does not require a violation to exist |
| Evidence against | A queryable period field does not exist in the ledger, so the strong form needs a ledger change |
| Dependency | `OB-02` on the ledger owner for the strong form |
| `T0-13` dependency | Satisfies it |
| Accounting consequence | Period truth preserved and reportable |
| Period consequence | Recognition period survives the posting date |
| Scope consequence | COMPANY |
| Audit consequence | Full |

### `OPT-D` — separate the concepts entirely

| Field | Content |
|-------|---------|
| Description | Recognition event carries its period; posting act carries its date; independent by construction |
| Evidence for | Removes the defect class rather than the instance, on both paths |
| Evidence against | Largest change; cannot be scoped before the accounting-event identity exists |
| Dependency | Boss `D-5` |
| `T0-13` dependency | Satisfies it |
| Accounting / period / scope / audit | As `OPT-C`, structurally rather than by convention |

### `OPT-E` — post at the true date under a recorded lock exception  *(restored by discovery, not by authority)*

| Field | Content |
|-------|---------|
| Description | A shipped first-class exception object records company, user, reason, validity window and the original lock date; an active exception suppresses the violation so the entry posts **at its own date** |
| Evidence for | **No period object and no ledger change required.** The exception itself is the attributable trace. Present in the two newer deployed databases |
| Evidence against | The irreversible hard lock is **not** exception-able. The object is **absent from the older estate line**, so this is unavailable on part of the estate. Reaches only the lock path |
| Dependency | Estate line |
| `T0-13` dependency | Satisfies the lock half; **does not reach the lock-free path** |
| Audit consequence | Strong — a named user and a stated reason |

### `OPT-F` — post the divergence as a chatter trace  *(restored by discovery)*

| Field | Content |
|-------|---------|
| Description | Record the original period as a message on the entry, as the adjacent branch of the same routine already does for a deferred accounting date |
| Evidence for | Costs nothing another process owns. **Proves the silence is a choice, not a limitation.** Reaches both paths |
| Evidence against | Not queryable; weaker than `OPT-C` |
| `T0-13` dependency | Satisfies the refined condition in its weakest admissible form |

## 4. Option Adequacy Against the **Refined** Close Condition

The refined condition: *where a mutation path has no violation to detect, an attributable trace is mandatory, not alternative.*

| Option | Lock-triggered path | Lock-free path | Adequate under the refined condition **if adopted**? |
|--------|--------------------|----------------|------------------------------------------------------|
| `OPT-A` | no | no | No |
| `OPT-B` | yes | **no — nothing to refuse** | **No** |
| `OPT-C` | yes | yes | Yes |
| `OPT-D` | yes | yes | Yes |
| `OPT-E` | yes | **no** | No, alone |
| `OPT-F` | yes | yes | Yes, weakest form |
| `OPT-B` + `OPT-F` | yes | yes | Yes |
| `OPT-E` + `OPT-F` | yes | yes | Yes |

**This table is conditional throughout.** It states what would follow **if** the Boss adopts `T0-13`. It eliminates nothing.

**Material consequence of the refinement:** P10's earlier reading, that `T0-13` admitted two alternatives and that refusal was one of them, is superseded. Under the refined condition **refusal alone is not a complete answer**, and any combination that satisfies the boundary must include a trace.

## 5. What P10 Recommends — and what it does not do

P10 **recommends** `OPT-C`, or `OPT-B`+`OPT-F` as a cheaper equivalent, and records that `OPT-E` is worth taking regardless because it costs nothing and improves the lock path immediately.

P10 **does not** eliminate `OPT-A`, does not rank the adequate options, and does not decide `T0-13`. All of that is `BOSS DECISION REQUIRED AT FINAL GATE`.
