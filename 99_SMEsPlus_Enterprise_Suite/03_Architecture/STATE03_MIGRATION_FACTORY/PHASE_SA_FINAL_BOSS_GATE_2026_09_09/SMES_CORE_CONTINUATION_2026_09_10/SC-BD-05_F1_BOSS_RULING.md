# SC-BD-05 — BOSS DECISION RECORD — `F1`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-05` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F1` — COGS recognition and reversal basis |
| **Atomic IDs in family** | `JT-04`, `JT-05` |
| **Ruled by this record** | **2 of 2** — `JT-04`, `JT-05` |
| **NOT ruled — see §8** | none |

## 1. Exact question
Which event recognises cost of sales — the physical movement or the customer invoice (`JT-04`) — and does a return reverse at original or current cost (`JT-05`)?

## 2. Selected option
> ## `JT-04 = THE BUSINESS EVENT (PHYSICAL MOVEMENT) · JT-05 = ORIGINAL COST`

Cost of sales is recognised on the **physical movement**, with `Perpetual` and `Periodic` **defined wherever the terms appear**. A return reverses at **original cost**.

Recognition and posting separate cleanly; the handoff contract already carries both dates (elements 3 and 4), so the audit trail is date-complete.

## 3. Rejected alternatives
**Invoice + original cost** — cost would follow the commercial document, and a delivery without an invoice would carry no cost until invoiced. **Movement + current cost** — would avoid the `Average`-costing residual at the cost of a reversal that does not match the original posting. **Hold pending the Thai statutory input** — rejected; holding would leave 10 of 22 scenarios at `expected value pending` and force costing rework after Functional Design.

## 4. SMEs Core recommendation
`JT-04` → movement; `JT-05` → original cost. **This was a SMEs Core *position*, not a prior Boss ruling** — `SC-01` §4.3 measured the claim that an approved direction already binds COGS to delivery and found **it does not exist**: every hit is a commissioning prompt, a scope bullet or a glossary entry.

## 5. SMT disposition
Accounting / Thai Accounting-Tax SMT — **`BOSS-ONLY DECISION`, with two conditions accepted**:

- **`SC-SMT-01`** — under **`Average`** costing, original-cost reversal **leaves a residual that nothing in the recommendation places**. `09_JT05` §5 assigns that reconciliation-control design to **Boss** at primary text. **Now named rather than latent.**
- **`SC-SMT-02`** — whether **TAS 2** constrains the trigger is **untested**; carried as an explicit **`HOLD / EVIDENCE REQUIRED`**.

## 6. Affected vetoes
**None discharged.** `AAS-V-03`'s COGS limb interacts with `F1`: on the `F6` branch ruled at `SC-BD-03` that limb is **vacuous**, so `F1` does not revive it. **Vacuous is not discharged.**

## 7. Affected Pre-Test entry state
Not entry-gating. **It fixes expected values:** the 10 of 22 scenarios carrying `expected value pending` can now be valued on the movement basis.

## 8. Downstream obligations / what this record does NOT rule
1. **`SC-SMT-01` is a live obligation, not a closed condition.** The `Average`-costing reversal residual needs a **reconciliation-control design**, and `09_JT05` §5 assigns it to **Boss**. It is **not** discharged by this ruling and must be tracked.
2. **`SC-SMT-02` remains `HOLD / EVIDENCE REQUIRED`** — no TAS 2 claim is made anywhere by this ruling.
3. The recognition role sits inside the immutable identity basis, so this ruling is a **prerequisite of costing design**, not an input to be revisited during it.

## 9. Source evidence
`SC-06` `F1` card · `SC-01` §4.3 (the measured non-existence of a prior binding direction) · `08_JT04` §5 · `09_JT05` §5 · `SC-03` (`SC-SMT-01`, `SC-SMT-02`)

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
