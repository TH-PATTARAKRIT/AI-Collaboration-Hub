# STATE04-READY TOOLCHAIN BASELINE

**Scope of this baseline: APPROVED ITEMS ONLY.** This is a planning baseline.
It is **not** development authorization.

## APPROVED — EIGHT PLATFORM DOMAINS (Boss ruling R1, R2, R3)
| ID | Domain | Approved direction | Classification |
|---|---|---|---|
| TC-08 | Identity, Session & Cache | External shared session store; tenant resolved before authorisation; TOTP second factor | EVIDENCE_CONFIRMED |
| TC-09 | Background Jobs & Scheduling | Persistent tenant-aware job table with failure tracking; jobs run as a user in a tenant, never unscoped | EVIDENCE_CONFIRMED |
| TC-10 | Document Numbering | Configurable prefix/suffix/padding/increment per company, with date-range scoping | EVIDENCE_CONFIRMED |
| TC-11 | Attachments & File Storage | Object storage by reference with DB-blob fallback; per-attachment access token; content indexing; auto-delete lifecycle | EVIDENCE_CONFIRMED |
| TC-12 | Internationalisation | Per-field JSON keyed by language, stored inline on the row; per-language locale data; Thai + English first-class | EVIDENCE_CONFIRMED (R3: ARCHITECTURE_DIRECTION) |
| TC-13 | Customer/Vendor/Partner Data Handling | Guardrail only — no raw personal data export; aggregates not personal records | DATA_HANDLING_GUARDRAIL_ONLY |
| TC-14 | Backup & Disaster Recovery | Multiple configurable destinations; restores exercised, not assumed | EVIDENCE_CONFIRMED |
| TC-15 | Observability | Structured logs with tenant/user/request correlation; statutory job failure alerts a human | JUDGMENT_RECOMMENDED |

## NOT IN THIS BASELINE — CORE DOMAINS REMAIN UNRULED
The following are **BOSS_DECISION_REQUIRED** and must not be treated as settled:
persistence (incl. database vendor and money representation) · authorisation model ·
workflow/approval service · audit & eventing · document rendering · integration boundaries ·
development toolchain (language, API style, testing, CI).

## COVERAGE AGAINST THE FROZEN BASELINE
| Coverage | Frozen findings |
|---|---|
| Partially covered by approved items | S3, S5, S7, S10 |
| **No approved coverage** | S2, S4, S6, S8, S9, S11, and S1 (open dependency) |

**Read this plainly:** the approved baseline supports platform services. It does **not**
yet support the core accounting, authorisation and rendering decisions that most of the
frozen findings depend on.

## DEFERRED (R4)
Frontend stack · hosting topology and region · cloud vendor.

## OPEN (R5, R6)
Gap-free statutory sequence (pending RD confirmation) · S1 Thai statutory reporting ·
duplicate DB artefact · generic WHT engine · 8 residual localization modules · payroll WHT scope.

## STATUS
Planning baseline only. No development, coding, deployment or merge is authorized.
Boss remains the sole Final Approver.
