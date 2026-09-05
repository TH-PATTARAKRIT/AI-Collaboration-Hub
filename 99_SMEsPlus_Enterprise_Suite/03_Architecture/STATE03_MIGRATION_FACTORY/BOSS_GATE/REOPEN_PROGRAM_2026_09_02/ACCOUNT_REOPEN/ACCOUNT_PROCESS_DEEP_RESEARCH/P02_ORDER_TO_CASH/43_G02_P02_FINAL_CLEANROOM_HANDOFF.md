# 43 — G02-P02 FINAL CLEAN-ROOM HANDOFF

`LAYER 1 — CLEAN ROOM.` SMEsPlus business semantics only. **No vendor implementation detail.**

Prompt `[SMEPLUS-26-09-05-G02-P02-O2C-TARGETED-CLOSURE-002]`.
**This is a handoff, not an approval.** Nothing here is frozen, merged, or authorised for build.

---

## 1. What P02 Establishes

**E-1 — Order-to-Cash has two timelines and one bridge, and the bridge is the weakest part.**
The fulfilment side carries **occurrence** dates. The billing side carries **accounting** dates. The
only stage that joins them is **cost recognition** — and across every deployed accounting population
examined, that join has **never executed**. A business fact that has never produced an accounting
effect anywhere is not a working control.

**E-2 — Cost recognition must be a first-class platform rule, not a per-tenant configuration.**
Where cost is recognised is currently decided by settings held on **different objects**, which are not
validated against each other in the direction that matters. One reachable combination recognises cost
**nowhere**, and it was observed in a live business carrying a large inventory value.

**E-3 — Delivered-not-invoiced is a real, aged, unaccounted position.**
Goods leave, the operational record correctly flags the balance as billable, and **the ledger never
learns of it**. Positions were found open for over **two years**. The information exists; it simply
never becomes accounting. **SMEsPlus must carry this as an ageable position with an accounting date.**

**E-4 — Period close must mean closed.**
Closing controls are almost entirely unused across the deployed estate, and an automation that appears
to close periods was found to have **no accounting effect at all**. A close that can be re-opened, or
that never barred anything, is not a close.

**E-5 — The physical record is immutable and the accounting record is not.**
Durability is inverted relative to accounting importance: what happened physically cannot be changed,
while its financial consequence can be reversed, re-dated, or removed.

**E-6 — Scope must be resolved from the record, never from who is asking.**
Configuration that belongs to a company is currently resolved from the acting context. On the newest
reference generation one value is resolved from **two different company sources in a single
expression**. SMEsPlus requires: **missing scope denies; it does not default.**

**E-7 — Every operational total needs an accounting counterpart, and they are different numbers.**
The operational billing counter includes drafts; the accounting counter does not. Measuring the
business on the operational counter **understated the exposure by more than twenty times** and pointed
the conclusion in the wrong direction.

---

## 2. What G02-P10 Receives

- The measured **billing-versus-performance** position, with the caution that it must be segmented by
  each line's billing basis before it is treated as an exposure — billing ahead of delivery is the
  *designed* behaviour for order-based billing.
- **Bill-and-hold** has no representation and needs a policy decision.
- A deployment observed **delivering without ever billing**.
- The open question of who owns the un-invoiced obligation position.

## 3. What G02-P06 Will Later Receive

- Settlement may be split across **many deduction lines chosen at payment time**, reaching accounts not
  fixed by the receivable.
- Certain outbound accounts are configured so that **matching is impossible in principle**.
- Separation of cash, receivable and confirmation currently rests on configuration, not structure.

## 4. What Shared Controls Receive

**Tax / localisation.** Withholding is implemented several times over in the same estate; customer-side
withholding reaches no report. A statutory report prints the accounting date under a heading that says
invoice date. **Every localisation conclusion is generation-bound and must be re-established per
generation.**

**Close / reporting.** The inventory value and the ledger can disagree without detection. Provisions for
returns and warranties do not exist. A large delivered-not-invoiced balance never reaches the close.

**Management accounting.** The analytic dimension does not reliably survive the settlement path.

## 5. What P11 Receives

- Three **scope holds**: currency rate, chart of accounts, intercompany execution.
- Six **design candidates**: obligation position, event identity, two-date model, close-means-closed,
  deterministic account derivation, deny-on-missing-scope.
- The invariant **one business fact → one canonical event owner → one accounting effect path** is
  **not** satisfied by the reference at the correction/reversal stage.

## 6. Boss Decisions

| # | Decision | Status |
|---|---|---|
| 1 | Invoice policy is separate from cost-recognition policy | **Boss policy — preserved, not re-decided** |
| 2 | For perpetual + storable, physical delivery is the cost trigger | **Boss policy — preserved.** Note: the newest reference generation **cannot be configured** to do this, so it becomes a **build requirement** |
| 3 | Revenue on billing versus performance | **OPEN — Boss reserved.** P02 supplies measurement only |
| 4 | One bounded authorisation to reproduce a cost-recognition repeat-execution question in an isolated disposable sandbox | **REQUESTED** |

## 7. Exact Unresolved Dependencies

| # | Dependency | Owner |
|---|---|---|
| 1 | Behaviour of the customised code that overrides sales and inventory in the largest deployments — **unreadable** | Evidence required |
| 2 | Whether the oldest generation enforces the credit limits it has configured | Evidence required |
| 3 | The **value** (not quantity) of the delivered-not-invoiced position | Evidence required |
| 4 | Statutory treatment of withholding and VAT | Tax process + statutory source |
| 5 | Revenue timing | Boss / P10 |
| 6 | Repeat-execution of cost recognition | Boss authorisation |

## 8. Reliance Statement

**P02 is complete to the maximum evidence obtainable without new authority, and it is not a
verification of the reference system.** Its strongest conclusions are those measured directly from
deployed accounting data; its weakest are those derived from reference code that **no deployment
demonstrably runs**. **Twelve of this round's own conclusions were corrected by independent challenge,
four of them against work published in the same round.** Reliance should be placed on the measured
findings and on the design requirements above, not on any statement about how the reference behaves.
