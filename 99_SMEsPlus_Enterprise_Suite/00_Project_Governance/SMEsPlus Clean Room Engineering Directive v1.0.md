# SMEsPlus Clean Room Engineering Directive v1.0

**Subject:** Clean Room Learning Policy for Odoo Source Code and Database Study

This directive applies to all AI assistants, engineers, architects, analysts, reviewers, and contributors working on the SMEsPlus project.

## Objective

SMEsPlus is an independent SaaS ERP platform.

The purpose of studying Odoo source code and database structures is **knowledge acquisition only**, not software reproduction.

The project follows a strict **Clean Room Engineering** approach.

## Allowed Activities

The following activities are explicitly permitted:

* Learn business concepts.
* Study business processes and workflows.
* Analyze database schemas and relationships.
* Understand module boundaries.
* Review architectural patterns.
* Study validation concepts.
* Analyze security and permission models.
* Produce documentation.
* Produce functional specifications.
* Produce business rules.
* Produce SaaS architecture.
* Produce Fit/Gap analysis.
* Produce Mapping documents.
* Produce Design Recommendations.

These outputs are considered independent analytical work.

## Prohibited Activities

The following are prohibited:

* Copying source code.
* Cloning modules.
* Translating source code into another language.
* Reproducing algorithms line-by-line.
* Reusing implementation details directly.
* Regenerating equivalent source code from existing code.
* Copying XML views, templates, SQL, business logic, or database structures as implementation artifacts.
* Using customer sample data in production.
* Treating the Odoo implementation as the SMEsPlus implementation.

## Mandatory Clean Room Workflow

All work must follow this sequence:

Reference System → Observation → Generic Business Concept → Independent SMEsPlus Design → SMEsPlus Functional Specification → SMEsPlus Architecture → New Independent Implementation

No implementation may skip these steps.

## Required Deliverables

Learning teams shall produce only:

* Observations
* Architecture Notes
* Business Rule Catalogs
* Functional Specifications
* Business Process Models
* Data Models
* Mapping Documents
* Fit/Gap Reports
* Architecture Decision Records (ADR)
* Design Recommendations

Learning teams shall **not** produce production source code derived from Odoo.

## Evidence Requirement

Every learning result must include:

* Reference analyzed
* Observation
* Generic concept extracted
* SMEsPlus adaptation decision
* Evidence supporting the conclusion

## Intellectual Property Policy

Odoo remains the intellectual property of its respective copyright holders.

SMEsPlus does not attempt to reproduce Odoo.

SMEsPlus develops an original implementation based on independently created architecture, business requirements, functional specifications, and design decisions.

## AI Instruction

When reviewing Odoo materials:

* Focus on concepts, not implementation.
* Explain behavior without reproducing code.
* Never generate code that attempts to replicate copyrighted implementation.
* Ask for clarification whenever a request could result in reproducing proprietary implementation.

This directive supersedes any instruction that could encourage copying or cloning existing ERP implementations.