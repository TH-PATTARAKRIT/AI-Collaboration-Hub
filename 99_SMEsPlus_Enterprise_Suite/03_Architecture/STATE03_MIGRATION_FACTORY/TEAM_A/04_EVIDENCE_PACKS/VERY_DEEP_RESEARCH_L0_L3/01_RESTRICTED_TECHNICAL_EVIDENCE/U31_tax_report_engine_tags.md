# U31 — tax_report_engine_tags (Thai Tax Core: tax report and tax grid tag infrastructure)

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION` — no V-level, no Complete, no coverage %, no Gate PASS. Not legal or tax advice.

- **Unit:** U31 `tax_report_engine_tags` (Thai Tax Core lane, source-level completion of the tax REPORT and TAG infrastructure that TXA1, TXA2, TXC and U24 listed as not read).
- **Modules read:** `account` (report, line, expression, column, external value, tag, tax repartition line, move, move line, partial reconcile, chart template, company, security, views, data), `l10n_th` (report data, tax and tax-group templates, manifest, hook), `account_update_tax_tags` (re-read), `spreadsheet_account` and `spreadsheet_dashboard_account` (discovered, installed), `hr_expense` (tag path), `l10n_account_withholding_tax` (tag path, uninstalled). Foreign-localization files were touched only as grep hits and are labelled `FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE`.
- **Source revision:** `19.0.post20260921`. **Date:** 2026-10-02. **DB:** restored dump `itest19c_research`, configuration queries only (counts, flags, names of seeded configuration; no business data).
- **Prior units read first (not redone):** U13, U24, TXC, U23, plus TXA1 and TXA2 claims on tags, closing flag, lock dates and cash basis; TXS statutory register and supplement for statutory identifiers only.

## 0. Scope, method and Function-ID mapping

**Question set.** (1) the report definition family; (2) the evaluation engines present and the entry points that run or display a report; (3) the tax tag lifecycle; (4) the closing flag, carry-over and date scope; (5) access control and company scope; (6) what Thai VAT and withholding reporting would need from this layer (candidates only, tied to TXS identifiers).

**Headline findings (all claim-backed below).**
1. The report layer in Community is a *definition store*: five models and their constraints, tag synchronisation, and formula validators. There is no evaluator for any of the six engines, no screen, menu, window action, client action, controller, cron, print template or export for any `account.report` (VDR-U31-C076 VDR-U31-C086). U24 stated this; this unit verifies it with the greps listed in section 14 and widens it (viewer hook, upgrade prompt, empty menu containers, spreadsheet path).
2. Tax tags are the only part of the layer that is fully live in Community: tags are created from report rules, written onto journal items while a document is draft, carry no sign (the sign is a leading minus in the report rule), net credit notes by amount sign, and are re-applied to history only by an optional tool that is not installed.
3. The closing flag (`use_in_tax_closing`), the tax-group payable and receivable accounts, the tax lock date help text, the `previous_return_period` date scope and the carry-over fields all describe a closing and return process whose implementation is not in Community.
4. Correction recorded as CONTRA: the Thai report data holds 29 expressions, not 24 plus 5 generic (VDR-U31-C101).

**Function-ID mapping.** The existing index (53 ids) has no entry for reports, tags, tag lifecycle or returns. `PCO-F01` (lock dates) is used only on tax-lock claims; `PCO-F02` (fiscal year and period) only on return-period and date-scope claims; every other claim is `FUNCTION MAPPING REQUIRED`.

| Capability | Function-ID(s) | Note |
|---|---|---|
| CAP-U31-01 Report definition structure | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U31-02 Computation methods (rules) | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U31-03 Running, displaying, exporting, filing (absence inventory) | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U31-04 Thai report definitions as supplied | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U31-05 Tag provisioning, naming, country scope | FUNCTION MAPPING REQUIRED | no index entry |
| CAP-U31-06 Tag application to journal items | PCO-F01 on the tax-lock claims only; otherwise FUNCTION MAPPING REQUIRED | lock-date index entry matches only the lock claims |
| CAP-U31-07 Cash-basis tags | PCO-F01 on one reversal-date claim; otherwise FUNCTION MAPPING REQUIRED | |
| CAP-U31-08 Re-applying tags | PCO-F01 on two lock claims only | |
| CAP-U31-09 Closing flag, return period, date scope, carry-over | PCO-F01 (tax lock) and PCO-F02 (return period, date scope) on matching claims only | |
| CAP-U31-10 Access, company scope, audit | FUNCTION MAPPING REQUIRED | |

**Method.** Full read of `account/models/account_report.py` (967 lines) and `account_account_tag.py` (140 lines); targeted reads of `account_tax.py` (tag paths, repartition line, closing flag, constraints), `account_move.py` and `account_move_line.py` (tag fields, lock checks, reversal, sync), `account_partial_reconcile.py` (cash-basis tags), `chart_template.py` (tag mapper), `company.py`, the security files and menus, the Thai report data, the Thai tax and tax-group templates, the update-tags wizard, `spreadsheet_account`. DB queried for counts, constraints, ACL, record rules, menus, actions, module states. Absence claims are `UNKNOWN` with a grep log (section 14).

## CAP-U31-01 Report definition structure

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Lets a country package describe a tax return (or any report) as stored data: sections, numbered lines, per-line computation rules, display columns, and national variants of a generic report, so tag names, line labels and formulas stay consistent (VDR-U31-C001 VDR-U31-C007). The definition says nothing about who runs it or how it is shown.

### D2 Architecture, data, objects
Five models in one file: report (VDR-U31-C001), line (VDR-U31-C002), expression/rule (VDR-U31-C003), column (VDR-U31-C004) and external value (VDR-U31-C005). Report owns lines and columns (VDR-U31-C006); variants point to a root (VDR-U31-C007); composite reports list sections (VDR-U31-C008); availability by country, chart or always (VDR-U31-C011 VDR-U31-C012); 15 viewer-filter switches with inheritance from root or main report (VDR-U31-C015 VDR-U31-C016); other options (VDR-U31-C017 VDR-U31-C018 VDR-U31-C019 VDR-U31-C020). Lines form a tree (VDR-U31-C025) with unique code per report (VDR-U31-C026), hierarchy level derived from the parent (VDR-U31-C027), optional groupby (VDR-U31-C028) and display flags (VDR-U31-C032). Rules are unique per line and label (VDR-U31-C033). Columns link to a rule label by text (VDR-U31-C034 VDR-U31-C035 VDR-U31-C036).
Seeded generic data: three reports without lines (VDR-U31-C039 VDR-U31-C040); Thai variants are in CAP-U31-04.

### D3 Source/technical/workflow logic
Constraints: variants one level deep (VDR-U31-C009), sections one level deep (VDR-U31-C010), country availability needs a country (VDR-U31-C013), parent before child (VDR-U31-C030), no self-parent (VDR-U31-C031), no children under a groupby parent (VDR-U31-C029), delete refused with variants (VDR-U31-C023). Copy rewrites codes (VDR-U31-C021 VDR-U31-C022). Report write on country change moves or creates tags (CAP-U31-05).
State machine (definition record): `created -> edited [write; tags synchronised for tag rules] -> copied [copy; codes suffixed] -> deleted [unlink; refused if variants exist]`. Columns are not removed with a deleted report (VDR-U31-C037).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Data file or ORM call creates report, lines, rules, columns; constraints pass (VDR-U31-C001 VDR-U31-C006 VDR-U31-C025). |
| 2 Reversal / negative | Delete refused with variants (VDR-U31-C023); orphan columns possible on delete (VDR-U31-C037); invalid parent order, self-parent, groupby with children refused (VDR-U31-C030 VDR-U31-C031 VDR-U31-C029). |
| 3 Multi-company / data-scope | No company on report, line, rule, column; shared data scoped by country; only external values have a company (VDR-U31-C255 VDR-U31-C005). |
| 4 Side effects | Rule create or write creates, renames or archives tags (CAP-U31-05); report country change moves tags (VDR-U31-C123). |
| 5 Configuration and optionality | Availability (VDR-U31-C011), viewer switches (VDR-U31-C015), defaults (VDR-U31-C018 VDR-U31-C019); variants inherit defaults (VDR-U31-C016). |
| 6 Validation and constraints | See D3 list; database uniqueness of line code and rule label (VDR-U31-C026 VDR-U31-C033). |
| 7 Roles and permissions | Read: basic, read-only, administrator groups; write: administrator only; invoicing and plain internal users none (VDR-U31-C247). |
| 8 Scheduled / automated | NOT APPLICABLE - no cron or automation on these models (VDR-U31-C038). |
| 9 Exception and failure | ValidationError and UserError messages on the constraints above; module uninstall bypasses the variant-delete guard (VDR-U31-C023). |
| 10 Accounting, audit, compliance | Definitions are not tracked (VDR-U31-C024); changes can silently alter tags (VDR-U31-C120); no accounting entry is created by this capability. |

### DB reconciliation (config only)
5 models in the DB (VDR-U31-C038): 6 reports (1 generic root, 2 generic variants, 3 Thai variants), 24 lines, 29 expressions, 9 columns, 0 external values, 0 section links. ACL rows 14 (report 3, line 3, expression 3, column 3, external value 2) equal source rows 129-143 (VDR-U31-C247 VDR-U31-C248); record rules: external value only (VDR-U31-C255); cron 0, automation 0, window action 0, view 0 (VDR-U31-C038). Constraints present: line code unique, rule label unique, domain-engine subformula check (VDR-U31-C026 VDR-U31-C033 VDR-U31-C052).

### Unknown / Runtime list
Presentation of lines and switches (no viewer in scope) - `RT`. Whether orphan columns can arise in practice - not executed.

## CAP-U31-02 Computation methods a report line can declare

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Each report line holds one or more computation rules. A rule says where its number would come from: journal items matched by a stored condition, journal items carrying tax grid tags, an arithmetic combination of other rules, account-code prefixes, a value entered by a user, or a custom routine (VDR-U31-C041). In Community only the *declaration* and its save-time validation exist; the numbers are produced by a layer that is not in the edition (VDR-U31-C063).

### D2 Architecture, data, objects
Engine selection (VDR-U31-C041 VDR-U31-C042); formula and subformula fields; shortcut fields on the line per engine (VDR-U31-C050 VDR-U31-C049 VDR-U31-C051); date scope (CAP-U31-09); figure type, growth flag, blank-if-zero, auditable (VDR-U31-C059 VDR-U31-C058); external values store (VDR-U31-C005).

### D3 Source/technical/workflow logic
Save-time checks: domain formula parsed with literal_eval and test-searched (VDR-U31-C043); account_codes tokens against a regex that also admits a tag reference (VDR-U31-C044 VDR-U31-C045); aggregation formula fully matched against a numeric and line_code.label grammar, with sum_children as the only keyword (VDR-U31-C046 VDR-U31-C047); tag, external and custom formulas unchecked (VDR-U31-C048). Constraints: domain engine needs a subformula (VDR-U31-C052); aggregation or external rule refused on a groupby line (VDR-U31-C053); cross-report cannot reference itself (VDR-U31-C054). Helpers: dependency expansion (VDR-U31-C055 VDR-U31-C056 VDR-U31-C057) without a caller in Community (VDR-U31-C061); external value rows never created or read in Community (VDR-U31-C062); a tag reports whether its rule negates (VDR-U31-C060).
State machine (rule): `declared -> validated [save: engine-specific check] -> (evaluated) [NOT PRESENT]`; shortcut write replaces or deletes the generated balance rule (VDR-U31-C050).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | A valid rule saves; tax_tags rules create tags (CAP-U31-05) (VDR-U31-C041 VDR-U31-C046). |
| 2 Reversal / negative | Invalid formula raises ValidationError (VDR-U31-C043 VDR-U31-C044 VDR-U31-C046); shortcut set to empty deletes its rule (VDR-U31-C050). |
| 3 Multi-company | Rules are shared (no company); external values are company-scoped (VDR-U31-C255 VDR-U31-C254). |
| 4 Side effects | tax_tags rules create or rename tags (VDR-U31-C113 VDR-U31-C118). |
| 5 Configuration and optionality | Custom needs a routine from another package (VDR-U31-C064); aggregations can cross reports (VDR-U31-C056). |
| 6 Validation and constraints | As D3; tag, external, custom unvalidated (VDR-U31-C048). |
| 7 Roles and permissions | Administrator edits (VDR-U31-C247). |
| 8 Scheduled / automated | NOT APPLICABLE - nothing evaluates rules on a schedule (VDR-U31-C063). |
| 9 Exception and failure | UserError for malformed or self cross-report (VDR-U31-C054); unknown tag names do not fail: a new tag is created (VDR-U31-C113). |
| 10 Accounting, audit, compliance | No figure can be derived from the shipped edition; domain formulas are not executed as code (VDR-U31-C262). |

### DB reconciliation (config only)
29 expressions (all Thai): tax_tags 13, aggregation 15, external 1; domain, account_codes and custom 0 (VDR-U31-C101). 24 have data identifiers, 5 are generated from line shortcuts (VDR-U31-C102). 0 external value rows (VDR-U31-C038).

### Unknown / Runtime list
VDR-U31-C063 (numeric results, sub-formula semantics, rounding, treatment of the negation prefix); VDR-U31-C064. `RT`.

## CAP-U31-03 Running, displaying, exporting and filing a report (entry points and what is absent)

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A Thai entity must produce monthly VAT returns, withholding returns, tax books and certificates (statutory register S09, S13, S15). This capability inventories what Community offers to run or show a tax report: the answer is that nothing runs, shows, exports or files an `account.report` definition (VDR-U31-C076 VDR-U31-C086).

### D2 Architecture, data, objects
What exists: the definition store (CAP-U31-01); a viewer lookup hook (VDR-U31-C065); a settings upgrade prompt for a dynamic-reports module that is not in the tree or the DB (VDR-U31-C068 VDR-U31-C069 VDR-U31-C070); empty menu containers (VDR-U31-C071 VDR-U31-C072); management analyses unrelated to tags (VDR-U31-C073); invoice-type print actions (VDR-U31-C074 VDR-U31-C075); a tax-details query helper used only by tests (VDR-U31-C081); an exigible-lines domain with no caller (VDR-U31-C082); an installed spreadsheet formula package and one dashboard that read ledger balances by account code or account tag, not by tax grid tag (VDR-U31-C077 VDR-U31-C078 VDR-U31-C079 VDR-U31-C080).

### D3 Source/technical/workflow logic
Control flow of a would-be report: definition (CAP-U31-01) -> [viewer: NOT PRESENT] -> [engine: NOT PRESENT] -> [export or filing: NOT PRESENT]. The only live code that mentions a viewer asks whether a client action of kind `account_report` carries the report id (VDR-U31-C065); the DB has none (VDR-U31-C066); a web test builds its own (VDR-U31-C067). Greps that establish absence are in section 14 (VDR-U31-C086 VDR-U31-C087). A foreign pack extends `account.report` with a viewer hook whose base method is not defined here (VDR-U31-C083) and its test is the only caller of an evaluator (VDR-U31-C084) - both labelled FOREIGN, evidence that the viewer is expected from a package outside Community.
State machine: NOT APPLICABLE - no report run, period or return state exists in Community.

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | NOT PRESENT: no path from definition to figure (VDR-U31-C086). |
| 2 Reversal / negative | NOT APPLICABLE. |
| 3 Multi-company / data-scope | Spreadsheet formulas take a company id and read through the ORM under caller rights (VDR-U31-C263); menu containers are group-gated (VDR-U31-C071). |
| 4 Side effects | None. |
| 5 Configuration and optionality | Upgrade switch for a package outside Community (VDR-U31-C068); spreadsheet package is auto-install (VDR-U31-C079). |
| 6 Validation and constraints | NOT APPLICABLE. |
| 7 Roles and permissions | Reporting menu visible to read-only accounting and invoicing groups (VDR-U31-C071); dashboard to the same groups (VDR-U31-C080). |
| 8 Scheduled / automated | None: cron 0 and automation 0 on the report models (VDR-U31-C076). |
| 9 Exception and failure | NOT APPLICABLE; the viewer lookup silently returns none (VDR-U31-C066). |
| 10 Accounting, audit, compliance | A reader may assume Thai returns exist because definitions do (VDR-U31-C085); statutory filing, e-filing, certificates and books are absent (VDR-U31-C087); see section 11 for candidates. |

### DB reconciliation (config only)
Window actions, server actions, views (except 3 tag views), cron, automation on the report models: 0 (VDR-U31-C076). Client actions 5, none for reports (VDR-U31-C066). Menu containers Partner Reports, Taxes and Fiscal, Statement Reports have no children; Management has 3 (VDR-U31-C072). Print actions in the account family: 6 plus the Thai commercial invoice (VDR-U31-C074 VDR-U31-C075). Modules: `account_reports` has no row; `spreadsheet_account`, `spreadsheet_dashboard`, `spreadsheet_dashboard_account` installed (VDR-U31-C070 VDR-U31-C079).

### Unknown / Runtime list
VDR-U31-C088: behaviour of the outside package. `RT`.

## CAP-U31-04 Thai VAT and withholding report definitions as supplied

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
The Thai package ships three report definitions whose layout follows the structure of a monthly VAT return and of the two withholding summaries by payee type (VDR-U31-C089 VDR-U31-C091 VDR-U31-C099 VDR-U31-C100). They are data only (CAP-U31-03). Whether they match current statutory forms is a legal question (VDR-U31-C106); this unit describes structure, not law.

### D2 Architecture, data, objects
- Tax Report: variant of the generic tax report, country Thailand, availability country, foreign VAT allowed, one balance column (VDR-U31-C089 VDR-U31-C090). 16 lines: four section lines (output tax, input tax, value added tax, net tax) each aggregating children (VDR-U31-C091) and 12 numbered lines.
- Tag rules on lines 1, 2, 3, 5 (negated) and 6, 7, 10 (not negated) (VDR-U31-C092 VDR-U31-C093); aggregation lines 4, 8, 9, 11, 12 (VDR-U31-C094 VDR-U31-C095); line 10 combines an external most-recent value with date scope previous return period, a tag and a sum (VDR-U31-C097); line 12 has partial results and a carry-over target pointing at line 10 (VDR-U31-C098).
- PND53 and PND3: four lines each, three tag rules and one aggregation (VDR-U31-C099 VDR-U31-C100).
- Hard-coded currency THB in positive-part subformulas (VDR-U31-C096); Thai translations shipped for names but language inactive (VDR-U31-C104).
- Counts: 3 reports, 24 lines, 29 expressions, 3 columns (VDR-U31-C101 VDR-U31-C102).

### D3 Source/technical/workflow logic
Data load: report records -> lines -> rules; each tag rule creates its tag on create (CAP-U31-05); shortcut `aggregation_formula` on five lines generates five rules without data identifiers (VDR-U31-C102). Template tax rows then name the same tags by text so the template loader can map them (VDR-U31-C129); the surcharge tags and the carried-forward tag are on no tax (VDR-U31-C103).
Sign convention: output-side rules negate; input-side and all withholding rules do not (VDR-U31-C092 VDR-U31-C093 VDR-U31-C099); on a vendor bill the withholding tax line is credit-negative so the raw value of those tag rules is negative (VDR-U31-C105) - presentation sign is an open item for the evaluator.
State machine: NOT APPLICABLE (static definitions).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Module install loads definitions and tags; no figure is produced (VDR-U31-C089 VDR-U31-C101). |
| 2 Reversal / negative | Credit notes net automatically through same tags and opposite amounts (CAP-U31-06); no correction-return structure in the definitions (VDR-U31-C091). |
| 3 Multi-company / data-scope | Shared definitions, available where the company fiscal country is Thailand (VDR-U31-C089 VDR-U31-C257); foreign VAT allowed on the main report (VDR-U31-C089). |
| 4 Side effects | Creates 13 tax tags (VDR-U31-C139). |
| 5 Configuration and optionality | Optional carry-forward (line 10 and 12) needs an external value mechanism not present (VDR-U31-C097 VDR-U31-C242). |
| 6 Validation and constraints | Parent-first order and unique codes satisfied by the data (VDR-U31-C030 VDR-U31-C026); aggregation grammar satisfied (VDR-U31-C046). |
| 7 Roles and permissions | Administrator edits; basic and read-only read (VDR-U31-C247). |
| 8 Scheduled / automated | None (VDR-U31-C038). |
| 9 Exception and failure | A tag name mistyped between report and tax template stops chart loading (VDR-U31-C130). |
| 10 Accounting, audit, compliance | Statutory fit UNKNOWN (VDR-U31-C106); withholding rules read tags with no negation (VDR-U31-C105); surcharges only by manual tagging (VDR-U31-C103). |

### DB reconciliation (config only)
Reports 3 / lines 24 (16+4+4) / expressions 29 (13 tax_tags, 15 aggregation, 1 external; 24 with data identifiers, 5 generated) / columns 3; source declares 24 line records and 24 explicit expression records, plus 5 shortcut-generated rules (VDR-U31-C101). **CONTRA** to U24 section 10 text ("Thai 24 expressions + 5 generic"; summary row "expressions 24 (source = DB)") and to the TXC reconciliation table row ("24 (+5 from account module)"): generic reports have no lines or expressions; the 5 are Thai. Tags 13, tag-to-rule match 1:1 by name (VDR-U31-C139); 10 tags used on 60 distribution links, 3 unused (VDR-U31-C103).

### Unknown / Runtime list
VDR-U31-C106; VDR-U31-C105. `RT`.

## CAP-U31-05 Provisioning, naming and country scope of tax grid tags

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Tax grid tags are the bridge between tax configuration and report lines: a tag marks a journal item as belonging to a return box. Tags are named after report rules, bound to a country, never carry a sign, and can be archived but not deleted while in use (VDR-U31-C107 VDR-U31-C108 VDR-U31-C113).

### D2 Architecture, data, objects
Tag record (VDR-U31-C107); unique per name, applicability, country (VDR-U31-C109 VDR-U31-C110); computed link to the rule and negate flag (VDR-U31-C108 VDR-U31-C111 VDR-U31-C112); relation to distribution lines and journal items restricted on delete (VDR-U31-C125 VDR-U31-C126); form-level country domain (VDR-U31-C127 VDR-U31-C128); product and account tags (VDR-U31-C137 VDR-U31-C138); master cash-flow tags (VDR-U31-C124).

### D3 Source/technical/workflow logic
Provisioning: rule create or engine change -> tag created in the report country if missing, name without minus (VDR-U31-C113 VDR-U31-C114 VDR-U31-C115 VDR-U31-C116 VDR-U31-C117). Rename: formula change on all users renames, else new tag (VDR-U31-C118 VDR-U31-C119) with silent effect on history (VDR-U31-C120). Delete: last rule removed -> archive if journal items carry the tag else delete; removed from distribution lines (VDR-U31-C121 VDR-U31-C122); a recreated rule reuses the archived tag (VDR-U31-C143). Country change of a report: move or duplicate tags (VDR-U31-C123). Templates: tags are only mapped by name, never created; missing name stops the load unless ignored (VDR-U31-C129 VDR-U31-C130 VDR-U31-C131 VDR-U31-C132 VDR-U31-C133). Translation: copied from line labels on tag create and on language load (VDR-U31-C134 VDR-U31-C135 VDR-U31-C136). Upgrade protection helper (VDR-U31-C141 VDR-U31-C140).
State machine (tag): `absent -> active [rule saved] -> renamed [all rules changed] -> archived [last rule deleted, in use] -> absent [last rule deleted, unused or manual delete]`; `archived -> (reused by recreated rule, stays archived)` (VDR-U31-C143).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Install country package: rules create tags; chart template maps tag names on taxes (VDR-U31-C113 VDR-U31-C129). |
| 2 Reversal / negative | Delete rule -> archive or unlink (VDR-U31-C121); missing tag name raises redirect warning (VDR-U31-C130); delete of a used tag blocked (VDR-U31-C126). |
| 3 Multi-company / data-scope | Tags are shared by all companies, scoped by country; display adds country code only with foreign VAT (VDR-U31-C107 VDR-U31-C256); distribution-line choice filtered by company fiscal and foreign VAT countries in the form only (VDR-U31-C127 VDR-U31-C128). |
| 4 Side effects | Translation SQL on create and language load (VDR-U31-C135 VDR-U31-C136). |
| 5 Configuration and optionality | Product and account purposes (VDR-U31-C137 VDR-U31-C138); ignore-missing context (VDR-U31-C131). |
| 6 Validation and constraints | Unique constraint (VDR-U31-C109); null-country duplicates possible (VDR-U31-C110); master tags undeletable (VDR-U31-C124). |
| 7 Roles and permissions | Full accounting group edits tags; internal users read (VDR-U31-C249). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure | RedirectWarning on missing tag (VDR-U31-C130); name-only matching can mis-resolve (VDR-U31-C111). |
| 10 Accounting, audit, compliance | Renaming or archiving changes how posted entries are read and is not logged (VDR-U31-C120 VDR-U31-C265); country FK set null turns tags global (VDR-U31-C142). |

### DB reconciliation (config only)
16 tags: 3 account-purpose master tags with data identifiers; 13 Thai tax tags (no identifiers), all country Thailand; unique constraint present; every tag_tags rule has its tag and every tax tag has a rule (VDR-U31-C139); 60 distribution links over 10 tags (VDR-U31-C103); the hook has nothing to protect (VDR-U31-C140). ACL rows (6 on tag in the DB: internal user, accounting user, read-only, invoicing, salesman, purchase user) equal source rows (VDR-U31-C249 VDR-U31-C250 VDR-U31-C251). No window action or menu opens the tag views (VDR-U31-C076).

### Unknown / Runtime list
VDR-U31-C144; reuse of an archived tag in practice (VDR-U31-C143). `RT`.

## CAP-U31-06 Applying tax grid tags to journal items (documents, credit notes, entries, reversals)

**Function-ID(s):** PCO-F01 on the tax-lock claims only; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
When an invoice, bill, credit note or tax entry is built, each journal item receives the tags of the tax distribution that produced it, so that a report summing tagged balances reproduces the return boxes. Credit notes and reversals use the same tags with opposite amounts, so they net automatically; the displayed sign comes from the rule (VDR-U31-C146 VDR-U31-C154).

### D2 Architecture, data, objects
Journal item tags (VDR-U31-C145); engine paths for base and tax lines, product tags, include-base (VDR-U31-C146 VDR-U31-C147 VDR-U31-C148 VDR-U31-C149); invoice or refund choice (VDR-U31-C150 VDR-U31-C151 VDR-U31-C152 VDR-U31-C153); grouping key includes tags (VDR-U31-C156); updates written with amounts (VDR-U31-C155); rounding and early-payment lines (VDR-U31-C160 VDR-U31-C161); expenses (VDR-U31-C163); distribution constraints (VDR-U31-C171 VDR-U31-C172 VDR-U31-C173).

### D3 Source/technical/workflow logic
Flow: tax distribution lines (VDR-U31-C177) -> engine adds tags to base and tax lines (VDR-U31-C146 VDR-U31-C148) -> synchronised onto draft move lines only (VDR-U31-C157 VDR-U31-C155) -> posting changes no tags (VDR-U31-C158) -> after posting, edits to balance, tax or tags are checked against the tax lock date (VDR-U31-C167 VDR-U31-C168 VDR-U31-C169) and tax edits are refused (VDR-U31-C170). Reversal: invoice copied with opposite type and recomputed with refund distribution (VDR-U31-C164); entries copied with tags and negated amounts (VDR-U31-C165 VDR-U31-C166). Reverse charge uses negative-factor lines and no base tags (VDR-U31-C174 VDR-U31-C175). Zero-amount tax lines are dropped (VDR-U31-C162). No propagation of tag changes to existing lines (VDR-U31-C176).
State machine (journal item tags): `untagged -> tagged [draft sync: tax set or recomputed] -> tagged (posted, frozen except by tool) -> cleared [all taxes removed on a non-posted entry]` (VDR-U31-C159); `posted -> edit refused or lock-checked [tax lock date]` (VDR-U31-C168).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Invoice with Output VAT 7%: base line gets sales-amount tag, tax line gets output-tax tag (VDR-U31-C146 VDR-U31-C148; Thai tax set in CAP-U31-04). |
| 2 Reversal / negative | Credit note uses refund distribution; reversal of entry negates amounts keeping tags (VDR-U31-C150 VDR-U31-C165 VDR-U31-C166); tags cleared when taxes removed (VDR-U31-C159). |
| 3 Multi-company / data-scope | Tags shared by company; items company-scoped (U11); tag choice by fiscal country in the form (VDR-U31-C127). |
| 4 Side effects | Tags change what a tax report would count; tax line grouping splits by tag (VDR-U31-C156). |
| 5 Configuration and optionality | Tags only if the tax distribution carries tags (VDR-U31-C177); product tags optional (VDR-U31-C147). |
| 6 Validation and constraints | Distribution rules (VDR-U31-C171 VDR-U31-C172 VDR-U31-C173); tax edits on posted lines refused (VDR-U31-C170); lock-date check (VDR-U31-C167). |
| 7 Roles and permissions | Posting and editing follow invoice and accounting groups (U11, U12); tag field is read-only technical in views (U13). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure | UserError when taxes of a posted line are edited or the tax lock date is violated (VDR-U31-C170 VDR-U31-C168). |
| 10 Accounting, audit, compliance | Tag edits after first posting are logged (VDR-U31-C260); hash does not cover tags (TXA2 C189); presentation sign and withholding sign open (VDR-U31-C179 VDR-U31-C105); manual entries with mixed taxes default by sign (VDR-U31-C178). |

### DB reconciliation (config only)
No journal items in the DB (0 moves, 0 lines). Tax distribution: 72 lines (36 invoice, 36 refund), 36 tax-type, 12 flagged for closing; 60 tag links (VDR-U31-C103 VDR-U31-C219). 0 taxes with include-base. Tracking: `tax_tag_ids` tracked (VDR-U31-C259 VDR-U31-C260).

### Unknown / Runtime list
VDR-U31-C182; VDR-U31-C166; VDR-U31-C179. `RT`.

## CAP-U31-07 Cash-basis exigibility and its tags

**Function-ID(s):** PCO-F01 on one reversal-date claim; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
For taxes due on payment, tags must reach the report when the payment is made, not when the invoice is posted. Community does this with a separate cash-basis entry per partial reconciliation. The Thai company has the switch on but every Thai tax is due on invoice, so the path is dormant (VDR-U31-C183 VDR-U31-C185 VDR-U31-C200).

### D2 Architecture, data, objects
Company switch and tax field (VDR-U31-C183 VDR-U31-C184); move flags (VDR-U31-C187); cash-basis entry model fields (origin move, partial) (VDR-U31-C188); base and tax line builders (VDR-U31-C190 VDR-U31-C191); constraints (VDR-U31-C194 VDR-U31-C195); exigible-lines domain with no caller (VDR-U31-C082); report switch only-exigible (VDR-U31-C196); tax-details helper (VDR-U31-C197); payment-time withholding add-on, uninstalled (VDR-U31-C198 VDR-U31-C199).

### D3 Source/technical/workflow logic
Invoice time: tags of on-payment taxes omitted (VDR-U31-C186); non-invoice moves always exigible and tagged (VDR-U31-C187). Payment time: partial reconcile -> cash-basis entry dated settlement date or after fiscal lock (VDR-U31-C188 VDR-U31-C189) with tags (VDR-U31-C190 VDR-U31-C191). Undo reconciliation: reverse the cash-basis entries in the origin period or after lock (VDR-U31-C192 VDR-U31-C193). Mixing on one line forbidden when tags are shared (VDR-U31-C194); mixed-currency entries unsupported (VDR-U31-C195).
State machine: `invoice posted (no caba tags) -> partial reconciled [cash-basis entry posted with tags] -> unreconciled [cash-basis entry reversed]`.

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | NOT EXERCISED in Thai configuration; mechanism per D3 (VDR-U31-C185). |
| 2 Reversal / negative | Unreconcile reverses the cash-basis entry (VDR-U31-C192 VDR-U31-C193). |
| 3 Multi-company / data-scope | Cash-basis journal and base account are company fields (VDR-U31-C183). |
| 4 Side effects | Creates an extra journal entry per partial (VDR-U31-C188). |
| 5 Configuration and optionality | Company switch plus per-tax exigibility (VDR-U31-C183 VDR-U31-C184). |
| 6 Validation and constraints | Tag-sharing constraint, single-currency limitation (VDR-U31-C194 VDR-U31-C195). |
| 7 Roles and permissions | Follows reconciliation rights (U12). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure | ValidationError on tag sharing (VDR-U31-C194). |
| 10 Accounting, audit, compliance | Dormant for Thailand; payment-time withholding would activate it (VDR-U31-C200 VDR-U31-C198); the update-tags tool ignores exigibility (CAP-U31-08). |

### DB reconciliation (config only)
Company cash-basis switch true; 18 taxes all on_invoice (VDR-U31-C185); report only-exigible true on 6 of 6 (VDR-U31-C196); cash-basis journal exists (TXA2 C215). `l10n_account_withholding_tax` uninstalled (VDR-U31-C198).

### Unknown / Runtime list
VDR-U31-C201; VDR-U31-C199. `RT`.

## CAP-U31-08 Re-applying tags to existing journal items

**Function-ID(s):** PCO-F01 on two lock claims only; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
After a legal or configuration change of tax grids, history must be re-tagged. Community has no automatic propagation (VDR-U31-C176 VDR-U31-C204); the only path is an optional administrator tool, not installed here (VDR-U31-C202 VDR-U31-C203). This unit re-reads it (U23 covered it) and adds two inference risks.

### D2 Architecture, data, objects
One transient model, one SQL method, a settings button, an ACL row (VDR-U31-C212); no record rules.

### D3 Source/technical/workflow logic
Settings (debug) -> wizard -> default date from tax lock date (VDR-U31-C211) -> multi-parent guard (VDR-U31-C210) -> one SQL statement: select target tags (scope VDR-U31-C205; entry rule VDR-U31-C206; cash-basis origin VDR-U31-C207) -> delete all tag links (VDR-U31-C208) -> insert new (VDR-U31-C209) -> flush and invalidate (VDR-U31-C214); no state filter (VDR-U31-C215).
State machine: `wizard open -> update executed [irreversible] -> tags rewritten`; `wizard open -> refused [multi-parent child tax]`.
New inferences (not in U23): product-purpose tags are deleted and not re-inserted (VDR-U31-C216); on-payment taxes are not skipped so the tool could add tags the engine deliberately omits (VDR-U31-C217).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Pick a date, press Update: tags realigned (VDR-U31-C208 VDR-U31-C209). |
| 2 Reversal / negative | Irreversible (VDR-U31-C213); only refusal is multi-parent (VDR-U31-C210). |
| 3 Multi-company / data-scope | One company per run (VDR-U31-C205); no rules (VDR-U31-C212). |
| 4 Side effects | Raw SQL: no tracking, no constraints, no log (VDR-U31-C214). |
| 5 Configuration and optionality | Optional add-on, debug-mode button (VDR-U31-C202). |
| 6 Validation and constraints | Only multi-parent check; lock date is a warning (VDR-U31-C211 VDR-U31-C210). |
| 7 Roles and permissions | Accounting administrator (VDR-U31-C212). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure | UserError on multi-parent (VDR-U31-C210); SQL errors generic. |
| 10 Accounting, audit, compliance | Rewrites history, all states (VDR-U31-C215); product-tag loss and on-payment tags are open risks (VDR-U31-C216 VDR-U31-C217). |

### DB reconciliation (config only)
Module uninstalled, wizard model absent (VDR-U31-C203). 0 rows seeded (U23 C190).

### Unknown / Runtime list
VDR-U31-C218. `RT`.

## CAP-U31-09 Tax closing flag, return periods, date scope and carry-over

**Function-ID(s):** PCO-F01 (tax lock) and PCO-F02 (return period, date scope) on matching claims only; otherwise FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
A monthly VAT return needs a period, a closing of tax balances, a carry-forward of excess input tax and a lock of the filed period. Community declares the vocabulary (a closing flag on distribution lines, payable and receivable accounts on tax groups, a tax lock date, a return-period option, date scopes, carry-over labels and fields) but ships no routine that uses it as a process (VDR-U31-C219 VDR-U31-C227 VDR-U31-C230 VDR-U31-C232 VDR-U31-C234 VDR-U31-C237).

### D2 Architecture, data, objects
Closing flag (VDR-U31-C219 VDR-U31-C220); tax group accounts (VDR-U31-C227 VDR-U31-C228); lock date (VDR-U31-C230); deprecated hook (VDR-U31-C231); return-period options and default opening (VDR-U31-C232 VDR-U31-C243); date scope (VDR-U31-C234 VDR-U31-C235 VDR-U31-C236); carry-over fields and constraints (VDR-U31-C237 VDR-U31-C238 VDR-U31-C239 VDR-U31-C240 VDR-U31-C241); tax-unit mode (VDR-U31-C244).

### D3 Source/technical/workflow logic
Closing flag readers (four, none a closing routine): analytic grouping (VDR-U31-C221), legacy compute interface (VDR-U31-C222), tax-details SQL (VDR-U31-C223), change log (VDR-U31-C224); list column (VDR-U31-C225); grep conclusion (VDR-U31-C226). Tax group accounts have no reader (VDR-U31-C229). Tax lock date has no writer (VDR-U31-C230). Return periods have no model or company field in the DB (VDR-U31-C233). Date scope is a six-value selection with default strict range; only Thai line 10 differs (VDR-U31-C234 VDR-U31-C235 VDR-U31-C236). Carry-over: labels with a carry prefix point to labels with an applied-carry prefix, by default on the same line (VDR-U31-C240 VDR-U31-C239 VDR-U31-C241); no caller of the target resolver (VDR-U31-C242); the Thai VAT line 10 and 12 use the convention (VDR-U31-C097 VDR-U31-C098).
State machine: NOT APPLICABLE in Community (no period, return or closing state). Documented candidate states `period open -> closed [closing entry] -> locked [tax lock date set]` exist only as help text (VDR-U31-C230 VDR-U31-C227).

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | NOT PRESENT: no closing, return or carry-forward routine (VDR-U31-C245). |
| 2 Reversal / negative | NOT APPLICABLE; lock date is manual; corrections after a lock need exceptions or later dating (U11, U13). |
| 3 Multi-company / data-scope | Tax-unit multi-company mode declared, no tax unit concept (VDR-U31-C244); external value company-scoped (VDR-U31-C254). |
| 4 Side effects | Flag affects analytic distribution on tax lines (VDR-U31-C221). |
| 5 Configuration and optionality | Flag editable per distribution line (VDR-U31-C219); defaults (VDR-U31-C220). |
| 6 Validation and constraints | Carry-over label rules (VDR-U31-C239 VDR-U31-C240 VDR-U31-C241). |
| 7 Roles and permissions | Administrator edits tax groups and flags (TXA1); external values administrators (VDR-U31-C248). |
| 8 Scheduled / automated | NOT APPLICABLE (VDR-U31-C245). |
| 9 Exception and failure | UserError when the applied-carry rule is missing (VDR-U31-C241). |
| 10 Accounting, audit, compliance | Month-end transfer of tax balances, carry-forward of excess input tax and lock-date advancement are manual (VDR-U31-C245 VDR-U31-C230); statutory links S09-01, S09-06, S09-07 (section 11). |

### DB reconciliation (config only)
Thai distribution lines: 72, flagged for closing 12 (all tax-type VAT lines) (VDR-U31-C219); 5 tax groups with payable and receivable set, advance unset (VDR-U31-C228); company lock dates all null; res_company has no return-periodicity column (VDR-U31-C233); all 6 reports default to previous return period (VDR-U31-C243); 1 of 29 rules has a non-default date scope (VDR-U31-C236); no external values.

### Unknown / Runtime list
VDR-U31-C245; VDR-U31-C246. `RT`.

## CAP-U31-10 Access control, company scope and audit of report and tag data

**Function-ID(s):** FUNCTION MAPPING REQUIRED

### D1 Business purpose and process semantics
Who may read or change report definitions, tags and external values; whether definitions follow companies; whether changes leave a trail.

### D2 Architecture, data, objects
ACL rows: report family (VDR-U31-C247), external value (VDR-U31-C248), tags (VDR-U31-C249 VDR-U31-C250 VDR-U31-C251), distribution lines (VDR-U31-C252). Record rule: external value only (VDR-U31-C253 VDR-U31-C254). No company on definitions or tags (VDR-U31-C255). Fiscal country selection (VDR-U31-C257 VDR-U31-C258). Tracking: journal item tags and tax distribution tracked; definitions not (VDR-U31-C260 VDR-U31-C261 VDR-U31-C259). Spreadsheet reads (VDR-U31-C263).

### D3 Source/technical/workflow logic
Access is by ACL group; shared definitions and tags are filtered by country only (VDR-U31-C256 VDR-U31-C257). Formula safety: domain formulas parsed, not executed (VDR-U31-C262). Edits to shared definitions and tag names are global and unlogged (VDR-U31-C264 VDR-U31-C265).
State machine: NOT APPLICABLE.

### Ten-dimension table
| Dimension | Statement |
|---|---|
| 1 Happy path | Accountant reads reports and tags; administrator edits definitions (VDR-U31-C247 VDR-U31-C249). |
| 2 Reversal / negative | AccessError for invoicing and plain users on definitions (VDR-U31-C247). |
| 3 Multi-company / data-scope | Definitions and tags shared; external values and entries per company (VDR-U31-C255 VDR-U31-C253). |
| 4 Side effects | One company's admin change affects all (VDR-U31-C264). |
| 5 Configuration and optionality | Fiscal country decides applicable reports and tag country (VDR-U31-C257 VDR-U31-C258). |
| 6 Validation and constraints | NOT APPLICABLE. |
| 7 Roles and permissions | See D2 rows; group names in DB: Basic, Show Accounting Features - Readonly, Show Full Accounting Features, Administrator, Invoicing (VDR-U31-C247 VDR-U31-C249). |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure | Standard access errors; none specific. |
| 10 Accounting, audit, compliance | No trail for definition changes although they alter reading of history (VDR-U31-C259 VDR-U31-C265); entry tag edits logged (VDR-U31-C260). |

### DB reconciliation (config only)
ACL rows in the DB equal source rows: report family 12, external value 2, tag 6 (source account 4 + sale 1 + purchase 1), distribution line 4 (VDR-U31-C247 VDR-U31-C248 VDR-U31-C249 VDR-U31-C252). Record rules on these models: tax, distribution line, external value only (VDR-U31-C255). Tracked fields on the report and tag models: 0 (VDR-U31-C259).

### Unknown / Runtime list
VDR-U31-C266. `RT`.

## 11. What Thai VAT and withholding reporting would need from this layer (candidates only)

Rule applied: a candidate is listed only where a verified statutory need exists in the TXS register or its supplement (`07_THAI_TAX_CORE/TXS_thai_statutory_source_register.md`, `07b_THAI_STATUTORY_REGISTER_SUPPLEMENT_TXS-R1.md`); identifiers below are TXS statement ids, not legal assertions. Community absence is not proof that a need does not exist; the `Class` column keeps Odoo behaviour and statutory need separate.

| Need (neutral) | TXS ids | What Community provides | Class | Candidate (Cat-ID) | Claim-IDs |
|---|---|---|---|---|---|
| Monthly VAT return figures by return box (sales, zero-rated, exempt, output tax, input tax, payable, excess) | S09-01, S09-02 | Tag definitions and a 16-line definition; tags written onto entries in draft; no evaluator, no period selection, no display | NATIVE GAP / EXTENSION REQUIRED | U31-F03, U31-F04 | VDR-U31-C091 VDR-U31-C146 VDR-U31-C063 VDR-U31-C086 |
| Return form output and filing data (PP 30, internet filing) | S09-02, S09-09 | None | NATIVE GAP / EXTENSION REQUIRED | U31-F05 | VDR-U31-C087 |
| Carry-forward of excess input tax and refund claim | S09-06 | Definition lines 9, 10, 12 and carry-over fields; no routine creates or reads carry-over values; no closing | NATIVE GAP / EXTENSION REQUIRED | U31-F15 | VDR-U31-C097 VDR-U31-C098 VDR-U31-C242 VDR-U31-C245 |
| Corrective (additional) return | S09-07 | Manual tax lock date only; no return record | NATIVE GAP / EXTENSION REQUIRED | U31-F15 | VDR-U31-C230 VDR-U31-C245 |
| Output tax and input tax books kept per document | S09-08, S15-01 | Tags carry no document reference; a details helper exists but is called only by tests | NATIVE GAP / EXTENSION REQUIRED | U31-F07 | VDR-U31-C081 VDR-U31-C087 |
| Branch-level return filing | S11-04 | Foreign-VAT permission on the report only; no branch return concept | UNKNOWN (overlaps U28) | U31-F05 | VDR-U31-C089 |
| Withholding returns by payee type (PND 3, PND 53) with remittance by month | S13-04, S13-08 | Four-line definitions with tags; withholding taxes tagged at the invoice; no evaluator, no remittance or filing | NATIVE GAP / EXTENSION REQUIRED | U31-F06 | VDR-U31-C099 VDR-U31-C100 VDR-U31-C087 |
| Withholding certificate to the payee | S13-02, S13-03 | None | NATIVE GAP / EXTENSION REQUIRED | U31-F06 | VDR-U31-C087 |
| Foreign-payee withholding return and reverse-charge VAT return | S13-04, S10-02 | No tax, tag, report or form (U24 C214) | NATIVE GAP / EXTENSION REQUIRED | U31-F08 | VDR-U31-C087 |
| Retention of tax documents and reports for the prescribed years | S15-02 | Posted entries persist; no retention or archive policy in this layer | UNKNOWN (outside this layer) | none | VDR-U31-C259 |

Direction of the extension (not a design): an evaluation layer that reads tax grid tags on posted entries per period and company; a display and export layer; return and carry-over records tied to the tax lock date; Thai filing data and certificate documents; tax books. Each must preserve the Odoo findings above: tags are unsigned, sign comes from the rule, credit notes net by amount sign, history is re-tagged only by an explicit tool, and the report definitions are shared across companies.

## REGISTER: Function Catalog

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Entry points / triggers | Claim-IDs | Statutory link (statutory-register id or n/a) | Native status |
|---|---|---|---|---|---|---|---|
| U31-F01 | Maintain report definitions as data (reports, variants, sections, lines, columns) | 9 | FUNCTION MAPPING REQUIRED | Data files and ORM calls; no screen or menu | VDR-U31-C001 VDR-U31-C007 VDR-U31-C025 VDR-U31-C034 VDR-U31-C076 | n/a | PARTIAL |
| U31-F02 | Declare computation rules and validate formulas at save time | 9 | FUNCTION MAPPING REQUIRED | Rule create and write | VDR-U31-C041 VDR-U31-C043 VDR-U31-C046 VDR-U31-C048 | n/a | PARTIAL |
| U31-F03 | Evaluate report rules into figures (tags, aggregation, domain, account codes, external values, custom) | 9 | FUNCTION MAPPING REQUIRED | none | VDR-U31-C063 VDR-U31-C061 VDR-U31-C062 | S09-01, S09-02, S15-01 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F04 | Display, print or export a tax report | 9 | FUNCTION MAPPING REQUIRED | none (viewer hook, empty menu containers, upgrade prompt) | VDR-U31-C065 VDR-U31-C071 VDR-U31-C068 VDR-U31-C086 | S09-01, S09-08, S15-01 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F05 | Produce VAT return filing data and file it | 9 | FUNCTION MAPPING REQUIRED | none | VDR-U31-C087 | S09-02, S09-09, S11-04 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F06 | Produce withholding returns (PND 3, PND 53) and payee certificates | 9 | FUNCTION MAPPING REQUIRED | definitions only | VDR-U31-C099 VDR-U31-C100 VDR-U31-C087 | S13-02, S13-03, S13-04, S13-08 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F07 | Output tax and input tax books per document | 9 | FUNCTION MAPPING REQUIRED | none | VDR-U31-C081 VDR-U31-C087 | S09-08, S15-01 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F08 | Foreign-payee withholding and reverse-charge VAT return data | 9 | FUNCTION MAPPING REQUIRED | none | VDR-U31-C087 | S10-02, S13-04 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F09 | Provision tax grid tags from report rules | 1 | FUNCTION MAPPING REQUIRED | Rule create, engine change, rule delete, report country change | VDR-U31-C113 VDR-U31-C118 VDR-U31-C121 VDR-U31-C123 | n/a | NATIVE |
| U31-F10 | Map tags by name in chart templates | 8 | FUNCTION MAPPING REQUIRED | Chart template load | VDR-U31-C129 VDR-U31-C130 VDR-U31-C132 | n/a | NATIVE |
| U31-F11 | Apply tags to journal items of invoices, bills, credit notes and tax entries | 1, 7 | FUNCTION MAPPING REQUIRED | Draft document tax synchronisation | VDR-U31-C146 VDR-U31-C148 VDR-U31-C150 VDR-U31-C157 | n/a | NATIVE |
| U31-F12 | Tags on reversal and credit notes (netting by amount sign) | 4, 7 | FUNCTION MAPPING REQUIRED | Reverse and credit note actions | VDR-U31-C164 VDR-U31-C165 VDR-U31-C166 VDR-U31-C154 | n/a | NATIVE |
| U31-F13 | Tags on cash-basis (payment-time) entries | 5, 7 | FUNCTION MAPPING REQUIRED | Partial reconcile | VDR-U31-C188 VDR-U31-C190 VDR-U31-C191 VDR-U31-C200 | S05-02 | PARTIAL |
| U31-F14 | Re-apply tags to existing entries after configuration change | 7, 9 | FUNCTION MAPPING REQUIRED | Optional administrator tool (not installed) | VDR-U31-C202 VDR-U31-C203 VDR-U31-C208 VDR-U31-C176 | n/a | PARTIAL |
| U31-F15 | Tax closing, return period and carry-forward of excess input tax | 5, 9 | PCO-F02 on return-period claims only; otherwise FUNCTION MAPPING REQUIRED | none | VDR-U31-C226 VDR-U31-C229 VDR-U31-C242 VDR-U31-C245 | S09-01, S09-06, S09-07 | NATIVE GAP / EXTENSION REQUIRED |
| U31-F16 | Tax lock date guarding tax-affecting entries and tag edits | 5 | PCO-F01 | Write, post, unlink on journal items | VDR-U31-C167 VDR-U31-C168 VDR-U31-C169 VDR-U31-C170 | n/a | NATIVE |
| U31-F17 | Access and company scope of report and tag data | 10 | FUNCTION MAPPING REQUIRED | ACL and record rules | VDR-U31-C247 VDR-U31-C249 VDR-U31-C248 VDR-U31-C255 | n/a | PARTIAL |
| U31-F18 | Audit trail of tag and definition changes | 10 | FUNCTION MAPPING REQUIRED | Tracking on entries and tax distribution | VDR-U31-C260 VDR-U31-C261 VDR-U31-C259 | n/a | PARTIAL |
| U31-F19 | Ledger balance spreadsheet formulas and invoicing dashboard | 12 | FUNCTION MAPPING REQUIRED | Spreadsheet package (installed) | VDR-U31-C077 VDR-U31-C078 VDR-U31-C080 | n/a | NATIVE |
| U31-F20 | Thai VAT and withholding report definitions as supplied | 9 | FUNCTION MAPPING REQUIRED | Thai package data load | VDR-U31-C089 VDR-U31-C091 VDR-U31-C099 VDR-U31-C101 VDR-U31-C106 | S09-01, S13-04 | PARTIAL |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Claim-IDs | Class |
|---|---|---|---|---|
| BR-U31-01 | A variant cannot have a variant, and a section cannot have sections | always | VDR-U31-C009 VDR-U31-C010 | CONSTRAINT |
| BR-U31-02 | A parent line precedes its children; no self-parent; no children under a groupby line | always | VDR-U31-C030 VDR-U31-C031 VDR-U31-C029 | CONSTRAINT |
| BR-U31-03 | Line code unique per report; rule label unique per line | always | VDR-U31-C026 VDR-U31-C033 | CONSTRAINT |
| BR-U31-04 | A report with variants cannot be deleted | outside module uninstall | VDR-U31-C023 | CONSTRAINT |
| BR-U31-05 | Country-match availability requires a country; a variant with country defaults to it | always | VDR-U31-C012 VDR-U31-C013 | CONSTRAINT |
| BR-U31-06 | Copy suffixes line codes and rewrites them inside formulas | on copy | VDR-U31-C021 VDR-U31-C022 | DERIVATION |
| BR-U31-07 | Domain, account-code and aggregation formulas are validated at save; tag, external, custom are not | always | VDR-U31-C043 VDR-U31-C044 VDR-U31-C046 VDR-U31-C048 | CONSTRAINT |
| BR-U31-08 | A domain rule needs a subformula; aggregation and external rules refused on groupby lines | always | VDR-U31-C052 VDR-U31-C053 | CONSTRAINT |
| BR-U31-09 | Tag rule formula is the tag name, a leading minus negates the displayed balance | tag_tags engine | VDR-U31-C060 VDR-U31-C114 | DERIVATION |
| BR-U31-10 | Saving a tag rule creates the tag in the report country if absent | rule create or engine change | VDR-U31-C113 VDR-U31-C116 VDR-U31-C117 | DERIVATION |
| BR-U31-11 | Tag name unique per purpose and country; null-country duplicates possible | always | VDR-U31-C109 VDR-U31-C110 | CONSTRAINT |
| BR-U31-12 | Formula change renames the tag only if all its rules change together | rule write | VDR-U31-C118 VDR-U31-C119 VDR-U31-C120 | DERIVATION |
| BR-U31-13 | Last rule deleted: tag archived if used on entries else deleted; removed from distribution lines | rule unlink | VDR-U31-C121 VDR-U31-C122 | DERIVATION |
| BR-U31-14 | Report country change moves or duplicates tags | report write | VDR-U31-C123 | DERIVATION |
| BR-U31-15 | Master cash-flow tags cannot be deleted; used tags cannot be deleted directly | always | VDR-U31-C124 VDR-U31-C125 VDR-U31-C126 | CONSTRAINT |
| BR-U31-16 | Distribution tag choice is filtered by fiscal and foreign VAT countries in the form only | form view | VDR-U31-C127 VDR-U31-C128 | CONFIG |
| BR-U31-17 | Chart templates map tags by name and never create them; missing name stops the load unless ignored | chart template load | VDR-U31-C129 VDR-U31-C130 VDR-U31-C131 VDR-U31-C132 | CONSTRAINT |
| BR-U31-18 | Tags are applied to lines while the document is draft; posting does not recompute | always | VDR-U31-C157 VDR-U31-C158 VDR-U31-C155 | DERIVATION |
| BR-U31-19 | Credit notes use refund distribution; entries choose by amount sign and tax purpose | always | VDR-U31-C150 VDR-U31-C151 VDR-U31-C152 VDR-U31-C153 | DERIVATION |
| BR-U31-20 | Tags carry no sign; credit notes net by amount; displayed sign is the rule's minus | always | VDR-U31-C154 VDR-U31-C060 VDR-U31-C108 | DERIVATION |
| BR-U31-21 | Invoice and refund distribution must match in count, order, basis and percentage; factors total 100 | always | VDR-U31-C171 VDR-U31-C172 VDR-U31-C173 | CONSTRAINT |
| BR-U31-22 | Reverse charge uses negative-factor lines and no base tags | reverse-charge tax | VDR-U31-C174 VDR-U31-C175 | DERIVATION |
| BR-U31-23 | Tax lines with zero amount are dropped; zero-rated sales carry base tags only | always | VDR-U31-C162 | DERIVATION |
| BR-U31-24 | Posted line edits of balance, tax or tags are tax-lock checked; tax edits refused | posted line | VDR-U31-C167 VDR-U31-C168 VDR-U31-C169 VDR-U31-C170 | CONSTRAINT |
| BR-U31-25 | Changing distribution tags does not change existing lines | always | VDR-U31-C176 VDR-U31-C204 | DERIVATION |
| BR-U31-26 | On-payment taxes carry no tag on the invoice; tags arrive on the cash-basis entry | tax on_payment | VDR-U31-C186 VDR-U31-C188 VDR-U31-C190 | DERIVATION |
| BR-U31-27 | On-payment and on-invoice taxes cannot share a tag on one line; mixed currencies unsupported | always | VDR-U31-C194 VDR-U31-C195 | CONSTRAINT |
| BR-U31-28 | The re-tag tool refuses multi-parent child taxes and has no other gate | tool installed | VDR-U31-C210 VDR-U31-C211 VDR-U31-C212 | CONSTRAINT |
| BR-U31-29 | The closing flag defaults true for tax-type lines on non-income, non-expense accounts and has no closing reader | always | VDR-U31-C220 VDR-U31-C226 | CONFIG |
| BR-U31-30 | Carry-over target only on carry-labelled rules and must point to applied-carry labels | always | VDR-U31-C239 VDR-U31-C240 VDR-U31-C241 | CONSTRAINT |
| BR-U31-31 | Report definitions: read by basic, read-only, administrator; write administrator only | always | VDR-U31-C247 | CONFIG |
| BR-U31-32 | Tags: internal users read; full accounting group writes | always | VDR-U31-C249 | CONFIG |
| BR-U31-33 | External values: company rule; basic group has no access | always | VDR-U31-C248 VDR-U31-C253 | CONFIG |

## REGISTER: Source and Override Map

| Concept | Base definition (module:file:line) | Overrides in installed Community modules (module:file:line) | Effective-behaviour condition | Claim-IDs |
|---|---|---|---|---|
| Report definition family | `account/models/account_report.py:45` | none in installed modules; one foreign pack (not installed) extends the report model: `l10n_in/models/l10n_in_report_handler.py:7` | always | VDR-U31-C001 VDR-U31-C083 |
| Tag model and its sync with rules | `account/models/account_account_tag.py:12` ; `account/models/account_report.py:711` | none (l10n_th models extend move, partner, report action, bank, chart template only): `l10n_th/models/account_move.py:5` | always | VDR-U31-C107 VDR-U31-C113 VDR-U31-C180 |
| Tag application by the tax engine | `account/models/account_tax.py:2413` ; `account/models/account_tax.py:2483` | hr_expense extends grouping keys with the expense id only: `hr_expense/models/account_tax.py:36`; expense path `hr_expense/models/hr_expense.py:1649` | account installed; hr_expense installed | VDR-U31-C146 VDR-U31-C148 VDR-U31-C181 VDR-U31-C163 |
| Journal item tag field and lock-date protection | `account/models/account_move_line.py:240` ; `account/models/account_move_line.py:3488` | none (grep of the method names) | always | VDR-U31-C145 VDR-U31-C167 VDR-U31-C169 |
| Cash-basis tag builders | `account/models/account_partial_reconcile.py:378` ; `account/models/account_partial_reconcile.py:430` | none | tax on_payment | VDR-U31-C190 VDR-U31-C191 |
| Chart template tag mapper | `account/models/chart_template.py:1246` | l10n_th supplies template data only: `l10n_th/models/template_th.py:41` | chart template load | VDR-U31-C129 VDR-U31-C185 |
| Thai report definitions | `l10n_th/data/account_tax_report_data.xml:3` | none | l10n_th installed | VDR-U31-C089 VDR-U31-C101 |
| Closing flag and tax group accounts | `account/models/account_tax.py:5341` ; `account/models/account_tax.py:39` | none; no reader beyond those listed | always | VDR-U31-C219 VDR-U31-C226 VDR-U31-C229 |
| Tag re-application | `account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:139` (module not installed) | n/a | module installed | VDR-U31-C208 VDR-U31-C203 |
| Ledger balance spreadsheet formulas | `spreadsheet_account/models/account.py:44` (extends account.account, installed) | n/a | spreadsheet_account installed | VDR-U31-C077 VDR-U31-C079 |
| Report viewer hook | `account/models/account_report.py:209` | none in Community | no client action exists | VDR-U31-C065 VDR-U31-C066 |

## REGISTER: State and Reversal

| Document/entity | State or event | Trigger | Reversal / cancel / correction path | Blocked when | Claim-IDs |
|---|---|---|---|---|---|
| Tax tag | created | tag rule saved or engine changed | rename (all users change) or archive/delete via rule delete | delete blocked while used on a line or distribution line | VDR-U31-C113 VDR-U31-C118 VDR-U31-C126 |
| Tax tag | archived | last rule deleted while entries carry it | recreate rule: archived tag reused, stays archived (inference) | n/a | VDR-U31-C121 VDR-U31-C143 |
| Tax tag | country moved or duplicated | report country changed | change country back (tags used by other reports kept) | n/a | VDR-U31-C123 |
| Journal item tags (draft document) | set or recomputed | tax synchronisation on draft | edit taxes in draft; tags cleared when taxes removed | posted document (no recomputation) | VDR-U31-C157 VDR-U31-C155 VDR-U31-C159 |
| Journal item tags (posted) | frozen | posting | edit refused or lock-checked; re-tag only by the optional tool | tax lock date on affected lines; tax edits refused | VDR-U31-C158 VDR-U31-C168 VDR-U31-C170 VDR-U31-C208 |
| Invoice | reversed | reverse action | credit note recomputed with refund distribution | lock rules (U11) | VDR-U31-C164 VDR-U31-C150 |
| Tax entry (manual) | reversed | reverse action | lines copied with tags, amounts negated | lock rules | VDR-U31-C165 VDR-U31-C166 |
| Cash-basis entry | created | partial reconcile | undo reconcile reverses it in origin period or after lock | mixed currencies unsupported | VDR-U31-C188 VDR-U31-C192 VDR-U31-C193 VDR-U31-C195 |
| Tag re-application run | executed | administrator presses Update | none (irreversible except backup) | multi-parent child tax | VDR-U31-C213 VDR-U31-C210 |
| Report definition | deleted | unlink | none | variants exist | VDR-U31-C023 |
| Return, period, closing (not present) | n/a | n/a | n/a | n/a | VDR-U31-C245 |

## REGISTER: Accounting Impact

| Event | Entries created or changed (neutral) | Tax lines / tags / accounts affected | Period/lock/date effect | Reversal effect | Claim-IDs |
|---|---|---|---|---|---|
| Post customer invoice or vendor bill with taxes | No new entry here; tag links on its base and tax lines | Base lines get base tags, tax lines get distribution tags; zero-amount tax lines dropped | Tax lock date applies to tax-affecting entries (U11) | Credit note uses refund distribution with the same tags | VDR-U31-C146 VDR-U31-C148 VDR-U31-C162 VDR-U31-C168 |
| Issue credit note | Lines with opposite amounts | Same tags, refund distribution | as above | n/a | VDR-U31-C150 VDR-U31-C154 |
| Manual entry with taxes | Lines tagged by amount sign and tax purpose | Invoice or refund distribution | as above | Reverse copies tags with negated amounts | VDR-U31-C152 VDR-U31-C153 VDR-U31-C165 |
| Thai withholding on a vendor bill | Tax line on a liability account, negative percent | Base tag Income PND53 or Income PND3, tax tag PND53 or PND3, no closing flag | as above | Credit note nets | VDR-U31-C105 VDR-U31-C099 |
| Payment of invoice with on-payment tax (dormant for Thailand) | Separate cash-basis entry per partial | Tags on base and tax lines at settlement date | Dated after the fiscal lock if needed | Unreconcile reverses it | VDR-U31-C188 VDR-U31-C189 VDR-U31-C192 VDR-U31-C200 |
| Edit of a report formula or country | No entry | Tags renamed, created, moved or archived; reading of posted entries changes | None | None | VDR-U31-C118 VDR-U31-C120 VDR-U31-C123 |
| Run of the re-tag tool | Tag links rewritten on selected entries | All tag links replaced from current distribution | Warning only for locked periods | Irreversible | VDR-U31-C208 VDR-U31-C211 VDR-U31-C213 |
| Month-end tax closing (not present) | None created | Closing flag unused; tax group counterpart accounts unused | Tax lock date manual | n/a | VDR-U31-C226 VDR-U31-C229 VDR-U31-C230 |

## 12. Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U31-C001 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | FACT | always | — | The report model is defined in the account module; its record is a report definition with name, sequence, active flag, lines, columns, root report, variants and sections. | N-U31-001 |
| VDR-U31-C002 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:350 | _name = 'account.report.line' | FACT | always | — | The report line model sits in the same source file as the report model. | N-U31-001 |
| VDR-U31-C003 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:580 | _name = 'account.report.expression' | FACT | always | — | The report expression model (computation rule) sits in the same file; its display name is the line name plus the rule label. | N-U31-001 |
| VDR-U31-C004 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:933 | _name = 'account.report.column' | FACT | always | — | The report column model sits in the same file. | N-U31-001 |
| VDR-U31-C005 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:948 | _name = 'account.report.external.value' | FACT | always | — | The external value model, the only one of the five with a company, sits in the same file; it is company-checked and ordered by date. | N-U31-001 |
| VDR-U31-C006 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:54 | line_ids = fields.One2many | FACT | always | — | A report owns its lines and its columns through two one-to-many links. | N-U31-001 |
| VDR-U31-C007 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:56 | this report is a variant of | FACT | always | — | root_report_id marks a report as a variant of a root report; variant_report_ids lists the variants. | N-U31-002 |
| VDR-U31-C008 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:58 | account_report_section_rel | FACT | always | — | Sections of a composite report are a many-to-many self-relation (main report to sub report); use_sections is computed from it. | N-U31-002 |
| VDR-U31-C009 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:237 | Only a report without a root | FACT | always | — | A constraint refuses a root report that itself has a root: variants are one level deep. | N-U31-007 |
| VDR-U31-C010 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:253 | cannot have sections themselves | FACT | always | — | A constraint refuses sections that themselves have sections. | N-U31-007 |
| VDR-U31-C011 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:73 | availability_condition = fields.Selection | FACT | always | — | availability_condition is country match, chart-of-accounts match or always; it is computed and stored, editable. | N-U31-013 |
| VDR-U31-C012 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:224 | report.availability_condition = 'country' | FACT | report is a variant and has a country | — | A variant with a country defaults to country-match availability, otherwise the default is always. | N-U31-012 |
| VDR-U31-C013 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:259 | is set to 'Country Matches' | FACT | always | — | Country-match availability without a country raises a validation error. | N-U31-012 |
| VDR-U31-C014 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:65 | chart_template = fields.Selection | FACT | always | — | A report can name a chart template (a selection of installed templates) and a country. | N-U31-013 |
| VDR-U31-C015 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:120 | filter_multi_company = fields.Selection | FACT | always | — | Fifteen filter switches (multi-company mode with company selector or tax units, date range, draft entries, unreconciled, unfold all, hide zero lines, period comparison, growth comparison, journals, analytic, account groups, account type, partners, favorite filters, budgets) control which viewer menus the report would show. | N-U31-014 |
| VDR-U31-C016 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:212 | prevent updating the filters | FACT | always | — | Filter switches are computed from the root report for variants and from the main report for single-use sections; the lookup tests whether a client action of kind account_report carries the report id. | N-U31-014 |
| VDR-U31-C017 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:80 | prefix_groups_threshold = fields.Integer | FACT | always | — | Further report options: load_more_limit, search_bar, prefix_groups_threshold (default 4000), integer_rounding, allow_foreign_vat. | N-U31-015 |
| VDR-U31-C018 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:88 | default_opening_date_filter = fields.Selection | FACT | always | — | default_opening_date_filter offers this/previous year, quarter, month, today and this/previous return period. | N-U31-015 |
| VDR-U31-C019 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:106 | currency_translation = fields.Selection | FACT | always | — | currency_translation is either the latest rate at the report date or cumulative translation adjustment (default cta via the filter default). | N-U31-015 |
| VDR-U31-C020 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:67 | only_tax_exigible = fields.Boolean | FACT | always | — | only_tax_exigible is a report option inherited from the root report; nothing in Community reads it. | N-U31-015 |
| VDR-U31-C021 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:294 | def copy(self, default=None) | FACT | always | — | Copy duplicates lines recursively, copies columns, and rewrites old line codes inside aggregation formulas and subformulas of the copy. | N-U31-011 |
| VDR-U31-C022 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:488 | '_COPY' | FACT | always | — | A copied line code gets the suffix _COPY, repeated until it is unique. | N-U31-011 |
| VDR-U31-C023 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:326 | delete a report that has variants | FACT | ondelete at_uninstall=False | — | Deleting a report with variants raises a user error (module uninstall bypasses the check). | N-U31-010 |
| VDR-U31-C024 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:44 | class AccountReport(models.Model) | OBSERVATION | restored DB | — | The report class has no thread or tracking mixin; in the DB none of the five report models, nor the tag model, has a tracked field or a message field. | N-U31-017 |
| VDR-U31-C025 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:377 | parent_id = fields.Many2one | FACT | always | — | A line has a parent line (set null on delete), children and a computed hierarchy level; report_id is computed from the parent and cascades on delete. | N-U31-003 |
| VDR-U31-C026 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:399 | unique (report_id, code) | FACT | always | — | Line code is unique per report (database constraint). | N-U31-009 |
| VDR-U31-C027 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:407 | increase_level = 3 | FACT | always | — | hierarchy_level is 1 for a top line; a child of a level-0 parent gets 3, any other child its parent plus 2. | N-U31-005 |
| VDR-U31-C028 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:379 | groupby = fields.Char | FACT | always | — | A line can declare comma-separated journal item fields to group by (groupby and user_groupby). | N-U31-003 |
| VDR-U31-C029 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:438 | both children and a groupby | FACT | always | — | A line whose parent has a groupby is refused: a line cannot have both children and a groupby value. | N-U31-008 |
| VDR-U31-C030 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:246 | The parent must always come first. | FACT | always | — | Report line order is validated: a parent appearing after its child is refused. | N-U31-008 |
| VDR-U31-C031 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:447 | defines itself as its parent | FACT | always | — | A line that is its own parent is refused. | N-U31-008 |
| VDR-U31-C032 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:390 | hide_if_zero = fields.Boolean | FACT | always | — | Line display flags: foldable, print_on_new_page, hide_if_zero and an action link; horizontal_split_side is inherited from the parent. | N-U31-005 |
| VDR-U31-C033 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:631 | UNIQUE(report_line_id,label) | FACT | always | — | An expression label is unique per line (database constraint). | N-U31-009 |
| VDR-U31-C034 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:938 | expression_label = fields.Char | FACT | always | — | A column holds a name, the label of the expression it displays (a text link, not a foreign key), sortable and blank_if_zero flags and an optional audit action. | N-U31-004 |
| VDR-U31-C035 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:942 | default="monetary" | FACT | always | — | Column figure_type is required and defaults to monetary. | N-U31-004 |
| VDR-U31-C036 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:17 | ('datetime', "Datetime") | FACT | always | — | Figure types are monetary, percentage, integer, float, date, datetime, boolean and string. | N-U31-004 |
| VDR-U31-C037 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:940 | index='btree_not_null' | INFERENCE | restored DB | — | Column.report_id is an ordinary many-to-one (DB foreign key ON DELETE SET NULL, unlike lines which cascade), so deleting a report would leave its columns with an empty report. | N-U31-018 |
| VDR-U31-C038 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | OBSERVATION | restored DB | — | DB: 6 reports (generic root, 2 generic variants, 3 Thai variants), 24 lines (all Thai), 29 expressions (all Thai), 9 columns (6 generic, 3 Thai), 0 external values, 0 section links; 0 window actions, 0 server actions, 0 views, 0 cron jobs and 0 automations on these models. | N-U31-001 |
| VDR-U31-C039 | FUNCTION MAPPING REQUIRED | account/data/account_reports_data.xml:6 | id="generic_tax_report" | FACT | account installed | — | The account module ships three generic tax report records without lines: a root with net and tax columns, multi-company mode tax units, foreign VAT allowed, default opening previous return period and only-tax-exigible on, and two variants (group by account then tax; tax then account) with availability always. | N-U31-121 |
| VDR-U31-C040 | FUNCTION MAPPING REQUIRED | account/data/account_reports_data.xml:26 | generic_tax_report_account_tax | FACT | account installed | — | The two generic variants point to the root and carry their own net and tax columns. | N-U31-002 |
| VDR-U31-C041 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:591 | ('tax_tags', "Tax Tags") | FACT | always | — | The expression engine selection has six values: domain, tax_tags, aggregation, account_codes, external, custom. | N-U31-020 |
| VDR-U31-C042 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:595 | ('custom', "Custom Python Function") | FACT | always | — | custom is declared as a selection value; no code in Community registers a routine for it. | N-U31-025 |
| VDR-U31-C043 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:653 | ast.literal_eval(expression.formula) | FACT | domain engine | — | A domain formula is read with literal_eval and test-searched on journal items; failure raises an invalid-formula error. | N-U31-021 |
| VDR-U31-C044 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:659 | ACCOUNT_CODES_ENGINE_SPLIT_REGEX.split | FACT | account_codes engine | — | An account_codes formula is split on plus and minus signs and each term must match the term regex (prefix, optional exclusions, optional D or C balance character). | N-U31-021 |
| VDR-U31-C045 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:30 | (?P<balance_character>[DC]?) | FACT | always | — | The term regex also admits a tag(...) prefix, i.e. account codes engine terms can refer to tags. | N-U31-021 |
| VDR-U31-C046 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:667 | AGGREGATION_ENGINE_FORMULA_REGEX.fullmatch | FACT | aggregation engine | — | An aggregation formula must fully match a regex of numbers and line_code.label references joined by operators, or be sum_children. | N-U31-021 |
| VDR-U31-C047 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:36 | hard_formulas = ['sum_children'] | FACT | always | — | sum_children is the only keyword formula of the aggregation grammar. | N-U31-021 |
| VDR-U31-C048 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:650 | expressions_by_engine = self.grouped('engine') | INFERENCE | reading lines 643-668 | — | The formula check iterates only the domain, account_codes and aggregation groups; tag, external and custom formulas are not validated. | N-U31-030 |
| VDR-U31-C049 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:22 | DOMAIN_REGEX = re.compile | FACT | always | — | The domain shortcut field accepts sum(...) or -sum(...) wrapping a domain; the wrapper becomes the subformula and the inner text the formula. | N-U31-022 |
| VDR-U31-C050 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:508 | def _create_report_expression | FACT | always | — | Each shortcut field (domain, account_codes, aggregation, external, tax_tags) creates, or rewrites, the line expression labelled balance; an empty shortcut deletes the one it generated. | N-U31-022 |
| VDR-U31-C051 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:523 | subformula, formula = 'editable', 'most_recent' | FACT | always | — | The external shortcut builds a most_recent rule with subformula editable (rounding 0 for percentage, formula sum for monetary). | N-U31-024 |
| VDR-U31-C052 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:628 | should all have a subformula | FACT | always | — | A database check requires a subformula whenever the engine is domain. | N-U31-028 |
| VDR-U31-C053 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:683 | Groupby feature isn't supported by | FACT | always | — | Aggregation and external expressions are refused on a line with a groupby or user_groupby. | N-U31-028 |
| VDR-U31-C054 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:842 | cross report on itself | FACT | always | — | A cross-report subformula pointing at the same report raises a user error; an unparsable reference or missing report also raises. | N-U31-028 |
| VDR-U31-C055 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:800 | def _expand_aggregations | FACT | always | — | Aggregation dependencies are expanded transitively, via sum_children over child lines, or via line_code and label terms in the same or a cross-referenced report. | N-U31-023 |
| VDR-U31-C056 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:815 | startswith('cross_report') | FACT | always | — | A subformula of the form cross_report(report id or xml id) redirects the aggregation terms to another report. | N-U31-023 |
| VDR-U31-C057 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:879 | if_other_expr_ | FACT | always | — | The term parser recognises if_other_expr_above and if_other_expr_below subformulas as extra dependencies. | N-U31-023 |
| VDR-U31-C058 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:689 | 'external', 'aggregation' | FACT | always | — | Every engine except custom is auditable (the auditable flag is computed from the engine). | N-U31-026 |
| VDR-U31-C059 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:615 | green_on_positive = fields.Boolean | FACT | always | — | An expression may carry figure_type, green_on_positive (default true), blank_if_zero and auditable. | N-U31-027 |
| VDR-U31-C060 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:67 | STARTS_WITH(%s, '-') | FACT | always | — | A tag reports balance_negate as whether the matching expression formula starts with a minus sign. | N-U31-029 |
| VDR-U31-C061 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:800 | def _expand_aggregations | INFERENCE | grep over odoo/addons | — | Grep finds no caller of _expand_aggregations in Community; _get_aggregation_terms_details is called only from _expand_aggregations in the same file. | N-U31-031 |
| VDR-U31-C062 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:948 | _name = 'account.report.external.value' | INFERENCE | grep over odoo/addons | — | Grep finds no code that creates or reads external-value rows in Community: only the model, its ACL and rule, and two foreign-pack migrations. | N-U31-031 |
| VDR-U31-C063 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | RT | NOT PRESENT IN COMMUNITY SOURCE: any evaluator of the six engines. Greps over odoo/addons py, xml, js, csv, json (excluding i18n): _compute_formula_batch, _report_expand_unfoldable, _compute_expression_totals, _get_report_expressions, caret_options return nothing; get_options and get_report_information appear only in a foreign-pack test; _report_custom_engine appears only in foreign-pack data files. Numeric results cannot be established without the outside layer. | N-U31-032 |
| VDR-U31-C064 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: any handler providing custom-engine routines (grep for report.custom.handler and def _report_custom_engine returns no definition). | N-U31-025 |
| VDR-U31-C065 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:209 | 'ir.actions.client'].search_count | FACT | always | — | The only trace of a report viewer is a search for a client action with tag account_report whose context names the report id, used to decide filter defaults. | N-U31-036 |
| VDR-U31-C066 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:209 | 'ir.actions.client'].search_count | OBSERVATION | restored DB | — | DB: no client action has tag account_report or a context naming a report id (5 client actions exist, all stock or manufacturing reports), so the lookup always finds none. | N-U31-036 |
| VDR-U31-C067 | FUNCTION MAPPING REQUIRED | web/tests/test_action.py:53 | 'tag': 'account_report', | FACT | tests | — | The only other mention of that client action tag in Community is a web test fixture that creates its own action. | N-U31-036 |
| VDR-U31-C068 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:84 | module_account_reports = fields.Boolean("Dynamic Reports") | FACT | always | — | The settings field Dynamic Reports is a module switch; its view uses the upgrade_boolean widget. | N-U31-035 |
| VDR-U31-C069 | FUNCTION MAPPING REQUIRED | account/views/res_config_settings_views.xml:350 | widget="upgrade_boolean" | FACT | always | — | The settings view renders the dynamic-reports switch as an upgrade prompt. | N-U31-035 |
| VDR-U31-C070 | FUNCTION MAPPING REQUIRED | account/models/res_config_settings.py:84 | module_account_reports | OBSERVATION | restored DB | — | DB: there is no module row named account_reports (nor account_accountant) and no directory of that name in the Community tree. | N-U31-035 |
| VDR-U31-C071 | FUNCTION MAPPING REQUIRED | account/views/account_menuitem.xml:39 | account_reports_taxes_and_fiscal_menu | FACT | always | — | Menu containers Partner Reports, Taxes and Fiscal, Management and Statement Reports are declared under Reporting; the first, second and fourth have no children declared in Community. | N-U31-034 |
| VDR-U31-C072 | FUNCTION MAPPING REQUIRED | account/views/account_menuitem.xml:39 | account_reports_taxes_and_fiscal_menu | OBSERVATION | restored DB | — | DB: those three containers hold no menu entries; Management holds invoice analysis, analytic report and product margins. | N-U31-034 |
| VDR-U31-C073 | FUNCTION MAPPING REQUIRED | product_margin/views/product_product_views.xml:87 | account.account_reports_management_menu | FACT | product_margin installed | — | Product margins is attached to the Management container; invoice analysis and the analytic report are declared in the account menu file. | N-U31-038 |
| VDR-U31-C074 | FUNCTION MAPPING REQUIRED | account/views/account_report.xml:87 | <field name="report_name">account.report_hash_integrity</field> | FACT | always | — | The account module declares six print actions: invoices with payments, original vendor bill, invoice, payment receipt, statement and ledger hash integrity; the DB adds the Thai commercial invoice as the seventh account-related action. | N-U31-037 |
| VDR-U31-C075 | FUNCTION MAPPING REQUIRED | l10n_th/views/report_invoice.xml:32 | l10n_th.report_commercial_invoice | FACT | l10n_th installed | — | The Thai package adds one print action, the commercial invoice; it is not a tax return or book. | N-U31-037 |
| VDR-U31-C076 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | OBSERVATION | restored DB | — | DB: window actions, server actions, views, cron jobs and automations on the five report models and the tag model are all 0 (3 views exist for the tag model: form, list, search; no action or menu opens them). | N-U31-033 |
| VDR-U31-C077 | FUNCTION MAPPING REQUIRED | spreadsheet_account/models/account.py:44 | def _build_spreadsheet_formula_domain | FACT | spreadsheet_account installed | — | The spreadsheet formula domain selects journal items by account codes or by account tags (account_id.tag_ids), by period, company and posted state; it never filters on tax_tag_ids. | N-U31-039 |
| VDR-U31-C078 | FUNCTION MAPPING REQUIRED | spreadsheet_account/models/account.py:63 | account_id.tag_ids | FACT | spreadsheet_account installed | — | Formula ODOO.BALANCE.TAG selects accounts whose account tags are given, not entries carrying a tax grid tag. | N-U31-039 |
| VDR-U31-C079 | FUNCTION MAPPING REQUIRED | spreadsheet_account/__manifest__.py:11 | 'auto_install': True | OBSERVATION | restored DB | — | DB: spreadsheet_account, spreadsheet_dashboard and the accounting dashboard module are installed. | N-U31-039 |
| VDR-U31-C080 | FUNCTION MAPPING REQUIRED | spreadsheet_dashboard_account/data/dashboards.xml:4 | dashboard_invoicing | FACT | always | — | The accounting dashboard module declares one dashboard, Invoicing, for the read-only accounting and invoicing groups. | N-U31-039 |
| VDR-U31-C081 | FUNCTION MAPPING REQUIRED | account/tests/test_account_move_line_tax_details.py:28 | _get_query_tax_details_from_domain | FACT | tests | — | The tax-details query helper is called only by its own test in Community. | N-U31-040 |
| VDR-U31-C082 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:3456 | def _get_tax_exigible_domain | INFERENCE | grep over odoo/addons | — | The exigible-lines domain helper is defined with a docstring saying it identifies lines allowed in the tax report, and has no caller anywhere in Community. | N-U31-040 |
| VDR-U31-C083 | FUNCTION MAPPING REQUIRED | l10n_in/models/l10n_in_report_handler.py:7 | def _init_options_buttons | OBSERVATION | FOREIGN LOCALIZATION (not installed); label only | — | FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE: a foreign pack extends the report model with a viewer hook whose base method is not defined in Community; evidence that the viewer layer lives outside. | N-U31-044 |
| VDR-U31-C084 | FUNCTION MAPPING REQUIRED | l10n_fr_account/tests/test_fr_tax_report.py:48 | get_report_information | OBSERVATION | FOREIGN LOCALIZATION (not installed); label only | — | FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE: the only Community code that calls an evaluator of a report is a foreign-pack test. | N-U31-044 |
| VDR-U31-C085 | FUNCTION MAPPING REQUIRED | account/tests/test_account_report.py:11 | def test_copy_report | INFERENCE | tests | — | Community report tests cover copy, formula validation and tag synchronisation only; none evaluates a report. | N-U31-043 |
| VDR-U31-C086 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | RT | NOT PRESENT IN COMMUNITY SOURCE: rendering, export or filing of any report built from account.report definitions. Greps over odoo/addons py, xml, js, csv, json excluding i18n: export_to_xlsx, export_to_pdf, export_to_xml, action_open_returns, _get_lines, _dispatch_report, _get_report_filename: no definition; _init_options and get_options: only foreign packs. | N-U31-033 |
| VDR-U31-C087 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | — | NOT PRESENT IN COMMUNITY SOURCE: any Revenue Department filing, e-filing, PP 30 or PND form generation, withholding certificate, or output/input tax book. Greps over odoo/addons excluding l10n_th and i18n: pp 30 (only an unrelated Croatian tax name), pp 36, pnd (including pnd 54), rd.go.th, revenue department, withholding certificate, sales/purchase tax book, tax ledger: nothing relevant. Matches the earlier U24 absence claims. | N-U31-041 |
| VDR-U31-C088 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | outside package | RT | UNKNOWN - EVIDENCE INSUFFICIENT: how an outside reporting package would select periods, create returns and export formats; not studied (no source in scope). | N-U31-045 |
| VDR-U31-C089 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:3 | model="account.report" | FACT | l10n_th installed | — | The Thai Tax Report is a variant of the generic tax report for country Thailand with availability country and foreign VAT allowed (lines 3-9). | N-U31-046 |
| VDR-U31-C090 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:11 | tax_report_balance | FACT | l10n_th installed | — | Each Thai report has a single balance column (VAT report line 11, withholding reports lines 234 and 298). | N-U31-046 |
| VDR-U31-C091 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:18 | tax_report_out_tax_title | FACT | l10n_th installed | — | The VAT report has four level-0 section lines (output tax, input tax, value added tax, net tax; lines 18, 79, 112, 169) each with an aggregation shortcut and children. | N-U31-048 |
| VDR-U31-C092 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:32 | -1. Sales amount | FACT | l10n_th installed | — | Output-side tag rules (sales amount, zero-rated sales, exempt sales, output tax at lines 32, 44, 56, 73) have a leading minus. | N-U31-049 |
| VDR-U31-C093 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:94 | 6. Purchase amount that is entitled | FACT | l10n_th installed | — | Input-side tag rules (purchase amount line 94, input tax line 106) and the carried-forward tag (line 158) have no minus. | N-U31-049 |
| VDR-U31-C094 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:63 | OUTPUTTAX_SALEAMOUNT.balance-(OUTPUTTAX_SALE_ZERO.balance | FACT | l10n_th installed | — | Taxable sales is an aggregation: sales amount minus (zero-rated plus exempt). | N-U31-050 |
| VDR-U31-C095 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:126 | OUTPUTTAX_TAX.balance - INPUTTAX_TAX.balance | FACT | l10n_th installed | — | Tax payable is output minus input tax with subformula if_above(THB(0)); excess (line 139) is the reverse with the same subformula; net tax payable (line 184) is tax payable minus carried excess, again if_above(THB(0)). | N-U31-050 |
| VDR-U31-C096 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:127 | if_above(THB(0)) | FACT | l10n_th installed | — | The positive-part subformulas hard-code the currency THB. | N-U31-053 |
| VDR-U31-C097 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:152 | most_recent | FACT | l10n_th installed | — | Line 10 holds three rules: an external rule most_recent labelled _applied_carryover_balance with date scope previous_return_period, a tag rule labelled tag (line 155-159), and an aggregation adding both (line 163). | N-U31-051 |
| VDR-U31-C098 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:218 | carryover_target | FACT | l10n_th installed | — | Line 12 holds net_vat_payable (198), net_vat_excess (205-206, subformula if_other_expr_above(9_VAT_EXCESS.balance, THB(0))), the balance sum (212) and a _carryover_balance rule whose carryover_target is line 10 _applied_carryover_balance. | N-U31-051 |
| VDR-U31-C099 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:227 | tax_report_pnd53 | FACT | l10n_th installed | — | The PND53 report has lines Total Income (tag Income PND53), Total Remittance (tag PND53), Surcharge (tag SUR53) and Total (aggregation P53 plus S53); none of the tag rules has a minus. | N-U31-052 |
| VDR-U31-C100 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:291 | tax_report_pnd3 | FACT | l10n_th installed | — | The PND3 report is the same with tags Income PND3, PND3 and SUR3 and aggregation P3 plus S3. | N-U31-052 |
| VDR-U31-C101 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:3 | model="account.report" | OBSERVATION | restored DB | CONTRA | DB: Thai reports 3, lines 24 (16 + 4 + 4), expressions 29 (13 tax_tags, 15 aggregation, 1 external); 24 expressions have data identifiers and 5 (the four section lines and taxable sales, from aggregation_formula shortcuts) do not. CONTRA to the U24 section-10 summary and the TXC reconciliation table that count 24 Thai expressions plus 5 from the account module: the 5 are Thai shortcut-generated; the generic reports hold 0 lines and 0 expressions. | N-U31-047 |
| VDR-U31-C102 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:21 | aggregation_formula | FACT | l10n_th installed | — | Lines at 21, 63, 83, 115 and 172 declare only an aggregation_formula shortcut, which creates the five identifier-less balance expressions. | N-U31-047 |
| VDR-U31-C103 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:273 | SUR53 | OBSERVATION | restored DB | — | DB: of 13 Thai tax tags, 10 sit on 60 distribution-line links; 10 Excess tax payment carried forward, SUR53 and SUR3 sit on none (consistent with U24 C074). | N-U31-054 |
| VDR-U31-C104 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:5 | name@th | FACT | l10n_th installed | — | The data ships Thai translations of report, line and column names (name@th) alongside English; DB holds no th_TH value because that language is not installed. | N-U31-056 |
| VDR-U31-C105 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax-th.csv:26 | -1.0 | INFERENCE | l10n_th chart loaded | RT | Purchase withholding taxes are negative percentages with tax tags PND53 or PND3 on a liability account and income tags on the base, while the PND report rules have no minus; the raw balance sign of the tax tag on a vendor bill is therefore credit (negative); presentation is decided by an evaluator not present. | N-U31-055 |
| VDR-U31-C106 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | legal review | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether the shipped return layouts match current statutory forms; resolve against TXS statutory register (S09, S13) by legal review, not from Odoo behaviour. | N-U31-057 |
| VDR-U31-C107 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:12 | applicability = fields.Selection | FACT | always | — | A tag has name (translatable), applicability accounts, taxes or products (default accounts), color, active and an optional country described as the country for which the tag is available when applied on taxes. | N-U31-058 |
| VDR-U31-C108 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:20 | balance_negate = fields.Boolean | FACT | always | — | report_expression_id and balance_negate are computed (not stored) fields allowing the sign of the report line used to display the amount to be read from the matching expression. | N-U31-059 |
| VDR-U31-C109 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:23 | unique(name, applicability, country_id) | FACT | always | — | Tag name is unique per applicability and country (database constraint over the translatable name); the restored DB has the same UNIQUE constraint on name, applicability and country. | N-U31-063 |
| VDR-U31-C110 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:23 | unique(name, applicability, country_id) | INFERENCE | tag without country | — | With a null country the unique constraint does not collide (PostgreSQL treats nulls as distinct), so duplicate names are possible for tags without a country. | N-U31-063 |
| VDR-U31-C111 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:59 | LTRIM(%s, '-') | INFERENCE | always | — | The tag-to-expression join compares the tag English name to the formula without minus with no country or engine condition, while the related-expressions method adds the country; identical formula text in two countries would match both. | N-U31-073 |
| VDR-U31-C112 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:105 | Domain('formula', 'in', (record.name, '-' + record.name)) | FACT | always | — | Related tag expressions are those with engine tax_tags in the tag country and formula equal to the name with or without a minus. | N-U31-059 |
| VDR-U31-C113 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:711 | tag_name = expression.formula | FACT | expression create | — | Creating a tag expression creates the missing tag in the report country. | N-U31-060 |
| VDR-U31-C114 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:902 | 'name': tag_name.lstrip('-') | FACT | always | — | New tag values: name without leading minus, applicability taxes, country of the report. | N-U31-060 |
| VDR-U31-C115 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:697 | if not existing_tag: | FACT | always | — | Tag creation looks up existing tags first (archived included) and creates only when none exist. | N-U31-060 |
| VDR-U31-C116 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:724 | if vals.get('engine') == 'tax_tags': | FACT | expression write | — | Changing an expression engine to tax_tags creates its tag in the report country if missing. | N-U31-060 |
| VDR-U31-C117 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:713 | country = expression.report_line_id.report_id.country_id | INFERENCE | report without country | — | The tag country comes from the report of the line (not the root report); a report without a country yields a tag with an empty country. | N-U31-071 |
| VDR-U31-C118 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:757 | _update_field_translations('name' | FACT | expression write | — | When all rules using a tag change formula together the tag English name is rewritten (minus stripped); otherwise a new tag is created. | N-U31-064 |
| VDR-U31-C119 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:756 | changing the formula of all | FACT | expression write | — | The rename branch is taken only if every related expression of the old tag is in the written set. | N-U31-064 |
| VDR-U31-C120 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:757 | _update_field_translations('name' | INFERENCE | posted entries carry the tag | — | The rename writes the tag name directly; no check on journal items carrying the tag, no lock-date check and no log. | N-U31-074 |
| VDR-U31-C121 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:784 | tags_to_archive += tag | FACT | expression unlink | — | Deleting the last expression using a tag archives the tag when a journal item carries it, unlinks it otherwise. | N-U31-065 |
| VDR-U31-C122 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:790 | rep_lines_with_tag.write({'tag_ids': [Command.unlink | FACT | expression unlink | — | The tag is also removed from every tax distribution line before archive or delete. | N-U31-065 |
| VDR-U31-C123 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:279 | tax_tags.write({'country_id': vals['country_id']}) | FACT | report write country_id | — | Changing a report country rewrites the country of tags used only by reports in the write; tags shared with other reports are kept and new tags are created in the target country. | N-U31-066 |
| VDR-U31-C124 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:112 | master_xmlids = [ | FACT | always | — | The three cash-flow master tags (operating, financing, investing) cannot be deleted. | N-U31-067 |
| VDR-U31-C125 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5336 | ondelete='restrict') | FACT | always | — | Distribution line tag_ids is restricted on tag delete. | N-U31-068 |
| VDR-U31-C126 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:237 | ondelete='restrict', | FACT | always | — | Journal item tax_tag_ids is restricted on tag delete. | N-U31-068 |
| VDR-U31-C127 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5351 | allowed_country_ids = (False | FACT | form view | — | The dynamic tag domain admits tax tags with no country, the company fiscal country or its foreign VAT countries. | N-U31-069 |
| VDR-U31-C128 | FUNCTION MAPPING REQUIRED | account/views/account_tax_views.xml:50 | domain="tag_ids_domain" | FACT | form view | — | The dynamic domain is applied in the repartition list view only; the tag_ids field itself declares just applicability taxes (no create option in the view). | N-U31-069 |
| VDR-U31-C129 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1246 | def _get_tag_mapper | FACT | chart template load | — | Template tag cells are resolved by name through a mapper that searches tax tags of the template country, archived included. | N-U31-061 |
| VDR-U31-C130 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1267 | missing tax tag %(tag_name)s for country | FACT | chart template load | — | An unknown tag name raises a redirect warning suggesting to update the localization. | N-U31-061 |
| VDR-U31-C131 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1264 | ignore_missing_tags | FACT | chart template load | — | With context ignore_missing_tags (used for translation loading) a missing tag is only logged and skipped. | N-U31-061 |
| VDR-U31-C132 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:1247 | self.env['account.account.tag'].with_context(active_test=False | INFERENCE | grep of chart_template.py | — | Apart from this lookup and the xml-id preserve helper the file never creates tax tags: grep for account.account.tag in chart_template.py finds lines 48 and 1247 only. | N-U31-061 |
| VDR-U31-C133 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:33 | TAX_TAG_DELIMITER | FACT | always | — | Several tag names in one template cell are separated by a double vertical bar. | N-U31-061 |
| VDR-U31-C134 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:122 | def _translate_tax_tags | FACT | always | — | A SQL helper copies line-label translations onto tags whose English name equals the line name (first character kept as sign). | N-U31-062 |
| VDR-U31-C135 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:74 | self._translate_tax_tags(tag_ids=tax_tags.ids) | FACT | tag create | — | Tax tags are translated when created. | N-U31-062 |
| VDR-U31-C136 | FUNCTION MAPPING REQUIRED | account/models/ir_module.py:91 | _translate_tax_tags(langs=langs) | FACT | language install | — | Tax tags are translated again when languages are loaded. | N-U31-062 |
| VDR-U31-C137 | FUNCTION MAPPING REQUIRED | account/models/product.py:61 | account_tag_ids = fields.Many2many | FACT | always | — | Products carry tags of applicability products, described as tags set on the base and tax journal items created for the product. | N-U31-070 |
| VDR-U31-C138 | FUNCTION MAPPING REQUIRED | account/models/account_account.py:109 | Optional tags you may want | FACT | always | — | Accounts carry tags (computed default from the closest parent account) for custom reporting. | N-U31-070 |
| VDR-U31-C139 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:12 | applicability = fields.Selection | OBSERVATION | restored DB | — | DB: 16 tags: 3 account-purpose master tags (with data identifiers) and 13 tax tags, all country Thailand, none with a data identifier; unique constraint present; tags are 1:1 with the 13 tax_tags expressions by name. | N-U31-072 |
| VDR-U31-C140 | FUNCTION MAPPING REQUIRED | l10n_th/__init__.py:6 | preserve_existing_tags_on_taxes(env, 'l10n_th') | FACT | l10n_th install | — | The post-install hook marks existing tag data records of the module as noupdate; the Thai tags have no data records, so in this DB it has nothing to mark. | N-U31-072 |
| VDR-U31-C141 | FUNCTION MAPPING REQUIRED | account/models/chart_template.py:50 | update ir_model_data set noupdate = 't' | FACT | always | — | Helper sets noupdate on tag data records of a module so upgrades keep existing tags. | N-U31-072 |
| VDR-U31-C142 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:15 | country_id = fields.Many2one | OBSERVATION | restored DB | — | DB: tag.country_id foreign key is ON DELETE SET NULL. | N-U31-075 |
| VDR-U31-C143 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:84 | active_test=False | INFERENCE | rule recreated after archive | RT | Tag lookup includes archived tags (active_test False), so a recreated rule finds the archived tag and creates nothing; no code reactivates it, and the archive step already removed it from distribution lines. | N-U31-076 |
| VDR-U31-C144 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | language th_TH activated | RT | UNKNOWN - EVIDENCE INSUFFICIENT: result of translating Thai tags when th_TH is installed (names, uniqueness over translated jsonb); resolve by AWT on a copy. | N-U31-077 |
| VDR-U31-C145 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:240 | determines its impact on financial reports | FACT | always | — | Journal item tax_tag_ids holds the tags assigned by the tax creating the line; it determines the line impact on financial reports; it is tracked (change log) and restricted on delete. | N-U31-079 |
| VDR-U31-C146 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2413 | base_line['tax_tag_ids'] | FACT | tax on invoice or caba tags requested | — | A base line gets the base-type distribution tags of each non-reverse-charge tax. | N-U31-079 |
| VDR-U31-C147 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2405 | product_tags = product.sudo().account_tag_ids | FACT | line has product | — | Product tags are added to the base line and (below) to every tax line. | N-U31-079 |
| VDR-U31-C148 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2483 | tax_rep_data['tax_tags'] = product_tags | FACT | always | — | A tax line starts with the product tags and adds the tags of its tax-type distribution line. | N-U31-079 |
| VDR-U31-C149 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2486 | if tax.include_base_amount: | FACT | always | — | A tax that affects the base of later taxes receives the base tags of those later taxes. | N-U31-079 |
| VDR-U31-C150 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2394 | repartition_lines_field = 'refund_repartition_line_ids' | FACT | always | — | is_refund selects the refund or invoice distribution lines for amounts, accounts and tags. | N-U31-080 |
| VDR-U31-C151 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1637 | is_refund=self.move_type in ('out_refund', 'in_refund') | FACT | always | — | For documents is_refund is true for customer and vendor credit notes. | N-U31-080 |
| VDR-U31-C152 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1220 | tax_type == 'sale' | FACT | entry (miscellaneous) move | — | For entries without a tax line is_refund follows the amount side and the first tax purpose; with both purposes the invoice side is the default; a reversed entry flips it. | N-U31-080 |
| VDR-U31-C153 | FUNCTION MAPPING REQUIRED | account/tests/test_invoice_taxes.py:394 | ref_tax_rep_ln.id | FACT | tests | — | A test confirms a sale tax on a debit base line uses the refund distribution line and on a credit base line the invoice one, with the same tags. | N-U31-080 |
| VDR-U31-C154 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:17 | sign of the report line | FACT | always | — | The tag model comment states that tag sign is obtained from the report line expression that generated the tag. | N-U31-081 |
| VDR-U31-C155 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3100 | 'tax_tag_ids': [Command.set(base_line['tax_tag_ids'].ids)], | FACT | always | — | Base lines to update carry tax_tag_ids together with balance and amount_currency in the same update. | N-U31-078 |
| VDR-U31-C156 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2342 | 'tax_tag_ids': [Command.set(tax_rep_data['tax_tags'].ids)], | FACT | always | — | The tax line grouping key includes the tags, so lines with different tags are not merged. | N-U31-085 |
| VDR-U31-C157 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3365 | if move.state != 'draft': | FACT | always | — | The dynamic tax-line synchronisation skips non-draft moves, so tags and tax lines are recomputed only while a move is draft. | N-U31-078 |
| VDR-U31-C158 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5569 | def _post(self, soft=True) | INFERENCE | grep of account_move.py | — | Posting contains no tag logic: tax_tag_ids appears in account_move.py only in a compute dependency (1930-1931) and in rounding (3137), clearing (3218) and early-payment (5163, 5206) code. | N-U31-078 |
| VDR-U31-C159 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3218 | move.line_ids.tax_tag_ids = [Command.set([])] | FACT | non-posted move whose taxes were all removed | — | When taxes disappear from all lines the tax lines are unlinked and the tags are cleared. | N-U31-087 |
| VDR-U31-C160 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3137 | 'tax_tag_ids': [(6, 0, biggest_tax_line.tax_tag_ids.ids)] | FACT | cash rounding biggest_tax | — | The rounding line copies repartition line, account, tags and taxes of the biggest tax line. | N-U31-083 |
| VDR-U31-C161 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5206 | 'tax_tag_ids': tax_line_vals['tax_tag_ids'], | FACT | early payment discount mixed | — | Early-payment-discount tax lines reuse the computed tax tags; the base lines reuse the base line tags (line 5163). | N-U31-083 |
| VDR-U31-C162 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3115 | tax lines having a zero amount | FACT | always | — | Tax lines whose amount and balance are zero are dropped unless flagged to keep, so a 0 percent tax yields base tags only. | N-U31-084 |
| VDR-U31-C163 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1649 | include_caba_tags=self.payment_mode == 'company_account' | FACT | hr_expense installed | — | Company-paid expenses build base and tax lines with the engine and include cash-basis tags. | N-U31-086 |
| VDR-U31-C164 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5515 | 'move_type': TYPE_REVERSE_MAP[move.move_type], | FACT | always | — | Reversal copies the move with the opposite type (invoice to credit note) and a link to the reversed entry. | N-U31-082 |
| VDR-U31-C165 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:5532 | line.display_type == 'cogs' | FACT | reversal | — | Only for entries (and cogs lines) are balance and amount_currency negated after the copy. | N-U31-082 |
| VDR-U31-C166 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:234 | tax_tag_ids = fields.Many2many( | INFERENCE | reversal of an entry | RT | tax_tag_ids declares no copy=False, so a copy of an entry line keeps its tags; the reversed entry is thus tagged identically with opposite amounts (not executed). | N-U31-082 |
| VDR-U31-C167 | PCO-F01 | account/models/account_move_line.py:3488 | tax_fnames = ['balance', 'tax_line_id', 'tax_ids', 'tax_tag_ids'] | FACT | always | — | Tax lock date protects balance, tax_line_id, tax_ids and tax_tag_ids of journal items. | N-U31-088 |
| VDR-U31-C168 | PCO-F01 | account/models/account_move_line.py:1539 | if violated_lock_dates and line._affect_tax_report(): | FACT | posted line, tax lock date violated | — | The tax lock check applies only to lines that affect the tax report. | N-U31-088 |
| VDR-U31-C169 | PCO-F01 | account/models/account_move_line.py:1522 | _affect_tax_report | FACT | always | — | A line affects the tax report if it has taxes, is a tax line, or has tags with applicability taxes. | N-U31-088 |
| VDR-U31-C170 | PCO-F01 | account/models/account_move_line.py:1850 | modify the taxes related to | FACT | posted line | — | Changing tax_ids or tax_line_id of a posted line is refused at write. | N-U31-088 |
| VDR-U31-C171 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:557 | exactly one line for the base | FACT | always | — | Each document type (invoice and refund) must have exactly one base distribution line. | N-U31-089 |
| VDR-U31-C172 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:585 | distribution should match | FACT | always | — | Invoice and refund distribution lines must match in basis type and percentage, in sequence order. | N-U31-089 |
| VDR-U31-C173 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:591 | total factor (+) equals to 100 | FACT | always | — | Positive tax factors must total 100 percent; any negative factors must total minus 100 percent. | N-U31-089 |
| VDR-U31-C174 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2418 | tax_rep_sign = -1.0 | FACT | reverse-charge tax | — | Reverse-charge uses tax distribution lines with negative factor and sign minus one. | N-U31-090 |
| VDR-U31-C175 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2412 | not tax_data['is_reverse_charge'] | FACT | always | — | Reverse-charge taxes add no base tags. | N-U31-090 |
| VDR-U31-C176 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:670 | return super().write(self._sanitize_vals(vals)) | INFERENCE | grep: no write hook on tax or distribution line | — | AccountTax.write only sanitises values and the distribution line class has no write: nothing re-tags existing journal items when distribution tags change. | N-U31-091 |
| VDR-U31-C177 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:492 | 'repartition_type': 'base', 'tag_ids': [] | FACT | tax created without lines | — | Default distribution lines created for a new tax have empty tag lists. | N-U31-092 |
| VDR-U31-C178 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1213 | both purchase and sale taxes | FACT | entry with both tax purposes | — | Source comment: with both sale and purchase taxes on a line, invoice is chosen by default. | N-U31-093 |
| VDR-U31-C179 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:261 | PND53 | INFERENCE | l10n_th withholding on vendor bills | RT | The Thai PND rules have no minus although the withholding tax line is credit-negative on a vendor bill; presentation sign is open. | N-U31-094 |
| VDR-U31-C180 | FUNCTION MAPPING REQUIRED | l10n_th/models/account_move.py:5 | _inherit = "account.move" | INFERENCE | l10n_th installed; grep of _inherit in l10n_th/models | — | The Thai package extends only the move report selector, partner, report action, bank and chart template; it overrides no tag, tax, report, lock or reconcile method and no model of the report family. | N-U31-072 |
| VDR-U31-C181 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:36 | def _prepare_base_line_grouping_key | FACT | hr_expense installed | — | hr_expense extends the tax engine grouping keys with the expense id only (base and tax lines); it does not change tag selection. | N-U31-086 |
| VDR-U31-C182 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | no transactions in DB | RT | UNKNOWN - EVIDENCE INSUFFICIENT: executed tag outcomes of invoices, credit notes and reversals; resolve by AWT with Thai taxes. | N-U31-095 |
| VDR-U31-C183 | FUNCTION MAPPING REQUIRED | account/models/company.py:220 | tax_exigibility = fields.Boolean(string='Use Cash Basis') | FACT | always | — | Company switch Use Cash Basis, with cash basis journal and base-tax-received account. | N-U31-096 |
| VDR-U31-C184 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection | FACT | always | — | Each tax is on_invoice (default) or on_payment. | N-U31-096 |
| VDR-U31-C185 | FUNCTION MAPPING REQUIRED | l10n_th/models/template_th.py:41 | 'tax_exigibility': 'True' | OBSERVATION | restored DB | — | DB: the Thai company has the cash-basis switch on; all 18 taxes are on_invoice (11 purchase, 7 sale). | N-U31-096 |
| VDR-U31-C186 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2484 | include_caba_tags or tax.tax_exigibility == 'on_invoice' | FACT | always | — | On the original document tax tags are added only when the tax is on_invoice or cash-basis tags are requested. | N-U31-097 |
| VDR-U31-C187 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1019 | record.always_tax_exigible = not record.is_invoice(True) | FACT | always | — | A move that is not an invoice and has no cash-basis lines is always exigible and receives cash-basis tags at entry time. | N-U31-098 |
| VDR-U31-C188 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:563 | 'tax_cash_basis_origin_move_id': move.id | FACT | tax on_payment, partial reconcile | — | Each partial reconcile creates a cash-basis entry in the cash-basis journal linked to the origin move and the partial. | N-U31-097 |
| VDR-U31-C189 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:554 | move_date = max(partial_values['settlement_date'], lock_date + timedelta(days=1)) | FACT | tax on_payment | — | The cash-basis entry is dated the settlement date or the day after the fiscal lock date, whichever is later (the tax lock date is not consulted). | N-U31-097 |
| VDR-U31-C190 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:378 | tax_tags = tax_ids.get_tax_tags(is_refund, 'base') | FACT | always | — | Cash-basis base lines carry the base tags of the on_payment taxes plus product tags, by invoice or refund type. | N-U31-097 |
| VDR-U31-C191 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:430 | all_tags = base_tags + tax_line.tax_repartition_line_id.tag_ids | FACT | always | — | Cash-basis tax lines carry the distribution tags, product tags and base tags. | N-U31-097 |
| VDR-U31-C192 | FUNCTION MAPPING REQUIRED | account/models/account_partial_reconcile.py:117 | moves_to_reverse = self.env['account.move'].search([('tax_cash_basis_rec_id' | FACT | partial unlink | — | Unlinking a partial reverses the cash-basis entries created for it. | N-U31-100 |
| VDR-U31-C193 | PCO-F01 | account/models/account_partial_reconcile.py:140 | reversal in the origin | FACT | partial unlink | — | The reversal date is the origin date, moved after the violated lock date if any. | N-U31-100 |
| VDR-U31-C194 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1591 | cannot be mixed on the same | FACT | always | — | A journal item cannot mix on-payment and on-invoice taxes that share a tag. | N-U31-101 |
| VDR-U31-C195 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:4184 | multiple involved currencies | FACT | always | — | Cash-basis values are not collected when several currencies are involved. | N-U31-102 |
| VDR-U31-C196 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:67 | only_tax_exigible = fields.Boolean | OBSERVATION | restored DB | — | DB: only_tax_exigible is true on all six reports. | N-U31-103 |
| VDR-U31-C197 | FUNCTION MAPPING REQUIRED | account/models/account_move_line_tax_details.py:407 | OR tax_move.always_tax_exigible | FACT | details helper used | — | The tax-details helper exposes a tax_exigible flag per tax line (not on_payment, or from a cash-basis entry, or always exigible). | N-U31-103 |
| VDR-U31-C198 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:383 | tax_line_vals in tax_results['tax_lines_to_add'] | FACT | add-on installed (uninstalled in DB) | — | Withholding entry tax lines are built from the engine tax lines (so they carry the distribution tags) with negated amounts and balances. | N-U31-099 |
| VDR-U31-C199 | FUNCTION MAPPING REQUIRED | l10n_account_withholding_tax/models/account_withholding_line.py:414 | 'tax_tag_ids': [], | INFERENCE | add-on installed (uninstalled in DB) | RT | The withholding base line is created with empty tax_ids and tax_tag_ids while the counterpart base line spreads the grouping key (which holds the base tags); not executed. | N-U31-099 |
| VDR-U31-C200 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:164 | tax_exigibility = fields.Selection | OBSERVATION | restored DB | — | DB: no tax is on_payment; no cash-basis entry can arise in this configuration; payment-time withholding (uninstalled add-on) would activate the path. | N-U31-104 |
| VDR-U31-C201 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | tax on_payment configured | RT | UNKNOWN - EVIDENCE INSUFFICIENT: cash-basis entry outcomes (tags, dates, partial payments, refunds); resolve by AWT with an on_payment tax. | N-U31-105 |
| VDR-U31-C202 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/__manifest__.py:10 | legal changes | FACT | add-on installed | — | The add-on allows updating tax grids on existing entries; in debug mode a button appears in accounting settings (U23 C168). | N-U31-106 |
| VDR-U31-C203 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/__manifest__.py:13 | 'depends': ['account'] | OBSERVATION | restored DB | — | DB: add-on state uninstalled; wizard model absent. | N-U31-106 |
| VDR-U31-C204 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:669 | def write(self, vals): | INFERENCE | grep | — | No Community code propagates a distribution tag change to existing lines; the add-on is the only re-tagging path found. | N-U31-106 |
| VDR-U31-C205 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:56 | aml.date >= %(date_from)s | FACT | wizard update | — | Base lines are limited to the company and to line date on or after the start date; tax lines have the same filters (line 128). | N-U31-107 |
| VDR-U31-C206 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:94 | impossible to decide for balance | FACT | wizard update | — | For plain entries invoice or refund distribution is derived from amount sign and tax purpose; zero amount defaults to invoice. | N-U31-107 |
| VDR-U31-C207 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:76 | COALESCE(caba_origin_move.move_type, move.move_type) | FACT | wizard update | — | For cash-basis entries the origin document type decides invoice or refund distribution. | N-U31-107 |
| VDR-U31-C208 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:139 | DELETE FROM account_account_tag_account_move_line_rel aml_tags | FACT | wizard update | — | All tag links of every selected line are deleted whatever their origin. | N-U31-107 |
| VDR-U31-C209 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:147 | INSERT INTO account_account_tag_account_move_line_rel | FACT | wizard update | — | Only tags read from base or tax distribution lines are inserted. | N-U31-107 |
| VDR-U31-C210 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:181 | multiple parents is not supported | FACT | wizard update | — | A child tax that belongs to several parent group taxes stops the update with a user error. | N-U31-108 |
| VDR-U31-C211 | PCO-F01 | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:26 | tax_lock_date + timedelta(days=1) | FACT | wizard open | — | The tax lock date only seeds the start date and a display warning; no gate. | N-U31-108 |
| VDR-U31-C212 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/security/ir.model.access.csv:2 | account.group_account_manager | FACT | add-on installed | — | The wizard ACL gives the accounting administrator group read, write and create. | N-U31-108 |
| VDR-U31-C213 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.xml:10 | irreversible | FACT | wizard open | — | The wizard text warns the action is irreversible, will impact reports and recommends a backup. | N-U31-109 |
| VDR-U31-C214 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:49 | self.env.flush_all() | FACT | wizard update | — | The method flushes the ORM and runs raw SQL, then invalidates caches: no ORM write, tracking, constraint or log. | N-U31-109 |
| VDR-U31-C215 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:128 | aml.company_id = %(company_id)s | INFERENCE | wizard update | RT | Neither selection filters on move state, so draft, posted and cancelled entries are all rewritten (re-verifies U23 C185). | N-U31-109 |
| VDR-U31-C216 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:139 | DELETE FROM account_account_tag_account_move_line_rel aml_tags | INFERENCE | items carry product tags | RT | The delete removes every tag link of an affected line, but the insert reads only distribution-line tags; tags of applicability products copied from the product by the engine (AT lines 2405 and 2482) are not re-inserted and are lost. | N-U31-110 |
| VDR-U31-C217 | FUNCTION MAPPING REQUIRED | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:68 | JOIN account_tax_repartition_line tax_to_rep_line | INFERENCE | entries with on_payment taxes | RT | The base-line query joins every tax of the line with no tax_exigibility filter, and the tax-line query keys on the distribution line: on an invoice whose taxes are on_payment the tool would add tags that the engine omits (AT 2412, 2484), risking double counting with cash-basis entries. | N-U31-111 |
| VDR-U31-C218 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | tool executed | RT | UNKNOWN - EVIDENCE INSUFFICIENT: effect on closed returns, hashed entries, reconciled items and report caches; resolve by AWT on a copy (extends U23 C191). | N-U31-112 |
| VDR-U31-C219 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5341 | use_in_tax_closing = fields.Boolean( | FACT | always | — | Distribution line flag use_in_tax_closing (label Tax Closing Entry), computed and stored, editable. | N-U31-113 |
| VDR-U31-C220 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5360 | rep_line.account_id.internal_group not in ('income', 'expense') | FACT | always | — | It defaults true for tax-type lines with an account whose group is neither income nor expense. | N-U31-113 |
| VDR-U31-C221 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:2337 | if tax.analytic or not tax_rep.use_in_tax_closing | FACT | always | — | Reader 1: tax lines inherit the base analytic distribution only for analytic taxes or lines not used in tax closing. | N-U31-114 |
| VDR-U31-C222 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5069 | 'use_in_tax_closing': rep_line.use_in_tax_closing | FACT | always | — | Reader 2: the legacy compute_all result returns the flag per tax line. | N-U31-114 |
| VDR-U31-C223 | FUNCTION MAPPING REQUIRED | account/models/account_move_line_tax_details.py:147 | tax_rep.use_in_tax_closing IS TRUE | FACT | details helper used | — | Reader 3: the tax-details query pairs base and tax lines with it (alongside analytic distribution equality). | N-U31-114 |
| VDR-U31-C224 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:403 | Use in tax closing | FACT | tax used | — | Reader 4: the tax change log text includes the flag. | N-U31-114 |
| VDR-U31-C225 | FUNCTION MAPPING REQUIRED | account/views/account_tax_views.xml:51 | <field name="use_in_tax_closing" | FACT | form view | — | The flag is an optional hidden list column of the distribution lines. | N-U31-114 |
| VDR-U31-C226 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:5341 | use_in_tax_closing = fields.Boolean( | INFERENCE | grep of odoo/addons excluding l10n and tests | — | Grep finds the flag only in account (above readers) and in tests; no closing-entry routine reads it. | N-U31-114 |
| VDR-U31-C227 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:39 | Tax Closing Entry | FACT | always | — | Tax group payable, receivable and advance accounts are described as counterparts or inputs of the Tax Closing Entry. | N-U31-115 |
| VDR-U31-C228 | FUNCTION MAPPING REQUIRED | l10n_th/data/template/account.tax.group-th.csv:6 | tax_group_vat_7 | OBSERVATION | restored DB | — | DB: all five Thai tax groups have payable and receivable accounts set (VAT group 213400 and 114400), none an advance account. | N-U31-115 |
| VDR-U31-C229 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:35 | tax_payable_account_id = fields.Many2one( | INFERENCE | grep of odoo/addons | — | Grep finds the three fields only in their declaration, tax-group views, the chart loader (copy rule and foreign tax-group account creation), foreign template data and an uninstalled regional pack; no closing routine. | N-U31-115 |
| VDR-U31-C230 | PCO-F01 | account/models/company.py:81 | tax_lock_date = fields.Date( | INFERENCE | grep of odoo/addons | — | The help text says the tax lock date is set automatically when the tax closing entry is posted; grep shows no writer in Community (the update-tags add-on only reads it). | N-U31-116 |
| VDR-U31-C231 | FUNCTION MAPPING REQUIRED | account/models/company.py:1151 | def _check_tax_return_configuration | FACT | always | — | A deprecated hook for localizations to check tax return configuration is empty. | N-U31-117 |
| VDR-U31-C232 | PCO-F02 | account/models/account_report.py:98 | This Return Period | FACT | always | — | Report options this return period and last return period exist as selection values. | N-U31-117 |
| VDR-U31-C233 | PCO-F02 | l10n_es_edi_sii/models/account_move.py:57 | 'account_return_periodicity' in self.company_id._fields | OBSERVATION | FOREIGN LOCALIZATION (not installed); label only; restored DB | — | DB: res_company has fiscal-year and lock columns but no return periodicity column; foreign packs guard on the field existing, confirming it is optional and outside Community. | N-U31-117 |
| VDR-U31-C234 | PCO-F02 | account/models/account_report.py:601 | date_scope = fields.Selection( | FACT | always | — | date_scope values: from_beginning, from_fiscalyear, to_beginning_of_fiscalyear, to_beginning_of_period, strict_range, previous_return_period. | N-U31-118 |
| VDR-U31-C235 | PCO-F02 | account/models/account_report.py:612 | default='strict_range' | FACT | always | — | Required, default strict_range. | N-U31-118 |
| VDR-U31-C236 | PCO-F02 | l10n_th/data/account_tax_report_data.xml:153 | previous_return_period | FACT | l10n_th installed | — | Only the Thai line 10 external rule uses a non-default scope in the DB (1 of 29 rules). | N-U31-118 |
| VDR-U31-C237 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:620 | carryover_target = fields.Char( | FACT | always | — | carryover_target is a formula line_code.expression_label naming the carry-over target. | N-U31-119 |
| VDR-U31-C238 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:966 | carryover_origin_expression_label = fields.Char | FACT | always | — | The external value stores the origin expression label and origin line of a carry-over. | N-U31-119 |
| VDR-U31-C239 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:640 | _applied_carryover_ | FACT | always | — | The target label must start with _applied_carryover_. | N-U31-120 |
| VDR-U31-C240 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:639 | label starting with _carryover_ | FACT | always | — | The carryover_target field may be used only on an expression whose label starts with _carryover_. | N-U31-120 |
| VDR-U31-C241 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:927 | Could not determine carryover target automatically | FACT | always | — | Without carryover_target the same-line expression _applied_carryover_<name> is chosen; its absence raises a user error. | N-U31-120 |
| VDR-U31-C242 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:911 | def _get_carryover_target_expression | INFERENCE | grep of odoo/addons | — | No Community code calls _get_carryover_target_expression or creates carry-over values. | N-U31-119 |
| VDR-U31-C243 | PCO-F02 | account/data/account_reports_data.xml:10 | previous_return_period | FACT | always | — | The generic root report opens by default on the previous return period; DB: all six reports carry that default. | N-U31-121 |
| VDR-U31-C244 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:122 | "Use Tax Units" | FACT | always | — | Multi-company mode offers Use Tax Units; the generic report selects it; DB has no tax unit table and the source defines no tax unit model. | N-U31-123 |
| VDR-U31-C245 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | Community source | RT | NOT PRESENT IN COMMUNITY SOURCE: any tax closing entry, return, or period routine. Greps of odoo/addons excluding foreign data and tests: _get_tax_closing, _generate_tax_closing, get_tax_closing, account_return, tax unit return nothing (matches U13 C297, U24 C055, TXA2 C116). | N-U31-122 |
| VDR-U31-C246 | PCO-F02 | n/a | n/a | UNKNOWN | outside package | RT | UNKNOWN - EVIDENCE INSUFFICIENT: how return periods for a Thai monthly filer would be derived and how date scopes are evaluated. | N-U31-124 |
| VDR-U31-C247 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:138 | access_account_report_column_basic | FACT | always | — | Report, line, expression and column definitions: group account_basic read; account_readonly read; account_manager read, write, create, unlink (rows 129-140). | N-U31-125 |
| VDR-U31-C248 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:142 | access_account_report_external_value_readonly | FACT | always | — | External value: account_readonly read; account_manager full (rows 142-143); no row for account_basic. | N-U31-127 |
| VDR-U31-C249 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:78 | access_account_tag_internal_user | FACT | always | — | Tag: internal user read, full accounting group (account_user) read, write, create, unlink, read-only and invoicing groups read (rows 78-81). | N-U31-126 |
| VDR-U31-C250 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:4 | access_account_account_tag_sale_salesman | FACT | sale installed | — | Sales salesman group may read tags. | N-U31-126 |
| VDR-U31-C251 | FUNCTION MAPPING REQUIRED | purchase/security/ir.model.access.csv:17 | access_account_tag_purchase_user | FACT | purchase installed | — | Purchase user group may read tags. | N-U31-126 |
| VDR-U31-C252 | FUNCTION MAPPING REQUIRED | account/security/ir.model.access.csv:85 | access_account_tax_repartition_line_manager | FACT | always | — | Distribution line: internal users, readonly and invoicing read; administrator full (rows 82-85). | N-U31-126 |
| VDR-U31-C253 | FUNCTION MAPPING REQUIRED | account/security/account_security.xml:313 | report_external_value_comp_rule | FACT | always | — | A global record rule limits external values to the user companies. | N-U31-127 |
| VDR-U31-C254 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:950 | _check_company_auto = True | FACT | always | — | External value is company-checked and has a required company with default current company. | N-U31-127 |
| VDR-U31-C255 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | OBSERVATION | restored DB | — | DB: record rules exist on tax, distribution line and external value only; none on the report, line, expression, column or tag models; those four report models and tags have no company field. | N-U31-128 |
| VDR-U31-C256 | FUNCTION MAPPING REQUIRED | account/models/account_account_tag.py:30 | if not self.env.company.multi_vat_foreign_country_ids | FACT | always | — | A tag display name appends the country code only when the company has foreign VAT countries and the tag country differs from its fiscal country. | N-U31-128 |
| VDR-U31-C257 | FUNCTION MAPPING REQUIRED | account/models/company.py:209 | country to use the tax reports | FACT | always | — | Company fiscal country is stored, editable, defaults to the company country and is documented as the country whose tax reports are used. | N-U31-132 |
| VDR-U31-C258 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:301 | tax.country_id = tax.company_id.account_fiscal_country_id | FACT | always | — | Taxes take their country from the company fiscal country, so taxes, tags and reports align per company. | N-U31-132 |
| VDR-U31-C259 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:44 | class AccountReport(models.Model) | OBSERVATION | restored DB | — | DB: no tracked field on report, line, expression, column, external value, tag or distribution line models; the report model has no chatter fields. | N-U31-129 |
| VDR-U31-C260 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:239 | tracking=True, | FACT | always | — | Journal item tax_tag_ids is tracked: edits after the move was posted once are logged on the move. | N-U31-129 |
| VDR-U31-C261 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:210 | repartition_lines_str = fields.Char | FACT | always | — | Tax distribution changes (accounts, factors, grids, closing flag) are tracked through repartition_lines_str when the tax is used (messages 408-420). | N-U31-129 |
| VDR-U31-C262 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:653 | ast.literal_eval(expression.formula) | FACT | domain engine | — | Domain formulas are parsed with literal_eval, not eval. | N-U31-131 |
| VDR-U31-C263 | FUNCTION MAPPING REQUIRED | spreadsheet_account/models/account.py:127 | MoveLines = self.env["account.move.line"].with_company(company_id) | INFERENCE | spreadsheet_account installed | RT | Spreadsheet fetch methods read journal items through the ORM (no sudo) for the requested company; effective access follows record rules. | N-U31-130 |
| VDR-U31-C264 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:45 | _name = 'account.report' | INFERENCE | always | — | Report definitions are writable by the administrator group and shared across companies (no company field, no rule): one administrator change applies to every company. | N-U31-133 |
| VDR-U31-C265 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:718 | def write(self, vals): | INFERENCE | expression write | — | An expression write can rename tags and create tags without any change log. | N-U31-134 |
| VDR-U31-C266 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | real users | RT | UNKNOWN - EVIDENCE INSUFFICIENT: effective access of Thai user roles to report data; DB rows equal source rows, execution not done. | N-U31-135 |
| VDR-U31-C267 | FUNCTION MAPPING REQUIRED | l10n_th/data/account_tax_report_data.xml:7 | <field name="country_id" ref="base.th"/> | INFERENCE | Thai package data | — | The Thai package ships report, lines, tag names and formulas as one data file bound to the country; inferred purpose: layout, tags and formulas are kept consistent without code (no stated rationale in source). | N-U31-006 |
| VDR-U31-C268 | FUNCTION MAPPING REQUIRED | account/models/company.py:203 | account_fiscal_country_id = fields.Many2one( | FACT | always | — | The company fiscal country field selects the country of tax reports; it is defaulted from the company country by a compute at 389-390. | N-U31-016 |
| VDR-U31-C269 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | no viewer in scope | RT | UNKNOWN - EVIDENCE INSUFFICIENT: how lines, columns and options would be presented to a user, because no viewer or client action exists in Community (see the viewer-hook claim). | N-U31-019 |
| VDR-U31-C270 | FUNCTION MAPPING REQUIRED | account/models/account_report.py:209 | ir.actions.client | INFERENCE | derived from the absence claims; viewer hook is the only trace | — | Inference from the not-present claims for evaluator, viewer, export and filing: any Thai return or tax book needs an evaluation, display, export and filing layer from outside the Community source. | N-U31-042 |

## 13. Report items

- **Capabilities covered:** CAP-U31-01 to CAP-U31-10 (10). No capability left unfinished; evaluation, display and filing are NOT PRESENT in Community and are documented as absence with greps (section 14), not as unfinished work.
- **Claims:** 270 rows (203 FACT, 21 OBSERVATION, 32 INFERENCE, 14 UNKNOWN). **Neutral statements:** 135.
- **Native-gap candidates:** U31-F03, F04, F05, F06, F07, F08, F15 (see sections 11 and the Function Catalog); partials: F01, F02, F13, F14, F17, F18, F20.
- **CONTRA with earlier units:** (1) U24 section 10 text and summary row, and the TXC reconciliation table row, count 24 Thai expressions plus 5 from the account module; DB and source show 29 Thai expressions of which 5 are generated from line shortcuts, and 0 generic expressions (VDR-U31-C101 VDR-U31-C102). Locators: U24 lines 106 and 657 (text, no claim id), TXC line 429 (table, no claim id); nearest claim VDR-U24-C075. Refinements, not contradictions: VDR-U13-C038 and VDR-TXA1-C097 describe the tag country filter as a limit on selectable tags; it is a form-level domain only (VDR-U31-C127 VDR-U31-C128); VDR-U23-C180/C181 are consistent with the new inference that product-purpose tags are lost (VDR-U31-C216).
- **RT items:** VDR-U31-C063; VDR-U31-C086; VDR-U31-C088; VDR-U31-C105; VDR-U31-C106; VDR-U31-C143; VDR-U31-C144; VDR-U31-C166; VDR-U31-C179; VDR-U31-C182; VDR-U31-C199; VDR-U31-C201; VDR-U31-C215; VDR-U31-C216; VDR-U31-C217; VDR-U31-C218; VDR-U31-C245; VDR-U31-C246; VDR-U31-C263; VDR-U31-C266; VDR-U31-C269.
- **DISCOVERED SUPPORTING MODULES:** `spreadsheet_account` (installed, auto-install; ledger balance formulas by account code and account tag), `spreadsheet_dashboard` and `spreadsheet_dashboard_account` (installed; invoicing dashboard), `spreadsheet` (installed, dependency), `hr_expense` (installed; company-paid expense tags), `l10n_account_withholding_tax` (uninstalled; payment-time withholding tags, scope of U23 and U24), `account_update_tax_tags` (uninstalled; U23 scope, re-read), `product_margin` (menu only). Foreign hits (labelled, not studied): `l10n_in`, `l10n_fr_account`, `l10n_es_edi_sii`, `l10n_it`.

## 14. Greps performed and limits

Greps run over `odoo/addons` (py, xml, js, csv, json, scss; excluding `i18n`), Community only:
1. Evaluators and viewer: `_compute_formula_batch`, `_report_expand_unfoldable`, `_compute_expression_totals`, `_get_report_expressions`, `caret_options`, `export_to_xlsx`, `export_to_pdf`, `export_to_xml`, `action_open_returns`, `_get_lines\b`, `_dispatch_report`, `_get_report_filename`: no definition. `get_options(`, `get_report_information`, `_init_options`: only foreign-pack hits (`l10n_fr_account` test, `l10n_in` model). `_report_custom_engine`: only foreign-pack data. `report.custom.handler`, `def _report_custom_engine`: none.
2. Client action and menus: `'account_report'`: one source reference (`account_report.py:209`) and one web test; menu ids `account_reports_taxes_and_fiscal_menu`, `account_reports_legal_statements_menu`, `account_reports_partners_reports_menu`, `account_report_folder`: declarations only, no children in Community.
3. Helpers without callers: `_get_tax_exigible_domain` (definition only), `_get_query_tax_details` (test only), `_expand_aggregations`, `_get_carryover_target_expression` (foreign override only), `account.report.external.value` (model, ACL, rule, two foreign migrations).
4. Closing and period: `use_in_tax_closing` (readers listed in CAP-U31-09), `tax_payable_account_id|tax_receivable_account_id|advance_tax_payment_account_id`, `_get_tax_closing`, `_generate_tax_closing`, `get_tax_closing`, `account_return`, `account.return`, `tax_unit_ids`, `account.tax.unit`, `return_period` (declarations and foreign guards only); writers of `tax_lock_date`: none.
5. Statutory outputs: `pp ?30`, `pp ?36`, `pnd` (incl. 54), `e-?filing`, `rd.go.th`, `revenue department`, `withholding certificate`, sales and purchase tax book, tax ledger: nothing relevant outside `l10n_th` (matches only an unrelated Croatian tax name and CSS class names).
6. Tags: `tax_tag_ids`, `account_tag_ids`, `_get_tax_tags`, `_get_matching_tags`, `balance_negate`, `tax_negate` (only foreign migrations), `account.account.tag` in `chart_template.py` (lines 48, 1247 only).

DB queries: counts of report, line, expression, column, external value, tag models; engine split; constraints; ACL, record rules; menus, actions, views, cron, automation; tracked fields; module states; tax exigibility; tax group accounts; tag-to-rule matching; tag distribution links; company lock and cash-basis fields.

**Not read:** the optional reporting package outside Community (no source in scope); `account_edi*` report paths (U13); POS tag path in `point_of_sale` (module uninstalled; only grep hits); the JS of the tax-field widgets in `account/static` (not tag-grid related); `account_tax.js` tax engine mirror; tests other than those cited; foreign localization data (labelled only). Not executed: nothing (source and DB only); no AWT.
