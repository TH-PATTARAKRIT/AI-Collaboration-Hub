# U120 — Multi-Company Accounting in Odoo 19 Community
## Neutral Business Knowledge
## Date: 2026-10-02
## Gap IDs: GAP-002, GAP-018
## Function IDs: MCT-F02 (Intercompany Journal Automation), MCT-F03 (Shared Chart of Accounts)

---

## 1. What Odoo 19 Community Provides for Multi-Company Accounting

Odoo 19 Community includes solid foundational support for operating multiple companies within one installation, but it does not include automated intercompany document creation. The following capabilities are present natively.

### 1.1 Company Isolation on Journals
Each journal (sales, purchase, bank, cash, general) belongs to exactly one company and cannot be shared. This company assignment is permanent once the journal has been used. All journal entries posted through a journal are automatically stamped with that journal's company. If a journal entry's company is changed, the system automatically reselects a journal belonging to the new company. This means all accounting entries are fully segregated by company at the journal level.

### 1.2 Shared Chart of Accounts
Unlike journals, individual account records can be shared across multiple companies simultaneously. This is the core mechanism for a shared chart of accounts in Community. A single account record can be assigned to two or more companies, and each company can have its own account code for that shared account. The system stores per-company account codes in a JSON structure keyed by the company hierarchy root, allowing the same underlying account to appear under different code numbers in different companies.

The shared account model has two important restrictions: Bank and Cash accounts cannot be shared between companies (they must be exclusive to one company), and every account must belong to at least one company.

### 1.3 Subsidiary Chart of Accounts Inheritance
When a subsidiary company (a company with a parent company) installs a chart of accounts template, the system does not create a separate copy of the accounts. Instead, the subsidiary inherits the parent company's existing account records. Default accounts (such as the default receivable, payable, and suspense accounts) for the subsidiary are set to point to the same account records used by the parent company. This means a group of companies under one parent naturally shares a common set of accounts without duplication. The chart of accounts template is automatically propagated down to all direct subsidiaries when it is installed on the parent.

### 1.4 Per-Company Code Mapping
When multiple companies share an account, each company can maintain its own account code for that record. The code mapping is a user interface construct that does not create separate database rows — instead it manages codes stored within the account's code storage field. When a new company is added to an existing account's company list, the system automatically generates an available code for that company's namespace. Conversely, when a shared account needs to be separated, Community provides an administrative action to split the shared account into individual per-company accounts, updating all references accordingly.

### 1.5 Suspense Account Per Company
Each company configures its own journal suspense account. This suspense account is automatically inherited by all bank, cash, and credit journals belonging to that company. The suspense account is used for bank statement lines that have not yet been reconciled. The system enforces that the suspense account must belong to the same company that configures it.

### 1.6 Per-Company Fiscal Lock Dates
Each company independently controls five types of accounting period lock dates: fiscal year lock, tax lock, sale lock, purchase lock, and hard lock. There is no shared global lock across companies. Period-end closing and lock date management is entirely per-company.

### 1.7 Balance Validation Per Company
When the system validates that a journal entry is balanced (debits equal credits), it performs this check using the decimal precision of the entry's own company currency. Entries belonging to different companies are never aggregated for balance checking. This ensures that rounding differences in multi-currency environments are handled according to each company's own currency rules.

### 1.8 Opening Entry Per Company
Each company has its own opening journal entry and opening date configuration. Multi-company accounting period initialization is fully independent, with no requirement for companies to share the same accounting start date or opening entry.

---

## 2. What Is Absent from Community (GAP-002 and GAP-018 Assessment)

### 2.1 Intercompany Invoice Automation (GAP-002 — OPEN in Community)
The module responsible for automated intercompany journal creation (the intercompany rules module) is completely absent from the Odoo 19 Community addons directory. This module, which exists in Odoo Enterprise, provides the following capabilities that are not available in Community:

- When a customer invoice is confirmed in Company A, automatically generating a corresponding vendor bill in Company B
- When a vendor bill is confirmed in Company B, automatically generating a corresponding customer invoice in Company A
- Configurable rules for which companies trigger automated mirror documents in which other companies
- Intercompany payable and receivable account configuration per company pair

In Community, there is no automated mechanism of any kind that creates a matching document in another company when a document is posted. Any intercompany transaction must be entered manually in each company. There are no intercompany payable or receivable account fields on the company record in Community — only a same-company inter-bank transfer account (for moving money between the company's own bank accounts).

### 2.2 Shared Chart of Accounts (GAP-018 — PARTIAL in Community)
Community does support sharing account records across multiple companies through the many-to-many company assignment mechanism. A group of companies can therefore share a common chart of accounts. However, several aspects differ from a full Enterprise-level shared COA:

- The sharing is opt-in per account — there is no single "shared COA" flag or central governance mechanism
- Bank and Cash accounts cannot be shared
- The subsidiary inheritance model works during template installation but does not enforce ongoing synchronization of account properties across companies
- There is no automated propagation of new accounts created in one company to sibling companies
- The Account Groups synchronization is per-company root and managed through the delay_account_group_sync mechanism

---

## 3. Company Domain Enforcement Summary

The following enforcement mechanisms exist in Community to prevent cross-company data mixing:

- Automatic ORM-level validation of all company-restricted relational fields on journal entries (activated via the model-level flag)
- Validation that a journal entry's company always matches its journal's company
- Validation that a journal entry line's company matches the parent entry's company
- Validation that a bank journal's linked bank account belongs to the same company
- Validation that account codes are unique within the company hierarchy (not just the current company)
- Validation that the company cannot be removed from an account if journal entries exist for that company
- Validation that a journal's company cannot be changed once journal entries exist

---

## 4. Relevance to SMEsPlus Programme

For the SMEsPlus programme operating across multiple legal entities:

- Manual intercompany entry is the only available method in Community — automated intercompany document generation requires the Enterprise intercompany rules module or a custom implementation
- A shared chart of accounts is achievable in Community through the subsidiary inheritance model, but requires careful account structure design before deployment
- Each entity (company) will have fully independent fiscal calendars, lock dates, and tax configurations
- Bank and cash accounts must be per-company and cannot be pooled under a shared account record

GAP-002 (MCT-F02 intercompany journal automation) remains OPEN in Community — there is no built-in automated intercompany journal creation.

GAP-018 (MCT-F03 shared chart of accounts) is PARTIAL in Community — account sharing is technically available through the many-to-many company assignment and subsidiary inheritance, but lacks the governance and automation layer present in Enterprise.
