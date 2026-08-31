# STEP0303R1 — TOOLCHAIN MATRIX COMPLETION (§2.8 – §2.17)

Prompt: SMEPLUS-26-08-24-STEP0303R1 | Date: 2026-08-24
Completes STEP0303. Same honesty rule: **[E]** evidence-derived, **[J]** engineering judgment.
Status: **RECOMMENDATIONS ONLY. No development authorised. Boss is sole approver.**

## WHAT WAS INCOMPLETE
STEP0303 covered persistence, authorisation, workflow, audit, rendering, integration and
dev toolchain (§2.1–§2.7), and explicitly excluded three areas. This completion adds nine
platform domains that were absent altogether, and returns to the three exclusions.

---

### 2.8 IDENTITY, SESSION & CACHE
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Session store | **External shared store (Redis or equivalent), not in-process** | **[E]** | `wk_redis_session` exists in the approved scope precisely to move sessions out of the app — declares `redis`. A multi-node SaaS cannot hold sessions in memory. |
| Tenant resolution | Resolve tenant on every request before authorisation runs | **[E]** | S5/S7 — RLS and policy evaluation both need tenant context established first. |
| Authentication | Own credential store + TOTP; SSO via OIDC later | **[J]** | Reference scope contained `auth_totp_mail`; second-factor is expected, the protocol choice is judgment. |

### 2.9 BACKGROUND JOBS & SCHEDULING
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Scheduler | **Persistent, tenant-aware job table with failure tracking** — not in-process timers | **[E]** | `ir_cron` carries `interval_number`, `interval_type`, `nextcall`, `lastcall`, **`failure_count`**, **`first_failure_date`**, `priority`, `user_id`. The reference platform tracks *repeated failure*, not just schedule. |
| Design rule | Jobs run **as a user in a tenant**, never as an unscoped superuser | **[E]** | `ir_cron.user_id` + S5 RLS. An unscoped job is the classic multi-tenant data leak. |

### 2.10 DOCUMENT NUMBERING
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Sequence service | **Configurable prefix / suffix / padding / increment, per company, with date-range scoping** | **[E]** | `ir_sequence` columns: `prefix`, `suffix`, `padding`, `number_next`, `number_increment`, `company_id`, **`use_date_range`**. Boss Extra adds `conf.prefix` (`equipment_sequence`) and `product_sequence`, `order_line_sequence`, `contact_reference_sequence` — numbering is heavily customised in practice. |
| Thai note | Date-range scoping matters: Thai documents are commonly numbered per fiscal year | **[E]** | `use_date_range` + S5 period scoping. |
| Gap-free requirement | Statutory documents (tax invoice, WHT cert) need **gap-free** sequences | **[J]** | Not directly evidenced in the dump, but a standard Thai Revenue Department expectation — flag for confirmation, do not assume. |

### 2.11 ATTACHMENTS & FILE STORAGE
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Storage strategy | **Object storage by reference, with DB-blob fallback** | **[E]** | `ir_attachment` has BOTH `store_fname` (filesystem/object) and `db_datas bytea` (in-DB) — the reference supports either. Also `file_size`, `mimetype`, `checksum`-style dedup fields. |
| Access control | Per-attachment `access_token` + `public` flag, scoped to tenant | **[E]** | `ir_attachment.access_token`, `.public`, `.company_id`. |
| Content indexing | Extracted text kept for search | **[E]** | `ir_attachment.index_content`. |
| Lifecycle | Auto-delete flag for transient files | **[E]** | `ir_attachment.auto_delete`. |
| Thai note | Statutory attachments include the WHT certificate **signature image** | **[E]** | `withholding.tax.cert.signature` (Binary) in source. |

### 2.12 INTERNATIONALISATION — EVIDENCE CHANGES THE DEFAULT ANSWER
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Translatable field storage | **Per-field JSON keyed by language code, stored inline on the row** — NOT a side translation table | **[E]** | **503 jsonb columns** in the dump; the Thai PND query reads `jsonb_extract_path_text(rcp1.name, 'en_US')`. Concentrated on `res_partner` (31), `product_template` (27), `res_company` (9). |
| Locale data | Per-language `date_format`, `time_format`, `decimal_point`, `thousands_sep`, `grouping`, `week_start`, `direction` | **[E]** | `res_lang` columns. |
| Language set | Thai + English as first-class pair | **[E]** | Thai/English name pairs in `l10n_th_partner`; `en_US` key in the PND query. |

