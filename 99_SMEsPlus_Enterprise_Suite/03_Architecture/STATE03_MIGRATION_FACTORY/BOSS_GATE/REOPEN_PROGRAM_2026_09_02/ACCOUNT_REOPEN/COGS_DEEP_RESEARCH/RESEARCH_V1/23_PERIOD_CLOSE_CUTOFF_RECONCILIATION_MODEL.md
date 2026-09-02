# 23 — Period-End Closing / Cut-Off with Unbilled Receipts and Uninvoiced Deliveries — Reconciliation Model

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `Layer A evidence gathered (reference ERP official documentation, versions 15.0–19.0). Layer B = HOLD, owned by file 24. Layer C = CANDIDATE/HOLD only. No Boss decision, no PASS, no gate closure implied.`

---

## 1. Scope and Question Fingerprint

This file answers Question 13 of the fingerprint register (`01_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` §5) and Scenario 30 of the governing prompt §10 ("Period-end closing / cut-off with unbilled receipts and uninvoiced deliveries"). It feeds evidence toward `JT-06` (late supplier bill after period close), `JT-07` (period close design and snapshot content), and `JT-12` (period lock policy and backdating exception grants). None of `JT-06`/`JT-07`/`JT-12` is closed here — this file supplies evidence, not a decision.

The prior Inventory-side design (already fixed, not re-litigated) is:
- Inventory owns a native period guard enforced **at movement entry and at movement validation**.
- Accounting supplies the lock date consumed by that guard.
- An exception path exists, requiring: a named grantor, a written reason, an expiry date, and a permanent record.
- A global bypass toggle is explicitly **REJECTED** as unauditable.
- Late-arriving cost after close is an explicitly **unresolved** Joint item (`JT-06`).

This file's job is to test that design against what the reference ERP's own documentation shows an accounting close actually needs, and to state plainly where a gap remains rather than assume the guard is sufficient.

---

## 2. Layer A — Reference ERP Observed Behavior

### 2.1 Version delta — the close/cut-off model changed shape across versions

Two materially different architectures were observed and must not be silently merged:

**Pre-19 architecture ("Automatic" vs "Manual" valuation, Continental vs Anglo-Saxon):**
- `Manual` valuation (also documented as Periodic): the accounting team posts journal entries based on a physical inventory count; the accounting team, not the system, determines the closing inventory value. Products default to a `Standard Price` costing method.
- `Automated` valuation (Perpetual under the older label): the system updates inventory value in real time by creating a journal entry on every stock move between locations, independent of vendor bill or customer invoice timing.
- Under `Anglo-Saxon` accounting, costs are recognized when goods are sold/delivered; `Stock Input Account` and `Stock Output Account` are distinct current-asset accounts.
- Under `Continental` accounting, costs are recognized as soon as goods are received into stock; `Stock Input` and `Stock Output` use the **same** current-asset account.
- Evidence: `Reference ERP official documentation — Inventory valuation configuration (Automatic/Manual, Continental/Anglo-Saxon), version saas-16.4, retrieved 2026-09-02`.

**Version-19 architecture (renamed "Perpetual (at invoicing)" vs "Periodic (at closing)"):**
- `Periodic (at closing)`: inventory valuation updates only during a stock-closing process; physical movements are tracked in the Inventory Stock report but are **not** automatically synchronized to the financial books between closes. The expense account is debited when the vendor bill posts, not when the goods are received.
- `Perpetual (at invoicing)`: this is the renamed, redesigned successor to the old "Automated" behavior. It no longer posts at every stock move. It now posts the stock valuation account **at the invoice/bill level**. The closing entry is repositioned to manage the residual gaps: bills to receive, invoices to issue, deferred revenue, prepaid expenses, and other timing differences between the inventory ledger and the accounting ledger.
- Evidence: `Reference ERP official documentation — Inventory valuation (Periodic vs Perpetual, closing entries), version 19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02`.

**Version-delta consequence for this session:** an old "Automatic valuation posts at every stock move" mental model must not be carried forward unexamined into a v19-labelled "Perpetual" read — the two behave differently at the exact point (receipt/delivery vs invoice/bill) this scenario cares about. Any SMEsPlus candidate design must state, explicitly, which of the two postures (event-triggered-at-movement vs event-triggered-at-invoice-with-closing-catchup) it is drawing from, rather than blending them.

### 2.2 Field evidence — close/cut-off-relevant fields

