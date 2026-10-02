# U9001 — Fixture order lifecycle (neutral knowledge)

SYNTHETIC GATE FIXTURE — NOT RESEARCH EVIDENCE

## Order lifecycle

### WHAT
- An order moves through three states: draft, confirmed and cancelled. [N-U9001-001]

### WHY
- A new order starts as a draft so it can be reviewed before commitment. [N-U9001-002]

### BUSINESS RULE
- Only a draft order may be confirmed; any other order is refused with an error. [N-U9001-003]

### STATE
- An order that is already cancelled cannot be cancelled again. [N-U9001-004]

### OPTIONALITY
- Cancellation is available both before and after confirmation. [N-U9001-005]

### DEPENDENCY
- Confirmation records the confirmed state; lasting storage must be shown at runtime. [N-U9001-006]

### CONSTRAINT
- No further constraint is stated. [N-U9001-003]

### RISK
- Behaviour under simultaneous changes is unknown. [N-U9001-007]

### UNKNOWN
- Concurrency handling is not determined from the source. [N-U9001-007]
