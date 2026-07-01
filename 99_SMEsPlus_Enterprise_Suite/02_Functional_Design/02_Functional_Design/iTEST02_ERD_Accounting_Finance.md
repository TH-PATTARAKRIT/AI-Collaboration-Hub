# iTEST02 ERD - Accounting Finance

Source dump: `iTEST02_2026-06-14_14-41-19.dump`

This ERD is a readable module-level extraction from the PostgreSQL custom dump. It intentionally limits the number of tables and edges so reviewers can understand the functional relationships without opening the full 1,395-table schema.

## Scope

- Module: `Accounting_Finance`
- Tables in module: 178
- Tables shown in ERD: 18
- Full foreign key inventory: see `iTEST02_foreign_keys.csv`

## Mermaid ERD

```mermaid
erDiagram
  ACCOUNT_ACCOUNT {
    int id PK
    int currency_id FK
    int create_uid
    int write_uid
    string account_type
    json name
    json description
    json code_store
  }
  ACCOUNT_MOVE {
    int id PK
    int sequence_number
    int message_main_attachment_id FK
    int journal_id FK
    int company_id FK
    int origin_payment_id FK
    int statement_line_id FK
    int tax_cash_basis_rec_id FK
  }
  ACCOUNT_JOURNAL {
    int id PK
    int alias_id FK
    int default_account_id FK
    int suspense_account_id FK
    int non_deductible_account_id FK
    int sequence
    int currency_id FK
    int company_id FK
  }
  ACCOUNT_MOVE_LINE {
    int id PK
    int move_id FK
    int journal_id FK
    int company_id FK
    int company_currency_id FK
    int sequence
    int account_id FK
    int currency_id FK
  }
  ACCOUNT_PAYMENT {
    int id PK
    int message_main_attachment_id FK
    int move_id FK
    int journal_id FK
    int company_id FK
    int partner_bank_id FK
    int paired_internal_transfer_payment_id FK
    int payment_method_line_id FK
  }
  ACCOUNT_TAX {
    int id PK
    int company_id FK
    int sequence
    int tax_group_id FK
    int cash_basis_transition_account_id FK
    int country_id FK
    int create_uid
    int write_uid
  }
  ACCOUNT_ANALYTIC_LINE {
    int id PK
    int account_id FK
    int product_uom_id FK
    int partner_id FK
    int user_id FK
    int company_id FK
    int currency_id FK
    int create_uid
  }
  ACCOUNT_ASSET {
    int id PK
    int company_id FK
    int currency_id FK
    int method_number
    int account_asset_id FK
    int asset_group_id FK
    int account_depreciation_id FK
    int account_depreciation_expense_id FK
  }
  PAYMENT_TRANSACTION {
    int id PK
    int provider_id FK
    int company_id FK
    int payment_method_id FK
    int currency_id FK
    int token_id FK
    int source_transaction_id FK
    int partner_id FK
  }
  ACCOUNT_BANK_STATEMENT_LINE {
    int id PK
    int move_id FK
    int journal_id FK
    int company_id FK
    int statement_id FK
    int sequence
    int partner_id FK
    int currency_id FK
  }
  ACCOUNT_PAYMENT_REGISTER {
    int id PK
    int currency_id FK
    int journal_id FK
    int partner_bank_id FK
    int custom_user_currency_id FK
    int source_currency_id FK
    int company_id FK
    int partner_id FK
  }
  PAYMENT_PROVIDER {
    int id PK
    int sequence
    int company_id FK
    int redirect_form_view_id FK
    int inline_form_view_id FK
    int token_inline_form_view_id FK
    int express_checkout_form_view_id FK
    int color
  }
  ACCOUNT_RETURN {
    int id PK
    int message_main_attachment_id FK
    int type_id FK
    int company_id FK
    int tax_unit_id FK
    int create_uid
    int write_uid
    string state
  }
  ACCOUNT_REPORT {
    int id PK
    int sequence
    int root_report_id FK
    int country_id FK
    int load_more_limit
    int prefix_groups_threshold
    int create_uid
    int write_uid
  }
  ACCOUNT_FISCAL_POSITION {
    int id PK
    int sequence
    int company_id FK
    int country_id FK
    int country_group_id FK
    int create_uid
    int write_uid
    string zip_from
  }
  ACCOUNT_ANALYTIC_ACCOUNT {
    int id PK
    int plan_id FK
    int root_plan_id FK
    int company_id FK
    int partner_id FK
    int create_uid
    int write_uid
    string code
  }
  ACCOUNT_PAYMENT_METHOD_LINE {
    int id PK
    int sequence
    int payment_method_id FK
    int payment_account_id FK
    int journal_id FK
    int create_uid
    int write_uid
    string name
  }
  ACCOUNT_WITHHOLDING_TAX {
    int id PK
    int account_id FK
    int tax_id FK
    int company_id FK
    int create_uid
    int write_uid
    string name
    string type
  }
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ACCOUNT : "account_stock_expense_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ACCOUNT : "account_stock_variation_id"
  ACCOUNT_ANALYTIC_ACCOUNT ||--o{ ACCOUNT_ANALYTIC_LINE : "account_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ANALYTIC_LINE : "general_account_id"
  ACCOUNT_JOURNAL ||--o{ ACCOUNT_ANALYTIC_LINE : "journal_id"
  ACCOUNT_MOVE_LINE ||--o{ ACCOUNT_ANALYTIC_LINE : "move_line_id"
  ACCOUNT_MOVE ||--o{ ACCOUNT_ANALYTIC_LINE : "timesheet_invoice_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ASSET : "account_asset_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ASSET : "account_depreciation_expense_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_ASSET : "account_depreciation_id"
  ACCOUNT_JOURNAL ||--o{ ACCOUNT_ASSET : "journal_id"
  ACCOUNT_ASSET ||--o{ ACCOUNT_ASSET : "model_id"
  ACCOUNT_ASSET ||--o{ ACCOUNT_ASSET : "parent_id"
  ACCOUNT_JOURNAL ||--o{ ACCOUNT_BANK_STATEMENT_LINE : "journal_id"
  ACCOUNT_MOVE ||--o{ ACCOUNT_BANK_STATEMENT_LINE : "move_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_JOURNAL : "default_account_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_JOURNAL : "loss_account_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_JOURNAL : "non_deductible_account_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_JOURNAL : "profit_account_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_JOURNAL : "suspense_account_id"
  ACCOUNT_ASSET ||--o{ ACCOUNT_MOVE : "asset_id"
  ACCOUNT_MOVE ||--o{ ACCOUNT_MOVE : "auto_invoice_id"
  ACCOUNT_MOVE ||--o{ ACCOUNT_MOVE : "auto_post_origin_id"
  ACCOUNT_RETURN ||--o{ ACCOUNT_MOVE : "closing_return_id"
  ACCOUNT_FISCAL_POSITION ||--o{ ACCOUNT_MOVE : "fiscal_position_id"
  ACCOUNT_JOURNAL ||--o{ ACCOUNT_MOVE : "journal_id"
  ACCOUNT_ACCOUNT ||--o{ ACCOUNT_MOVE_LINE : "account_id"
  ACCOUNT_MOVE_LINE ||--o{ ACCOUNT_MOVE_LINE : "cogs_origin_id"
  ACCOUNT_TAX ||--o{ ACCOUNT_MOVE_LINE : "group_tax_id"
  ACCOUNT_JOURNAL ||--o{ ACCOUNT_MOVE_LINE : "journal_id"
```

## Selected tables

- `account_account`
- `account_move`
- `account_journal`
- `account_move_line`
- `account_payment`
- `account_tax`
- `account_analytic_line`
- `account_asset`
- `payment_transaction`
- `account_bank_statement_line`
- `account_payment_register`
- `payment_provider`
- `account_return`
- `account_report`
- `account_fiscal_position`
- `account_analytic_account`
- `account_payment_method_line`
- `account_withholding_tax`
