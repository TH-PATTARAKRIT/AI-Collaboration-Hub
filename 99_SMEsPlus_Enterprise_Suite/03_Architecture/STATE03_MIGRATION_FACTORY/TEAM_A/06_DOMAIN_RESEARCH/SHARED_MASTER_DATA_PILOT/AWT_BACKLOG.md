> Domain: SHARED_MASTER_DATA_PILOT | AWT Backlog | Not executable in this container

# AWT BACKLOG

### SMD-F04 — Access Rights/Groups × Multi-Company Record Rule interaction (highest priority in this pilot; documentation pass complete 2026-09-29)

- **Criticality**: C1
- **Hypothesis to verify**: a user's effective access to a model is the intersection, not just the union, of (a) their Groups' model-level grant and (b) any applicable Multi-Company Record Rule's row-level filter — i.e., a Group grant does not bypass company-scoping, and company-scoping does not itself grant model-level access absent a Group.
- **Documentation-tier resolution (`GAP-SMD-04`, `EV-SMD-05`)**: confirmed — the two layers compose as global (no-group) rules AND-combined as a hard floor, group-carrying rules OR-combined among themselves; Multi-Company rules are typically global, so they act as an unconditional filter no Group can bypass. This matches the hypothesis's intersection framing.
- **Required environment**: an authorized Odoo 19 environment with at least two companies, two Groups with differing model access, and one user in a non-default company.
- **Runtime action**: attempt CRUD operations across the Group/company combinations and observe allow/deny outcomes.
- **Expected observable result**: access denied whenever either axis alone would deny it (true intersection), not just whichever axis is checked first.
- **Evidence required**: exact allow/deny outcome per Group/company combination tested.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: full runtime confirmation only — this pilot's documentation-tier characterization of each axis independently, and of their composition rule, is now complete; only live-environment confirmation remains.

### SMD-F01/F02/F03

Carry-forward from `GROUP_01_SALES_INVENTORY_PURCHASE` — that track's own AWT/runtime posture (if any) applies; not duplicated here.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 1 (SMD-F04)
FUNCTIONS CARRIED FORWARD (no new AWT plan from this pilot) : 3 (SMD-F01/F02/F03)
```
