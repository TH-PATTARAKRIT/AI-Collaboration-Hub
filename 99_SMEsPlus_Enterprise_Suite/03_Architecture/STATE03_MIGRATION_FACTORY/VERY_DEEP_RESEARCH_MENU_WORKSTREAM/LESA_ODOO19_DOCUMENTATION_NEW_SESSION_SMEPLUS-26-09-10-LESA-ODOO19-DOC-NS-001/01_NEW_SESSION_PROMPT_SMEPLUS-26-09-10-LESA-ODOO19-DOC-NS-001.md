# [SMEPLUS-26-09-10-LESA-ODOO19-DOC-NS-001]
# LESA Odoo 19 Documentation Knowledge Study — NEW SESSION / L9999.9999

Project: `SMEsPlus ENTERPRISE SUITE`  
State: `STATE03 — Architecture / Very Deep Research Support`  
Jira: `ERPPLUS-158`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Primary Owner: `LESA — Learning Evidence Navigator / Source Learning Expert`  
Boss: `Sole Final Approver`

Parent VDR Session: `[SMEPLUS-26-09-10-VDR-MENU-NS-001]` / `ERPPLUS-154`  
Related Consultant Session: `[SMEPLUS-26-09-10-VDR-CONSULT-NS-001]` / `ERPPLUS-157`

Required History File:
`00_CONVERSATION_HISTORY_AND_DECISION_LINEAGE.md`

## 1. Boss Intent

Study the official Odoo 19 documentation root:

`https://www.odoo.com/documentation/19.0/`

for supplementary knowledge, functional orientation, explanation, discovery, terminology, configuration/use-case discovery, and VDR guidance.

This documentation is **NOT Source of Truth for SMEsPlus**.

It is a supporting knowledge source only.

## 2. Constitutional Evidence Separation

Mandatory rule:

```text
Documentation Evidence
!= Source Evidence
!= Runtime Evidence
!= Configuration Reachability Evidence
!= Functional Completeness
!= SMEsPlus Design Decision
```

Also:

```text
Documentation Topic != Runtime Menu
Documentation Function != Runtime Reachable Function
```

LESA MUST preserve these distinctions in every output.

## 3. Why this work exists

The documentation tree can expose:
- application/domain structure;
- documented functions;
- configuration surfaces;
- workflows/use cases;
- reports;
- controls;
- dependencies;
- user-facing terminology;
- exceptions described by the vendor;
- areas that existing source/menu research may have missed.

The objective is not to copy Odoo. The objective is to improve learning completeness and explanation quality before SMEsPlus Functional Design.

## 4. Clean-room Rule

SMEsPlus is a NEW 100% clean-room Node.js SaaS ERP.

Odoo may be used only for:
- learning;
- reference;
- comparison;
- terminology orientation;
- behavior discovery;
- challenge generation;
- generic ERP concept derivation.

Forbidden:
- copying source code;
- cloning schema;
- cloning ORM;
- cloning internal workflow architecture;
- porting implementation mechanisms;
- treating Odoo architecture as SMEsPlus architecture.

## 5. LESA Study Method

Proceed from the documentation root and build a controlled documentation population.

Classify each discovered item as applicable:

```text
DOC-APPLICATION
DOC-DOMAIN
DOC-TOPIC
DOC-SUBTOPIC
DOC-CONFIGURATION
DOC-FUNCTION
DOC-USE-CASE
DOC-REPORT
DOC-CONTROL
DOC-TECHNICAL
```

Each material item should receive a traceable Documentation Learning ID and map to an existing VDR Learning ID where one exists.

## 6. Mandatory Traceability Model

For each material documentation item, capture where applicable:

```text
Documentation URL
→ Documentation Classification
→ Domain / Application
→ Topic / Sub-topic
→ Function / Use Case / Configuration
→ Existing Learning ID (if any)
→ Existing VDR Register Pointer (if any)
→ Source Verification Required? Y/N
→ Runtime Verification Required? Y/N
→ Configuration Verification Required? Y/N
→ Cross-Module Impact Candidate
→ Critical Area Candidate
→ SMEsPlus Interpretation Status
→ Evidence / Notes
```

## 7. Knowledge Status

Use explicit status values:

- `DOCUMENTED`
- `MAPPED TO EXISTING LEARNING`
- `NEW CANDIDATE LEARNING`
- `SOURCE VERIFICATION REQUIRED`
- `RUNTIME VERIFICATION REQUIRED`
- `CONFIGURATION VERIFICATION REQUIRED`
- `CONTRADICTION TO INVESTIGATE`
- `NOT APPLICABLE TO SMEPLUS`
- `CLEAN-ROOM CONCEPT ONLY`

Do not use `PROVEN` solely because the documentation describes it.

## 8. Required Deliverables

LESA shall produce at minimum:

1. `ODOO19_DOCUMENTATION_APPLICATION_DOMAIN_INDEX.md`
2. `ODOO19_DOCUMENTATION_TOPIC_FUNCTION_REGISTER.md`
3. `ODOO19_DOCUMENTATION_TO_VDR_LEARNING_ID_MAP.md`
4. `ODOO19_DOCUMENTATION_CONFIGURATION_AND_DEPENDENCY_HINTS.md`
5. `ODOO19_DOCUMENTATION_CROSS_DOMAIN_KNOWLEDGE_MAP.md`
6. `ODOO19_DOCUMENTATION_CANDIDATE_VDR_GAP_REGISTER.md`
7. `ODOO19_DOCUMENTATION_EXPLANATION_NOTES_FOR_SMEPLUS.md`
8. `ODOO19_DOCUMENTATION_CONTRADICTION_AND_SOURCE_VERIFICATION_QUEUE.md`
9. `ODOO19_DOCUMENTATION_CLEAN_ROOM_INTERPRETATION_REGISTER.md`
10. `LESA_ODOO19_DOCUMENTATION_FINAL_STUDY_REPORT.md`

## 9. Domain Coverage

Study the full documentation tree, not Accounting only.

The official documentation index currently exposes major application groups including Finance, Sales, Inventory & MRP, HR, Services, Productivity, General, Settings, Studio, Marketing, Websites and Odoo Essentials.

Prioritize SMEsPlus-relevant domains first, but preserve a full discovered population so undocumented skips are visible.

## 10. Point-Focus Rule

Do not perform broad reading without traceability.

Every study pass must answer:
- What was discovered?
- Which Learning ID does it affect?
- Is it already known?
- Is there a material delta?
- Does it expose a missing function/configuration/use case?
- Does it challenge an existing VDR claim?
- What further Source/Runtime evidence is required?

No repeated research without material delta.

## 11. Relationship to Canonical VDR

This session supports the Primary VDR. It does not replace it.

Expected flow:

```text
Odoo 19 Official Documentation
→ Documentation Discovery
→ LESA Learning Mapping
→ Candidate Gap / Contradiction
→ Source Resolution
→ Targeted Delta VDR
→ Runtime / Configuration Verification
→ VDR Register Update
→ Coverage Recalculation
→ SMEs Core Independent Challenge
→ PMO Verification
→ Boss Decision
```

## 12. VDR Threshold Rules Carried Forward

For downstream readiness:

- Every Applicable Area / Coverage Dimension must be `>= 96%`.
- Critical Area Coverage must be `100%`.
- `Critical Gap % = 0.00%`.
- `Critical Gap Count = 0`.
- Invalid denominator = `HOLD`.
- Unknown critical function = `HOLD`.
- Missing required runtime/configuration proof = `HOLD`.
- Unresolved material contradiction = `HOLD`.

Documentation coverage is supplementary and cannot compensate for missing Source/Runtime/Configuration proof.

## 13. Specific Questions LESA Must Challenge

For each documented capability:

1. Is this a real runtime menu, a configuration surface, a use case, or only explanatory text?
2. Is the capability always available or optional/module-dependent?
3. What configuration enables/disables it?
4. What permissions/security groups may affect reachability?
5. What business state or prerequisite affects it?
6. Does existing VDR already contain it?
7. If existing VDR contains it, is the understanding consistent with documentation?
8. If inconsistent, which claim requires Source/Runtime resolution?
9. Does it have accounting, inventory, tenant/company, approval, audit, identity, or reconciliation impact?
10. Is it suitable as a reusable ERP concept for SMEsPlus clean-room design, or only product-specific behavior?

## 14. Evidence Rules

Every material statement in LESA outputs must carry an evidence pointer to the documentation URL and, when elevated into verified VDR knowledge, additional Source/Runtime evidence as required.

`Official Documentation` may establish that Odoo officially documents a behavior or feature.

It does NOT establish that:
- the feature is installed;
- it is reachable in a specific database;
- configuration enables it;
- permission allows it;
- runtime behavior matches the documentation in every condition;
- SMEsPlus should implement it the same way.

## 15. Stop Conditions

LESA may stop this session at `DOCUMENTATION STUDY COMPLETE / READY FOR VDR DELTA REVIEW` only when:

- discovered documentation population is recorded;
- material SMEsPlus-relevant domains are studied;
- mappings to Learning IDs are produced;
- candidate gaps/contradictions are listed;
- source/runtime/configuration verification queue is produced;
- no documentation-derived claim is mislabeled as Source of Truth;
- clean-room interpretation is preserved;
- final study report is published.

This status is NOT `RESEARCH COMPLETE` for the underlying ERP functions.

## 16. Governance

- `No Evidence = No Progress`
- `Never Skip Gate`
- `Challenge First → Prompt Second → Execution Third`
- `No repeated question without material delta`
- Boss is the Sole Final Approver.
- LESA may identify, explain, map, resolve source-learning questions and recommend targeted delta research.
- LESA may not self-approve Final SMEsPlus Architecture, Functional Design, Development authorization, Release, or Production.

## 17. Final Principle

```text
Use Documentation to KNOW WHAT TO LOOK FOR.
Use Source to KNOW WHAT EXISTS.
Use Configuration to KNOW WHAT CAN BE ENABLED.
Use Runtime to KNOW WHAT ACTUALLY WORKS.
Use VDR to KNOW WHAT IT MEANS END-TO-END.
Use SMEsPlus Design Authority to DECIDE WHAT WE SHOULD BUILD.
```
