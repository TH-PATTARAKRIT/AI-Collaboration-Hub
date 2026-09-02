# 34 — Next Controlled Action and Owner Matrix

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `RECOMMENDATION ONLY — NO ACTION AUTHORIZED BY THIS FILE — BOSS DECIDES SEQUENCE AND OWNERS`

---

## 1. Priority 1 — Boss-Only Rulings That Block This Package's Own Reliability

| # | Decision | Register ID | Owner |
|---|---|---|---|
| 1 | **Direct-fetch re-verification of the version-19.0 Finance/Accounting settings surface.** Two automated fetch attempts failed with empty-content errors; the entire `19.0` field set in files `02`, `03`, `04`, `06` rests on search-index reconstruction. A short, targeted follow-up pass (not a full re-run of this session) should re-attempt direct extraction before any Joint session treats `19.0`-specific claims as more than `PROVISIONAL`. | `CGS-U04` | Boss to commission a short follow-up research pass |
| 2 | **Live-instance verification of Case 8** (product category reassignment with existing stock — does accumulated Stock Valuation balance re-class?). Documentation-only research could not resolve this and flags it as the single most operationally risky unresolved item in the precedence matrix. | `CGS-U07` | Boss to commission a live reference-instance walkthrough, out of scope for a documentation-only session |
| 3 | **Live-instance verification of the FIFO customer-return layer discrepancy.** Community-corroborated only; a worked FIFO return example was never independently confirmed. | `CGS-U32` (sub-item) | Same as above |
| 4 | **`RISK-U07` charter ruling** (two rival "9 Veto Challenge Council" charter definitions, both claiming Boss approval) — carried unresolved from the Inventory package and directly affects the evaluation standard used in this package's own file `28`. | `RISK-U07` (carried) | Boss only |

---

## 2. Priority 2 — Convene the Joint Accounting ↔ Inventory Session

This package's central conclusion is that `JT-01`–`JT-12` cannot be resolved by studying the reference ERP alone — every one of them requires an explicit SMEsPlus decision, informed by but not dictated by reference behavior. The Joint session should convene with this package (files `00`–`34`), the Inventory Final Solution v1.0 package, and the two Boss-approved Joint controls (22-Scenario Cross-Proof baseline, 16-field Minimum Handoff Data Contract) all in hand.

| # | Decision | Priority Within Joint Session | Why First |
|---|---|---|---|
| 5 | `JT-01` (valuation policy ownership: category/product/warehouse/standalone) | First — every other Joint decision below is scoped by this one | The precedence matrix (file `11`), Menu A–D evidence (files `03`–`06`), and multi-company register (file `25`) all show ownership scope shifted materially between reference-ERP versions; SMEsPlus must pick its own answer, not inherit either version's |
| 6 | `JT-04` (COGS recognition timing — dispatch vs. invoice) | Second — this package's single most cross-corroborated open question | Files `12`, `13`, `14`, `16`, `18` show no stable reference answer exists; the Thai matching-principle requirement (file `24` §2.4, `AUTHORITATIVE`) is the constraint the eventual answer must satisfy |
| 7 | `JT-05`/`C-03` (customer return cost basis) | Third — this package's single most material carried-forward gap | File `19` shows the reference ERP itself has no clean answer and admits a documented, unreconciled discrepancy between credit-note amount and inventory-value reversal |
| 8 | `JT-02` (permitted costing methods & change rules) | Fourth | File `15` supplies the method-by-method evidence; `TH-HOLD-COGS-03` (entity-vs-category consistency-rule scope) must be resolved by the Accounting-Tax track before this can close cleanly |
| 9 | `JT-03` (continuous vs. periodic valuation timing) | Fifth, alongside `JT-04` | File `14`'s comparison matrix supplies the evidence; row 13 (Thai SME operational fit) remains `HOLD` pending a lightweight practitioner validation (see item 12 below) |
| 10 | `JT-08` (landed-cost eligibility and posting structure) | Sixth | Scenario 11 (file `16`) is the sharpest evidence — a version-inconsistent, sometimes-unposted mechanism must not be inherited as-is |
| 11 | `JT-06` (late supplier bill after period close) | Seventh | File `08` §2.7 and file `23` §5.2 (GAP-2) show the reference ERP has no documented prior-period attribution mechanism at all — this is largely original design work |
| 12 | `JT-07` (period close design and snapshot content) | Eighth | Depends on `JT-01`/`JT-03`/`JT-04` being settled first; file `08` §1's "no dedicated closing wizard" finding reframes this as a configuration-and-ownership question, not a UI-feature question |
| 13 | `JT-09` (WIP recognition timing) | Ninth, conditional | Blocked on `GAP-FS-19` (Manufacturing in scope at all) being decided by Boss first — see Priority 3 |
| 14 | `JT-10` (inter-company transfer treatment) | Tenth | File `25` §2.7 corroborates, and does not require reopening, the existing two-fact design; mainly needs the `RISK-U03`/`GAP-FS-10` re-scoping (item 15) resolved alongside it |
| 15 | `JT-11`/`G-5` (opening-balance certification) | Eleventh | File `26` supplies candidate requirements (`AC-01`–`AC-05`); blocked on `GAP-FS-08` (below) |
| 16 | `JT-12` (period lock policy and backdating exceptions) | Twelfth | File `08` §2.6 and file `23` §2.6 largely corroborate the existing Inventory-side design; lowest incremental risk of the twelve |

