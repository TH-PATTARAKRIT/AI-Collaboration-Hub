> Domain: SHARED_MASTER_DATA_PILOT | AWT Backlog | Not executable in this container

# AWT BACKLOG

### SMD-F04 — Access Rights/Groups × Multi-Company Record Rule interaction (highest priority in this pilot; documentation pass 2026-09-29, source-code verification 2026-09-30)

- **Criticality**: C1
- **Hypothesis verified**: a user's effective access to a model is the intersection, not just the union, of (a) their Groups' model-level grant and (b) any applicable Multi-Company Record Rule's row-level filter — confirmed directly in source (`ir_rule.py`) for the `base`/`sale` module sample.
- **New AWT item added 2026-09-30**: **superuser/`sudo()` execution bypasses record rules entirely** (`ir_rule.py:120-121`) — this needs its own runtime confirmation, distinct from the ordinary-user-access test below: verify in a live environment that a background job or system-level process running as superuser can indeed read/write across company boundaries that would otherwise be blocked for an ordinary user in the same Groups.
- **Required environment**: an authorized Odoo 19 environment with at least two companies, two Groups with differing model access, and one user in a non-default company; plus one server-side scripted action or automation known to run via `sudo()`, to test the superuser path specifically.
- **Runtime action**: (1) attempt CRUD operations across the Group/company combinations and observe allow/deny outcomes; (2) trigger the known `sudo()` automation and confirm it can act across companies that its underlying user could not.
- **Expected observable result**: (1) access denied whenever either axis alone would deny it (true intersection) for ordinary access; (2) the `sudo()` path succeeds regardless of company scoping.
- **Evidence required**: exact allow/deny outcome per Group/company combination tested; confirmation of the `sudo()` path's actual cross-company behavior.
- **Target V**: V5 (floor V4) | **Current V**: source-code-tier (higher confidence than V2 documentation, not on this Deep Study's own V0-V5 runtime-verification scale) | **Missing proof**: full runtime confirmation only, for both the ordinary-access composition rule and the newly-identified superuser bypass path — and a full (not sampled) module sweep of `ir.rule` records beyond `base`/`sale` if completeness is ever required.

### SMD-F01/F02/F03

Carry-forward from `GROUP_01_SALES_INVENTORY_PURCHASE` — that track's own AWT/runtime posture (if any) applies; not duplicated here.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 1 (SMD-F04)
FUNCTIONS CARRIED FORWARD (no new AWT plan from this pilot) : 3 (SMD-F01/F02/F03)
```
