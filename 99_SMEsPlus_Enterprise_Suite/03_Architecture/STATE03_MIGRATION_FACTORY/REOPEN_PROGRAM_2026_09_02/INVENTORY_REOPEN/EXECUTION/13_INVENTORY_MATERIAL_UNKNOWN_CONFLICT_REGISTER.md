# Inventory Full Reopen — Material Unknown & Conflict Register

Session: `SMEPLUS-26-09-02-INV-REOPEN-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-06 OUTPUT — MATERIAL UNKNOWN EXHAUSTION REGISTER — NOT A GATE DECISION`

This register exists to prevent the exact failure Track 01 (Audit VETO) flagged in deliverable `03` §3.5: that DR-002's own named "Material Unknown Exhaustion" test was never formally re-run or formally superseded across five corrective rounds. This document is this reopen's explicit, current-dated answer to that test. **Material Unknown Exhaustion is not claimed here.** Nine items below are unresolved by design (genuine Council-vs-Special-Team divergence, preserved rather than arbitrated per the Charter), and several more are genuine unknowns no pass has yet closed. That is the honest state of the evidence, not a defect in this reopen's own execution.

---

## Tier 1 — Track-Level Verdict Conflicts (Council vs. Special Team disagree on the headline recommendation)

Per each deliverable's own reconciliation policy, a genuine verdict-label conflict is not arbitrated by this program on its own authority — it is marked `HOLD` (the more conservative label) and carried to Boss undisguised.

| Track | Council | Special Team | Reconciled | Deliverable |
|---|---|---|---|---|
| 07 — Security/Privacy/Resilience | `HOLD` | `CONTINUE_WITH_NOTES` | `HOLD` | `09` §2 |
| 08 — Clean-Room/IP/Provenance | `CONTINUE_WITH_NOTES` | `HOLD` | `HOLD` | `10` §2 |
| 09 — AI Control/Automation | `HOLD` | `CONTINUE_WITH_NOTES` | `HOLD` | `11` §2 |

