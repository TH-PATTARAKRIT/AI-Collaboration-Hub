# STEP0303R2 — BOSS TOOLCHAIN RULING RECORD

Prompt ID: SMEPLUS-26-08-24-STEP0303R2 | Date: 2026-08-24
Recorded by: Claude (Executor only — no approval, no selection, no development)
Approver: Boss (Sole Final Approver)

## RULINGS AS GIVEN BY THE BOSS

### R1 — Nine added toolchain domains from STEP0303R1
**Decision: ACCEPTED**
Recorded scope: domains **§2.8 – §2.15**, being Identity/Session/Cache, Background Jobs &
Scheduling, Document Numbering, Attachments & File Storage, Internationalisation,
Customer/Vendor/Partner Data Handling, Backup & DR, Observability.

> **RECORDING NOTE — COUNT DISCREPANCY.** The ruling text says "nine added domains".
> The matrix contains **eight** newly added domains (§2.8–§2.15). The figure "nine"
> originated in my own STEP0303R1 wording and was quoted into the ruling; the error is mine.
> §2.16 (frontend) and §2.17 (hosting) were *returned exclusions*, not new domains, and are
> DEFERRED under R4 — so they cannot be the ninth. Recorded as **eight domains**.
> Logged as OPEN-08 / PMO-09 for Boss confirmation. No item was added or dropped.

### R2 — Customer / Vendor / Partner data handling guardrail
**Decision: ACCEPTED AS DATA_HANDLING_GUARDRAIL_ONLY**
Recorded exactly as ruled:
- PDPA Deep Research **is not to be opened**
- PDPA **is not a blocker**
- Treated only as a data handling / no-raw-personal-data-export guardrail
- Research focus remains Customer / Vendor / Partner **data structure and business behaviour**

> The STEP0303R1 recommendation to place PDPA in the architecture baseline is **superseded**
> by this ruling and reclassified DATA_HANDLING_GUARDRAIL_ONLY. Governance Rules 9 and 10 apply.

### R3 — Per-field JSONB i18n direction
**Decision: ACCEPTED AS ARCHITECTURE_DIRECTION**

### R4 — Frontend / Hosting
**Decision: DEFERRED** — not required to close the STATE03 backend/toolchain baseline.
No cloud vendor and no frontend stack selected.

### R5 — Gap-free statutory sequence requirement
**Decision: OPEN_PENDING_RD_CONFIRMATION** — requires external RD/legal/statutory
confirmation. Not to be assumed.

### R6 — Still-open freeze items
**Decision: CARRY_FORWARD_OPEN_ITEMS** — carried forward without solving:
S1 Thai statutory reporting · duplicate DB artefact · generic WHT engine ruling ·
8 residual localization modules · payroll WHT scope.

## WHAT WAS *NOT* RULED
**STEP0303 §2.1 – §2.7 has no Boss ruling.** The STEP0303 review sheet (its own R1–R6) was
never answered. Those seven domains — persistence, authorisation, workflow, audit/eventing,
document rendering, integration boundaries, development toolchain — carry the
highest-consequence decisions in the matrix and are recorded here as
**BOSS_DECISION_REQUIRED** (OPEN-01), not as approved.

Nothing has been marked APPROVED without an explicit Boss decision present.
