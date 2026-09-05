# P08_UNSEARCHED_TREE_DISCHARGE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · partial discharge of `P08-U-18`

`P08-U-18` — **32 modules installed in a deployed database exist in neither searched source tree** — was the single lifting condition on which **all four expert vetoes converged**. Two reviewers named it independently. This file discharges it in part, and what it found changes three published findings.

---

## 1. The package searched the wrong custom tree

**A third custom module tree exists on this host and was never searched. It is on the 16.0 product line — the same line as the deployed database — while the tree the package did search is on 18.0.**

| Tree | Line | Modules | Covers, of the 190 installed in `DB-SM` |
|---|---|---|---|
| Reference tree — **searched** | 18.0 | 790 | 130 |
| Custom tree — **searched** | 18.0 | 65 | 28 |
| **Custom tree — NOT searched** | **16.0** | **58** | **45** |
| A fourth tree named by a reviewer | — | **0 module manifests** | 0 |

**The unsearched tree covers more of the deployed estate than the searched custom tree does — 45 modules against 28 — and it is on the matching product line.**

**ENUMERATION.** POPULATION: the 190 modules recorded as installed in `DB-SM`. PATTERN: exact name match against every directory holding a module manifest in each tree. PATH SET: the four trees named above. UNIT: **one module**. POSITIVE CONTROL: the searched reference tree resolves 130 of the 190, so the matcher fires.

