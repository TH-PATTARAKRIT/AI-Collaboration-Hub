# 06_RC06_P11_CHALLENGE

RC: `RC-06` · Owner: P11 · Frozen surface: `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
Dependency: RC-05 balance premise independently executed over four frozen DB dumps.
Result: **`RC-FAIL — MATERIAL DEFECT FOUND`**

## What survives
`Q-P11-04` correctly:
- withdraws the old `F-02` counterexample based on `1e-7 = 3`;
- states the correct answer to the falsification question is NO;
- re-states `CI-01` as zero at every tested tolerance including exact equality;
- strikes the rule `A soundness claim without a tolerance is not a claim`;
- explicitly marks that rule **WITHDRAWN, not re-grounded**.

The P08 notification predates P11's first correction commit and is received/attributed correctly after `CO-F-02`.

## Material findings
### RC06-F1 — withdrawn tolerance rule survives as live reconvergence wording
`P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md`, axis 9, still says:
`Arithmetic sound at a declared tolerance (F-02)`.

That is the practical policy residue of the rule the same file has just withdrawn. The independently reproduced balance result is zero **at exact equality and every tested tolerance**; this instance does not support a requirement that soundness be stated only “at a declared tolerance”.

Required correction: mark the old wording superseded and restate the axis without re-grounding the withdrawn rule.

### RC06-F2 — P11 still carries the three-DB P08 premise
P11's Q-P11-04 correction and `CI-01` lineage consume the P08 three-DB result (`DB-SM`, `DB-BK`, `DB-EV`). RC-05 now independently establishes the same balance result on the fourth frozen dump DB-T2. P11 must not close Phase S on the stale three-DB premise.

Required correction: after P08 publishes its bounded RC-05 correction at a new immutable SHA, re-point P11's balance premise to that owner evidence and preserve the three-DB result as superseded lineage.

## Gate impact
RC-06 cannot pass until the two bounded propagation residues are corrected and fresh-challenged. No re-derivation of P08 balances by P11 is authorized.