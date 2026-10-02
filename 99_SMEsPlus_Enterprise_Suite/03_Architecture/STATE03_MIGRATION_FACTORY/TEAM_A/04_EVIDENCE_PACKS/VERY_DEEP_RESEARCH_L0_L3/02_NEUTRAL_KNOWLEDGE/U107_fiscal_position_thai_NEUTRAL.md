# U107 — Neutral Knowledge Layer: Fiscal Position Thai Edge Cases
<!-- ALL CONTENT: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION -->

**Unit**: U107  
**Knowledge layer**: Neutral (no implementation-specific identifiers)  

---

## NR-01 — Fiscal Position Model Structure
A fiscal position is an ordered accounting rule set that adapts taxes and revenue or expense accounts on transactions involving specific partners or geographies. Ordering is controlled by a sequence number. Company ownership is enforced to prevent cross-company data leakage.

## NR-02 — Tax Substitution Link
A fiscal position maintains a collection of replacement taxes. The relationship between a fiscal position and its associated taxes is recorded in a dedicated database join table, allowing many-to-many linkage in both directions.

## NR-03 — Tax Mapping Algorithm
The engine for tax substitution relies on a two-level lookup. Each replacement tax declares which original domestic tax or taxes it replaces. The fiscal position assembles this into a reverse index at compute time: for each original tax, the index records which replacement taxes should be used instead. Taxes not present in the index pass through unchanged.

## NR-04 — No-Position Passthrough
When no fiscal position is active on a transaction, all taxes on a product or line are applied as-is. No substitution or removal occurs.

## NR-05 — Empty-Mapping Filter Behavior
When a fiscal position is active but carries no tax substitution rules, any tax that is explicitly designated as belonging to a named fiscal position is removed from the transaction. Only taxes with no fiscal position designation are kept. This is an important edge case: a fiscal position without rules can act as a filter that removes foreign or specialized taxes from a domestic transaction.

## NR-06 — Substitution Passthrough for Unmapped Taxes
During tax substitution, any tax on a line that has no entry in the fiscal position's substitution index is passed through to the output unchanged. This means partial mappings are safe: only the specified taxes are replaced, all others remain.

## NR-07 — Account Substitution
Fiscal positions may also remap revenue and expense accounts. The account substitution is a simple dictionary lookup: if the source account has an entry in the mapping, the destination account is used instead. If not, the original account is returned.

## NR-08 — Auto-Detection Logic
Automatic fiscal position selection evaluates each candidate position (flagged for automatic detection) against the delivery partner in sequence order, applying five criteria in order: whether the partner has a tax registration number (if required), whether the partner's postal code falls in the configured range, whether the partner's administrative region is in the allowed set, whether the partner's country matches, and whether the partner's country belongs to the configured country grouping. The first position passing all active criteria is selected.

## NR-09 — VAT Number Gate
A fiscal position may require that a partner possess a valid tax identification number before the position applies. This is used to distinguish business-to-business transactions from consumer transactions, a common VAT regulatory distinction.

## NR-10 — Postal Code Range
Fiscal positions support selection by postal code range, enabling sub-national tax zones such as special economic areas or free trade zones to be handled without creating separate country-level positions.

## NR-11 — Three-Tier Priority
Fiscal position resolution uses a fixed priority chain. A company-level default for purchase receipt documents takes the highest priority. A manually assigned position on the partner record takes the next priority. Automatic detection from partner geography and attributes applies last. Manual assignment always wins over automatic detection.

## NR-12 — Purchase Receipt Override
A separate company-level setting allows a fixed fiscal position to be applied to all purchase receipt documents regardless of partner. This is intended for regulatory contexts where purchase receipts must always use a specific tax treatment.

## NR-13 — Foreign VAT Country Alignment
When a fiscal position carries a foreign tax registration number, the tax country for all journal entries under that position is set to the country of the fiscal position rather than the company's own fiscal country. A validation constraint prevents posting entries that mix taxes from different countries on the same document when this cross-border position is in use.

## NR-14 — Domestic Position Flag
A fiscal position is designated as domestic when it matches the company's primary domestic fiscal position record. This flag propagates to taxes: a tax is domestic when it has no fiscal position assignment at all, or when the domestic position is among its assigned positions.

## NR-15 — Thai Template: No Fiscal Positions
The Thai chart of accounts template ships with no pre-configured fiscal position records. All tax records in the Thai template leave the fiscal position assignment blank, meaning every Thai tax is treated as a domestic tax at installation time.

## NR-16 — Thai Standard VAT
The Thai template configures 7 percent as the standard value-added tax rate for both purchases and sales. This rate is set as the company-wide default for new transactions.

## NR-17 — Thai Zero Rate and Exempt Categories
The Thai template distinguishes between two non-standard VAT categories: a zero-rate category (applicable to exports and certain internationally traded services) and an exempt category (applicable to goods and services legally excluded from the VAT system entirely). These are defined as separate tax records with separate report tags matching Thailand's VAT form structure, but are not linked to any fiscal position at installation.

## NR-18 — Thai Withholding Tax Groups
The Thai template defines four withholding tax groups at 1, 2, 3, and 5 percent, each associated with dedicated payable and receivable accounts. These groups correspond to Thai Revenue Code categories for different income types. Withholding taxes are entirely separate from VAT and have no fiscal position assignment in the template.

## NR-19 — No Thai Intra-Company Fiscal Position Template
The Thai template provides no intra-company fiscal position. Any requirement to apply different tax treatment for transactions between related Thai entities must be built manually at deployment time. The EU-specific intra-community logic built into the auto-detection engine (which uses VAT registration prefix matching) has no counterpart for Thailand.

## NR-20 — User-Triggered Line Update
Changing the fiscal position on a draft document with existing lines does not immediately re-map taxes or accounts. A user-visible flag is set to prompt the operator to trigger an update, preserving existing line data until explicitly refreshed.

---

## Key Thai-Specific Gaps Identified

1. No fiscal position template for export (zero rate) scenario — must be created manually
2. No fiscal position template to switch from standard 7 percent to zero rate or exempt on specific partner geographies
3. Withholding taxes have no fiscal position interaction defined — WHT co-existence with VAT fiscal positions requires manual design
4. No intra-company fiscal position shipped — multi-entity Thai deployments need manual configuration
5. The empty-mapping filter behavior (NR-05) is a critical edge case: a Thai export fiscal position created with no tax rules would strip all non-domestic taxes but leave domestic VAT — potentially incorrect behavior if the intent was to substitute 7 percent with 0 percent
