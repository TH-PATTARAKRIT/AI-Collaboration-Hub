# P07 — FINDINGS REGISTER

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 0. Why This File Exists

Independent challenge established that the package cited 39 distinct `P07-F-nn`
identifiers, used them as the entire content of the finding column in four registers, and
**defined none of them anywhere**. Every finding reference was a dangling pointer. This
register is the definition of record. It was written after the challenge round, so each
entry carries its post-challenge state, not its draft state.

## 1. Severity and Status Vocabulary

| Severity | Meaning |
|---|---|
| `S1` | Statutory output is wrong, absent, or silently empty |
| `S2` | Statutory output is derivable but not reproducible, or a boundary is unenforced |
| `S3` | Correctness or maintainability defect with no direct statutory effect |

| Evidence state | Meaning |
|---|---|
| `SRC` | Derived from source, complete chain, not executed (`P07-U-02` applies to all of them) |
| `SRC-CHAL` | Source-derived and independently re-verified by an adversarial reviewer reading the same code |
| `INF` | Inference with a complete mechanism but one unverified link |
| `MEAS` | Measured by enumeration over a declared population |

**Superseded at r-final.** Findings `P07-F-01`, `-F-03`, `-F-37`, `-F-40`, `-F-42` are now **runtime-verified** against a deployed database of the declared generation; `P07-F-51` is refined by it. See `22_P07_RUNTIME_EVIDENCE.md`, which also records that this session's own "no database was queried" boundary was false and concealed a dump inside its own declared PATH SET. All other findings remain source-derived.

## 2. Findings

