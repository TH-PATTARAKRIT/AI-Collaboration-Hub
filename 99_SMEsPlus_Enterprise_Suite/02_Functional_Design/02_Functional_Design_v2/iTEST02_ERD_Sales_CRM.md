# iTEST02 ERD - Sales CRM

Source dump: `iTEST02_2026-06-14_14-41-19.dump`

This ERD is a readable module-level extraction from the PostgreSQL custom dump. It intentionally limits the number of tables and edges so reviewers can understand the functional relationships without opening the full 1,395-table schema.

## Scope

- Module: `Sales_CRM`
- Tables in module: 60
- Tables shown in ERD: 18
- Full foreign key inventory: see `iTEST02_foreign_keys.csv`

## Mermaid ERD

```mermaid
erDiagram
  SALE_ORDER {
    int id PK
    int campaign_id FK
    int source_id FK
    int medium_id FK
    int company_id FK
    int partner_id FK
    int pending_email_template_id FK
    int journal_id FK
  }
  SALE_ORDER_LINE {
    int id PK
    int order_id FK
    int sequence
    int company_id FK
    int currency_id FK
    int order_partner_id FK
    int salesman_id FK
    int product_id FK
  }
  CRM_LEAD {
    int id PK
    int campaign_id FK
    int source_id FK
    int medium_id FK
    int message_bounce
    int user_id FK
    int team_id FK
    int company_id FK
  }
  CRM_TEAM {
    int id PK
    int sequence
    int company_id FK
    int user_id FK
    int color
    int create_uid
    int write_uid
    json name
  }
  UTM_CAMPAIGN {
    int id PK
    int user_id FK
    int stage_id FK
    int color
    int create_uid
    int write_uid
    string name
    json title
  }
  CRM_IAP_LEAD_MINING_REQUEST {
    int id PK
    int lead_number
    int team_id FK
    int user_id FK
    int company_size_min
    int company_size_max
    int contact_number
    int preferred_role_id FK
  }
  UTM_SOURCE {
    int id PK
    int create_uid
    int write_uid
    string name
    date create_date
    date write_date
  }
  CRM_LEAD2OPPORTUNITY_PARTNER_MASS {
    int id PK
    int lead_id FK
    int commercial_partner_id FK
    int partner_id FK
    int user_id FK
    int team_id FK
    int create_uid
    int write_uid
  }
  UTM_MEDIUM {
    int id PK
    int create_uid
    int write_uid
    string name
    bool active
    date create_date
    date write_date
  }
  SALE_ORDER_TEMPLATE {
    int id PK
    int company_id FK
    int sequence
    int mail_template_id FK
    int number_of_days
    int create_uid
    int write_uid
    string name
  }
  CRM_LEAD2OPPORTUNITY_PARTNER {
    int id PK
    int lead_id FK
    int commercial_partner_id FK
    int partner_id FK
    int user_id FK
    int team_id FK
    int create_uid
    int write_uid
  }
  SALE_JOB_TYPE {
    int id PK
    int sequence
    int color
    int create_uid
    int write_uid
    string code
    json name
    string description
  }
  SALE_ORDER_SPREADSHEET {
    int id PK
    int company_id FK
    int order_id FK
    int create_uid
    int write_uid
    string name
    date create_date
    date write_date
  }
  SALE_ORDER_TEMPLATE_LINE {
    int id PK
    int sale_order_template_id FK
    int sequence
    int company_id FK
    int product_id FK
    int product_uom_id FK
    int create_uid
    int write_uid
  }
  CRM_TAG {
    int id PK
    int color
    int create_uid
    int write_uid
    json name
    date create_date
    date write_date
  }
  CRM_LEAD_CONVERT2TICKET {
    int id PK
    int lead_id FK
    int partner_id FK
    int team_id FK
    int create_uid
    int write_uid
    date create_date
    date write_date
  }
  CRM_MERGE_OPPORTUNITY {
    int id PK
    int user_id FK
    int team_id FK
    int create_uid
    int write_uid
    date create_date
    date write_date
  }
  SALE_ADVANCE_PAYMENT_INV {
    int id PK
    int currency_id FK
    int company_id FK
    int create_uid
    int write_uid
    string advance_payment_method
    float fixed_amount
    bool deduct_down_payments
  }
  CRM_TEAM ||--o{ CRM_IAP_LEAD_MINING_REQUEST : "team_id"
  CRM_LEAD ||--o{ CRM_LEAD2OPPORTUNITY_PARTNER : "lead_id"
  CRM_LEAD ||--o{ CRM_LEAD2OPPORTUNITY_PARTNER_MASS : "lead_id"
  CRM_TEAM ||--o{ CRM_LEAD2OPPORTUNITY_PARTNER_MASS : "team_id"
  CRM_TEAM ||--o{ CRM_LEAD2OPPORTUNITY_PARTNER : "team_id"
  UTM_CAMPAIGN ||--o{ CRM_LEAD : "campaign_id"
  CRM_LEAD ||--o{ CRM_LEAD_CONVERT2TICKET : "lead_id"
  CRM_IAP_LEAD_MINING_REQUEST ||--o{ CRM_LEAD : "lead_mining_request_id"
  UTM_MEDIUM ||--o{ CRM_LEAD : "medium_id"
  UTM_SOURCE ||--o{ CRM_LEAD : "source_id"
  CRM_TEAM ||--o{ CRM_LEAD : "team_id"
  CRM_TEAM ||--o{ CRM_MERGE_OPPORTUNITY : "team_id"
  UTM_CAMPAIGN ||--o{ SALE_ORDER : "campaign_id"
  SALE_JOB_TYPE ||--o{ SALE_ORDER : "job_type_id"
  SALE_ORDER_LINE ||--o{ SALE_ORDER_LINE : "linked_line_id"
  SALE_ORDER ||--o{ SALE_ORDER_LINE : "order_id"
  UTM_MEDIUM ||--o{ SALE_ORDER : "medium_id"
  CRM_LEAD ||--o{ SALE_ORDER : "opportunity_id"
  SALE_ORDER_TEMPLATE ||--o{ SALE_ORDER : "sale_order_template_id"
  UTM_SOURCE ||--o{ SALE_ORDER : "source_id"
  SALE_ORDER ||--o{ SALE_ORDER_SPREADSHEET : "order_id"
  CRM_TEAM ||--o{ SALE_ORDER : "team_id"
  SALE_ORDER_TEMPLATE ||--o{ SALE_ORDER_TEMPLATE_LINE : "sale_order_template_id"
  SALE_ORDER_SPREADSHEET ||--o{ SALE_ORDER_TEMPLATE : "spreadsheet_template_id"
```

## Selected tables

- `sale_order`
- `sale_order_line`
- `crm_lead`
- `crm_team`
- `utm_campaign`
- `crm_iap_lead_mining_request`
- `utm_source`
- `crm_lead2opportunity_partner_mass`
- `utm_medium`
- `sale_order_template`
- `crm_lead2opportunity_partner`
- `sale_job_type`
- `sale_order_spreadsheet`
- `sale_order_template_line`
- `crm_tag`
- `crm_lead_convert2ticket`
- `crm_merge_opportunity`
- `sale_advance_payment_inv`
