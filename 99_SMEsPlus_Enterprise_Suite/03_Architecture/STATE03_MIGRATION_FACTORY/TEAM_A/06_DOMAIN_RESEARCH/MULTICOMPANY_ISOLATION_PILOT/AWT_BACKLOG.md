> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx9

### MCT-F02 — Inter-company stock-move sync valuation (HIGH VALUE, joins capstone session)

- **Criticality**: C1
- **Hypothesis to verify, refined 2026-09-30 (source-static lead, Handoff round 2 `R4`)**: When Inter-Company Transactions synchronizes a stock move between two companies, each side computes its own valuation independently (per its own costing method/category), rather than the value being copied across the company boundary — consistent with a per-company `standard_price` field and no found value-copy mechanism, but the sync feature itself was not traced to Community source, so it may be implemented by a non-Community module with different behavior.
- **Required environment**: Two companies in one database, Inter-Company Transactions enabled with stock-move sync, different costing methods on each side (to make divergence observable if it occurs).
- **Runtime action**: Trigger a cross-company stock move; inspect the valuation entry on each company's books.
- **Expected observable result**: Either independently-computed values (supporting the hypothesis) or an identical copied value (contradicting it) — a clean, decisive test.
- **Cross-module observation**: Compare against every prior Gx's valuation findings — this is effectively the same question asked across a company boundary instead of within one.
- **Evidence required**: Journal entries on both sides of the sync.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: The core question.

### MCT-F05 — Warehouse-level access control

- **Hypothesis to verify, refined 2026-09-30 (source-static lead, Handoff round 2 `R8`)**: No native single-field mechanism exists at Community-source tier — confirmed by direct code reading (every stock security rule found is company-scoped, none warehouse-scoped); only manually constructed record rules/groups (or a custom module, not yet scanned) achieve warehouse-level restriction.
- **Required environment**: Same database, two warehouses in one company, attempt to find a native "restrict user to warehouse" field before resorting to record rules.
- **Runtime action**: Search the user/warehouse configuration UI directly for a native restriction field.
- **Expected observable result**: None found natively; record rules confirmed as the only path.
- **Evidence required**: UI walkthrough confirming absence.
- **Target V**: V5 (floor V4) | **Current V**: V1 | **Missing proof**: Direct confirmation of the absence, and the actual record-rule mechanics if attempted.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 (MCT-F02, MCT-F05)
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7, Gx8, Gx9
```
