# P08_ORPHAN_DUPLICATE_FINANCIAL_EFFECT_ATTACK

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T13`

Extends `16_P08_ORPHAN_DUPLICATE_POSTING_ATTACK.md` — which established the attack surface from source — with **measurement against a deployed database of 169,143 posted entries**.

## 1. Orphan financial effect — measured

An orphan is a financial effect with no business source. The test: does the posted entry carry a link to any originating object — a payment, a bank statement line, a reversed entry, a source-document reference, a tax-basis origin, or an auto-post origin?

| Population, `DB-SM`, posted entries | Count | Share |
|---|---|---|
| Total posted entries | 169,143 | — |
| **Carrying no link to any originating object** | **111,224** | **65.8%** |
| — of which are document-type entries (vendor bill, customer invoice, refund) | 27,404 | |
| — **of which are plain journal entries** | **83,820** | **49.6% of all posted entries** |
| Carrying no link **and** no reference text at all | 6,406 | |
| **Plain journal entries with no link and no reference** | **5,786** | |

**The honest reading, and the limit of this test.** A vendor bill or customer invoice **is** the business document — for those 27,404, the absence of a link to something else is expected and is not an orphan. The finding is the other group.

**83,820 posted entries are plain journal entries carrying no link to any originating object.** For these, the ledger holds a financial effect and **no object in the ledger says what caused it**. Of those, **5,786 additionally carry no reference text**, so not even a human-readable origin exists.

`FACT VERIFIED`. This is the measured form of `KRN-08`: under a manual journal the general ledger is original truth with no origin at all — and in this database that describes roughly half of all posted entries.

**What this test cannot show:** a link may be absent because the producing process never set one, not because no process existed. The test measures **recoverable provenance in the ledger**, which is precisely what an auditor has. It does not measure whether a business fact existed.

## 2. Duplicate financial effect — measured, and the detection signal is unusable

The benchmark's only duplicate-detection mechanism matches on a **reference string**, warns rather than blocks, and covers only customer and supplier documents.

| Test | Result |
|---|---|
| Posted entries sharing (reference, company, entry type) with at least one other | **33,147 entries in 4,308 groups** |
| Largest single group | **3,461 entries** sharing one reference |
| Next largest groups | 294, 240, 232, 228, 226 |

The largest groups are recurring operational patterns — a standing transfer, and per-asset depreciation runs repeating monthly. **These are almost certainly legitimate.** That is the finding.

`FACT VERIFIED`: **the only signal the system has for detecting a duplicate posting is shared by 33,147 posted entries that are not duplicates.** A detector whose positive rate is dominated by legitimate recurrence cannot distinguish a genuine double-post. The mechanism is not merely weak — in a real population it is **swamped**.

This converts `AT-01` from "duplicate detection warns rather than blocks, and covers only two document types" to a stronger and measured statement: *even where it applies, its signal is not discriminating in production data.*

## 3. The attack set, re-scored against deployment

| Attack | Source verdict | Deployment verdict |
|---|---|---|
| `AT-01` same business fact posted twice | not stopped | **not stopped, and the detection signal is swamped** (§2) |
| `AT-02` duplicate through a second book | not stopped | unchanged |
| `AT-03` duplicate import | not stopped | **the import bridge is uninstalled in 3 of 3** — not live |
| `AT-04`..`AT-06` orphan / stripped / falsified provenance | not stopped | **83,820 posted entries carry no recoverable origin** (§1) |
| `AT-07` posted entry with no lines | not stopped | not tested against data |
| `AT-10` unbalanced entry posted | not stopped | **0 occurrences** in company currency — latent, not realised |
| `AT-11` unbalanced in transaction currency | not stopped | **53 posted entries** with multiple non-offsetting foreign-currency lines |
| `AT-14` seal narrowing | not stopped | **moot — no entry carries a seal** |
| `AT-15` posted entry deleted | ordinary path refused | **retention feature absent from the deployed version** |
| `AT-16` renumbering after posting | not stopped | 0 duplicate (journal, number) observed |
| `AT-17`/`AT-17b` reach-through from outside accounting | not stopped | unchanged — both paths are in the reference layer, not custom |
| `AT-18` cross-company settlement | not stopped | **live risk: two databases carry 44 companies each** |
| `AT-20` custom access-check override | not stopped | **uninstalled or absent in 3 of 3 — not live** |
| `AT-21` settings-level ledger erase | not stopped | **INSTALLED in 3 of 3 — live** |
| `AT-22` custom re-dating utility | not stopped | **uninstalled or absent in 3 of 3 — not live** |

## 4. Net

Deployment evidence **de-escalated four attacks** (`AT-03`, `AT-14`, `AT-20`, `AT-22`) and **escalated three** (`AT-01` swamped signal, `AT-04`..`06` measured orphan population, `AT-21` confirmed installed).

The pattern that survives unchanged is the one this package has held from the start: **the controls live in application code, and the deployed configuration engages almost none of them.** The two strongest — the seal and the period lock — are switched off everywhere examined; the module that can erase the ledger outside the object layer is switched on everywhere examined.
