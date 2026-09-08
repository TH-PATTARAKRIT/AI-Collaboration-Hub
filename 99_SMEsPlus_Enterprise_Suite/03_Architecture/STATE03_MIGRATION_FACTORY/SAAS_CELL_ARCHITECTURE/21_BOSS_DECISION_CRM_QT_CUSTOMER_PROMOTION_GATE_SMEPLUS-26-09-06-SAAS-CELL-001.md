# Boss Decision — CRM Quotation and Customer Promotion Gate

Session: `[SMEPLUS-26-09-06-SAAS-CELL-001]`
Jira: `ERPPLUS-151`
Status: **BOSS APPROVED**
Final Approver: Boss

## Decision

SMEsPlus CRM shall support Quotation (QT) before a Lead becomes a Customer.

Approved business flow:

```text
Lead
-> Opportunity
-> CRM Quotation (QT)
-> Confirm QT
-> Customer Resolution Gate
   -> Existing Customer/Contact: link existing record; do not create duplicate
   -> New Customer/Contact: create canonical Customer/Contact
-> Sales Order (SO)
```

## Approved Rules

1. A raw Lead is not automatically a Customer Master record.
2. CRM may create and manage QT against Lead/Prospect information before Customer creation.
3. `Confirm QT => SO` is the Customer Promotion / Customer Resolution Gate.
4. Before creating a new Customer or Contact, SMEsPlus must search/match for an existing canonical Customer/Contact.
5. If an existing Customer is found, link the QT/SO to that Customer and do not create a duplicate Customer from the Lead.
6. If the Customer exists but the Contact does not, create/link only the new Contact under the existing Customer as appropriate.
7. If no existing Customer/Contact is found and QT is confirmed, create the required canonical Customer/Contact and then create the SO.
8. High-volume unqualified Leads from channels such as Facebook, Website, Campaign, Event, or Import must remain outside Customer Master until the promotion gate is reached.

## Architecture Boundary

```text
CRM
Lead -> Opportunity -> Quotation
                         |
                         | Confirm
                         v
                Customer Resolution
                   |           |
               Existing       New
                   |           |
                   +-----+-----+
                         v
                       Sales
                         v
                    Sales Order
```

## Core Principle

> **Quotation Confirmation is the Customer Promotion Gate.**

> **Lead will not create Customer Master automatically. Existing Customer/Contact must be linked rather than duplicated.**

## Data Hygiene Intent

This decision prevents large volumes of acquisition data (for example, thousands of Facebook Leads) from polluting canonical Customer Master data when only a small subset converts to actual business transactions.

## Scope Note

This decision freezes the architecture/business rule only. Detailed UI, matching algorithm, deduplication confidence rules, exception handling, and field-level design remain open for later Functional / UX design unless separately approved by Boss.
