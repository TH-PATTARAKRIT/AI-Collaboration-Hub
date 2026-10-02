# U9002 — Fixture order lifecycle (intentionally-invalid gate fixture)

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

- Unit: U9002 (SYNTHETIC GATE FIXTURE — NOT RESEARCH EVIDENCE)
- Status label: SYNTHETIC GATE FIXTURE — expected candidate verdict FAIL
- Planted defects: wrong anchor, missing source file, bad class, missing neutral ref,
  invented Function-ID, line beyond end of file, 8-column row, duplicate Claim-ID.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U9002-C001 | FIX-F01 | fixmod/models/fixture_order.py:6 | def action_ship | FACT | always | — | Wrong anchor: not within 3 lines. | N-U9002-001 |
| VDR-U9002-C002 | FIX-F01 | fixmod/models/missing_file.py:3 | anything | FACT | always | — | Pointer to a file that does not exist. | N-U9002-001 |
| VDR-U9002-C003 | FIX-F01 | fixmod/models/fixture_order.py:9 | self.state = "draft" | GUESS | always | — | Class outside the allowed set. | N-U9002-001 |
| VDR-U9002-C004 | FIX-F01 | fixmod/models/fixture_order.py:9 | self.state = "draft" | FACT | always | — | Neutral reference absent from neutral file. | N-U9002-099 |
| VDR-U9002-C005 | FIX-F99 | fixmod/models/fixture_order.py:9 | self.state = "draft" | FACT | always | — | Invented Function-ID. | N-U9002-001 |
| VDR-U9002-C006 | FIX-F01 | fixmod/models/fixture_order.py:999 | anything | FACT | always | — | Line beyond end of file. | N-U9002-001 |
| VDR-U9002-C007 | FIX-F01 | fixmod/models/fixture_order.py:9 | self.state = "draft" | FACT | always | — | N-U9002-001 |
| VDR-U9002-C001 | FIX-F01 | fixmod/models/fixture_order.py:9 | self.state = "draft" | FACT | always | — | Duplicate Claim-ID. | N-U9002-001 |
