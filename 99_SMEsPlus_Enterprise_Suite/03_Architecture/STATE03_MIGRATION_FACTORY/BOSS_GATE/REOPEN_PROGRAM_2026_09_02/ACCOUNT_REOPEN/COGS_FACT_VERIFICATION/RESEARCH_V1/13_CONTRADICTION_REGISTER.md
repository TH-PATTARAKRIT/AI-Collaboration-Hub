# 13 — Contradiction Register

Every item the source register (`30`) itself labels `CONFLICTING`, preserved with lineage, none deleted.

## CONTRADICTION-01 — Price Difference Account Scope (`CGS-U03`)

- **Evidence A:** One source ties Price Difference Account scope to Standard Price costing only.
- **Evidence B:** Another source describes it applying to FIFO/AVCO "cost adjustments" also.
- **Evidence C (partial):** A further secondary source describes removal-then-reintroduction with narrower scope; a distinct "Variation Account" reported new in 19.0 may or may not be the same concept.
- **Why They Differ:** Likely version drift (pre-19 vs. 19.0 terminology and scope both changed) compounded by secondary-source imprecision.
- **Configuration Context:** Depends on costing method (Standard vs. AVCO/FIFO) and version.
- **Temporal/Version Context:** Spans multiple major reference-ERP versions.
- **Which Evidence Is Stronger:** None conclusively — all three are documentation-tier (Level 6), none is a direct primary-page quote confirmed on the current version.
- **Resolution:** Not resolved. Routed to `JT-02`.
- **Remaining Uncertainty:** Full — this is a genuine open conflict, not a research gap that more of the same reading would close; needs direct-fetch re-verification (`CGS-U04`/`CGS-U12` root cause) or a live-instance check.

## CONTRADICTION-02 — Landed Cost Residual Posting on Fully-Sold Stock (`CGS-U34`, `CGS-U36`)

- **Evidence A:** One source states the residual auto-books to COGS.
- **Evidence B:** Another source, attributed to 19.0+, states it requires a manually-generated entry via a dedicated Landed Cost Clearing account.
- **Evidence C:** At least one reported case (Scenario 11 in the 32-scenario register) generates **no journal entry at all** — described as a control break, not a third documented mechanism.
- **Why They Differ:** Version drift, compounded by what appears to be a genuine defect/gap in at least one reported reference-ERP configuration (the no-entry case is not attributed to any documented design, it is reported as unexpected).
- **Configuration Context:** Depends on version and possibly on landed-cost timing relative to sale completion.
- **Temporal/Version Context:** Version-specific claims conflict; the no-entry case's version is not clearly pinned.
- **Which Evidence Is Stronger:** Evidence B (19.0+, manual entry via Clearing account) is the most specific and version-attributed, but this does not resolve Evidence C, which describes an outright failure mode rather than an alternative rule.
- **Resolution:** Not resolved. Routed to `JT-08` and flagged by the DR session as an Audit VETO concern (`CGS-U36`).
- **Remaining Uncertainty:** Full — SMEsPlus must design its own landed-cost-after-sale handling rather than adopt any of the three reference behaviors, since one of the three is a documented failure mode.

## Discarded, Not Treated as a Contradiction — `CGS-U12`'s 19.0 Field Claim

The source register itself notes one 19.0-specific claim (Stock Input Account reported Cost-of-Revenue-typed in one fetch summary) was **discarded as a fetch-summarization artifact**, not treated as an unresolved conflict, because the alternative reading (Current Assets, matching the reliable directly-quoted 18.0 citation) rests on stronger evidence (a direct quote vs. a search-summary reconstruction). This session concurs with that evidentiary call and does not re-open it as a third contradiction — recorded here only so the distinction between "genuine unresolved conflict" and "one weak claim outweighed by a stronger one" is explicit and traceable, per the instruction not to silently smooth over evidence.

## Verdict

Two genuine, unresolved contradictions exist in the material unknown register (`CONTRADICTION-01`, `CONTRADICTION-02`); both were correctly labeled `CONFLICTING` by the source register and remain so. No new contradiction was discovered by this session's re-verification pass, and no existing contradiction was resolved (consistent with the documentation-only evidence ceiling in file `05`).
