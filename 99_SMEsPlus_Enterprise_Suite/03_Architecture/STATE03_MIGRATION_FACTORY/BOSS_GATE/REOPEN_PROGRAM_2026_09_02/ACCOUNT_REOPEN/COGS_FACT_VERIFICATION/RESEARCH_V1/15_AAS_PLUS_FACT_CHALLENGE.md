# 15 — AAS+ Independent Fact Challenge

Answering the twelve mandatory challenge questions against this package's own major claims.

1. **Is this actual fact or interpretation?** The core claim (reference ERP has no single COGS-timing or return-cost-basis answer) is fact, directly sourced from multiple independently-corroborating documentation files. The claim that this makes `JT-04`/`JT-05` "undecidable from documentation alone" is this research's own interpretive judgment layered on that fact — clearly labeled as such in files `09` and `10`.
2. **Does runtime evidence support it?** No runtime evidence exists for SMEsPlus (file `05`); reference-ERP runtime was not independently re-observed this session either — all claims trace to prior documentation research, not to a live session.
3. **Is behavior configuration-dependent?** Yes, extensively — costing method, version, and Periodic/Perpetual mode all gate behavior throughout file `03`. This is called out per-item, not glossed over.
4. **Are accounting and inventory events being conflated?** No — file `06` keeps quantity impact, value impact, and COGS/accounting impact in separate columns throughout, following the parent prompt's own boundary rule (`Inventory = Stock Truth`, `Accounting = Financial Truth`).
5. **Is valuation being conflated with posting?** No — file `06` Section D (cost flow) and Section F (interim accounts) are kept distinct from Section E (recognition event), and file `07` explicitly refuses to fabricate posting-level IDs precisely to avoid this conflation.
6. **Is COGS being conflated with invoice recognition?** This is exactly the open question `JT-04` addresses; this package does not resolve it in either direction and says so directly (file `09` §4).
7. **Is a vendor-specific implementation being treated as universal?** No — every fact in files `06`–`10` is explicitly labeled as reference-ERP/benchmark behavior, not a SMEsPlus requirement, per the "Target Design" row in each fact package.
8. **Is migration behavior contaminating future-state semantics?** Not observed in this package; migration-specific unknowns (`CGS-U45`–`U47`, category U17) are kept in their own section of file `03`, separate from the core recognition/valuation facts.
9. **Is one-company evidence being generalized to SaaS?** No — the multi-company/tenant unknowns (`CGS-U42`–`44`) are explicitly flagged as BLOCKING precisely because company-scoping is unconfirmed, not assumed.
10. **Are exceptions ignored?** No — negative-cost, zero-cost, and version-inconsistent exceptions (`CGS-U18`, `CGS-U36`) are carried forward as BLOCKING items, not smoothed into the general pattern.
11. **Does contradictory evidence exist?** Yes, two genuine contradictions (file `13`), both preserved with lineage, neither resolved by assertion.
12. **Would a reasonable auditor reach the same conclusion?** On the evidence presented — a documentation-only research base with zero runtime/database evidence for SMEsPlus itself, and two internally-inconsistent benchmark-system behaviors for the two priority JT items — a reasonable auditor would reach the same HOLD conclusion this package reaches, and would object to any stronger claim (e.g., "COGS facts are now sufficient for closure") as unsupported by what is actually in evidence.

## AAS+ Overall Finding

No overreach identified in this package's own claims. The package's most significant self-imposed discipline is refusing to fabricate Level 1–5 evidence that does not exist (file `07`) rather than papering over the gap with plausible-looking synthetic data — this is the correct response to Question 12, not a shortfall.