| ID | Severity | Statement | Evidence state | Where argued |
|---|---|---|---|---|
| `P07-F-01` | `S1` | The two SMEsPlus statutory VAT registers admit a row only if the raw stored value of the tax group's name equals the dict `{'en_US': 'VAT 7%'}`. Because that name is a translatable field, any Thai value in it takes the predicate out. **The published trigger (*installing Thai*) is REFUTED and the consequence was never measured — `P07-F-72`, `P07-F-73`, `22 §17`: the real condition is the chart loading while Thai is already active (install order), and the defect fires only in an identity holding 2–3 VAT-7% tax lines while the two deployments holding 5,202 and 32,672 do not fire. Severity stays `S1`; the basis is prospective with a measured magnitude.** | **VERIFIED**, deployment-dependent. Base restated at `22 §7.4`: **1 database identity of 3 examined, observed at two dates a month apart** (persistence established; "2 of 4" counted snapshots as identities) | `02 §5.1`, `22 §4.1`, `§7.1`, `§7.4` |
| `P07-F-02` | `S1` | Tax-period membership is selected by the accounting date. A tax-point field exists and is displayed on the register; the predecessor implementation substituted it into the period predicate and that substitution was removed in the v19 migration. | `SRC-CHAL` (diffed independently) | `04 §4` |
| `P07-F-03` | `S2` | The line-level tax-period field is written only in `create`, never on `write`, and no report, compute, domain or SQL reads it; its sole reader is a hidden list column. | `SRC-CHAL` | `04 §3` |
| `P07-F-04` | `S1` | All three SQL sites of the SMEsPlus registers inner-join the partner, dropping partnerless supplies — which is the abbreviated tax invoice case the statute provides for and the vendor report explicitly handles. | `SRC-CHAL` | `01 R-V-14` |
| `P07-F-05` | `S1` | Zero-rated and exempt portions of a mixed-rate invoice appear on neither register: excluded from the main one by the group predicate, and from the zero one by a move-level `amount_tax = 0` test. | `SRC-CHAL` | `02 §4 V-D-06` |
| `P07-F-06` | `S2` | "Thai branch" exists in four representations across two scopes and is used inconsistently by four statutory outputs; the company-scope filing attribute is read by none of them. | `SRC-CHAL` | `20 §6`, `11 P07-C-02` |
| `P07-F-07` | `S1` | No credit- or debit-note class, and no original-tax-invoice reference, exists in the Thai reporting layer, which s.86/9 and s.86/10 require. | `SRC` | `05 §1`, `08 §2` |
| `P07-F-09` | `S2` | The statutory filing unit is the place of business; the system files per company, optionally grouped across companies, with no branch dimension. | `SRC` | `01 R-V-21` |
| `P07-F-10` | `S1` | Both PND exports recompute the withheld amount as `rate × base / 100` rather than reading the posted amount, so the filing figure and the ledger figure are independent computations of one fact. | `SRC-CHAL` | `03 §3 W-C-03` |
| `P07-F-11` | `S1` | The withholding actually posted is reported by neither branch of the PND query; the originating bill is reported in its place, on the bill's date. | `SRC-CHAL` (both exclusion mechanisms verified independently) | `03 §3` |
| `P07-F-12` | `S1` | A partial payment causes the whole document's withholding to be reported, because the branch predicate is `payment_state != 'not_paid'`. | `SRC-CHAL` | `03 §3 W-C-02` |
| `P07-F-13` | `S1` | The PND income type is derived from the tax rate through a four-value mapping; every other rate emits an empty classification. | `SRC-CHAL` | `03 §4 W-K-01` |
| `P07-F-14` | `S2` | The condition of withholding is the hard-coded literal `'1'`; the certificate's own condition field is not read by the export. | `SRC-CHAL` | `03 §4 W-K-02` |
| `P07-F-15` | `S1` | PND3 versus PND53 is decided by a contact-structure flag plus a case-insensitive substring test against a translatable tag label, read from the first element of a collection with no declared order. There are **four** divergent implementations of this same determination in the declared set. | `SRC-CHAL` | `03 §4 W-K-03`, `§4.2` |
| `P07-F-16` | `S1` | Restated after challenge. **Posting layer:** a base-application guard silently discards the Thai withholding line when both withholding frameworks act on one payment — after the payment amount has already been reduced — producing silent under-recognition. **Reporting layer:** no guard, so the vendor path's real tax lines land in PND branch 1 while the same invoice is reported by branch 2. Conditional on a deliberate install: no Thai module depends on the vendor framework. | `SRC-CHAL` | `03 §6.1` |
| `P07-F-18` | `S1` | The withholding master record conflates a `PLATFORM` statutory reference with a `COMPANY` financial binding, and its company ownership is taken from the acting session although the source tax carries a required company. No `check_company` on the account binding. | `SRC-CHAL` | `20 §4` row 6 |
| `P07-F-19` | `S2` | The s.50 bis certificate — a record with a five-year retention obligation — is unlinkable by the billing group; the creation wizard and both WHT report models are granted full create/write/unlink to every internal user; the withholding master record is likewise unlinkable by the billing group. | `SRC-CHAL` | `20 §5` row 13 |
| `P07-F-20` | `S3` | `l10n_th_withholding_tax_multi` declares a dependency absent from the declared source set, so multiple withholding taxes per payment is not installable from it. Set-composition artefact — two same-generation roots outside the declared set do contain it. | `MEAS` | `12 P07-D-01`, `13 §2.1` |
| `P07-F-21` | `S2` | Form coverage is inconsistent across four layers: PND 54 has a general-ledger account and nothing else; PND 1 has an account and a certificate type; PND 3a a certificate type only; PND 2 nothing. | `MEAS` | `03 §4.1` |
| `P07-F-26` | `S1` | The Thai tax invoice is not a document object: no identity, no own number, no issuance event, no copy. The title substitution covers one of thirteen title states. | `SRC-CHAL` | `05 §2`, `§2.1` |
| `P07-F-27` | `S3` | Two modules override `create` with an `@api.model` decorator while handling a list, which is not the multi-create contract of this ORM generation. | `SRC` | `05 §3`, `08 A-13` |
| `P07-F-30` | `S3` | The national statutory catalogue, a `PLATFORM` reference, is instantiated per company and independently mutable there; one of those mutable labels is used as a statutory report predicate. | `SRC` | `20 §3` row 1 |
| `P07-F-34` | `S2` | The shipped descriptions of the two VAT settlement accounts are transposed relative to the roles the repartition and tax-group data assign them, in both English and Thai. Documentation defect, not a posting defect. | `SRC-CHAL` (confirmed precisely) | `06 §4` |
| `P07-F-35` | `S3` | The sale-side and purchase-side zero-rate registers render the same statutory book with different column sets (9 against 11). | `SRC-CHAL` (both sides counted independently) | `07 §3` |
| `P07-F-36` | `S1` | Restated after challenge. The reported statutory figure is a render-time computation over live master data, so **no filed figure is reproducible**; at least seven ordinary non-privileged actions change an already-filed report without touching the ledger, two of them rewriting monetary amounts and classifications. | `SRC-CHAL` | `08 §4` |
| `P07-F-37` | `S2` | Thailand registers one generically-named return type on a filing framework that 118 localisation modules provision, sets none of its data attributes, and registers none of its three withholding returns. Workflow and deadline are inherited by computation, so the deadline shown is generic and unrelated to the statutory date. | `MEAS` + `SRC-CHAL` | `08 §5` |
| `P07-F-38` | `S2` | Fiscal position / tax mapping is entirely unprovisioned for Thailand — no template, no populated mapping column — and the mapping filter is commented out on all four statutory registers. Peer baseline 94 of 126 chart-shipping localisations. | `MEAS` (ratio corrected after challenge) | `12 §5` |
| `P07-F-39` | `S2` | The cross-company tax-unit mechanism the Thai registers opt into carries no tenant constraint of its own, and two of its operations walk an unbounded company search. | `SRC` | `20 §6` row 19 |
| `P07-F-40` | `S1` | The statutory monthly VAT period is asserted nowhere by the Thai localisation; the effective period comes from a company-level setting with seven values whose platform default happens to be monthly, and that same setting governs the look-back of the excess-input-VAT carry-forward. | `SRC` | `01 R-V-24` |
| `P07-F-41` | `S3` | The `Tax Name` column of the two main registers is structurally empty, because it is read from the tax line rather than the base line. | `SRC` | `07 §5A` |
| `P07-F-42` | `S1` | Zero-rated and exempt VAT taxes resolve at template load into the tax group `WHT 1%` and therefore **carry a non-VAT tax group**. The *settle against withholding control accounts* clause is **withdrawn as latent** — see `P07-F-70`, `22 §15`: zero-amount taxes generate no tax line, so the group's control account is never reached; the live consequence is that 15,973 posted base lines are invisible to any tax-group-selected VAT report. Seven-step chain traced; posting-path consequence, not only reporting. | **VERIFIED in 3 of 3 database identities, 4 of 4 snapshots, **8 of 8** in-generation company sets and **17 of 17** across all 7 identities, enumerated (`22 §10.7`, `§15.3`)** — the best-evidenced finding in this package by a wider margin under the corrected unit; `P07-U-20` CLOSED | `06 §3A`, `22 §4.2`, `§7.2`, `§7.4` |
| `P07-F-43` | `S3` | In all four SMEsPlus handlers `return res` sits outside the column-group loop, so with more than one column group only the last group's rows survive. Pre-existing, not a migration regression. | `SRC` | `07 §5A` |
| `P07-F-44` | `S3` | Dead and duplicated code in the migrated handler: an unused second query build, an unused tax-detail query, and parameters passed for placeholders that do not occur. | `SRC` | `07 §5A` |
| `P07-F-45` | `S3` | Sign asymmetry between row and total in the sale-zero handler; inert only because the tax amount is pinned to zero by the row predicate. | `SRC` | `07 §5A` |
| `P07-F-46` | `S2` | The Thai title substitution replaces one of thirteen title states, so draft, cancelled, pro-forma, credit-note and vendor-bill renderings print the base wording. | `SRC-CHAL` | `05 §2.1` |
| `P07-F-47` | `S1` | Every tax-invoice capability this package finds structurally absent existed as a first-class model in the prior generation of this product line. The gap is a **regression**, and remediation is restoration rather than design from nothing. | `SRC-CHAL` | `05 §2.2` |
| `P07-F-48` | `S3` | A byte-identical duplicate of the Thai amount-in-words module sits in the same addons path under a different name, both installable, both overriding the same method — so the Thai wording on the statutory certificate is produced by whichever loads last. | `MEAS` | `13 §5.1` |
| `P07-F-49` | `S2` | A module in the declared set exists solely to update tax grids on already-posted entries — i.e. to mutate the inputs to the statutory registers after filing — and was absent from the first enumeration. | `MEAS` | `13 §5.1` |
| `P07-F-50` | `S1` | The tenant boundary is **specified and not built**: nine tenant requirements at status `NEW`, and zero tenant ORM models anywhere on the storage volume. | `MEAS`, class `A` | `20 §7` |
| `P07-F-51` | `S1` | The third-party withholding path is **inert on a fresh install of the declared set**: no account carries the withholding-account flag, so the withholding account domain is empty, the certificate wizard's required field has an empty domain, and enabling withholding on any shipped tax raises an error. | `SRC-CHAL` | `03 §7` |
| `P07-F-52` | `S2` | The withholding wizard reads a payment field defined only in the certificate module, on which it does not depend, so the base withholding module alone raises on any payment against a withholding-flagged line. | `SRC-CHAL` | `03 §7` |
| `P07-F-53` | `S1` | The "less withholding already posted" subtraction cannot subtract, because of its sign, so a second partial payment re-withholds the full amount. | `SRC-CHAL` | `03 §5 W-M-04` |
| `P07-F-54` | `S2` | The PND3/PND53 producer runs raw SQL against two tables supplied by modules it does not declare as dependencies, so an incomplete install fails with a database error at the moment of filing. | `SRC-CHAL` | `12 P07-D-26` |
| `P07-F-55` | `S2` | Neither withholding test suite can execute: both import symbols that do not exist in this generation, and one asserts an error raised by commented-out code. There is no regression coverage for the withholding path in either direction. | `SRC-CHAL` | `12 P07-D-27` |
| `P07-F-56` | `S3` | Licence inversion: an AGPL-3 module hard-depends on an Enterprise-licensed module, and two LGPL-3 SMEsPlus modules inherit from Enterprise-licensed code. Routed, not adjudicated. | `SRC` | `12 P07-D-07` |
| `P07-F-58` | `S1` | A supply does not require consideration under Thai VAT, and a fixed asset is "goods". Donation, scrapping, application to a non-business purpose, stock shortfall and goods on cessation are supplies; the researched system has **no output-tax event and no tax document for any of them**, and the disposal path produces no tax invoice. Definitional limb verified; the extent of the non-business-use limb is held at `P07-U-23`. | `SRC` + `VERIFIED` statute | `21 §3`, `02 §2A` |
| `P07-F-59` | `S1` | A hire purchase or instalment sale — the ordinary Thai route for machinery and vehicles — carries a tax point and a **tax invoice on every instalment due date**. The researched system has no instalment tax point, no tax-invoice object to issue, and no mapping to route the contract; the three gaps compound rather than overlap. | `SRC` + `VERIFIED` statute | `21 §4` |
| `P07-F-60` | — | **WITHDRAWN 2026-09-05.** Claimed no statutory withholding certificate has ever been issued. Refuted: a v16 identity holds 5,201 and the second in-generation identity holds one. Kept as a row rather than deleted so the identifier resolves; replaced by `P07-F-62`. | withdrawn | `22 §8.1`, `15 REV-E-29` |
| `P07-F-61` | `S3` | The cross-company tax-unit mechanism the Thai VAT registers opt into is **unused** — `account_tax_unit` **present and empty in 6 of 7 identities; ABSENT from the archive TOC in the seventh** (module not installed) — `22 §13.4`, `REV-E-52` (empty vs absent disambiguated against the archive TOC at `22 §10.4`; the earlier test could not tell the two apart). So `P07-F-39`'s unbounded-company-search exposure is **latent in every deployment examined**, not active. Scoping for `P07-U-14`, which stays open. | runtime | `22 §4.6`, `§8`, `§9` |
| `P07-F-62` | `S2` | **5,201 withholding certificates** in one **v16** deployment (§9 — out of the declared generation; the in-generation identity holds one) carry a populated s.40 income-type taxonomy (domain 15 values; **observed** 3 values over 6,507 cert lines in **two** generations — `22 §12.5`) — the most statutorily faithful classification in the declared set — while the PND export ignores that field and derives income type from the tax rate. The divergence has a real, sizeable population on the correct side of it. Replaces the withdrawn `P07-F-60`. | runtime, 3 identities | `22 §8.1` |
| `P07-F-63` | `S2` | The withholding-account flag the localisation never provisions is a **de facto required provisioning step**: **PARTLY REFUTED at the corrected population (`22 §10.4`, `REV-E-39`)** — the universality claim is withdrawn: a fourth in-generation identity has 237 accounts and **zero** flagged. Corrected: a **fresh** v19 identity ships with zero flagged, confirming the localisation never provisions the field; every identity that went on to transact flagged some, and **no two agree** — 3 of 586, 2 of 544, 1 of 339. The step being undocumented, there is no guidance on which accounts qualify, so a field that gates the whole withholding path (`P07-F-51a`) is configured divergently in every deployment examined. Surfaced only by splitting the compound `P07-F-51`. | runtime, 3 identities | `22 §4.5`, `15 REV-M-18` |
| `P07-F-64` | `S1` | **A path set excluded from the declared scope on a false stated reason supplies modules installed in every deployment.** `13 §2.1` excludes `efaplus-custom` (59 manifests) as *"Different products. Out of scope."*; that root holds 24–35 of the **installed** modules in each in-generation identity, including `l10n_th_withholding_tax`, `_cert`, `l10n_th_reports_ext` and `l10n_th_partner` — the modules this package's withholding findings are drawn from. All four database table sets are owned by role `efaplus`. | runtime, 3 of 3 in-generation | `22 §11.2`, `13 §2.1` |
| `P07-F-65` | `S1` | **Two different code bodies ship under one version string, so no manifest can identify the deployed copy.** The declared copy and the excluded copy of `l10n_th_withholding_tax` and `l10n_th_reports_ext` both declare `19.0.1.4` while differing by **17–179** lines of Python (normalised; the first published figures counted line endings — `22 §14.4`). For `l10n_th_withholding_tax_cert` the version *does* discriminate, and against the declared set: declared `19.0.1.5`, excluded copy and **all three deployments** `19.0.1.4`. `P07-U-01` is not closable by reading manifests; source-side attribution opened as `P07-U-28`. | runtime + source diff | `22 §11.3`, `§11.4` |
| `P07-F-66` | `S1` | **The runtime census was drawn over two undeclared directories, and a sixth identity sits outside them** — a **v18** database (`base 18.0.1.3`, uuid `551ab874-…`, 40,353 move lines, 4 companies) dated later than every artefact previously enumerated, in a sibling directory of one of the two searched. `22 §10`'s **7 snapshots / 5 identities** is now **SUPERSEDED AND A LOWER BOUND** (≥ 8 / 6) pending a full content sweep. `PATH SET` was declared rigorously for source evidence and author-chosen for runtime evidence in the same package. | runtime, verified independently | `22 §12` |
| `P07-F-67` | `S1` | **`P07-F-42` holds in 7 of 7 database identities across 3 generations (v16, v18, v19).** The target group is **exactly the lowest-id tax group of each company** in every identity — including one where the ids do not begin at 1 — and is named `Taxes` / `TAX 1%` / `WHT 1%` by generation, i.e. a **withholding or generic group every time and never a VAT group**. Census finished: 15 snapshots, 7 identities, roots `$HOME` + every `/Volumes` entry, keyed on `database.uuid`. Class stays `INF` on the load-order link (`P07-U-20`). | runtime, 7 of 7 identities | `22 §13.3`, `§13.4` |
| `P07-F-68` | `S1` | **The declared PATH SET is not the deployed set, in either direction.** Per in-generation identity, **14–26 installed modules are in no declared root** (49 in the v18 identity); union across four identities **85 modules**, fourteen of them accounting- or tax-adjacent. Conversely 1,042–1,284 declared module directories are not installed anywhere examined. `account_payment_multi_deduction` is **installed** in two identities, confirming `P07-F-20`'s set-composition classification and removing any reading of it as a capability gap. | runtime, 4 identities | `22 §14.1` |
| `P07-F-69` | `S1` | **The tax-period module this package analysed is installed in 0 of 4 identities.** `smesplus_tax_period_date` (declared) is installed nowhere; `scgl_tax_period_date` — **in no declared root** — is installed in 2 of 4, and carries the **same display name and the same version** `19.0.0.1`. After normalising line endings the two are **identical code** but for the manifest `author`, so `P07-F-03`, `P07-N-02`, `04 §4` and the tax-point rows **transfer intact**; what is wrong is every statement identifying the mechanism by technical module name. Inverse of `P07-F-65`: there one version covered two code bodies, here one display name and version cover two technical identities holding the same code. **Neither name nor version nor display name identifies deployed code — only the installed-module list does.** | runtime + normalised diff | `22 §14.2`, `§14.3` |
| `P07-F-70` | `S1` | **`P07-F-42`'s accounting consequence is LATENT, not live — and its reporting consequence is worse.** A zero-amount tax generates no tax line, and a tax group's control account is only reachable through one, so the *settles against withholding control accounts* clause has **never occurred**: **0 zero-rate tax lines** in both transacted identities, against positive controls of **5,202** and **33,114** real tax lines. What is live instead: **15,973 posted base lines** in the v16 identity carry a zero-rate tax whose group is **not a VAT group**, so any report selecting by tax group — including the two s.87 registers of `P07-F-01` — cannot see them as VAT supplies. Configuration defect unchanged: **17 of 17 company sets** holding zero-rate taxes, across 7 identities, resolve to a withholding or generic group. Severity stays `S1`; posting-path mechanism withdrawn as unevidenced, retained as **conditional** should any such rate cease to be zero. | runtime, 2 transacted identities with positive controls | `22 §15` |
| `P07-F-71` | `S2` | **Code identity is not decidable from a database snapshot for the modules `P07-F-65` left open — because the two copies differ only in Python method bodies.** Class-level field sets identical (0/0, 19/19, 37/37, AST-verified, 26 of 26 files parsed, 0 failures) and view XML identical, so **nothing that differs is persisted**. This **narrows `P07-U-28`**: source findings citing structure (models, fields, views) are **discharged** — both copies agree; findings citing method logic (`P07-F-11`, `-F-51`, `-F-52`, `-F-57`, `-F-63` source half) remain **open**, and method bodies are exactly where the copies diverge by 17–179 lines. Closing it needs the deployment's addons directory, which is not on this host. | AST + XML diff + 3 deployed identities | `22 §16` |
| `P07-F-72` | `S1` | **`P07-F-01`'s published trigger is REFUTED.** *"Installing Thai changes the stored value"* is false: `th_TH` is **active in 4 of 5 identities and only 1 carries the translation** (including the 3,480-partner v18 deployment). Measured instead: in the firing identity all five groups were created **in one transaction already carrying both languages and never edited**; where Thai was activated *after* the chart loaded, the names stayed `en_US`-only. The condition is **the chart template loading while Thai is already active** — an **install-order** property. `FACT` on the data pattern, `SUPPORTED INTERPRETATION` on the mechanism; `P07-U-29` opened to close it by execution. | runtime, 5 identities, create/write timestamps | `22 §17.1` |
| `P07-F-73` | `S1` | **`P07-F-01`'s consequence was never measured, and the exposure is prospective — with a measured magnitude.** The only identity where the defect fires holds **2–3 VAT-7% tax lines**; the two deployments where an empty statutory register would matter hold **5,202** and **32,672** and do **not** fire. The defect **fires only where there is no data to reveal it**. `P07-F-01` stays `S1`, its basis changing from realised to **prospective**: any populated deployment that loads the Thai chart while Thai is active puts those 5,202 / 32,672 VAT-bearing lines outside the s.87 registers. Withdrawn: *"empties both registers"* as observed cause. | runtime, 6 snapshots | `22 §17.2`, `§17.3` |
| `P07-F-74` | `S2` | **Code identity CLOSED for the tax-period module — not narrowed.** All **five** copies on this host (the declared `smesplus_` one and four `scgl_` ones) hash to **one distinct tree**, CR-normalised over `.py`/`.xml`/`.csv` excluding `__manifest__.py`, 4 real files each and not the empty-input sentinel; the only difference anywhere is the manifest `author`. So which copy is deployed cannot change any finding drawn from it, **structural or behavioural**: `P07-F-03`, `P07-N-02`, `04 §4` and the tax-point rows are **fully discharged** on code identity and leave `P07-U-28`. Stronger than `P07-F-71` only because these copies happen not to have diverged. | whole-tree hash, 5 copies | `22 §18.2` |
| `P07-F-75` | `S2` | **The open-item register — the thing that carries the HOLD — had 12 orphans out of 27 cited, and two naming conventions.** The orphan check was written for `P07-F-nn` and never extended; run across every family it reports 0 orphans for `P07-N`, `-C`, `-D`, `REV-E`, `REV-M` and **12 for `P07-U`**. Items were split across three files under `P07-U-nn` (`20`, `22`) and bare `U-nn` (`09`), so no single reading could enumerate them. Consolidated at `§5` and classified by what would close each. | own extended check | `§5` |
| `P07-F-76` | `S1` | **The code-identity question was a false dichotomy.** `P07-U-28` was framed as declared copy vs excluded copy. Host-wide enumeration, whole-tree hashed: `l10n_th_withholding_tax` **61 copies / 20 distinct trees**, `_cert` **49 / 15**, `l10n_th_reports_ext` **13 / 3**. The deployed body is one of **twenty** candidates, not one of two, and `P07-F-65` is confirmed but understated. Structural claims stay discharged (`P07-F-71`); the **behavioural** exposure widens from 2 candidates to 20. | host-wide hash enumeration | `22 §19` |
| `P07-F-77` | `S3` | **The identifier check covered 8 of 46 cited families; the 26 owned ones never enumerated are now clean.** 253 definitions, 253 citations, **0 orphans**, including all of `S-01`…`S-40` — **no legal claim cites a statutory source with no register row** (`S` alone carries 319 citations). Seven uncovered families are **foreign by attribution** (`P04-B`, `P04-F`, `P11-G`, licence and external-doc tags) and correctly not this package's to define. Localises `P07-F-75`: that was a **scope** failure, not a convention failure — this package uses one definition convention throughout. | own extended check, coverage declared | `22 §20.1`, `§20.2` |
| `P07-F-78` | `S2` | **`P07-U-28` CLOSED on evidence — all four behavioural claims discharged.** Filtering the 61 copies to the **13 declaring v19**, then hashing only the **cited** files, gives **2 candidate bodies per file, not 20**. `P07-F-11`: the two bodies of `tax_report_pnd.py` differ **only in the `title` column** (a partner company-type lookup vs a bound parameter) — the PND branch logic is byte-identical. `P07-F-51`/`-63`: the `wt_account` guard and its `UserError` are in both. `P07-F-57`: both index `[0]` while guarding on the union — same latent error, differently chained. `P07-F-52`: the wizard is **0 changed lines**, cited line identical, `depends` identical. Which copy is deployed cannot change any published finding. `P07-U-01` stays open — *which* copy runs is still undecidable, but the answer no longer matters. | claim-level hash + diff over 13 same-generation copies | `22 §21` |
| `P07-F-79` | `S3` | **The coverage audit that corrected an under-scoped check was itself computed over an under-scoped population.** `22 §20.1`'s family census carried an **undeclared frequency floor** (`c >= 2`), so *"46 families"* was author-chosen; with no floor there are **48**. Re-classified with reasons: **34 owned / 1,861 citations**, 10 foreign by attribution, 4 not identifiers, **0 unclassified**. The floor hid two singletons, both benign — but had it hidden an owned family with one citation, the audit would have reported clean coverage over a family it never examined. | own re-run, no floor | `22 §22.1` |
| `P07-F-80` | `S1` | **`P07-F-16` was analysed on a stack that is not the deployed stack.** `account_payment_multi_deduction` (v19.0.1.0.2) is **installed and outside the declared PATH SET**, declares `_inherit = ["account.payment.register", "analytic.mixin"]`, and **overrides `_prepare_move_line_default_vals`** — the method carrying `P07-F-16`'s base guard. It calls `super()` first, then post-processes `write_off_line_vals`, so its handling runs over a list from which the guard has **already** discarded the write-off contribution when withholding lines exist. `FACT` on the override, its `_inherit` and its call order; `SUPPORTED INTERPRETATION` on the interaction, which is **not** asserted. `P07-U-30` opened. **Not copy-dependent** — 21 copies on this host, 5 (tree, version) groups, and **every v19 copy is one tree** (`22 §23.2a`), which also gives the inverse of `P07-F-65`: two version strings over one body. It does **not** touch `P07-F-52`'s surface (zero references to `move_line_ids`/`wt_tax_id`), so that discharge stands. | runtime `ir_model_data` resolved through `ir_model_fields`/`ir_ui_view`, plus source | `22 §23.2` |
| `P07-F-82` | `S2` | **Two owned families shared a stem and every check reported them clean.** `P07-D-01` is a **broken module dependency**; `D-01` was the **tax invoice**, the most consequential statutory document in the package — different objects, one name, and a reader meeting `` `D-01` `` in `10` or `12` could not tell which. Structurally invisible: **every identifier resolved; two resolved to different things under the same name.** Document family renamed `DOC-01`…`DOC-10` (16 occurrences, 3 files; dependency family verified unchanged at 47 citations as the control). Found by P04's rule — **count the forms, not the identifiers**: 31 of 34 owned families are single-form and safe by construction, and only the 3 dual-form ones could carry this. | own form census | `22 §24.2` |
| `P07-F-83` | `S2` | **Both headline findings rest on a fully declared stack.** Per model, across three in-generation identities: **no installed module outside the declared PATH SET declares on `account.tax.group`, `account.tax`, `account.account`, `withholding.tax.cert`, `withholding.tax.cert.line` or `withholding.tax.report`** — so `P07-F-01`, `P07-F-42`, `P07-F-67`, `P07-F-51`, `P07-F-63`, `P07-F-62` and `P07-F-11` sit on a stack wholly inside the declared scope. Exposed instead: `P07-F-03`/`P07-F-57`/`P07-F-70` (3 modules on `account.move`/`.line`, one already discharged by `P07-F-74`) and `P07-F-16`/`P07-F-52` (`account_payment_multi_deduction`, `P07-F-80`). **`P07-F-57` is clear on copy identity (`§21.2`) and open on stack — two different questions.** Limit binds: `ir_model_data` sees only XML-id declarations, so this is a **floor on the declared stack, not proof of a complete one**; `P07-U-30` stays open and no blocker moves. | runtime, 3 identities | `22 §25` |
| `P07-F-84` | `S2` | **Fifteen stale restatements — the fourth occurrence of the propagation defect, and the first found by an identifier-level check.** `22 §7.4`, `§8` and `§8.4` carry before/after tables whose **"after" column is itself superseded**: `P07-F-01` at *1 of 2 in-generation*, `P07-F-42`, `P07-F-61` and `P07-F-51` half `b` at *2 of 2*, and three population statements at 7 · 5 — all corrected at `§10.4` and `§13`, none of which reached the tables that stated them. Earlier phrase greps missed them because each row states the same figure in different wording. Corrected by **population banner**, not rewrite. Also: P04's sweep unit `1c` (stems carrying two families) run here flagged **4 stems, 0 genuine collisions** — all legitimate restatements; reported as false-positive-prone rather than as four findings. | own identifier-level check | `22 §26.2`, `§26.3` |
| `P07-F-85` | `S2` | **Three assertive citations of `P07-F-01` still carried the refuted trigger or the superseded basis** — `02 §7` and `17 §5` calling it *the highest-severity finding* on the realised basis, `16 §4` stating *empties both registers on a Thai-language install*. Fifth occurrence of the propagation defect. `02` corrected in place; `16` and `17` are challenge/AAS+ records, so the correction is attached and the record left standing. Method: enumerate citations **by identifier, never by wording** (P04) — and the refinement this run forced, that the rule applied literally reports **162** unqualified citations of eight narrowed findings, of which **3** are real, so it must be scoped to citations that **assert** the narrowed claim. | own qualifier check | `22 §27` |
| `P07-F-86` | `S1` | **Five of seventeen negatives were bounded by a scope this session later proved incomplete, and none was re-run when the boundary moved.** `P07-N-01`, `-N-02`, `-N-06` are bounded by the declared PATH SET — proven not the deployed set (`P07-F-68`, 85 installed modules outside it). `P07-N-03` and **`P07-N-25`** are bounded by `/Volumes/iMacSys` — proven incomplete by `22 §13`, since `$HOME` holds addon trees and 8 of the 15 database snapshots. **`P07-N-25` underpins `P07-F-50`** (tenant boundary specified-not-built): its boundary was *all `.py` under the volume*, and **`$HOME` was never searched**. Re-run over the corrected root set is executing; `P07-F-50` stands as published until it returns. Counter-case worth the record: the four negatives written with a **narrow** declared boundary are the ones that did **not** go stale. | own boundary audit | `22 §28` |
| `P07-F-57` | `S3` | Latent index error in the withholding candidate filter: it indexes the first tag of the first repartition line while guarding only on the union of tags. Latent because the shipped chart tags base lines. | `SRC-CHAL` | `03 §4 W-K-03` |

