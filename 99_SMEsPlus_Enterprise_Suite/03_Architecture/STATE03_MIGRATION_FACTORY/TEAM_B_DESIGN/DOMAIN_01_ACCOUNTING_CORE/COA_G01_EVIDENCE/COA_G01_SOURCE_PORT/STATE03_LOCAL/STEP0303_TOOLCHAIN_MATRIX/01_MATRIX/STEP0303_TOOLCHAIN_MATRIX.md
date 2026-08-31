# STEP0303 — TECHNOLOGY & DEVELOPMENT TOOLCHAIN ARCHITECTURE MATRIX

Prompt: SMEPLUS-26-08-24-STEP0303 | Date: 2026-08-24
Gate: STATE03 FROZEN (S2–S11 baseline, S1 open) | **No development authorised**
Status: **RECOMMENDATIONS ONLY — nothing selected. Boss is sole approver.**

## 0. METHOD AND HONESTY RULE
Every row is tagged for its basis:
- **[E]** EVIDENCE-DERIVED — traces to a frozen finding (S2–S11) or to observed evidence.
- **[J]** ENGINEERING JUDGMENT — a conventional choice, no project evidence behind it.

The distinction is stated because dressing convention up as evidence would corrupt the
baseline the freeze just established. Where a choice is [J], the Boss is choosing on my
judgment, not on proven need — and should weigh it accordingly.

## 1. FIXED INPUTS (not open for selection)
| Input | Source |
|---|---|
| Node.js backend core | Project identity, Boss-declared |
| Multi-tenant SaaS | Project identity, Boss-declared |
| Clean-room — no Odoo code reuse | Governance Rule 3 |
| Thailand-driven backend scope | STATE03 freeze scope statement |

## 2. THE MATRIX

### 2.1 PERSISTENCE
| Concern | Recommendation | Basis | Driven by | Trade-off |
|---|---|---|---|---|
| Primary datastore | **PostgreSQL** | **[E]** | S2, S9 — WHT is a payment-time posting event; the journal must be transactionally exact. Reference system's own evidence base is 1,395 PG tables with 6,682 constraints and 5,141 FK edges. | Operationally heavier than a managed document store; correct for double-entry. |
| Money representation | **NUMERIC/DECIMAL, never float** | **[E]** | Evidence shows `wht_amount` as `double precision` and WHT amounts computed as `rate * base / 100`. Float money in a statutory filing is a defect waiting to happen. | Slower arithmetic; irrelevant at ERP volumes. |
| Extensible journal attributes | **Typed core columns + JSONB extension column, promoted to typed columns when stable** | **[E]** | S9 — `account.move` was extended 10× and `account.move.line` 8× by customisation. Schema churn on the journal is the predicted failure mode. | JSONB weakens constraints; mitigate by promoting stabilised attributes. |
| Temporal reference data | **Effective-dated rows (valid_from / valid_to), never in-place update** | **[E]** | S4 — statutory reference data must be versioned with effective dates. WHT rates change by decree; a filing must reproduce the rates in force on its date. | Every read needs an as-of date; unavoidable for statutory correctness. |
| Multi-tenancy isolation | **Row-level with tenant_id on every table + PostgreSQL RLS, three-level key (tenant → legal entity → tax branch)** | **[E]** | S5 — Thai filings are produced per tax branch, so branch is part of the identity key, not an attribute. | Schema-per-tenant isolates harder but does not scale to SMB tenant counts; RLS must never be bypassed by a service account. |
| Migrations | **Versioned, forward-only, reviewed migration files** | **[J]** | — | Convention. |

### 2.2 AUTHORISATION — THE HIGHEST-RISK COMPONENT
| Concern | Recommendation | Basis | Driven by |
|---|---|---|---|
| Authorisation model | **Policy-as-data engine evaluated at request time; permissions are tenant-editable RECORDS, not code-declared roles** | **[E]** | S7 — the reference deployment built `dynamic.access.right` keyed by module OR model with menu-level detail, precisely because static groups could not express its rules. |
| Enforcement point | **Server-side, at the data-access layer, not in the UI** | **[E]** | S7 + evidence that access rules were menu-scoped in the reference system, i.e. UI-level — the failure mode to avoid. |
| Candidate approaches | Own policy tables + evaluator (recommended); Casbin; OPA/Rego | **[J]** | Own tables keep the model tenant-administrable and inspectable; OPA adds an external dependency and a second language for rules. |

