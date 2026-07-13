# STATE 01 PROJECT CHARTER — SMEsPlus Enterprise Suite

Document ID: SMEPLUS-STATE01-CHARTER-001  
Version: 1.0  
State: 01 — Project Identity  
Status: APPROVED BASELINE  
Approval Date: 2026-07-13  
Final Approver: Boss  
Execution Coordinator: Executive Secretary  
AI PMO Role: Support Only

## 1. Project Identity

- Official Project Name: SMEsPlus Enterprise Suite
- Project ID: SMEPLUS-ENTERPRISE-001
- Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
- Branch: SMEsPlus
- Primary Path: 99_SMEsPlus_Enterprise_Suite/

## 2. Product Vision

SMEsPlus Enterprise Suite is an Odoo-first, enterprise-controlled SaaS ERP platform for Thai SMEs and enterprise-lite organizations. It must be simple to use, traceable, scalable, secure, and governed by evidence-based gates.

## 3. Business Problem

Thai SMEs need an ERP platform that reduces operational complexity, supports Thai localization, provides approval and audit controls, integrates core business processes, and avoids uncontrolled customization and fragmented data.

## 4. Target Customers

- Thai SMEs and enterprise-lite organizations
- Multi-company and multi-branch businesses
- Organizations requiring Accounting, Sales, Purchase, Inventory, Approval, Audit, Reporting, and Integration capabilities
- Organizations requiring Thai localization and role-based control

## 5. Initial Product Scope

- SaaS Foundation and tenant control
- Company, user, role, and entitlement management
- Accounting Thailand
- Sales, Purchase, Inventory, Product, and Master Data
- Approval, Audit, Reporting, Dashboard, Integration, and Configuration foundations

## 6. Initial Exclusions

Unless separately approved by Boss:

- Full advanced manufacturing, payroll, and industry-specific solutions
- Customer-specific uncontrolled source customization
- Direct copying or cloning of reference source code
- Broad AI-generated production code without approved FDS, design, tests, and evidence
- Production deployment before the Production Gate passes

## 7. Core Principles

- UI/UX = Simple + Odoo-first
- Control = SMEsPlus / Enterprise-first
- Approval Engine approves only
- Source Module executes
- Posting Engine posts
- Events are immutable facts
- Clean Room 100%
- Business Concept → Business Rule → SMEsPlus Design → New Implementation
- No Evidence = No Progress
- No Gate skipping
- AI cannot self-approve
- Boss is final approval authority

## 8. Delivery Authority

- Jira: execution source
- GitHub: controlled published baseline and version control
- Figma: design authority
- Make: integration and automation layer
- Claude Code: controlled coding agent
- ChatGPT: architect, reviewer, governance controller, and executive secretary support
- ReadyIDC / Proxmox: infrastructure platform

## 9. AI PMO Correction

AI PMO is not an Accountable Owner. AI PMO may prepare drafts, checklists, reports, and evidence only. It may not approve, pass a gate, declare completion, merge, release, deploy, or report unsupported progress.

## 10. Current Gate Boundary

Allowed: identity, governance, architecture preparation, functional design, learning, evidence preparation, UX preparation, and test preparation.

Held: feature build, broad AI coding, merge, release, production deployment, and production use until their required gates pass.

## 11. Success Criteria for State 01

State 01 passes when the Charter, Scope, Principles, RACI, Source-of-Truth Policy, Evidence Register, Gate Review Record, and Boss Approval Record exist in GitHub and are internally consistent.

## 12. Approval

Boss approved execution of State 01 on 2026-07-13. This charter records that decision as the State 01 project identity baseline.