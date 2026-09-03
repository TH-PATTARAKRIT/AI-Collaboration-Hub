# 24 — ASSET MODIFICATION RESEARCH
**LAYER 2 — AUDIT QUARANTINE**

Answers §29. One wizard implements five different accounting events (`04` §4
`UI-06`), so this deliverable separates them.

## 1. The five actions

| Action | Available when | What it is, accounting-wise |
|---|---|---|
| **Re-evaluate** | always | A change in estimate, a capital addition, or a write-down — depending on direction |
| **Pause** | running | A deferral of the schedule |
| **Resume** | paused only (and it is then the *only* option offered) | Restart with a shifted calendar |
| **Dispose** | always | Derecognition without proceeds |
| **Sell** | always, but requires a posted customer invoice | Derecognition with proceeds |

## 2. The universal shape

Every action except pure re-evaluation-with-no-change performs the same three steps
(`06` §3.2):

1. **Catch up** — one entry covering the part-period up to the operation date,
   computed on the same engine.
2. **Destroy the future** — drafts deleted, posted future entries **reversed**.
3. **Rebuild** — recompute forward from the day after the operation.

**No posted entry is ever modified.** `FACT VERIFIED`

## 3. What each change actually does

### 3.1 Increase value

The wizard compares the asset's book value **at the operation date** with the
requested new depreciable + non-depreciable amounts. The increase is decomposed:

```
residual_increase = max(0, requested_depreciable − allowable_new_depreciable)
salvage_increase  = max(0, requested_salvage    − allowable_new_salvage)
```

If the total increase is positive, the wizard:

1. posts `Dr gross-increase asset account / Cr counterpart account`;
2. creates a **new child asset** for the increase, dated the day after the
   operation, inheriting method, duration, period and computation mode, with the
   revaluation entry's asset line as its source;
3. **confirms that child immediately**, which posts its whole board.

The **parent is not restated**. `FACT VERIFIED`

The child's depreciation deliberately follows the parent's **curve**: for
declining-then-linear assets the code reconstructs the parent's pre-revaluation
proportion so that the child switches from declining to linear at the same moment
the parent did, and scales by the ratio of the two lifetimes.

### 3.2 Decrease value

Posts a single entry in the canonical depreciation shape, flagged as a **value
change** and typed *negative revaluation*. Because it is flagged, the board excludes
it from cumulative depreciation, and future straight-line amounts are reduced by
spreading the decrease over the remaining life:

```
reduction per period = period days × decrease ÷ (lifetime days − days already elapsed at the decrease)
```

`FACT VERIFIED`

### 3.3 Change duration or period length

Written straight to the asset, then catch-up and rebuild. Because the engine is
cumulative-difference, the rebuilt schedule uses a **restated total-lifetime-left**
basis rather than the original one, so the remaining value is spread over the new
remaining life without disturbing history.

**Children are cascaded**: any child assets receive the same duration, period and
paused-days values, are caught up, rebuilt, checked and posted.

`FACT VERIFIED`

### 3.4 Change residual

See `18` §4. Bounded and asymmetric; an increase beyond the available book value
becomes a child asset.

### 3.5 Change method

Permitted. Applies to the rebuild only, so the historical curve stays as it was and
the future takes the new shape. **No warning, no disclosure prompt.**

Expert 1's Level 6 challenge stands: this is a change in accounting estimate that
would normally require disclosure, and the system permits it silently.
`D6-02`

### 3.6 Change accounts or journal

Written to the asset. **Prior entries keep the old accounts.** The asset's account
triple stops describing its own history — `FAIL-X09`, and one of the three ways to
break sub-ledger/GL agreement (`22` §7).

### 3.7 Change the asset model

There is **no such action**. The model field is a plain link and changing it does
not re-apply anything — `14` §5.

## 4. Guards

| Guard | Effect |
|---|---|
| Lock date | Cannot re-evaluate before it |
| Earlier drafts | Cannot re-evaluate while unposted earlier depreciations exist |
| Gain/loss account | Cannot be the same as the depreciation account |
| Running child increase | Cannot **sell** a parent with a running child; must dispose of the child first |
| Resume ordering | Cannot resume on or before the pause date |
| Board invariant | The rebuilt board must close to zero |

`FACT VERIFIED`

## 5. Audit trail

Four tracked fields — duration, period, depreciable value, non-depreciable value —
produce a chatter entry with before/after values and the user's note.

**Not tracked:** method, computation mode, accounts, journal, analytic distribution.

So a change of **computation mode** — the field that switches between 30/360 and
calendar days, the most consequential field on the asset (`16` §3) — **leaves no
audit trail at all.**

`FACT VERIFIED`. For a Thai-compliance-sensitive deployment this is a material
control weakness, and it is a cheap fix in SMEsPlus.

## 6. Answers to §29

| Question | Answer |
|---|---|
| Historical rewrite? | **Never** |
| Future recomputation? | **Always** |
| New asset component? | **Yes, for upward revaluation** |
| New journal entry? | Catch-up always; plus a revaluation entry when value changes |
| Audit trail? | **Partial** — four fields tracked, the critical ones not |
