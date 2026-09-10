# SC-BD-08 — BOSS DECISION RECORD — `F3`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-08` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F3` — Direct shipment (supplier → customer) |
| **Atomic IDs in family** | `XMC-D-01` (conditional); `C2-D-02` already closed |
| **Ruled by this record** | **1 of 1** — the conditional decision is resolved and **leaves the Boss list** |
| **NOT ruled — see §8** | none |

## 1. Exact question
Does `BD-ACC-03A`'s Product-Category valuation authority reach a route with **no internal end**?

## 2. Selected option
> ## `OPTION (a) — APPLY BD-ACC-03A AS RULED, WITH NO ROUTE-SPECIFIC EXCEPTION`

The movement chain emits valuation facts under the product category's ruled policy. **No route-specific exception class is created.** `F3` **leaves the Boss decision list entirely**.

## 3. Rejected alternatives
**Option (b) — state that `BD-ACC-03A` does not reach this route.** Rejected. It was the only branch requiring a Boss **act**, and it would have given SMEsPlus a route-shaped exception to a Product-Category-authored policy, with every future route lacking an internal end raising the same question again.

## 4. SMEs Core recommendation
**Option (a).** **The asymmetry Boss was shown:** option (a) **requires nothing of Boss** — it applies `BD-ACC-03A` as ruled; only option (b) required a Boss statement. Under `CF-D-01` (*"only Boss may state what a Boss ruling covers"*) SMEs Core did **not** make that statement, and the argument that a *route* may not override the ruling **was available and deliberately not used**.

## 5. SMT disposition
Inventory SMT — **`PASS WITH CONDITION`**; Cross-Module Integration SMT — **`PASS`** on `C2-D-02`.

**`SC-SMT-04`** required option (a) to specify the **location semantics** of a movement with no internal end. **Closed in-session:** the location context is the **counterparty pair** — supplier origin and customer destination — recorded as **external endpoints with reason**, not `N/A`.

## 6. Affected vetoes
**None discharged.**

## 7. Affected Pre-Test entry state
Not entry-gating. **No exception class exists to build or test**, so the direct-shipment path adds no Pre-Test surface beyond the ordinary route.

## 8. Downstream obligations / what this record does NOT rule
1. **Location semantics are fixed as the counterparty pair**, recorded as external endpoints **with reason**.
2. **`C2-D-02` remains CLOSED** — cost binds to the same canonical Accounting Event Identity as the revenue (`XMC-C-C6` + `BD-ACC-01`), verified by `SC-SMT-10`. Its remaining variable is the **date**, which is `F1`'s and was **not asked twice**.
3. **Published weakness, carried forward not suppressed:** *"resolves the movement chain"* does not by itself exclude resolving to a **zero-length** chain (`SC-02` §6.1). This is a specification item for Functional Design, not a Boss decision.
4. **The evidence basis is recorded:** the reference's direct-shipment capability is installed in **0 of 3** readable deployments, measured on two differently-shaped instruments. Every direct-shipment fact in the corpus is source-derived from a capability no deployment runs — `SOURCE IS EVIDENCE, NOT DESIGN`.

## 9. Source evidence
`SC-06` `F3` card · `SC-02` (bounded verification, and §6.1 the published weakness) · `SC-03` (`SC-SMT-04`, `SC-SMT-10`) · `BD-ACC-03A`, `BD-ACC-01`, `XMC-C-C6`, `CF-D-01`

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
