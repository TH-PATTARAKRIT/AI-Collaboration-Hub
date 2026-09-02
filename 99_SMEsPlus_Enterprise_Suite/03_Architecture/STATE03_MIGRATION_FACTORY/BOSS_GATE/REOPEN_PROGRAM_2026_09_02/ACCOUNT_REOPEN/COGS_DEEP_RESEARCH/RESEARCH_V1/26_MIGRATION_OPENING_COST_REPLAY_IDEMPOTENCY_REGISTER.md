# 26 — Migration / Opening Cost Replay Idempotency Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE PARTIAL — CP-08 SCENARIOS 31/32 MAPPED, GAP-FS-08 STILL OPEN, JT-11/G-5 STILL JOINT`

---

## 1. Purpose and Boundary

This file answers governing prompt §10 scenarios 31 and 32 **from the Accounting side only**. It is the financial-truth complement to the Inventory-side idempotency question already carried as `C-02` / `IV-06`, and it does not re-litigate that Inventory-side question. It also does not re-open `JT-11`/`G-5` (opening-balance certification mechanics), which remain Joint and unresolved on exactly how certification is performed — this file treats that certification step as a precondition that must have already occurred before any of the accounting postings discussed below are permitted to fire.

Foundational rule restated: `Inventory emits facts; Accounting decides postings.` A migration/opening run is, structurally, a very large batch of facts arriving at once (or a replay of the same batch). Everything below asks: given a correctly certified opening fact set, how does Accounting avoid posting it twice, and what happens to historical COGS truth that predates the new system entirely.

Three evidence layers are kept separate throughout, per governing prompt §3 and session convention `CV-01`–`CV-04`.

---

## 2. Layer A — Reference ERP Documented Behavior for Opening Inventory Value

### 2.1 Where opening inventory value is configured

Reference ERP official documentation — Inventory Valuation setup (Accounting → Configuration → Settings, Inventory Valuation section), version 19.0, retrieved 2026-09-02: inventory valuation method (two named options, a real-time-triggered mode and a closing-triggered mode), a costing method selector, a **Valuation Account** described as the asset account recording "the financial value of physical stock," a **Variation Account** reached from a link beside the Valuation Account field, and a posting **Journal**. This is the same Menu A surface already evidenced in file `03` of this package; it is restated here only insofar as it is the account set that an opening/initial posting must land on.

### 2.2 How initial/opening stock is entered

Reference ERP official documentation — Set your Initial Stock, version 13.0, retrieved 2026-09-02: opening quantities are entered through an inventory-adjustment surface (bulk, via an adjustment covering all products, or per-product via a quantity-update action on the product form). The documented steps describe **quantity** entry only. The retrieved text of this page does **not** state whether the same action carries a value/cost input, nor does it state whether it produces an accounting journal entry, nor which account any such entry would use. This is recorded as `HOLD / EVIDENCE REQUIRED` — the initial-stock page is quantity-only evidence; it is not proof that the reference system's opening-quantity action is also the opening-value action.

### 2.3 How the go-live sequence is documented

Reference ERP official documentation — Accounting Get Started / opening entries sequence, version 19.0, retrieved 2026-09-02: the documented go-live order is (1) open customer/vendor invoices and bills, (2) opening inventory, (3) opening trial balance, (4) opening bank/credit-card transactions, (5) final validation. The documentation states the opening trial balance must reconcile against two figures pulled from the other imports: the accumulated **inventory count** value and the accumulated **AR/AP open-item** value. It explicitly names transition timing and sequencing as a source of risk, stating that importing opening entries at the wrong time or in the wrong order can produce duplicated values across financial records — the same failure mode scenario 32 exists to test.

The documentation as retrieved does **not** spell out a single canonical mechanism (e.g., a dedicated "Opening Entries" journal type, a reversing-entry convention, or a locking step) that structurally prevents that duplication; it names the risk and prescribes a sequence and a reconciliation check, not a system-enforced control. This is recorded `HOLD / EVIDENCE REQUIRED` as to whether any structural (as opposed to procedural) duplicate-prevention exists for the opening-inventory-value posting specifically.

