# 06 — DEEP LEVEL 3: FUNCTION FORENSIC
**LAYER 2 — AUDIT QUARANTINE**

Method required by §20: every material function traced
UI → module → model → field → method → rule → calculation → state → database →
journal → analytic → exception → audit trail.

Detailed per-function forensics are in `14`–`25`. This file is the **spine**: the
complete function inventory with its trace status, plus the findings that only
appear when the functions are viewed together.

## 1. Function inventory and trace status

| # | Function | Trigger | State change | GL effect | Analytic | Traced to | Status |
|---|---|---|---|---|---|---|---|
| F01 | Create asset manually | User | → `draft` | none | user-set | model + create | `FACT VERIFIED` |
| F02 | Auto-create from vendor bill | Posting a bill on a flagged account | → `draft` or `open` | none at creation | **inherited from the bill line** | bill-posting hook | `FACT VERIFIED` |
| F03 | Split one bill line into N assets | Account flag + line quantity | N × `draft` | none | inherited | same hook | `FACT VERIFIED` |
| F04 | Apply an Asset Model | Selecting a model | fields copied | none | — | model-onchange | `FACT VERIFIED` |
| F05 | Turn a posted entry into an asset | User action on a move | → `draft` | none | — | move action | `FACT VERIFIED` |
| F06 | **Confirm** | User | `draft` → `open` | **posts the whole board** | per line | confirm method | `FACT VERIFIED` |
| F07 | Compute board | Confirm, or explicit button | — | creates + posts entries | per line | board methods | `FACT VERIFIED` |
| F08 | Post one depreciation | Automatic on the board | — | **Dr expense / Cr accumulated** | on both lines | move preparation | `FACT VERIFIED` |
| F09 | **Re-evaluate upward** | Modify wizard | parent unchanged; **a new child asset is created and confirmed** | Dr asset / Cr counterpart | copied from parent | modify method | `FACT VERIFIED` |
| F10 | **Re-evaluate downward** | Modify wizard | — | a depreciation-type entry flagged as a value change | inherited | modify method | `FACT VERIFIED` |
| F11 | Change duration / accounts / salvage | Modify wizard | — | catch-up entry to the operation date, then rebuild forward | inherited | modify method | `FACT VERIFIED` |
| F12 | **Pause** | Modify wizard | `open` → `paused` | catch-up entry to the pause date, posted | inherited | pause method | `FACT VERIFIED` |
| F13 | **Resume** | Button | `paused` → `open` | rebuild forward | inherited | resume path | `FACT VERIFIED` |
| F14 | **Dispose** (no invoice) | Modify wizard | → `close` | cost out, accumulated out, balance to **loss/gain** | **from the asset** | disposal builder | `FACT VERIFIED` |
| F15 | **Sell** (invoice required) | Modify wizard | → `close` | as F14 plus proceeds | from the asset | disposal builder | `FACT VERIFIED` |
| F16 | **Cancel** | Button | → `cancelled` | **reverses every posted entry**, deletes drafts, resets paused days | reversal inherits | cancel method | `FACT VERIFIED` |
| F17 | Reset to draft | Button | → `draft` | none | — | trivial write | `FACT VERIFIED` |
| F18 | Reset to running | Button | `close` → `open` | runs a modify to rebuild | inherited | reset path | `FACT VERIFIED` |
| F19 | Archive | Checkbox | — | none | — | archive guard | `FACT VERIFIED` |
| F20 | Delete | User | gone | none | — | delete guard | `FACT VERIFIED` |
| F21 | Depreciation Schedule report | Menu | — | — | — | report model | `FACT VERIFIED` |
| F22 | **Equipment status flip on confirm** | F06, custom override | equipment → *To Assets* | none | — | custom override | `FACT VERIFIED` (custom) |
| F23 | **Equipment deactivate on sale** | intended on F15 | — | — | — | custom wizard file | **`CONTRADICTED` — dead code, see `19`** |
| F24 | Transfer / split / merge an existing asset | — | — | — | — | — | `VERIFIED GAP` |
| F25 | Impairment | — | — | — | — | — | `VERIFIED GAP` |
| F26 | Tax-book depreciation | — | — | — | — | — | `VERIFIED GAP` |
| F27 | Sub-ledger ↔ GL reconciliation | — | — | — | — | — | `VERIFIED GAP` — `22` |

**24 functions traced to primary source. 1 contradicted. 4 verified gaps.**

## 2. The canonical journal entry

Every ordinary depreciation posts exactly **two lines**:

```
Dr   Depreciation Expense account          amount
Cr   Accumulated Depreciation account       amount
```

with, on **both** lines: the asset's analytic distribution (only if one exists),
the partner from the source bill (only if there is exactly one), the asset's
currency, and a link back to the asset. The entry date is the **period end**, and
a separate technical field records the **period start**.

`FACT VERIFIED`

Variations found: sign inversion for deferred-revenue-style records; the
value-decrease entry (F10) uses the same shape but is flagged as a value change so
that the board excludes it from cumulative depreciation; the disposal entry (F14/
F15) is the only multi-line asset entry.

## 3. Findings that only appear when functions are viewed together

