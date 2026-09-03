# 09 — JT-05 Targeted Resolution: Return Cost Basis (C-03)

Source fact package: Fact Verification session file `10_JT05_FACT_PACKAGE.md`.

## 1. What Is Known (cited)

- AVCO: return valued at current average cost at return time, not original sale cost; average not retroactively recalculated. Vendor's own documentation admits a discrepancy between the credit-note financial reversal and the inventory-valuation reversal, with "manual adjustment" as its own stated fix (`CGS-U32`).
- FIFO: layer-consumption on return is community-corroborated only, not primary-documented — materially weaker evidence tier.
- Three independently-settable dates on a later-period return (sale date, physical return date, credit-note date) with no forced alignment.
- Return feature documentation itself is silent on cost basis (`CGS-U33`).
- No evidence that Thai TAS 2 names "returns" explicitly, though its general costing-consistency principle is unresolved as applied to this case (`TH-NEW-02`, unresearched).
- No business-stakeholder answer on whether SMEsPlus should reverse returns at original or current cost (`SME-Q-02`, unanswered).

## 2. What Is Genuinely Unknown

Whether SMEsPlus values a cross-period return at original sale cost (requiring per-unit cost lineage — a data-model requirement) or current cost (accepting a variance line), and whether the FIFO sub-case behaves as the community claims (unverified against a primary source or live instance).

## 3. Classification of the Unknown Itself

Two distinct sub-questions with two distinct classifications:
- **AVCO cost-basis choice** — a **BUSINESS POLICY / ACCOUNTING POLICY** decision. The reference behavior is a documented anti-pattern (the vendor's own admitted gap), not a design to copy, so there is no "adopt the reference" shortcut available even in principle.
- **FIFO mechanism** — a **FACT** question (what actually happens), currently unverifiable above community-evidence tier.

## 4. Evidence That Would Resolve It

1. `SME-Q-02` answered (original-cost vs. current-cost policy preference, and whether per-unit cost lineage is an acceptable data-model cost).
2. `TH-NEW-02` researched (does TAS 2's costing-consistency principle constrain the original-vs-current choice).
3. Live reference-instance FIFO-return test, or a stronger primary source than community corroboration, for the FIFO sub-case specifically.

None of these three is available this session.

## 5. Owner

- `SME-Q-02` → Business SME.
- `TH-NEW-02` → Thai Accounting-Tax research track.
- FIFO mechanism verification → Research owner, requires live-instance access this session does not have.
- Final return-cost-basis rule (and the reconciliation-control design for the AVCO admitted gap) → **Boss**.

## 6. Can It Be Parallelized?

Yes. `SME-Q-02`, `TH-NEW-02`, and the FIFO live-instance test are three independent evidence threads and can run concurrently.

## 7. Does It Block a Gate?

Yes — `JT-05` is the other named priority Joint Decision, and DR file `30` §11 (re-confirmed by Fact Verification file `10`) independently flags it as the single most material carried-forward gap in the entire 59-item register.

## 8. Disposition: NOT DECIDABLE

**NOT DECIDABLE this session**, for the AVCO policy choice (missing `SME-Q-02` and `TH-NEW-02`) **and** the FIFO mechanism fact (missing live-instance access or a stronger primary source).

This session evaluated **DECIDABLE WITH CONTROL** as a candidate classification for the AVCO sub-case specifically — e.g., "adopt current-cost valuation plus a mandatory variance-review control for cross-period returns above a materiality threshold." This is a plausible eventual design, but it is rejected as a this-session classification because (a) it would be inventing the materiality threshold and the control mechanics without `SME-Q-02` input on whether the business can even supply original-cost lineage today, and (b) `TH-NEW-02` has not been tested, so it is not established that current-cost valuation is even statutorily acceptable under TAS 2's consistency principle. A future session with `SME-Q-02` and `TH-NEW-02` answered could very plausibly reclassify this sub-case to DECIDABLE WITH CONTROL — that reclassification is not made here.

## 9. One-Line Reason (for the final report)

Vendor's own documentation admits an unreconciled AVCO return-reversal gap with no adoptable reference answer, the FIFO mechanism is unverified above community evidence, and neither the business's cost-basis preference nor a Thai TAS 2 test of the choice is available this session.
