# P11 — UNIFIED SETTLEMENT / RECONCILIATION ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 7 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The finding that reorders this whole area

> ## Reconciliation is a **producer** of accounting events, not only a consumer.
>
> Three accounting events are emitted **by the act of matching**: the exchange difference (`UAE-01`),
> its reversal on unmatch (`UAE-02`), and cash-basis tax recognition (`UAE-03`). **Two of the three
> can be attributed to a period other than the one the underlying event belongs to** when that period
> is locked — and `UAE-03` can cross a **fiscal year** boundary.

`P06` is therefore not a downstream consumer of `P02` and `P01`. It is a producing process whose
output lands in `P07`'s return and `P08`'s comparatives, and **it owns none of the three events it
emits** (`C2` FAIL, `P11_UNIFIED_EVENT_OWNERSHIP_REGISTER.md` §3).

## 2. Settlement register

| Settlement type | Open item | Matcher | Emits | Reversal | Guard status |
|---|---|---|---|---|---|
| Customer payment ↔ receivable | AR item | `P06` | `UAE-01` where measurement moved | unmatch → `UAE-02` | **over-reconciliation unguarded** (`T0-05`) |
| Vendor payment ↔ payable | AP item | `P06` | as above | as above | as above |
| Bank line ↔ ledger item | liquidity item | `P06` | may clear through a **suspense** account | unmatch | **unreconciled lines block period locking** — a good pattern, worth generalising |
| Credit note ↔ invoice | AR/AP item | `P02`/`P01` | — | **auto-matched on posting where it cancels** | partial guard, cancelling case only (`DC-06`) |
| Reversal ↔ original | any | `P08` | — | **auto-matched on posting** | **lineage is a `CLOSED — VERIFIED DEFECT`** (`MCU-15`/`BW-35`) |
| Inventory ledger ↔ GL | not an open item | Inventory + `P08` | — | — | **agreement holds at the closing boundary, not continuously; the report must disclose which posture it measures** |
| Intercompany transfer | `?` | — | — | — | **path never traced end to end** (`GAP-FS-07`, `JT-10`) |

## 3. The four unguarded mechanisms

| id | Mechanism | Evidence |
|---|---|---|
| `SR-01` | **The matching record is unconstrained against the item it matches.** Nothing at storage level prevents a match exceeding the residual | `COR-09`; `T0-05` `UNRESOLVED` |
| `SR-02` | **Residual, reconciled marker and payment state are stored-computed and capable of drifting from their inputs**, and no mechanism was identified that reconstructs them after drift | `EV-014`; `GAP-E03` `UNKNOWN` |
| `SR-03` | **The entry-balance invariant is enforced in one currency dimension only**, and **the balance assertion itself is suppressible by context with three shipped production consumers — `unbalanced-and-posted` is reachable** | `T0-11`, `T0-12` — both `UNRESOLVED`; the 48-token bucket **never opened** |
| `SR-04` | **Cash-basis tax on unmatch**: `M-02` (FX) is explicitly auto-reversed when a match is removed; **`M-03` (cash-basis tax) is not stated to be**, and its row reads *"not itself reconciled"* / *"can be reversed but cannot be reset to draft"*. Unmatch-then-rematch is a candidate **double tax recognition** | `DC-07` — **`UNRESOLVED — EVIDENCE REQUIRED`, new at P11** |

`SR-04` is a gap **between two rows of one table**, visible only when they are read against each
other. It is recorded as a P11 contribution and as an **unknown**, not as a defect: the register does
not say the reversal is absent, it simply does not say it is present, and a negative claim over an
unread mechanism would be class `E` wearing class `A`'s label.

## 4. Positions

| id | Position | Basis |
|---|---|---|
| `SRP-01` | **A settlement may never exceed the residual it settles, enforced at storage level, not by application guard** | `SR-01`, `T0-05` |
| `SRP-02` | **Every stored-derived settlement value is reconstructible from its facts, and a reconstruction check is a first-class function** | `SR-02` |
| `SRP-03` | **The balance assertion is not suppressible. There is no context, key or flag that disables it** | `T0-12` — the most severe open item in the inherited base |
| `SRP-04` | **The balance invariant holds in every currency dimension the item carries, not only the company one** | `T0-11` |
| `SRP-05` | **Every event emitted by reconciliation names its owning process and its own recognition date, and is denied rather than re-dated when that period is closed** | `UAE-01`…`UAE-03`, `OWN-03` |
| `SRP-06` | **Bank-reconciliation completeness gates period locking** — adopt and generalise into the close checklist | `EV-019`; endorsed |
