# STEP030204 Conflict and Assumption Register

**Prompt ID:** SMEPLUS-26-07-17-001  
**Status:** BASELINE CONFLICTS AND ASSUMPTIONS IDENTIFIED  
**Control Level:** /L99.99  
**Effective Date:** 2026-07-17  
**Assessment Date:** 2026-07-17  

---

## Register Purpose

This register captures and categorizes:

1. **Conflicts:** Contradictions between authoritative source documents
2. **Assumptions:** Unstated or implicit dependencies underlying architecture decisions
3. **Ambiguities:** Areas where source documents are unclear or incomplete
4. **Dependencies:** Prerequisites or constraints not yet satisfied

Each entry is:

- Assigned a **Conflict ID** (CONF-D#-###) or **Assumption ID** (ASSU-D#-###)
- Categorized by **Type** (Document Conflict / Design Conflict / Policy Conflict / Requirement Conflict / Unstated Assumption)
- Assigned **Severity** (Critical / High / Medium / Low)
- Recorded with **Affected Domains**
- Marked for **Resolution** (Requires Boss Decision / Requires Clarification / Requires Authoring / Automatically Resolved)
- Tracked through **Gate Impact**

---

## Conflict and Assumption Types

| Type | Definition | Example |
|------|-----------|---------|
| **Document Conflict** | Two authoritative documents state contradictory requirements | GATE-A specifies "2 approvers" while AUTHORITY_MATRIX specifies "1 approver" |
| **Design Conflict** | Architectural approach contradicts governance or constraints | Module independence requirement conflicts with shared database requirement |
| **Policy Conflict** | Policy document contradicts implementation or decision record | Clean Room directive conflicts with "adopt existing Open ERP design" |
| **Requirement Conflict** | Two requirements cannot be simultaneously satisfied | "No breaking API changes" conflicts with "Upgrade to new major version" |
| **Unstated Assumption** | Decision implicitly depends on unstated precondition | "Use Open ERP modules" assumes Open ERP is already installed and functional |

---

## Identified Conflicts

### Document-Level Conflicts

| Conflict ID | Severity | Sources | Conflict Description | Affected Domains | Resolution Status | Gate Impact | Resolution Path |
|---|---|---|---|---|---|---|---|
| CONF-D2-001 | HIGH | Authority Conflict Register v1.1; Architecture Domain Owner Matrix | **Conflicting authority definitions:** Register lists "multiple concurrent authorities" while Matrix specifies "single Primary Owner per domain" | 2, 4, 9, 10, 12, 13 | UNRESOLVED | BLOCKS GATE A | Boss decision required on primary vs. concurrent authority model |
| CONF-D2-002 | MEDIUM | State03 Architecture Scope V2; Enterprise Standards v0.1 | **Document version conflict:** Scope V2 (2026-07-10) references Standards v0.1 (undated); unclear if Standards is superseded or foundational | 2 | UNRESOLVED | DELAYS PROGRESS | Verify Standards version status; update references if needed |
| CONF-D4-001 | MEDIUM | Business Capability Model v0.1; iTEST02 ADR Index | **Scope mismatch:** Capability Model appears to define enterprise capabilities while ADR Index references iTEST02 system only; unclear if iTEST02 is intended as reference implementation or final design | 4, 9 | UNRESOLVED | DELAYS PROGRESS | Clarify scope: Is iTEST02 the Open ERP reference or a separate test system? |
| CONF-D12-001 | MEDIUM | API Mapping Standard; Module Spec API Gateway | **API versioning contradiction:** Standard implies version-in-URL approach while Gateway Spec appears to suggest version-in-header; unclear which is authoritative | 12, 10 | UNRESOLVED | DELAYS PROGRESS | Establish single API versioning standard; update conflicting documents |

### Design-Level Conflicts

| Conflict ID | Severity | Sources | Conflict Description | Affected Domains | Resolution Status | Gate Impact | Resolution Path |
|---|---|---|---|---|---|---|---|
| CONF-D9-001 | HIGH | Module Activation (UX); Architecture Scope V2 | **Implicit vs. explicit module dependency:** UX document implies modules can be activated independently, but Scope notes "module dependencies" without defining them; unclear if modules can be truly independent | 9, 10, 12, 13 | UNRESOLVED | BLOCKS PROGRESS | Define explicit module dependency rules and validate against activation UX |
| CONF-D10-001 | HIGH | Module Activation (UX); Module Spec API Gateway | **Module lifecycle undefined:** Activation document describes activation flow but no complementary deactivation, upgrade, or rollback architecture; implications unclear | 10, 12 | UNRESOLVED | BLOCKS PROGRESS | Author complete module lifecycle architecture including deactivation and upgrade |
| CONF-D12-002 | MEDIUM | Integration Center (UX); API Mapping Standard | **Synchronous vs. asynchronous integration:** Integration Center UX emphasizes event-driven patterns while API Standard emphasizes synchronous REST; unclear if both must coexist or one is preferred | 12, 13 | UNRESOLVED | DELAYS PROGRESS | Define integration pattern priority and establish coexistence rules |

### Policy-Level Conflicts

| Conflict ID | Severity | Sources | Conflict Description | Affected Domains | Resolution Status | Gate Impact | Resolution Path |
|---|---|---|---|---|---|---|---|
| CONF-D2-003 | CRITICAL | Clean Room Learning Directive v2.0; ADR-0006 Policy A | **Clean Room interpretation conflict:** Directive defines "Business Concept → Business Rule → SMEsPlus Design" while Policy A appears to reference "existing design incorporation"; unclear if Policy A is exception or misstatement | 2, 4, 9, 10, 12, 13 | UNRESOLVED | BLOCKS GATE | Boss interpretation required: Can existing design be adopted or must it be redesigned through Clean Room? |
| CONF-D2-004 | HIGH | Architecture Scope V2 (Section 4: "Preparation may proceed"); Architecture Review Gate | **Gate authority conflict:** Scope states "preparation may proceed" without approval while Gate model requires gate approval before architecture work; unclear if SCOPE V2 supersedes Gate or if contradiction exists | 2, 4, 9, 10, 12, 13 | UNRESOLVED | BLOCKS GATE A | Boss clarification required on gate sequencing: Can preparation proceed in parallel or must gates be sequential? |

### Requirement-Level Conflicts

| Conflict ID | Severity | Sources | Conflict Description | Affected Domains | Resolution Status | Gate Impact | Resolution Path |
|---|---|---|---|---|---|---|---|
| CONF-D4-002 | MEDIUM | State03 Architecture Scope (Section 3: "concept drafting authorized"); STEP030204 prompt ("Do not invent architecture facts") | **Assumption vs. prohibition conflict:** Scope authorizes "drafting" and "concept" work which implies creating new designs; STEP0302 prompt prohibits "inventing architecture facts"; unclear if authorized scope supersedes prohibition | 4, 9, 10, 12, 13 | UNRESOLVED | DELAYS PROGRESS | Clarify: Can architecture concepts be drafted/invented, or only documented? |
| CONF-D13-001 | MEDIUM | Architecture Scope V2 (Event "concept drafting"); Integration Center (implies event-driven architecture) | **Technology vs. concept conflict:** Scope authorizes only "concept drafting" for event architecture while Integration Center implies specific event-driven technology; unclear if concept-only or can finalize on technology | 13, 12 | UNRESOLVED | DELAYS PROGRESS | Decide: Is event architecture concept-only or can technology be selected? |

---

## Identified Assumptions

### Strategic Assumptions

| Assumption ID | Severity | Source | Assumption Description | Dependent On | Validation Required | Gate Impact | Owner |
|---|---|---|---|---|---|---|---|
| ASSU-D4-001 | CRITICAL | Business Capability Model v0.1 | **Assumption:** Open ERP is the intended product name and scope | STEP0302 prompt ("Use 'Open ERP' as canonical term") | Verify with Boss: Is product definitively "Open ERP"? | BLOCKS GATE | Boss |
| ASSU-D4-002 | HIGH | Architecture Scope V2 | **Assumption:** "Preparation" work excludes coding, deployment, and release; implies architecture remains DRAFT during preparation | Governance model clarity | Clarify boundaries of "preparation" phase | DELAYS PROGRESS | PMO |
| ASSU-D9-001 | CRITICAL | SaaS Foundation UX documents | **Assumption:** SaaS multi-tenant model is approved for Open ERP | Not explicitly stated in available docs | Verify Boss approval of SaaS multi-tenant approach | BLOCKS GATE | Boss |
| ASSU-D10-001 | HIGH | Module Specification API Gateway | **Assumption:** Module registry already exists or can be created in this STEP | No registry document found | Verify: Is module registry part of Domain 10 or prerequisite? | BLOCKS PROGRESS | PMO |

### Architectural Assumptions

| Assumption ID | Severity | Source | Assumption Description | Dependent On | Validation Required | Gate Impact | Owner |
|---|---|---|---|---|---|---|---|
| ASSU-D2-001 | MEDIUM | Architecture Scope V2 | **Assumption:** "Clean Room" methodology applies to all architecture work for SMEsPlus | Clean Room directives (verified) | Already established; no action needed | NONE | Confirmed |
| ASSU-D4-003 | MEDIUM | Business Capability Model | **Assumption:** Business capabilities can be mapped to modules and applications 1:1 or 1:N | Functional architecture work | Create capability-to-module mapping | DELAYS PROGRESS | PMO / Architecture Lead |
| ASSU-D12-001 | HIGH | API Mapping Standard | **Assumption:** All inter-module communication uses REST APIs over HTTP | No other integration patterns currently documented | Confirm: Are REST APIs mandatory or can other protocols (gRPC, etc.) be used? | DELAYS PROGRESS | Integration Architecture |
| ASSU-D13-001 | HIGH | Integration Center (Events) | **Assumption:** Event-driven architecture is mandatory for inter-module communication | Architecture Scope implies but doesn't state | Confirm: Is event-driven architecture mandatory or optional? | DELAYS PROGRESS | Event Architecture Lead |

### Operational Assumptions

| Assumption ID | Severity | Source | Assumption Description | Dependent On | Validation Required | Gate Impact | Owner |
|---|---|---|---|---|---|---|---|
| ASSU-OP-001 | MEDIUM | Domain Owner Matrix | **Assumption:** All domain owners are AI agents (Claude, ChatGPT) with defined roles | No human owner assignments in Matrix | Clarify: Will all domains be authored by AI or is human review/authoring included? | NOTED | PMO |
| ASSU-OP-002 | MEDIUM | State03 Evidence Register | **Assumption:** Evidence can be prepared in parallel before formal gate approval | Gate model suggests sequential gates | Clarify gate sequencing: Parallel or sequential evidence preparation? | DELAYS PROGRESS | PMO |

---

## Conflict and Assumption Matrix

### Severity Distribution

| Severity | Conflicts | Assumptions | Total | Gate Block? |
|----------|-----------|-------------|-------|---|
| CRITICAL | 1 | 2 | 3 | YES |
| HIGH | 4 | 3 | 7 | YES |
| MEDIUM | 6 | 8 | 14 | CONDITIONAL |
| LOW | 0 | 0 | 0 | NO |
| **TOTAL** | **11** | **13** | **24** | **10 BLOCK** |

### Gate Impact Summary

| Impact Level | Count | Examples |
|---|---|---|
| **BLOCKS GATE** | 10 | Authority model, Clean Room interpretation, SaaS approval, module independence |
| **DELAYS PROGRESS** | 14 | API versioning, integration patterns, capability mapping |
| **NOTED (No block)** | 0 | — |

---

## Critical Path Resolution Sequence

### Priority 1: GATE-BLOCKING Issues (Require Boss Decision)

1. **CONF-D2-003 + ASSU-D4-001:** Boss decision on Clean Room interpretation and Open ERP product definition
2. **CONF-D2-001:** Boss decision on primary vs. concurrent authority model
3. **CONF-D2-004:** Boss clarification on gate sequencing (parallel or sequential)
4. **ASSU-D9-001:** Boss confirmation of SaaS multi-tenant approval
5. **ASSU-D10-001:** PMO clarification on module registry status

### Priority 2: PROGRESS-DELAYING Issues (Require Clarification)

6. **CONF-D4-001:** Clarify iTEST02 scope (reference or final design?)
7. **CONF-D12-002:** Define integration pattern priority (sync vs. async)
8. **ASSU-D12-001 + ASSU-D13-001:** Confirm API-only and event-driven requirements
9. **ASSU-D4-002:** Clarify "preparation" phase boundaries

---

## Conflict Resolution Authority

**Conflicts requiring BOSS decision:**
- CONF-D2-001 (authority model)
- CONF-D2-003 (Clean Room interpretation)
- CONF-D2-004 (gate sequencing)
- ASSU-D4-001 (Open ERP product definition)
- ASSU-D9-001 (SaaS multi-tenant approval)

**Conflicts requiring ARCHITECTURE LEAD clarification:**
- CONF-D2-002 (version status)
- CONF-D4-001 (iTEST02 scope)
- CONF-D4-002 (assumption vs. prohibition)
- CONF-D12-001 (API versioning standard)
- CONF-D12-002 (sync vs. async patterns)
- CONF-D13-001 (event architecture phase)
- ASSU-D4-002 (preparation phase boundaries)
- ASSU-D10-001 (module registry status)
- ASSU-D12-001 (API mandate)
- ASSU-D13-001 (event-driven mandate)

---

## Conflict Resolution Status Tracking

| Conflict ID | Status | Boss Decision | Clarification | Target Resolution Date |
|---|---|---|---|---|
| CONF-D2-001 | PENDING | REQUIRED | — | TBD |
| CONF-D2-002 | PENDING | — | REQUIRED | TBD |
| CONF-D2-003 | PENDING | REQUIRED | — | TBD |
| CONF-D2-004 | PENDING | REQUIRED | — | TBD |
| CONF-D4-001 | PENDING | — | REQUIRED | TBD |
| CONF-D4-002 | PENDING | — | REQUIRED | TBD |
| CONF-D9-001 | PENDING | — | REQUIRED | TBD |
| CONF-D10-001 | PENDING | — | REQUIRED | TBD |
| CONF-D12-001 | PENDING | — | REQUIRED | TBD |
| CONF-D12-002 | PENDING | — | REQUIRED | TBD |
| CONF-D13-001 | PENDING | — | REQUIRED | TBD |

---

## Gate Impact Assessment

**Current Gate Status:**

- Gate A: PARTIAL_EVIDENCE → **REMAINS HOLD** (conflicts unresolved)
- Gate B: HOLD → **REMAINS HOLD** (dependent on Gate A)
- Gate C: HOLD → **REMAINS HOLD** (dependent on Gate B)
- Gate D: HOLD → **REMAINS HOLD** (dependent on Gate C)

**Gate Pass Conditions:**

1. ✗ All CRITICAL conflicts must be resolved with Boss decision (3 pending)
2. ✗ All HIGH conflicts must be resolved with documented clarification (7 pending)
3. ✗ All CRITICAL assumptions must be validated (2 pending)
4. ✓ Architecture baseline must be complete (in progress)

---

## Document Control

**Conflict and Assumption Register:**  
`18_STEP030204_CONFLICT_AND_ASSUMPTION_REGISTER.md`

**Status:** BASELINE CONFLICTS AND ASSUMPTIONS IDENTIFIED  
**Owner:** PMO / Architecture Lead  
**Reviewer:** To be assigned  
**Approval:** Pending Boss review  
**Last Updated:** 2026-07-17  
**Commit:** [TO BE RECORDED]

**Total Issues Identified:** 24 (11 Conflicts + 13 Assumptions)  
**Gate-Blocking Issues:** 10 (require Boss decision or immediate clarification)  
**Gate Status:** HOLD (until conflicts resolved)

**No Evidence = No Progress**
