# 14 — Periodic vs Perpetual Comparison Matrix

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COMPARISON ONLY — NO RECOMMENDATION — FEEDS JT-03, CP-05/CP-06/CP-07 PREREQUISITE — HOLD ITEMS OPEN`

---

## 1. Purpose, Scope, and Non-Recommendation Statement

This file builds the mandatory comparison matrix required by the governing prompt §8.3. It compares the Periodic and Perpetual accounting patterns across fourteen dimensions using reference-ERP observed evidence (Layer A), flags where Thai evidence is required but not yet produced (Layer B — owned by file `24`), and states neutral SMEsPlus candidate semantics only where the governing prompt's three-layer transformation permits it (Layer C).

This file makes **no recommendation** between Periodic and Perpetual. The choice is explicitly reserved for Joint decision `JT-03` (continuous/perpetual vs periodic valuation timing), which this file feeds and does not close. Nothing in this file may be read as a SMEsPlus design decision.

Foundational rule carried from Inventory Final Solution v1.0 and restated here: **Inventory emits facts; Accounting decides postings.** Every dimension below describes what the reference ERP's Accounting layer does with a stock fact under each timing pattern — not a redefinition of what Inventory emits.

This file assumes the full Periodic and Perpetual lifecycle narratives are separately built in files `12` and `13` (governing prompt §8.1/§8.2). Where those files are not yet populated at the time of this writing, this matrix stands on its own directly-cited evidence and does not borrow unstated conclusions from `12`/`13`.

---

## 2. Evidence Layer Legend

- **Layer A** — Reference ERP observed behavior, cited as `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`.
- **Layer B** — Thai accounting/tax/audit evidence. File `24` is the owning file for authoritative Thai evidence; this file only flags where a Thai check is required and states `HOLD / EVIDENCE REQUIRED` unless a general, non-jurisdiction-specific accounting-framework point is being distinguished from a Thai-specific statutory claim (see §7).
- **Layer C** — Neutral SMEsPlus candidate semantics, marked `CANDIDATE` (a tentative business-meaning restatement, not a design decision) or `HOLD/JOINT` (explicitly reserved for `JT-03` or another named Joint ID).

No cell in the tables below is left blank. Where evidence does not exist, the cell reads `UNKNOWN / HOLD`.

---

## 3. Version-Delta Notice — Material Change in Perpetual Trigger Timing

Before the matrix, one version-delta finding governs several rows below and must not be silently carried forward from older learning.

Reference ERP documentation for the current major version states explicitly that the point at which a Perpetual-pattern stock valuation journal entry is generated **changed** relative to prior versions:

- Prior-version behavior (versions below the current major release, evidenced against version 13.0 through the version immediately preceding the change): the Perpetual/Automated pattern posted a real-time accounting entry **at each stock movement** — i.e., at goods receipt and at goods delivery/dispatch, independent of vendor bill or customer invoice posting.
- Current-version behavior: the documentation states the Perpetual pattern now "impacts the stock valuation account at the invoice level," with the stock-movement-level entries no longer posted individually in real time; a closing-entry mechanism reconciles the remainder.

Evidence: `Reference ERP official documentation — Inventory Valuation / Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`, cross-checked against `Reference ERP official documentation — Automatic Inventory Valuation Configuration, version 18.0, retrieved 2026-09-02` (which still describes the pre-change, movement-level real-time posting behavior) and `Reference ERP official documentation — Inventory Valuation Configuration, version 13.0, retrieved 2026-09-02` (earliest version checked, same movement-level real-time posting behavior, under the label "Automated Inventory Valuation").

**Fact status: PROVISIONAL.** This finding is drawn from documentation-search retrieval rather than a full line-by-line reading of the current-version page in this session; the wording quoted ("impacts the stock valuation account at the invoice level," "before [the version-19 release], ... posting real-time accounting entries at each stock movement") was returned near-verbatim by the retrieval tool from the current-version cheat-sheet page (vendor/product name redacted per clean-room rule), which raises confidence above a bare paraphrase, but a second independent read is recommended before this delta is treated as closed evidence in files `12`/`13`.

**Consequence for this matrix:** every row that depends on "when does a Perpetual entry post" (Accounting Event Trigger, Inventory Asset Timing, COGS Timing, Close Workload, Reconciliation Burden, Audit Traceability) must be read as version-qualified, not as one universal "Perpetual" behavior. This matrix marks each affected cell with `[pre-19]` / `[19+]` qualifiers rather than asserting a single answer. **This delta must be entered in file `02` (Reference Version Behavior Delta Register) as a first-class entry; it is repeated here only because it is load-bearing for §8.3.**

---

## 4. Master Comparison Matrix

| # | Dimension | Periodic (Layer A evidence) | Perpetual (Layer A evidence) |
|---|---|---|---|
| 1 | Accounting event trigger | Vendor bill posting expenses the purchase "by nature" (no capitalization at receipt); the stock-side entry is generated only by the closing-entry process. | `[pre-19]` Each stock movement (receipt, delivery) posts a real-time entry independent of bill/invoice. `[19+]` The stock valuation account is impacted "at the invoice level" — i.e., vendor bill / customer invoice posting is the trigger, with a closing entry handling residual reconciliation. |
| 2 | Inventory Asset timing | Not updated transaction-by-transaction; the Inventory/Stock Valuation Account is corrected only at stock closing via the Stock Variation Account. | `[pre-19]` Updated at each physical movement. `[19+]` Updated at invoice posting, with movements before invoicing not individually reflected in the asset account until then. |
| 3 | COGS timing | No COGS account is populated transaction-by-transaction under the Periodic pattern; expense-by-nature accounts absorb the vendor bill, and the closing entry adjusts Stock Variation — COGS as a distinct P&L line is a closing-derived figure, not an event-level posting. | Anglo-Saxon-associated pattern: "report expenses when goods are sold (cost of goods sold)." `[pre-19]` COGS recognized at the delivery movement. `[19+]` COGS recognized at customer invoice posting (evidence: current-version wording ties the Perpetual entry to "the invoice level" without carving out a separate delivery-level COGS post). **HOLD**: whether `[19+]` fully eliminates a delivery-triggered COGS entry in all configurations (e.g., invoice policy "on delivered quantities" vs "ordered quantities") is not yet independently verified in this session — see §7. |
| 4 | Purchase expense timing | Expense-by-nature account debited when the vendor bill is posted (Continental pattern: "the cost of a good is taken into account as soon as the product is received in stock" is the conceptual framing found in the earliest version checked, but the ledger-level expense recognition documented for Periodic ties to bill posting, reconciled at close — see §7 for the residual ambiguity between "received" and "billed" framing across versions). | Vendor bill posts to the Stock Valuation Account (an asset), not an expense account — no P&L expense at purchase time under Perpetual; expense only arises at COGS recognition (row 3). |
| 5 | Stock variation | Central mechanic. A dedicated Variation Account (Continental: expense-type; Anglo-Saxon-with-Periodic: current-asset or expense type per documentation) absorbs the difference between the vendor-bill-driven expense and the physically verified closing stock value, posted only at the closing entry. | Still present but secondary: `[19+]` closing-entry reconciliation exists precisely because invoice-level posting does not automatically equal the physically moved quantity/value; a residual variation is still closed periodically even under Perpetual. `[pre-19]` variation is smaller/rarer because movement-level entries already track physical flow in real time. |
| 6 | Close workload | High. The stock closing process is the sole mechanism that produces the inventory-value-affecting journal entry; every period-end requires deriving closing stock value and posting the variation. | Lower for the value-affecting entries themselves `[pre-19]`, since they already exist in real time; close workload shifts to *reconciliation*, not *generation*. `[19+]` closing workload rises again relative to `[pre-19]` because more of the value-affecting posting logic has moved back toward a period-boundary mechanism (invoice-level plus closing entry), though still lighter than full Periodic since invoice-level postings already carry most of the asset movement. |
| 7 | Reconciliation burden | Between Stock Truth (physical inventory report) and Financial Truth (ledger) is carried entirely by the close: the closing entry *is* the reconciliation act. No native per-transaction reconciliation exists. | `[pre-19]` Reconciliation burden is continuous but small per event (each movement is already booked; the closing entry is mostly a check). `[19+]` Reconciliation burden concentrates again around invoice timing and the closing entry, because physical movement and invoice posting are no longer assumed to coincide. |
| 8 | Late cost (landed cost, late supplier bill) | Absorbed into the next closing entry; because Inventory Asset is not tracked transaction-by-transaction, a late cost simply changes the next period's closing valuation input — no per-unit cost-layer correction is described in the documentation for this pattern. | Landed Costs is a dedicated feature (`Reference ERP official documentation — Landed Costs, version 18.0/19.0, retrieved 2026-09-02`) that posts an additional valuation adjustment journal entry through a configurable default journal, referencing the original vendor bill; this exists specifically because Perpetual already capitalized a value that a late cost must now adjust. A late supplier bill whose price differs from the receipt valuation is handled through a Price Difference Account when Standard costing is used (see file `15`). |
| 9 | Returns | Returns are absorbed into the next stock closing figure; no discrete return-cost-basis mechanic is described for Periodic in the evidence gathered this session. **HOLD** pending file `19`. | Explicit mechanic for Average Cost: `Reference ERP official documentation — Average Price on Returned Goods, version 19.0, retrieved 2026-09-02` states the average cost is **not** automatically recalculated on return — the documentation states the system "does not automatically update the [weighted-average] calculation... because this can potentially create inconsistencies with inventory valuation" (vendor name redacted per clean-room rule) — the return reverses at the average that existed when the goods left, not a newly computed average. FIFO-specific return-layer behavior is deferred to file `19`/`15`. |
| 10 | Negative stock | Not materially distinguished in the evidence gathered — Periodic's closing-entry mechanic operates on a physical-count snapshot, and negative-stock exposure is chiefly a Perpetual/automated-valuation concern per the documentation surveyed. **HOLD.** | Documented and named risk under FIFO with automated valuation: "[the system] compensates the faulty valuation layer valued at an estimated price with the price of future receipts if any... [and] will automatically create a revaluation journal entry to account for the negative inventory utilized in the prior transaction" (`Reference ERP official documentation — Using Inventory Valuation / FIFO costing, version 17.0/18.0, retrieved 2026-09-02`, corroborated by community/support-channel evidence not treated as authoritative here — see file `15` §5 for full negative-stock treatment by method). |
| 11 | Audit traceability | Traceability runs through the physical stock report plus the closing entry; the documentation does not describe a movement-level audit trail feeding the ledger under Periodic — the ledger-level trail effectively starts at the closing entry, which is a materially thinner audit chain than Perpetual's movement-or-invoice-level entries. | `[pre-19]` Each physical movement has a corresponding ledger entry, giving a dense audit trail directly traceable to a stock move. `[19+]` The trail is anchored to invoice posting plus the closing entry, which is a coarser (though still evidenced) chain than `[pre-19]`; this is a materially different audit posture and must not be assumed equivalent across versions. |
| 12 | Migration complexity | Lower ledger-side complexity to *initiate* (no per-movement valuation layer to seed), but the opening-balance certification still requires a verified physical count and a correct opening Variation baseline; historic movement-level provenance is not reconstructable from the ledger alone because it was never posted at that granularity. | Higher migration complexity: cost layers (FIFO) or a running average (AVCO) must be seeded correctly at cutover, and `[19+]` the invoice-level trigger point must be understood correctly or migrated opening entries will misalign with subsequent invoice postings. See file `26` for the full migration/opening-balance requirement; this row states only the comparative shape of the complexity, not a resolved migration design. |
| 13 | Thai SME operational fit | `HOLD / EVIDENCE REQUIRED`. No Thai-specific authoritative evidence has been produced in this file; file `24` owns this evidence and must independently determine which pattern is more consistent with Thai bookkeeping/tax-filing practice, VAT-invoice timing norms, and typical Thai SME accountant workflow (monthly/period close cadence). Do not infer Thai fit from the "Continental = Europe" / "Anglo-Saxon = USA, India" documentation framing — that framing is a reference-vendor generalization, not Thai authoritative evidence, and Thailand is not named in the source material reviewed. | `HOLD / EVIDENCE REQUIRED`. Same caveat applies symmetrically; the reference documentation names the Perpetual pattern as fitting Anglo-Saxon-style jurisdictions without naming Thailand, so no inference toward or away from Perpetual is safe without file `24` evidence. |
| 14 | SaaS / multi-company control | Both patterns are configured at a company-scoped level in the reference ERP (the valuation/costing configuration surface sits under company-scoped Accounting settings and/or product-category records, per Menu A/B evidence — see files `03`/`04`). Periodic's single closing-entry mechanic is simpler to reason about per company but concentrates period-end control risk on the close-initiation and approval step, which must be independently controlled per company/tenant. | Perpetual distributes the value-affecting postings across many more discrete events (`[pre-19]`: every movement; `[19+]`: every invoice), which increases the number of control points needing per-company/tenant policy isolation (account resolution, currency, period lock) but reduces concentration risk on a single closing act. Full multi-company/tenant isolation proof is owned by file `25`; this row states only the comparative control-surface shape. |

---

## 5. Dimension Notes Requiring Explicit Flag

### 5.1 Rows 3–4 — the "received vs billed" ambiguity across versions

The earliest version checked (13.0) frames Continental accounting conceptually as expense recognition "as soon as the product is received in stock," while the Periodic configuration documentation for later versions ties the ledger-level expense posting to **vendor bill posting**, not physical receipt. These are not necessarily contradictory (a well-run Continental/Periodic company may bill and receive close together), but they are not proven identical either. **Fact status: HOLD** — file `12` (Periodic end-to-end model) must resolve, with direct version-matched citation, whether "received" or "billed" is the actual documented Periodic trigger, rather than this file assuming either.

### 5.2 Row 6/7 — close workload is not monotonically lower under Perpetual

A naive assumption that "Perpetual removes closing work" is **not supported** by the evidence gathered. The `[19+]` shift of the trigger from stock-movement to invoice-level, plus the persistent Stock Variation / closing-entry mechanic documented even for Perpetual, shows close workload as version- and configuration-dependent, not categorically lower under Perpetual. This directly informs `JT-03` and must not be pre-decided by this file.

### 5.3 Row 9/10 — return and negative-stock evidence is asymmetric between methods

The Average-Cost return evidence (row 9) and FIFO negative-stock evidence (row 10) were both found under the Perpetual/automated pattern specifically, because these are automated-valuation-layer mechanics; the Periodic pattern's coarser, closing-only mechanic does not appear (in the evidence gathered this session) to expose an equivalent discrete mechanic to observe. This is treated as `UNKNOWN / HOLD` for Periodic, not as evidence that Periodic has no such exposure — a closing-entry-driven pattern still absorbs return and negative-stock effects, just without a documented discrete mechanic.

---

## 6. Reconciliation Identity Cross-Reference

This file does not test the reconciliation identities in governing prompt §14 (Physical Stock, Inventory Value, Cost Release, Periodic COGS Candidate, Cross-System Reconciliation) — that is file `27`'s ownership. It is noted here only that the "Periodic COGS Candidate" identity (`Opening Inventory + Net Purchases - Closing Inventory = COGS`) is the direct accounting expression of Row 3 (COGS timing) under the Periodic pattern, and file `27` must classify it `VERIFIED / CANDIDATE / HOLD` against the same version-qualified evidence used in Row 3 above, not independently of it.

---

## 7. Open Material HOLD / Conflict Items From This File

| ID | Item | Owning file for resolution |
|---|---|---|
| CMP-14-01 | `[19+]` invoice-level Perpetual trigger — is a delivery/dispatch-level COGS entry fully eliminated in every invoicing-policy configuration, or only in the default? | `13` (Perpetual end-to-end model), corroborated by a second independent documentation read |
| CMP-14-02 | "Received" vs "billed" as the true Periodic Continental trigger across versions | `12` (Periodic end-to-end model) |
| CMP-14-03 | Periodic-pattern return cost-basis mechanic (no discrete mechanic found in evidence gathered) | `19` |
| CMP-14-04 | Periodic-pattern negative-stock exposure (no discrete mechanic found in evidence gathered) | `15`, `20` |
| CMP-14-05 | Thai SME operational fit for both patterns — no authoritative Thai evidence produced in this file | `24` |
| CMP-14-06 | Full multi-company/tenant control-surface proof for both patterns | `25` |
| CMP-14-07 | Version-delta entry for the pre-19/19+ Perpetual trigger change must be formally logged | `02` |

---

## 8. JT-03 Explicit Non-Closure Statement

`JT-03` (continuous/perpetual vs periodic valuation timing) is **not closed** by this file. This file supplies comparative, version-qualified evidence only. No dimension in §4 is to be read as a ranking, weighting, or preference. The Joint session convened to resolve `JT-03` must additionally consume file `24` (Thai evidence, currently `HOLD` on rows 13/14 above) before any candidate can be proposed, and must independently verify CMP-14-01 given its load-bearing effect on Rows 1–3 and 6–7, 11.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
