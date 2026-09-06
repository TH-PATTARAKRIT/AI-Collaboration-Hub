# P06_CROSS_PROCESS_OWNERSHIP_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Supersedes:** the *status* column of `09_P06_CROSS_PROCESS_OWNERSHIP.md`. That file's evidence stands; its ownership assignments were made **without reading a single peer package** and are now reconciled against seven of them.

---

## 1. What changed

At prior close, every one of P06's twenty cross-boundary assignments was a **proposal**. Seven peer packages have since been read. This register records, for each fact: P06's proposal, what the peer actually says, and the resulting disposition.

**The most important change is not to any single row. It is to P06's own self-description.**

**CPO2-F-01 — P06 is a producer of accounting events, not a terminal consumer.**
`09_` stated *"P06 owns nothing else."* P11 states the opposite and is right:
> *"Reconciliation is a **producer** of accounting events, not only a consumer. Three accounting events are emitted **by the act of matching** … `P06` is therefore not a downstream consumer of `P02` and `P01`."* — `P11_SETTLEMENT_RECONCILIATION_ARCHITECTURE.md` §1

**P06 accepts the correction.** Three events are emitted by matching: the exchange difference, its reversal on unmatch, and cash-basis tax recognition. P06 **emits** all three and **owns** none — which is precisely the condition that requires each emitted event to name its owning process and its own recognition date.

---

## 2. The register — twenty facts, reconciled

Legend — **Disposition:** `SETTLED` (peer agrees or P06 defers) · `CONTESTED` (two claims stand) · `UNOWNED` (no process claims it) · `OPEN` (~~counterparty unpublished~~ → **no counterparty ruling exists**; every peer branch P01–P10 is published **[REV-E-22, 2026-09-06]**) · `HOLD`.

