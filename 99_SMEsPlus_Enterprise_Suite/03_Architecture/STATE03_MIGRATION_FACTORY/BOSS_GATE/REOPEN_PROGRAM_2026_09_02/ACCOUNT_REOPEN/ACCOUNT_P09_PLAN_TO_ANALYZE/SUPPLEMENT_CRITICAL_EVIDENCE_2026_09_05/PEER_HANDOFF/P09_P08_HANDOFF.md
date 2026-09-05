# P09_P08_HANDOFF — Record-to-Report
**Last consumed P08 commit:** `4bdf8a23d03d6df045d5f7791be3dc61c65d0e48` · **Checkpoint:** `CP-P09S17`

**P09 does not redefine Core Ledger truth.** Everything below is handed over, not ruled on.

| # | Item | Class |
|---|---|---|
| 1 | **account-type semantics.** The consumption gate matches on the **first token** of the account type, so a depreciation-**expense** type resolves to `expense` and is admitted. Does that conflate a *statement* classification with a *nature* classification? | **P08 owns the answer** |
| 2 | **journal-item eligibility.** Management records are created for a row if and only if the row carries an allocation — no account-type, row-type, context or company test on the creation path | FACT VERIFIED, see `S04` |
| 3 | **the budget query's financial-leg issue.** A balance-sheet-typed leg, where admitted, annihilates the attribution | FACT VERIFIED |
| 4 | **the measured shape of the ledger: 226,612 of 339,382 management records — 66.8 % — sit on balance-sheet general accounts** in a deployed database | **FACT VERIFIED.** The largest single number in this supplement |
| 5 | **depreciation posting** — a two-row entry whose allocation is written to both legs | FACT VERIFIED |
| 6 | **financial-vs-management truth.** The ledger is correct throughout; only the attribution annihilates. **No financial defect is asserted anywhere in P09** | stated for the record |
| 7 | the accounting-event identity P09 needs and the reference lacks — P09's standing blocking dependency | **UNRESOLVED — blocking** |