---

## 3. Priority 3 — Scope and Routing Decisions

| # | Decision | Register ID | Owner |
|---|---|---|---|
| 17 | **Re-scope `RISK-U03`/`GAP-FS-10`** to explicitly include the Accounting-side policy-sharing question this package surfaces (Product Category company-scoping unconfirmed) — this is new scope on an existing Boss-blocking gap, not a new gap. | `CGS-U42`, `CGS-U43` | Boss |
| 18 | **Design `GAP-FS-08`** (migration provenance reference) jointly between Accounting and Inventory before any automated migration/replay tooling is built — this package's Accounting-side idempotency candidates (`AC-01`–`AC-05`, file `26` §5.2) cannot be implemented until it exists. | `GAP-FS-08`, `CGS-U45` | Joint Accounting × Inventory |
| 19 | **Confirm the receiving owner in the Accounting-Tax track** for all `TH-HOLD-*` and `TH-HOLD-COGS-*` items — a routing with no confirmed recipient is not a routing, as the Inventory package's own file `13` (E-3) already flagged. | All `TH-HOLD-*`/`TH-HOLD-COGS-*` | Boss to confirm the track's receiving owner |
| 20 | **Re-attempt extraction of the gazetted TAS 2 standard text** (as opposed to TFAC's own explanatory manual, which this session did successfully read and cite as `AUTHORITATIVE` on standard-setter authority). | `TH-HOLD-05-residual` | Accounting-Tax track |
| 21 | **Decide `GAP-FS-19`** (whether Manufacturing is in SMEsPlus v1.0 scope) — file `22`'s entire content is explicitly evidence-in-reserve, conditional on this Boss-owned scope question, not a design this session is authorized to assume. | `GAP-FS-19` (carried) | Boss |
| 22 | **Commission a lightweight Thai-accountant validation** (three to five practicing SME bookkeepers/accountants) on Periodic-vs-Perpetual operational fit, once `JT-03` is otherwise ready to convene — proportionate given the strength of file `24`'s statutory findings, per file `28` V-2's position. | `T-COGS-4` | Boss to commission |
| 23 | **Verify against the actual 16-field Minimum Handoff Data Contract** whether it already includes an as-of-date "unmatched valuation fact" query capability — this session did not re-open that Boss-approved contract's content, only flagged the question. | `CGS-U41` | Whoever holds the contract (Boss-approved artifact, commit `d9e845e`) |
| 24 | **Independent re-audit of this package**, or Boss reads it directly — this executor cannot self-certify (file `28` V-1/S-1 tension, mirroring the Inventory package's own unresolved `T-5`). | `T-COGS-5` (this file) | Boss |

---

## 4. What Happens If These Are Not Actioned

If Priority 1 items are not actioned, any Joint session convened on the strength of this package inherits `PROVISIONAL`-grade evidence for a materially large slice of current-version behavior without knowing it unless this register is read alongside the package. If Priority 2 is not convened, `JT-01`–`JT-12` remain exactly as open as they entered this session, and no COGS Final Solution candidate can be produced — this package is evidence, not a design, and was never intended to substitute for the Joint decisions it feeds.

---

## 5. Recommended Next Session Shape

Consistent with the Inventory programme's own precedent (Menu Deep Challenge → Final Solution), the next controlled session in this track should be a **COGS Final Solution** session, analogous in structure to `INVENTORY_FINAL_SOLUTION_V1`, that:

1. Digests this package's Layer 2 controlled evidence into Layer 1 SMEsPlus-owned candidate design language (per file `28` V-8's flagged requirement).
2. Is explicitly gated on Priority 1 and Priority 2 items above having at least a Boss ruling or Joint session outcome to build from — it should not proceed on the twelve open `JT-*` items being silently assumed.
3. Produces its own risk/gap/decision register, AI Audit challenge, and Boss Final Gate package, exactly as `INVENTORY_FINAL_SOLUTION_V1` did, rather than declaring any design frozen.

This recommendation is offered for Boss's consideration; it is not authorized by this file.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
