# P10 — PERIOD GRID AND CONVENTION TRACE  (`CQ-P10-03`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.**

---

## 1. Schedule Generation

| Element | Reference behaviour | Class |
|---|---|---|
| Trigger | Source-document posting, **or** a button on a report — selected by one company setting per direction | FACT |
| Window | Two dates on a journal item, both **inclusive** | FACT |
| Grid | **Calendar month ends, unconditionally.** No configuration changes it | FACT |
| Period count | Derived from the window; a window falling wholly inside the source document's own month produces **no entries at all** | FACT |
| Schedule object | **None.** The segment set is computed, consumed and discarded inside one generation call | FACT |
| Amendment | **No modification path exists** other than tearing down the source document | FACT, bounded to the deferral mechanism |

> **The grid is monthly in every configuration. The day/month/full-month setting changes the *weights*, never the *dates*.** "Daily recognition" is not expressible.

## 2. Convention — three engines, not two

This is the round's material correction to the prior baseline.

| Engine | Convention | Note |
|---|---|---|
| Deferral | A named 30/360 standard **with its February exception deleted** — both endpoints snapped to day 30, no February carve-out | |
| Asset | Matches **none** of the named conventions — mid-month days scaled by actual month length | |
| **Loan** | A complete, standards-named library of **eight** conventions, default `30E/360`, **implementing correctly the February exception the deferral engine omits** | **not previously reported** |

**Worked divergence**, arithmetic on both bodies: a 14–28 February window in a non-leap year yields `17/30` under the deferral engine and `16.07/30` under the asset engine — **5.5% apart on the same fraction of the same month**.

> The earlier phrasing *"same conventions, different code"* **understates it: they are not the same convention.** And the same codebase implements a named standard correctly in one module and, in another, the same standard with its one exception removed — the exception applying to precisely the month where the prior Asset round measured the largest divergence.

**Design consequence:** a convention library was P10's least-qualified kernel element. It changes from **build** to **adopt-and-extend** — a complete standards-named library already exists inside the declared root. That is a materially different recommendation and it is a `DESIGN CANDIDATE`, not an architecture decision.

## 3. First and Last Period

| Case | Behaviour |
|---|---|
| First partial period | Pro-rated from the window start |
| Last partial period | Pro-rated **plus all rounding residue** |
| Window shorter than one period | One period; **none at all** if it falls in the source document's own month |
| Window expressed start → same day next year | 12 + 1/30 periods, uneven amounts; **advisory warning only, no constraint** |

## 4. Rounding and Residue — four policies, and they disagree by design

| Mechanism | Residue destination |
|---|---|
| Deferral, validation path | forced into the **last period's profit-and-loss** |
| Deferral, grouped path | a **plug line on the balance-sheet control account** — a different statement |
| Asset | absorbed at end of life against the residual |
| Loan | **refused** — a contractual table must reconcile or the confirmation raises |

**A previously unrecorded consequence:** the grouped path's plug line carries **no attribution, no product and no partner**, and the entry is reversed the next day, so the ledger nets and the **management ledger does not**. Its analytic total differs from its ledger total by the residue, permanently and by construction.

> **Two paths for one economic fact place the residue in two different financial statements.** That is a second, independent instance of the one-fact-two-shapes violation and it was not previously cited in support of it.

Residue policy is an **assertion about who owns a difference**, not an arithmetic setting. It is confirmed **domain-owned** and must never be defaulted.

## 5. Disposition

`CQ-P10-03`: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, bounded to the declared root. The three-engine finding and the residue-destination divergence are new this round and are recorded as corrections to the prior baseline, not as replacements of it.
