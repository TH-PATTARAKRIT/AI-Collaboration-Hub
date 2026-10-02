# U9001 — Fixture order lifecycle (known-valid gate fixture)

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

- Unit: U9001 (SYNTHETIC GATE FIXTURE — NOT RESEARCH EVIDENCE)
- Modules: fixmod (synthetic, `tools/vdr_gate_fixtures/source`)
- Source revision: git index blob of the fixture source file
- Status label: SYNTHETIC GATE FIXTURE — expected candidate verdict PASS

## CAP-U9001-01 Fixture order lifecycle

Function-ID: FIX-F01. State list: draft -> confirmed [confirm]; draft|confirmed -> cancelled [cancel].

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U9001-C001 | FIX-F01 | fixmod/models/fixture_order.py:6 | `STATES = (` | FACT | always | — | The order declares three states: draft, confirmed, cancelled. | N-U9001-001 |
| VDR-U9001-C002 | FIX-F01 | fixmod/models/fixture_order.py:9 | self.state = "draft" | FACT | always | — | A new order starts in draft. | N-U9001-002 |
| VDR-U9001-C003 | FIX-F01 | fixmod/models/fixture_order.py:12 | def action_confirm | FACT | always | — | Confirmation is guarded by a draft-state check. | N-U9001-003 |
| VDR-U9001-C004 | FIX-F01 | fixmod/models/fixture_order.py:13 | Only draft orders can be confirmed | FACT | always | — | Confirming a non-draft order raises an error. | N-U9001-003 |
| VDR-U9001-C005 | FIX-F01 | fixmod/models/fixture_order.py:18 | Order already cancelled | FACT | always | — | Cancelling an already cancelled order raises an error. | N-U9001-004 |
| VDR-U9001-C006 | FIX-F01 | fixmod/models/fixture_order.py:19 | self.state = "cancelled" | INFERENCE | always | — | Lines 17-19: cancellation is reachable from draft and confirmed. | N-U9001-005 |
| VDR-U9001-C007 | FUNCTION MAPPING REQUIRED | fixmod/models/fixture_order.py:14 | self.state = "confirmed" | FACT | always | RT | Confirmation sets the confirmed state; persistence needs runtime proof. | N-U9001-006 |
| VDR-U9001-C008 | FIX-F01 | — | — | UNKNOWN | always | RT | Concurrency behaviour is not stated by the source. | N-U9001-007 |
