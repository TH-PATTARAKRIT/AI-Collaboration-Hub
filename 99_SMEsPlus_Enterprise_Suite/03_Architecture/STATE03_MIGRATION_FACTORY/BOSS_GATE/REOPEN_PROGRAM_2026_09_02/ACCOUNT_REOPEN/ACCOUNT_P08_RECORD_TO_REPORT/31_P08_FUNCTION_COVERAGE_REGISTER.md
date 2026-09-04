# P08_FUNCTION_COVERAGE_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Coverage of the process directive's own subject list. `COVERED` = examined against primary source with findings recorded. `PARTIAL` = examined, with a named residual. `ROUTED` = owned by another process.

| # | Directive subject | State | Where |
|---|---|---|---|
| 1 | Chart of accounts | COVERED | `02` |
| 2 | Account identity | COVERED | `04` |
| 3 | Account types | COVERED | `02` (`COA-09`..`COA-13`) |
| 4 | Account groups | COVERED | `02` (`COA-14`..`COA-16`) |
| 5 | Journals | COVERED | `05`, `07` |
| 6 | Journal groups | COVERED | `05` |
| 7 | Journal entries | COVERED | `05` |
| 8 | Journal items | COVERED | `05` |
| 9 | Posting engine semantics | COVERED | `05` |
| 10 | Source module posting | COVERED — denominator declared as a **floor** | `06`, `12` |
| 11 | Reversal | **PARTIAL** — reversal dating found unconstrained only at review; `P08-RQ-PC-09` | `05`, `09` §7A |
| 12 | Correction | COVERED | `07` |
| 13 | Manual GL | COVERED | `07` |
| 14 | Reconciliation | COVERED | `08` |
| 15 | Currencies | COVERED | `10` |
| 16 | Exchange rates | COVERED | `10` |
| 17 | Fiscal years | COVERED | `09` |
| 18 | Periods | COVERED | `09` |
| 19 | Lock dates | COVERED | `09` |
| 20 | Month close | COVERED | `09` |
| 21 | Year close | **PARTIAL** — the central negative is class `B`, not `A` | `09` |
| 22 | Retained earnings | COVERED | `09`, `11` |
| 23 | Closing adjustments | COVERED | `09` |
| 24 | Trial balance | COVERED | `11` |
| 25 | General ledger | COVERED | `11` |
| 26 | Balance sheet | COVERED | `11` |
| 27 | Profit & loss | COVERED | `11` |
| 28 | Cash flow | COVERED | `11` |
| 29 | Partner ledger | COVERED | `08`, `11` |
| 30 | Journal report | COVERED | `11` |
| 31 | Audit trail | COVERED | `05`, `11` |

**31 of 31 addressed. 28 covered, 3 partial, 0 omitted.**

**Residuals that bound this coverage, and are not hidden by it:** every finding is stated against the base implementation of the target root, while **43 files extend the ledger entry object and were not examined** (`P08-U-14`); **20 of the 21 custom modules that touch the ledger were not examined** (`P08-U-10`); and **~19 class-`A` claims were not re-run across the root set** (`P08-U-13`). Coverage of a subject is not coverage of its extensions.
