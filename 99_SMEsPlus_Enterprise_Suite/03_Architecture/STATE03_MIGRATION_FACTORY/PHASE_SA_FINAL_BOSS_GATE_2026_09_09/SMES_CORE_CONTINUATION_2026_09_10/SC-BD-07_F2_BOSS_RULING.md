# SC-BD-07 — BOSS DECISION RECORD — `F2`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-07` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F2` — Commercial control-default policy |
| **Atomic IDs in family** | three members, incl. `XD1-P1` |
| **Ruled by this record** | **3 of 3**, as one principle |
| **NOT ruled — see §8** | none |

## 1. Exact question
When a commercial control fires and the business has not configured a preference, does SMEsPlus default to `block`, `warn-and-allow`, or `allow-silently`?

## 2. Selected option
> ## `BLOCK — ON ALL THREE MEMBERS, RULED ONCE AS A PRINCIPLE`

The default is **`block`**. Friction lands on the user at the moment of the breach; sell-side exposure and stock truth are protected by default; a tenant needing looser behaviour configures it.

## 3. Rejected alternatives
**`warn-and-allow` as one principle** — friction would land on whoever later reconciles the recorded owed-conditions; nothing would be silently lost, because `M-1`/`M-6` forbid silence. **Split the ruling across the three members** — rejected; CORR3 had kept them separate so as not to conflate separately-evidenced elections, and Boss ruled them as one principle instead.

## 4. SMEs Core recommendation
**`block`** on all three, ruled once as a principle.

## 5. SMT disposition
Internal Control / Audit SMT — **`PASS WITH CONDITION`** on the mechanism; **`BOSS-ONLY DECISION`** on the default.

**The mechanism is specified, so the election carried no unspecified consequence.** Six invariants bind on **every** branch: every firing emits an event; an allowed breach records a **non-dismissible** owed-condition carrying who/when/basis; the override is Company-scoped and the default platform-owned; no override may lower a control **floor**; the audit record has the **same shape** on both branches; and **`M-6` — the event's *emission* is not configurable, only the control's *outcome* is.**

**`M-6` was added by SMT challenge `SC-SMT-06`.** Without it a configuration could suppress the event and turn `warn-and-allow` into `allow-silently` **without anyone electing it** — the defect shape this programme has already measured once.

## 6. Affected vetoes
**None discharged.**

## 7. Affected Pre-Test entry state
Not entry-gating. The six invariants `M-1`…`M-6` become Pre-Test assertions on **both** branches, and the ruled branch fixes the expected outcome.

## 8. Downstream obligations / what this record does NOT rule
1. `M-1`…`M-6` are binding design invariants and must be carried into Functional Design and Pre-Test as assertions.
2. **`M-6` is load-bearing** — emission is not configurable. Any later configuration surface that could suppress a control event contradicts this ruling.
3. The override path stays **Company-scoped** with the default **platform-owned**, and **no override may lower a control floor**.

## 9. Source evidence
`SC-06` `F2` card · `SC-01` §5 (the six invariants) · `SC-03` (`SC-SMT-06`) · `SC-05` §2.1 item 4

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