| Field | Menu Path (observed) | Purpose | Values / Options | Default | Scope | Account Type Impact | Version Delta | Evidence | Fact Status |
|---|---|---|---|---|---|---|---|---|---|
| Valuation Method | Accounting → Configuration → Settings → Inventory Valuation | Chooses whether financial recognition tracks physical movement or invoice/bill posting | Perpetual (at invoicing) / Periodic (at closing) | UNKNOWN (localization-dependent) | Company-scoped setting (see file 25) | Determines when Inventory Asset / COGS accounts move | Renamed and re-mechanized in v19 vs pre-19 Automatic/Manual (§2.1) | `Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02` | VERIFIED (current label), CONFLICTING (mechanism vs pre-19) |
| Periodic Valuation (automation) | Same menu | Sets cadence of the closing/catch-up entry | Manual / Daily / Monthly | UNKNOWN | Company-scoped | Triggers closing entry generation | Not observed pre-19 in this form | `Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02` | PROVISIONAL |
| Stock Input Account / Stock Interim (Received) | Product Categories → Accounting; Balance Sheet nesting under Current Assets | Interim asset capturing a receipt before the vendor bill exists — the GRNI position | Any current-asset account | UNKNOWN | Category-level, product-overridable | Current Asset (interim) | Present pre-19 and post-19, but the *closing* logic that clears it changed (§2.1) | `Reference ERP official documentation — Inventory valuation configuration, version saas-16.4, retrieved 2026-09-02`; `Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02` | VERIFIED (existence), HOLD (clearing mechanics detail) |
| Stock Output Account / Stock Interim (Delivered) | Same | Interim asset/contra capturing a delivery before the customer invoice exists — the GDNI position | Any current-asset account | UNKNOWN | Category-level, product-overridable | Current Asset (interim) or Expense depending on posture | Same caveat as above | Same as above | VERIFIED (existence), HOLD (clearing mechanics detail) |
| Bill Control (3-way match policy) | Purchase → Configuration → Settings → Invoicing; Vendor Bill Control policies doc | Governs whether a vendor bill can even be drafted from ordered quantity or only from received quantity | On ordered quantities / On received quantities | Set per install, applied to new products; existing products keep prior value | Company default, product-overridable | Determines which population is "unbilled" at cutoff | No material delta observed 15.0–19.0 | `Reference ERP official documentation — Bill control policies (Control policies), versions 16.0–19.0, retrieved 2026-09-02` | VERIFIED |
| Invoicing Policy | Product form → Sales; visible when Sales app installed | Governs whether a customer invoice can be drafted at order confirmation or only after delivery | Ordered quantities / Delivered quantities | "Ordered quantities" is the commonly documented default; product-level field only appears once the product is a sale-type product | Product-level, category-independent | Determines which population is "un-invoiced" at cutoff | No material delta observed 14.0–19.0 | `Reference ERP official documentation — Invoicing policies, version 19.0, retrieved 2026-09-02` | VERIFIED |
| Lock Dates (Sales/Purchase entries, Hard Lock) | Accounting → Accounting → Lock Dates | Prevents posting/editing journal entries on or before a date | Date fields per lock type; Hard Lock is irreversible | UNKNOWN | Company-scoped | Controls whether a late bill/invoice can post into the closed period at all | Structure (exception mechanics) most fully documented at v18–19 | `Reference ERP official documentation — Year-end closing, version 19.0, retrieved 2026-09-02` | VERIFIED |

No blank material cells: `UNKNOWN`/`HOLD` used where the fetched documentation excerpts did not state a value.

### 2.3 What an "unbilled receipt" looks like in the reference documentation

A vendor bill's existence is gated by the Bill Control policy (§2.2). Under `On received quantities`, a bill literally cannot be drafted until goods are received — the system will error. This means the population of "receipt exists, bill does not" is a first-class, queryable state in the reference design: every received line sits in the interim/`Stock Input` position until a bill is created against it. Under `On ordered quantities`, the bill can precede the receipt, producing the mirror-image cutoff case (bill exists, receipt does not) — the reference documentation frames this as the counterpart to 3-way matching, which exists specifically to stop payment until receipt quantities are confirmed.

Evidence: `Reference ERP official documentation — Manage vendor bills, versions 15.0–19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Bill control policies, versions 16.0–19.0, retrieved 2026-09-02`.

### 2.4 What an "uninvoiced delivery" looks like in the reference documentation

Symmetrically, a customer invoice's existence is gated by the product's Invoicing Policy. Under `Delivered quantities`, the documentation is explicit: once the sales order is confirmed, "you cannot create the invoice without delivering the product to the customer" — the delivered-but-not-invoiced population is structurally unavoidable for any business using this policy, and is exactly the interim `Stock Output` position until the invoice posts. Under `Ordered quantities`, the invoice can be raised at order confirmation before delivery happens, producing the mirror case.