> This row is the clearest case in the whole matrix where evidence overrides the conventional
> answer. The default instinct is a separate translations table; the reference system —
> and the Thai statutory query that reads it — uses inline per-field JSON.

### 2.13 PERSONAL DATA & PDPA — MISSING FROM STEP0303, AND IT SHOULD NOT HAVE BEEN
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Scope of the problem | **292 candidate personal/financial columns across 126 tables** | **[E]** | Column inventory scan: `hr_employee` (18), `res_company` (16), `hr_version` (13), `account_move` (12), `account_move_line` (10), `hr_applicant` (10), `crm_lead` (8), `res_partner` (8). |
| Architecture consequence | PDPA is **cross-cutting**, not a module. Classify columns at the schema level, and carry the classification into audit, export and erasure. | **[E]** | The spread across 126 tables makes a bolt-on approach unworkable. |
| Data subject rights | Export and erasure must be **first-class services**, tenant-scoped | **[J]** | Thailand's PDPA grants access/erasure rights; the reference had `om_data_remove` (data cleanup), but nothing purpose-built for subject rights. |
| Encryption | At rest and in transit; field-level for tax IDs and bank details | **[J]** | Prudent, not evidenced. |
| Operational rule already applied | Restores of production data must extract **aggregates, not personal records** | **[E]** | The control set applied at STEP040304R3B/R3C. |

> This is a genuine omission from STEP0303, not a deferred item. A Thai SaaS handling 292
> personal-data columns needs PDPA in the architecture baseline, and I should have raised it
> in the first pass.

### 2.14 BACKUP & DISASTER RECOVERY
| Concern | Recommendation | Basis | Evidence |
|---|---|---|---|
| Backup targets | Multiple destinations, configurable per deployment | **[E]** | `auto_database_backup` declares `dropbox`, `boto3` (S3), `paramiko` (SFTP) and defines a 56-field `db.backup.configure` model. |
| Restore testing | Restores must be **exercised**, not assumed | **[E]** | Hard-won on this project: the dump proved to be a configuration database with 6 journal entries and zero WHT certificates. An untested backup is an unverified assumption. |
| Tenant granularity | Per-tenant restore, not only whole-cluster | **[J]** | Follows from multi-tenancy; not evidenced. |

### 2.15 OBSERVABILITY
| Concern | Recommendation | Basis |
|---|---|---|
| Structured logs with tenant + user + request correlation | **[J]** | Convention; tenant tagging follows from S5. |
| Metrics and tracing | **[J]** | Convention. |
| Statutory job alerting — failed filings must page a human | **[E]** | `ir_cron.failure_count` / `first_failure_date` show the reference tracked repeated failure; a failed statutory job has a legal deadline attached. |

### 2.16 FRONTEND STACK — PREVIOUSLY EXCLUDED, NOW OFFERED AS JUDGMENT
STEP0303 excluded this for lack of evidence. That remains true: **nothing in the frozen
baseline constrains the frontend.** Offered so the matrix is complete, clearly marked:
| Concern | Recommendation | Basis |
|---|---|---|
| Framework | React or Vue with TypeScript — team familiarity should decide, not this matrix | **[J]** |
| Rendering | SPA against the REST/command API | **[J]** |
| Thai typography | Thai-capable webfont, and **test line-breaking in the UI, not only in PDF** | **[E]** | annex T3 — Thai has no inter-word spaces; the browser handles it, but the font must cover Thai glyphs and marks. |
| Data grids | Must support Thai collation ordering and B.E. date display | **[E]** | annex T1/T9. |

### 2.17 HOSTING & DEPLOYMENT — PREVIOUSLY EXCLUDED, NOW OFFERED AS JUDGMENT
| Concern | Recommendation | Basis |
|---|---|---|
| Region | **Thailand or nearest region** — PDPA and latency both point the same way | **[J]** with a PDPA rationale (§2.13) |
| Topology | Containerised app tier, managed PostgreSQL, object storage, managed Redis | **[J]** |
| Cloud vendor | Not recommended here — no evidence, and it is a commercial decision | — |

---

## 3. COMPLETION STATEMENT
The matrix now covers seventeen domains. Coverage of the **frozen baseline S2–S11 is
complete**: every frozen finding has at least one corresponding toolchain row.

| Still not decided | Why |
|---|---|
| Thai statutory report definitions | **S1 open.** Blocked until route (a) or (b) supplies the specification. |
| Cloud vendor | Commercial decision, no technical evidence to offer. |
| Gap-free sequence requirement | Flagged [J] — needs confirmation against Thai Revenue Department rules. |
