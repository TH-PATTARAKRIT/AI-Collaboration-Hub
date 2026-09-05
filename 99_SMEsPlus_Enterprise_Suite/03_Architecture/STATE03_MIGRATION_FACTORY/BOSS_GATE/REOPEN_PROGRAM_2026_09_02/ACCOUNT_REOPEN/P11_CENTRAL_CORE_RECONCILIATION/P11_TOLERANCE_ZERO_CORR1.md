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

> **13 boundaries. `0` resolved. `2` restored by id. `5` strengthened. `0` narrowed. `0` superseded.**

## 3. The three strengthened to their maximum available form, by `P08` @ `838134f`

| Boundary | Prior P11 form | `P08`'s form |
|---|---|---|
| `T0-08` / `UAE-29` | *no accounting-event identity* — class `C`, root undeclared | **`A VERIFIED ABSENCE` across all 22 declared roots.** The root set is now declared and independently reproduced |
| `T0-12` / `T0-01` | *the balance assertion is suppressible by context* | **"No database constraint enforces it in any of the 22 declared roots"** — and the assertion is *"application-level, suppressible by a caller-supplied parameter, and asserted in the reporting currency only"* |
| `T0-03` | *immutability is configuration* | **"Nine header attributes are protected and the protection is waived by a caller-supplied parameter; a posted journal item's account, counterparty, label, reference and cost allocation are editable in place"** |

> **This is the first time in the programme that a tolerance-zero boundary has been stated as class `A`
> over a declared root set.** It does not resolve any of them — **it removes the last excuse for
> treating them as bounded-scope uncertainties.**

## 4. Position

`13` boundaries · `0` resolved · `0` closable by more source reading · `CONDITIONAL PASS` unavailable
**by rule**. **CORR1 restored two, strengthened five, and resolved none.**