`P07-F-58` and `P07-F-59` were added after intake of peer evidence from P04 and independent
retrieval of the statute behind it. Both close gaps this package had — not defects it
inherited. See `21_P07_PEER_EVIDENCE_INTAKE_P04.md`.

**Open items opened and closed by this round.** `P07-U-27` (unexamined database identities)
is **CLOSED** — all snapshots and identities opened; the population at closure was 7/5 and is now **15 snapshots / 7 identities** (`22 §13`). `P07-U-01` (which extra-addon
copy is deployed) is **NOT closable by manifest version** — see `P07-F-65`. **`P07-U-28` is
OPENED:** for `P07-F-11`, `P07-F-51`, `P07-F-57`, `P07-F-62` and the source half of
`P07-F-63`, the line cited is from the declared copy, and whether that copy is the deployed
one is **decided against it** in one module and **undecidable by version** in two (`22 §11.4`).
The findings are not withdrawn — their runtime halves are read from the databases, and no
re-reading has yet shown the cited behaviour differs between copies. What is withdrawn is the
assumption that the declared copy is the deployed one.

**Population corrected — every runtime denominator in this register was written over 2
in-generation identities; the eligible number is 4.** A peer's version table named an identity
this package had recorded as *unexamined*. Re-deriving rather than patching found two further
defects: the snapshot census was taken by file **extension**, missing two `.zip`-borne dumps
(5 → **7 snapshots**), and the identity unit was the **filename**, so two different databases
sharing the name `iEVING` were counted as one (4 → **5 identities**, keyed on
`database.uuid`). Full re-derivation and the per-finding effect at `22 §10`; `REV-E-38`…`-42`.
`P07-F-01` weakens (1 of 4, not 1 of 2), `P07-F-42` strengthens (4 of 4 plus v16),
`P07-F-63` is partly refuted ninety minutes after publication.

