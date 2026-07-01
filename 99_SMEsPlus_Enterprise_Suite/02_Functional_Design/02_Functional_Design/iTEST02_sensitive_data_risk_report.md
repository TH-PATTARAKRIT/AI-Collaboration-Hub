# iTEST02 Sensitive Data Risk Report

## Executive Summary

The uploaded file is a PostgreSQL custom dump for database `iTEST02`. The schema has ERP/Odoo characteristics and covers accounting, sales, inventory, HR, payroll, manufacturing, website, helpdesk, documents, signing, and AI/knowledge functions. Because this dump contains broad enterprise modules and many columns that match personal, financial, credential, and communication-content patterns, it should be treated as production-like and sensitive unless proven otherwise.

## Dump Metadata

| Item | Value |
|---|---:|
| Dump format | PostgreSQL custom database dump |
| Database name | iTEST02 |
| PostgreSQL version string | 18.4 Debian 18.4-1.pgdg12+1 |
| Tables detected | 1395 |
| Foreign keys detected | 5141 |
| Sensitive-column pattern matches | 1744 |

## Sensitive Data Findings by Category

| Category | Matched columns |
|---|---:|
| PII_Contact | 881 |
| Communication_Content | 338 |
| Financial_Bank | 286 |
| Credential_Token_Secret | 124 |
| HR_Private | 115 |

## Highest Priority Risk Areas

1. **Credentials, tokens, and secrets**: columns matching password, token, secret, API key, OAuth, session, cookie, and private key patterns require immediate masking before external sharing.
2. **HR and payroll**: employee, private address, salary, wage, visa, work permit, marital, emergency contact, and similar fields should be restricted to need-to-know access.
3. **Financial and banking data**: bank, IBAN, account number, payment, balance, credit, debit, salary, and wage related fields require strong protection and audit logging.
4. **PII and customer data**: names, email, phone, address, VAT, tax ID, identification, birthday, and contact fields are privacy-sensitive.
5. **Free-text communication content**: body, message, note, comment, subject, content, and HTML fields may contain uncontrolled personal or confidential business data.

## Top Tables by Sensitive Column Matches

| Table | Matches |
|---|---:|
| `res_partner` | 41 |
| `res_company` | 40 |
| `hr_employee` | 32 |
| `account_move` | 30 |
| `res_config_settings` | 27 |
| `account_move_line` | 23 |
| `hr_version` | 23 |
| `db_backup_configure` | 21 |
| `product_template` | 18 |
| `crm_lead` | 17 |
| `hr_applicant` | 15 |
| `account_payment` | 14 |
| `account_payment_register` | 14 |
| `bh_parent_company` | 14 |
| `hr_salary_rule` | 14 |
| `account_tax` | 13 |
| `sale_order` | 13 |
| `hr_expense` | 12 |
| `payment_transaction` | 12 |
| `hr_payslip` | 11 |
| `appointment_type` | 10 |
| `mail_message` | 10 |
| `helpdesk_ticket` | 10 |
| `purchase_order` | 10 |
| `survey_survey` | 10 |
| `website` | 10 |
| `fetchmail_server` | 9 |
| `ir_mail_server` | 9 |
| `project_task` | 9 |
| `res_country` | 9 |

## Recommended Controls

- Restore only in an isolated environment with no public network exposure.
- Use a separate PostgreSQL role with least privilege for analysis.
- Never provide raw dump data to AI systems or third parties without masking.
- Mask or remove credential, token, bank, salary, employee private, and customer contact fields before sharing.
- Generate domain-specific ERDs and evidence records for Accounting, Stock, HR, Sales, and AI modules.
- Keep checksum, source, restore command, and reviewer sign-off as evidence for backup governance.

## Files Generated

- `iTEST02_module_inventory.csv`
- `iTEST02_foreign_keys.csv`
- `iTEST02_sensitive_columns_inventory.csv`
- `iTEST02_ERD_Accounting_Finance.md`
- `iTEST02_ERD_Sales_CRM.md`
- `iTEST02_ERD_Inventory_Purchase.md`
- `iTEST02_ERD_HR_Payroll.md`
