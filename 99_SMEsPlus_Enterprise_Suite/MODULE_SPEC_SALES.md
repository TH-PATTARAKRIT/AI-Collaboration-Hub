# MODULE_SPEC_SALES.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Module

Sales

---

# Purpose

This module controls sales quotation, sales order, pricing, customer confirmation, and sales order lifecycle.

---

# Functional Scope

- Sales quotation
- Sales order
- Customer selection
- Product selection
- Price and discount
- Tax and total calculation
- Sales approval trigger
- Order status tracking
- Sales audit reference

---

# Business Rules

BR-SAL-001: Sales document must belong to one tenant and organization.

BR-SAL-002: Customer must be active before order confirmation.

BR-SAL-003: Product and price must be valid before confirmation.

BR-SAL-004: Sales order above approval threshold must follow approval workflow.

BR-SAL-005: Confirmed sales order must create downstream fulfillment reference when applicable.

---

# Workflow

1. User creates quotation.
2. System validates customer and product data.
3. System calculates price, discount, tax, and total.
4. User submits quotation or confirms sales order.
5. System checks approval rule.
6. System updates sales status.
7. System records sales event.

---

# Database Mapping

- Sales quotation entity
- Sales order entity
- Sales line entity
- Customer reference
- Product reference
- Price reference
- Sales audit entity

---

# API Mapping

- Create quotation API
- Update quotation API
- Confirm sales order API
- Get sales order API
- Cancel sales order API

---

# UI Mapping

- Sales quotation list screen
- Sales quotation detail screen
- Sales order list screen
- Sales order detail screen
- Sales approval status area

---

# Acceptance Criteria

AC-SAL-001: User can create sales quotation with customer and product.

AC-SAL-002: System calculates total correctly based on rule.

AC-SAL-003: Sales order requiring approval cannot bypass approval.

AC-SAL-004: Confirmed sales order changes status correctly.

AC-SAL-005: Sales event is recorded.

---

# Traceability

Trace to TRACEABILITY_MATRIX.md after review.

---

# Gate Impact

FDS Gate, Sales Gate, Approval Gate, Traceability Gate

---

# End
