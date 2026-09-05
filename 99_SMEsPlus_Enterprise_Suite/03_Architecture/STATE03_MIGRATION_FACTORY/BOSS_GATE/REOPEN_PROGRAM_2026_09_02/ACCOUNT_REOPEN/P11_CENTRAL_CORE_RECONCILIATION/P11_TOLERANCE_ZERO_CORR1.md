# P11 — C6 · TOLERANCE-ZERO POPULATION RECONCILED

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C06 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **`CONDITIONAL PASS` may not be used to bypass any row below.**

---

## 1. The prompt says 13. The package contains 11 by id. Both are true, and the gap is the finding.

`POPULATION` every `T0-nn` id referenced in any P11 package file · `PATTERN` `T0-[0-9]*` ·
`PATH SET` the package directory at `43195fd` · `UNIT` one distinct id. **Controls run first.**

> **Executed: 11 distinct ids** — `T0-01`, `03`, `04`, `05`, `06`, `07`, `09`, `10`, `11`, `12`, `13`.
>
> **Absent: `T0-02` and `T0-08`.**

**The inherited population is 13** (Wave A's `T0-01`…`T0-12`, plus `T0-13` opened by P11). **P11's own
package references only 11 of them by id.** `T0-02` (*posting without a measurement*) and `T0-08`
(*entry identity*) exist **only inside the range string `T0-01…T0-12`** in two files and are named
nowhere.

> ### `P11-F-13` — the `P11-G-01` defect, in P11's own tolerance-zero carriage, found by executing the count.
>
> P11 accepted `P11-G-01` — *carry-forward must enumerate **open items by id**, not by class* — from
> `P04`, **applied it to its own blocker register in prose, and never applied it to its
> tolerance-zero rows.** Two tolerance-zero boundaries dropped out of the package as a consequence.
> **They were never dispositioned, never argued, and never visible to a reader of P11 alone.**

## 2. The reconciled population

| id | Boundary | Status | CORR1 disposition |
|---|---|---|---|
| `T0-01` | Entry balance | `UNRESOLVED` | unchanged. **Strengthened by `P08`** — see §3 |
| **`T0-02`** | **Posting without a measurement** | `UNRESOLVED` | **RESTORED by id.** Never carried in P11 |
| `T0-03` | Deletion / rewrite of a posted fact | `UNRESOLVED` | **Strengthened by `P08`** — nine header attributes protected, protection waived by a caller-supplied parameter |
| `T0-04` | Tenant isolation | `UNRESOLVED` | unchanged |
| `T0-05` | Over-reconciliation | `UNRESOLVED` | unchanged |
| `T0-06` | Cross-company rewrite of a posted fact | `UNRESOLVED` | unchanged |
| `T0-07` | Cross-company rate resolution outside every record rule | `UNRESOLVED` | unchanged |
| **`T0-08`** | **Entry identity** | `UNRESOLVED` | **RESTORED by id. Materially strengthened** — `P08` answers it as `A VERIFIED ABSENCE` across all 22 declared roots |
| `T0-09` | Declared-but-inert control | `UNRESOLVED` | unchanged |
| `T0-10` | Cross-company lock-exception grant/revoke | `UNRESOLVED` | unchanged |
| `T0-11` | Balance invariant in one currency dimension only | `UNRESOLVED` | **Strengthened by `P08`** — asserted in the reporting currency only |
| `T0-12` | Balance assertion suppressible; `unbalanced-and-posted` reachable | `UNRESOLVED` | **Strengthened to its maximum available form** — see §3 |
| `T0-13` | An accounting fact may not be silently mutated, at any scope | `UNRESOLVED` | **Strengthened by `P10`** — a locked-period *recognition* entry is silently re-dated, so the mechanism reaches `P10` as well as `P01`/`P03`/`P04` |

> **13 boundaries. `0` resolved. `2` restored by id. `6` strengthened** *(corrected from ~~5~~ per `A-05`; the table marks six)* **— of which 2 carry an inheritance embargo. `1` headline WITHDRAWN. `0` narrowed.**

## 3. The three strengthened to their maximum available form, by `P08` @ `838134f`

| Boundary | Prior P11 form | `P08`'s form |
|---|---|---|
| `T0-08` / `UAE-29` | *no accounting-event identity* — class `C`, root undeclared | ~~`A VERIFIED ABSENCE` across all 22 declared roots~~ **WITHDRAWN `2026-09-05` per `C-01`.** P11 quoted `P08`'s **superseded** pack. `P08` `52_…_V2` supersedes it: **event identity is *the business record, per channel* — absent as a *platform property*; `FACT VERIFIED`, base narrowed**, with identity on **one inbound channel, a nullable column, `0 of 13,814` rows populated**. The correctly-scoped successor is **`UNTESTED across the root set`** |
| `T0-12` / `T0-01` | *the balance assertion is suppressible by context* | **"No database constraint enforces it in any of the 22 declared roots"** — and the assertion is *"application-level, suppressible by a caller-supplied parameter, and asserted in the reporting currency only"* |
| `T0-03` | *immutability is configuration* | **"Nine header attributes are protected and the protection is waived by a caller-supplied parameter; a posted journal item's account, counterparty, label, reference and cost allocation are editable in place"** |

> ~~**This is the first time in the programme that a tolerance-zero boundary has been stated as class `A` over a declared root set.**~~ **WITHDRAWN per `C-01` / `A-02`.**
>
> **Corrected position.** `P08` phrases its class-`A` negatives as **21 of 21 roots**, not 22 — and `P08-CONTRA-34`, *confirmed against the author by content hash*, records only **7 distinct contents**, so *"apparent strength is overstated by roughly threefold"*. **No tolerance-zero boundary is stated as class `A` over a declared root set.** What is available instead is **measured deployment evidence**, which is different and in places stronger: `0 of 13,814` identity rows, `0 of 109` sealed journals, `0 of 89` companies with a period lock.
>
> **`T0-11`/`T0-12` additionally carry an inheritance embargo:** `KRN-INV-00` is `CONTESTED` per `P08-BD-18` and **must not be inherited downstream** until the per-currency-frame question is answered (`C-03`).

## 3b. `T0-14` — added by the `S8` re-run, `2026-09-05`

| id | Boundary | Evidence |
|---|---|---|
| **`T0-14`** | **Financial history and the audit trail are deletable with no server-side authorisation** | `P06` `70_`: `om_data_remove` **INSTALLED on a real Odoo 19 database in this estate** — unfiltered `DELETE FROM` across bank statements, payments, journal entries, journal items, reconciliations and the audit trail; **`NO SERVER-SIDE AUTHORIZATION VERIFIED`** on the whole RPC dispatch chain; **`REACHABLE — DEPLOYMENT VERIFIED`**. `P08` raised the same module as its own `P08-T0-08` and left reachability `D UNKNOWN`; **`P06` closed that question** |

> **This is the only tolerance-zero boundary in the package that is `REACHABLE — DEPLOYMENT VERIFIED`
> rather than source-established.** Every other boundary describes what the software permits; this one
> describes what is installed and, on a first-party account, already run. **It is bounded by `D-1`** —
> the v19 database is not confirmed to be the SMEsPlus target — and that bound is recorded, not used to
> soften it.

## 4. Position

`14` boundaries · `0` resolved · `0` closable by more source reading · `CONDITIONAL PASS` unavailable
**by rule**. **CORR1 restored two, strengthened five, added one, and resolved none.**
