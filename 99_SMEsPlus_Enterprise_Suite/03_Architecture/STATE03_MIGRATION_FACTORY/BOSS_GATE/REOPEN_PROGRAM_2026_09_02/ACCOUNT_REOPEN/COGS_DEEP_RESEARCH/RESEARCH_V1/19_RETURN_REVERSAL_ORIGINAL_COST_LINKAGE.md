# 19 — Return / Reversal / Original Cost Linkage

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COLLECTION — CP-08 SCENARIOS 7, 8, 17, 18, 19, 20 — MATERIAL HOLD OPEN ON JT-05/C-03`

---

## 1. Scope and Method

This file answers governing-prompt §12 for the return/reversal archetypes and §10 scenarios 7 (purchase return before bill), 8 (purchase return after bill), 17 (customer return same period), 18 (customer return later period), 19 (cancellation before physical movement), 20 (correction/reversal after physical movement), plus the broken-link case (return with no traceable original document).

Three evidence layers are kept separate per governing-prompt §3 and are never merged into one unsupported conclusion:

- `Layer A` — Reference ERP observed documentation behavior (public documentation pages only; the product is called "the reference ERP" throughout, never by vendor name).
- `Layer B` — Thai accounting/tax/statutory evidence. This file does not carry primary Thai research (that is file `24`'s track). Where a Thai point is material to a return/reversal archetype, it is flagged `THAI RULE STATUS: HOLD — see file 24` rather than answered here.
- `Layer C` — SMEsPlus clean-room candidate semantics, always downstream of A and B, never a copy of A.

All citations use the form: `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`.

Foundational rule carried into every archetype below: **inventory emits facts; accounting decides postings.** Nothing in this file proposes a journal entry, account code, or cost figure for SMEsPlus. Every numeric example is the reference ERP's own illustrative figure, reproduced only to show mechanism, not as an SMEsPlus candidate value.

---

## 2. The Single Most Material Open Item — JT-05 / C-03 (Customer Return Cost Basis)

Per the Inventory Final Solution v1.0 register (file `12`, ID `JT-05` / `C-03`), the cost basis assigned to a customer return is **explicitly still open** and is **not resolved by this file**. This file's job is to add evidence, not to close the decision.

Material finding from Layer A: the reference ERP's own **Returns and refunds** documentation page (the feature-level guide a business user would read) contains **no statement at all** of what cost value is used to bring returned goods back into stock. It documents the mechanical steps (reverse transfer, credit note, before/after-invoice branching) and is silent on valuation. The valuation answer has to be assembled from a **separate** documentation surface (the accounting/valuation cheat sheet and the average-price-on-returns page), and even there the two reference cost methods disagree in a materially relevant way:

- Average Cost (AVCO): a return is valued at the **current** average unit cost at the moment of return, not at the unit cost that applied when the item was originally sold or purchased. The average itself is **not recalculated** by a return — a return only removes/adds quantity and value at whatever the average already is.
- First-In-First-Out (FIFO): outgoing movements consume the oldest surviving cost layer(s) at time of delivery. A return is documented as reversing a movement "based on the costing method defined on the product," and community-level discussion around the official documentation (weaker, secondary evidence, not treated as authoritative here) describes edge cases where a return does not cleanly restore the exact original layer it came from, particularly when intervening receipts or deliveries have already consumed or altered the layer structure.

`Fact Status: CONFLICTING (documented mechanism vs. documented silence)`. The mechanical "how to click Return" documentation and the "how cost is computed" documentation are two different pages that do not cross-reference each other's treatment of cost basis. This is itself evidence worth preserving: a reference-ERP user following only the feature-level Returns documentation would not learn the valuation answer at all. This materially reinforces why `JT-05/C-03` must stay open rather than be inferred from UI convenience.

Evidence:
- `Reference ERP official documentation — Returns and refunds, version 18.0/19.0, retrieved 2026-09-02`
- `Reference ERP official documentation — Average price on returned goods, version 19.0, retrieved 2026-09-02`
- `Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02`

---

## 3. Archetype — Purchase Return Before Bill (Scenario 7)

### REFERENCE OBSERVATION
A goods receipt has been validated (physical stock recorded) but no vendor bill exists yet. The user opens the validated receipt and uses the "Return" action, which opens a reverse-transfer window defaulting to the received quantities; quantities can be edited or lines removed before confirming. Validating the reverse transfer creates an outbound warehouse operation that reduces on-hand quantity and, under automated/perpetual valuation, generates an accounting entry reversing the inbound valuation. Because no bill exists yet, the purchase order's "received but not billed" quantity is updated so that a bill created afterward is generated only for the quantity actually retained.

### ACCOUNTING MEANING
This is a pure Stock Truth correction with no Financial Truth artifact (no payable, no invoice) yet in existence. The valuation reversal undoes a provisional inventory-asset increase that was never matched to a vendor obligation. There is no COGS effect — nothing was ever sold — and no price-difference exposure yet because no bill price exists to compare against.

### THAI RULE STATUS
HOLD — see file 24. No statutory conflict is expected in principle (the item never left controlled custody and no revenue/expense was recognized), but documentary evidence support (delivery note / return note matching under Thai practice) for this specific pre-bill return path has not been independently verified in this file and must not be assumed.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE (low material risk)`: a pre-bill purchase return should be treated by SMEsPlus as a pure inventory-fact reversal referencing the original receipt fact, with no accounting recognition beyond the inventory-asset reversal already implied by the original receipt fact ever having been provisionally capitalized. This candidate is downstream of Inventory's `HX-07` (receipt valuation fact) and `HX-10` (return fact) handoff rows and does not itself decide whether SMEsPlus capitalizes at receipt at all — that is `JT-03`/`JT-04` territory, not this file's.

