# STEP0303R3 — CORE TOOLCHAIN RULING RECORD (STEP0303 §2.1–§2.7)

Prompt ID: SMEPLUS-26-08-24-STEP0303R3 | Date: 2026-08-24
Recorded by: Claude (Executor only) | Approver: Boss (Sole Final Approver)
Purpose: close the seven core toolchain domains flagged unruled by STEP0303R2 (A1 / OPEN-01).

## RULINGS AS GIVEN

| Ruling | Domain | Decision |
|---|---|---|
| R1 | §2.1 Persistence / Database | ACCEPTED AS PLANNING_BASELINE |
| R2 | §2.2 Authorisation / RBAC | ACCEPTED AS PLANNING_BASELINE |
| R3 | §2.3 Workflow / Approval | ACCEPTED AS PLANNING_BASELINE |
| R4 | §2.4 Audit / Event / Evidence | ACCEPTED AS PLANNING_BASELINE |
| R5 | §2.5 Rendering / Document Output | ACCEPTED AS PLANNING_BASELINE |
| R6 | §2.6 Integration | ACCEPTED AS PLANNING_BASELINE |
| R7 | §2.7 Development Toolchain | ACCEPTED AS PLANNING_BASELINE |

STEP0303R2 open gate A1 / OPEN-01 is hereby **CLOSED**.

## RECORDING NOTES — WHERE I APPLIED THE RULINGS' OWN CONDITIONS

### N1 — R1 database direction, recorded within its condition
R1 permits a database direction "only as planning baseline **if supported by STEP0303
evidence**". Recorded as **CT-02: a relational, transactional datastore direction
(PostgreSQL-class)** — direction only. No vendor lock, no version, no schema, no project
init. The supporting evidence is the reference evidence base (1,395 tables, 6,682
constraints, 5,141 FK edges) plus S2/S9 requiring transactional exactness on the journal.

### N2 — R5 rendering engine deliberately NOT selected
R5 permits selecting a final rendering library "unless evidence already supports it".
The evidence supports the **requirement** — Thai text shaping and line-breaking, print
layout as configuration, XLSX as a statutory output — but it does **not** name an engine.
Recorded as **CT-15: specific rendering engine NOT selected**, classification
JUDGMENT_RECOMMENDED, tracked as OPEN-R3-09. The STEP0303 recommendation of headless
Chromium remains a recommendation, not a selection.

### N3 — R7 named tooling is Boss-directed, not evidence-derived
The eleven named tools in R7 (GitHub, Jira, Claude Code, ChatGPT/Archimedes, Codex,
Playwright, Selenium, Figma, Google Drive, Make, Proxmox/ReadyIDC) are recorded as
**BOSS_APPROVED_PLANNING_BASELINE**. None of them trace to the 134-module evidence base,
and none is marked EVIDENCE_CONFIRMED. They are organisational and process decisions, which
are the Boss's to make — the classification simply records that basis accurately.

### N4 — R7 infrastructure vs the STEP0303R2 R4 deferral
STEP0303R2 R4 DEFERRED frontend and hosting. R7 now sets **Proxmox / ReadyIDC as
infrastructure direction until further freeze**. Recorded as a **partial supersession**, not
a conflict: infrastructure direction is now set; **cloud vendor and frontend stack remain
deferred and unselected** (OPEN-R3-08). Tracked for reconciliation as PMO-R3-10.

### N5 — R6 Make pathway vs no vendor lock-in
R6 requires support for a "Make / API / external automation pathway" while forbidding
vendor-specific lock-in. Recorded as adapter-based integration (CT-17) in which Make is a
**supported pathway, not an embedded dependency** (CT-18). The two requirements are
consistent under that reading.

### N6 — R3 refines S8 and S9
The responsibility split — Approval Engine approves only, Source Module executes, Posting
Engine posts, events are immutable facts — is a Boss-directed refinement that sharpens
frozen findings S8 and S9. It does not modify S2–S11; it elaborates how they will be met.

## WHAT WAS NOT DONE
No development, no repository, no schema, no project files, no framework or version
selection beyond what is recorded above. S1 not closed. Frozen findings S2–S11 unmodified.
PDPA deep research not opened. 134-module research not reopened. No proprietary source read.
