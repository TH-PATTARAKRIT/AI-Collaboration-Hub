# 19 — AI EXPERT ROLES OVERLAY REVIEW (4 ROLES)

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / L999.999` |
| Document status | `PROCESS REFERENCE ONLY` — challenge record; not a Gate PASS, not a Final Solution, not development/production authorization |
| Ai Audit structure | `Ai Audit SMEsPlus = 9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Roles Overlay` — three separate layers, kept in files 17 / 18 / 19 |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` `Open ERP / Odoo = Process Benchmark Only.` `SMEsPlus = New Thai Business Process Design Candidate, not final solution.`

## 0. Overlay rule

The four AI Expert roles (per the Reopen session package index: Leader Functional Design; Leadership Database Design; Lead Integration & Localization; Lead Code & UI Architect) **review and comment only**. They are an overlay on files 02–16 and on the Council/Special Team findings (17/18). **Overlay only — not a replacement for the 9 Veto Challenge Council or the 9 Special Team Challenge.** No role authorizes Team B, Team C, development or production.

## R1 — Leader Functional Design (Expert IBPV / Team B / UX / UAT lens)

- The menu-by-menu map (05) and handoff map (04) are usable as the **input skeleton** for a future Thai accounting functional design: stage order, per-menu input/action/output, and Thai candidate vocabulary are now in one place.
- Functional-flow risks to carry forward, not resolve here: (1) consumption triggers for Thai document classes are not enumerated (05 objection 5) — every correction/reversal flow depends on them; (2) approval-before-posting is assumed in the close checklist but exists only as STATE04 draft ACC-004 (14 OBJN-07); (3) "Consumable — quantity-aware" sub-state (08 SC-16) has no benchmark precedent and would need original design; (4) receipt-time tax point for services (11/10) cannot be designed until VAT research exists.
- UX observation: the benchmark's own Thai labels are unfit; the naming register (15) must go to TBRAC before any wireframe.
**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

## R2 — Leadership Database Design (Team A / Team B / migration-proof lens)

- The package deliberately proposes no schema; that is correct at this stage. Data-identity observations for the eventual design owner: (1) migration tie-out is specified only at G1/GL level; AR/AP/WHT/asset subledgers and the inventory value have no identity contract (18 ST-04); (2) the Thai template's `999999` placeholder and the designated-RE requirement (MG-C15) collide — a migration mapping decision; (3) system-generated lines (tax/term/rounding) must be distinguishable from user lines at migration (AU-08) or double counting follows; (4) the benchmark's `service + storable` 989-row anomaly (Inventory file 12) shows that classification integrity must be enforced at durable write, not by application defaults.
- Benchmark schema shapes (single overloaded document table, six lock fields, one-directional storable clamp) are recorded in 16 as negative examples only.
**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

## R3 — Lead Integration & Localization (Thai accounting-tax lens)

- WHT: the most evidenced Thai process; still `PARTIAL` with `ACC-WHT-06` HIGH. New instance fact (A2): the reference deployment ran without the multi-rate module — the Boss decision on module baseline is now better informed, not made.
- VAT: templates exist but contain a self-contradictory exempt-input mapping, no non-deductible input VAT, no Undue VAT process; CIT: nothing. A Thai localization design cannot start from these templates alone.
- Tax-group closing accounts netting purchase WHT liabilities against sales WHT assets (10 §2.2) is a concrete configuration error to avoid inheriting.
- Statutory forms present in the chart but absent from scope (PND1, PND54, PP36) need a Boss in/out ruling.
- Branch (สาขา) already appears as a statutory attribute on WHT output in the benchmark localization; treating it purely as a management dimension would be a localization error if per-branch VAT filing applies (13 UK-01, LEGAL_TAX_REVIEW_REQUIRED).
**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

## R4 — Lead Code & UI Architect (future implementation-impact lens; no Team C authorization)

- Forward-looking implementation risk flags only, for whenever Team C/D work is authorized (none is): (1) do not inherit suppressible balance validation, reset-to-draft after posting, context-sentinel lock bypass, opt-in hash, single-rate WHT tagging, duplicated PND report logic, hardcoded WHT condition, manual certificate issuance (16 negative-example list); (2) report engine behaviour is entirely black-box — any future reporting implementation must be specified from B07/B08/B09 principles and Thai statutory formats, not from benchmark screens; (3) the docker-based metadata extraction used for A1/A2 is a research technique, not a migration tool — no migration tooling is implied.
- UI: folder-level labels (Review, Control, Closing, Statement Reports) have candidate names only in 15 §4 and are not registered rows — a future UX pass must add them.
**Overlay only — not a replacement for 9 Veto Council or 9 Special Team Challenge.**

## Overlay consolidated note

All four roles concur with the Council position: the package is a **process reference** suitable for Boss review and for routing to legal-tax, TBRAC, Joint Session 3 and scope decisions; none of it moves a gate. **No role substitution occurred**: every Council seat (17) and Special Team (18) carries its own finding independent of this overlay.
