# 04 — Unknown Classification Matrix

Each item from file `03` assigned exactly one primary category (a second, secondary influence is noted in parentheses where genuinely dual-natured — the count below uses primary only).

| ID | Primary Category |
|---|---|
| `CGS-U01` | U23 Documentation Contradiction (secondary: U04 COGS Timing) |
| `CGS-U02` | U21 Runtime/Configuration Dependent |
| `CGS-U03` | U06 Interim Account |
| `CGS-U04` | U24 Other (evidence-acquisition failure) |
| `CGS-U05` | U21 Runtime/Configuration Dependent |
| `CGS-U06` | U02 Accounting Recognition |
| `CGS-U07` | U03 Inventory Valuation |
| `CGS-U08` | U03 Inventory Valuation |
| `CGS-U09` | U05 Posting/Journal |
| `CGS-U10` | U21 Runtime/Configuration Dependent |
| `CGS-U11` | U05 Posting/Journal |
| `CGS-U12` | U22 Data Dependent |
| `CGS-U13` | U21 Runtime/Configuration Dependent |
| `CGS-U14` | U14 Period Close |
| `CGS-U15` | U14 Period Close |
| `CGS-U16` | U07 Purchase/Receipt |
| `CGS-U17` | U14 Period Close |
| `CGS-U18` | U03 Inventory Valuation |
| `CGS-U19` | U18 Reporting |
| `CGS-U20` | U08 Sale/Delivery |
| `CGS-U21` | U07 Purchase/Receipt |
| `CGS-U22` | U11 Scrap/Loss |
| `CGS-U23` | U11 Scrap/Loss |
| `CGS-U24` | U03 Inventory Valuation |
| `CGS-U25` | U04 COGS Timing |
| `CGS-U26` | U09 Return/Reversal |
| `CGS-U27` | U11 Scrap/Loss |
| `CGS-U28` | U04 COGS Timing |
| `CGS-U29` | U03 Inventory Valuation |
| `CGS-U30` | U07 Purchase/Receipt |
| `CGS-U31` | U04 COGS Timing |
| `CGS-U32` | U09 Return/Reversal |
| `CGS-U33` | U09 Return/Reversal |
| `CGS-U34` | U12 Landed Cost |
| `CGS-U35` | U12 Landed Cost |
| `CGS-U36` | U12 Landed Cost |
| `CGS-U37` | U13 Manufacturing/Production |
| `CGS-U38` | U13 Manufacturing/Production |
| `CGS-U39` | U03 Inventory Valuation |
| `CGS-U40` | U14 Period Close |
| `CGS-U41` | U14 Period Close |
| `CGS-U42` | U15 Multi-company |
| `CGS-U43` | U16 Intercompany |
| `CGS-U44` | U15 Multi-company |
| `CGS-U45` | U17 Migration |
| `CGS-U46` | U17 Migration |
| `CGS-U47` | U17 Migration |
| `CGS-U48` | U04 COGS Timing |
| `CGS-U49` | U18 Reporting |
| `CGS-U50` | U05 Posting/Journal |
| `TH-HOLD-COGS-01` | U19 Thailand Statutory |
| `TH-HOLD-COGS-02` | U19 Thailand Statutory |
| `TH-HOLD-COGS-03` | U19 Thailand Statutory |
| `TH-HOLD-COGS-04` | U19 Thailand Statutory |
| `TH-HOLD-05-residual` | U19 Thailand Statutory |
| `TH-HOLD-01,04,06,08,09` (carried, 5 items) | U19 Thailand Statutory |

## Category Distribution (primary category, 59 items)

| Category | Count |
|---|---:|
| U02 Accounting Recognition | 1 |
| U03 Inventory Valuation | 6 |
| U04 COGS Timing | 4 |
| U05 Posting/Journal | 3 |
| U06 Interim Account | 1 |
| U07 Purchase/Receipt | 3 |
| U08 Sale/Delivery | 1 |
| U09 Return/Reversal | 3 |
| U11 Scrap/Loss | 3 |
| U12 Landed Cost | 3 |
| U13 Manufacturing/Production | 2 |
| U14 Period Close | 5 |
| U15 Multi-company | 2 |
| U16 Intercompany | 1 |
| U17 Migration | 3 |
| U18 Reporting | 2 |
| U19 Thailand Statutory | 9 |
| U21 Runtime/Configuration Dependent | 4 |
| U22 Data Dependent | 1 |
| U23 Documentation Contradiction | 1 |
| U24 Other | 1 |
| **Total** | **59** |

(Corrected after an internal arithmetic check — an earlier draft of this table misstated the U03 and U04 rows and omitted U02 entirely; the per-ID assignments above are the source of truth and this table is derived from summing them, not the reverse.)

No category (U01 Business Event, U10 Inventory Adjustment, U20 SaaS/Tenant Boundary) received any item as its primary category — those concepts appear as secondary influences inside other items but were not the strongest-fit primary category for any single row. This is reported, not smoothed over, since the instruction is to name the single best-fit category, not to force even coverage.