---

## 4. Archetype — Purchase Return After Bill (Scenario 8)

### REFERENCE OBSERVATION
A vendor bill has already been posted (a payable and an expense/asset entry exist) when the return is initiated. The reverse-transfer mechanism itself is identical to the before-bill case, but it is documented as insufficient alone: the bill "cannot be directly modified" once validated, so the user must separately open the posted bill and use its "Credit Note" action (or create a vendor refund from scratch under Accounting → Vendors → Refunds) to produce a matching financial reversal. The reference documentation explicitly warns of a **discrepancy risk**: a full-value credit note reverses the entire original bill entry, but the return's own inventory valuation reversal is computed independently (at the return-time cost basis, per §2 above) — the two reversal amounts are not guaranteed to be equal, and the documentation states this "can cause a discrepancy between the return inventory valuation and the credit note, requiring manual adjustment of the inventory valuation journal entry."

### ACCOUNTING MEANING
Two independent reversal computations exist for the same physical event: (1) the inventory valuation reversal, driven by the costing method's current cost (AVCO current average, or FIFO layer state) at time of return; and (2) the vendor-side financial reversal, driven by whatever the credit note is written for (which may follow the original bill price, a partial amount, or a negotiated adjustment). When (1) ≠ (2), a residual sits somewhere — the documentation's own answer is "manual adjustment," i.e., the reference ERP does not auto-reconcile this gap. This is a directly relevant precedent for the "Price Difference" concept already scoped in governing-prompt §5/§6, extended here to the return path specifically, not just the original receipt path.

### THAI RULE STATUS
HOLD — see file 24. The credit-note-vs-inventory-reversal gap has a plausible Thai tax-document angle (a purchase return typically requires a supplier-issued credit/debit tax invoice under Thai VAT practice) that is outside this file's authority to confirm; flagged, not resolved.

### SMEPLUS CANDIDATE / HOLD
`HOLD`: the reference ERP's own documented admission of a residual/manual-adjustment gap between financial reversal and inventory-value reversal is material enough that SMEsPlus must not silently assume automatic reconciliation is achievable. Any SMEsPlus design must explicitly decide who owns closing this gap (Accounting, per the domain boundary in governing-prompt §2) and how the residual is classified (price variance vs. loss vs. suspense) — none of which this file may pre-decide. This links directly to `JT-06` (late supplier bill / price variance) and should be evidenced jointly with it rather than treated as a fully separate question.

---

## 5. Archetype — Customer Return, Same Period (Scenario 17)

### REFERENCE OBSERVATION
Before an invoice has been sent, a return is completed by a reverse transfer alone: the delivery order's "Return" action opens the same reverse-transfer mechanism, and on validation the sales order's delivered quantity is reduced. When an invoice is subsequently generated, it is generated only for the net (retained) quantity — i.e. the reference ERP prevents ever invoicing the returned units in the same-period-before-invoice case, rather than invoicing and then crediting them.

