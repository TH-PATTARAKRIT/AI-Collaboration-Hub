# P07 — CONTRADICTION REGISTER

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Scope of This Register

`EC-05` requires every material contradiction between primary research, source evidence,
independent reviewers, AAS+, PMO, or prior canonical evidence to be dispositioned with
traceable evidence. This register covers four classes:

- **§2 Internal contradictions** — the system contradicts itself
- **§3 Statute-versus-system contradictions** — the system contradicts Thai law
- **§4 Source contradictions** — two evidence sources disagree
- **§5 Negative-claim control** — every system-wide negative in this package, with class and boundary

## 2. Internal Contradictions in the Declared Source Set

| ID | Contradiction | Side A | Side B | Disposition |
|---|---|---|---|---|
| `P07-C-01` | The same statutory book (s.87 output/input tax report) has **two implementations** with different selection predicates. | Vendor XLSX generator + SMEsPlus override: tag-based, partnerless rows retained, zero/exempt included | SMEsPlus dynamic reports: tax-group-name literal, partnerless rows dropped, zero/exempt excluded | **UNRESOLVED — architectural.** Neither is declared canonical. The SMEsPlus reports are derivably a subset of the vendor reports (`07 §5`). Boss decision required on which is the statutory book. |
| `P07-C-02` | The same statutory column (branch) is sourced from **two different partner fields**, and a third `COMPANY`-scope field exists that no report reads. | `company_registry` → `l10n_th_branch_name` (`l10n_th`, `smesplus_account_reports`) | `res.partner.branch` (`l10n_th_partner`, used by the `_ext` override and the PND override) | **UNRESOLVED.** Two statutory reports can print different branch values for one taxpayer. `res.company.branch` — the actual filing-unit attribute — is read by none of them. |
| `P07-C-03` | The tax point is **stored and displayed** but **not applied**. | `account.move.tax_period` shown as a report column | Period selection uses the accounting date; the predecessor substitution was removed | **UNRESOLVED.** The report shows the reader a date it did not use. |
| `P07-C-04` | The withholding **classification knowledge** exists correctly in one model and is ignored by the statutory export. | Certificate model: 16-value s.40 income-type selection, `tax_payer` condition, `payment_date` | PND export: income type derived from rate, condition hard-coded `'1'`, date taken from the invoice move | **UNRESOLVED.** The system knows the right answer and files a different one. |
| `P07-C-05` | The **withholding accounting event** and the **withholding reported event** are different objects on different dates. | Payment write-off line (the posting) | Invoice line (what the PND query returns) | **UNRESOLVED — this is the P07 headline.** `03 §3` |
| `P07-C-06` | **Two withholding frameworks** occupy the same extension point with no mutual exclusion. | Vendor `l10n_account_withholding_tax` | Third-party `l10n_th_withholding_tax` | **UNRESOLVED.** Duplicate tax recognition surface. |
| `P07-C-07` | Chart account **descriptions** contradict the roles the repartition and tax-group data assign. | `213200 Output VAT` described as the net liability; `213400 VAT Payable` described as tax collected from sales | Repartition posts daily output VAT to `213200`; `213400` is the group settlement account, mirroring the coherent WHT pattern and `114200`'s own description | **CONFIRMED as a documentation defect, not a posting defect.** `P07-F-34` |
| `P07-C-08` | The same statutory book is rendered with **different column sets** on the two sides of the trade. | `sale_vat_report_zero`: 9 columns, no tax period, no tax name | `purchase_vat_report_zero`: 11 columns, both present | **CONFIRMED.** `P07-F-35` |
| `P07-C-09` | The chart **provisions an obligation** the reporting layer cannot serve. | `213303 Tax Withheld - PND 54`, with a bilingual description naming the remittance form | No PND 54 tax, tag, handler, certificate type or wizard entry | **CONFIRMED.** `W-K-07` |
| `P07-C-10` | Sales-side withholding is **provisioned in the chart and in tax templates** and carries no tags, so it reaches no report. | `tax_wht_income_{1,2,3,5}` → `114300 WHT Creditable` | Both PND handlers select on tag membership | **CONFIRMED.** `W-K-08` |

