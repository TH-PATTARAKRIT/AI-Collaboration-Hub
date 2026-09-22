# Pipeline Transition Control — Corrected QID Lineage

```text
PRE-MODEL S1/S2
  -> preserve + external seal
  -> GMVQ authoring/control input only
  -> never A2

FROZEN W1-STD + W1-B01
  -> Corrected A1 fresh answer package (105 rows)
  -> Controller validation + valid SHA-256 manifest
  -> A1-QID-SEALED
  -> A2 blind fresh answer package (105 rows)
  -> A2-BLIND-SEALED
  -> A2 reconciliation
  -> A3 adversarial challenge
  -> MASTER candidate reconciliation
  -> Boss-controlled one-way release gate
```

Hard gates:

- no unresolved placeholder;
- all bank/freeze hashes match;
- exact row count and unique MODULE+QID set equality;
- evidence IDs resolve;
- no source-specific expression in clean handoff fields;
- no old S1/S2 evidence IDs used as answer evidence;
- manifest verifies and inventory equals;
- A2 context independence attested.