### ACCOUNTING MEANING
No revenue was ever recognized for the returned units, so there is no COGS-reversal-plus-revenue-reversal pairing to perform — the system simply never creates the revenue or COGS fact for the returned quantity in the first place. This is the cleanest of the four return archetypes because it avoids the credit-note/valuation-reversal mismatch described in §4 and §6: there is only one financial event (the eventual net invoice), not two independent reversals to reconcile.

### THAI RULE STATUS
HOLD — see file 24. Whether Thai practice would still require a documented delivery/return note trail even when no tax invoice was ever issued for the returned quantity is a statutory documentation question, not an accounting-recognition question, and is out of this file's authority.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE (low material risk, same rationale as §3)`: pre-invoice same-period customer returns are a pure Stock Truth reversal referencing the original delivery fact, with COGS/revenue recognition deferred to (and net of the return at) actual invoice time — consistent with `JT-04`'s still-open dispatch-vs-invoice timing question, not a resolution of it.

---

## 6. Archetype — Customer Return, Later Period (Scenario 18)

### REFERENCE OBSERVATION
Where an invoice has already been validated (whether same period or a prior period), the documented process is two-step: the reverse transfer is processed identically to §5, but because the validated invoice "cannot be directly modified," the user must separately open the invoice and use its "Credit Note" action. The credit note form requires a stated reason, a journal, and a Reversal Date, and offers "Reverse" or "Reverse and Create Invoice." On completion the customer shows an outstanding credit balance available for allocation against other invoices.

### ACCOUNTING MEANING
Exactly the same structural gap as §4 (purchase return after bill) exists on the sales side, mirrored: the reverse transfer computes an inventory-value restoration at a cost basis independent of what revenue amount the credit note actually reverses. If the credit note is issued at the original invoiced price but the goods are restocked at a different current cost (AVCO current average, or a FIFO layer that no longer matches what was originally shipped), gross margin recognized in the return period will not exactly mirror the margin originally recognized at sale. Because this scenario crosses a period boundary (18, as distinct from 17), any such mismatch also becomes a cross-period recognition question — the credit note's Reversal Date field is documented as a distinct, user-set field, meaning the reference ERP does **not** force the financial reversal to land in the same period as the original sale, nor does it force it to land in the same period as the physical return. All three dates (original invoice, physical return, credit note reversal date) can differ.

### THAI RULE STATUS
HOLD — see file 24. Cross-period reversal of previously recognized revenue/COGS, and the acceptable Thai tax period for issuing a credit note against an already-filed VAT output tax invoice, is a statutory question this file does not have authority to answer. This is flagged as materially relevant to `JT-05/C-03` rather than resolved.

### SMEPLUS CANDIDATE / HOLD
`HOLD`: this is the archetype where `JT-05/C-03` bites hardest. Three independently-settable dates (original sale, physical return, financial reversal) combined with two independently-computed values (inventory-value restoration vs. credit note amount) means SMEsPlus cannot treat "process a customer return" as a single atomic event with one obvious cost basis. Candidate framing only: the return must carry an explicit reference back to the original sale's cost-release fact (per Inventory's `HX-10` return-fact row) so that Accounting — not Inventory — decides whether to reverse at original cost, current cost, or a policy-defined blend; SMEsPlus must not pick one of these three without a resolved `JT-05/C-03`.

---

## 7. Archetype — Cancellation Before Physical Movement (Scenario 19)

### REFERENCE OBSERVATION
The reference ERP's warehouse operations carry a documented state progression (draft/waiting → confirmed → done, with a separate cancelled state). Search-level and forum-level evidence (secondary, not an official documentation page, and treated here at reduced confidence) consistently describes that cancelling a transfer **before** it reaches the done/validated state leaves no stock movement and no accounting entry to reverse, because none was ever created — automated valuation entries are documented as being generated at validation, not at draft/confirmation. Once a transfer has reached done state (and, where applicable, its automated valuation entry has posted), the same secondary evidence describes cancellation as no longer a simple state change: reversing a done, journal-posted movement requires an explicit correcting action (an "Unlock" and quantity edit, or a dedicated reversal), not a plain cancel.

