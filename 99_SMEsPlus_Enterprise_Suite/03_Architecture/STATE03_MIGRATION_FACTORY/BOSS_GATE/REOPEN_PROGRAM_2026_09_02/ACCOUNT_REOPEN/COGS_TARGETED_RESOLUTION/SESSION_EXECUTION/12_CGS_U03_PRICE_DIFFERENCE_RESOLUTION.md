# 12 — CGS-U03 Price Difference Account Resolution Attempt

Source: Fact Verification file `03` row `CGS-U03`; contradiction lineage in Fact Verification file `13` `CONTRADICTION-01`.

## 1. What Is Known

Three documentation sources describe the Price Difference Account's scope differently:
- Source A: scoped to Standard-Price costing only.
- Source B: applies to FIFO/AVCO "cost adjustments" also.
- Source C (partial/secondary): describes a removal-then-reintroduction with narrower scope, plus a possibly-distinct "Variation Account" reported new in 19.0.

## 2. What Is Genuinely Unknown

Whether the Price Difference Account and the newer "Variation Account" are the same concept under different names, different concepts that coexist, or a version-drift renaming — and which costing methods each actually applies to on the current reference version.

## 3. Attempt to Resolve This Session

**Attempted, not resolved.** This session does not have a working live documentation-fetch tool this session (file `01` §2), which is the specific evidence needed (a direct primary-page quote on the current version, per Fact Verification file `13`). No live reference-ERP instance was available either. This session therefore could not distinguish which of Sources A/B/C is correct, or whether they describe the same or different accounts.

## 4. Disposition

**HOLD — EVIDENCE REQUIRED.** Both prior sessions' classification stands unchanged: `MATERIAL / CONFLICTING`, routed to `JT-02`. This session did not weaken or strengthen either reading — no new evidence was available to do so. The contradiction is preserved with full lineage (see file `16` of this package).

## 5. Next Action, Concretely

A direct re-fetch of the current reference-ERP version's Accounting configuration documentation, specifically the field-level description of both "Price Difference Account" and "Variation Account" (if both exist as named fields), is the single bounded action that would close this — not a live-instance test, since this is a documentation-scope question, not a behavioral one. Owner: Docs/Research owner. Estimated effort: low (one or two targeted page fetches), contingent on tool availability in a future session.
