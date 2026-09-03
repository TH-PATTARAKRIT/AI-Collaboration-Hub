# 23 — ASSET LIFECYCLE STATE MACHINE
**LAYER 2 — AUDIT QUARANTINE**

Answers §28.

## 1. The actual states

Six, and no others. The field is **read-only on the model** — every transition goes
through a method.

| State | Meaning |
|---|---|
| `model` | A template |
| `draft` | Created, not started |
| `open` | Running |
| `paused` | On hold |
| `close` | Closed / disposed |
| `cancelled` | Cancelled, entries reversed |

**States that do NOT exist**, despite being asked for by §28:

| Asked for | Reality |
|---|---|
| Fully Depreciated | **No such state.** The asset stays `open` — `10` §3.2 |
| Modified | Not a state; modification is an operation |
| Sold | Not distinguished from disposed at the asset level. The **journal entry** carries *sale* vs *disposal*, the asset does not |

`FACT VERIFIED`

## 2. Transitions

| From | To | Trigger | Precondition | Schedule effect | GL effect | Audit |
|---|---|---|---|---|---|---|
| `draft` | `open` | Confirm | Board must close to zero; accounts must permit posting | Board computed if absent | **Every unposted entry is posted, including future** | Tracked message with parameters; message on each source bill |
| `draft`/`model` | *(deleted)* | Delete | No posted entries | — | — | Message on the source move |
| `open` | `paused` | Pause | — (**no lock-date check**) | Catch-up entry to the pause date | That entry posted | Chatter message |
| `paused` | `open` | Resume | Resume date must be after the pause date | Paused days accumulated; **schedule shifts and the end date extends** | Rebuild forward | Chatter message |
| `open` | `open` | Re-evaluate | Not before the lock date; no earlier draft entries | Catch-up, reverse future, rebuild | Value increase or decrease entry | Tracked field changes |
| `open`/`paused` | `close` | Dispose or Sell | Not before the lock date; no running child increase (for sale) | Catch-up to the disposal date | Multi-line disposal entry | Chatter message |
| any | `cancelled` | Cancel | — | Drafts deleted; **paused days reset to zero** | **Every posted entry reversed** | Detailed chatter listing every reversed entry with its value |
| `close` | `open` | Reset to running | — | Runs a modify to rebuild if the last line is non-zero | Rebuild | Stored gain reset to zero |
| any | `draft` | Reset to draft | — | — | — | — |
| `close`/`model` | *(archived)* | Archive | **Must be `close` or `model`** | — | — | — |

`FACT VERIFIED` — every row from its transition method.

## 3. Properties worth transferring

1. **The state is never written directly.** Every transition is a method with
   preconditions. Any reimplementation with a writable status field inherits the
   shape and none of the guards (Expert 4, `07`).
2. **Cancel is a genuine reversal, and it says so.** The chatter message names every
   reversed entry with its date, reference and value, and states the net effect on
   both accounts. This is exemplary audit behaviour and should be copied.
3. **Cancel resets the paused-day accumulator**, so a cancelled-and-restarted asset
   does not carry a stale calendar shift.
4. **Closure is not terminal.** Reset-to-running exists and rebuilds the board.

## 4. Gaps for SMEsPlus

| Gap | Consequence |
|---|---|
| No *fully depreciated* state | The condition central to the Boss's post-depreciation design must be **detected**, not observed — `10` §3.2 |
| Sale and disposal not distinguished on the asset | Any report of "assets sold" must go to the journal entries |
| No *under construction* / *not yet in service* state | Capitalisation has no pending stage — `02` §3 item 4 |
| No *transferred* state | No transfer capability at all |
| Pause has no lock-date check | `UNR-09` |
| Confirm has no lock-date check | `UNR-09` |