In all three cases, per-item cross-checking found **no factual contradiction** underlying the label split — both bodies converge on nearly every specific claim examined (Tracks 07 and 09's own convergence documents run this check explicitly, "Level 1 / Level 2" style, before reconciling). The label gap in Tracks 07 and 09 is a difference in how much named, bounded, checklist-relevant residual risk a VETO track should tolerate before recommending `HOLD` versus `CONTINUE_WITH_NOTES` — a threshold judgment, not a dispute over evidence. **Track 08 is different and more serious**: see Tier 2, item C-04, below — its verdict conflict traces directly to an unresolved item-level conflict over actual document content, not only threshold judgment.

---

## Tier 2 — Item-Level Conflicts (same fact examined by both bodies, different conclusion)

### C-01 — Cancellation-cascade symmetry (`MOV-31`) — Track 03 (IBPV)
**The shared fact:** the Purchase-side post-confirmation cancellation-cascade symmetry claim rests entirely on a finding imported from GROUP_A's CORR-003 work, never independently re-traced within Inventory Core Backbone by either body this round.
**Council:** `PARTIALLY VERIFIED` — downgrades the item given GROUP_A's 2026-09-02 organizational split from Inventory and its own evidence-chain index's known staleness (`F-04`); recommends a fresh native re-trace.
**Special Team:** `CLOSED_WITH_EVIDENCE, reconfirmed, no delta` — treats the directly-traced Sale-side mechanism as sufficient on its own; treats the un-retraced Purchase-side nuance as secondary.
**Resolution path:** one bounded, native re-trace of the Purchase-side cancellation cascade within Inventory Core Backbone's own evidence (not borrowed from GROUP_A). Small, scoped, does not require Team B authorization. **Owner:** Team A / Track 01. Source: `05_IBPV_DEEP_FINDINGS.md` §4.5.

### C-02 — Idempotency/migration-replay severity — Track 04 (IDTM)
**The shared fact:** no unified idempotency-key mechanism exists in the reference system; no source-identity provenance field exists on any Inventory record; migration/import replayability is confirmed absent as a reference-system mechanism.
**Council:** treats the combined absence as "the single weakest point in the whole chain for this mandate," un-advanced across five corrective rounds; recommends it become a named, first-class Team B functional requirement from day one.
**Special Team:** reaches the identical factual floor but characterizes it as "a material gap confirmed," correctly routed to Team A/Migration design, not an Inventory Evidence Gate blocker on its own.
**Resolution path:** Boss weighs whether this is a Gate-blocking requirement or a downstream design input — this is explicitly named as "the central unresolved question" in `06_IDTM_DEEP_FINDINGS.md` §6.1. **Owner:** Boss directly.

### C-03 — Return-valuation cost basis — Track 06 (Financial)
**The shared fact:** whether returned stock re-enters inventory at its original issue cost or a recomputed cost.
**Council:** found this untraced anywhere in the CORR-007B evidence package; lists it as an open, unevidenced risk (`FIN-DELTA-05`).
**Special Team:** independently traced the actual mechanism (`_get_value_from_returns()`) at primary source; reports it confirmed, well-designed, and closed.
**Resolution path:** exercise the Council pass's own review-of-Special-Team-findings function (per Charter §2) specifically on this citation — a narrow, bounded check, not a re-derivation. **Owner:** Track 01, on Boss's instruction. Source: `08_FINANCIAL_ACCOUNTING_INTERFACE_VETO_FINDINGS.md` §4.4, §10.2.

### C-04 — N-CONC-01 row-locking for `stock.quant` reservation — Track 07 (Security)
**The shared fact:** `try_lock_for_update()` at `stock_quant.py:1082`, spotted by IDR-007, never further characterized by either of the two subsequent rounds that had the opportunity to.
**Council:** `UNKNOWN WITH AN UNFOLLOWED LEAD` — treated as blocking, one of four named `HOLD` conditions.
**Special Team:** `PARTIALLY VERIFIED` — the register's own `EVIDENCE_MISSING` framing is more conservative than the primary source actually supports; not listed among its own open risks.
**Resolution path:** one bounded verification pass (locking mode, coverage across every quant-mutation path, sufficiency against the named race pattern) — already spotted twice, never followed up. **Owner:** Team A / Track 07. Source: `09_SECURITY_PRIVACY_RESILIENCE_VETO_FINDINGS.md` §3.2.

### C-05 — N-A12-01 evidence package (CORR-007B files 08/09) — Track 08 (Clean-Room) — **HIGHEST PRIORITY IN THIS ENTIRE REGISTER**
**The shared fact:** both bodies independently identify CORR-007B's N-A12-01 Account-led Inventory Period Close / Product Category Valuation proof package (files `08` and `09`) as the single highest clean-room-risk material in the whole chain, and both agree CORR-007B's own dedicated Clean-Room Compliance Review (file `12`) failed to catch what each separately found there.
**Council's finding is about language:** phrasing that drifts from descriptive toward prescriptive (e.g. file `09` §7: *"SMEsPlus functional design must use the location-based model actually present in source..."*). Council's verdict: a **material caution**, correctable by rewriting, a named precondition on a future Team B kickoff — not itself grounds to hold the chain today.
**Special Team's finding is about literal code:** verbatim, fenced-code-block reproductions of actual Odoo Python source — the full body and decorator of `_compute_valuation()`, the complete `property_valuation` field declaration with its exact Selection values and docstring, and the full boolean return expression of `_should_create_account_move()`. This directly contradicts the project's own written standard (A17, self-scored `VERIFIED` in DR-002: *"No vendor source code body... was copied verbatim into any A0-A20 deliverable"*), independently confirmed honored everywhere else in the 28 newly-added CORR-006/007A/007B files **except** these two. Special Team's verdict: `HOLD` — files `08`/`09` must be remediated **before** Team B or Team C are authorized to read this evidence.
**Why this is not merely coverage asymmetry:** neither body's own dedicated read of these exact two files caught what the other found. Read together, the two findings describe *more* risk than either shows alone — a document that both drifts toward prescriptive framing of reference-system structure *and* separately reproduces that system's literal source code.
**Resolution path (per `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md` §7, verbatim):**
1. Remediate files `08`/`09` to the project's own inline `file:line -- Class.field_or_method_name` citation style, removing the fenced Odoo Python code blocks — before Team B or Team C read this evidence for any N-A12-01 design work.
2. Correct or explicitly re-qualify the prescriptive-language passages as reference-only.
3. **Recommended tie-breaking action:** an independent third pass, or Boss's own direct read, of files `08`/`09` checking for both defect types, to establish one non-conflicting record before this package is ever handed to an authorized Team B/C session.
4. The planned `N_A12_01_CLEAN_ROOM_TARGET_CLOSE_CONTRACT.md` deliverable must be authored from the remediated version, not from files `08`/`09` as they stand today.
**Owner:** Track 01 / PMO, with Boss's direct tie-breaking read recommended. **This is the single item in this entire reopen most likely to warrant Boss's personal attention before any other downstream action.**

---

## Tier 3 — Genuine Material Unknowns (no conflict — simply unanswered)

| Ref | Item | Why it is a genuine unknown, not a carry-forward | Owner |
|---|---|---|---|
| U-01 | Warehouse-level (intra-company) authorization | The full 16-row `ir.rule` table scopes exclusively by `company_id`; no location/warehouse dimension found in either independent full read. Not merely undesigned — unevidenced either way. | Track 07 |
| U-02 | Damaged-goods receiving/warehouse exception category | Direct text search across the full nine-round chain, run independently by both TBRAC and IBPV, returns zero hits. Neither a defect nor a closed non-requirement — simply never asked. | Track 02/03 |
| U-03 | Inventory-side SaaS tenancy/company/runtime-isolation architecture (`SI-01..10` extension question) | No document anywhere states whether the Boss-approved Cross-Gate SaaS Invariants ruling extends to Inventory or whether Inventory needs its own, separately-approved invariant set. No Inventory-side gate register exists to attach an answer to. | Track 05, Boss |
| U-04 | `G-5` migration-cutover first opening balance | Source-confirmed to have **no reference mechanism at all** — not merely undesigned, genuinely absent as a concept in the reference system. Named the highest AI-fabrication-risk point in the whole Inventory scope. | Track 06/09, joint Account×Inventory |
| U-05 | Whether this reopen's own 9-Council/9-Special-Team dispatch is genuinely parallel | Both AI Control bodies independently raised this, unprompted by each other — a form of corroboration in itself. Neither can verify genuine concurrency versus another instance of the single-session-sequential pattern CORR-007B's file 14 disclosed at smaller scale, from inside its own sandbox. No session-log or invocation-ID evidence exists in the repository either way. | Track 01 / PMO |
| U-06 | Whether "Material Unknown Exhaustion" was ever formally re-declared or formally superseded | DR-002 declared it `NOT ACHIEVED`; no subsequent round (through CORR-007B) re-invokes the named standard, despite the chain visibly moving to an item-by-item Boss-challenge model instead. Neither closed nor explicitly retired. | Track 01, Boss |
| U-07 | Identity of the governing "9 Veto Challenge Council" | CORR-007B's own branch contains a self-declared, differently-composed "9 Veto Challenge Council" document (execution-team roster: Team A/B/C/D, Figma/UX, Functional/DB/Integration/Code leads), timestamped 8 minutes before the actual Boss-ratified Charter (audit-mandate roster: Audit/TBRAC/IBPV/IDTM/IESA/Financial/Security/Clean-Room/AI-Control). Neither cross-references the other. Both claim Boss approval. Conclusions happen to agree (N-A12-01 reopened HIGH) but the authority question itself is unresolved. | Track 01, Boss |

---

## Priority Ranking for Boss

1. **C-05** (Clean-Room, N-A12-01 files 08/09 code reproduction) — highest priority; sits directly in the path a future Team B author will read first once N-A12-01 unblocks.
2. **U-07** (which Council charter governs) — a foundational authority question underneath everything else in this register.
3. **C-02** (idempotency severity) and **U-04** (`G-5` opening balance) — both bear directly on AI-orchestrated migration safety, Boss's own stated priority for this reopen.
4. **U-03** (Inventory SaaS tenancy framework) — structural planning gap affecting every future Team B design session.
5. **C-01, C-03, C-04** — each a single bounded verification pass, low effort, high traceability value.
6. **U-01, U-02, U-05, U-06** — carry forward as named items; none blocks any other track's own progress.

No item in this register requires re-opening a CLOSED_WITH_EVIDENCE item elsewhere in the chain, and no item here was resolved by inventing evidence. Full citations for every row are in deliverables `01`, `03`–`12`.
