# 17 — LEVEL 10: ACCOUNTING MIGRATION SEMANTIC REQUIREMENTS

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

> **Conceptual only.** No migration code, no mapping, no execution. This Level states what a
> migration must be *able to preserve*, derived from the Wave A evidence.

## 1. What the reference model provides, and what it does not

| Element | Reference provision | Evidence |
|---|---|---|
| Opening balances | an ordinary posted entry, balanced to current-year earnings | `EV-017` |
| Per-account opening figures | computed fields writing into that single entry | `EV-017` |
| "Accounting is initialised" | defined as: that entry exists and is posted | `EV-017` |
| Open receivables and payables | must be migrated as **individually reconcilable items**, or later settlement cannot match them | `EV-014` |
| **Provenance of any migrated figure** | **none — no carrier exists** | `EV-017` |
| **Historical entries before the opening date** | no mechanism; the opening entry is a single summary | `EV-017` |
| **Continuity of tamper-evidence across migration** | **impossible — the chain is keyed on storage row identifiers** | `COR-12` |
| Historical currency of migrated items | the item carries a transaction currency; **the rate that produced the legacy valuation is not carried** | `EV-013`, `EV-018` |
| Retained earnings at migration | balanced into current-year earnings, **not into a retained-earnings account** | `EV-017` |

## 2. Migration semantic requirements

| # | Requirement | Why — derived from evidence |
|---|---|---|
| `MG-01` | Every migrated fact carries **provenance**: source system, source identifier, extraction run, and the date of extraction. | No carrier exists (`EV-017`); without it, a migrated balance cannot be defended to an auditor |
| `MG-02` | Every migrated fact carries an **idempotency key**, so re-running an extraction cannot double-post. | No duplicate-event guard exists (`XM-01`) |
| `MG-03` | Open items migrate **individually**, never as summarised balances, and carry counterparty, due date, currency, original amount and residual. | Settlement matches items, not balances (`EV-014`); ageing needs the due date |
| `MG-04` | A migrated open item's **residual is asserted, and must be reconcilable to its original amount less prior settlements**. | Residual is stored-derived (`EV-014`) and nothing bounds it (`COR-09`) |
| `MG-05` | The **valuation rate** that produced each legacy company-currency amount is preserved as a fact, not re-derived. | Re-deriving would apply today's rate to a historical measurement; and a missing rate silently converts at par (`COR-14`) |
| `MG-06` | **Retained earnings and current-year earnings are migrated as distinct positions**, and the choice between them is explicit. | The reference balances everything to current-year earnings (`EV-017`), which is wrong for any migration after year one |
| `MG-07` | Account **identity mapping is recorded permanently** — legacy account to SMEsPlus account — and is never destroyed by later consolidation. | Merge deletes the predecessor with no record (`COR-08`) |
| `MG-08` | Historical **reporting continuity** is stated explicitly: which periods are reportable from migrated data, at what granularity, and which are not. | The opening entry is a summary; anything before it is unreportable in detail (`EV-017`) |
| `MG-09` | The migration's **own accounting events are identifiable as such**, and distinguishable from operational postings, permanently. | Otherwise a migration correction is indistinguishable from a business transaction |
| `MG-10` | **Tamper-evidence is re-established after migration on business identity**, and the migration itself is attested. | The reference chain cannot cross the boundary (`COR-12`) |
| `MG-11` | Migrated **tax positions and carry-forwards** are stated as facts with provenance, not recomputed. | `WAVE-D TAX` owns the content; the requirement is Wave A's |
| `MG-12` | **Asset and deferred-recognition dependencies** are reconciled to the ledger opening position before it is asserted. | Prior sessions record both domains as unresolved (`XM-04`, `XM-05`) |
| `MG-13` | The opening position is **locked by a hard, irreversible lock** once accepted. | The one unconditional control the reference offers (`EV-008`) |
| `MG-14` | An **opening reconciliation** is produced and retained: legacy trial balance to SMEsPlus opening balances, per account, with differences explained. | Nothing in the reference requires or retains this |

## 3. Dependencies that must be resolved before a migration can be designed

| # | Dependency | Status |
|---|---|---|
| `MD-01` | Retained-earnings treatment at year end | `UNKNOWN` — decision `CL-02`, Boss |
| `MD-02` | Whether a closed period is a record or a date | `UNKNOWN` — decision `CL-01`, Boss |
| `MD-03` | Cost-of-sales semantics | `PRIOR` — `PARTIAL RESOLUTION`; three questions `NOT DECIDABLE` |
| `MD-04` | Asset depreciation computation mode in the source system | `PRIOR` — recorded there as the top open blocker |
| `MD-05` | Thai statutory retention and filing-history requirements | `HOLD / EVIDENCE REQUIRED` — Accounting-Tax track |
| `MD-06` | Standard-template versus tenant-specific chart distinction | `UNKNOWN` — no reference answer exists (file 16) |

`RECOMMENDATION:` `MD-01` and `MD-02` are prerequisites, not parallel work. A migration cannot state
its opening equity position without knowing whether year-end results are posted or computed.

## CHECKPOINT L10

| Item | Record |
|---|---|
| Scope completed | Reference provision assessed; 14 migration semantic requirements; 6 blocking dependencies |
| Verified findings | The reference provides a single summarised opening entry with no provenance carrier, no historical detail, and tamper-evidence that cannot cross the boundary |
| Contradictions | — |
| Unknowns | Six dependencies, two of them prerequisites |
| Risks | Migrating retained earnings into current-year earnings, as the reference does, misstates equity for any migration after the first year |
| Next research target | Level 11 — reconciliation proof |

`CHECKPOINT L10 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
