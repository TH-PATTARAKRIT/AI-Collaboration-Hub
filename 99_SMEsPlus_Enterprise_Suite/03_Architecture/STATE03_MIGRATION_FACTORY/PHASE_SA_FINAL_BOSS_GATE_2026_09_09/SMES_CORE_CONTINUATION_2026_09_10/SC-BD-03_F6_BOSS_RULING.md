# SC-BD-03 — BOSS DECISION RECORD — `F6`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-03` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F6` — Cross-company visibility and commercial scope |
| **Atomic IDs in family** | `MTI-D-04`, `RC-D-03`, `RC-D-04`, `TV6-BOSS-02` |
| **Ruled by this record** | **2 of 4** — `MTI-D-04`, `TV6-BOSS-02` |
| **NOT ruled — see §8** | **`RC-D-03`, `RC-D-04`** — no SMEs Core recommendation existed for either, so neither was put to Boss |

## 1. Exact question
Does a sanctioned cross-company **read** exist inside a tenant at all (`MTI-D-04`); who owns the mapping layer (`RC-D-04`); what escalates a tenant to the Private Company model (`RC-D-03`); and is a product's base sell price a tenant fact or a company fact (`TV6-BOSS-02`)?

## 2. Selected option
> ## `MTI-D-04 = NO CROSS-COMPANY GRANT IN v1 · TV6-BOSS-02 = COMPANY-SCOPED`

No sanctioned cross-company read grant exists in v1. The group-view need is met by **per-company export**, which becomes the **designed** answer rather than the informal one. A product's base sell price is a **company** fact.

## 3. Rejected alternatives
**Permit a sanctioned cross-company read** — rejected. `SC-SMT-05` recorded that on any grant-permitting branch `MTA-11` finds **every grant mechanism degrades toward permanence** and **no review cadence is designed anywhere**, so ruling a grant would rule an **undesigned review obligation** into existence. **Rule the two entry-gating members only** — not taken as a narrower option; the ruling matches it in effect because no recommendation existed for the other two.

## 4. SMEs Core recommendation
`MTI-D-04` → **no grant in v1**; `TV6-BOSS-02` → **company-scoped**. **No recommendation was offered for `RC-D-03` or `RC-D-04`.**

**Recorded counter-argument, weighed:** *"Not deciding is not neutral — the need gets met by export, which is the worst outcome."* Under this ruling export becomes the **designed** route rather than the informal one.

## 5. SMT disposition
SaaS / Multi-Company SMT — dispositioned. `SC-SMT-05` surfaced the grant-permanence consequence as a **consequence of an existing decision, not a new decision**.

## 6. Affected vetoes
**No veto is discharged by this record.** Two are **materially affected**, and both discharges belong to AAS+ with Boss ratification:

- **`AAS-V-03`** — its COGS limb becomes **vacuous** on this branch. **Vacuous is not discharged.** AAS+ must still act.
- **`CF-V-02`** — its **first limb** is closed by this ruling. The veto itself is **not** lifted.

**Vetoes remain 6 in force / 0 discharged / 0 self-discharged.**

## 7. Affected Pre-Test entry state
**Entry-gating decision `MTI-D-04` is now RULED.** `CF3-P-04` is **struck**, so the isolation suite's exception set is **empty and known** rather than unknown. `XCR-02` and `CF-XCR-GAP-01` are settled by the same ruling.

## 8. Downstream obligations / what this record does NOT rule
1. **Per-company export becomes a designed deliverable**, not an informal workaround.
2. **`RC-D-03` and `RC-D-04` remain OPEN Boss decisions.** No recommendation exists for either — `SC-01` lists them only as family members on the management-information side of `BD-ACC-02`. **SMEs Core owes a recommendation on both before they are re-put to Boss**, and they must not be treated as ruled.
3. AAS+ must act on `AAS-V-03` and on `CF-V-02`'s remaining limb; Boss ratifies.
4. **`BD-ACC-02` is not re-opened, re-interpreted or re-asked.** All four members sit on the management-information side of the line Boss already drew; `0 of 4` re-ask closed statutory scope.

## 9. Source evidence
`SC-06` `F6` card · `SC-01` §F6 member table (lines 317–321 — `RC-D-03` / `RC-D-04` carry no recommendation) · `SC-05` §2.3 · `SC-04` veto register · `SC-03` (`SC-SMT-05`)

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
