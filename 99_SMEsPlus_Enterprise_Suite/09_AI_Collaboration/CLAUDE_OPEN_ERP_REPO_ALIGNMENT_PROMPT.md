# Claude AI Prompt: Open ERP Repository Alignment

**Project:** SMEsPlus Enterprise Suite  
**Repository:** TH-PATTARAKRIT/AI-Collaboration-Hub  
**Branch:** SMEsPlus  
**Scope:** `99_SMEsPlus_Enterprise_Suite/`  
**Mode:** Documentation alignment / terminology governance / evidence-controlled update  
**Status:** Approved for documentation update only  

---

## 1. Role

Act as a Senior Technical Documentation Engineer, SaaS Architect Assistant, and Repository Governance Assistant for the SMEsPlus Enterprise Suite.

Your task is to align all SMEsPlus architecture, design, standard, and functional documentation with the approved terminology standard:

```text
Use "Open ERP" instead of "Odoo" as the general architecture/design/business term.
```

This is required to keep SMEsPlus vendor-independent and clean-room compliant.

---

## 2. Primary Objective

Update repository documentation so that SMEsPlus uses **Open ERP** consistently in architecture, functional design, standards, and governance documents.

The goal is not to remove all legal/product references. The goal is to remove vendor-specific wording from SMEsPlus-owned architecture and design language.

---

## 3. Mandatory Reference Document

Before changing any file, read and follow:

```text
99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md
```

This document is the single source of truth for the technology stack and terminology policy.

---

## 4. Required Replacement Rule

Replace generic SMEsPlus-owned terminology as follows:

| Old Term | New Term |
|---|---|
| Odoo-first | Open ERP-first |
| Odoo first | Open ERP-first |
| Odoo Architecture | Open ERP Architecture |
| Odoo architecture | Open ERP architecture |
| Odoo Module | Open ERP Module |
| Odoo module | Open ERP module |
| Odoo Standard | Open ERP Standard |
| Odoo standard | Open ERP standard |
| Odoo Database | Open ERP Database |
| Odoo database | Open ERP database |
| Odoo Integration | Open ERP Integration |
| Odoo integration | Open ERP integration |
| Odoo Localization | Open ERP Localization |
| Odoo localization | Open ERP localization |
| Odoo Thai Localization | Open ERP Thai Localization |
| Odoo-style | Open ERP-style |
| Odoo-based | Open ERP-based |
| Odoo reference | Open ERP reference |
| Odoo functional | Open ERP functional |

---

## 5. Do Not Replace in These Cases

Do not replace `Odoo` when the document is referring to the actual product, legal source, license, codebase, ORM, API, module name, evidence, or external reference.

Keep `Odoo` when it appears in contexts like:

```text
Odoo API
Odoo ORM
Odoo source code
Odoo 19
Odoo Enterprise
Odoo Community
Odoo documentation
Odoo license
Odoo migration
Odoo module technical reference
odoo-19.0+e
/path/to/odoo
```

Also do not modify:

- File paths unless explicitly required
- URLs
- GitHub links
- Source-code identifiers
- Package names
- Legal or license statements
- Evidence records from external systems
- Raw logs
- Dump file names
- Screenshot names

---

## 6. Files to Review

Review all Markdown and text documentation under:

```text
99_SMEsPlus_Enterprise_Suite/
```

Priority folders:

```text
00_PROJECT_STANDARD/
01_SaaS_Foundation/
02_Functional_Design/
03_Database_Design/
04_API_Design/
05_Frontend_Design/
06_Engineering/
07_Infrastructure/
08_QA_UAT/
09_AI_Collaboration/
Learning_Analysis/
```

File types to review:

```text
.md
.txt
```

Do not modify binary files.

---

## 7. Required Work Method

Perform the work in this sequence:

1. Scan target files for the word `Odoo`.
2. Classify each occurrence as either:
   - Generic SMEsPlus terminology: replace with `Open ERP`
   - Product/legal/evidence/source reference: keep as `Odoo`
3. Update only the approved generic occurrences.
4. Do not change meaning, scope, gate status, owner, evidence, Jira ID, date, or file reference.
5. Preserve Markdown structure.
6. Preserve table formatting where possible.
7. Create a summary report after edits.

---

## 8. Evidence Report Required

After completing the update, create or update this file:

```text
99_SMEsPlus_Enterprise_Suite/09_AI_Collaboration/OPEN_ERP_TERMINOLOGY_ALIGNMENT_REPORT.md
```

The report must include:

```markdown
# Open ERP Terminology Alignment Report

## 1. Executive Summary
- Status:
- Scope:
- Total files scanned:
- Total files changed:
- Total generic occurrences replaced:
- Total product/legal/evidence occurrences kept:

## 2. Changed Files
| File | Replacement Count | Notes |
|---|---:|---|

## 3. Kept Odoo References
| File | Count | Reason |
|---|---:|---|

## 4. Risk / Blocker
| Risk | Impact | Required Action |
|---|---|---|

## 5. Final Gate Status
- Documentation Alignment:
- Architecture Terminology:
- Clean-room Terminology:
- Build/Coding Impact:
```

---

## 9. Gate Control

This task is allowed for documentation update only.

Allowed:

- Documentation terminology update
- Markdown standardization
- Alignment report creation
- Evidence report creation

Not allowed:

- Feature coding
- Database schema change
- API behavior change
- Package/framework change
- CI/CD change
- Production deployment
- Removing evidence references
- Removing legal/product references

---

## 10. Acceptance Criteria

The task is complete only when:

- `TECHNOLOGY_STACK_STANDARD.md` exists and uses Open ERP terminology.
- Generic SMEsPlus documentation no longer uses `Odoo` as a general architecture term.
- Product/legal/source/evidence references remain unchanged.
- Alignment report is created.
- All changed files are listed with replacement counts.
- No source code or binary files are modified.

---

## 11. Commit Message Recommendation

Use this commit message:

```text
docs: align SMEsPlus terminology from Odoo to Open ERP
```

---

## 12. Final Output Required

Return this summary to Boss:

```text
Open ERP terminology alignment completed.

Files scanned:
Files changed:
Generic replacements:
Product/legal/evidence references kept:
Report file:
Gate status:
Risks/blockers:
Next action:
```

**End of Prompt**
