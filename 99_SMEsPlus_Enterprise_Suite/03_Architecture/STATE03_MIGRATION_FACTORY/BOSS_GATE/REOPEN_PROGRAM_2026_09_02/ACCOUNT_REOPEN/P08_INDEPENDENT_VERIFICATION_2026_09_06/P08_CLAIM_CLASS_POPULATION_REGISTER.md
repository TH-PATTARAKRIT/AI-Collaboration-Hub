# P08_CLAIM_CLASS_POPULATION_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-003]` · frozen surface `00ccd66`

The mandate names nine claim classes. **For each: the population as this verifier enumerated it, not as the package asserted it.**

Column key: `Correction/Claim ID | Claim Class | Original Location | Current Location(s) | Unit | Denominator | Independent Method | Result | Handoff Impact | Disposition`.

---

## 1. Class-to-correction mapping, enumerated

**POPULATION:** the 32 correction ids `-43` … `-74` at the frozen SHA. **UNIT:** one correction id. **CONTROL:** every id resolves to a definition-bearing statement (32 of 32).

| Class (mandate §4) | Correction ids | Ids in this class |
|---|---|---|
| 1 · Entry-number uniqueness | `-62` | 1 |
| 2 · Posted-entry finality / immutability | `-54`, `-56`, `-70`, `-71` | 4 |
| 3 · Deletion control | `-55`, `-73` | 2 |
| 4 · Preventive-control denominator | `-43`, `-65`, `-66` | 3 |
| 5 · Version discipline | `-67`, `-69`, `-72` | 3 |
| 6 · `VERIFIED ABSENCE` / structural claims re-scoped | `-68`, `-53`, `-74` | 3 |
| 7 · Predicate / unit / instrument / scope corrections | `-44` … `-52`, `-57` … `-64` | 17 |
| 8 · Candidate handoffs | `-48`, `-53`, `-57`, `-58`, `-59`, `-60`, `-62`, `-63`, `-65`, `-68`, `-72`, `-73` (handoff-bearing) | 12 |
| 9 · Vetoes and lifting conditions | none — the vetoes are recorded outside the correction family | 0 |

**Sum of class memberships exceeds 32 because ids belong to more than one class.** Stated because a class table whose rows sum past its population is a unit conflation unless declared — and here it is declared.

## 2. The one arithmetic question the mandate raises

The prompt's §2 records *"four independent re-derivations found **one arithmetic error**"*. **The frozen package says the opposite**: `61` §1 states *"not one arithmetic error was found"*, and `62` §3 repeats *"no arithmetic error"*.

**Verifier finding `IVR-F-07` · MATERIAL.** The two are irreconcilable as written, and **the package's own record is the weaker of the two.** The audited round's challengers reported at least four figures as `CONFIRMED WITH CORRECTION` — a ratio stated as 175× where the underlying division gives 182×, a settlement population stated as 63,779 where the three databases sum to 63,782, an all-zero entry count of 38 where the "both frames" predicate yields 36, and a mis-prefix count of 4,895 against a re-run of 4,995.

**These are arithmetic or rounding corrections, and the package's headline "not one arithmetic error was found" does not survive its own challenge record.** The claim is **CONTRADICTED**, and it matters because it is the sentence the package uses to argue that only its interpretation layer failed.

## 3. CURRENT versus HISTORICAL text — the separation the mandate requires

**Where the package applied a correction in place**, the superseded wording is quoted and struck. **Verified: this holds wherever an in-place correction was made.**

**Where the package appended a correction section**, the superseded wording **remains live in the standing table above it**. **Four instances — `IVR-F-03` … `-06`.** For those four, `CURRENT` and `HISTORICAL` are **not separated in the artefact**, and a reader consuming the summary receives the historical form.

| Artefact | Standing text | Status |
|---|---|---|
| `55` §4 | *"Artefacts audited 22 · Contaminated 2 · Domains 11 · `DOMAIN PURITY PRESERVED`"* | **HISTORICAL, presented as current** |
| `54` §5 | *"CANDIDATE INPUT 11"* | **HISTORICAL, presented as current** |
| `53` per-question dispositions | four lines claiming five `UNRESOLVED` items | **HISTORICAL, presented as current** |
| `57` disposition | *"one named `UNRESOLVED` (the deployed reporting module)"* | **HISTORICAL — the item was closed in the same file** |

## 4. Load-bearing claims this verifier could NOT re-derive itself

Declared so the register is not read as broader than it is.

| Claim | Why not re-derived here | Where it is being tested |
|---|---|---|
| All deployed counts (entry-number collisions, denominators, origin predicates, tax-period decomposition, settlement figures) | They rest on extracts produced by the party under audit; re-derivation from the original dumps is required | the database challenge |
| Reproducibility of each corrected claim from the artefact alone | requires per-claim predicate reconstruction | the code/instrument challenge |
| Outbound handoff wording against evidence | requires the full handoff set | the integration challenge |
| Finality and period-object semantics | requires source re-reading across three lines | the functional challenge |

**Until those return and are re-checked, this register's substantive coverage is the correction-surface bookkeeping, not the accounting claims themselves.**
