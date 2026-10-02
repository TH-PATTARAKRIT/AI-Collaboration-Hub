# Cumulative cost and progress ledger

> **DEEPSEEK-REPORTED.** Updated 2026-10-02 at each boundary. Cost is recorded in **tokens and tool requests** as reported by each delegated worker's completion record; **monetary cost is not computed** (no pricing data available to this harness). Main-controller session usage is not separately metered by this harness and is **not included**.

| Metric | Value |
|---|---|
| Completed delegated research workers | 69 |
| Cumulative worker tokens (reported) | 24,033,386 (+ U47–U63 fix/gate pass session — tokens not separately metered) |
| Cumulative worker tool requests (reported) | 5,713+ |
| Workers running at last update | see `NEXT_ATOMIC_UNIT_QUEUE.tsv` and PR #74 notifications |
| Claude-accepted units / packets (evidenced in verifier log) | listed below |

## Claude-accepted (as evidenced in `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` §10–§28)
- U20
- U24
- U25
- U26
- U27
- U28
- U29
- TXA1
- TXA2
- TXC
- TXS
- TXS-R1
- U24-R1 (correction)
- correction packets U08-R1,U10-R1,U10-R2,U10-R3,U11-R1,U11-R2,U06-R1,U07-R2,SCOPE-R1 (full read) and others at metadata level

Units whose log entry shows only mechanical hash-integrity intake (pending confirmed semantic review): U01–U04, U06–U19, U21–U23, C01, C02 (also see the Claude verification column of the module matrix).

## Per-worker usage
| Worker | Tokens | Tool requests |
|---|---|---|
| U01 | 573,914 | 124 |
| U02 | 574,043 | 118 |
| U03 | 567,376 | 124 |
| U04 | 556,212 | 113 |
| U05 | 541,722 | 134 |
| U06 | 359,616 | 59 |
| U07 | 524,254 | 105 |
| U08 | 631,922 | 146 |
| U09 | 499,935 | 111 |
| U10 | 433,029 | 81 |
| U11 | 508,615 | 124 |
| U12 | 680,852 | 158 |
| U13 | 729,597 | 148 |
| U14 | 700,737 | 152 |
| U15 | 541,011 | 130 |
| U16 | 559,145 | 122 |
| U17 | 710,060 | 163 |
| U18 | 723,123 | 147 |
| U19 | 531,333 | 147 |
| U20 | 568,873 | 128 |
| U21 | 681,467 | 159 |
| U22 | 572,562 | 129 |
| U23 | 660,944 | 131 |
| C01 | 695,280 | 160 |
| C02 | 853,367 | 233 |
| CorrW(U10-R3,U06-R1,U07-R2) | 448,383 | 118 |
| U24 | 465,016 | 147 |
| U25 | 511,346 | 171 |
| U26 | 451,189 | 156 |
| U27 | 518,967 | 156 |
| U28 | 450,505 | 128 |
| U29 | 440,552 | 104 |
| TXS | 353,044 | 139 |
| TXA1 | 624,486 | 157 |
| TXA2 | 703,097 | 184 |
| TXC | 406,635 | 111 |
| TXS-R1 | 572,359 | 172 |
| U36 | 607,651 | 119 |
| U39 | 594,774 | 133 |
| U34 | 634,994 | 102 |
| U41 | 608,156 | 123 |
| U30 | 663,243 | 147 |
| U42 | — | — |
| U43 | — | — |
| U44 | — | — |
| U45 | — | — |
| U46 | — | — |
| U47 | — | 150 |
| U48 | — | 121 |
| U49 | — | — |
| U50 | — | 155 |
| U51 | — | 105 |
| U52 | — | 155 |
| U53 | — | 125 |
| U54 | — | 130 |
| U56 | — | 125 |
| U57 | — | 160 |
| U58 | — | 150 |
| U59 | — | 105 |
| U60 | — | 105 |
| U61 | — | 130 |
| U62 | — | 152 |
| U63 | — | 145 |
| U64 | — | 80 |
| U65 | — | 125 |
| U66 | — | 88 |
| U67 | — | 105 |
| U68 | — | 91 |
| U69 (reconciliation) | — | — |
| U70 | COST TELEMETRY NOT VERIFIED | 88 |
| U71 | COST TELEMETRY NOT VERIFIED | 100 |
| U72 | COST TELEMETRY NOT VERIFIED | 49 |
| U73 | COST TELEMETRY NOT VERIFIED | 52 |
| U74 | COST TELEMETRY NOT VERIFIED | 37 |
| U75 | COST TELEMETRY NOT VERIFIED | 64 |
| U76 | COST TELEMETRY NOT VERIFIED | 109 |
| U77 | COST TELEMETRY NOT VERIFIED | 100 |
| U78 | COST TELEMETRY NOT VERIFIED | 70 |
| U79 | COST TELEMETRY NOT VERIFIED | 57 |
| U80 | COST TELEMETRY NOT VERIFIED | 38 |
| U81 | COST TELEMETRY NOT VERIFIED | 53 |
| U82 | COST TELEMETRY NOT VERIFIED | 52 |
| U83 | COST TELEMETRY NOT VERIFIED | 45 |
| U84 | COST TELEMETRY NOT VERIFIED | 53 |
| U85 | COST TELEMETRY NOT VERIFIED | 44 |