| # | Fact | P06's prior proposal | Peer position | Disposition |
|---|---|---|---|---|
| F-01 | Customer receivable open item + residual | P02 authors | P02 confirms; adds that a line carries **two** residuals that can diverge under multi-currency | **SETTLED**, with P02's mechanism absorbed |
| F-02 | Vendor payable open item + residual | P01 authors | ~~**P01 unpublished**~~ → **P01 IS PUBLISHED** at `b820b29` (`research/account-p01-procure-to-pay-2026-09-04-001`), verified by `git ls-remote --heads origin`; **NOT CONSUMED by P06** — `P06-OQ-124` **[REV-E-22, 2026-09-06 — stale current claim missed by the round-5 repair pass]** | **OPEN** — `P06-B-54` |
| F-03 | Employee reimbursement obligation | CONTESTED | **P11 `UBE-33` assigns "Employee reimbursed" to P06**; P05 concedes it *"creates and posts payments"* it does not own (`EX-03`, HIGH) | **SETTLED to P06** — and P06 inherits a door P05 operates |
| F-04 | **Payment intent** | CONTESTED, four entry points, no author | P05 confirms a fifth path with **no payment object at all** (`SR-04`) | **CONTESTED — and worse than stated**; see `P06-B-53` |
| F-05 | Payment state | P06 authors (with defect) | P05 `SR-01` independently: *"Settlement status on this branch is an **assumption, not an observation**"* | **SETTLED to P06**, defect corroborated |
| F-06 | Accounting posting state | CONTESTED | ~~P08 unpublished~~ → **P08 PUBLISHED and read** (`53_`); the *decision* is still open **[REV-E-22, 2026-09-06 — stale publication status; all ten peer branches P01–P10 exist on origin, verified by `git ls-remote --heads origin`. NOT CONSUMED — `P06-OQ-124`/`P06-OQ-128`]** | **OPEN** |
| F-07 | **Bank confirmation state** | UNOWNED — no field exists | P11 Delta 01 adopts verbatim: *"bank confirmation state, which has **no field in the system at all**"*; **P02 `P02-F-43` asserts the opposite** | **CONTESTED — `P06-XC-01`**, routed to P11 |
| F-08 | Reconciliation state | P06 authors | P11 and P02 both scope the matching record **COMPANY**, mutate **never** | **SETTLED to P06** |
| F-09 | Invoice payment status | CONTESTED, two writers | P02 supplies the full 7-value enumeration and notes **two values are never assigned by the computation**; P07 shows a statutory consequence (`W-C-02`) | **SETTLED as CONTESTED** — two writers confirmed by two peers |
| F-10 | FX rate applied at settlement | CONTESTED | P11 `DEP-14`: **BOSS DECISION REQUIRED, packaged not decided**; P02 adds a second silent fallback arm | **HOLD — BOSS DECISION**, evidence enlarged |
| F-11 | Realised FX gain/loss amount and account | P-CORE owns, P06 triggers | **P11 `UBE-36`: "the ledger owns this — it is emitted, not requested"** | **SETTLED — P06 does not contest** |
| F-12 | Bank charges and interest | **UNOWNED** | **P10 `X-08` asks P06 directly**; no peer claims it | **UNOWNED — and P06 now answers P10** (see `35_` §6). **The answer is delivered; the dependency is NOT closed — P10 carries it `OPEN — PEER EVIDENCE` at `1fea562` [REV-E-18, 2026-09-06]** |
| F-13 | Withholding tax deducted at payment | HOLD, statutory | **P07 names P06 owner of the payment fact and marks it BLOCKING** (`X-07`, `X-08`, `X-09`); P11 `UBE-39` assigns the *tax* fact to P07 | **SETTLED: P06 owns the payment fact, P07 owns the tax fact.** Statutory HOLD mirrored, not resolved |
| F-14 | Early-payment discount | P02 authors terms, P06 applies | P02 silent on the split | **SETTLED by default**, unopposed |
| F-15 | Cash/bank GL balance | P-CORE | ~~P08 unpublished~~ → **P08 PUBLISHED and read** (`53_`); P08 disclaims it back to P06 **[REV-E-22, 2026-09-06 — stale publication status; all ten peer branches P01–P10 exist on origin, verified by `git ls-remote --heads origin`. NOT CONSUMED — `P06-OQ-124`/`P06-OQ-128`]** | **OPEN** |
| F-16 | Which physical bank account a GL balance belongs to | **UNOWNED** | **P11 intakes it as a new scope-mismatch row**: *"Reconciliation must be journal-scoped, not account-scoped"* | **SETTLED — accepted into P11's matrix** |
| F-17 | Period lock / close status | CONTESTED | **P04 `P04-B-43`** supplies the mechanism: hard lock is the **maximum over the whole parent chain**, elevated privilege, **including archived companies**, irreversible. P11 `PC-03`/`PC-04` add that soft locks move backward freely | **SETTLED to P08 — evidence enlarged by P04**; ~~`P08` unpublished~~ → **P08 PUBLISHED and read**, so the *decision* is open for want of a ruling, not for want of a package **[REV-E-22, 2026-09-06 — stale publication status; all ten peer branches P01–P10 exist on origin, verified by `git ls-remote --heads origin`. NOT CONSUMED — `P06-OQ-124`/`P06-OQ-128`]** |
| F-18 | Bank statement line identity | CONTESTED | **P11 adopts P06's mechanism as the one it lacked**; escalates to `P11-B-02`, *"the root"* | **SETTLED to P06 — and escalated above P06** |
| F-19 | Intercompany settlement | UNOWNED for payments | No peer claims it | **UNOWNED** — confirmed by silence across seven packages |
| F-20 | Advance / deposit before an obligation exists | CONTESTED | **P02 `P02-F-33`**: an unset down-payment property recognises the deposit as **immediate revenue**, and *"no chart template in the reference tree supplies it"*. **P05**: *"no advance asset account exists on this path"* | **SETTLED as CONTESTED — and materially worse**, two peers independently found the default is wrong |

**Reconciled: 20 of 20.** Prior: 8 CONTESTED, 4 UNOWNED, 1 HOLD, 7 assigned — **all as proposals**.
Now, **measured from the Disposition column of the 20 `F-` rows** — *not summed from the narrative* [REV-E-23, 2026-09-06]: **10 SETTLED · 4 CONTESTED** *(2 of them recorded as "SETTLED as CONTESTED")* **· 2 UNOWNED · 3 OPEN · 1 HOLD = 20.** ~~*"3 UNOWNED"*~~ was taken from the three facts listed at §-below, but **`F-16`'s Disposition cell reads SETTLED — accepted into P11's matrix**; it is *unowned by any process* and *not undisposed*, and the earlier tally summed two different columns into one figure. *The 3 OPEN rows were attributed to "P01/P08 unpublished"; **both are published** — P08 read (`53_`), P01 unconsumed (`P06-OQ-124`). The rows stay OPEN because no ruling exists, not because no package exists.* **[REV-E-22, 2026-09-06 — stale publication status; all ten peer branches P01–P10 exist on origin, verified by `git ls-remote --heads origin`. NOT CONSUMED — `P06-OQ-124`/`P06-OQ-128`]**

