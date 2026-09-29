> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx10 (FINAL)

### RCN-F02 — Ordinary (non-backdated) stock↔financial cross-link (HIGH PRIORITY, closes GAP-RCN-01)

- **Criticality**: C1
- **Hypothesis to verify, refined 2026-09-30 (source-static lead, Handoff round 2 `R9`)**: An ordinary, non-backdated stock movement's resulting journal entry (where one exists, per the Gx6/Gx8 rule) carries an inspectable reference back to its originating stock move — source confirms this reference is set for every move-level accounting entry, not conditioned on backdating. The chatter mirroring itself is likely a backdating-specific *visibility* enhancement layered on a reference that already existed, not the reference's origin. Still unconfirmed: whether bill/invoice-line-originated entries (a separate mechanism) are ever mistaken for the same provenance link by a user inspecting them.
- **Required environment**: Same as the capstone session.
- **Runtime action**: Validate an ordinary receipt/delivery under automatic valuation; locate the resulting journal entry; check whether it references the originating stock move/picking (by ID, by a linked-record field, or only by matching date/amount coincidentally).
- **Expected observable result**: A real reference field (strong provenance) vs. no direct reference, only correlation by date/amount (weak provenance) — a decisive, important distinction.
- **Cross-module observation**: Run alongside every other capstone test — this is a natural add-on, not a separate session.
- **Evidence required**: The journal entry's linked-record fields, if any.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: The core question — does provenance strength require the backdating feature, or is it always present?

### RCN-F03 — AVCO per-lot tracking

- **Hypothesis to verify, refined 2026-09-30 (source-static lead, Handoff round 2 `R9`)**: Per-lot origin tracking (confirmed for FIFO) also applies, in some form, under AVCO — source confirms Standard/Average/FIFO all feed the same lot-cost computation and an outgoing move uses that lot's own cost; runtime confirmation of the actual numbers (especially against a late vendor bill) is still needed.
- **Runtime action**: Repeat the Total-Value click-through check under an AVCO-costed product category.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: AVCO-specific confirmation.

## Backlog status — FINAL

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 (RCN-F02, RCN-F03)
CAPSTONE SESSION NOW SPANS ALL 10 SCENARIOS (Gx1-Gx10, Gx3 folded into Gx1)
```

This is the last AWT backlog addition for the current continuous-execution run. The full capstone session (spanning every C1 function across all 10 scenarios) is now the single largest, highest-value piece of queued work in `STATE03_BOSS_GATE_QUEUE.md` `BGQ-04`.
