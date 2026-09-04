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
| `SRC` | Derived from source, complete chain, not executed (`U-02` applies to all of them) |
| `SRC-CHAL` | Source-derived and independently re-verified by an adversarial reviewer reading the same code |
| `INF` | Inference with a complete mechanism but one unverified link |
| `MEAS` | Measured by enumeration over a declared population |

No finding in this package is runtime-observed. No database was queried (`13 §7`).

## 2. Findings

| ID | Severity | Statement | Evidence state | Where argued |
|---|---|---|---|---|
| `P07-F-01` | `S1` | The two SMEsPlus statutory VAT registers admit a row only if the raw stored value of the tax group's name equals the dict `{'en_US': 'VAT 7%'}`. Because that name is a translatable field, installing Thai adds a second entry and the equality fails for **every** row, so both registers return no data at all, silently. | `SRC-CHAL` (two reviewers, independently) | `02 §5.1` |
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
| `P07-F-42` | `S1` | Zero-rated and exempt VAT taxes resolve at template load into the tax group `WHT 1%` and therefore settle against the **withholding** control accounts. Seven-step chain traced; posting-path consequence, not only reporting. | `INF` (complete chain, one load-order link unexecuted) — reached independently by two reviewers | `06 §3A` |
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
| `P07-F-58` | `S1` | A supply does not require consideration under Thai VAT, and a fixed asset is "goods". Donation, scrapping, application to a non-business purpose, stock shortfall and goods on cessation are supplies; the researched system has **no output-tax event and no tax document for any of them**, and the disposal path produces no tax invoice. Definitional limb verified; the extent of the non-business-use limb is held at `U-23`. | `SRC` + `VERIFIED` statute | `21 §3`, `02 §2A` |
| `P07-F-59` | `S1` | A hire purchase or instalment sale — the ordinary Thai route for machinery and vehicles — carries a tax point and a **tax invoice on every instalment due date**. The researched system has no instalment tax point, no tax-invoice object to issue, and no mapping to route the contract; the three gaps compound rather than overlap. | `SRC` + `VERIFIED` statute | `21 §4` |
| `P07-F-57` | `S3` | Latent index error in the withholding candidate filter: it indexes the first tag of the first repartition line while guarding only on the union of tags. Latent because the shipped chart tags base lines. | `SRC-CHAL` | `03 §4 W-K-03` |

`P07-F-58` and `P07-F-59` were added after intake of peer evidence from P04 and independent
retrieval of the statute behind it. Both close gaps this package had — not defects it
inherited. See `21_P07_PEER_EVIDENCE_INTAKE_P04.md`.

**Identifiers not issued:** `P07-F-08`, `-17`, `-22`…`-25`, `-28`, `-29`, `-31`, `-32`,
`-33`. These numbers were consumed during drafting by observations that were merged into
other findings or discarded as not defects (see `15 §4` `REV-E-05`, `REV-E-06`, `REV-E-08`).
They are recorded as not issued so that a gap in the sequence is not mistaken for a lost
finding.

## 3. Distribution

| Severity | Count |
|---|---|
| `S1` — statutory output wrong, absent or silently empty | 21 |
| `S2` — not reproducible, or an unenforced boundary | 16 |
| `S3` — correctness or maintainability | 12 |
| **Total issued** | **49** |

| Evidence state | Count |
|---|---|
| `SRC-CHAL` — independently re-verified by an adversarial reviewer | 26 |
| `SRC` | 16 |
| `MEAS` | 6 |
| `INF` | 1 |

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