## 3. Statute-Versus-System Contradictions

Each cites the statutory source and the implementing evidence; none is asserted from ERP
behaviour.

| ID | Statutory rule | System behaviour | Severity |
|---|---|---|---|
| `P07-C-11` | VAT tax point is an event; services are payment-based (`S-01` `S-02`) | Accounting date | **tolerance-relevant** — determines the statutory month of every supply |
| `P07-C-12` | WHT is withheld at every time of payment; remit within 7 days (`S-30` `S-32`) | PND period driven by the invoice date | **tolerance-relevant** |
| `P07-C-13` | Credit/debit notes adjust in the month issued/received, referencing the original tax invoice (`S-13` `S-14` `S-23` `S-24`) | Netted by sign, no note class, no original reference, placed by accounting date | **tolerance-relevant** |
| `P07-C-14` | A tax invoice carries its own serial number and is issued at the tax point (`S-19` `S-20`) | Print-title substitution on the accounting document | **tolerance-relevant** |
| `P07-C-15` | Filing is per place of business unless the DG approves consolidation (`S-15`) | Per company, optionally grouped across companies | **tolerance-relevant** |
| `P07-C-16` | The certificate is issued in duplicate, immediately on every withholding (`S-31`) | Manual wizard, no duplicate-copy record | material |
| `P07-C-17` | The return states the tax withheld of **each person** (`S-33`) | Amount recomputed from rate × base rather than read from the ledger | material |
| `P07-C-18` | Reports must be retained 5 years (`S-26`) | The statutory certificate is unlinkable by the billing group | material |
| `P07-C-19` | Zero-rated (`S-07`) and exempt are distinct classes | Both keyed on move-level `amount_tax = 0` | material |
| `P07-C-24` | The VAT taxable period is the calendar month (`S-15` `S-34`) | Taken from a company-level setting with seven options, defaulting to monthly; the Thai localisation asserts nothing | material — the statutory period is a coincidence of a platform default, and the excess-VAT carry-forward resolves against it |

## 4. Source Contradictions

| ID | Sources in conflict | Resolution | Basis |
|---|---|---|---|
| `P07-C-20` | A commercial source stated PND53 is for **service** invoices and PND3 for **rental** invoices to juristic persons. | **Commercial source rejected.** The split is by payee legal personality: PND3 natural persons, PND53 juristic persons. | `S-30` `S-33`; the Thai chart's own account descriptions (`213301` "Individual Suppliers", `213302` "Juristic (Company) Suppliers") independently corroborate the statutory reading. Recorded at `09 §5`. |
| `P07-C-21` | The current 7% VAT reduction was initially retrieved as expiring 30 September 2026, 26 days after this session's date. | **Corrected before use.** A further extension to 30 September 2027 was approved by Cabinet on 27 July 2026 and confirmed by a Revenue Department notice on 2 August 2026. No finding in this package asserts an imminent lapse. | `S-35`; decree number held at `P07-U-04` |
| `P07-C-22` | Four Thai tax-document modules (`l10n_th_tax_invoice`, `l10n_th_tax_report`, `l10n_th_expense_tax_invoice`, `l10n_th_expense_withholding_tax`) are absent from the declared source set but present in the v14 and v12 trees on the same volume. | **Both true; recorded as class `A` within the declared scope and class `E` at volume scope.** Whether they were superseded, replaced or dropped is `P07-U-18`. | `05 §5`; `13 §2.1` |
| `P07-C-25` | This package's VAT event model treated every source business event as consideration-based, while `S-36` defines a sale as not requiring consideration. | **Self-contradiction against a statute this session had not retrieved.** Closed by retrieving s.77/1(8) and (9) after a peer flagged the definition; `02 §2A` added, `P07-F-58` issued. The gap was found by a peer reading a definition this session never opened — not by this session's own controls. | `21 §3` |
| `P07-C-23` | This session's own draft asserted that PND 54 appears nowhere and that the whole filing/close segment was absent. | **Both self-contradictions found and corrected before publication**, by running the declared pattern rather than trusting the draft. PND 54 has a general-ledger account; the base set has a full return-filing framework. | `03 §4.1`; `08 §5`; recorded in `15 §4` |

