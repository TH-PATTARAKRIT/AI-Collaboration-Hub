# [STATE04][STEP0402][STEP040204] BUSINESS GROUP AND FUNCTION CATALOG

## Introduction

This catalog derives the complete Business Group and Function taxonomy from the 69 Controlled Delta items, organized by Thailand relevance.

## THAILAND IN-SCOPE FUNCTIONS

### Business Group 1: Accounting & Finance (11 functions)

| Function ID | Function Name | Related Delta IDs | Classification |
|---|---|---|---|
| BG1-F1 | Thailand Withholding Tax Calculation | DELTA-001 | IN-SCOPE |
| BG1-F2 | Thailand Withholding Tax Certificate Management | DELTA-002, DELTA-003 | IN-SCOPE |
| BG1-F3 | Thailand Multi-Tax Withholding | DELTA-004 | IN-SCOPE |
| BG1-F4 | Thailand Withholding Tax Reporting | DELTA-005 | IN-SCOPE |
| BG1-F5 | Thailand Accounting Reports | DELTA-006 | IN-SCOPE |
| BG1-F6 | Thailand Revenue Department VAT Integration | DELTA-010 | IN-SCOPE |
| BG1-F7 | PromptPay Invoice Integration | DELTA-012 | IN-SCOPE |

### Business Group 2: Localization (2 functions)

| Function ID | Function Name | Related Delta IDs | Classification |
|---|---|---|---|
| BG2-F1 | Thailand Location Master Data | DELTA-007 | IN-SCOPE |
| BG2-F2 | Thailand Partner Data Localization | DELTA-008 | IN-SCOPE |
| BG2-F3 | Thai Amount Text Conversion | DELTA-009, DELTA-011 | IN-SCOPE |

### Business Group 3: Payment Processing (1 function)

| Function ID | Function Name | Related Delta IDs | Classification |
|---|---|---|---|
| BG3-F1 | 2c2p Payment Gateway | DELTA-013 | IN-SCOPE |

---

## GENERAL BUSINESS FUNCTIONS (OUT-OF-SCOPE FOR THAILAND DESIGN)

### Business Group 4: Sales & Order Management (8 functions)
Sales order sequencing, product branding, product information, gross profit tracking, price history, product filtering

### Business Group 5: Purchasing & Procurement (3 functions)
Purchase requests, purchase discount management

### Business Group 6: Accounting & Reporting (10 functions)
Journal entry printing, check printing, payment remittance, voucher printing, Excel reports, effective dating

### Business Group 7: Product Management (4 functions)
Product sequencing, category filtering, variant management, equipment stock tracking

### Business Group 8: Master Data Management (5 functions)
Location data, location import, contact references, partner types, partner name components

### Business Group 9: Workflow & Approvals (3 functions)
Multi-level approvals, approval configuration, HR approval workflows

### Business Group 10: Data & Infrastructure (8 functions)
Database backup, Redis session management, data removal, file preview, PDF viewer, report integration, file download, import bridges

### Business Group 11: Utilities & Tools (6 functions)
Courier types, date ranges, AI integration, equipment sequencing, bill summarization, app icon hiding, window title

### Business Group 12: Audit & Logging (1 function)
User tracking history

---

## Summary

| Category | Count | Status |
|---|---|---|
| Thailand In-Scope Functions | 13 | READY FOR FUNCTIONAL DESIGN |
| General Business Functions | 44 | OUT-OF-SCOPE FOR THAILAND DESIGN |
| Company-Specific Functions | 11 | OUT-OF-SCOPE (COMPANY-SPECIFIC) |
| **TOTAL** | **69** | **COMPLETE** |

**Note:** Open ERP terminology used per project governance. No "Odoo ERP" project-system name introduced in official documentation.

---
_Generated: 2026-07-17_
