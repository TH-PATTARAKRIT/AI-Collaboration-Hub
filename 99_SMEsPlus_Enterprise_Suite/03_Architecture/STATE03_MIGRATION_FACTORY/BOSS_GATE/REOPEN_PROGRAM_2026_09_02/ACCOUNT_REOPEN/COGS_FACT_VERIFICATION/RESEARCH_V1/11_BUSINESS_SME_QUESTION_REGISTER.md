# 11 — Business SME Question Register

Only unknowns that cannot be resolved technically (by re-reading existing documentation, or by re-fetching a specific page) are listed here. Items resolvable by re-fetch or by re-reading an already-approved contract are excluded (routed instead in file `18` Next Action Routing Matrix).

## SME-Q-01

- **Related Unknown:** `CGS-U22`, `CGS-U08`, `CGS-U16`, `CGS-U40`, `CGS-U45`, `CGS-U48`, `CGS-U50` (the "not every value decrease is COGS" cluster)
- **Related JT:** `JT-01`, `JT-06`
- **Exact Question:** When SMEsPlus records an inventory value decrease that is *not* a sale (adjustment, scrap, shrinkage, write-down, late-cost absorption), what is the business's actual current practice for classifying it — does the business's bookkeeper/accountant already separate these into distinct accounts today (in whatever system or manual process they currently use), or are they currently all lumped into one COGS-like line?
- **Why Required:** No reference-ERP documentation supplies a safe default, and no Thai statutory source mandates a specific chart-of-accounts structure for this distinction — it is a business-practice and control-design question, not a documentation gap.
- **Choices if applicable:** (a) Mirror current manual/legacy practice; (b) Design a new distinct-account structure regardless of current practice; (c) Ask the business's external accountant/auditor what they require for statement presentation.
- **Evidence Already Known:** DR file `24` confirms Thai TAS 2 requires COGS-matching recognition and separate write-down disclosure, but does not mandate a specific sub-ledger structure.
- **Impact of Each Answer:** Directly shapes the chart-of-accounts design for `JT-01` and the close-reconciliation design for `JT-06`.

## SME-Q-02

- **Related Unknown:** `CGS-U32`, `CGS-U33` (return cost basis, `JT-05`)
- **Related JT:** `JT-05`
- **Exact Question:** When a customer returns goods in a later accounting period than the original sale, does the business currently expect the return to be valued at the *original* selling cost, or is it acceptable for it to be valued at whatever the *current* cost happens to be at return time (potentially different due to intervening purchases at different prices)?
- **Why Required:** This is precisely the fact the reference ERP itself cannot answer consistently (it patches the gap with "manual adjustment"). It is a genuine business-policy choice, not a technical unknown.
- **Choices if applicable:** (a) Always reverse at original cost (requires tracking original cost per unit sold — a traceability requirement); (b) Reverse at current cost, accept a residual variance line; (c) Reverse at current cost only within the same period, require manual review for cross-period returns.
- **Evidence Already Known:** `CGS-U32` full fact pattern (file `10`).
- **Impact of Each Answer:** Directly determines whether SMEsPlus needs per-unit original-cost lineage (a data-model requirement) or can rely on a period-average model with a variance-tolerance control.

## SME-Q-03

- **Related Unknown:** `CGS-U01`, `CGS-U20`, `CGS-U31` (COGS recognition timing, `JT-04`)
- **Related JT:** `JT-04`
- **Exact Question:** In the business's actual sales process, does the customer invoice typically get issued at the same time as delivery, before delivery (e.g., prepayment/advance billing), or after delivery (e.g., invoicing on a billing cycle)? Is this consistent across all customers, or does it vary?
- **Why Required:** The reference-ERP evidence shows recognition timing is architecturally tied to whichever event (delivery or invoice) actually happens in practice — but does not tell us which pattern SMEsPlus's actual target businesses follow. This is empirical fact about the business, not a documentation gap.
- **Choices if applicable:** N/A — open-ended factual answer expected.
- **Evidence Already Known:** None — this specific operational-pattern question was not asked of any business stakeholder in the DR session.
- **Impact of Each Answer:** If invoice-after-delivery is universal, a delivery-triggered COGS model is safe from the matching-principle risk in `CGS-U31`. If invoice-before-delivery occurs at all, `JT-04` must explicitly design a control for it, not just pick an event.

## Not Asked (and Why)

Several items initially considered for SME questions were excluded because they are answerable from existing evidence without needing a business stakeholder:

- `CGS-U41` (whether the 16-field handoff contract already covers unmatched-fact queries) — answerable by re-reading the already-approved contract text directly; routed as a documentation task in file `18`, not an SME question.
- `CGS-U04`/`CGS-U12` (19.0 field reconstruction) — answerable by a direct re-fetch attempt, a technical task, not a business question.