### 3.1 Confirming an asset posts its entire life immediately

`F06` does not merely change status. It computes the board and then posts **every
line that is not already posted** — including all future periods. Future-dated
entries are created as posted-and-auto-posting rather than left as drafts.

Consequence: **an asset confirmed today writes journal entries dated years into
the future.** Any SMEsPlus period-close, lock-date or reporting design must expect
posted entries beyond the current period. This is not a corner case; it is the
normal path.

`FACT VERIFIED` — confirm method, and the board's post-on-create behaviour.

### 3.2 History is never restated. Every change is a catch-up plus a rebuild.

Every mid-life change — F10, F11, F12, F13 — follows the identical three-step
shape:

1. **Catch up**: post one entry covering the part-period from the last posted
   entry up to the operation date.
2. **Destroy the future**: drafts are deleted; **posted future entries are
   reversed**, not deleted.
3. **Rebuild**: recompute the board forward from the day after the operation.

**No posted entry is ever modified.** This is the single most important
architectural property of the engine for SMEsPlus to inherit, and it answers §29
directly: historical rewrite does **not** occur; future recomputation does.

`FACT VERIFIED`

### 3.3 An upward re-evaluation is not a re-evaluation

`F09` leaves the parent asset's original value, duration and board untouched. It
creates a **new child asset** with its own board, its own entries, and a
`parent_id` pointing at the original. The parent's book value then includes the
child's by recursion.

So "the value of that machine" is a **tree aggregate**, and the number of asset
records grows every time a machine is improved. Consequences for SMEsPlus:

- asset counts are not machine counts;
- any per-machine cost pool must sum a tree, not read a row;
- the child inherits the parent's depreciation **curve** deliberately (the code
  reconstructs the parent's pre-revaluation proportion so the child switches from
  declining to linear at the same moment the parent did).

`FACT VERIFIED`

### 3.4 Pause is calendar-shift, not schedule-freeze — §30 answered

On pause: a catch-up entry is posted to the pause date and the state changes.
On resume: the number of days between the last entry and the resume date, **minus
one**, is added to a running `asset_paused_days` accumulator. Every subsequent
computation uses `prorata_date + paused_days` as its origin.

Therefore:

| §30 question | Answer |
|---|---|
| Does calendar time still advance? | Yes |
| Does the asset's end date extend? | **Yes** — the last day is derived from the shifted origin |
| Does the schedule shift? | Yes, wholesale |
| Does the residual change? | No |
| Does total depreciation change? | No — the same base over a later window |
| Does the GL change? | Only in timing |

The "minus one day" is deliberate: pausing and resuming on the same day produces
zero shift. `FACT VERIFIED`

**Thai implication, flagged not answered:** a pause defers deduction into later
tax years. Whether Thai tax law permits an entity to suspend depreciation on an
asset it still owns is a statutory question. `HOLD / EVIDENCE REQUIRED` → `26`.

### 3.5 Lock dates are respected — but only on three of the five paths

Disposal and re-evaluation both check the fiscal lock date and refuse to operate
before it. **Pause does not perform that check itself**, and neither does confirm.

`FACT VERIFIED` — the guard is present in the disposal and modify paths and absent
from the pause path. Whether the underlying posting layer catches it anyway is
**not established from this module's source**. Recorded as `UNR-09`.

### 3.6 One invariant governs the whole board

A constraint enforces: **for any asset in `open` state, the last depreciation line
must leave a remaining value of exactly zero.** Every function that touches the
board must leave that true, or the transaction is rejected.

This is why F11 and F13 always rebuild rather than patch, and it is the strongest
single guarantee the engine offers. `FACT VERIFIED`

### 3.7 Analytic is inherited once and then frozen — §27 answered in outline

The asset's distribution is computed from its source bill lines, **balance
weighted**, at creation. Thereafter it is a plain stored field. Each depreciation
entry copies the asset's distribution **at the moment the entry is prepared**.

Consequence: changing the distribution changes **future** entries only. Already
posted entries keep the old distribution and are not revisited. Full treatment,
including the multi-dimensional and archived-account cases, in `21`.

`FACT VERIFIED`

## 4. Exception and failure paths found

| Guard | Blocks |
|---|---|
| Board integrity | Confirming or leaving an asset `open` with a non-zero final remaining value |
| Draft source lines | Creating an asset from an unposted bill |
| Mixed accounts | Source lines from more than one account |
| Zero / offsetting value | Source lines netting to zero |
| Source change after start | Adding or removing bills once running or closed |
| Delete | Deleting anything not `draft`/`model`, or anything with posted entries |
| Archive | Archiving anything not `close`/`model` |
| Draft asset, posted entry | Posting an entry against a `draft` asset |
| Reset to draft | Resetting a move that has a non-draft asset |
| Lock date | Disposal and re-evaluation before the lock date |
| Unposted priors | Re-evaluating while earlier draft depreciations exist |
| Same-account | Selecting the depreciation account as the gain or loss account |
| Running gross increase | Selling a parent that still has a running child |

`FACT VERIFIED` — thirteen distinct guards.

## 5. Four Expert opinions

See `07_LEVEL3_FOUR_EXPERT_OPINIONS.md`.
