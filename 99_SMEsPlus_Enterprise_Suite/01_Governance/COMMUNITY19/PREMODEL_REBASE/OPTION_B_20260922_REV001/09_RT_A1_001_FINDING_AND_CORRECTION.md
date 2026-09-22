# RT-A1-001 — A1 Output Shape Versus Frozen Question Model

Severity: `HIGH`
Status after this package: `CORRECTION CONTRACT CREATED / OLD LINEAGE HELD`

## Finding

S1/S2 generated source-unit dispositions, candidate functions, rules, scenarios and gaps, but no `MODULE + QID` join key. They cannot be compared cell-to-cell against the frozen question universe and cannot enter A2 reconciliation directly.

## Correction

- adopt Option B;
- preserve S1/S2 as pre-model evidence;
- create the 47-row authoring/control crosswalk;
- bind new A1/A2 contracts to frozen W1-STD and W1-B01;
- require 105 exact answer rows for `base`;
- prohibit old-lineage A2 dispatch.

Closure condition: an independent reviewer confirms this package, then a fresh corrected A1 package validates and seals. Until then `RT-A1-001` remains open at execution level.
