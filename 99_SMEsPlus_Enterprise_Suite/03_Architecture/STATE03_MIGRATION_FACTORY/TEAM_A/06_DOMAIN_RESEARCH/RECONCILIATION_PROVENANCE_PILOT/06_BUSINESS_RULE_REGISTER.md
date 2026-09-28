> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx10)

### RCN-F01 — Stock Moves History / Stock Report

- **WHAT**: A "Stock history" view shows a product's stock-move history, including quantity, description, and why the product moved between locations.
- **WHY**: Physical-side traceability — knowing not just that stock moved, but why.
- **BUSINESS RULE**: Applying an inventory adjustment "simultaneously creates a stock move record in the Moves History report" — i.e., even a pure quantity correction is captured in the same traceability mechanism as an ordinary receipt/delivery move, not as a separate/special record type.
- **STATE**: Any stock-changing action → a Moves History entry.
- **DATA CONCEPT**: A stock move record with a reason/description field.
- **CONTROL**: This is the Stock Truth side's own audit trail, independent of whatever financial posting (or non-posting, per Gx6) accompanies it.
- **DEPENDENCY**: Every prior Gx's stock-changing functions (receipt, delivery, adjustment, scrap, manufacturing consumption/completion) all presumably feed this same Moves History mechanism, though not independently confirmed per-function this round.
- **EVENT**: "Stock move recorded."
- **RISK**: None identified — this is a traceability mechanism, not a control with a failure mode of its own.
- **UNKNOWN**: Whether Moves History links directly (by ID/reference) to any resulting journal entry, or is purely a stock-side record — see RCN-F02 for the one confirmed cross-link mechanism found.

### RCN-F02 — Backdating audit trail (dual chatter) — THE KEY FINDING

- **WHAT**: When an inventory transfer is backdated, a new optional field documents why; Odoo's chatter (its built-in comment/log thread, attached to individual records) posts a message on **both** the picking (stock-side record) **and** the journal entry (financial-side record), recording who backdated it, when, and why.
- **WHY**: A backdated transfer is exactly the kind of event where Stock Truth and Financial Truth could silently drift out of sync (the physical date and the accounting date now deliberately differ) — this dual-chatter mechanism is the documented safeguard.
- **BUSINESS RULE**: This is a **synchronized, dual-sided audit record** — not merely two independent logs that happen to both exist, but a deliberate design so that inspecting either side (the picking or the journal entry) reveals the same who/when/why.
- **STATE**: Transfer backdated → chatter message posted on picking → corresponding chatter message posted on the linked journal entry.
- **DATA CONCEPT**: This is the clearest evidence this Deep Study has found that a stock-side record and a financial-side record are **directly linked** (the journal entry "belonging to" a specific picking) — not merely related via shared timing or account structure, but referenced explicitly enough that a chatter message can be mirrored onto both.
- **CONTROL**: A genuine audit/event control — this is exactly the "Reconciliation identity / provenance from Stock Fact to Financial Fact" this scenario asks about, made concrete.
- **DEPENDENCY**: Depends on backdating being used at all — this mechanism was only found documented in the backdating context, not confirmed as present for an ordinary, non-backdated transfer.
- **EVENT**: "Backdate chatter recorded" (dual-sided).
- **RISK**: If this dual-chatter link only exists for the backdating *feature* specifically, then ordinary transfers may lack an equivalently visible cross-link, even though one presumably exists internally (a journal entry must reference *some* originating stock move to have been created at all) — this is an important nuance not to over-generalize from.
- **UNKNOWN**: Whether the underlying stock-move-to-journal-entry reference exists and is inspectable for *every* transaction, or whether the chatter mirroring is a backdating-specific enhancement layered on top of a reference that already existed but was previously less visible — not evidenced this round.

### RCN-F03 — Cost/valuation origin tracking

- **WHAT**: Clicking a product's Total Value (in the valuation report) shows all incoming quantities together with each one's remaining quantity and valuation.
- **WHY**: Under FIFO/AVCO (per Gx1's `GRV-F04`), different incoming lots can carry different unit costs — the system needs to track which specific incoming quantity a given remaining unit's value traces back to.
- **BUSINESS RULE**: This is a per-incoming-move ledger, not a single blended total — confirms and extends Gx1's finding that "remaining units from each previous incoming move retain their own individual valuation" (FIFO).
- **STATE**: Each incoming move → its own remaining-quantity/valuation record, decremented as that specific lot is consumed (by delivery, scrap, or otherwise).
- **DATA CONCEPT**: This is the "identity" half of "reconciliation identity/provenance" — a specific unit's value has a traceable origin, not just an aggregate.
- **CONTROL**: Underlies GRV-F05's landed cost allocation (which adjusts a *specific* prior receipt's valuation) and IAV-F03's adjustment mechanism.
- **DEPENDENCY**: Builds on Gx1 `GRV-F04`'s FIFO finding.
- **EVENT**: N/A — a standing ledger structure, not a discrete event.
- **RISK**: None new — this strengthens confidence in, rather than contradicts, prior findings.
- **UNKNOWN**: Whether this same per-lot tracking exists under AVCO (which conceptually blends cost, unlike FIFO) or is FIFO-specific — not evidenced this round.

### RCN-F04 — Bank Reconciliation (explicitly Not Applicable to this scenario)

- **WHAT**: Bank Reconciliation matches bank transactions against counterpart business records (customer invoices, vendor bills, payments); unmatched items (e.g., bank fees) are written off manually or via configurable Reconciliation Models (manual action buttons, or automatic rules for recurring flows).
- **WHY**: Recorded here **only to explicitly distinguish it** from this scenario's actual subject. "Reconciliation" in Odoo's own documentation predominantly means this bank-matching concept, not Stock-Fact-to-Financial-Fact provenance.
- **BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: Out of scope for this scenario — recorded for terminology hygiene, not as a finding about Stock↔Financial provenance.
- **RISK**: The only risk here is a *future reader* confusing this Gx's actual subject (RCN-F01-F03) with Bank Reconciliation because both use the word "reconciliation" — mitigated by this explicit entry.
- **UNKNOWN**: N/A.
