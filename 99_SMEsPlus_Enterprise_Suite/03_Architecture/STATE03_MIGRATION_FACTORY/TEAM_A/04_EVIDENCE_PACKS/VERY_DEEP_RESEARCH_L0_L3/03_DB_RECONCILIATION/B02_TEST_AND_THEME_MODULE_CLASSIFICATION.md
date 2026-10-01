# B02 — Test-framework and Theme Module Classification (installed in the dump)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Static structural classification only (counts from the module manifests/extracts and configuration rows in the restored dump). These 65 modules are **not business functions**; they are classified, not L2/L3-studied. No V-level, coverage or completeness claim.

## 1. Facts
| Item | Observation | Class |
|---|---|---|
| Installed `test_*` framework modules | 35 of the 356 installed modules (all Community, LGPL-3). Source declares 392 models and 433 access rows for them; the dump holds 433 access rows owned by `test_*` modules | OBSERVATION |
| Their purpose | Fixtures for the platform's own automated tests (ORM, inheritance, import/export, mail, HTTP, website, resource, translation, search panels, assets bundle, access rights, uninstall behaviour, linting) | INFERENCE from module names/manifests |
| Scheduled jobs / automations owned by them | 0 | OBSERVATION |
| Public web routes | `test_website` declares 37 controller routes; whether each is public or authenticated was **not traced** | UNKNOWN — study if the website module family is scoped (see U19) |
| `theme_*` modules | 30 installed, each declaring one model-level extension and no routes; they contribute website view/asset/page records (database holds none of type "ui view" owned by themes under their own namespace, theme-owned asset records are present — see B01 §2.1) | OBSERVATION |
| Business-process relevance | None of the O2C/P2P/accounting/stock chains depends on these modules | INFERENCE (reverse-dependency check on the extracts) |

## 2. Risk / hygiene notes (neutral)
1. A production-style database that has test-framework modules installed carries extra data models, access entries and (for the website test module) routes that serve no business purpose; whether this is intended for the test dump or would be reproduced in a target system is a decision for the owners of the target design. **RISK — configuration hygiene.**
2. Because they are installed, their access rows are counted inside the database totals (e.g. the 2,010 access-control entries); counts used for target-design sizing should separate business and test modules. **OBSERVATION.**
3. Behaviour of these modules at runtime was not exercised (**RUNTIME/AWT REQUIRED**), and nothing here is a statement about test results.

Per-module counts (models, routes, access rows, dependencies) are in the restricted local area; this note intentionally lists no vendor structure.