| | Count |
|---|---|
| Installed modules not in either **searched** tree | **32** *(reproduces the reviewers' figure exactly)* |
| **Newly located in the unsearched 16.0 tree** | **17** |
| **Still unlocated anywhere on this host** | **15** |

The 15 remaining are predominantly vendor enterprise-edition modules plus the two a reviewer flagged as most consequential — a numbering module and the customization container. **`P08-U-18` is reduced, not closed.** The customization container remains the residual route `44` §5 left open, and it is still `C NOT YET SEARCHED`.

Of the 17 newly located, **13 touch the ledger** by inheriting the entry, item, journal, account, numbering or currency models. **8 of those 13 are installed.**

`P08-M-16` — **a package must establish that its source tree matches the system it is describing before it describes it.** The version premise was corrected in `40` for the *reference* tree and never asked of the *custom* tree. This is the fourth instance in this programme of the evidence base itself being an unexamined claim.

---

## 2. Ledger numbering **is** overridden in deployment — three findings change

**The custom numbering module** (`CM-16`, resolved in quarantine) is **installed** in `DB-SM`. It replaces the entry's starting-sequence derivation with:

> **the journal code, then the accounting date's year, then its month, then a serial.**

It also replaces the monthly sequence pattern with a custom one requiring a four-digit year.

### 2.1 This identifies the mechanism behind `P08-F-41`

`48` §4 recorded 30 posted entries carrying a Buddhist-Era accounting date, with the bad year **burned into the entry number** — and could not explain how. **It is explained here.** The number is derived from the accounting date's year at assignment time. A date of 2567 produces a number containing 2567. **The number is a function of the date, so an unvalidated date permanently corrupts the identifier.**

`FACT VERIFIED` — 16.0 custom source, matching the 16.0 database in which the 30 entries sit.

### 2.2 It withdraws the deployed relevance of the numbering argument in `39`

`39` §3 argued that a uniqueness index on the entry number is *"structurally incapable of colliding"* because the numbering design guarantees distinctness — reasoning from **18.0 reference source**.

**The deployed system does not use that numbering.** It uses a custom derivation from journal code and accounting date. Whether that derivation preserves the distinctness property **was not assessed here**.

`P08-CONTRA-41`. The argument is **not contradicted — it is unscoped.** It describes a numbering scheme the measured database does not run. `C NOT YET SEARCHED` for the deployed scheme's collision behaviour.

### 2.3 It bears on the gap analysis a reviewer performed

A reviewer inferred 6,312 consumed-and-absent entry numbers by decomposing numbers into year, month and serial, **excluding prefixes whose format defeated the decomposition**. That decomposition is now known to be **the deployed module's own format**, which raises the reviewer's class-C inference — but the alternative explanation the reviewer declined to exclude, a manually set number, is **not** excluded by this file either. **Class `C` stands.**

---

## 3. A tax-period carrier **exists, is populated, and never reaches the level the statements read**

**The custom tax-period module** (`CM-17`, resolved in quarantine) is **installed** in `DB-SM`. It adds a tax-period date **to the entry** and a tax-period date **to the journal item**.

**This contradicts a published P08 position and answers a peer handoff P08 had recorded as open.**

### 3.1 What P08 published

`45` hop 10 and `36` §1 state that the period is a date range on a company record and that **no carrier distinguishes a tax period from the accounting date.** P07 handed P08 `X-11` and `X-12` on exactly this point — *if the tax point becomes the selector, P08 must accept that a tax fact and its accounting entry can fall in different periods* — and P08 answered that the platform **cannot express it today.**

**P08 was wrong. The deployed system expresses it, and has been expressing it for 61,157 posted entries.**

### 3.2 What the deployed data shows

**ENUMERATION.** POPULATION: 169,143 posted entries and 447,384 items in `DB-SM`. PATTERN: non-null test on the carrier columns, then comparison against the accounting date. PATH SET: the entry and item extracts. UNIT: **one posted entry**, then **one item**. POSITIVE CONTROL: the accounting date column is populated on 183,590 of 183,590 rows, so the non-null test fires.

| Measurement | Value |
|---|---|
| Posted entries carrying a tax period | **61,157 — 36.2%** |
| — where it **differs from the accounting date** | **5,228 — 8.5% of those carrying one** |
| — where it falls in a **different month** | **1,316** |

**And the propagation to the item is broken in a specific and consequential way:**

| Of the 61,157 entries carrying a tax period | Entries |
|---|---|
| **Every item carries it** | **0** |
| **No item carries it** | **43,018** |
| Only some items carry it | 18,139 |

**Not one entry propagates its tax period to all of its items.**

### 3.3 Why this is the sharpest instance of the package's central finding

`41` and `45` established that **the statements aggregate the item**, and that provenance and meaning sit above it. Here the same defect appears in its most consequential form yet, and this time it is a **statutory** dimension:

> **The tax period is known to the entry for 36.2% of posted entries and is unavailable at the item level for every single one of them.** A tax fact and its accounting entry can already fall in different periods — 1,316 times in different months — and nothing that reads the item can tell.

`FACT VERIFIED` — 16.0 custom source and 16.0 data, matching layers.

### 3.4 Disposition

| Item | Movement |
|---|---|
| `45` hop 10, `36` §1 — *"no carrier distinguishes a tax period from the accounting date"* | **`P08-CONTRA-42`. WITHDRAWN for the deployed system.** It holds for the reference kernel and is false for the measured estate |
| P07 `X-11`, `X-12`, and the dependency `P07-D-22` | **ANSWERED, and returned to P07 with a correction of P08's earlier answer.** A carrier exists, is partially populated, is inconsistent with the accounting date on 5,228 posted entries, and is absent at item level on all of them |
| `P08-BD-17` | **SHARPENED.** The question is no longer only whether a period control should be required, but **what a partially populated statutory period dimension means for a filed figure** |
| `P08-RQ-KRN-03` | **NEW.** *A period attribution that governs a statutory obligation must sit on the financial fact the statements aggregate, and must be complete over the fact set it claims to cover.* |

---

## 4. What remains open

| Item | Class |
|---|---|
| The 15 modules unlocated on this host, including the customization container able to carry arbitrary models and server-side automation | **GATING — `C NOT YET SEARCHED`.** `P08-U-18` is reduced from 32 to 15 and is **not closed** |
| The remaining 11 ledger-touching modules in the newly-found tree, examined only for what they inherit | `C NOT YET SEARCHED` |
| Whether the deployed numbering derivation preserves collision-freedom | `C NOT YET SEARCHED` — `P08-CONTRA-41` |
| Whether the rate-source module writes the rate master | `B NOT FOUND IN SEARCHED SCOPE` — the author's pattern found no direct write; the inherited update path was not traced |
| Two further Thai withholding-tax modules and a summarizing-bills module, all installed, none examined | `C NOT YET SEARCHED` |

**The four expert vetoes are not lifted by this file.** Three of their conditions move; the gating condition narrows from 32 modules to 15 and remains open. **P08 does not lift its own veto, and does not represent a reduced blocker as a closed one.**
