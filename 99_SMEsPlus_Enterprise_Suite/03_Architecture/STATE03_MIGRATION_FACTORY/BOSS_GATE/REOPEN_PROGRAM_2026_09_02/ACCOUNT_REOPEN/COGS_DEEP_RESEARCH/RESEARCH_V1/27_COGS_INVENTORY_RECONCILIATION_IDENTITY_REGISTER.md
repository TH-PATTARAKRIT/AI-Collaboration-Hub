# 27 — COGS / Inventory Reconciliation Identity Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE PARTIAL — FIVE IDENTITIES CLASSIFIED, NONE VERIFIED UNCONDITIONALLY, SCOPE CONDITIONS STATED`

---

## 1. Purpose

Governing prompt §14 supplies five candidate reconciliation identities and requires each to be derived and tested, not assumed. This file classifies each `VERIFIED / CANDIDATE / HOLD`, states the evidence for the classification, and — critically — states the **scope conditions**: under which accounting model (Periodic, Perpetual, both), and under which named exceptions, each identity holds or breaks. An identity classified `VERIFIED` here means verified *as a structural/definitional statement given the evidence*, not verified as an approved SMEsPlus design formula — no identity in this file authorizes a specific SMEsPlus journal structure or account code.

Classification discipline used throughout:

- `VERIFIED` — the identity holds by definition or is directly and unconditionally supported by Layer A/inherited evidence, with no material exception found.
- `CANDIDATE` — the identity holds under stated conditions, breaks under stated exceptions, and is a reasonable working formula for SMEsPlus to carry forward, pending Joint review.
- `HOLD` — the identity's truth cannot currently be determined from available evidence, or the evidence found actively conflicts with a naive reading of the identity.

---

## 2. Identity 1 — Physical Stock Conservation

> `Opening Qty + Valid Inflows − Valid Outflows +/− Controlled Adjustments = Closing Qty`

### 2.1 Ownership boundary

This identity describes **Stock Truth**, which the governing prompt (§2) and the inherited Inventory Final Solution v1.0 package both assign to Inventory, not Accounting. Accounting is a *consumer* of this identity's output (a certified closing quantity feeding valuation), not its owner or verifier. This file therefore does not attempt to independently prove quantity conservation — that proof, if it exists, lives in the Inventory package — and instead tests only what Accounting is entitled to assume about it.

### 2.2 Classification

`CANDIDATE` — from the Accounting side. The identity is structurally sound (it is a closed-system conservation law: nothing leaves stock except through a named outflow category, nothing enters except through a named inflow category, and any residual is captured as a controlled adjustment rather than silently dropped). But Accounting cannot classify it `VERIFIED` on its own evidence, for two reasons:

1. **"Controlled" is doing the load-bearing work.** An adjustment that is *not* controlled (unexplained shrinkage never counted, a movement bypassing the recognized inflow/outflow categories) breaks the identity silently — the equation will still "balance" arithmetically only if every real-world movement was captured under one of the named terms. This is precisely why scenario 30 (period-end close with unbilled receipts/uninvoiced deliveries) and scenarios 21–23 (adjustment gain/loss, scrap/damage/shrinkage) exist as separate scenarios rather than being folded into "inflow/outflow."
2. **`C-02`/`IV-06`/`T-1` (idempotency) is a precondition, not a consequence, of this identity.** If a movement fact can be double-counted or dropped (the exact question `T-1` leaves open), the conservation identity is falsified at the input level before Accounting ever sees a valuation figure. This file records that dependency rather than assuming it away.

### 2.3 Scope conditions

Holds under **both** Periodic and Perpetual as a quantity statement (quantity conservation is a physical fact independent of financial recognition timing). Does **not** hold as stated in any period where: (a) a movement was recorded outside the recognized inflow/outflow taxonomy, (b) a physical count has not yet been reconciled to system quantity (i.e., "Closing Qty" is system-theoretical, not counted-actual), or (c) inter-company/inter-location transfers are in transit at the measurement date and not consistently attributed to one side or the other (relevant to scenario 25/26).

---

## 3. Identity 2 — Inventory Value Identity

> `Opening Inventory Value + Capitalizable Cost Added − Cost Released +/− Approved Valuation Adjustments = Closing Inventory Value`

### 3.1 Layer A evidence

Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02: the Valuation Account is described as recording the financial value of physical stock, updated either at each qualifying transaction (Perpetual) or at the periodic closing process (Periodic) via the Variation Account. This confirms the structural shape of the identity — a value account that only moves through named categories of addition and release — but the retrieved documentation does not itself state the identity as a formula; it is derived from the account-behavior description, not quoted directly.

### 3.2 Classification

