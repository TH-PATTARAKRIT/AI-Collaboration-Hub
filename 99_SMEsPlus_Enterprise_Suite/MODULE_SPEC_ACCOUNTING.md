# MODULE_SPEC_ACCOUNTING.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Module

Accounting

---

# Purpose

This module controls accounting documents, posting control, journal reference, tax reference, payment reference, and financial reporting input.

---

# Functional Scope

- Chart of accounts
- Journal setup
- Customer invoice
- Vendor bill
- Payment record
- Tax record
- Accounting posting
- Accounting period control
- Accounting report input

---

# Business Rules

BR-ACC-001: Accounting document must belong to one tenant and organization.

BR-ACC-002: Posting must use valid account, journal, tax, and period.

BR-ACC-003: Draft accounting document can be edited before posting.

BR-ACC-004: Posted accounting document must not be changed without authorized reversal process.

---

# Workflow

1. User creates accounting document.
2. System validates account, journal, tax, and period.
3. User reviews document.
4. System posts accounting entry.
5. System updates financial reference.
6. System records accounting event.

---

# Database Mapping

- Account entity
- Journal entity
- Accounting document entity
- Accounting line entity
- Payment entity
- Tax entity
- Accounting event entity

---

# API Mapping

- Create invoice API
- Create bill API
- Post accounting document API
- Register payment API
- Get accounting entry API

---

# UI Mapping

- Chart of accounts screen
- Journal screen
- Customer invoice screen
- Vendor bill screen
- Payment screen
- Accounting entry screen

---

# Acceptance Criteria

AC-ACC-001: User can create accounting document.

AC-ACC-002: System validates required accounting setup.

AC-ACC-003: Posted document creates accounting entry.

AC-ACC-004: Posted document cannot be edited directly.

---

# Traceability

Trace to TRACEABILITY_MATRIX.md after review.

---

# Gate Impact

FDS Gate, Accounting Gate, Traceability Gate

---

# End