### ACCOUNTING MEANING
This maps to ordinary double-entry discipline: an unposted transaction has nothing to reverse; a posted transaction requires a correcting entry, not a deletion. The material accounting boundary is exactly the done/not-done transition, which is the same boundary the reference ERP uses to decide whether a valuation layer and journal entry exist at all.

### THAI RULE STATUS
HOLD — see file 24. Not independently a Thai-specific question in principle (this is general double-entry practice), but the acceptable Thai period-lock / backdating tolerance for correcting an already-posted, already-period-closed movement is `JT-12` territory and file 23's, not resolved here.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE`: SMEsPlus should treat "cancel before movement" as a no-financial-effect event as long as no valuation fact was ever emitted by Inventory for that event — consistent with the "Inventory emits facts; Accounting decides postings" boundary, since an event that never emitted a fact has nothing for Accounting to post or reverse. This candidate explicitly does **not** extend to a done/posted movement; see §8.

Evidence for this archetype is weaker than others in this file (secondary/community-level, not a fetched official documentation page confirming the exact cancel-state mechanics) — `Fact Status: PROVISIONAL`, and a targeted primary-source re-verification is recommended before this candidate is relied upon downstream.

---

## 8. Archetype — Correction/Reversal After Physical Movement (Scenario 20)

### REFERENCE OBSERVATION
Once a transfer is done and (under automated valuation) its journal entry posted, the documented correction paths observed across this file's evidence are all **additive reversals**, never in-place edits of the original entry: a reverse transfer (physical correction) paired with a credit note or vendor refund (financial correction) where a bill/invoice already exists, or a reverse transfer alone where no bill/invoice exists yet. No official documentation page reviewed in this session describes deleting or silently rewriting a posted valuation layer or journal entry as a supported correction path.

### ACCOUNTING MEANING
This is consistent with an audit-trail-preserving correction model: every correction is itself a new, dated, referenced transaction, not a mutation of history. This is favorable evidence for governing-prompt §15 Audit VETO expectations (evidence chain, no skipped gate) and for §22's "no hidden timing assumption" rule, because the reference ERP's own documented behavior does not hide the correction — it creates a second visible fact.

### THAI RULE STATUS
HOLD — see file 24. Consistent in principle with Thai audit-trail expectations for accounting records, but not independently verified against Thai statutory retention/correction rules in this file.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE`: SMEsPlus should require that any post-movement correction be modeled as a new, referenced reversal/adjustment fact carrying a pointer back to the original fact — never an in-place mutation — regardless of how `JT-05/C-03`, `JT-06`, or `JT-12` are eventually resolved. This is a process-shape candidate only; it does not decide cost basis, timing, or account classification.

---

## 9. Broken-Link Case — Return With No Traceable Original Document

### REFERENCE OBSERVATION
Every return mechanism reviewed in this file (§3–§6) is documented as originating **from** a specific validated receipt or delivery record (the "Return" button lives on that validated document itself), and the reverse-transfer window is documented as defaulting to that specific document's quantities. No official documentation page reviewed describes a supported path for creating a return with no source document reference — the feature is structurally document-linked, not a free-standing "receive stock back" action. A free-standing stock increase/decrease with no originating transfer would fall under the Inventory Adjustment mechanism (file `20`), not the Return mechanism, in the reference ERP's own model.

### ACCOUNTING MEANING
The reference ERP effectively treats "return" and "orphan inventory correction" as two different concepts with two different UI mechanisms and, materially, two different account-treatment expectations: a return is presumed to be a linked reversal of a known original cost fact, while an unlinked quantity change is presumed to be an adjustment (gain/loss), not a return. A "return" that arrives with no traceable original document is, on this evidence, not actually a return in the reference ERP's own vocabulary — it is an adjustment wearing a return's name.

### THAI RULE STATUS
HOLD — see file 24. Whether Thai practice would accept an unlinked "return" as a valid basis for a tax credit note (as opposed to requiring documentary linkage to an original tax invoice) is a statutory question outside this file's authority.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE`: SMEsPlus should require every return fact to carry a mandatory reference to an original cost-release or receipt fact; a claimed "return" that cannot resolve such a reference should be rejected at the Inventory-fact layer as a return and, if a business justification exists, re-entered as an adjustment fact instead (file `20`), never silently accepted as a return with an assumed or fabricated original cost. This directly enforces governing-prompt §22's "no fabricated cost" rule at the point of highest risk (an untraceable reversal is exactly where a fabricated cost would otherwise slip in).

