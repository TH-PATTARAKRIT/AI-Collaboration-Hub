# iTEST02 Functional Design Assumptions

**Generated date:** 2026-07-02

## Scope

This analysis is based on database dump metadata and extracted schema evidence. The work focuses on functional design discovery, module inventory, relationships, sensitive-data exposure, and migration-readiness controls.

## Assumptions

1. The dump is from a PostgreSQL-backed Odoo or Odoo-style ERP implementation.
2. Table and column names are used as the main signal for module grouping and risk classification.
3. The file should be treated as production-like unless explicitly proven otherwise.
4. Personal, financial, employee, token, and communication fields should be treated as sensitive.
5. Functional module boundaries are inferred and should be validated with business owners.

## Limitations

- Business workflows cannot be fully confirmed from schema alone.
- Record counts and live data values were not restored or inspected in this pass.
- Security classification is based on metadata patterns, not row-level content review.
- Some custom modules may be grouped by naming convention rather than confirmed ownership.

## Required Owner Validation

| Area | Owner to validate | Validation question |
|---|---|---|
| Accounting | Finance lead | Are the accounting tables in scope for migration and reporting? |
| Sales and CRM | Sales lead | Which pipeline, lead, and order data must be retained? |
| Stock and Purchase | Supply chain lead | Which warehouse and procurement history is legally or operationally required? |
| HR and Payroll | HR lead | Which employee and payroll fields require masking or exclusion? |
| AI and Knowledge | Product or AI owner | Which vector, chatbot, and knowledge data can be reused safely? |
| Security | Security owner | Which tokens, keys, sessions, or credentials must be purged before sharing? |
