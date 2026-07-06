# MODULE_SPEC_PURCHASE.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Module

Purchase

---

# Purpose

This module controls purchase request, purchase order, vendor selection, price validation, approval, and procurement lifecycle.

---

# Functional Scope

- Purchase request
- Purchase order
- Vendor selection
- Product selection
- Price and tax calculation
- Purchase approval trigger
- Order status tracking
- Purchase audit reference

---

# Business Rules

BR-PUR-001: Purchase document must belong to one tenant and organization.

BR-PUR-002: Vendor must be active before order confirmation.

BR-PUR-003: Product and price must be valid before confirmation.

BR-PUR-004: Purchase order above approval threshold must follow approval workflow.

BR-PUR-005: Confirmed purchase order must create downstream receiving reference when applicable.

---

# Workflow

1. User creates purchase request or purchase order.
2. System validates vendor and product data.
3. System calculates price, tax, and total.
4. User submits purchase document.
5. System checks approval rule.
6. System updates purchase status.
7. System records purchase event.

---

# Database Mapping

- Purchase request entity
- Purchase order entity
- Purchase line entity
- Vendor reference
- Product reference
- Price reference
- Purchase audit entity

---

# API Mapping

- Create purchase request API
- Create purchase order API
- Update purchase order API
- Confirm purchase order API
- Cancel purchase order API

---

# UI Mapping

- Purchase request list screen
- Purchase request detail screen
- Purchase order list screen
- Purchase order detail screen
- Purchase approval status area

---

# Acceptance Criteria

AC-PUR-001: User can create purchase document with vendor and product.

AC-PUR-002: System calculates total correctly based on rule.

AC-PUR-003: Purchase order requiring approval cannot bypass approval.

AC-PUR-004: Confirmed purchase order changes status correctly.

AC-PUR-005: Purchase event is recorded.

---

# Traceability

Trace to TRACEABILITY_MATRIX.md after review.

---

# Gate Impact

FDS Gate, Purchase Gate, Approval Gate, Traceability Gate

---

# End
