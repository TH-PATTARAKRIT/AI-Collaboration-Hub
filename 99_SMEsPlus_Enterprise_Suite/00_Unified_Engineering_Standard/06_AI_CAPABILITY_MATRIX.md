# SUES AI Capability Matrix

Status: MASTER STANDARD
Version: v1.0
Control Level: /L99

## Purpose

This matrix helps SMEsPlus assign the right AI assistant to the right work type while keeping PMO and gate control intact.

## Capability Matrix

| Work Type | ChatGPT | Claude | Gemini | Copilot | Rule |
|---|---|---|---|---|---|
| PMO Control | Lead | Support | Support | Not primary | Evidence and gate review required |
| Functional Design | Lead | Support | Support | Not primary | No coding |
| Architecture Review | Lead | Support | Support | Support | Evidence required |
| Code Generation | Review | Lead | Support | Lead | Development Gate required |
| Code Review | Lead | Lead | Support | Support | PR evidence required |
| UX/UI Design | Lead | Support | Lead | Not primary | Figma/design evidence required |
| QA/UAT | Lead | Support | Support | Support | Test evidence required |
| Infrastructure | Review | Support | Support | Support | Production HOLD unless approved |
| Evidence Reporting | Lead | Support | Support | Not primary | No Evidence = No Progress |

## Assignment Rule

The project must assign AI by state, module, work type, and gate status.

## Control Rule

AI capability does not equal approval authority. Approval remains with assigned owners, reviewers, PMO, Architecture, QA, Security, and Boss as applicable.
