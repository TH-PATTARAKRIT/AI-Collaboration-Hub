# P08_VERSION_PREMISE_CORRECTION

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001`

## 1. The defect

Phase C acquired database evidence and used it to confirm, quantify and de-escalate findings that had been derived from source. **The source and the databases are different product versions, and the session did not check before drawing cross-layer conclusions.**

Verified by the author against the module registry of each database:

| Evidence | Product line |
|---|---|
| `REF18` — the source root all P08 findings are derived from | **18.0** |
| `DB-SM` — the 447,384-item database carrying every scale measurement | **16.0** (189 of 190 installed modules at 16.0.x; the accounting kernel at 16.0.1.2) |
| `DB-BK` | **19.0** |
| `DB-EV` | **19.0** |

**No deployed database in the evidence set runs the version this package's source findings describe.**

Structurally corroborated: `DB-SM` carries journal-item columns that no longer exist by 19.0, and lacks several that 18.0 and 19.0 have. Two fields this session tested — a cost-of-sales origin pointer and an import marker — **do not exist as columns in `DB-SM` at all**, though both are declared in `REF18`. They are post-16 additions.

## 2. What survives unchanged

**Every measurement is a fact about the data it was taken from, and none is withdrawn.** These stand exactly as reported:

- 0 unbalanced posted entries in reporting currency, of 169,143
- 1,851 posted entries unbalanced in transaction currency; 53 with multiple non-offsetting foreign-currency lines
- 0 residual drift across 100,580 settled lines and 63,773 settlements
- 6,418 posted entries backdated more than a year; largest gap 6,701 days
- 22.7% of settlements recorded more than 30 days after their effective date
- 83,820 posted entries with no link to any originating object; 5,786 with no reference either
- 33,147 posted entries sharing a reference with another
- 0 of 13,814 bank statement lines carrying any deduplication key
- 0 of 89 companies with a period lock set; 0 of 64 journals with the tamper seal; 0 posted entries carrying a seal or a gapless counter
- module installation states

## 3. What must be re-scoped

Every sentence of the form *"control X exists in source **and** is switched off in deployment"* crossed a version boundary silently. Each is re-stated as two facts with their versions attached:

| Claim as written in Phase C | Corrected form |
|---|---|
| "the retention feature is absent from the deployed version, confirming the source finding" | **In 18.0 source, retention is a company option with no default. In the 16.0 and 19.0 databases examined, the column is absent.** Whether it is absent because the feature post-dates 16.0, was renamed by 19.0, or was never installed is **`UNRESOLVED — EVIDENCE REQUIRED`**. The two facts are not one finding |
| "the irrevocable lock column does not exist in the production-scale database" | **True of 16.0.** It is present in both 19.0 databases. This is a **version difference**, not a deployment choice, and the earlier wording implied the latter |
| "the tamper seal is opt-in in source and enabled on 0 of 64 journals" | Both halves stand; the inference chain crosses 18.0 → 16.0/19.0 and must say so |
| "the event identity exists in source and is populated on 0 of 13,814 rows" | Both halves stand. The 16.0 schema **does** carry both key columns, so the zero is a genuine population fact, not a schema absence — **this one survives the re-scoping intact** and is the strongest of the group |

## 4. What this vindicates

The programme has a standing blocker — recorded before this session — that **the reference implementation is not stable across the versions SMEsPlus spans**, and a standing unknown asking **which reference root SMEsPlus targets**. This session treated that as a methodological caution about source roots. It is not only that: **it is a live defect in cross-layer reasoning**, and this session committed it within hours of re-affirming the root-set discipline.

`P08-M-08` — **Evidence layers carry versions, and a finding that spans two layers must state the version of each.** Declaring POPULATION, PATTERN, PATH SET and UNIT is not sufficient when the layers are of different vintages.

## 5. Disposition

| Item | Action |
|---|---|
| Phase C measurements | **stand**, with the database version attached to each |
| Phase C cross-layer inferences | **re-scoped**, per §3 |
| The eight source-to-report traces | they describe **18.0 reference design** and are **not** evidence about the code that produced the `DB-SM` rows. Labelled accordingly |
| A 16.0 source tree | **not present on this host** within the searched path set — `C NOT YET SEARCHED` beyond it |
| 60 of 190 installed `DB-SM` modules | outside `REF18` entirely. Their behaviour is unexamined and is `C NOT YET SEARCHED` |
| `P08-BD-05` (which root SMEsPlus targets) | **sharpened and made urgent**: the deployed estate spans at least 16.0 and 19.0, and the package's source analysis is 18.0 — three versions, no declared target |
