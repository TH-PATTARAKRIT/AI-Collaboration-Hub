# VDR_CONFIGURATION_CONSEQUENCE_MATRIX.md
# Configuration consequence — and the retraction of the grade that claimed it

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 03.

---

## 1. The retraction that has to come first

PREP-004 published `CONFIGURATION 17.31%` on the rule *"an element is verified when its gate has all
nine axes determined."* An independent challenger demolished it:

> **The gates themselves are graded NOT research-verified — all 44 of them — while the 702 elements
> they govern were graded verified by inheriting their state.** And the same document declared, in its
> own limitations section, that *"which state each gate is actually in on each deployment"* is not
> determinable. **The inherited thing was undetermined.**

The challenger's verdict was RETRACTION REQUIRED, and it is accepted in full.
**`CONFIGURATION` returns to 0.00% research-verified.**

> **The governing rule adopted from this round on:** a dimension is research-verified only when an
> instrument **outside the register** established it *for that item*, and that instrument has a control
> that can fail. Inheriting a determination made about something else is not evidence about the item.

## 2. What IS established — and it is substantial

The retraction is of a **grade**, not of the research. All of the following stands, from source, with
its controls:

| | |
|---|---|
| Gates governing register elements | **42** — corrected from the 48 published in PREP-003, by two independent shapes that agree |
| Gates including switch-only | **49**, all covered |
| Kind split | **20 role gates · 29 capability gates** |
| Gates with a settings switch | **26 of 49** |
| Coverage | **49 of 49** resolved to a declaration with file and line; 11,874 declarative files parsed, 0 failures |

### The nine axes, determined for all 49

menu **CHANGES 30/49** · button 28 · **field 45** · action 9 (+52 contextual server actions) ·
workflow 30 · **automation NO CHANGE for all 49** · model/data: **schema NO CHANGE for all 49**, records
change for 7 · stock/accounting 6 · **security CHANGES for 21, and it WIDENS in every case measured** ·
cross-module 48 of 49.

## 3. The consequences that matter

### `CC5-F-01` — the field axis carries two mechanisms and only one is a control
View-level gating hides. **Field-level access control is enforced by the object layer on every channel
including remote calls and import — and only 12 gates use it.**

The on-hand valuation field is access-controlled to a manager role. **The analytic distribution field is
not**: turning analytic accounting off hides it in the interface and **leaves the write path fully open
to remote calls and import**. Off is not an integrity control.

### `CC5-F-02` — 67 declarations invert the gate
**Turning those gates ON removes interface, it does not only add it.** Any off-vs-on test that looks
only for elements appearing misses all 67.

### `CC5-F-03` — the switch that does not revoke, now confirmed at runtime
The switch machinery adds and removes an *implication* on the holder group and **never touches a user's
own group list**. Confirmed against three deployments' membership tables: **8, 7 and 6 gates
respectively are held by direct membership that no holder group implies.** Most are role groups where
that is intended; **the sharp cases are two capability gates on the transacted deployment** — the
settings page reads them OFF while they are live.

### `CC5-F-04` — an administrator's OFF decision is reversed by an unrelated module upgrade
Seven modules grant a gate to every internal user through install data, and **two are marked to
re-apply on every upgrade**. Demonstration-only grants were separated by parsing each module's manifest.

### `CC5-F-05` — a toggle whose OFF and ON are not inverses
One gate's OFF path archives **every** routing operation; its ON path restores only those sharing the
most recent modification timestamp. **A single operation archived afterwards redefines that maximum, and
ON then restores one operation and leaves the library archived.**

### `CC5-F-06` — two settings branches fire on every unrelated save
Both mass-write records whenever their box is unchecked, with **no before/after comparison** — one
resets a flag across bills of material, the other **re-archives every price list**. A third writes data
from a form-level handler, so the change lands whether or not the record is saved.

### `CC5-F-07` — the largest interface gate is not a security control
Every internal user is already a member; the framework treats it as a display flag and its own comment
says so. **56 elements whose only protection is this gate are protected by nothing.**

## 4. Runtime corroboration — necessary, not sufficient

Tested across five deployments: is a gate's presence necessary for its elements to be present, and is it
sufficient?

| Question | Result |
|----------|--------|
| Necessary? | **no counter-example** — 0 of 26 discriminable gates have elements present where the gate is absent |
| Sufficient? | **no — 4 gates are present where their gated elements are absent** |

**A gate installs nothing. It ships with the module that declares it and controls visibility over what
is already installed.**

## 5. Why the dimension is 0.00% and what would move it

The nine axes are determined **per gate**. §7 of this round requires the consequence to be proven **per
function**, across twenty configuration classes — global, company, tenant, role, product, warehouse,
operation type, route, rule, accounting, valuation, security, module, state, data condition, scheduler,
lead time, reporting, feature interaction, and default-versus-overridden.

**Per-gate is established. Per-function is not, and the two are not the same claim.** Moving this
dimension needs the gate consequence joined to each governed element's own behaviour — which is now
possible for the first time, because the process dimension has an instrument.

**Stated plainly: `CONFIGURATION` is 0.00% research-verified and roughly 100% determined. The previous
17.31% was the second of those figures wearing the first one's label.**
