# U9002 — Fixture order lifecycle (neutral knowledge, intentionally invalid)

SYNTHETIC GATE FIXTURE — planted leaks and a missing RISK section.

## Order lifecycle

### WHAT
- The `action_confirm` method in fixture_order.py on fixmod.models moves the order. [N-U9002-001]

### WHY
- Draft first. [N-U9002-001]

### BUSINESS RULE
- See fixmod/models/fixture_order.py:13 for the rule; Odoo behaves the same. [N-U9002-001]

### STATE
- Draft, confirmed, cancelled. [N-U9002-001]

### OPTIONALITY
- None. [N-U9002-001]

### DEPENDENCY
- None. [N-U9002-001]

### CONSTRAINT
- None. [N-U9002-001]

### UNKNOWN
- None. [N-U9002-001]
