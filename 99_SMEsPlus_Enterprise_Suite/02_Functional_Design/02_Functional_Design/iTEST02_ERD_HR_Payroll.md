# iTEST02 ERD - HR Payroll

Source dump: `iTEST02_2026-06-14_14-41-19.dump`

This ERD is a readable module-level extraction from the PostgreSQL custom dump. It intentionally limits the number of tables and edges so reviewers can understand the functional relationships without opening the full 1,395-table schema.

## Scope

- Module: `HR_Payroll`
- Tables in module: 179
- Tables shown in ERD: 18
- Full foreign key inventory: see `iTEST02_foreign_keys.csv`

## Mermaid ERD

```mermaid
erDiagram
  HR_EMPLOYEE {
    int id PK
    int resource_id FK
    int company_id FK
    int message_main_attachment_id FK
    int current_version_id FK
    int user_id FK
    int work_contact_id FK
    int country_of_birth
  }
  HR_APPLICANT {
    int id PK
    int campaign_id FK
    int source_id FK
    int medium_id FK
    int message_bounce
    int message_main_attachment_id FK
    int sequence
    int partner_id FK
  }
  HR_JOB {
    int id PK
    int sequence
    int no_of_recruitment
    int user_id FK
    int department_id FK
    int company_id FK
    int contract_type_id FK
    int create_uid
  }
  HR_VERSION {
    int id PK
    int company_id FK
    int employee_id FK
    int last_modified_uid
    int country_id FK
    int private_state_id FK
    int private_country_id FK
    int distance_home_work
  }
  HR_DEPARTMENT {
    int id PK
    int company_id FK
    int parent_id FK
    int manager_id FK
    int color
    int master_department_id FK
    int create_uid
    int write_uid
  }
  HR_EXPENSE {
    int id PK
    int message_main_attachment_id FK
    int employee_id FK
    int department_id FK
    int manager_id FK
    int company_id FK
    int product_id FK
    int product_uom_id FK
  }
  HR_PAYSLIP {
    int id PK
    int message_main_attachment_id FK
    int struct_id FK
    int employee_id FK
    int department_id FK
    int job_id FK
    int company_id FK
    int version_id FK
  }
  HR_LEAVE {
    int id PK
    int message_main_attachment_id FK
    int user_id FK
    int holiday_status_id FK
    int employee_id FK
    int employee_company_id FK
    int company_id FK
    int department_id FK
  }
  HR_APPRAISAL {
    int id PK
    int employee_id FK
    int company_id FK
    int department_id FK
    int job_id FK
    int appraisal_template_id FK
    int assessment_note
    int create_uid
  }
  PLANNING_SLOT {
    int id PK
    int resource_id FK
    int employee_id FK
    int department_id FK
    int user_id FK
    int manager_id FK
    int company_id FK
    int role_id FK
  }
  HR_WORK_LOCATION {
    int id PK
    int company_id FK
    int address_id FK
    int create_uid
    int write_uid
    string name
    string location_type
    string location_number
  }
  HR_APPRAISAL_GOAL {
    int id PK
    int company_id FK
    int template_goal_id FK
    int number_of_sibling_goals
    int number_of_completed_sibling_goals
    int parent_id FK
    int usual_duration_month
    int create_uid
  }
  HR_LEAVE_TYPE {
    int id PK
    int sequence
    int color
    int icon_id FK
    int company_id FK
    int country_id FK
    int leave_notif_subtype_id FK
    int allocation_notif_subtype_id FK
  }
  HR_SALARY_RULE {
    int id PK
    int struct_id FK
    int sequence
    int category_id FK
    int condition_other_input_id FK
    int amount_other_input_id FK
    int partner_id FK
    int input_section
  }
  HR_WORK_ENTRY_TYPE {
    int id PK
    int color
    int sequence
    int country_id FK
    int create_uid
    int write_uid
    string code
    string external_code
  }
  HR_PAYROLL_STRUCTURE {
    int id PK
    int type_id FK
    int country_id FK
    int report_id FK
    int create_uid
    int write_uid
    string code
    json name
  }
  HR_EXPENSE_SPLIT {
    int id PK
    int wizard_id FK
    int expense_id FK
    int product_id FK
    int employee_id FK
    int company_id FK
    int currency_id FK
    int manager_id FK
  }
  HR_SKILL {
    int id PK
    int sequence
    int skill_type_id FK
    int create_uid
    int write_uid
    json name
    date create_date
    date write_date
  }
  HR_DEPARTMENT ||--o{ HR_APPLICANT : "department_id"
  HR_EMPLOYEE ||--o{ HR_APPLICANT : "employee_id"
  HR_JOB ||--o{ HR_APPLICANT : "job_id"
  HR_APPLICANT ||--o{ HR_APPLICANT : "pool_applicant_id"
  HR_DEPARTMENT ||--o{ HR_APPRAISAL : "department_id"
  HR_EMPLOYEE ||--o{ HR_APPRAISAL : "employee_id"
  HR_APPRAISAL_GOAL ||--o{ HR_APPRAISAL_GOAL : "parent_id"
  HR_APPRAISAL_GOAL ||--o{ HR_APPRAISAL_GOAL : "template_goal_id"
  HR_JOB ||--o{ HR_APPRAISAL : "job_id"
  HR_JOB ||--o{ HR_APPRAISAL : "target_job_id"
  HR_EMPLOYEE ||--o{ HR_DEPARTMENT : "manager_id"
  HR_DEPARTMENT ||--o{ HR_DEPARTMENT : "master_department_id"
  HR_DEPARTMENT ||--o{ HR_DEPARTMENT : "parent_id"
  HR_EMPLOYEE ||--o{ HR_EMPLOYEE : "coach_id"
  HR_VERSION ||--o{ HR_EMPLOYEE : "current_version_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "friday_location_id"
  HR_APPRAISAL ||--o{ HR_EMPLOYEE : "last_appraisal_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "monday_location_id"
  HR_EMPLOYEE ||--o{ HR_EMPLOYEE : "parent_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "saturday_location_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "sunday_location_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "thursday_location_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "tuesday_location_id"
  HR_WORK_LOCATION ||--o{ HR_EMPLOYEE : "wednesday_location_id"
  HR_DEPARTMENT ||--o{ HR_EXPENSE : "department_id"
  HR_EMPLOYEE ||--o{ HR_EXPENSE : "employee_id"
  HR_PAYSLIP ||--o{ HR_EXPENSE : "payslip_id"
  HR_EMPLOYEE ||--o{ HR_EXPENSE_SPLIT : "employee_id"
  HR_EXPENSE ||--o{ HR_EXPENSE_SPLIT : "expense_id"
  HR_EXPENSE ||--o{ HR_EXPENSE : "split_expense_origin_id"
```

## Selected tables

- `hr_employee`
- `hr_applicant`
- `hr_job`
- `hr_version`
- `hr_department`
- `hr_expense`
- `hr_payslip`
- `hr_leave`
- `hr_appraisal`
- `planning_slot`
- `hr_work_location`
- `hr_appraisal_goal`
- `hr_leave_type`
- `hr_salary_rule`
- `hr_work_entry_type`
- `hr_payroll_structure`
- `hr_expense_split`
- `hr_skill`