## 5. Negative-Claim Control (`EC-06`)

Every system-wide negative asserted anywhere in this package, with its class and boundary.
`NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.` Classes: `A` verified absence within a
stated scope · `B` not found in searched scope · `C` not yet searched · `D` unknown ·
`E` contradicted.

| ID | Claim | Class | Declared boundary |
|---|---|---|---|
| `P07-N-01` | No tax-invoice numbering sequence distinct from the accounting document sequence | `A` | PATH SET `13 §2`; patterns `sequence`, `ir.sequence`, `tax_invoice`; 15 modules of `13 §5`; `l10n_th` read in full |
| `P07-N-02` | No **functional** consumer of `account.move.line.tax_period_date`: no report, compute, domain or SQL reads it. It does have one reader — a readonly, `optional="hide"` list column. | `A` | all three roots, all file types, `__pycache__`/`.po`/`.pot` excluded; pattern `tax_period`. **Corrected during independent challenge**: the first statement of this claim said "read by nothing", which was false. See `15 §4` `REV-E-09`. |
| `P07-N-03` | Four Thai tax-document modules absent from the declared set | `A` within scope, `E` at volume scope | directory-name search, declared set and whole volume |
| `P07-N-05` | No branch-level VAT return object | `B` | Thai module population; the base `account.return` framework was later found and is reported at `P07-F-37` — the branch dimension remains not found |
| `P07-N-06` | No VAT tax-point determination logic | `B` | PATH SET `13 §2`; patterns `13 §4`; all 15 modules read for tax-date handling |
| `P07-N-07` | No import tax point, no s.78/3 special tax point | `B` | as `P07-N-06` |
| `P07-N-08` | No self-assessed VAT mechanism in the Thai modules | `B` | **Thai module population only.** The base application's reverse-charge facilities were not examined. |
| `P07-N-09` | No tenant construct in the P07 module population | `B` | 15 modules of `13 §5` only. **This must not be read as "SMEsPlus has no tenant construct."** Superseded in relevance by `P07-F-39`: the question that matters is not whether P07 defines a tenant construct — it does not need one — but what contains the unbounded company search inside the tax-unit mechanism. |
| `P07-N-10` | No guard preventing both withholding frameworks from applying to one payment | `B` | all Python and XML of modules 3, 7, 8, 10, 11 of `13 §5`, read in full for the WHT path |
| `P07-N-11` | No PND 54 tax, handler, certificate type or wizard entry; no PND 2 artefact | PND 54: `A` for the four reporting layers, `E` for the chart layer; PND 2: `B` | pattern `pnd` case-insensitive, all file types, token census at `03 §4.1` |
| `P07-N-12` | No WHT remittance-deadline or filing-period object | `B` | as `P07-N-11` |
| `P07-N-13` | No traced executor of the month-end WHT consolidation described in the chart | `C — NOT YET SEARCHED` | the base tax-closing path was **not** examined; recorded as `P07-U-17` |
| `P07-N-14` | No abbreviated tax invoice, debit note or substitute tax invoice class in the Thai modules | `B` | Thai module population; the base document typology was not re-enumerated |
| `P07-N-15` | **WITHDRAWN.** Originally: the whole filing/close segment is absent. | `E — CONTRADICTED` | Replaced by `P07-F-37`, a measured provisioning gap on a framework that exists. Withdrawal recorded at `15 §4`. |
| `P07-N-16`…`P07-N-19` | Four negatives registered in `06 §6` (income-side tags; no report selecting the income-side fact; no canonical withholding shape; blank tax-group cells in the CSV). | `A`, `A`, `B`, `A` | as stated in `06 §6`; `P07-N-19` is explicitly a statement about the CSV, **not** about the resulting records |
| `P07-N-20`…`P07-N-24` | Five negatives registered in `08 §6` (debit-note class; report snapshot; tax-period object; refund-claim representation; and the **positive** immutability assumption, recorded as unverified). | `B`, `B`, `B`, `B`, `C` | as stated in `08 §6` |
| `P07-N-25` | No tenant ORM model exists anywhere on the storage volume, while the tenant boundary is specified with status `NEW`. | `A — VERIFIED ABSENCE` | all `.py` files under `/Volumes/iMacSys`; specification at `FR_DETAIL_TENANT_MANAGEMENT.md`. See `P07-F-50`. |

