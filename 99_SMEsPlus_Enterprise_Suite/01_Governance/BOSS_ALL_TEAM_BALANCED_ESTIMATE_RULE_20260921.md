# Boss All-Team Balanced Estimate Rule

Authority: Boss, active session, 2026-09-21
Applies to: ALL SMEsPlus research, verification, mapping, planning, and execution teams

## Principle

Do not treat a planning estimate as a target that the final result must equal.

Research naturally has additions and omissions. A working estimate exists to give direction and scale, not to force reality to match a predetermined number.

## Required operating behavior

1. Start from a reasonable documented estimate or working universe.
2. Proceed with research; do not wait for the estimate to become exact.
3. If an expected item cannot be evidenced, record `NO-STUDY-EVIDENCE-FOUND` with the search scope/method. Do not invent evidence and do not force the item to count as complete.
4. If a new valid item is discovered, append it as `DISCOVERED-DURING-RESEARCH` with evidence and provenance.
5. If an item is deferred/out of current product scope, keep it in the audit inventory as `DEFERRED-NEXT-PHASE`; do not delete it to make the count look cleaner.
6. If an item was estimated but later proven duplicate, non-applicable, wrong-edition, or outside source authority, record the disposition and remove it from the next working estimate.
7. Estimate drift is normal. It creates a planning delta, not a project-wide HOLD.
8. The final count is whatever the evidence-backed, fully dispositioned universe actually becomes. It does not need to equal the original estimate.
9. A result may be called complete only when every item in the actual final universe has a valid disposition and all mandatory proof requirements for that stage are satisfied.
10. Formal Coverage still requires a Boss-frozen canonical Function-ID denominator. A planning/module estimate is never a Formal Coverage denominator.

## Balanced-control rule

Be neither too strict nor too loose.

- Too strict: stopping useful research because a planning count moved.
- Too loose: declaring completion or coverage without evidence.
- Correct middle path: keep researching, log deltas, preserve provenance, and reserve hard gates for claims or actions that require certainty.

## What may continue with uncertainty

- source study
- module/function discovery
- taxonomy mapping
- dependency discovery
- candidate function extraction
- documentation of unknowns
- evidence gathering

## What still requires strict certainty before release/claim

- posting/accounting rules
- tax/statutory semantics
- tenant/company isolation
- clean-room/IP boundary
- irreversible cross-module controls
- Formal Coverage claims
- implementation/release decisions that rely on unresolved critical semantics

## Finality rule

`FINAL` is not a target number.

`FINAL` means the actual evidence-backed universe has been worked through and every row/function has a disposition such as:

- `RESEARCHED-EVIDENCE-FOUND`
- `NO-STUDY-EVIDENCE-FOUND`
- `DISCOVERED-DURING-RESEARCH`
- `DEFERRED-NEXT-PHASE`
- `NOT-APPLICABLE-WITH-EVIDENCE`
- `DUPLICATE/RECONCILED`
- `SUPERSEDED-WITH-PROVENANCE`

The final total may be lower or higher than the starting estimate.
