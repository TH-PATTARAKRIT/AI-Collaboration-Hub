# SC-BD-09 — BOSS DECISION RECORD — `F8`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-09` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F8` — Idempotency severity |
| **Atomic IDs in family** | one decision — gate severity only |
| **Ruled by this record** | **1 of 1** |
| **NOT ruled — see §8** | none |

## 1. Exact question
Is the absence of a deterministic idempotency identity **gate-blocking**, or a design input a phase may pass with?

## 2. Selected option
> ## `OPTION (b) — DESIGN INPUT, NOT GATE-BLOCKING`

Pre-Test proceeds. The deterministic-identity proof becomes a **Pre-Test / build obligation** rather than a phase-holding blocker.

## 3. Rejected alternatives
**Option (a) — gate-blocking.** Rejected. No phase would close until element 15 is built and `RT-E15-01`…`RT-E15-09` execute; element 15 is the join key, so **every** one of the 22 scenarios would be affected.

## 4. SMEs Core recommendation
**(b) design input, not phase-holding.**

**History Boss was shown, and it cut against the recommendation:** CORR5's first freeze declared this *"dissolved by standing rulings"* and **two challengers independently reversed it**. It was presented as open **precisely because the executing party twice tried to close it**.

## 5. SMT disposition
Cross-Module Integration / Internal Control SMT — dispositioned. **`SC-SMT-03`** asked *who determines when idempotency is required* — if undefined, the protection the recommendation leans on would be **vacuous**. **Closed by existing authority, not by assumption:** `BD-ACC-01`'s sentence is **unqualified**, so for accounting events idempotency is **always** required, the handoff contract §4 condition is always met, and the protection exists one level down **on a stated ground**.

## 6. Affected vetoes
**None discharged.**

## 7. Affected Pre-Test entry state
Not entry-gating. **It sets Pre-Test *exit* criteria** — which is why it was ruled **before** those criteria are agreed.

## 8. Downstream obligations / what this record does NOT rule
1. **Element 15 is specified and not built.** The deterministic-identity proof and `RT-E15-01`…`RT-E15-09` become **Pre-Test exit criteria**, and must be written into them.
2. **Whether idempotency is required is NOT re-openable** — `BD-ACC-01` rules it, and `UAE-29`, the Account programme's root blocker, is thereby ruled. Only severity was ever open, and it is now ruled.
3. Accounting Core owns the canonical event identity.

## 9. Source evidence
`SC-06` `F8` card · `SC-03` (`SC-SMT-03`) · `BD-ACC-01` · `UAE-29` · handoff contract §4

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
