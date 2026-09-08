# 02_RC02_P11_CHALLENGE

RC: `RC-02` · Owner: P11 · Frozen surface: `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
Result: **`RC-PASS — BOUNDED SURFACE SURVIVES INDEPENDENT CHALLENGE`**

## Q-P11-01 pin-honouring challenge
`intake_derivations_pinned.py` was independently re-executed.

Frozen result:
- D1 = **56**
- D2 = **48**
- D3 = **157**
- UNION = **214**
- D1∩D2 = **19**; D1\D2 = **37**; D2\D1 = **29**

Falsification controls:
- P09 pin changed from `4778792` to earlier substantive `acf58d2`: output changed to `54 / 48 / 154 / 211`; the pin is actually consumed.
- P09 pin changed to prompt commit `92de8a1`: instrument exits fail-closed with `NON-SUBSTANTIVE under P11-G-10`.
- Published floating and pin-honoured unions both have cardinality **214** but differ in identity by one-out/one-in. This reproduces the stated lesson that equal cardinality is insufficient.

## Q-P11-02 namespace challenge
Across the bounded live CORR3 surface after excluding declared lineage/different-namespace carriers:
- **23** producer-qualified P08 `HO-` citations across **6** files;
- **0** bare live `HO-13` / `HO-14` citations;
- P06's separate family remains `HO-01…HO-06`; P08 owns `P08-HO-13/-14`.

## Q-P11-03 B-38 challenge
At the declared substantive P09 pin `4778792`, the stale “unexecuted L1-L8” limb is struck as superseded; `AAS+-VETO-04` remains undischarged; unlock is re-pointed to M-1/M-2. No P11 self-discharge was found.

## Scope limit
This RC certifies **only Q-P11-01/02/03 repairs**. It does **not** certify P11's intake instrument as a whole, does not close `B-35`, and does not override P11's `TERMINAL B` package state.