Evidence: `Reference ERP official documentation — Invoicing policies, version 19.0, retrieved 2026-09-02`.

### 2.5 The closing entry mechanism

The v19 documentation states the closing entry's job directly: it "manages bills to receive, invoices to issue, deferred revenues, prepaid expenses, and other gaps between inventory values and accounting ones." This is the single most direct piece of Layer A evidence that the reference treats period-end unbilled-receipt / uninvoiced-delivery cutoff as **an Accounting-owned closing procedure**, not as a byproduct of the inventory movement guard. The pre-19 architecture reaches a structurally similar place from the opposite direction: under `Periodic (Manual)` valuation, the *entire* inventory value is only ever brought into the books at closing, via a stock-variation account that is explicitly described as capturing the difference between the accounting books and the physical inventory as of the close date.

Evidence: `Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02`.

### 2.6 Lock dates, exceptions, and reopening

- A lock date, once set, blocks both edits to existing entries dated on/before it and new postings dated on/before it; an attempted new posting on/before the lock date has its accounting date automatically shifted to the day after the lock date rather than being silently accepted at the original date.
- An administrator can create a **temporary exception**: the lock is removed, and the exception is explicitly scoped — to the current user, or to everyone — for a stated duration, with an optional reason, and the grant is logged against the company record as an auditable event.
- A separate **Hard Lock** date exists and is documented as irreversible, specifically to meet statutory inalterability requirements in certain countries — once set, it cannot be unlocked at all, not even via the exception mechanism above.

Evidence: `Reference ERP official documentation — Year-end closing, version 19.0, retrieved 2026-09-02`.

**Divergence flagged, not adopted:** the reference's "everyone" exception scope is structurally close to the global bypass toggle the Inventory-side design already rejected as unauditable. This session does not adopt it. The reference's "current user + reason + duration + logged" exception variant, by contrast, is structurally consistent with the Inventory-side design already in force (named grantor, written reason, expiry, permanent record) — it is corroborating Layer A evidence for a design SMEsPlus already committed to, not a new input. The reference's two-tier soft-lock/exception vs. irreversible Hard Lock split is **not** present in the Inventory-side design as described to this session, and is surfaced below as Layer C candidate material for `JT-12`, not as something already decided.

---

## 3. Layer B — Thai Cut-Off / Physical-Count Evidence

`HOLD.` File 24 (`24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md`) owns authoritative Thai evidence on period cut-off and physical stock evidence per the governing prompt §13. This file does not assert Thai statutory content. It records only the pointer obligation: whatever Thai authoritative rule exists for physical stock-count evidence at cut-off (and any `TH-HOLD-*` item already carried from the Inventory package, per `01_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` §3.3) must be read against §5 below before any candidate in this file is treated as more than provisional. No Thai statutory claim is made or implied in this file.

---

## 4. Layer C — Neutral SMEsPlus Candidate Semantics

All entries below are `CANDIDATE` or `HOLD` only. None is a decision; none closes `JT-06`, `JT-07`, or `JT-12`.

| Candidate ID | Statement | Status | Depends On |
|---|---|---|---|
| `L23-C01` | An "unmatched valuation fact" is a neutral, non-vendor-specific way to describe both the unbilled-receipt and the uninvoiced-delivery cutoff population, expressed as an Inventory-emitted fact (consistent with the `HX-07`/`HX-08`/`HX-09` vocabulary already fixed in the Inventory package) that has not yet been paired with a billing/invoicing fact. | CANDIDATE | `HX-07`, `HX-08`, `HX-09`, `JT-06` |
| `L23-C02` | A two-tier lock — a reversible lock with a scoped, logged exception, plus a separate irreversible hard lock usable once a period is statutorily filed — is worth evaluating for the Inventory-side period guard and the Accounting lock-date supply relationship, informed by §2.6. | CANDIDATE | `JT-12` |
| `L23-C03` | The reference's "everyone" exception scope is explicitly **not** carried forward; only the named-user + reason + expiry + logged variant is retained as consistent with the existing rejection of a global bypass toggle. | CANDIDATE (restatement of an existing rejection, not a new one) | `JT-12` |
| `L23-C04` | The closing entry / catch-up procedure that clears unmatched valuation facts into the correct financial period is an **Accounting-owned** procedure that consumes Inventory facts; it is not something the Inventory-side movement guard produces on its own. | CANDIDATE | `JT-07` |

---

## 5. Reconciliation with the Inventory-Side Period Guard — Gap Analysis

### 5.1 What the guard already guarantees (recap, not re-opened)

