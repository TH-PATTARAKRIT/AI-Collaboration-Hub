# P11 — UNIFIED SUBLEDGER ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 5 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The test a subledger must pass

A subledger is **of record** only if all four hold:

`S1` it holds detail that the control account aggregates;
`S2` it agrees with the control account at a stated moment, by a stated rule;
`S3` its detail is immutable once posted, correctable only by further facts;
`S4` it cannot be rebuilt from other data in a way that could differ from what it says.

A structure failing `S3` or `S4` is a **derived view**, not a subledger, and no reconciliation may be
claimed against it.

## 2. Register

| Subledger | Control | Owner | `S1` | `S2` | `S3` | `S4` | Verdict |
|---|---|---|---|---|---|---|---|
| **AR — open receivable items** | receivable control | `P02` | ✔ | ✔ at any time | ✔ | ✔ | **of record** |
| **AP — open payable items** | payable control | `P01`/`P05` | ✔ | ✔ | ✔ | ✔ | **of record** |
| **Bank / liquidity items** | bank control | `P06` | ✔ | ✔; **unreconciled lines block period locking** | ✔ | ✔ | **of record** |
| **Inventory valuation layers** | inventory control | Inventory | ✔ | **✘ — agreement holds at the closing boundary, not continuously** | ✔ | ✔ | **of record, with a disclosed agreement rule** |
| **Asset register** | asset + accumulated depreciation | `P04` | ✔ | ✔ | ✔ | **✘ — `CTR-06`, a check never run: assets whose posted depreciation does not sum to the depreciable amount** | **of record, unverified** |
| **Tax items** | tax control | `P07` | ✔ | ✔ | **✘ — tax items are outside hash coverage** | ✔ | **of record, unprotected** |
| **Settlement / matching records** | — | `P06` | ✔ | n/a | ✔ | **✘ — the matching record is unconstrained against the item it matches; residual and payment state are stored-computed and can drift** | **of record, undefended** |
| **Analytic lines** | — | `P09` | ✔ | n/a | **✘ — deleted on un-post, regenerated on repost** | **✘ — regeneration can differ from what was destroyed** | **NOT a subledger. Derived view** |
| **WIP** | WIP control | `P03` | ✔ | `?` | ✔ | **✘ — `JT-09` open** | **`HOLD`** |
| **Deferred schedules** | deferral control | `P10` | `?` | `?` | `?` | `?` | **`UNKNOWN — EVIDENCE REQUIRED`** |

~~**10 candidates. 3 unqualified. 4 qualified-with-a-defect. 1 rejected. 2 unknown.**~~

> ### SUPERSEDED `2026-09-05` — this §2 applied *"fails both"* while §1 states *"fails `S3` **or** `S4`"* (`X2-F06`, **CRITICAL**).
> **Re-run against the stated rule at `P11_SUBLEDGER_RERUN_B17.md`: 0 unqualified · 2 qualified · 7 derived views · 1 unknown.** The superseded table above is retained unedited for lineage, per `P11-G-03`. **Do not cite it.**

## 3. The rejection matters most

**Analytic is not a subledger of record**, and the whole of `P09` management accounting rests on it.
`SL-01` `06` §3 classifies analytic lines as *derived, destructible*; `EV-012` records that they are
deleted on un-post and regenerated on repost. A structure that a producer's ordinary correction can
destroy cannot carry management-accounting truth, and no variance, margin or profitability figure
computed from it can be reconciled to the ledger after any correction.

`P11-DERIVED.` Remedy, offered as `DESIGN CANDIDATE`: **analytic distribution is intent and lives on
the accounting event (`F2`); analytic lines are a derived projection rebuilt from intent; the rebuild
is itself a recorded event.** This is `OWN-04`.

## 4. The generalised handoff contract — `BC-02` extended to all ten processes

`BC-02` is `BOSS APPROVED / EFFECTIVE` **for Inventory → Accounting only**. Nine other producing
processes hand facts to the ledger under **no contract at all**. `P11` records that as `P11-F-02` and
proposes the generalisation below as a `DESIGN CANDIDATE` — it is a Boss control decision, not an AI
one.

| # | Element | `BC-02` wording | P11 generalisation |
|---|---|---|---|
| 1–9 | what / who / when physical / when financial / quantity / UOM / basis / identity / location | unchanged | **applies to every producer**; 5, 6, 8, 9 become `N/A + reason` where the producer moves no goods |
| **10** | `WHICH Company / Tenant` — *mandatory* | **restated under `SMEPLUS-26-09-04-ACC-REV2-CORR1`**: *the object's declared scope, and every context that scope requires — no more and no less* | stricter in effect: it also forbids supplying a context the scope does not authorise (`RV-05`) |
| 11–13 | source document / original event / reversal link | unchanged | applies to every producer |
| **14** | migration / replay batch identity | unchanged | **`TENANT`-scoped batch identity; does not exist today (`GAP-FS-08`)** |
| **15** | deterministic idempotency identity | unchanged | **the single element that prevents `DC-01`; does not exist today (`RISK-C02`)** |
| 16 | evidence reference | unchanged | applies to every producer |
| **17** | *new* — **owning process, named on the event** | — | `OWN-01`; without it `C2` cannot be evaluated |
| **18** | *new* — **declared scope (`F8`)** | — | `SCP-01`; without it `MISSING REQUIRED SCOPE = DENY` is unevaluable |

Compliance today, on the only handoffs measured: **0 of 10**, with elements **10, 14 and 15 failing on
every one**. Elements 17 and 18 are unmeasured because they do not yet exist as requirements.