---

## 3. Facts P06 gained that it did not have

**CPO2-F-02 — A settlement path with no payment object.** ~~*"A fifth settlement door"*~~ [REV-E-23, 2026-09-06] — **this file gave the same finding two different ordinals** (*"fifth"* here, *"an 8th path"* at `:81`), and both are withdrawn: it is **P05's path 5 of its own 7**, on a different axis from P06's seven ingestion doors (`55_` SDD-F-01/02, `REV-E-12`).
P05 `SR-04`: the advance cash-return path *"creates a journal entry against the payment journal's default account **without an `account.payment`** … The cash movement **will not appear in payment listings, payment-based reports, or the bank-reconciliation matching model that keys on payments.**"*
**P06's seven-door ingestion denominator counted ways a bank event enters. This is a way cash moves that produces no payment and is invisible to matching.** It is a different axis, and P06 did not have it. `P06-B-53`.

**CPO2-F-03 — RELOCATE is core behaviour, not a reconciliation quirk.**
P04 `P04-F-61`, stated after its own independent challenge: *"**The silent re-dating is the accounting core's generic posting routine.**"*
P06 documented date relocation on three reconciliation paths. P04 shows it reaches **any** event that posts through the core routine. **This generalises `P06-B-46` well beyond P06's own evidence.**

**CPO2-F-04 — The lock cascade is worse than P06 measured.**
P06 established (B27-F-05) that the hard lock is the maximum across `parent_ids`. **P04 adds two facts P06 did not have:** the traversal is *"computed with elevated privilege"* and *"**including archived companies**"*, and the hard lock *"cannot be removed or moved earlier"*. `P06-B-45` is amended to carry both.

**CPO2-F-05 — P02 independently reached P06's `root_id` conclusion, and stated the legal consequence outright.**
P02 `SF-06`: *"**Reconciliation crosses legal entities on a shared root** … Journal items of two different legal entities that share one root are reconcilable."*
**P02 reached this before P06 closed `P06-B-27`, from different evidence, and phrased it as a legal-entity crossing.** This is the strongest corroboration in the package.

---

## 4. Ownership invariant, re-tested

**ONE FACT → ONE OWNER → ONE ACCOUNTING EFFECT**

| Fact | One owner? | One effect? | Change since prior round |
|---|---|---|---|
| Money arrived at the bank | no — 7 doors | yes per line | unchanged |
| Cash moved through a bank journal | **no — the `SR-04` path emits none** ~~*"an 8th path"*~~ [REV-E-23, 2026-09-06] | — | **worse** (CPO2-F-02) |
| Obligation settled | no | no | unchanged |
| Difference on settlement | no — 6 write-off entry points | yes | unchanged |
| FX difference | **yes — the ledger** | yes | **improved** — P11 settles it |
| Bank charge | **none** | — | unchanged, and P10 confirms no peer wants it |
| Employee reimbursement | **yes — P06** | yes | **improved** — P11 `UBE-33` settles it |
| Withholding at payment | **yes — split P06/P07** | yes | **improved** — P07 settles the split |
| Bank event identity | **yes — P06**, escalated to P11 | — | **improved** |
| Transfer between own banks | none | two effects | unchanged |

**Four facts moved from contested to owned. One got worse. Five are unchanged.**

---

## 5. What remains genuinely unowned

Three facts, after seven peer packages:

1. **Bank charges, interest and provider commission** (F-12). No process claims them; P10 asked P06 and P06 answers that the object does not exist for either. **The answer is delivered, not accepted — still `OPEN — PEER EVIDENCE` in P10's register at `1fea562` **[REV-E-18, 2026-09-06]**.**
2. **Intercompany money in transit** (F-19). Requires a TENANT-scoped carrier that owns neither company's effect.
3. **Which physical bank account a GL balance belongs to** (F-16) — accepted into P11's matrix but with no owning process yet.

**These are the three places where the target must create an owner, not assign one.**
