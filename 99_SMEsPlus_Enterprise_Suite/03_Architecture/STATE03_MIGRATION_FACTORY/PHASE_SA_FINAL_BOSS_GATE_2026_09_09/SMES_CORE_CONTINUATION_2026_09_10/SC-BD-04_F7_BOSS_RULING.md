# SC-BD-04 — BOSS DECISION RECORD — `F7`

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head at ruling `e113258f` · Gate prompt `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md`
**Boss decision ID `SC-BD-04` · 2026-09-10 · Boss is the SOLE FINAL APPROVER.**

| | |
|---|---|
| **Family** | `F7` — Authorization axis and configurable-record scope |
| **Atomic IDs in family** | `RC-D-01`, `RC-D-02`, `CF-D-01`, `CF-D-02` |
| **Ruled by this record** | **4 of 4**, by confirmation of the registers as they stand |
| **NOT ruled — see §8** | none — but see §8 on the basis of the confirmation |

## 1. Exact question
Is `location` an authorization axis (`RC-D-01`)? What closes the configurable-record enumeration (`RC-D-02`)? Is `MTI-D-03`'s *"Unit of Measure Category"* the same object as the context matrix's *"Unit group and unit"* (`CF-D-01`)? What closes the platform-owned operation-class enumeration (`CF-D-02`)?

## 2. Selected option
> ## `CONFIRM THE REGISTERS AS THEY STAND · location IS NOT AN AUTHORIZATION AXIS`

The registers stand as written. The **denial enumeration is 3 axes — Company, Warehouse, Operation-Type**, as ruled by `MTI-D-02`. **`location` is not among them.** `S-01`…`S-08` enumerate over that ruled set.

## 3. Rejected alternatives
**Rule `location` IN as a 4th axis** — rejected. Had it been taken, the **positive complement inverts**: cases asserting access-allowed-across-locations become denials, and the negative-access suite would be re-enumerated over 4 axes before Pre-Test. **Rule `RC-D-01` only, hold the enumerations** — not taken.

## 4. SMEs Core recommendation
**As the registers state; no new position originated.** `CF-D-01`'s ground is decisive and general: *"only Boss may state what a Boss ruling covers."*

## 5. SMT disposition
Internal Control / Audit SMT — **`BOSS-ONLY DECISION`**. `SC-SMT-07` required the denominator to be stated in **both halves**, because declaring only the denial half is the wrong-denominator class this programme has recorded repeatedly.

## 6. Affected vetoes
**None discharged.** No veto turns on `F7`.

## 7. Affected Pre-Test entry state
**Entry-gating decision `RC-D-01` is now RULED.** The negative-access suite's axis set is fixed at **3 axes**, declared in both halves — denial enumeration and positive complement. The complement **does not invert**.

## 8. Downstream obligations / what this record does NOT rule
1. `S-01`…`S-08` enumerate over the 3-axis ruled set; the positive complement is fixed.
2. **Basis of the confirmation, stated so it is visible and correctable:** `RC-D-01` was ruled on its own explicit terms. **`RC-D-02`, `CF-D-01` and `CF-D-02` are ruled by family-level confirmation of the registers, not by a bespoke election on each.** If Boss intended a narrower ruling covering `RC-D-01` alone, this record is the place to correct it, and the three enumeration closures return to `OPEN`.
3. A reading that made `RC-D-01` non-entry-gating **did not survive its own test and remains withdrawn** (`SC-05` §1.1).

## 9. Source evidence
`SC-06` `F7` card · `SC-05` §2.3 (denominator in both halves) and §1.1 (withdrawn reading) · `SC-03` (`SC-SMT-07`) · `MTI-D-02` (the 3 ruled axes)

## 10. Authority
> Boss is the **SOLE FINAL APPROVER**. This records a ruling Boss made; it is not a SMEs Core decision,
> not a `PASS`, not a Phase SA closure and not a Pre-Test authorisation. **Phase SA is NOT closed.**
> **No veto is discharged by this record.** No structural independence is claimed.
