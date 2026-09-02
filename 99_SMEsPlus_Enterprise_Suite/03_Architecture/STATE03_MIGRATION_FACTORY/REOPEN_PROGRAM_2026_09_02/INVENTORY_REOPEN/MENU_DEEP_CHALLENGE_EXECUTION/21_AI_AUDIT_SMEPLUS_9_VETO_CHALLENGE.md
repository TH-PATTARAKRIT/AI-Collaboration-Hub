# 21 — AI Audit SMEsPlus: 9 Veto Challenge Council

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-09 OUTPUT — 9 VETO COUNCIL CHALLENGE OF THE MENU REFERENCE PACKAGE — NOT A GATE DECISION`
Charter: `SMEPLUS-GOV-9VETO-001` v1.0. Rule: most conservative unresolved material verdict controls the package. No majority vote. Boss = Sole Final Approver.

Independence disclosure (per CORR-007B file 14 precedent and reopen `U-05`): the nine tracks below were produced by one executing session applying nine mandates in sequence over the package it authored. They are not nine independent parties. They are an honest self-challenge against the Charter's nine boundaries and must not be cited as external verification. The reopen package's own nine-track findings (`170af9ea`, deliverables `03`–`11`) were loaded as prior challenge state; duplicate questions are suppressed and only delta questions are raised.

Delta pack challenged: 29 new files; new intent = menu-level process reference + Thai naming + 4-role overlay; new evidence = CORR-007B remediation record; no Boss Gate decision on the reopen package found.

---

## Track 01 — Audit VETO / Evidence & Governance

| Item | Challenge | Finding | Verdict input |
|---|---|---|---|
| A01-1 | Is the evidence chain for this package traceable? | Yes: base commit `7884795`, reopen `170af9ea`, remediation `9996072a` verified as objects; branch isolation verified; all 29 files present. | — |
| A01-2 | Did the session skip any Gate? | No Gate exists to skip; the package declares no PASS. The reopen package still has no written Boss Gate decision (recurrence of the reopen's Tier 0 item 0.5). | Note |
| A01-3 | Are prior questions re-asked without delta? | No: 14 carry-forward groups suppressed (01 §2.1). Menu-depth reopen is justified by Boss intent delta. | — |
| A01-4 | Is the screenshot evidence chain adequate? | Image files absent from repo; transcription in prompt is evidence of record. Archive gap. | `HOLD` sub-item |
| A01-5 | Are owners/verifiers real? | Owners are challenge tracks, not execution teams; every Verifier is `UNVERIFIED`. Honest but means no independent verification exists. | Note |
| A01-6 | Are the 9+9+4 layers independent? | No (disclosure above). Same structural limitation as `U-05`. | Note |
| A01-7 | Global Challenge Ledger still lacks `INV-FP` rows; this session adds none to canonical (read-only) | Governance hygiene item persists. | Note |

**Track 01 verdict: `CONTINUE_WITH_NOTES`** — package is traceable and honestly labelled; conditions: archive screenshots; record that no independent verification exists; ledger population remains outstanding.

## Track 02 — TBRAC / Thailand Business Reality & User Fitness

| Item | Challenge | Finding |
|---|---|---|
| A02-1 | Are the Thai candidate names validated by real Thai users? | **No.** Every label is `UNVALIDATED`. The structural real-user gap from 2026-08-30 is unchanged; TBRAC named membership still unassigned. |
| A02-2 | Does the Transfers split (รับเข้า/จ่ายออก/โอนย้าย) reflect Thai practice? | Plausible from common Thai warehouse vocabulary, but asserted by the executor, not evidenced. |
| A02-3 | Are statutory claims (stock report, scrap destruction, import VAT/duty, costing norm) evidenced? | No — all marked `HOLD / EVIDENCE REQUIRED` and routed to Accounting-Tax. Correct handling. |
| A02-4 | Industry conditionality (food/pharma expiry, consignment, dropship, service+parts) | Named as conditions; edge cases still untested (`N-A5-02/03`, `INV-FP-13` edge cases). |
| A02-5 | Is SME simplicity preserved? | Tiered configuration (T0/T1/T2) and hiding rules/scheduler are consistent with SME fitness; unvalidated. |

**Track 02 verdict: `HOLD`** — no real Thai user input exists for any menu name, flow, or control; the package may inform design but cannot be treated as Thai-fit.

## Track 03 — IBPV / Business Process & Design Integrity

| Item | Challenge | Finding |
|---|---|---|
| A03-1 | Is every menu mapped end-to-end with exceptions? | 29/29 mapped; exception grammar defined (14 §6); over-receipt tolerance and partial representation remain open design briefs (`GAP-MD-06/07`). |
| A03-2 | Ownership boundary | Consistent with reopen: Inventory owns stock truth; Joint items not closed. Untestable until a target schema exists (unchanged). |
| A03-3 | Count/adjust approval flow | Candidate flow adds approval and reason; freeze policy still unselected (`N-A7-01`). |
| A03-4 | Cancellation cascade `C-01` | Still conflicting; package does not resolve it. |
| A03-5 | Scrap vs damaged-goods hold | Candidate hold state proposed; `U-02` remains unknown. |

**Track 03 verdict: `HOLD`** — process reference is complete at menu level, but the same design briefs the reopen demanded (over-receipt, partial, freeze policy) still do not exist and this session may not author them.

## Track 04 — IDTM / Data, Identity, Reconciliation & Integrity

| Item | Challenge | Finding |
|---|---|---|
| A04-1 | Are identities and migration keys stated for every object? | 36 objects with candidate identities (03); provenance map must be originated (`GAP-MD-27`). |
| A04-2 | Reconciliation identities | REC-01..10 candidate formulas (18 §2); `G-5` cross-proof Joint. |
| A04-3 | Idempotency `C-02` | Unresolved; package makes it a candidate invariant (INV-06) but severity is Boss's. |
| A04-4 | Variants, packagings, barcodes | No evidence — held. |
| A04-5 | Product kind tie-break | Undecided (`GAP-MD-10`). |

**Track 04 verdict: `HOLD`** — identity and reconciliation requirements are now explicit, but none is evidenced against a target and the provenance layer does not exist.

## Track 05 — IESA / ERP & SaaS System Integrity

| Item | Challenge | Finding |
|---|---|---|
| A05-1 | Multi-warehouse / multi-company flows | Single-company flows mapped; cross-company transfer still untraced (`GAP-MD-20`). |
| A05-2 | Route/rule architecture | Transformed into templates; no vendor architecture carried. Idempotent resolution is a requirement, not proven. |
| A05-3 | SaaS invariants for Inventory | Still no Inventory-side invariant set (`U-03`); every matrix row is `Y` on SaaS impact with nothing to test against. |
| A05-4 | Settings/warehouse provisioning | `SAAS-04` transformed into "version, never regenerate" candidate; unverified. |

**Track 05 verdict: `HOLD / EVIDENCE REQUIRED`** — no target-side tenancy architecture exists; unchanged from reopen.

## Track 06 — Financial / Accounting / Tax / Statutory VETO

| Item | Challenge | Finding |
|---|---|---|
| A06-1 | Did Inventory close any Accounting item? | No. All valuation/close/policy items classified Joint or Account (15 §5, 04 §4). |
| A06-2 | Landed cost | Process mapped; mechanism completeness and Thai import treatment held. |
| A06-3 | Scrap deductibility, stock report format, costing norm | Held with authoritative-evidence requirement; not asserted. |
| A06-4 | COGS timing, return cost basis, late bill | Carried as Joint (`FIN-DELTA-03/04`, `C-03`). |
| A06-5 | `N-A12-01` | Unchanged `HIGH FUNCTIONAL DESIGN GAP — REOPENED`. |

**Track 06 verdict: `HOLD / EVIDENCE REQUIRED`** — boundary discipline is intact; substantive items remain blocked on `COA-G04..G08` and the Joint Session.

## Track 07 — Security / Privacy / Resilience VETO

| Item | Challenge | Finding |
|---|---|---|
| A07-1 | Permissions per menu | Candidate SoD matrix (11 §4, 19) — not evidence; warehouse-level axis unknown (`U-01`). |
| A07-2 | Destructive actions | Adjust/scrap/period-unlock identified with controls; benchmark weaknesses (`G-2`) not inherited by default. |
| A07-3 | Audit trail | Requirements stated per menu; not verified. |
| A07-4 | PDPA | Absent; newly flagged `GAP-MD-29`. |
| A07-5 | Concurrency `C-04` | Unresolved. |

**Track 07 verdict: `HOLD`** — control requirements are now itemised, which was the reopen's gap, but none is evidenced and Boss scope ruling on warehouse/operation-level authorization is still needed.

## Track 08 — Clean-Room / IP / Provenance VETO

| Item | Challenge | Finding |
|---|---|---|
| A08-1 | Was Layer 2 opened? | No (20 §3). |
| A08-2 | Did vendor vocabulary leak into the package? | Mechanical scan performed pre-publication (28 §5); residual tokens limited to project IDs and "what not to copy" labels. |
| A08-3 | Are Thai templates a transliteration? | No; they are business phrases. |
| A08-4 | `C-05` | Remediated surface used only (file `09` Layer 1); independent re-audit still not performed; preserved Boss-visible. |
| A08-5 | Does any statement say SMEsPlus must follow the benchmark? | None found; "must" statements are candidate requirements. |
| A08-6 | Default-by-absence risk | Still the dominant risk: without Thai user evidence the benchmark remains the only voice. Named in 20 §6. |

**Track 08 verdict: `CONTINUE_WITH_NOTES`** for this package's own content; **`HOLD` carried** for `C-05` until the independent re-audit exists. Controlling label for the track: `HOLD` (conservative).

## Track 09 — AI Control / Automation / Human Oversight VETO

| Item | Challenge | Finding |
|---|---|---|
| A09-1 | Did this session fabricate any stock fact, quantity or evidence? | No stock facts asserted; the only numeric data quoted (83,753 / 989 / 3,980 / 6.6%) are carried from reopen `12` with citation. |
| A09-2 | Scheduler and replenishment automation boundary | Deterministic-control requirement stated; AI limited to explain/flag (12 §4). |
| A09-3 | AI in migration | Requirements restated from reopen `11`; none designed. |
| A09-4 | Self-referential independence | Disclosed (header). |
| A09-5 | Were the extraction passes' outputs trusted blindly? | Extracts were reconciled against the executor's own full reads of deliverables `01`, `02`, `13`–`20` and CORR-007B `17`; IDs cross-checked. Residual risk: `03`–`12` were read fully only by the extraction passes. |

**Track 09 verdict: `CONTINUE_WITH_NOTES`** — no fabrication; deterministic boundaries stated; structural independence limitation disclosed.

---

## Convergence

| Track | Verdict |
|---|---|
| 01 Audit | `CONTINUE_WITH_NOTES` |
| 02 TBRAC | `HOLD` |
| 03 IBPV | `HOLD` |
| 04 IDTM | `HOLD` |
| 05 IESA | `HOLD / EVIDENCE REQUIRED` |
| 06 Financial | `HOLD / EVIDENCE REQUIRED` |
| 07 Security | `HOLD` |
| 08 Clean-Room | `HOLD` (carried `C-05`) / `CONTINUE_WITH_NOTES` (package content) |
| 09 AI Control | `CONTINUE_WITH_NOTES` |

**Controlling verdict: `HOLD / EVIDENCE REQUIRED`.** Nothing reaches `FAIL / FROZEN`. The package is publishable as a process reference; it is not evidence that Inventory is Thai-fit, design-ready, or Gate-ready.

Unresolved objections carried to 24: real-user validation (02); design briefs (03); provenance/idempotency (04); Inventory SaaS invariants (05); Joint/Account blockers (06); authorization scope ruling and PDPA (07); `C-05` re-audit (08); independence verification (01/09).

Required evidence before any Gate movement: listed in 24 §4 and 25 §6.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
