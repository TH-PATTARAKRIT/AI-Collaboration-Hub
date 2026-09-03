# 14 — Business SME Decision Package

Carries the three Business SME questions forward from the Fact Verification session (file `11`) unchanged in substance, packaged for direct routing to a business stakeholder. No SME was available this session (file `01` §2) — these are not answered here.

## SME-Q-01 — Non-Sale Inventory Value Decreases

**Question:** When SMEsPlus records an inventory value decrease that is not a sale (adjustment, scrap, shrinkage, write-down, late-cost absorption), does the business's bookkeeper/accountant already separate these into distinct accounts today, or are they currently all lumped into one COGS-like line?

**Why it matters now:** Blocks `JT-01` (chart-of-accounts design) and `JT-06` (close-reconciliation design). Directly relevant to P0 items `CGS-U16`, `CGS-U22`, `CGS-U40`, `CGS-U45`, `CGS-U48`, `CGS-U50`.

**Choices:** (a) mirror current manual/legacy practice; (b) design a new distinct-account structure regardless of current practice; (c) ask the business's external accountant/auditor what they require for statement presentation.

**Status:** UNANSWERED. Routed to Business SME.

## SME-Q-02 — Return Cost Basis Preference

**Question:** When a customer returns goods in a later accounting period than the original sale, does the business expect the return valued at original selling cost, or is current cost at return time acceptable?

**Why it matters now:** Directly gates `JT-05` (file `09` of this package). This is the single highest-leverage SME answer available — `JT-05` is one of only two priority-tier items and this question is its primary missing input alongside `TH-NEW-02`.

**Choices:** (a) always reverse at original cost (requires per-unit cost lineage — a data-model requirement); (b) reverse at current cost, accept a residual variance line; (c) reverse at current cost only within the same period, require manual review for cross-period returns.

**Status:** UNANSWERED. Routed to Business SME.

## SME-Q-03 — Invoice/Delivery Sequencing Pattern

**Question:** Does the business's customer invoice typically get issued at the same time as delivery, before delivery (prepayment/advance billing), or after delivery (billing cycle)? Is this consistent across all customers?

**Why it matters now:** Directly gates `JT-04` (file `08` of this package) and is the deciding input for whether Models A, B, or D in file `11` are even operationally viable without a matching-principle control.

**Choices:** N/A — open-ended factual answer expected about actual business practice.

**Status:** UNANSWERED. Routed to Business SME.

## Recommended Sequencing If Only One Question Can Be Asked First

If Business SME time is scarce, this session recommends **SME-Q-03** first: it has the most direct, least-ambiguous downstream effect (it substantially narrows the Model A/B/D choice in file `11` even before `TH-NEW-01` is researched), whereas `SME-Q-01` and `SME-Q-02` each still require a follow-on Thai-statutory or design step regardless of the answer. This is a sequencing recommendation only — this session does not decide which question is asked, or when.

## Explicit Non-Action

This session does not answer any of these three questions on the business's behalf, infer a likely answer, or select a "reasonable default" — doing so would substitute this session's assumption for the business's actual practice, which the governing rule against converting assumptions into facts forbids.
