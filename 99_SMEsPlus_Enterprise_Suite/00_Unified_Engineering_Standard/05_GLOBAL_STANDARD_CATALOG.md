# SUES Global Standard Catalog

Status: MASTER STANDARD
Version: v1.0
Control Level: /L99

## Purpose

This catalog defines the global standards that every SMEsPlus state and module must inherit.

## Global Standards

```text
01 Functional Standard
02 Architecture Standard
03 Database Standard
04 UI UX Standard
05 API Standard
06 Security and Audit Standard
07 Infrastructure Standard
08 QA and UAT Standard
09 Evidence Standard
10 AI Execution Standard
11 PMO Gate Standard
12 Knowledge Base Standard
```

## Standard Ownership

Each global standard must have:

```text
Owner
Reviewer
Approver
Evidence path
Jira ID
Version
Gate status
```

## Mandatory Inheritance

Every state and module must inherit the applicable global standards.

Example:

```text
State 04 Functional Specification inherits:
- Functional Standard
- Evidence Standard
- AI Execution Standard
- PMO Gate Standard
- Thai Localization rules where applicable
```

## Flexibility

A module may add extra rules, but must not remove inherited rules unless an approved override exists.
