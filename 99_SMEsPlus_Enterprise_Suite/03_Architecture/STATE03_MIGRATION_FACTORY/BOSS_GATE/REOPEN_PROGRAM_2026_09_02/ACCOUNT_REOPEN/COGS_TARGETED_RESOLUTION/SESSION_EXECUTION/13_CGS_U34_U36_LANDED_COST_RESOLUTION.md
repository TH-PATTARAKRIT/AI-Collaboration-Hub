# 13 — CGS-U34 / CGS-U36 Landed Cost Resolution Attempt

Source: Fact Verification file `03` rows `CGS-U34`, `CGS-U36`; contradiction lineage in Fact Verification file `13` `CONTRADICTION-02`. Flagged by the COGS Deep Research session as an **Audit VETO concern** — this flag is carried forward, not softened.

## 1. What Is Known

Three distinct, non-reconcilable behaviors are documented for landed-cost residual posting on stock that has already been fully sold:
- Evidence A: auto-books the residual to COGS.
- Evidence B (19.0+, most version-specific and best-attributed): requires a manually-generated entry via a dedicated Landed Cost Clearing account.
- Evidence C: at least one reported case generates **no journal entry at all** — an outright control-break/failure mode, not a third documented design.

## 2. What Is Genuinely Unknown

Which of A/B is the current reference behavior (version not fully pinned for the no-entry case), and — separately and more importantly for SMEsPlus — what control SMEsPlus itself must design so that a landed-cost-after-full-sale event can never silently produce no entry at all (Evidence C's failure mode).

## 3. Attempt to Resolve This Session

**Attempted, not resolved, and this session concludes it should not be resolved by document-reading alone even with tool access.** Two of the three evidence items are a genuine documentation conflict (A vs. B), potentially closable by a targeted re-fetch. But Evidence C describes a **documented product failure**, not an alternative rule — no amount of reading resolves what SMEsPlus's own control should be when the underlying system (whichever behavior it settles into) fails to post at all. That is a Boss-level control-design decision, not a fact gap, regardless of whether A or B turns out to be the "correct" current reference behavior.

## 4. Disposition

**HOLD — BOSS RULING REQUIRED, WITH A BOUNDED EVIDENCE SUB-TASK.** Two-part disposition:
1. The A-vs-B documentation conflict: `OPEN — EVIDENCE REQUIRED`, same next action as file `12` (a targeted re-fetch), owner Docs/Research.
2. The Evidence-C control-break risk: **not evidence-closable at all**. This session recommends Boss treat this as requiring an explicit, positive control in SMEsPlus's own design — e.g., a mandatory reconciliation check that flags any landed-cost allocation against fully-sold stock with zero resulting journal entries — independent of which reference behavior (A or B) SMEsPlus's documentation research eventually confirms as most current. This recommendation is a control-design *option surfaced for Boss*, not a ruling made by this session.

## 5. Audit VETO Flag — Retained

Per the governing rule that this session must not soften a flagged Audit VETO concern: `CGS-U36`'s VETO flag from the COGS Deep Research session is carried forward unchanged into file `21` (Independent Targeted-Resolution Audit) of this package and into file `19` (AAS+ Challenge). It is not downgraded by this session's routing work.

## 6. Next Action, Concretely

- Docs/Research owner: targeted re-fetch to pin Evidence A vs. B to the current reference version.
- Boss: decide whether to adopt the recommended reconciliation-check control described in §4, independent of the A/B outcome.
- Both actions can run in parallel; neither blocks the other.