**Orphan check.** Every `P07-F-nn` cited anywhere in the package now resolves to a row here.
Run mechanically — parse this register's definition rows, collect every citation across all
files, diff the two sets — after P04 reported the same class of defect in its own package for
the third time. It found two: `P07-F-61` was **created in `22 §4.6` and never added here**,
and `P07-F-60` was **withdrawn without leaving a row**, so a reader looking either up found
nothing. Both are exactly the defect this register was written to fix (`§0`), reappearing in
the register itself. `REV-E-36`.

**Re-running it immediately caught a third — mine, one edit old.** `P07-F-63` was created in
`22 §4.5` in the *same* edit that added the two rows above, and went in with no row here. The
defect recurred **inside its own correction**, and the same pass left `P07-F-60`'s row one
column short. This is the yield fact, not a confession: the first run found two defects both
older than a day; the second found one ninety seconds old. **A check cheap enough to re-run
after every edit finds what a check run once before publication cannot** — and re-reading the
edit I had just written would not have found it, consistent with `15 REV-M-09`. The check is
now the last step before every commit of this package, not a pre-publication gate. `REV-E-37`.

**The identifier check is not the only check, and it returned CLEAN on a broken package.**
Run at the same moment, a **per-table structural check** (every row's unescaped-pipe count
against its own table's header, strict renderer semantics) found **seven malformed rows** in
four files — including all four rows of `03 §6.1`, the section added after independent
challenge, where the entire `Evidence` column was absent. The identifier check cannot see
those; it only sees identifiers. **The check that catches a defect is the one whose unit
matches the defect** (`REV-M-20`). Both now run before every commit: 149 tables, 0 malformed.

Both runs are reproduced in `15 §REV-E-36/37`. The script parses definition rows from `§2`,
collects `P07-F-<n>` across all 23 files, and diffs the sets. `P07-F-08` is expected in its
output and excluded by the not-issued list below: an identifier never issued is not an orphan,
but the check cannot know that, so the exclusion is **declared here rather than coded**.

**Identifiers not issued:** `P07-F-81` — never issued; it appears in this package **only**
inside `15 REV-E-64` and `22 §19.3`, which describe a false positive in the identifier check
itself. Documenting a spurious identifier creates a genuine citation of it, so the check
reports it forever unless it is declared here. `P07-F-08`, `-17`, `-22`…`-25`, `-28`, `-29`, `-31`, `-32`,
`-33`. These numbers were consumed during drafting by observations that were merged into
other findings or discarded as not defects (see `15 §4` `REV-E-05`, `REV-E-06`, `REV-E-08`).
They are recorded as not issued so that a gap in the sequence is not mistaken for a lost
finding.

## 3. Distribution

**Counts below are EXECUTED, not asserted.** `UNIT` = one table row in §2, enumerated by
call site. The first issue of this section asserted totals that were wrong in every cell —
see §3.1.

| Severity | Count |
|---|---|
| `S1` — statutory output wrong, absent or silently empty | 22 |
| `S2` — not reproducible, or an unenforced boundary | 15 |
| `S3` — correctness or maintainability | 11 |
| **Total issued** | **48** |

| Evidence state | Count |
|---|---|
| `SRC-CHAL` — independently re-verified by an adversarial reviewer | 27 |
| `SRC` (includes 2 cells reading `SRC` + `VERIFIED` statute) | 13 |
| `MEAS` (includes 1 dual-state cell `MEAS` + `SRC-CHAL`, counted once here) | 7 |
| `INF` | 1 |
| **Total** | **48** |

### 3.1 Correction — These Totals Were Asserted Before They Were Executed

| Cell | Asserted | Executed |
|---|---|---|
| Total issued | 49 | **48** |
| `S1` / `S2` / `S3` | 21 / 16 / 12 | **22 / 15 / 11** |
| `SRC-CHAL` / `SRC` / `MEAS` / `INF` | 26 / 16 / 6 / 1 | **27 / 13 / 7 / 1** |

Every cell was wrong. The register that exists to make this package's findings countable
carried an uncounted total.

Two method points, both of which cost something:

1. **The count was never executed.** It was maintained by hand as findings were added, and
   drifted immediately. Enumerating the rows takes one command; asserting them takes none,
   and the two are indistinguishable to a reader.
2. **The first attempt to correct it repeated the underlying defect.** Re-deriving the
   evidence-state counts with a second pattern double-counted a dual-state cell and produced
   a total that summed correctly by coincidence. The figures above come from enumerating the
   rows and reading the column — the project rule is *enumerate by call site, then read;
   never extract a value with a second pattern*, and the first correction attempt broke it.

Found by applying to P07 a correction P04 raised against its own register in the same
exchange. Registered as `REV-E-16`, and as a Class 2 instance in
`SMEPLUS_EVIDENCE_SUBSTITUTION_STANDARD_PROPOSED`.

## 4. The Two Findings That Should Be Read First

`P07-F-01` and `P07-F-42` were both **escalations produced by independent challenge**, both
reached by two reviewers separately, and both change the character of the package:

- `P07-F-01` was recorded by this session as a brittle-label dependency. It is in fact a
  translation-mapping equality, so the expected act of installing the Thai language empties
  both statutory VAT registers.
- `P07-F-42` was recorded by this session as "these taxes have no tax group". They do have
  one: the first Thai group by id, which is `WHT 1%`. Zero-rated and exempt VAT therefore
  settles against withholding control accounts — a posting-path defect the session had
  classified as a reporting-path gap.

Neither was found by the author. Both were found by reviewers reading the same code the
author had already read.


---

## 5. Open Items — Consolidated, and Classified by What Would Close Them

**Why this section exists, and what was wrong before it.** The orphan check introduced at `§2`
was written for `P07-F-nn` and never extended. Run across every identifier family it reports
`P07-F` 0 orphans, `P07-N` 0, `P07-C` 0, `P07-D` 0, `REV-E` 0, `REV-M` 0 — and **`P07-U`: 12
orphans out of 27 cited.** The open items are what carry the HOLD, and **44% of them had no
definition row anywhere.** They were also split across three files under **two naming
conventions** (`P07-U-nn` in `20` and `22`, bare `U-nn` in `09`), so no single reading of the
package could enumerate them. `P07-F-75`, `REV-E-63`.

**The classification is P04's and it changes the shape of the register rather than its size.**
Every row below is open for one of three reasons, and only the first is closable by more
research:

- **`NOT YET READ`** — the evidence exists and has not been looked at.
- **`NOT ON THIS HOST`** — the evidence exists somewhere, but not anywhere reachable from here.
- **`EVIDENCE NEVER RECORDED`** — the fact is a past act that nothing preserved. No archive,
  no wider census and no better query can settle it; only a controlled execution can.

| ID | Statement | Closes by | Argued at |
|---|---|---|---|
| `P07-U-01` | Which extra-addon copy is deployed. Not closable by reading manifests (`P07-F-65`: one version over two code bodies). **Partly closed** — where copies hash identically the question is void (`P07-F-74`). | `NOT ON THIS HOST` | `22 §11.4`, `§18.2` |
| `P07-U-02` | Whether the reproduction caveat holds for archives needing the newer client. | `NOT YET READ` | `22 §7` |
| `P07-U-03` | The deferred input-tax claim instrument (`AASR-P07-VETO-01` rests on it). | `NOT YET READ` | `09` |
| `P07-U-04` | Statutory retention/format of the s.87 books. | `NOT YET READ` | `09` |
| `P07-U-07`…`P07-U-10` | Four statutory questions on tax point, credit/debit note and correction, unresolved against primary sources. | `NOT YET READ` | `09` |
| `P07-U-11` | Residue of the four declared Thai-module patterns; **materialised** as `P07-F-48` — a fifth artefact findable by a `*thai*` glob that was never run. | `NOT YET READ` | `13 §5.1` |
| `P07-U-12` | Carryover period source. **CLOSED** — lines 11 and 12 consume it, conditional on `R-V-24`. | *closed* | `01`, `08 §2` |
| `P07-U-13` | Duplicate-copy tax invoice: number and date computed, the duplicate not modelled. | `NOT YET READ` | `05 §3` |
| `P07-U-14` | Tenant boundary **specified and not built**. Closed as a finding (`P07-F-50`), retained as a decision. | *closed as finding* | `20 §5` |
| `P07-U-15` | Egress of taxpayer identifiers to an external Revenue Department service, not scope-assessed. | `NOT YET READ` | `20 §5` |
| `P07-U-16` | Whether cash-basis exigibility is configured in any deployment. | `NOT YET READ` | `02 §5`, `04 §2` |
| `P07-U-17` | The base tax-closing path was not examined. | `NOT YET READ` | `03 §7`, `11 §4` |
| `P07-U-18` | Whether the v14 tax-invoice capability was dropped, superseded or lost in migration (`P07-F-47` is a regression on it). | `NOT YET READ` | `05 §2`, `§4` |
| `P07-U-19` | The base `account.return` framework's own attachment behaviour, not examined. | `NOT YET READ` | `08 §5` |
| `P07-U-20` | The load-order link that keeps `P07-F-42` at class `INF`. **A database records the result of a load order, never the order.** | **`EVIDENCE NEVER RECORDED`** | `22 §18.3` |
| `P07-U-21` | The premise `A-15`'s framing leans on, not searched. | `NOT YET READ` | `08 §5` |
| `P07-U-22` | A comparison surface not version-compared in this session. | `NOT YET READ` | `13 §2.1` |
| `P07-U-23`…`P07-U-26` | Four Thai statutory questions from the P04 intake, incl. `P07-U-26` — the prescribed contents of the s.87(3) report, which gates `P04-F-67` at SUPPORTED INTERPRETATION. Attempted, not located. | `NOT YET READ` | `09 §5`, `21` |
| `P07-U-27` | Unexamined database identities. **CLOSED** — 15 snapshots / 7 identities all opened. | *closed* | `22 §13` |
| `P07-U-28` | Source-side attribution for **behavioural** claims. **CLOSED on evidence — `P07-F-78`:** all four hold in both same-generation candidate bodies, so which copy is deployed cannot change them. | *closed* | `22 §21` |
| `P07-U-30` | (**widened at `22 §25.2`** to `account_discount_catalog` and `scgl_product_image` on `account.move`/`.line`.) Whether `account_payment_multi_deduction`'s override of `_prepare_move_line_default_vals` alters the withholding/write-off outcome `P07-F-16` describes. The module is readable on this host; what is unread is the full call chain, and what is untested is the interaction. | `NOT YET READ` | `22 §23.2` |
| `P07-U-29` | Whether the chart template loading under an active Thai language is what writes the translated group name — `P07-F-01`'s real trigger. | **`EVIDENCE NEVER RECORDED`** | `22 §17.1`, `§18.3` |

### 5.1 What the classification says that the count does not

**28 items: 4 closed, 21 `NOT YET READ`, 1 `NOT ON THIS HOST`, 2 `EVIDENCE NEVER RECORDED`.**
(`P07-U-28` closed on evidence at `22 §21` — the first item closed that way rather than by self-correction.)

The last two are the only items in this package that **no amount of further research can close** —
and they are the ones the two headline findings turn on. P04 holds one of the same class
(`P04-B-47`: whether asset entries were never created or created and removed — a database
records the result of a write sequence, never the sequence).

**Those three items are one ask.** A controlled execution, run twice in opposite orders, with
the result recorded. If a runtime request is ever granted they should travel together, because
separately each looks like a small residue and together they are the only category of evidence
neither package can manufacture.

**And this is the more useful thing to give a decision-maker than the count of open rows** —
which is all this package published until now.
