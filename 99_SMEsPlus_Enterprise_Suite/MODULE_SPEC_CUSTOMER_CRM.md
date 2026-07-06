# MODULE_SPEC_CUSTOMER_CRM.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Module

Customer CRM

---

# Purpose

This module controls customer master data, lead conversion, customer contact management, and customer relationship tracking.

---

# Functional Scope

- Lead record
- Customer profile
- Contact person
- Customer status
- Customer group
- Customer communication log
- Customer ownership
- Customer audit reference

---

# Business Rules

BR-CRM-001: Every customer must belong to one tenant.

BR-CRM-002: Customer code or identity must be unique within tenant scope.

BR-CRM-003: Lead can be converted to customer after required data is complete.

BR-CRM-004: Customer status must control transaction eligibility.

---

# Workflow

1. User creates lead or customer record.
2. System validates required customer data.
3. System checks duplicate identity.
4. User completes customer profile and contact data.
5. System saves customer record.
6. System records customer event.

---

# Database Mapping

- Lead entity
- Customer entity
- Contact entity
- Customer group entity
- Customer communication entity
- Customer audit entity

---

# API Mapping

- Create lead API
- Convert lead API
- Create customer API
- Update customer API
- Get customer profile API

---

# UI Mapping

- Lead list screen
- Lead detail screen
- Customer list screen
- Customer detail screen
- Contact tab
- Communication log tab

---

# Acceptance Criteria

AC-CRM-001: User can create customer with required data.

AC-CRM-002: Duplicate customer identity is detected.

AC-CRM-003: Lead can convert to customer after validation.

AC-CRM-004: Inactive customer cannot be selected for new transaction if rule applies.

---

# Traceability

Trace to TRACEABILITY_MATRIX.md after review.

---

# Gate Impact

FDS Gate, CRM Gate, Traceability Gate

---

# End
