# P08_SUPPORTED_INTERPRETATION_CLOSURE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · Phase C · `CP-T04`

## 1. The evidence base changed, and that is itself the finding

The prior session recorded, in its own manifest: *"Database — no. Runtime — no. Nothing was executed."* That statement was true of what the session had looked for, and **false of what was available.**

**Three deployed database dumps exist on the evidence host and are readable.** This continuation located and read them.

| Ref | Scale | Readable |
|---|---|---|
| `DB-SM` | **447,384 journal items · 183,590 entries · 169,143 posted · 339 accounts · 21 journals · 1 company** | yes |
| `DB-BK` | 563 journal items · 16 entries · 544 accounts · 43 journals · 44 companies | yes |
| `DB-EV` | 15 journal items · 6 entries · 544 accounts · 44 companies | yes |
| — | a fourth dump | not readable by the archive reader |

**Method, and its limits.** The dumps were read with an offline archive reader that emits table data as text. **No database server was started. No write of any kind was performed. Nothing was installed, migrated or deployed.** This is read-only evidence acquisition, and it is bounded: three databases are three databases, not the deployed estate.

This is the second time in this programme that a session declared "source-only" without having searched for database evidence that was present on the host. It is recorded as a method finding, `P08-M-06`.

## 2. Findings converted to `FACT VERIFIED` by database evidence

| ID | Was | Now | Evidence |
|---|---|---|---|
| `JPM-20` | The gapless counter is declared and nothing writes it — source-only | **`FACT VERIFIED`** | **0 of 169,143 posted entries carry a counter value**, in 3 of 3 databases |
| `JPM-17` | The tamper seal is opt-in per book | **`FACT VERIFIED`, and materially worse than "opt-in"** | **0 of 64 journals have it enabled; 0 of 169,143 posted entries carry a seal.** The seal is not merely optional — **it is not in use in any database examined** |
| `AT-21` / `P08-T0-08` | A settings action erases ledger tables by direct statement; **deployment status unknown** | **`FACT VERIFIED` — the module is INSTALLED in 3 of 3 databases** | module registry |
| `PC-07` | Five lock dates exist and constrain posting | **`FACT VERIFIED`, and unused** | **0 of 89 companies have any fiscal-year lock set**, in 3 of 3 databases |
| `JPM-08` / `AT-11` | The balance assertion sums company currency only, so an entry can be unbalanced in its transaction currency | **`FACT VERIFIED` with a population** | **1,851 posted entries in `DB-SM` carry a non-zero transaction-currency sum.** See §4 for the honest qualification |
| `JPM-28` | Retention is a company option that is off by default | **`FACT VERIFIED`, and stronger** | **the retention column does not exist in any of the 3 databases** — the feature is absent from the deployed version, so there is nothing to switch on |

## 3. Findings **de-escalated** or retracted by database evidence

Recorded with the same weight as the escalations.

| ID | Claim | Database result | Disposition |
|---|---|---|---|
| `AT-20` | A custom module overrides the framework access check on the universal base object, defeating permission and isolation | **uninstalled in 2 databases, absent from the module registry of the third** | **NOT LIVE in any database examined.** The code defect stands on record; its exploitation in these deployments is `CONTRADICTED`. Severity for these deployments is withdrawn |
| `AT-22` | A custom re-dating utility discards entry numbers | **uninstalled or absent in 3 of 3** | **NOT LIVE in these deployments** |
| `AT-03` / `L-24` | A bulk import bridge creates entries with operator-supplied numbers | **uninstalled in 3 of 3** | **NOT LIVE in these deployments** |
| `AT-10` | An unbalanced entry can be posted, because the assertion is suppressible | **0 unbalanced posted entries in company currency, across 169,143 posted entries** | **The mechanism stands (`FACT VERIFIED` from source); the occurrence is zero.** The risk is **latent, not realised**, in these databases. `SUPPORTED INTERPRETATION` on exploitability is unchanged — a zero occurrence is not proof the path is closed |
| `AT-15` | Posted entries hard-deleted | **0 duplicate or missing (journal, number) pairs detected among posted entries** | no positive evidence of deletion found; the test is weak (a deleted entry leaves no row to count) and is recorded as such |
| `AID-02` | No database uniqueness on the account code | **0 duplicate account codes in `DB-SM`** | the absence of a constraint is confirmed from source; the data happens to be clean. Both facts are recorded — a clean population is not a control |
| `REC-15` | Stored open amounts can be overwritten out of step with the matches, by a direct-statement toggle path | **0 drifting lines of 100,580 settled lines checked**, reconstructed against 63,773 partial settlements | **Mechanism stands (source-verified); occurrence is zero.** The same shape as `AT-10`: latent, not realised, in this database. The claim is bounded accordingly and is no longer carried as an active data-integrity concern for these deployments |

## 4. The transaction-currency imbalance, stated precisely

**1,851 posted entries in `DB-SM` have a non-zero sum of transaction-currency amounts within one currency.** Characterisation, because the raw number would over-claim:

| Property | Count |
|---|---|
| Posted entries with a non-zero transaction-currency sum | **1,851** |
| Of which entry type is a manual or system journal entry (not an invoice) | **1,851 — all of them** |
| Of which **only one line** carries the foreign currency | **1,798** |
| Of which **two or more** foreign-currency lines exist and still do not offset | **53** |

The 1,798 single-line cases are a shape that **cannot** self-offset and may be entirely intended — a denominated leg against a reporting-currency counter-leg. They are **not** claimed as defects.

**The 53 are the population the missing assertion would have caught.** They carry two or more lines in the same foreign currency whose amounts do not sum to zero, in a posted entry. Sampled names indicate depreciation and opening-balance style entries.

That **none of the 1,851 is an invoice** is itself consistent with the source finding: invoice-shaped documents are built by a producing module that balances both frames; manual and system entries meet the fewest controls.

`FACT VERIFIED`: the assertion sums one currency frame only, and a real deployed database contains 53 posted entries that are unbalanced in the other frame.

## 4A. Two further findings measured at scale

### `REC-05` — retroactive settlement, now quantified

The settlement record carries **no event date**; its as-of date is the later of the two documents it matches. The prior session recorded the consequence — re-running a past period's ageing after a back-dated settlement returns a different answer — as a mechanism. It is now measured.

| Measurement over 63,773 settlements in `DB-SM` | Value |
|---|---|
| Recorded **after** their own as-of date | **29,595 — 46.4%** |
| Recorded more than 30 days after | **14,502 — 22.7%** |
| Recorded more than 90 days after | 4,818 — 7.6% |
| Recorded more than **a year** after | **710 — 1.1%** |
| Largest gap | **594 days** |
| Settlements that generated an exchange-difference entry | 3,169 |

`FACT VERIFIED`. Nearly a quarter of all settlements in this database were recorded more than a month after the date at which they take effect for ageing purposes, and there is **no stored date recording when the settlement was actually made** other than the row's own creation stamp. A prior-period ageing report re-run today is not the report that was run then, and nothing in the accounting data explains the difference.

### `JPM-04` / `PC-17` — backdating, now quantified, in a database with no period lock set

| Measurement over 169,143 posted entries in `DB-SM` | Value |
|---|---|
| Posted **after** their accounting date | 88,437 — 52.3% *(ordinary and expected)* |
| Posted more than 30 days after their accounting date | 28,847 — 17.1% |
| Posted more than 90 days after | 14,017 — 8.3% |
| **Posted more than a year after their accounting date** | **6,418 — 3.8%** |
| Largest gap | **6,701 days** |
| Accounting date in the **future** relative to creation | **22,162 — 13.1%** |

`FACT VERIFIED`. **6,418 posted entries carry an accounting date more than a year before the moment they were written** — that is, they were posted backwards across at least one fiscal-year boundary. This database has **no fiscal-year lock set on any company**, so nothing in the period-control layer was engaged for any of them.

This is the concrete form of the period finding: the control exists, is not configured, and 6,418 entries were written into prior fiscal years. The package does not assert that any of these is improper — a late-posted entry may be entirely legitimate. What is verified is that **no control was in a position to distinguish**.

## 5. Findings the database evidence could **not** settle

| ID | Why not |
|---|---|
| `P08-U-01` context-key reachability end to end | Needs an executed call against a running instance, not a dump. **`HOLD — RUNTIME EVIDENCE REQUIRED`** |
| ~~`REC-15` residual drift~~ | **NOW SETTLED — see §3.** The test was run: stored residual reconstructed from 63,773 partial settlements across **100,580 settled lines**. **Zero lines drift.** |
| `JPM-16` line re-parenting | A historical mutation leaves no trace in a snapshot. **`HOLD — RUNTIME EVIDENCE REQUIRED`** |
| `FR-23` statement re-run instability | Requires running the report engine twice against changed master data. **`HOLD — RUNTIME EVIDENCE REQUIRED`** |
| `AT-14` seal narrowing | Moot in these deployments: no entry carries a seal |

## 6. Net effect

| Category | Count |
|---|---|
| Converted to `FACT VERIFIED` by database evidence | **8** |
| De-escalated, retracted or bounded by database evidence | **7** |
| Still requiring runtime evidence | **3** |
| New material finding produced by the database evidence | **5** — the seal is unused; no lock is set anywhere; the retention feature is absent from the deployed version; 22.7% of settlements are recorded over a month after their effective date; and 6,418 posted entries are backdated across a fiscal-year boundary |

**The most consequential single result:** in the deployed databases examined, **the two controls this package treated as the strongest — the tamper seal and the period lock — are not in use at all**, and the retention control does not exist in the deployed version. Every mitigation credited to them elsewhere in this package does not apply to these deployments.

**The second most consequential:** the custom module that can erase the ledger by direct statement, whole-table and without a company predicate, **is installed in all three**.