The Inventory-side period guard, as already fixed, guarantees: (a) a movement cannot be entered or validated with an effective date on/before the Accounting-supplied lock date, except through the named-grantor/reason/expiry/permanent-record exception path; (b) there is no global bypass. This is a **control over when a physical/valuation fact may be dated**, enforced at the point of fact creation.

### 5.2 What Accounting still needs at close that the guard, by itself, does not supply

Section 2 shows the reference ERP's own closing procedure does three things a pure movement-date guard does not:

- **GAP-1 — Population query surface.** The reference's closing entry must be able to enumerate, as of the close date, every receipt without a matching bill and every delivery without a matching invoice (§2.3, §2.4, §2.5). A guard that blocks backdated movement entry says nothing about whether Inventory exposes an as-of-date query for "valuation facts with no paired billing/invoicing fact." Whether this query surface exists in the Boss-approved 16-field Inventory → Accounting Minimum Handoff Data Contract is `UNKNOWN` to this session — that contract was verified present on branch but its field-by-field content was not re-opened here (per `01_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` §2). **This is flagged as a material open item, not assumed resolved.**
- **GAP-2 — Accounting-date authority for late-arriving cost.** The guard prevents a *movement* from being backdated into a closed period. It says nothing about which period should absorb the *financial* effect when a bill or invoice for an already-closed, already-guarded movement arrives afterward. The reference's own answer (§2.5) is that the closing entry's job is precisely to manage "bills to receive, invoices to issue" gaps — i.e., a second, Accounting-owned decision layer sits on top of the movement-date guard. This is exactly the scope of `JT-06`, and `JT-06` is explicitly still unresolved. The movement guard being fully in force does **not** by itself resolve `JT-06`; it only ensures the physical fact's own date is not falsified. The decision of which financial period a late bill lands in remains open.
- **GAP-3 — Closing snapshot ownership and content.** The reference documentation (§2.1, §2.5) shows both architectures culminate in a closing artifact (a closing entry, or a stock-variation posting) that is the actual reconciling instrument between physical stock and the books. Whether Inventory emits a frozen, versioned closing-valuation snapshot fact (per `HX-17` in the existing Inventory handoff register) that Accounting's period close consumes, or whether Accounting is expected to compute this independently from live Inventory queries at close time, is the substance of `JT-07` and is explicitly not decided by this file.

### 5.3 Explicit non-assumption

This file does **not** conclude that the Inventory-side period guard is sufficient for an Accounting close, and does not conclude that it is insufficient by some specific missing feature that can be named with certainty — only that the reference ERP's own documented close procedure requires more than a movement-date block, and that the "more" (population query surface, late-cost period authority, snapshot ownership) maps directly onto `JT-06` and `JT-07`, both of which remain open per the governing prompt and the prior evidence index. Treating the guard as close-ready would be an unproven assumption; this file declines to make it.

---

## 6. Reconciliation Identities Challenged (Governing Prompt §14)

| Identity | Applicability to This Scenario | Classification | Notes |
|---|---|---|---|
| Physical Stock: `Opening Qty + Valid Inflows − Valid Outflows +/− Controlled Adjustments = Closing Qty` | Applies to the receipt and delivery events underlying scenario 30 | CANDIDATE | Depends on the Inventory-side movement guard already in force; not independently re-verified in this file. |
| Inventory Value: `Opening Value + Capitalizable Cost Added − Cost Released +/− Approved Valuation Adjustments = Closing Value` | Directly implicated — an unbilled receipt still adds capitalizable cost (at receipt-time provisional cost) before a bill fixes the final figure; an uninvoiced delivery still releases cost before revenue is recognized | HOLD | Whether the provisional receipt cost and the final billed cost reconcile through a price-difference mechanism at close is out of this file's scope (see `21_LANDED_COST_LATE_COST_PRICE_DIFFERENCE_RESEARCH.md`); flagged, not resolved, here. |
| Cost Release: `Inventory Cost Released → COGS OR another explicitly approved financial classification` | Applies once a delivery event releases cost before the matching invoice exists | HOLD | Depends on `JT-04` (COGS recognition timing) resolution, not re-litigated here. |
| Periodic COGS Candidate: `Opening Inventory + Net Purchases/Capitalizable Costs − Closing Inventory = COGS` | Only meaningful under the Periodic posture (§2.1); an unbilled receipt or uninvoiced delivery at the closing date directly distorts both the "Net Purchases" and "Closing Inventory" terms unless the closing entry correctly captures the interim position | CANDIDATE | Reference evidence (§2.5) supports this identity's mechanics under Periodic; Thai acceptability of the resulting figure is Layer B / file 24, `HOLD` here. |
| **Cross-System Reconciliation**: `Inventory valuation as-of-date ↔ Accounting inventory balance + fully explained reconciling items` | This is the identity scenario 30 exists to stress-test | HOLD | Per §5.2 GAP-1/GAP-3, this session cannot confirm the "fully explained reconciling items" set is actually enumerable end-to-end without the population-query surface and the snapshot-ownership question being answered by `JT-06`/`JT-07`. Reference evidence shows the reference ERP treats this identity as requiring an explicit closing procedure (§2.5), not as something that holds automatically from movement-level controls alone — which is consistent with, and reinforces, the GAP-1/GAP-3 finding above rather than resolving it. |

