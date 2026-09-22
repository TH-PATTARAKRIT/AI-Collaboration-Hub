# Corrected A2 Blind Contract — MODULE + QID

1. A2 receives the same frozen question identities and no A1 answer content before its blind package is sealed.
2. A2 uses a distinct session, context, scratch space, writer key and output directory.
3. A2 produces exactly 105 unique `base + QID` answer rows with the same mandatory fields and answer-status vocabulary.
4. A2 records its own evidence and does not infer that A1 is correct.
5. Only after A2 blind seal may the Controller release both manifests to the reconciliation phase.
6. Reconciliation classifies each QID as `MATCH`, `SEMANTIC-MATCH`, `CONFLICT`, `A1-ONLY`, `A2-ONLY`, `BOTH-NOT-OBSERVED`, or `CONTROL-DEFECT`.
7. A2 cannot close its own material CRQs or approve the batch.
