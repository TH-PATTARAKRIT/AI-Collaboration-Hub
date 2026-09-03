# 11 — COGS Recognition Options Analysis (Models A–E)

Direct support for `JT-04` (file `08`). Lays out five candidate recognition-trigger models and classifies each.

## Model A — Delivery-Triggered

COGS recognized at the moment of physical stock movement out of the warehouse (goods-issue event), independent of invoice timing.

- **Classification: POLICY, with FACT support.** The reference ERP's pre-19 behavior is exactly this model (FACT — directly documented). Whether SMEsPlus should adopt it is a POLICY choice, not compelled by the fact of the reference having once used it.
- **Evidence support in this repo:** Strong for "this model exists and has been implemented by a real system" (Fact Verification file `09` §1). No evidence it is required by Thai standards specifically (`TH-NEW-01` unresearched).
- **Requires Business/Boss decision:** Yes — whether SMEsPlus's actual sales process (invoice before, at, or after delivery — `SME-Q-03`, unanswered) makes this model safe or creates a mismatch with billing practice.

## Model B — Invoice-Triggered

COGS recognized at invoice/bill posting, independent of physical delivery timing.

- **Classification: POLICY, with FACT support.** The reference ERP's 19.0+ behavior is exactly this model (FACT — directly documented, with the delivery mechanism demoted to a period-close gap-filler).
- **Evidence support in this repo:** Strong for existence; the reference ERP's own version history shows the vendor moved *from* Model A *to* Model B, which is itself informative (a design trend) but not proof Model B is correct for SMEsPlus.
- **Requires Business/Boss decision:** Yes — same `SME-Q-03` dependency, and additionally carries the matching-principle risk flagged in `CGS-U31` if invoicing can precede delivery.

## Model C — Posting-Event-Triggered (Journal/GL Posting as the Trigger, Distinct from Invoice)

COGS recognized when a specific accounting-journal posting event occurs, which may or may not coincide with either delivery or invoice (e.g., a dedicated cost-release journal entry created by a background process).

- **Classification: CONFIGURATION / DESIGN DECISION.** No evidence in any file reviewed (Fact Verification or DR sessions) describes the reference ERP implementing a *third*, independent posting-event trigger distinct from Model A or B. This model is not evidenced as an existing reference pattern — it is a structural possibility this session names because the register's `CGS-U50` (Cost Release classification) and `CGS-U45` (accounting-side duplicate-posting risk) both imply SMEsPlus may need its own posting-event abstraction layer regardless of which physical/commercial event triggers it.
- **Evidence support in this repo:** None for this model existing as a reference-ERP pattern. Indirect support for the *need* for a posting-event abstraction from `CGS-U45`/`CGS-U50`.
- **Requires Business/Boss decision:** Yes, entirely — this would be original design work, not an adoption of any documented reference behavior.

## Model D — Hybrid (Configuration-Dependent, Mirroring Reference's Own Instability)

COGS recognition event is itself a per-category or per-invoicing-policy configuration choice (e.g., delivery-triggered for delivered-quantity invoicing policy, invoice-triggered for ordered-quantity invoicing policy), rather than one fixed system-wide rule.

- **Classification: CONFIGURATION, layered on a DESIGN DECISION.** This is the closest model to what `CGS-U20` (invoicing-policy interaction with the trigger table) implies could exist, but `CGS-U20` explicitly states this interaction is undocumented in any source reviewed — so this model is a plausible synthesis, not a confirmed reference pattern.
- **Evidence support in this repo:** Weak/indirect — inferred from the existence of two separately-documented axes (invoicing policy, and recognition timing) that were never cross-referenced in any source (Fact Verification file `03`, `CGS-U20`).
- **Requires Business/Boss decision:** Yes — and additionally requires the `CGS-U20` re-fetch to even confirm whether the reference ERP itself does this, before SMEsPlus could decide to imitate or diverge from it.

## Model E — Other (Named Because Evidence Suggests One Additional Candidate)

A **cut-off/period-close reconciliation model**, where interim postings (at delivery or invoice, whichever is operationally convenient) are provisional, and a period-close process reconciles them against a residual/Variation account — structurally similar to how the reference ERP's 19.0+ Variation-account mechanism already functions as a background reconciler regardless of the primary trigger event.

- **Classification: DESIGN DECISION, with FACT support for the reconciliation mechanism's existence.** The 19.0+ Variation-account pattern (FACT, documented in the reference ERP) already behaves partly this way as a secondary mechanism layered on top of Model B, not as a standalone trigger model — this session names it as "Model E" because it is a genuinely distinct architectural approach (treat the trigger event as provisional, treat close-time reconciliation as authoritative) rather than a variant of A or B.
- **Evidence support in this repo:** Moderate for the reconciliation-mechanism component (documented); none for it being used as a standalone SMEsPlus recognition model rather than a secondary control on top of A or B.
- **Requires Business/Boss decision:** Yes — this is the most original of the five, closest to `CGS-U37`/`CGS-U39`-style "no reference precedent, original design work required" territory.

## Summary Table

| Model | Classification | Reference-ERP evidence | Requires Business/Boss decision |
|---|---|---|---|
| A — Delivery-triggered | POLICY (FACT-supported) | Strong (pre-19 documented behavior) | Yes |
| B — Invoice-triggered | POLICY (FACT-supported) | Strong (19.0+ documented behavior) | Yes |
| C — Posting-event-triggered | CONFIGURATION/DESIGN DECISION | None as standalone reference pattern | Yes, entirely |
| D — Hybrid/config-dependent | CONFIGURATION on DESIGN DECISION | Weak/indirect, unconfirmed | Yes, plus a prerequisite re-fetch |
| E — Cut-off/reconciliation | DESIGN DECISION (FACT-supported mechanism only) | Moderate for the mechanism, none for standalone use | Yes, most original of the five |

## What the Evidence in This Repo Actually Supports vs. What Requires a Decision

The evidence supports, as FACT, only that Models A and B have each been implemented by a real system at different points in that system's history, and that a Variation-account reconciliation mechanism (relevant to Model E) exists in the current reference version. **No model is evidenced as required or even recommended for SMEsPlus.** Selecting among A/B/C/D/E is a Boss/Business decision in every case, informed by `SME-Q-03` (actual invoice/delivery sequencing) and `TH-NEW-01` (whether TAS 2 constrains the trigger event) — neither of which this session could obtain (file `01` §2). This file does not recommend a model; recommending one would exceed this session's evidence and mandate.
