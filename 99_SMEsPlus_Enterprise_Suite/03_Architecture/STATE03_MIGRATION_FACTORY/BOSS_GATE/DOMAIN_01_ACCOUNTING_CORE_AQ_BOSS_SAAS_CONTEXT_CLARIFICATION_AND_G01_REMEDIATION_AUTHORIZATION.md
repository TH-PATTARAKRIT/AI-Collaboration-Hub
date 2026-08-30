# DOMAIN_01 Accounting Core — AQ — Boss SaaS Context Clarification & COA-G01 Remediation Authorization

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Record Boss-approved SaaS Context clarification and authorize a controlled COA-G01 remediation pass | Claude (session SMEPLUS-26-08-30-COA-G01R-001), drafted from PMO/ChatGPT-issued session prompt | This artifact; Jira `ERPPLUS-132`; GitHub `SMEsPlus` branch | 2026-08-30 22:27 +0700 | Boss (final authority, decision pending); ChatGPT / PMO Secretary (drafting review, prior) | RECORDED / BOSS DECISION PENDING ON DOWNSTREAM GATE USE | Clarifies SI-01/SI-03 operational boundary for COA-G01 only; does not itself close any Gate |

## 1. Naming and Sequencing Note

The controlling session prompt recommended suffix `AR` for this ruling. Direct inspection of the `SMEsPlus` branch shows the DOMAIN_01 Accounting Core lettered-evidence sequence (spanning `BOSS_GATE/`, `CHATGPT_AUDIT/`, and `PMO_VERIFICATION/`) runs continuously `AD, AE, AF, AG, AH, AH, AI, AJ, AK, AL, AM, AN, AO, AP` with no gap before `AP` (the `AH` duplication is pre-existing project history, not introduced here). The true next-unused letter in that continuous sequence is **`AQ`**, not `AR`. To avoid creating an unexplained gap in the project's own lettering convention, this ruling uses **`AQ`** instead of the suggested `AR`. This deviation is recorded here for transparency and is subject to Boss correction if a different convention was intended.

## 2. Authority Chain Verified Before Drafting

The following were independently verified against the live `SMEsPlus` branch and Jira before this artifact was drafted (not merely assumed from the session prompt):

- Commit `e8cc4d942d7f5c611ca3add0266c39196515b636` — "governance(state03): authorize Thailand COA architecture closure and Boss freeze" — VERIFIED, exists on branch.
- Commit `c084a741b22e3352992fbeb0c212cbd1463efb92` — "governance(state03): add mandatory COA SaaS architecture gate" — VERIFIED.
- Commit `e16b29f35d8011723a6e2593994bc226870d9fd7` — "governance(state03): enforce cross-gate SaaS invariants for Thailand COA closure" — VERIFIED.
- Commit `79719e6866b6f9277ef8f8d99f42be1ffbdc01da` — "docs(state03): apply SaaS invariants to every COA closure gate" — VERIFIED.
- Commit `5c8cf97796223ec798096c5fc3014eb88ae4f608` — "docs(state03): publish COA closure carry-forward v3 with cross-gate SaaS invariants" — VERIFIED.
- Jira `ERPPLUS-132` — VERIFIED live; current Gate field reads `COA-G01 — Source Baseline Reconciliation = OPEN / AUTHORIZED`; comments `10898`–`10903` all present and match the governance record cited by the session prompt.

## 3. Boss-Approved SaaS Context Clarification (recorded verbatim as a controlled ruling)

This clarification is **recorded** by this session as instructed. It has not previously appeared in any `BOSS_GATE` artifact on this branch and is therefore new control content, not a restatement of an existing ruling:

1. Platform Template administration = **Platform Context**.
2. Tenant-owned or tenant-access operation = **Tenant Context mandatory**.
3. Company-scoped operation = **Tenant Context + Company Context mandatory**.
4. A Platform operation must not impersonate a Tenant operation.
5. A Tenant or Company operation must not access or mutate Platform-owned Published Standard Template data.

This resolves the operational boundary between **SI-01** (Tenant context is mandatory) and **SI-03** (Standard Template is not tenant-owned mutable data): SI-01 governs the tenant/company axis of every tenant-facing operation; SI-03 governs a separate, orthogonal Platform axis that a tenant/company operation must never cross into. Both invariants can hold simultaneously without contradiction once "Platform Context" is recognized as a third, distinct context alongside Tenant and Company.

**Status of this clarification: RECORDED AS CONTROLLED RULING. It is a boundary/definition control, not itself execution proof.** Per the Gate-appropriate evidence boundary (see `COA_G01_GATE_REPORT.md`), COA-G01 uses this clarification to classify source-baseline assumptions; production enforcement of the boundary remains the responsibility of `COA-G04S` and is NOT claimed as complete by this artifact.

## 4. Relevant local evidence informing SI-01/SI-02 application (not previously ported to GitHub)

Independent-session investigation of the local project working folder (`SMEsPlus ENTERPRISE SUITE/ACCOUNT`, outside this GitHub repo) surfaced a frozen local architecture finding directly relevant to how SI-01/SI-02 must be applied to the Thai source baseline:

> **Finding S5** (local `STATE03` architecture findings, frozen 2026-08-23): a two-level Tenant → Company model is **insufficient** for Thai statutory filing. The correct model is **Tenant → Legal Entity (Company) → Tax Branch**, because Thai Revenue Department filings (WHT certificates, VAT reporting) are addressed at the tax-branch level, not merely the company level.

This finding is **VERIFIED FACT at the local evidence layer** (file:line cited against Thai localization module structure) but has **not yet been committed to the `SMEsPlus` GitHub branch** — it exists only in the local filesystem. This is registered as a source-baseline evidence gap in `COA_G01_SOURCE_CONFLICT_REGISTER.md` and must inform Company Context modeling at `COA-G04S`; it is noted here, not adopted as a new Boss ruling, since only the Boss may rule on target architecture.

## 5. Authorization Scope (unchanged from session prompt)

This ruling authorizes a controlled COA-G01 remediation pass only. It does **not** close COA-G01 and does **not** authorize COA-G02 or any later Gate. Development Authorization = NOT GRANTED. Production Authorization = NOT GRANTED.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