`CANDIDATE`. The identity's shape matches both the reference system's documented account mechanics and the Inventory package's own valuation-fact model (file `01` §3.1: a valuation fact carries event type, cost basis/amount, effective date). It is not `VERIFIED` because:

1. **"Capitalizable" and "Approved" are unresolved SMEsPlus policy terms**, not yet defined by a closed rule set. Landed cost eligibility (`JT-08`), WIP recognition timing (`JT-09`), and the costing-method rules (`JT-02`) all bear directly on what counts as "capitalizable cost added," and none of those are closed.
2. **Timing mismatch between capitalizable cost arrival and cost release** (landed cost after partial or full sale — scenarios 9–11) means the identity can be temporarily true only against a value that itself still contains an unresolved allocation, i.e., the identity balances arithmetically at any snapshot but the *meaning* of "Closing Inventory Value" is provisional until all in-flight cost allocations settle.

### 3.3 Scope conditions

Holds under both Periodic and Perpetual as a bookkeeping identity for the Valuation/Inventory Asset account in isolation (by construction, any account's ending balance equals its opening balance plus debits minus credits within the account). It does **not** by itself prove the *value is correct* — it only proves the account is internally consistent. It breaks as a *true-value* statement in any period with (a) an unresolved landed-cost allocation not yet posted (scenario 9/10/11), (b) a mid-period costing-method change without a documented conversion adjustment (scenario tie to §7 of file `15`), or (c) negative-stock/negative-value exceptions where the reference system and the Inventory package both note valuation cannot be meaningfully computed until quantity is non-negative (cross-reference file `06`/`15` negative-stock handling).

---

## 4. Identity 3 — Cost Release Identity

> `Inventory Cost Released → COGS OR another explicitly approved financial classification`

### 4.1 Classification

`VERIFIED` — but only as a **structural/definitional** statement, and this distinction matters enough to state plainly. The identity as written is a disjunction with an open second branch ("OR another explicitly approved financial classification"), which makes it true almost by construction: it asserts that every cost release lands *somewhere* named and approved, without asserting that "somewhere" is always COGS. Read this way, the identity is simply a restatement of the governing prompt's own hard rule (§22): "Not every inventory-value decrease is COGS." It is `VERIFIED` as a **governing constraint** the accounting design must satisfy, not as evidence that any specific SMEsPlus classification scheme currently satisfies it.

### 4.2 What is NOT verified

What remains open — and is `CANDIDATE`/`HOLD`, not verified — is the actual **classification rule set** that decides which released cost goes to COGS versus another account: scrap/damage/shrinkage (scenario 23), write-down/impairment (scenario 24, Thai-authority-dependent, routed to file `24`), inventory adjustment loss not tied to a sale (scenario 22), inter-company transfer (scenario 26, possibly not a "release" at all but a relocation), and manufacturing consumption into WIP (scenario 27, a release from raw-material inventory that is *not* COGS — it is a transfer into another asset, WIP, until scenario 29 converts finished goods into COGS at sale). Each of these is evidence that the naive assumption "inventory decrease = COGS" is false in at least five of the 32 mandatory scenarios, which is itself the proof of why the identity needs the open second branch. This classification rule set is not decided in this session (governing prompt §12: "Do not prescribe final SMEsPlus account codes or journal structure in this research session") and remains `HOLD` pending the archetypes in file `12` and the classification register in file `20`.

### 4.3 Scope conditions

Holds under both Periodic and Perpetual as a governing constraint. Under Periodic specifically, §6.2 below shows this identity is at its most fragile in practice, because the periodic closing process computes a single residual "variation" figure that does not, by construction, separate COGS from non-COGS releases unless a separate physical-loss/adjustment figure has already been extracted before the residual is computed.

---

## 5. Identity 4 — Periodic COGS Candidate Identity

> `Opening Inventory + Net Purchases / Capitalizable Costs − Closing Inventory = COGS` (adjusted for the actual applicable accounting model)

### 5.1 Layer A evidence

Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02: under the Periodic method, the documented flow is "post vendor bills as expenses by nature, and update stock valuation in the closing entry by reducing expenses (stock variation)." Under the Perpetual method: "post vendor bills as assets (stock valuation), report expenses when goods are sold (cost of goods sold)." The closing process is described as posting "the difference between what has been invoiced and received/delivered." This is the clearest available Layer A confirmation that the Periodic method structurally computes its expense-side figure as a **residual/plug** at closing, rather than tracking it transaction-by-transaction — which is exactly the mechanical basis of the classic Opening+Purchases−Closing=COGS formula.

### 5.2 Classification — and the material finding

`CANDIDATE`, with a **material scope condition that must not be lost**: this identity holds *only* under the Periodic accounting model, and even then it holds only as a formula for the **aggregate residual/variation figure**, not automatically as a formula for **COGS specifically**. The finding, stated plainly because it directly serves the governing prompt's own emphasized principle ("Not every reduction in Inventory Value is COGS"):

**A naive application of this formula silently mislabels every non-sale inventory reduction as COGS, unless those reductions are separately identified and removed from the residual before the formula is applied.** Under a pure periodic count-based approach, the residual (Opening + Purchases − Closing) captures the *combined* effect of goods sold, goods scrapped, goods lost to shrinkage, goods written down, and any unrecorded movement — because the formula has no way to distinguish *why* the ending count is lower than expected. If scrap, shrinkage, or write-down amounts (scenarios 22–24) are not separately measured and subtracted out first, the identity as literally written produces an inflated COGS figure that has silently absorbed non-COGS losses — a direct violation of Identity 3 (§4) and of governing prompt §22. This is not a hypothetical risk; it is the documented mechanical behavior of "closing entry accounts for the difference" read together with the Inventory package's own insistence that scrap/loss/adjustment are separately-provenanced facts (`HX-11`, `HX-12`).

The corrected form this evidence supports — offered as a Layer C candidate only, not a decision — is:

`Opening Inventory + Net Purchases/Capitalizable Costs − Closing Inventory − Separately-Identified Non-COGS Releases (scrap/loss/write-down/adjustment, each independently evidenced) = COGS`

This corrected form is `CANDIDATE`, not `VERIFIED`, because it depends on SMEsPlus actually capturing "separately-identified non-COGS releases" as distinctly provenanced facts at the same granularity as the Inventory package's `HX-11`/`HX-12` handoff rows — which is a design commitment, not yet an implemented and evidenced one.

### 5.3 Scope conditions (explicit, per governing prompt §14 requirement)

| Condition | Effect on identity |
|---|---|
| Periodic method | Identity's residual form applies by construction (this is structurally how Periodic computes its expense figure) |
| Perpetual method | Identity does **not** apply as a defining formula — under Perpetual, COGS is recognized transaction-by-transaction at the sale/invoice event (per `JT-04`, still open on exact timing), and Opening+Purchases−Closing is at best a *plausibility check* against the sum of individually-recognized COGS entries, never itself the source of the COGS figure |
| Unresolved landed cost in the period | Breaks the identity — "Net Purchases/Capitalizable Costs" is understated or overstated until the landed-cost allocation settles (ties to Identity 2 §3.3 and to `JT-08`) |
| Costing-method change mid-period | Breaks the identity unless a documented conversion adjustment reconciles the opening balance under the old method to the closing computation under the new method — no such conversion mechanism is yet designed (`JT-02`) |
| Scrap/loss/write-down not separately captured | Silently corrupts the identity as described in §5.2 — the single most material finding of this identity's testing |
| Return flows (purchase or sales returns) not separately netted | Distorts "Net Purchases" and/or the implied sales-cost figure unless returns are correctly signed and dated within the same period boundary (ties to scenarios 7, 8, 17, 18 and to `JT-05`/`C-03`) |

---

## 6. Identity 5 — Cross-System Reconciliation Identity

> `Inventory valuation as-of-date ↔ Accounting inventory balance + fully explained reconciling items`

### 6.1 Layer A evidence

Reference ERP official documentation — Valuation cheat sheet and Inventory Valuation pages, version 19.0, retrieved 2026-09-02: the documented closing entry exists specifically "to account for the difference between what has been invoiced and received/delivered," and the variation amount is described (secondary phrasing consistent with the official pages' Variation Account description) as what the closing entry must post "to make the General Ledger agree with the Inventory subledger." This is direct, if indirect-phrased, Layer A confirmation that the reference system itself treats Inventory-subledger-to-General-Ledger agreement as something that requires an explicit reconciling posting, not something that holds automatically at all times.

### 6.2 Classification

`CANDIDATE`. This is the identity with the **strongest** direct Layer A support of the five, because the reference system's own closing-entry mechanism exists for no other documented purpose than to make this identity true at the point of closing. It is not `VERIFIED` unconditionally because the reference evidence itself frames it as something requiring periodic *repair* (a closing entry), which is proof that between closings the two sides are expected to diverge, not proof that they never diverge:

- Under **Perpetual with real-time posting** (older/some current documented behavior), the two sides track closely by design, but the 19.0 documentation itself notes a shift toward posting at the invoice/bill event rather than at every stock movement, reopening a timing gap that then needs its own closing-entry repair (§2.5 of file `26`; version-delta evidence).
- Under **Periodic**, the two sides are *expected* to diverge continuously between closings by design — Accounting does not update the inventory valuation account transaction-by-transaction at all — so this identity only holds at closing boundaries, never intra-period.

### 6.3 Typical reconciling items (evidence-anchored, not exhaustive)

| Reconciling item | Basis |
|---|---|
| Unposted/in-transit landed cost allocation | Identity 2 §3.3, `JT-08` |
| Receipt recorded physically but bill not yet posted (or vice versa) | Scenarios 2/3/5; Periodic/Perpetual purchase-cost-timing research (files `12`, `13`, `17`) |
| Delivery recorded physically but invoice not yet posted (or vice versa) | Scenarios 12/13/15/16; files `13`, `18` |
| Manual accounting-side adjustment not yet reflected in the Inventory subledger (or vice versa) | Structural consequence of two independently-updated ledgers; matches §2.4 of file `26` (clearing-account pattern exists precisely to manage this class of gap during migration) |
| Costing-method change mid-period without conversion | Identity 4 §5.3 |
| Negative-stock/negative-value exception periods | Cross-reference file `06`/`15` |
| Multi-company/tenant policy misalignment (different valuation timing per entity) | File `25`; `JT-01` |

### 6.4 Scope conditions

Holds, by the reference system's own documented design, **at the close of a defined closing/reconciliation cycle**, not continuously. Does not hold, and is not expected to hold, at arbitrary intra-period timestamps under Periodic. Under Perpetual, holds more closely intra-period but is not guaranteed to hold at arbitrary timestamps either, given the documented shift toward invoice-triggered (rather than movement-triggered) posting plus a residual closing entry. Any SMEsPlus "as-of-date" reconciliation report must therefore state, as part of its own output, which of these two postures it is measuring against — an unqualified "the two balances should always match" claim is not supported by any evidence gathered in this file.

---

## 7. Summary Table

| # | Identity | Classification | Holds unconditionally? | Primary breaking conditions |
|---|---|---|---|---|
| 1 | Physical Stock Conservation | `CANDIDATE` (Accounting-side view; Inventory-owned) | No | Uncontrolled/uncaptured movement; count not yet reconciled; in-transit transfers |
| 2 | Inventory Value | `CANDIDATE` | No — internally consistent by construction, but not proof of correctness | Unresolved landed cost; mid-period costing-method change; negative stock |
| 3 | Cost Release → COGS or approved classification | `VERIFIED` (as governing constraint only) | Yes, as a constraint; No, as evidence any classification rule set yet satisfies it | Classification rule set itself is `HOLD`, routed to files `12`, `20` |
| 4 | Periodic COGS Candidate | `CANDIDATE`, with material correction found (§5.2) | No | Perpetual model (does not apply); unseparated scrap/loss/write-down (silently corrupts); unresolved landed cost; costing-method change; unnetted returns |
| 5 | Cross-System Reconciliation | `CANDIDATE`, strongest direct Layer A support | No — holds at closing boundary, not continuously | Intra-period timing gaps under both models; multi-company misalignment |

---

## 8. Cross-References

- `JT-01`–`JT-12` — every identity above traces to one or more open Joint decisions as noted inline; none of the five identities is independent of those decisions.
- `HX-11`, `HX-12` (adjustment/scrap facts) — load-bearing for Identity 3 and the Identity 4 correction in §5.2.
- `C-02`/`IV-06`/`T-1` — precondition for Identity 1 (§2.2 point 2) and indirectly for all downstream identities, since a duplicated or dropped fact falsifies every identity built on top of it.
- File `26` §5–§6 — the migration-replay idempotency findings there are a direct application of Identity 2 and Identity 5 under the specific stress case of a migration/opening run.
- File `20` (Adjustment/Scrap/Loss/Write-down Classification) and file `12` (Periodic Accounting End-to-End Model) — own the classification rule set left `HOLD` under Identity 3 and Identity 4.

---

## 9. Open HOLD / JOINT Register (This File)

| ID | Item | Type |
|---|---|---|
| `H-27-01` | Classification rule set deciding COGS vs. other approved classification for a released cost | `HOLD` — routed to files `12`, `20` |
| `H-27-02` | Whether SMEsPlus will separately provenance non-COGS releases at the granularity Identity 4's corrected form requires | `CANDIDATE` only; no design commitment made here |
| `H-27-03` | Conversion mechanism for a mid-period costing-method change | `HOLD` — routed to `JT-02`, file `15` |
| `H-27-04` | Whether an "as-of-date" reconciliation report will disclose its closing-boundary-vs-continuous posture | `CANDIDATE` — recommended requirement, not a decision |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