**Registers added after challenge.** Files `06` and `08` originally carried no
negative-claim register at all, while `02`, `03` and `05` did. Independent challenge tested
both sets: **every negative that had been registered with a class and a boundary survived;
three of the unregistered ones were found to be wrong or over-stated** (`GL-02`'s "no tax
group", `GL-01`'s "every PND handler", and `08 §5.4`'s "no workflow"). The correlation
between "unregistered" and "wrong" is itself the finding, and it is the strongest available
evidence that the negative-claim control does real work rather than ceremonial work.

### 5.1 Restatement Check — Executed, and It Failed on First Run

The project rule warns that class `B`/`C`/`D` claims are upgraded to class `A` in
**summaries** rather than in the body.

The first issue of this section asserted that the check had been performed package-wide and
had passed. That assertion was **defective in two ways**, both found by independent
challenge: it named `16`, `17` and `18` as its coverage when those files did not yet exist,
and it excluded `01`–`15` and `20`, which is where restatement actually happens. A control
that certifies against absent artefacts cannot have been run as written.

The check was then executed properly, over every file in the package. It found **four
class-`B`-to-unqualified restatements, all of them in `19` — the one file cleared for
downstream reference** — plus one internal count error:

| Location | Restated claim | Underlying class | Disposition |
|---|---|---|---|
| `19` `POS-7` | "the filing entity's own attribute is read by nothing" | bounded in `20 §6` to the declared set | **corrected**: now "no statutory report examined in this research reads it" |
| `19` `POS-8` | "no rule of precedence" | `P07-N-18`, class `B` | **corrected**: now "no rule of precedence was found in the material examined", and the silent-discard guard is stated |
| `19` `POS-9` | "without leaving a trace" | no registered negative supported the absolute | **corrected**: replaced with the positive mechanism — the figure is a render-time computation over live master data |
| `19` §4 | "can never be filed from the system" | `P07-N-11`, class `A` for four reporting layers but `E` at the chart layer | **corrected**: now "no means of filing it was found anywhere in the material examined" |
| `19` §7 | "three design decisions" followed by four items | count error | **corrected** to four |

Every one of these was in the Layer-1 file. The lesson recorded for the next round is that
**the clean-room scrub and the restatement check are different controls**: `19` passed the
vendor-token scrub cleanly on first run and failed the restatement check on the same
content. Recorded as `REV-E-14`.

## 6. Contradictions Not Resolvable by P07

| ID | Item | Owner |
|---|---|---|
| `P07-C-01` | Which s.87 implementation is canonical | Boss |
| `P07-C-02` | Which branch attribute is the statutory one, at which scope | Boss, informed by P11 scope reconciliation |
| `P07-C-06` | Which withholding framework is canonical | Boss |
| `P07-C-11`…`P07-C-15` | Whether to restore tax-point ownership to P07 | Boss, with P06 and P08 |
