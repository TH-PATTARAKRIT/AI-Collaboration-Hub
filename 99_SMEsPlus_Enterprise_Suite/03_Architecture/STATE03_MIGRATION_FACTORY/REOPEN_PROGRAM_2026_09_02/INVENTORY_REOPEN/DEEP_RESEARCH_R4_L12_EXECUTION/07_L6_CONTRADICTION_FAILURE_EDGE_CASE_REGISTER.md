# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 07 — L6 Contradiction / Failure / Edge Case Register

Level: `L6 — Contradiction / Failure / Edge Case`
Scope: `15 mandated edge cases + 4 additional raised by R4`
Control Level: `/L9999.9999`
Status: `L6 COMPLETE FOR 15/15 MANDATED CASES + 4 ADDITIONAL — 6 ESCALATED TO L13+ — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Method

Each case is challenged rather than described. For each: what actually happens, what the reference pattern does (`L2-OBS` where inspected first-hand this session), where the contradiction or failure lies, and R4's disposition.

Disposition vocabulary:

| Disposition | Meaning |
|---|---|
| `RESOLVED IN DESIGN` | The v1.0 design position already answers it and R4 finds no delta. Nothing is closed by R4; the position is confirmed as still standing. |
| `OPEN — INVENTORY OWNED` | Inventory can answer it; nobody has. Not COGS-gated. |
| `OPEN — DEPENDENCY LOCKED` | Cannot be answered without the Accounting COGS Gap. |
| `NO REFERENCE PATTERN` | The benchmark supplies no answer to learn from; original design work. |
| `ESCALATED` | Requires a level beyond L12; see `19_L13_PLUS_ESCALATION_REGISTER.md`. |

---

## 2. The Fifteen Mandated Edge Cases

### `L6-01` Negative stock

**What happens.** Goods are delivered or consumed before their receipt has been recorded, leaving a negative balance.

**Reference behaviour.** `L2-OBS`: the balance genuinely can go negative; the *available* figure is clamped so it never displays below zero. There is an explicit internal allowance for reading a negative position, so negativity is a supported state rather than an error. A negative valued position is later compensated when the real receipt arrives — see `L6-13`.

**Contradiction.** A user reading the stock screen cannot distinguish "we have none" from "we owe two". The two situations require completely different actions.

**Disposition.** `OPEN — INVENTORY OWNED`. `IV-02` requires negative on-hand to be displayed and flagged, not hidden. R4 confirms via `R4-F-07` that the reference pattern hides it, so this is a required divergence, not an inheritance. The *valuation* consequence is `DEPENDENCY: ACCOUNTING COGS GAP`.

### `L6-02` Backorder

**What happens.** Less is delivered or received than was demanded, and the remainder must either follow or be abandoned.

**Reference behaviour.** A follow-up operation is created according to the operation type's policy — ask, always, or never.

**Contradiction.** The "never" setting silently closes a customer commitment short with no record of the decision. The commitment lives in Sale; the abandonment happens in Inventory.

**Disposition.** `OPEN — INVENTORY OWNED`. R4 records that closing a commitment short must be an explicit recorded act with a named actor, not a configuration side effect (`INV-F-08`). `GAP-MD-07` (unified partial/backorder/return Thai user flow) remains open.

### `L6-03` Partial delivery

**What happens.** Part of an order ships now, the rest later.

**Reference behaviour.** Handled through the same follow-up mechanism as `L6-02`.

**Contradiction.** The cost and revenue consequence of a partial delivery depends entirely on the recognition rule.

**Disposition.** `OPEN — DEPENDENCY LOCKED` — `JT-04` NOT DECIDABLE. Quantity handling is `RESOLVED IN DESIGN`; cost handling is not.

### `L6-04` Partial receipt

**What happens.** A supplier delivers part of an order.

**Reference behaviour.** As `L6-02`.

**Contradiction.** If a supplier bill covers the whole order but only part arrived, the bill and the stock disagree until the rest lands. Under a periodic posture the two sides are *expected* to diverge between closings by design, so the divergence is not itself an error — but nothing distinguishes an expected divergence from a real one.

**Disposition.** `OPEN — DEPENDENCY LOCKED` — `JT-03`, `JT-06`. R4's non-blocked contribution: an Inventory-to-ledger reconciliation output must state which posture it measures against (`RC-03`, and identity 5 in `05` §5).

### `L6-05` Return after invoice

**What happens.** A customer returns goods that have already been invoiced.

**Reference behaviour.** The quantity returns. `L2-OBS` plus the COGS evidence: under a weighted-average policy the return is valued at the **current** average at return time, not the original cost, and the average is not retroactively rebased. The evidence records a resulting discrepancy against the credit-note amount whose stated remedy in the reference system is a manual adjustment. Under a first-in-first-out policy the layer-consumption behaviour on return is **community-corroborated only, not primary-documented**.

**Contradiction.** The value returned to stock differs from the value that left it, so the two sides do not reconcile without intervention. Three dates — original sale, physical return, credit note — are independently settable with no forced alignment, so a cross-period return can be dated three different ways.

**Disposition.** `OPEN — DEPENDENCY LOCKED` and **the single most material case in this register**. `JT-05` / `RISK-C03` / `C-03` / `FIN-DELTA-05` is formally **NOT DECIDABLE** with three named missing inputs. R4's contribution is to state the consequence that Inventory owns: **if the original cost basis is chosen, Inventory must carry per-unit original-cost lineage, which is a data-model requirement.** That consequence must be understood before the decision is taken, not after.

### `L6-06` Return before invoice

**What happens.** Goods come back before any invoice exists.

**Reference behaviour.** Quantity returns; no financial document exists to reverse.

**Contradiction.** If cost is released at dispatch, a cost release exists with no revenue to match. If cost is released at invoicing, no release ever happened and there is nothing to reverse. The two postures produce structurally different corrections.

**Disposition.** `OPEN — DEPENDENCY LOCKED` — `JT-04` NOT DECIDABLE. R4 records this as the cleanest illustration of why `JT-04` cannot be deferred: the two answers are not variations of one design, they are different designs.

### `L6-07` Scrap with salvage value

**What happens.** Goods are written off but retain recoverable value — returnable packaging, scrap metal, usable parts. Thai SMEs do sell this.

**Reference behaviour.** `L2-OBS`: **none.** The scrap concept carries no salvage-value field and no salvage-recovery mechanism of any kind. Its lifecycle is two states, draft and done.

**Contradiction.** The business event is real and common; the system has no representation of it. A business that sells salvage either records it nowhere or records it as an unrelated sale, breaking the link to the write-off it came from.

**Disposition.** `NO REFERENCE PATTERN` and `ESCALATED` to `L13`. This is a genuine R4 gap-fill: prior rounds recorded the question as unresearched; R4 establishes it is unanswerable from the benchmark and must be originated. Findings `R4-F-03`, function `INV-F-13`.

### `L6-08` Lot mismatch

**What happens.** The batch physically picked is not the batch the system reserved; or a supplier reuses a batch code; or two records represent one physical batch.

**Reference behaviour.** `L2-OBS`: uniqueness is enforced on (identifier, product, company), and records with no company are possible, forcing a cross-company duplicate check as a special case.

**Contradiction.** Batch identity is presented to the business as a traceability guarantee, but its uniqueness is scoped in a way that permits collision across companies and permits company-less identities that collide with everything.

**Disposition.** `OPEN — INVENTORY OWNED`, feeding the L9 register. `R4-F-06`. `IV-04` is confirmed as necessary. Amendment and merge (`INV-F-20`) rewrite the recall chain and must be approved operations.

### `L6-09` UoM conversion mismatch

**What happens.** Goods are bought in one unit, stored in a second, sold in a third.

**Reference behaviour.** `L2-OBS`: conversion across categories is refused outright — correct and transferable. Within a category, conversion is factor-based and **rounds upward by default**.

**Contradiction.** Systematic upward rounding can only inflate quantity, never deflate it, and does so silently. For a Thai SME buying in `ลัง` and selling in `ชิ้น`, the inflation accumulates and eventually surfaces as an unexplained count difference — which will be investigated as theft.

**Disposition.** `OPEN — INVENTORY OWNED`. `R4-F-13`: rounding direction must be an explicit, per-category, versioned decision. `IV-11` (a factor change never alters historical quantity) is confirmed as necessary. Packaging contained-quantity changes (`INV-F-34`) carry the same non-retroactivity requirement.

### `L6-10` Scheduler duplication

**What happens.** A user presses run while a scheduled run is in progress, or presses it twice, or creates a purchase order manually while the scheduler is creating the same one.

**Reference behaviour.** `L2-OBS`: nothing prevents an overlapping run. There is no run-level mutual exclusion and no idempotency identity on what a run produces.

**Contradiction.** The precondition "the previous run is not still in progress" is required by correctness and enforced by nothing.

**Disposition.** `OPEN — INVENTORY OWNED` and `ESCALATED` to `L15`. `GAP-MD-21` is confirmed by R4 as a live structural exposure rather than a theoretical one. Root cause is shared with `L6-11` and with `RISK-C02`.

### `L6-11` Reordering rule conflict

**What happens.** More than one rule covers the same product and the same physical stock.

**Reference behaviour.** `L2-OBS`: uniqueness is enforced only on the combination (product, location, company). Two rules for the same product — one at a parent location, one at a child location — are both permitted and both active, and the shortfall computation walks the location hierarchy.

**Contradiction.** **Two overlapping rules on nested locations can each raise supply for the same shortfall.** The database constraint appears to prevent duplication but only prevents the exact-match case, which is the case a user is least likely to create by accident.

**Disposition.** `OPEN — INVENTORY OWNED`. `R4-F-11`. This is the most concrete new finding in R4's L2 work and it converts a Boss-mandated hypothetical into a demonstrated structural exposure. Combined with `R4-F-01` — the shortfall computation uses the greater of minimum and maximum, so an inverted min/max entry is silently accepted — `INV-M27` is the highest-value configuration-control target in the module.

### `L6-12` Multi-company location leakage

**What happens.** Stock, or visibility of stock, crosses a company boundary that should be closed.

**Reference behaviour.** `L2-OBS`: a location's company assignment is **optional**. Batch and serial identities may also be company-less. Company scoping on routes and their rules *is* genuinely enforced — a route belonging to one company with a rule belonging to another is rejected — which is a real strength worth transferring. Prior evidence records that company scoping generally is enforced at the application layer with **no database-layer backstop**, and that the audit of privileged bypass paths was never completed.

**Contradiction.** Isolation is asserted as a property of the system but is enforced by a layer that can be bypassed, on records whose company assignment is optional.

**Disposition.** `OPEN — INVENTORY OWNED` at the modelling level, **Boss-owned** at the architectural level. `RISK-U03` / `GAP-FS-10` — the Inventory-side multi-tenant invariant set **does not exist** — remains unresolved and is **Lane A, not COGS-gated**. Findings `R4-F-06`, `R4-F-09`. Full treatment in `10_L9_SAAS_MULTI_TENANT_MULTI_COMPANY_REGISTER.md`.

### `L6-13` Cost layer timing gap

**What happens.** Goods are issued before they are received. The issue must be valued at something, and the real cost is not known until the receipt lands.

**Reference behaviour.** `L2-OBS`: the issue is valued at an estimate and the resulting position is marked with a negative remaining quantity. When later receipts arrive, a compensation pass matches the estimated issues against the real receipts and books the difference. **The matching is sequenced by the technical creation order of the records, not by their effective business dates.**

**Contradiction.** A back-dated receipt entered after an estimated issue compensates as though it occurred later, because ordering follows entry sequence rather than event date. Since back-dated entry is routine in a Thai SME, the compensation can attribute cost to the wrong period. This also means a value adjustment can land after the period it economically belongs to has closed.

**Disposition.** `OPEN — DEPENDENCY LOCKED` and `ESCALATED` to `L13`. This is R4's most technically significant forensic finding and it was only obtainable from primary-source inspection. Recorded as `R4-F-20`.

### `L6-14` Landed cost after sale

**What happens.** A duty or freight invoice arrives after some or all of the goods have been sold. For Thai importers this is the normal case.

**Reference behaviour.** `L2-OBS`: the allocation splits by the proportion still on hand. The portion attaching to goods still held raises their value; the portion attaching to goods already gone cannot be capitalised. The COGS evidence records **three mutually incompatible behaviours** for that residual across versions, one of which produces **no journal entry at all** — characterised in that evidence as a control break rather than a third legitimate rule.

**Contradiction.** The most common real-world case for the target market is the case with the least stable reference behaviour.

**Disposition.** `OPEN — DEPENDENCY LOCKED` — `JT-08`, **Audit VETO concern retained**. The adopted conclusion stands unweakened: **SMEsPlus must design its own handling rather than adopt any of the three.** Inventory's non-blocked obligation is `LC-03` — state explicitly, at allocation time, which goods were still on hand and which had gone. `R4-F-05` adds that weight- and volume-based bases distort silently when those attributes are unmaintained.

### `L6-15` Inventory adjustment after period close

**What happens.** A count difference is discovered, or entered, after the period it relates to has been closed.

**Reference behaviour.** A lock date supplied by the accounting side gates it. Prior evidence records that the reference enforcement sits at the document level rather than the line level (`G-3`), and that a **global, unscoped bypass** exists (`G-2`).

**Contradiction.** A global unaudited bypass makes the control decorative: it can be switched off by anyone who can reach the setting, and its use leaves no trace.

**Disposition.** `RESOLVED IN DESIGN` at the mechanism level and `OPEN — DEPENDENCY LOCKED` at the consequence level. The v1.0 position — a native guard at both entry and validation, Accounting supplying the lock date, an exception path with named grantor, written reason, expiry and permanent record, and the global bypass **explicitly rejected as unauditable** — is treated as fixed and is not re-litigated. What remains open is `JT-06`: what happens to a late *cost*. The evidence records that the reference ERP has **no documented prior-period attribution mechanism at all**, so `JT-06` is largely original design work. `ESCALATED` to `L16`.

---

## 3. Four Additional Edge Cases Raised By R4

The mandated fifteen do not cover these, and each was surfaced by this session's forensic work.

### `L6-16` Enabling traceability on a product that already holds untracked stock

Existing balances have no batch identity. The system must decide what an untracked balance means once tracking is required: is it one implicit batch, is it unusable until counted, or is it silently exempt? No safe default is evidenced. `OPEN — INVENTORY OWNED`; connects to `GAP-MD-14` and `INV-F-26`.

### `L6-17` Changing a costing category while a product holds stock

`L2-OBS`: the reference system contains explicit handling for a product moving between categories with different costing methods, so the case is real and anticipated. The COGS evidence records that a method change does **not** retroactively rebase existing on-hand value — but that this is confirmed only for movement *away from* a standard-cost posture; the reverse and lateral directions remain a hold. `OPEN — DEPENDENCY LOCKED` — `JT-02`.

### `L6-18` A structured barcode that parses to a plausible but wrong quantity

A rejected scan is visible and gets fixed. A misparsed weight- or quantity-embedded barcode produces a credible number that nobody questions. `OPEN — INVENTORY OWNED`; `R4-F-12`; R4 records a scan-interpretation confirmation step as a design requirement.

### `L6-19` Running balance ordering under routine backdating

`R4-F-08`: ordering movement history by entry sequence and ordering it by effective date give different running balances the moment anything is backdated. The stock card is the document a Thai accountant and auditor rely on. `OPEN — INVENTORY OWNED`; the report must state its ordering rule and apply it consistently.

---

## 4. Contradiction Register — Unarbitrated Conflicts Carried Forward

R4 arbitrates none of these. Each is recorded because a future session must not mistake an unresolved disagreement for a settled position.

| ID | Conflict | Positions | Owner | R4 action |
|---|---|---|---|---|
| `C-01` / `RISK-C01` / `MOV-31` | Cancellation-cascade symmetry, sales side versus purchase side | One pass: partially verified. Another: closed with evidence, no delta | Team A / Track 01 | Recorded; native re-trace within Inventory Core still required |
| `C-02` / `RISK-C02` | Idempotency and replay: gate-blocking, or design input | One pass: the single weakest point in the whole chain. Another: a material gap but not a gate blocker | **Boss directly** | Recorded; R4 supplies new weight — see §5 |
| `C-03` / `RISK-C03` / `JT-05` / `FIN-DELTA-05` | Return cost basis | One pass: untraced, open, unevidenced. Another: traced and closed | Track 01 / Joint | Recorded; now formally NOT DECIDABLE at the Joint level |
| `C-04` / `N-CONC-01` | Row-locking sufficiency for reservation under concurrency | One pass: blocking unknown with an unfollowed lead. Another: partially verified, not blocking | Team A / Track 07 | Recorded; one bounded verification pass still required |
| `C-05` | Clean-room exposure in the prior evidence package | Council: language drift. Special Team: verbatim code reproduction | **Boss** | Recorded; containment state unchanged — see `13` §6 |
| `U-07` / `RISK-U07` | Which of two "9 Veto Challenge Council" definitions governs | Two documents, both claiming approval, not cross-referencing | **Boss** | Recorded; R4 follows the canonical charter roster and says so explicitly in `13` §2 |
| Contradiction on price-difference account scope | Blocks `JT-02` | Two incompatible readings | Joint | Recorded, dependency-locked |
| Contradiction on landed-cost residual posting | Blocks `JT-08`, Audit VETO retained | Three incompatible behaviours, one a failure mode | Joint | Recorded, dependency-locked |

---

## 5. R4's Weight On `C-02`

`C-02` has been an unresolved Boss decision across multiple rounds, with one side calling it gate-blocking and the other calling it a design input. R4 does not decide it, but it does supply new evidence that bears on it, and it would be a failure of this session to leave that evidence unstated.

Three independent lines converge on the same missing capability:

1. `L6-10` — scheduler runs can overlap with no mutual exclusion, so duplicate supply is producible.
2. `L6-11` — overlapping reordering rules on nested locations can each raise supply for the same shortfall.
3. `05` §4 — the Boss-approved 16-element handoff contract requires a deterministic idempotency identity, and Inventory cannot supply one. Under that contract's own stated rule, **no material handoff can be declared verified while element 15 is missing.**

Point 3 is the new one. When `C-02` was last argued, the 16-element contract did not yet exist. It now does, it is Boss-approved and effective, and it makes idempotency identity a precondition of *every* material Inventory-to-Accounting handoff rather than a quality improvement to some of them.

R4's recorded position: this is evidence the Boss should have when deciding `C-02`, and it points toward the gate-blocking reading. **R4 does not declare it gate-blocking. That remains a Boss decision.** Carried as `R4-F-16` and surfaced in `21_PMO_REVIEW_AND_RECOMMENDATION.md` and `22_BOSS_REVIEW_PACKAGE.md`.

---

## 6. L6 Coverage Result

| Measure | Result |
|---|---:|
| Mandated edge cases | 15 |
| Given full L6 treatment | 15 |
| Additional cases raised by R4 | 4 |
| Cases escalated beyond L12 | 6 — `L6-07`, `L6-10`, `L6-11` (via shared root cause), `L6-13`, `L6-15`, plus the reservation-concurrency aspect of `L5-03` |
| Cases with **no reference pattern at all** | 2 — `L6-07`, and the prior-period attribution aspect of `L6-15` |
| Cases dependency-locked | 6 — `L6-03`, `L6-04`, `L6-05`, `L6-06`, `L6-13`, `L6-14`, plus `L6-17` |
| Unarbitrated conflicts carried | 8 |
| Cases closed by this session | **0** |

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