### 2.4 Community/secondary evidence on the opening-value posting mechanics (non-authoritative)

Reference ERP community forum discussion (secondary, non-authoritative), retrieved 2026-09-02, topic: opening-stock entry and initial-stock-valuation practitioner threads, current-version load-initial-inventory thread: recurring practitioner guidance describes creating a **clearing account** set as the valuation-receiving account on the inventory-adjustment location, so that entering an opening quantity/value posts a debit to the stock Valuation Account and a credit to that clearing account; separately, the accountant imports the opening trial balance with the inventory line debited to the *same* clearing account (not directly to the inventory asset account) so that, once both sides are posted, the clearing account nets to zero and the full value sits correctly in the inventory asset account. This is **not** official documentation. It is retained here only as a labeled community pattern because it is the closest available description of *how* an opening inventory value is prevented from double-counting against a separately-imported trial balance — i.e., it names the two-sided risk (inventory-adjustment posting vs. trial-balance import both trying to claim the same asset balance) that this session's Contract A/B candidates must design against. It must not be cited as authoritative reference-system behavior and must not be copied into SMEsPlus design as architecture (clean-room boundary, governing prompt §3).

### 2.5 Version delta note

The terminology for valuation timing has changed across the retrieved version range (13.0 through 19.0): earlier documentation sets frame the choice as "Automatic" vs. "Manual" inventory valuation; the 19.0 set frames the same choice as "Perpetual (at invoicing)" vs. "Periodic (at closing)," and 19.0 further documents a change in how the perpetual/"automatic" mode posts — moving from posting at each stock movement toward posting at the invoice/bill event with a closing entry covering the remaining timing gap. This delta is already tracked at the programme level in file `02` of this package; it is restated here because it directly affects §3.3 below (an opening-balance posting produced under one version's automatic/perpetual semantics is not guaranteed to be reproducible or replay-safe under another version's semantics if a migration tool is re-run after a version upgrade). No opening-inventory-specific version delta beyond the general perpetual/periodic terminology and timing shift was found in the retrieved pages; this absence is recorded, not assumed to mean no delta exists.

---

## 3. Neutral Business Meaning (Layer A → Meaning)

| Reference Observation | Accounting Meaning | Status |
|---|---|---|
| A Valuation Account holds "the financial value of physical stock" | Opening inventory value must land on the Inventory Asset account (or its designated equivalent), not on an expense or COGS account, because it is a balance-sheet carrying amount, not a period cost | Meaning derived from Layer A; not yet a SMEsPlus decision |
| Opening trial balance must reconcile against the accumulated inventory-count value | The opening inventory value is not free-standing; it is one line of a larger balanced opening trial balance and must be provably equal to the certified inventory count's value, not merely internally consistent | Meaning derived from Layer A + governing prompt §1 target condition |
| Sequencing risk named but no structural duplicate-block documented | The reference system relies on **process discipline** (do this once, in this order) rather than a **system-enforced key** to prevent a duplicate opening posting; this is a documented gap in the reference system, not a control SMEsPlus can inherit by assumption | HOLD — confirms `GAP-FS-08` is real, not hypothetical |
| Community clearing-account pattern nets an adjustment-side and a trial-balance-side entry to zero | Practitioners solve the "two imports claim the same balance" problem with a temporary suspense/clearing account and manual verification that it nets to zero, not with an automated idempotency key | Secondary evidence only; illustrates the problem shape, not a proof of a reference-system solution |

---

## 4. Historical-COGS Continuity Boundary — Stated Plainly

This is stated as a hard boundary, not a design choice, because no evidence anywhere in this package or its inherited sources shows otherwise:

**COGS recognized in the legacy system before cutover is not re-derivable inside the new system.** The new system receives, at most, a certified **opening inventory value** (a balance-sheet carrying amount as of the cutover date) and, if separately provided, historical **P&L summary figures** for comparative reporting. It does not receive — and under this session's evidence, has no documented mechanism to receive — the transaction-level purchase, receipt, and cost-layer history that would let it *recompute* what COGS was in any pre-cutover period. Any pre-cutover COGS figure appearing in SMEsPlus after go-live is therefore either:

1. a **carried, static number** taken as given from the legacy system's own financial statements (comparative-period reporting only, never recomputed), or
2. **absent** for periods before cutover, with the opening inventory value serving only as the starting point for post-cutover COGS.

This matches the reference-system evidence at §2.3: the go-live import model treats the trial balance (a point-in-time balance set, inventory value included) as the transition artifact — it is documented as a balance to be matched, never as a derivation engine that reconstructs prior-period flow from opening and closing balances. Treating the opening balance as if it lets SMEsPlus *retroactively* generate pre-cutover COGS would be inventing a capability with no evidence behind it, prohibited under governing prompt §22 ("No fabricated cost"). This boundary statement is a required input to Teach-Back question 9 (file `32`) and to the Periodic COGS candidate identity tested in file `27` §6.

---

## 5. Accounting-Truth Idempotency — Distinct From `C-02`/`IV-06`

### 5.1 Why this is a separate question from the Inventory-side one

`C-02`/`IV-06` (per Inventory Final Solution v1.0, challenge lane V-4) asks whether a **movement fact** can be replayed without Inventory recording it twice — a Stock Truth question, answered (or held, per `T-1`) inside the Inventory package. This file asks a structurally different question: even if Inventory guarantees each fact is emitted exactly once (or that a duplicate fact is recognizable as such), **does that guarantee, by itself, guarantee no duplicate posting on the Accounting side?** The evidence says no, for three reasons found in this package's own inherited material and in Layer A:

1. **Cardinality mismatch.** Under the Periodic model (file `12`), Accounting does not post one journal entry per movement fact at all — it posts one aggregate closing entry per period, covering the net variation across many facts (§2.1, §2.3 above; also the reference-system cheat-sheet wording retrieved for file `27` §5: the closing entry "account[s] for the difference between what has been invoiced and received/delivered"). A migration/opening run that is safely idempotent at the fact level can still be posted twice at the *aggregate* level if the closing/opening posting step itself is re-run — the fact-level guarantee does not propagate automatically to the posting-level guarantee.
2. **Two independent import streams claiming one balance.** §2.4 (Layer A community evidence) shows the reference system's own practitioner base treating "opening inventory value" and "opening trial balance" as two separate imports that must be reconciled against each other, not one atomic operation. A migration architecture that lets these run on separate schedules or separate retries has two independent duplication surfaces, not one.
3. **No provenance reference exists yet (`GAP-FS-08`).** Per file `01` §3.3, a migration provenance reference — something that would let a retried replay be recognized by Accounting as "the same fact already posted" rather than "a new fact" — does not currently exist in either the Inventory or the Accounting design. Until it exists, Accounting-side idempotency cannot be *implemented*, only *designed for*.

### 5.2 What "safe from an accounting-truth perspective" would require (candidate requirements, not a decision)

These are Layer C candidates only — none is authorized, none may be treated as decided:

| # | Candidate requirement | Rationale | Status |
|---|---|---|---|
| `AC-01` | A posting-level idempotency key distinct from any Inventory movement-fact key — e.g., a `(migration batch reference, target period, posting purpose)` tuple attached to the journal entry itself, checked before any opening/migration posting is created | Addresses §5.1 point 1: the unit of posting (a batch/period aggregate) is not the same unit as the unit of fact (a single movement), so the idempotency key must live at the posting's own grain | CANDIDATE |
| `AC-02` | A single, atomic "opening set" concept that binds the opening-inventory-value posting and the opening-trial-balance posting together, rather than two independently retriable imports | Addresses §5.1 point 2 — removes the two-stream race the reference system's own community solves manually with a clearing account | CANDIDATE |
| `AC-03` | Reversal-only correction: a mis-posted or duplicate opening/migration entry is corrected by a dated reversing entry referencing the original, never by deletion or in-place edit | Consistent with the audit-trail expectation already implicit in `JT-12` (period lock/backdating) and with ordinary journal-entry integrity; no evidence found that the reference system does otherwise for posted entries | CANDIDATE |
| `AC-04` | The posting-level idempotency key must be checked and enforced by Accounting at the moment of posting, independent of whether Inventory's own fact-level guarand (`C-02`) is resolved as mandatory or as blocking-only-for-automated-paths (`T-1`) | Makes the Accounting-side control self-sufficient rather than dependent on how `T-1` is eventually ruled — Accounting cannot assume Inventory will always hand it a deduplicated stream | CANDIDATE — directly informs §6 |
| `AC-05` | The migration provenance reference required to make `AC-01`/`AC-02` implementable is designed jointly with Inventory, closing `GAP-FS-08`, before any automated migration/replay path is built | Names the actual blocking gap rather than assuming it will be solved incidentally elsewhere | HOLD / JOINT — this is the single most material open item this file surfaces |

