# STATE 01 SCOPE, PRINCIPLES AND RACI BASELINE

Document ID: SMEPLUS-STATE01-SPR-001  
Version: 1.0  
Status: APPROVED BASELINE  
Approval Date: 2026-07-13

## Product Boundary

In scope: SaaS foundation, tenant/company/user control, Accounting Thailand, Sales, Purchase, Inventory, Product and Master Data, Approval, Audit, Reporting, Dashboard, Integration, and Configuration foundations.

Out of scope unless separately approved: advanced manufacturing, advanced payroll, industry-specific packages, uncontrolled customer customization, direct source copying, unapproved AI coding, release, deployment, and production use.

## Mandatory Principles

1. UI/UX = Simple + Open ERP-first.
2. Control = SMEsPlus / Enterprise-first.
3. Approval Engine approves only.
4. Source Module executes.
5. Posting Engine posts.
6. Events are immutable facts.
7. Clean Room 100%.
8. Business Concept → Business Rule → SMEsPlus Design → New Implementation.
9. No Evidence = No Progress.
10. No Gate skipping.
11. AI cannot approve its own output.
12. Boss is final authority.

## Canonical RACI

| Work | Responsible | Accountable | Reviewer | Approver |
|---|---|---|---|---|
| Project identity documents | Executive Secretary / AI support | Executive Secretary | ChatGPT Governance Review | Boss |
| Governance documents | Assigned Governance Owner | Executive Secretary | Technical/PMO Reviewer | Boss |
| Architecture preparation | Architecture AI / Architect | Named Architecture Owner | ChatGPT Architecture Review | Boss |
| Functional specification | Functional Specification AI | Named Functional Owner | ChatGPT FDS Review | Boss |
| UX/UI design | Figma Design Team | Named UX Owner | Functional + Architecture Review | Boss |
| Development | Claude Code / Developer | Named Development Owner | Code Review + QA | Authorized Gate Approver |
| Testing/UAT | QA/UAT Team | Named QA Owner | Functional Owner | Boss/Authorized UAT Approver |
| Infrastructure | Infrastructure Team | Named Infrastructure Owner | Security/Architecture Reviewer | Boss for Production |

## AI PMO Boundary

AI PMO is Support Only. It may draft, consolidate, check, and prepare evidence. It cannot be Accountable, approve, pass gates, declare completion, merge, release, deploy, or replace Boss authority.

Any work without a named Accountable Owner is OWNER NOT ASSIGNED / HOLD.