> This is the single most consequential row in the matrix. S7 says retrofitting a
> tenant-administrable model onto a code-declared role system is a rewrite, not a change.

### 2.3 WORKFLOW / APPROVAL
| Concern | Recommendation | Basis | Driven by |
|---|---|---|---|
| Request lifecycle | **One approval-lifecycle service; document types plug in. States and transitions are data.** | **[E]** | S8 — the identical `_STATES` machine (draft / to_approve / approved / rejected) was copy-pasted across two request modules, while a third, unintegrated engine existed. |
| Implementation | Explicit state-machine table + transition guards | **[J]** | A library (XState etc.) is viable; a data-defined machine keeps transitions configurable per tenant, consistent with S7. |

### 2.4 AUDIT / EVENTING
| Concern | Recommendation | Basis | Driven by |
|---|---|---|---|
| Audit trail | **Append-only change log as a platform service, automatic on tracked fields — not per-feature code** | **[E]** | S10 — `tracking=True` on both SMEsPlus request state fields; the WHT certificate inherits mail thread/activity; a separate module adds a log-note history report. |
| Activity / notification | Platform service alongside audit | **[E]** | S10 |
| Transport | Postgres LISTEN/NOTIFY or an outbox table before introducing a broker | **[J]** | Avoid a message broker until a proven need; an outbox keeps delivery transactional with the posting. |

### 2.5 DOCUMENT RENDERING — HIGH THAI RISK
| Concern | Recommendation | Basis | Driven by |
|---|---|---|---|
| Layout model | **Templates + per-form coordinate configuration held as DATA** | **[E]** | S11 — `cheque.setting` carries **76 layout fields**; `ir.actions.report` extended 6× by customisation. |
| PDF engine | **Headless-Chromium HTML→PDF** (recommended) over a PDF-primitive library | **[E]** | Thai text shaping and line-breaking (§2.2 of the Thai annex) is solved by a browser text engine and is a project in itself in a primitive library. |
| Spreadsheet output | **XLSX writer required, not optional** | **[E]** | The Thai WHT report module declares `xlsxwriter` and `xlrd`, and ships an XLSX report — statutory output is spreadsheet, not only PDF. |

### 2.6 INTEGRATION BOUNDARIES
| Concern | Recommendation | Basis | Driven by |
|---|---|---|---|
| Payment gateway | **Backend payment service, independent of any storefront** | **[E]** | S6 — `payment_2c2p` (Thai gateway) depended on `website_sale` in the reference system; that coupling is a packaging artefact not to be inherited. |
| Thai RD VAT lookup | **External-service adapter with cache and offline fallback** | **[E]** | `bm_thai_rd_vat_company_search` is proprietary/black-box; its behaviour is only observable, so isolate it behind an adapter. |
| External sync | Adapter per integration; no direct coupling into the domain | **[J]** | Reference system had a Monday.com connector, Dropbox/S3/SFTP backup targets, and an OpenAI module — integration breadth is real. |

### 2.7 DEVELOPMENT TOOLCHAIN
| Concern | Recommendation | Basis | Note |
|---|---|---|---|
| Language | **TypeScript** on Node.js | **[J]** | Strong typing matters most on the journal and statutory models; recommended, not evidenced. |
| API style | REST for CRUD + explicit command endpoints for postings | **[J]** | A posting is a command, not a resource update; keep it explicit. |
| Testing | Unit + statutory **golden-file** tests for every Thai report | **[E]** | S1/S4 — statutory output correctness cannot be asserted by unit tests alone; a filing must be diffable against an approved specimen. |
| CI gates | Migration review, RLS test, statutory golden-file diff | **[E]** | Derived from S5 (RLS) and S4 (reference data). |
| Environments | dev / staging / prod, with tenant seeding | **[J]** | Convention. |

## 3. WHAT THIS MATRIX DOES NOT DECIDE
- **S1 is still open.** No reporting-engine choice can be finalised for Thai statutory output
  until the report specification exists (routes (a)/(b)). §2.5 recommends the rendering
  toolchain, NOT the report definitions.
- **No frontend stack** is proposed. Nothing in the frozen baseline constrains it, and
  inventing a UI decision here would breach "no new architecture decisions without evidence".
- **No hosting/cloud selection.** Same reason — no evidence in the frozen baseline.
- **No development is authorised.** This is selection input only.
