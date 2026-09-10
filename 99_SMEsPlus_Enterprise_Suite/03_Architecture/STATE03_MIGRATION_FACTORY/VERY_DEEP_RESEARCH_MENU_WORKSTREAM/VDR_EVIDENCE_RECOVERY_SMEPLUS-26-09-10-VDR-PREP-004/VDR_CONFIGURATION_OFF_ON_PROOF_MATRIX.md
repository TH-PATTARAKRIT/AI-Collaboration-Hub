# VDR_CONFIGURATION_OFF_ON_PROOF_MATRIX.md
# CONFIG OFF vs CONFIG ON — nine axes, every gate, source and runtime

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 06.

---

## 1. The unit, and a correction to the denominator

**The unit is the gate, not the element.** Elements inherit a gate's state; only a gate has an OFF and
an ON. Two independent shapes over the frozen register — a parsed read and a raw-text read — agree:

> **42 gates govern register elements, not the 48 published in PREP-003.** A further **7** exist only as
> settings switches governing no register element, giving **49** under the widest defensible reading.
> **All 49 are covered here.** The element counts (709 gated, 237 switches, 946 total) reconcile exactly;
> only the gate count was wrong.

The register's own gate list was re-derived independently in this round and returned **42**, matching.
`48` is corrected wherever it appears.

**Kind split: 20 role gates, 29 capability gates. 26 have a settings switch; 23 have none.**

## 2. Instrument and controls

| Control | Result |
|---------|--------|
| Gate resolution | **49 of 49** resolved to a declaration with file and line |
| Positive control, **corpus-drawn** | for all **709 of 709** register rows marked as gated, an independent scanner re-found the same gate in the same file. **0 misses** — and the inputs were the register's own pointers, not the searcher's vocabulary |
| Axis-scan coverage | 11,874 declarative files parsed, **0 parse failures**; 16,208 code files; 8,640 gate references classified; **49 of 49** gates carry at least one hit |
| Second shape, menu axis | a structural walk and an independent block extractor agree on 45 of 49; **all 4 deltas explained and reconciled to zero residual.** A naïve single-line text search was **rejected** — it under-counts badly because declarations wrap across lines |
| **Self-caught instrument defect** | a parse error on the settings-binding reader produced a clean, plausible **"0 of 42 gates have a switch."** Caught by disbelief at a round zero, fixed, re-run → **26 of 49**. *A silent failure that satisfied its own output format* |
| **Second self-caught defect** | the first group index, keyed naively, collapsed 279 records into 188 — **losing 91 extension records, every one of them an implication edge.** Uncaught, it would have hidden almost all of §5 |

## 3. The nine axes — determinations across all 49 gates

| # | Axis | Result |
|---|------|--------|
| 1 | **menu** | **CHANGES for 30 of 49**; determined NO CHANGE for 19 |
| 2 | **button** | CHANGES for 28 of 49 |
| 3 | **field** | **CHANGES for 45 of 49** — and by *two* mechanisms of different strength (§4) |
| 4 | **action** | CHANGES for 9, plus 52 contextual server actions across 12 gates |
| 5 | **workflow / state** | CHANGES for 30 of 49, via role checks in business logic |
| 6 | **automation** | **NO CHANGE for all 49 — a determination, hard-won** (§4) |
| 7 | **model / data** | **schema: NO CHANGE for all 49.** Constraints: no change for the 26 switch-driven gates. **Records: CHANGES for 7 gates** — the material ones |
| 8 | **stock / accounting** | **CHANGES for 6 gates**; presentation-only for the rest |
| 9 | **security** | **CHANGES for 21 of 49, and it WIDENS in every case measured.** No gate was found that narrows access by being granted |
| + | **cross-module handoff** | CHANGES for 48 of 49 — only three stay inside one module |

## 4. Three axis results that carry the weight

### `CF4-F-01` — the automation determination, and why it counts as one
*No gate changes any scheduled behaviour.* This is the axis most easily faked by a silent zero, so it
was attacked rather than accepted: 204 scheduled-job records parsed across 134 files (**0** reference a
gate, with the reader validated — 203 of the same 204 carry a model reference, so it fires); the jobs'
**method bodies** resolved and parsed, 196 of 209 located (93.8%), **0** reference a gate;
settings-driven job toggling shown to exist elsewhere in the corpus but **for no gate in this
population**; automated-rule records referencing a gate: 0.
**Declared limitation: reachability below the top-level job method is untraced.**

### `CF4-F-02` — the field axis hides two mechanisms, and only one is a control
- **View-level gating** is presentation. Hiding only.
- **Field-level access control** is enforced by the object layer on **every channel including remote calls and import**. **12 gates use it.**

**Materially:** the on-hand valuation field is access-controlled to the stock-manager role —
**inventory valuation is unreadable to an ordinary inventory user by enforced access control, not merely
hidden.** By contrast, the analytic gate governs 40 view fields but the analytic distribution field
itself carries **no access control**: **turning analytic accounting OFF hides the field while leaving
the write path fully open to remote calls and import. OFF is not an integrity control.**

### `CF4-F-03` — 67 references invert the gate
**67 declarations render an element only when a gate is OFF**, across 12 gates. **Turning those gates ON
removes user interface, it does not only add it.** Any OFF-vs-ON test plan that looks only for elements
appearing will miss every one of them.

## 5. Irreversibility — eight findings, and the first is the most consequential

### `CF4-F-04` — **OFF never revokes a direct assignment**
The switch machinery adds and removes an *implication* on the holder group. It **never touches a user's
own group list.** A corpus-wide sweep for group→user revocation — with its predicate validated against
the corresponding grant form — found **exactly one** site that clears user membership, for a single
gate.

