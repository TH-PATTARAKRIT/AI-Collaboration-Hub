# UNKNOWN_AND_EVIDENCE_GAP_REGISTER

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Rule | Unknown ≠ Fact. Zero progress credit for G-items until resolved. |

| ID | Question / Gap | Why important | Evidence searched | Missing | Risk | Owner | Next investigation | Status |
|---|---|---|---|---|---|---|---|---|
| Q-01 | Does the expanded Expert Deep Research directive extend the approved research scope beyond the 134-module register and/or into the 31 metadata-only / 19 black-box modules? | Governs what Team A may read at code level in A4 | STEP040303 scope + black-box registers, STEP040304R4 closeout, current directive | Explicit Boss scope ruling | Research either under-covers the system or violates a standing constraint | **Boss** | Boss decision at next gate | OPEN |
| Q-02 | Authoritative STEP binding for Migration Factory Team A | Progress % cannot be counted | STEP_BINDING_INVESTIGATION (MIG-A-001), STATE03 registers | STEP allocation by PMO/Boss | All progress stays TBD | **Boss/PMO** | Allocate existing or new STEP | OPEN (carry-forward) |
| Q-03 | Single authoritative factory location (`06 MIGRATION FACTORY` vs `03_Architecture/STATE03_MIGRATION_FACTORY`) | Evidence traceability & audit path | Both trees inspected | PMO confirmation | Fragmented evidence chain | PMO | Confirm + record decision | OPEN (B-01) |
| Q-04 | Module-count baseline advance 1,502 → 1,504 (ks modules) + classification of the 2 ks modules | Baseline integrity; prior registers stop at 1,502 | Fresh parse + all prior manifests reconciled | Authorized baseline update record | Delta re-flagged at every future gate | PMO | Record baseline v-next with delta evidence (this session's reconciliation file) | READY FOR DECISION |
| G-05 | Exact Odoo 19.0 patch level / commit of the source snapshot | Version pin for migration reproducibility | README/LICENSE/manifests; no release.py in addons-only bundle | odoo core (`odoo/odoo` bin) or deployment metadata | Ambiguity when comparing against upstream behavior | Team A | Ask customer for `odoo --version` / requirements or core tree; or infer from dump `ir_module_module` versions during DB phase | OPEN |
| G-06 | `l10n_th_withholding_tax_multi` depends on `account_payment_multi_deduction` — not present anywhere in tree | Module cannot install without it; WHT multi-deduction behavior unverifiable | find/grep across all 5 areas | The missing module (OCA `l10n-thailand` ecosystem) | Thai WHT capability partially unobservable | Team A → customer | Confirm with customer whether module existed in deployment; check dump `ir_module_module` rows in DB phase | OPEN |
| G-07 | Non-Odoo-named table `Products` (capitalized) visible in dump strings probe | Unknown data object; may be import/staging table with business data | Header strings probe only | Restored TOC / schema inspection | Unmapped customer data could be missed in migration | Team A | `pg_restore -l` TOC listing in controlled DB phase | OPEN |
| G-08 | Dump freshness: snapshot 2026-06-14 vs source state 2026-08-23+ | Migration profiling may not reflect current production reality | File dates, prior registers | Newer dump or customer confirmation this is the reference snapshot | Data-model drift between dump and live system | **Boss/customer** | Business decision: request fresher dump or freeze on iTEST02 | OPEN |
| G-09 | Rights/ownership confirmation for CLASS-D modules (10 customer-authored + 2 third-party) and OPL-1 purchased modules (licenses/receipts) | Clean-room + legal reuse boundary for migration deliverables | Manifests, MIG-A-001 delta register | Customer ownership statements / purchase records | IP exposure at handoff | **Boss/customer** | Collect ownership/purchase evidence | OPEN (carry-forward) |
| G-10 | Database deep observation not yet performed under this directive (object inventory, relationships, data profile, exceptions) | L9 proof layer for every domain | Prior R3A/R3B/R3C referenced | Controlled-restore session (Docker daemon currently down) | Domain findings stay source-only until proven against data | Team A (method) / PMO (authorization awareness) | Re-run R3C-style ephemeral no-network container; produce DATABASE_OBJECT_INVENTORY.md | PLANNED |
| G-11 | `hide_smesplus_menu` has no `__init__.py`; loadability unknown; `nthub_binary_field_preview` ships no active models | Understand whether these were actually active in production | Module tree read | Dump `ir_module_module.state` for these modules | Misclassification of active capability | Team A | Verify install-state in DB phase | OPEN |

## External research access

`EXTERNAL_RESEARCH_ACCESS = AVAILABLE (web tools present, not exercised this session)` —
multi-source triangulation (P1–P4) begins in Phase A6; no external citations were fabricated.
