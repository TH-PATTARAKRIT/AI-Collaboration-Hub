# Mixed Capsule Routing

Status: `STRUCTURAL PREFLIGHT ONLY / MASTER DECISION REQUIRED`

## Problem

A batch may contain multiple CFC capsules with different A2 recommendations. A batch-level handoff must not flatten `CONDITIONAL PASS` and `REJECT` into one state.

## Event sequence

```text
A2
  -> A2_MIXED_DISPOSITION_READY / ACTION_REQUIRED
       capsule A -> CONDITIONAL_PASS_RECOMMENDATION -> proposed A3
       capsule B -> REJECT_RETURN                  -> proposed A1

MASTER
  -> verifies scope, dependencies, CRQs, lineage and manifests
  -> MASTER_ROUTE_A3  / accepted subset only
  -> MASTER_RETURN_A1 / rejected subset only
  -> keeps batch HOLD until rejected and dependent scopes are reconciled
```

## Structural invariants

- `capsule_routes` must exactly match `cfc_revisions`.
- A mixed event must contain at least one A1-return route and one A3-forward route.
- Every A1 route must use `REJECT_RETURN`.
- No A3 route may use `REJECT_RETURN`.
- `MASTER_ROUTE_A3` may contain only A3 routes and requires zero Critical/High CRQs and no blocked dependency within the routed subset.
- `MASTER_RETURN_A1` may contain only A1 routes and every route must be rejected.
- The private controller must compare both MASTER children with the immutable A2 parent: child scopes must be disjoint, their union must equal the parent scope, and disposition/next-role values must not be relabelled.
- Splitting a batch does not change its module denominator, erase failed evidence, close CRQs, or release ROOM B.
- A2 recommendations are non-authoritative until MASTER and the private controller verify them.