> **For the other 48 gates, a user explicitly granted the capability keeps it after the switch is turned
> OFF — and the settings page reads OFF, because it only inspects the holder group.** The interface
> says the feature is off; for those users it is live.

### `CF4-F-05` — a warehouse creation silently turns two gates ON, and a deletion reverts only one
Creating a second warehouse **executes a settings save from inside record creation**, forcing the
multi-location gate ON and linking both it and the multi-warehouse gate to every internal user.
Dropping back to one warehouse removes **only** the multi-warehouse gate. **Multi-location is never
auto-reverted — and it cannot be turned off manually while more than one warehouse exists.** The user's
only warning is a form-level toast.

### `CF4-F-06` — a toggle whose OFF and ON are not inverses
The routing gate's OFF path archives **every** routing operation. Its ON path restores only those
sharing the single most recent modification timestamp. **One operation archived by a user after the mass
archive redefines that maximum — and ON then restores that one operation and leaves the entire routing
library archived.** Destructive and non-idempotent.

### `CF4-F-07` — two settings branches fire on every unrelated save
Two paths mass-write records whenever their box is unchecked, **with no before/after comparison**: one
resets a flag on all matching bills of material, the other **re-archives every price list**. Every save
of an unrelated setting on the same page re-applies them, silently undoing anything changed by remote
call since the last save. The only defence is a warning string that does not block and does not run on
remote writes.

### `CF4-F-08` — a data write inside a form-level handler
One gate mass-writes a lock flag across all open production orders from an **on-change handler** — so
the data change lands when the checkbox is toggled in the form, **whether or not the settings record is
ever saved, and even if the dialog is discarded.**

### `CF4-F-09` — an administrator's OFF decision is silently reversed by a module upgrade
Seven modules grant a gate to every internal user through install data; **two of them are marked to
re-apply on every upgrade.** An administrator who turns units-of-measure or product-variants OFF has
that decision **silently reversed by the next upgrade of an unrelated module**, with no log entry and no
settings interaction. Demonstration-only grants were separated from these by parsing each module's own
manifest — they do not fire on a production install.

### `CF4-F-10` — hard blocks, and one that cannot be deleted
Two gates refuse to turn off rather than mutate: lot tracking while any tracked product exists,
multi-location while more than one warehouse exists. And a gate bound to a settings field **cannot be
deleted at all** — the object layer refuses.

### `CF4-F-11` — a currency action mutates a product gate and creates master data
Activating a second currency applies the price-list gate to every internal user and **creates price-list
records**. A currency decision changes product configuration.

## 6. Silent widening — the implication graph

197 implication edges were extracted from **279** group records — 188 named plus **91 extension records
written by other modules**, the set the first index silently lost.

**Six edges widen access across application boundaries without any settings interaction:**

| Edge | Consequence |
|------|-------------|
| inventory user ⟹ quality user | installing quality grants **every inventory user** the quality role — retroactively, and again on every upgrade |
| manufacturing user ⟹ quality user | the same, for every manufacturing user |
| point-of-sale manager ⟹ inventory user | a POS administrator silently holds inventory rights — 68 access rows |
| helpdesk user ⟹ a timesheet capability | installing a bridge module widens the base role |
| sales manager ⟹ website editor | |
| salesperson ⟹ an event-desk capability | |

**And one subtractive edge**, the only one in the corpus: two modules write **opposite** implication
edges on the same pair, so **the resulting state depends on install order.** Recorded as a
load-order-dependent fact, not resolved by source.

### `CF4-F-12` — the largest gate in the domain is not a security control

One gate governs **56 register elements** and is the largest interface gate measured — 137 menus, 364
fields, 164 blocks, 55 buttons, across 199 modules. **Every internal user is already in it by
declaration.** The framework then discards it from the user's group set unless a debug flag is set, and
rewrites it in views into a private display attribute. **The source's own comment says it should not be
considered a security group.**

> **CONFIG OFF vs CONFIG ON for this gate is a per-session debug toggle, not stored configuration, and
> it is not enforced server-side. Any element whose only protection is this gate is protected by
> nothing** — including the 55 technical-only elements PREP-003 reported as concealed, and the object at
> the centre of `CRITICAL-GAP-06`.

## 8. Runtime corroboration — five deployments

The source result was tested against the deployments' own registries, asking whether a gate's presence
changes whether its gated elements are **present**:

| Question | Result |
|----------|--------|
| Is a gate **necessary** for its elements to be present? | **No case found against it** — 0 of 26 discriminable gates have elements present where the gate is absent |
| Is a gate **sufficient**? | **No — 4 gates are present on deployments where their gated elements are absent** |

**Conclusion, from runtime: a gate does not install anything. It ships with the module that declares it
and controls visibility over what is already installed.** This corroborates the source finding that no
gate changes schema, and it corroborates `CF4-F-02`'s distinction: presence is a module question,
*access* is a gate question.

## 9. Grade effect

`CONFIGURATION` rises from **7 (0.17%) to 709 (17.31%)** — the 702 gated elements whose gate now has all
nine axes determined, plus the 7 settings already traced end to end. **The 237 settings that are
themselves switches remain not-verified: 26 of 49 have their OFF/ON traced, not all of them**, and the
3,156 elements with no gate at all have no OFF/ON state to trace.

## 10. Not determinable from source — eight declared limitations

Automation reachability below the top-level job method · 13 of 209 job methods unresolvable to a
definition · the debug gate's live state in any deployment · **which state each gate is actually in on
each deployment** (the group-implication and membership tables were not extracted this round) · the
load-order outcome of the subtractive edge · whether the upgrade re-grant actually fires, which needs a
controlled install-toggle-upgrade cycle · client-side gating not separated by axis · 8 gates that appear
in the register's detail column but never in its condition column.

**Each is a bounded measurement with a named instrument. None is a Boss question.**
