# Cumulative cost and progress ledger

> **DEEPSEEK-REPORTED.** Updated 2026-10-02 at each boundary. Cost is recorded in **tokens and tool requests** as reported by each delegated worker's completion record; **monetary cost is not computed** (no pricing data available to this harness). Main-controller session usage is not separately metered by this harness and is **not included**.

| Metric | Value |
|---|---|
| Completed delegated research workers | 37 |
| Cumulative worker tokens (reported) | 20,924,568 |
| Cumulative worker tool requests (reported) | 5,089 |
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
