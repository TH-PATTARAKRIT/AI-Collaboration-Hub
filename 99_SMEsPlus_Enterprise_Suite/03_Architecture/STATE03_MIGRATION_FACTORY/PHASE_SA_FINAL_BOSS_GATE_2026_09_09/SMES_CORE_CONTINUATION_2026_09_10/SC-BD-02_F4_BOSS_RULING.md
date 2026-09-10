# SC-BD-02 — BOSS DECISION RECORD — `F4`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-02` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F4` — Cross-module contract scope and supply binding |
| **Atomic IDs in family** | `XMC-D-02`, `C2-D-01` |
| **Ruled by this record** | **2 of 2** — `XMC-D-02`, `C2-D-01` |
| **NOT ruled — see §8** | none |

## 1. Exact question
Does the Boss-approved 16-element handoff contract govern **every** cross-module boundary or only Inventory → Accounting (`XMC-D-02`)? And when a manufacturing shortage raises supply, is the fulfiller hard- or soft-bound (`C2-D-01`)?

## 2. Selected option
> ## `XMC-D-02 = EXTEND TO ALL BOUNDARIES · C2-D-01 = SOFT BINDING CONFIRMED`

One **general** contract with **declared per-boundary applicability** — not twelve bespoke contracts and not verbatim extension. The boundary denominator moves **1 → 12**.

**Binding condition carried into the ruling (`SC-SMT-08`):** an applicability declaration is **part of the contract amendment and carries the contract's authority**. **A boundary may propose; it may not declare.** Without this a boundary could exempt itself from the elements it found inconvenient.

## 3. Rejected alternatives
**Keep at Inventory → Accounting only** — would leave eleven mandated handoffs uncontracted; `XMC-C-D2` holds that a rule with no carrier is not a rule. **Split (extend, hold `C2-D-01`)** — not taken; both were ruled together.

## 4. SMEs Core recommendation
**EXTEND**, on the finding that **13 of the 16 elements are domain-general**; only unit of measure, product/lot/serial and warehouse/location are stock-shaped, and the contract already handles that with its `N/A`-plus-reason rule. The contract's *content* is domain-general; only its approved *scope* was domain-specific, and **no deliberate architecture rationale for that limitation was found**. `C2-D-01` → confirm the soft binding the target design already states and grades `FACT VERIFIED`.

## 5. SMT disposition
Cross-Module Integration SMT — dispositioned. `SC-SMT-08` accepted and closed in-session (the applicability-authority condition above). `SC-SMT-09` quantified the magnitude: **1 boundary → 12**, with attestation obligations `HF-CTX-06` / `HF-CTX-11` scaling accordingly.

## 6. Affected vetoes
**None discharged.** No veto turns on `F4`.

## 7. Affected Pre-Test entry state
**Entry-gating decision `XMC-D-02` is now RULED.** The Pre-Test Matrix element-contract denominator is fixed at **12 boundaries**, declared as a set. Building over 12 from the start is an increment, not a later re-scope.

## 8. Downstream obligations / what this record does NOT rule
1. The contract amendment must carry the **per-boundary applicability declaration** with contract-level authority.
2. Attestation obligations `HF-CTX-06` / `HF-CTX-11` extend to 12 boundaries.
3. **`C2-D-01`'s shortage-exit half was a defect, not an election** — SMEs Core specified a supply-raised exit; that specification stands and is not a Boss item.
4. **`E2E-04` is NOT re-graded `TRAVERSABLE` by this ruling.** A prior round attempted that and withdrew it under challenge; the re-grade is held for the independent reviewer.

## 9. Source evidence
`SC-06` `F4` card · `SC-01` §6.2 (`C2-D-01` shortage-exit specification) · `SC-05` §2.3 (entry denominator) · `SC-03` (`SC-SMT-08`, `SC-SMT-09`)

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