---

## 7. Scenario 30 Evidence Table — Periodic and Perpetual

| Sub-Case | Periodic Posture (reference evidence) | Perpetual Posture (reference evidence) | SMEsPlus Candidate/HOLD |
|---|---|---|---|
| Receipt before bill, period closes with no bill | Receipt has no accounting effect until the closing entry values the physical stock; the interim position is implicit in the physical count, not in a running interim account | Receipt sits in `Stock Input`/interim-received position (pre-19) or awaits invoice-level posting with the closing entry covering "bills to receive" (v19) | HOLD — pending `JT-06`/`JT-07` |
| Bill before receipt, period closes with no receipt | Bill is expensed/capitalized per policy; physical count at close will not show the goods, creating a variance the closing entry must explain | Bill posts; valuation is not corroborated by a physical receipt fact yet | HOLD — pending `JT-06` |
| Delivery before invoice, period closes with no invoice | Physical stock reduction only surfaces at the next physical count/closing entry | Delivery sits in `Stock Output`/interim-delivered position (pre-19) or awaits invoice-level posting with the closing entry covering "invoices to issue" (v19) | HOLD — pending `JT-04`/`JT-06`/`JT-07` |
| Invoice before delivery, period closes with no delivery | Revenue/expense recognized on invoice per policy; physical count will not show the reduction, creating a variance the closing entry must explain | Invoice posts; COGS release is not corroborated by a physical delivery fact yet | HOLD — pending `JT-04`/`JT-06` |

No journal entry, account code, or cost figure is asserted for SMEsPlus in this table, per the governing prompt's hard rule against fabricated postings.

---

## 8. Cross-Reference Table

| Joint/Risk ID | Status Entering This File | This File's Contribution |
|---|---|---|
| `JT-06` — Late supplier bill after period close | Unresolved (Inventory Final Solution v1.0, restated in `01`) | Confirms via Layer A evidence (§2.5, §5.2 GAP-2) that the reference ERP treats this as requiring an explicit Accounting-owned closing decision layer beyond the movement-date guard; does not resolve it |
| `JT-07` — Period close design and snapshot content | Unresolved | Confirms via Layer A evidence (§2.1, §2.5, §5.2 GAP-3) that a closing artifact (entry or snapshot) is structurally necessary in both postures observed; does not decide who computes/owns it |
| `JT-12` — Period lock policy and backdating exception grants | Unresolved | Supplies corroborating Layer A evidence for the already-fixed named-grantor/reason/expiry/logged exception design (§2.6) and a candidate two-tier soft/hard lock idea (`L23-C02`); does not decide either |
| `HX-07`/`HX-08`/`HX-09` | Existing Inventory handoff rows (receipt, bill-vs-cost, issue/COGS facts) | `L23-C01` proposes mapping the cutoff population onto these rows rather than a new vocabulary |
| `HX-17` — Close valuation summary | Existing Inventory handoff row | Directly implicated by GAP-3; not resolved here |

---

## 9. Open HOLD / Unknown Register (This File)

1. Whether the 16-field Minimum Handoff Data Contract already includes an as-of-date "unmatched fact" query capability (GAP-1) — `UNKNOWN`, contract content not re-opened in this session.
2. Which accounting period absorbs a late-arriving bill/invoice for an already-guarded, already-closed movement — `HOLD`, owned by `JT-06`.
3. Whether the closing artifact is an Inventory-emitted snapshot fact or an Accounting-computed derivation from live queries — `HOLD`, owned by `JT-07`.
4. Whether a two-tier soft/hard lock design is warranted for SMEsPlus — `CANDIDATE` only (`L23-C02`), not decided.
5. Thai statutory acceptability of any Periodic-posture closing-entry mechanic described in §2.5/§2.6/§7 — `HOLD`, deferred to file 24 in full.
6. Price-difference reconciliation between provisional receipt cost and final billed cost at a closing boundary — `HOLD`, deferred to file 21.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