None of `AC-01`–`AC-05` may be read as approved design. They are candidate shapes offered so the future Joint session has a starting vocabulary, per Contract C in file `31`.

---

## 6. Interaction With `T-1` (Idempotency: Mandatory Invariant vs. Blocking-Only-for-Automated-Paths)

The Inventory package carries two positions still unreconciled by Boss ruling: challenge lane V-4 treats movement idempotency as a mandatory invariant everywhere; challenge lane S-4 argues it is blocking only for automated/migration paths (i.e., a manually-entered, human-reviewed correction does not need the same machine-enforced guarantee a bulk migration replay needs). This file's Accounting-side evidence does not resolve `T-1` — that remains Inventory/Joint territory — but it does narrow what Accounting needs regardless of how `T-1` is ruled:

- If `T-1` is ruled in V-4's favor (mandatory everywhere), Accounting's `AC-01`–`AC-04` candidates are still required, because — per §5.1 point 1 — even a universally-idempotent Inventory fact stream does not make the Periodic-model *aggregate posting* automatically idempotent.
- If `T-1` is ruled in S-4's favor (blocking only for automated/migration paths), Accounting's candidates become *more* load-bearing, not less: a manual correction path with weaker Inventory-side guarantees increases the chance that Accounting receives an unflagged duplicate fact, so the posting-level key in `AC-01` becomes the last line of defense rather than a redundant one.

Either way, this file's conclusion is: **Accounting cannot outsource its own duplicate-posting risk to however `T-1` is eventually decided.** This is offered as evidence to the Joint session, not as a pre-emptive ruling on `T-1` itself.

---

## 7. Layer B — Thai Evidence Pointer

Opening-balance certification against the accountant's opening trial balance (both quantity and value) is the exact subject of `JT-11`/`G-5`, already flagged Joint/unresolved in the governing material this session inherits (file `01` §3.2). This file does not independently research Thai statutory certification requirements; that track is owned by file `24` (Thai Accounting/Tax/Audit Evidence Register) of this package. Any statement in this file about "certified opening balance" assumes, without proving, that file `24` and the eventual `JT-11`/`G-5` resolution establish what "certified" must mean procedurally and evidentially in a Thai SME context. This is recorded `HOLD — pointer to file 24` and must not be read as this file asserting a Thai requirement on its own authority.

---

## 8. Scenario 31/32 Evidence Mapping

