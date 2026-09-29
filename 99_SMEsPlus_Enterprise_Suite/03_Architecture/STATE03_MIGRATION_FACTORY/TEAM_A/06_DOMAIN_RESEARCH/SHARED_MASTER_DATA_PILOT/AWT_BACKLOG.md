> Domain: SHARED_MASTER_DATA_PILOT | AWT Backlog | Not executable in this container

# AWT BACKLOG

### SMD-F04 — Access Rights/Groups × Multi-Company Record Rule interaction (highest priority in this pilot)

- **Criticality**: C1
- **Hypothesis to verify**: a user's effective access to a model is the intersection, not just the union, of (a) their Groups' model-level grant and (b) any applicable Multi-Company Record Rule's row-level filter — i.e., a Group grant does not bypass company-scoping, and company-scoping does not itself grant model-level access absent a Group.
- **Required environment**: an authorized Odoo 19 environment with at least two companies, two Groups with differing model access, and one user in a non-default company.
- **Runtime action**: attempt CRUD operations across the Group/company combinations and observe allow/deny outcomes.
- **Expected observable result**: access denied whenever either axis alone would deny it (true intersection), not just whichever axis is checked first.
- **Evidence required**: exact allow/deny outcome per Group/company combination tested.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: full runtime confirmation only — this pilot's documentation-tier characterization of each axis independently is complete; their joint interaction is not evidenced by either this pilot or the Carry-forward reference track.

### SMD-F01/F02/F03

Carry-forward from `GROUP_01_SALES_INVENTORY_PURCHASE` — that track's own AWT/runtime posture (if any) applies; not duplicated here.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 1 (SMD-F04)
FUNCTIONS CARRIED FORWARD (no new AWT plan from this pilot) : 3 (SMD-F01/F02/F03)
```
