# 04_MENU_FUNCTION_DEEP_RESEARCH_REGISTER.md
# Register 04 — Menu / Function Deep Research (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. Honest scope statement

This Pilot's purpose is to **stress-test the Framework**, and its measured output is the
**function population**, not the researched function. This register therefore records what exists to
be researched and at what state each class stands. **It does not claim function coverage.**

Stating this plainly is itself a Framework requirement: the failure this prevents is a register that
looks populated and is read downstream as "researched".

---

## 2. Function population

| Function-bearing class | Count | Research state | What deep research must still establish |
|------------------------|------:|----------------|------------------------------------------|
| User-invocable controls (`BUTTON`) | 431 | `S1 SOURCE LOCATED` | what each does, its preconditions, its failure mode, its reversal |
| Behavioural overrides & validations (`BEHAVIOUR`) | 614 | `S1` | which are business rules vs plumbing; which can refuse; which mutate silently |
| Actions (`ACTION`) | 200 | `S1` | default filters and contexts, and what population each really shows |
| Views (`VIEW`) | 492 | `S1` | field-level editability by state and role; empty/warning/error states |
| Constraints (`CONSTRAINT`) | 32 | `S1` | the business rule each expresses and its user-visible message |
| Scheduled behaviour (`AUTOMATION`) | 26 | `S1`; a separate 8-item side-effect population is at `S4` | see Register 08 |
| **Total function-bearing Learning Items** | **1,795** | | |

### Control-type distribution (431 controls)

| Type | Count | Meaning |
|------|------:|---------|
| method invocation | 345 | runs code on the record |
| action invocation | 31 | opens another screen |
| **type not declared** | **53** | **defaults at runtime — the control's kind is not statically knowable** |
| domain-specific | 2 | specialised event control |

### FN-F-01 — 12.3% of user-invocable controls do not declare their own type
12.3% of user-invocable controls do not declare their own type. A control
inventory built from static declarations cannot say what 53 of 431 controls do without reading code.

---

## 3. Behavioural taxonomy (1,097 declarations)

| Kind | Count | Why it matters to a clean-room design |
|------|------:|----------------------------------------|
| dependency declarations | 483 | the recomputation graph — what changes when what changes |
| UI-invoked methods | 360 | the actual verbs of the domain |
| **create / write / delete / copy overrides** | **141** | **persistence is not neutral: 141 places intercept it** |
| onchange handlers | 54 | form-time behaviour with no server guarantee |
| validation constraints | 40 | the enforced business rules |
| deletion guards | 15 | what refuses to be deleted, and when |
| scheduled entry points | 4 | |

### FN-F-02 — Persistence is intercepted in 141 places (**CRITICAL**)
**141 persistence overrides** exist on 86 objects. Any SMEsPlus design
that assumes "saving a record stores a record" is inheriting an assumption the reference system does
not hold. Each of the 141 is a candidate hidden business rule and must be classified — *business rule*
vs *technical plumbing* — before Functional Design, because only the first class carries into SMEsPlus.

---

## 4. State transitions

14 objects in the Inventory domain carry an explicit lifecycle state. The complete transition
vocabularies were extracted:

| Object class | Distinct declared states |
|--------------|--------------------------|
| Movement document | 6 — new · waiting-other · waiting · ready · done · cancelled |
| Movement line | **NOT LITERAL — derived from the parent at runtime** |
| Individual movement | 7 — new · waiting-other · waiting · partially-available · available · done · cancelled |
| Batch/wave document | 4 — draft · in-progress · done · cancelled |
| Write-off document | 2 — draft · done |
| Landed-cost document | 3 — draft · posted · cancelled |
| Production document | 6 — draft · confirmed · in-progress · to-close · done · cancelled |
| Work step | 5 — blocked · to-do · in-progress · finished · cancelled |
| Teardown document | 2 — draft · done |
| Repair document | 5 — draft · confirmed · under-repair · repaired · cancelled |
| Forecast/report projections | 3 each — analytical, not lifecycle |

### FN-F-03 — One lifecycle state is not owned by the object that displays it
One lifecycle state is **not a literal** — it is derived from its parent
document at runtime. **A state machine transcribed from declarations would give that object a state it
does not independently own.** This is a design-relevant distinction (who owns the transition) and it
is invisible to any register built from declared selections.

### FN-F-04 — RESOLVED — Two documents are absolutely terminal once completed (**CRITICAL**)
The write-off and teardown documents declare **two** states — `draft` and `done` — and **no cancelled
state**. The first draft of this finding recorded reversibility as *unknown*. It is now established,
and the answer is stronger than "unknown":

| Remedy | Available? | Evidence |
|--------|-----------|----------|
| Cancel the document | **No** — no cancelled state exists | state declaration |
| Reverse the document | **No** — no reverse, undo or cancel method exists on either object | full method census of both objects |
| Delete the document | **No** — a deletion guard on both objects refuses deletion once the state is `done` | deletion-guard method on each object |

**A completed write-off or teardown is irreversible, uncancellable and undeletable.** The only remedy
available to a user is a **compensating entry** — a second, independent document in the opposite
direction.

Two consequences for SMEsPlus, and they pull in opposite directions:
- **Favourable:** this is genuine immutability, achieved by construction rather than by policy, on two
  objects that move stock and value.
- **Unfavourable:** the audit trail records the error permanently and shows **two events where the
  business had one mistake**. Reconciliation, valuation and reporting must all be designed for that.

Whether SMEsPlus adopts terminal-plus-compensation or reversal-with-linkage is `BOSS-DEC-11`.

**Method note:** the deletion guard is invisible to an access-grant census. Register 07 `SS-F-04`
counts 59 of 176 grants as permitting deletion; **at least two of those grants are overridden by a
code-level guard.** An access-rights model derived from grants alone overstates what can be deleted.

---

## 5. Coverage state

| Research state | Items | Share of 5,074 |
|----------------|------:|---------------:|
| `S1 SOURCE LOCATED` | 4,256 | 83.9% |
| `S3 CONFIG VERIFIED` | 755 | 14.9% |
| `S4 FUNCTION VERIFIED` | **63** | **1.24%** |
| `S5`–`S9` | 0 | 0% |

The 63 at `S4`: **46** row-level rules read in full · **9** menu entry methods traced (`SR-10`,
challenge `B-04`) · **7** toggle effect surfaces resolved (`SR-08`) · **2** documents' reversibility
established (`SR-09`) — with the 14 lifecycle-state vocabularies counted under their objects rather
than separately, after challenge finding `C-11` showed the earlier numerator mixed units with its
own denominator.

**This is the Pilot's central number and it is not a failure — it is the correctly-measured distance
between "we have a population" and "we have knowledge".** Prior programme rounds have reported high
coverage against denominators that were author-chosen. This one reports **1.24%** against a
denominator that was derived by rule, instrument-validated, published as a set, and then **attacked by
three independent reviewers who wrote their own instruments and corrected it eleven times.**

> The figure went **up** after challenge — 0.46% → 1.24% — because the challenge closed gaps as well as
> opening them. A correction round is not a penalty phase.