---

## 10. Version Delta Register (Return/Reversal Scope)

| Observation | Version(s) | Delta | Evidence |
|---|---|---|---|
| Perpetual/automated valuation posts at each stock movement in real time | 14.0–18.0 (as evidenced by cheat-sheet and valuation-config pages reviewed for those lines) | Baseline behavior assumed by most return-mechanism documentation reviewed | `Reference ERP official documentation — Automatic inventory valuation, version 17.0/18.0, retrieved 2026-09-02` |
| Perpetual valuation described as operating "at the invoice level" rather than creating a real-time entry at each stock movement | 19.0 | Material behavior change: the timing relationship between a return's physical reverse-transfer and its financial posting may differ under 19.0 versus the real-time model assumed in earlier versions. This directly affects the §6 "three independently-settable dates" finding — under a 19.0 invoice-level posting model, the financial posting trigger itself may have moved, not just its date field. | `Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02` |
| Scrap/Inventory-Loss location mechanism documented in materially the same shape (Location Type = Inventory Loss, associated Loss Account) | 13.0 through 19.0 pages reviewed | No material delta observed in this file's evidence for the returns/scrap boundary itself (full scrap treatment is file `20`'s territory) | `Reference ERP official documentation — Scrap inventory / Account for scrapped goods, versions 13.0–19.0, retrieved 2026-09-02` |

`Fact Status: PROVISIONAL` on the 19.0 "invoice-level" delta — this file located the statement in the valuation cheat sheet but did not independently trace its full mechanical effect on the return reverse-transfer timing specifically. This is flagged as a targeted follow-up, not resolved here.

---

## 11. Reconciliation Identity Check — Cost Released vs. Re-Capitalized

Governing-prompt §14's "Cost Release" identity (`Inventory Cost Released -> COGS OR another explicitly approved financial classification`) has a mirror-image return question this file surfaces but does not resolve: when a return re-capitalizes inventory, is the re-capitalized amount required to equal the amount originally released (symmetric reversal), or is it independently computed at current cost (as §2 and §6 show the reference ERP actually does)? The reference ERP's own documented behavior is **not symmetric** — release and re-capitalization are two independent computations that happen to often produce similar numbers when costs are stable, and documented as producing a visible residual when they are not (§4, §6). 

`Classification: HOLD`. This asymmetry is exactly the shape of `JT-05/C-03` and must be carried into any Joint Cross-Proof session as a named, evidenced risk — not smoothed over as if reversal were naturally symmetric.

---

## 12. Fact Status Summary

| Archetype | Fact Status |
|---|---|
| Purchase return before bill (§3) | VERIFIED (mechanism) / CANDIDATE (SMEsPlus treatment) |
| Purchase return after bill (§4) | VERIFIED (mechanism, including documented discrepancy risk) / HOLD (SMEsPlus treatment) |
| Customer return same period (§5) | VERIFIED (mechanism) / CANDIDATE (SMEsPlus treatment) |
| Customer return later period (§6) | VERIFIED (mechanism) / HOLD (SMEsPlus treatment) — carries `JT-05/C-03` |
| Cancellation before movement (§7) | PROVISIONAL (secondary evidence only) / CANDIDATE (SMEsPlus treatment, conditional on primary-source re-verification) |
| Correction/reversal after movement (§8) | VERIFIED (mechanism, by absence of any documented in-place-edit path) / CANDIDATE (SMEsPlus treatment) |
| Broken-link return (§9) | VERIFIED (mechanism absence) / CANDIDATE (SMEsPlus treatment) |
| 19.0 invoice-level posting delta (§10) | PROVISIONAL — targeted follow-up required |

---

## 13. What This File Does Not Do

This file does not resolve `JT-05/C-03`, `JT-06`, `JT-12`, or any other open Joint decision. It does not propose an SMEsPlus account code, journal line, or cost figure. It does not confirm any Thai statutory position (all Thai items are routed to file `24` as HOLD). It does not declare the Return/Reversal archetype set complete for Joint Cross-Proof purposes — the 19.0 version-delta item (§10) and the cancellation-mechanism evidence (§7) are both flagged `PROVISIONAL` and require further primary-source confirmation before this file's candidates can be upgraded to VERIFIED.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