| Scenario | What must be true (Accounting side) | Evidence basis | Status |
|---|---|---|---|
| 31 — Migration/opening inventory replay | A single certified opening inventory value posts once to the Inventory Asset account with an offsetting entry that nets against the separately-imported opening trial balance without residual balance in any suspense/clearing account | §2.1–§2.4 (Layer A + secondary), §4 (continuity boundary) | CANDIDATE structure only; no SMEsPlus posting design exists yet — `HOLD` on implementation |
| 31 — Historical COGS continuity | Pre-cutover COGS is carried as a static comparative figure or is absent; it is never recomputed from the opening balance | §4 | Stated as a boundary; `VERIFIED` as a logical necessity given available evidence, not as a design decision |
| 32 — Retry/idempotency/replay, no duplicated COGS or Inventory Value | Requires a posting-level idempotency key (`AC-01`) distinct from the Inventory fact-level key, plus an atomic opening-set binding (`AC-02`), plus a migration provenance reference closing `GAP-FS-08` | §5, §6 | `HOLD / EVIDENCE REQUIRED` — the mechanism does not exist yet; only candidate requirements exist |
| 32 — No duplicated COGS specifically | Because the opening posting lands on Inventory Asset, not on COGS/expense (§3), a duplicated *opening* posting duplicates Inventory Value and equity/suspense, not COGS directly — but a duplicated **closing/periodic** posting (§5.1 point 1) can duplicate COGS, since the Periodic closing entry is where the expense-side variation is recognized | §2.1, §5.1 | CANDIDATE distinction — narrows where the real COGS-duplication risk sits (closing entries, not the one-time opening entry) |

---

## 9. Open HOLD / JOINT Register (This File)

| ID | Item | Type | Routed To |
|---|---|---|---|
| `H-26-01` | Whether the reference system's initial-stock quantity action also carries a value/cost input, and what account any resulting entry uses | `HOLD / EVIDENCE REQUIRED` | Further Layer A research if needed before COGS Final Solution |
| `H-26-02` | Whether the reference system has any structural (system-enforced) duplicate-import block for the opening-inventory-value posting specifically, beyond documented sequencing discipline | `HOLD / EVIDENCE REQUIRED` | Further Layer A research |
| `H-26-03` | `GAP-FS-08` — migration provenance reference does not exist | `HOLD / JOINT` — **most material open item in this file** | Joint Accounting × Inventory design session |
| `H-26-04` | `AC-01`–`AC-05` candidate requirements | `CANDIDATE` only, not decided | File `31` Contract C; future Joint session |
| `H-26-05` | `T-1` (idempotency mandatory vs. automated-path-only) | `HOLD / JOINT` — inherited, not resolved here | Inventory/Joint track |
| `H-26-06` | `JT-11`/`G-5` opening-balance certification mechanics | `HOLD / JOINT` — inherited, not resolved here | Joint track; Thai evidence in file `24` |

---

## 10. Contract and Veto Touchpoints (Forward Pointers, Not Executed Here)

This file does not run the 9-Veto Council or write Contracts A/B/C — those are files `28` and `31` respectively — but two touchpoints are material enough to flag now so they are not lost between files:

- **Clean-Room/IP/Provenance VETO (veto 8).** The community clearing-account pattern at §2.4 is Layer-A-adjacent secondary evidence, not official documentation, and must be carried into file `28` labeled exactly as it is here — a problem-shape illustration, never a copied architecture. Any SMEsPlus candidate account structure that happens to resemble a "clearing account between two imports" must be independently justified from the accounting-truth reasoning in §5, not cited back to the reference system's community pattern as its source of authority.
- **AI Control/Human Oversight VETO (veto 9).** `AC-01`–`AC-05` are, by design, silent on *how* a migration/opening posting is triggered — whether by a human-run one-time script, a scheduled job, or an AI-assisted migration tool. Whatever triggers it, the posting-level idempotency key (`AC-01`) and the reversal-only correction rule (`AC-03`) must be enforced identically regardless of trigger, so that no automated or AI-assisted replay path is held to a weaker duplicate-posting standard than a human-run one. This directly narrows the accounting-side reading of `T-1` given in §6: even if Inventory's `T-1` is eventually ruled to bind only automated/migration paths, Accounting's own posting-level control in this file applies uniformly and does not vary by trigger type.

Contract B (COGS Recognition Contract, file `31`) must additionally state, as a direct consequence of §4 above, that a migration/opening run **never** originates a COGS posting — only an Inventory Asset (and matched suspense/equity-side) posting. Any COGS-labelled amount appearing in a migration context is therefore either a carried comparative figure (§4 option 1) or a defect, never a legitimate migration-time recognition event. This is offered as a candidate contract clause, not a decision.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
