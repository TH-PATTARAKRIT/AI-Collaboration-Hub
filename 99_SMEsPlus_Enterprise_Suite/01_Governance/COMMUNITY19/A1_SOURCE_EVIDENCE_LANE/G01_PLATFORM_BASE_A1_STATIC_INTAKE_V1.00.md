# G01 PLATFORM_BASE — A1 Static Source Intake V1.00

**Date:** 2026-09-24  
**Mode:** A1 Source Evidence Lane only  
**Current exact membership source:** FREEZE_W1-STD.json (23 modules)  
**Static manifest metadata source:** historical/mixed-source MODULE_MASTER_REGISTER_FULL.csv — SECONDARY EVIDENCE ONLY; requires Community19 source re-anchor.

## Initial Static Manifest Inventory

| Module | Declared name | Ver. | Licence | Install | App | Auto | Direct dependencies | Static declared purpose |
|---|---|---:|---|---|---|---|---|---|
| auth_signup | Signup | 1.0 | LGPL-3 | Yes | No | Yes | base_setup; mail; web | — |
| base | Base | 1.3 | LGPL-3 | Yes | No | Yes | — | — |
| base_automation | Automation Rules | 1.0 | LGPL-3 | Yes | No | No | base; digest; resource; mail; sms | — |
| base_setup | Initial Setup Tools | 1.0 | LGPL-3 | Yes | No | Yes | base; web | — |
| base_sparse_field | Sparse Fields | 1.0 | LGPL-3 | Yes | No | No | base | Implementation of sparse fields |
| bus | IM Bus | 1.0 | LGPL-3 | Yes | No | Yes | base; web | — |
| digest | KPI Digests | 1.1 | LGPL-3 | Yes | No | No | mail; portal; resource | — |
| google_recaptcha | Google reCAPTCHA integration | 1.0 | LGPL-3 | Yes | No | No | base_setup | — |
| html_builder | HTML Builder | 0.1 | LGPL-3 | Yes | No | No | base; html_editor; mail | Generic html builder |
| html_editor | HTML Editor | 1.0 | LGPL-3 | Yes | No | Yes | base; bus; web | A HTML Editor component and plugin system |
| http_routing | Web Routing | — | LGPL-3 | Yes | No | No | web | Web Routing |
| mail | Discuss | 1.19 | LGPL-3 | Yes | Yes | No | base; base_setup; bus; web_tour; html_editor | Chat, mail gateway and private channels |
| onboarding | Onboarding Toolbox | 1.2 | LGPL-3 | Yes | No | No | web | — |
| phone_validation | Phone Numbers Validation | 2.1 | LGPL-3 | Yes | No | Yes | base; mail | Validate and format phone numbers |
| portal | Customer Portal | — | LGPL-3 | Yes | No | No | web; html_editor; http_routing; mail; auth_signup | Customer Portal |
| privacy_lookup | Privacy | 1.0 | LGPL-3 | Yes | No | Yes | mail | — |
| resource | Resource | 1.1 | LGPL-3 | Yes | No | No | base; web | — |
| resource_mail | Resource Mail | 1.0 | LGPL-3 | Yes | No | Yes | resource; mail | — |
| utm | UTM Trackers | 1.1 | LGPL-3 | Yes | No | No | base; web | — |
| web | Web | 1.0 | LGPL-3 | Yes | No | Yes | base | — |
| web_hierarchy | Web Hierarchy | 1.0 | LGPL-3 | Yes | No | No | web | — |
| web_tour | Tours | 1.0 | LGPL-3 | Yes | No | Yes | web | — |
| web_unsplash | Unsplash Image Library | 1.1 | LGPL-3 | Yes | No | Yes | base_setup; html_editor | Find free high-resolution images from Unsplash |

## Static Dependency Observations — Intake Only

1. base is the zero-dependency root inside this G01 roster and is a direct dependency of several platform modules.
2. web depends on base and acts as a static dependency hub for setup, routing, portal, resource, UTM, tours and hierarchy capabilities.
3. mail depends on base, base_setup, bus, web_tour, and html_editor, indicating a cross-cutting communication layer with substantial platform coupling.
4. portal statically joins web/routing/html/mail/signup concerns.
5. html_editor statically joins web + bus + base; html_builder then joins base + html_editor + mail.
6. base_automation statically bridges base/digest/resource/mail and an out-of-roster dependency sms; this is a cross-group edge candidate, not yet a runtime claim.
7. digest bridges mail/portal/resource.
8. resource_mail bridges resource and mail.
9. google_recaptcha depends on setup; web_unsplash depends on setup + html editor.
10. Every row in this intake has LGPL-3 and no manifest parse error in the secondary register.

## A1 Next Extraction Targets

For each of the 23 modules, extract from current Community19 source when reachable:
- all model/entity declarations and inheritance/extension edges;
- key fields and identity/ownership semantics;
- state/lifecycle definitions;
- constraints/validations/defaults;
- groups/ACL/record rules;
- scheduled jobs/background mechanisms;
- controllers/routes and integration surfaces;
- actions/views/menus/buttons/field definitions as static surfaces;
- data/reference/migration/test artifacts;
- direct and reverse dependency edges;
- company/tenant-relevant static controls;
- contradictions and source gaps.

## Evidence Limitation

This intake establishes **membership + secondary manifest metadata**, not current-source byte-level completion. The historical/mixed-source register is not permitted to substitute for the authoritative Odoo Community 19.0.post20260921 source distribution. Therefore the present status is:

A1 INTAKE STARTED / CURRENT-SOURCE RE-ANCHOR PENDING

No A2, GMVQ answering, Formal Coverage, or Research-Complete claim is authorized.
