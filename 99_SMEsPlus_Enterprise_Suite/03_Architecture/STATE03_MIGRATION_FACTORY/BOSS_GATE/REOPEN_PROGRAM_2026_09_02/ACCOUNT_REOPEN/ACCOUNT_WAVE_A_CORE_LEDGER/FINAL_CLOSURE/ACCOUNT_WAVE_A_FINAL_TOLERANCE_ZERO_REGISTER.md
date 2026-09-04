# ACCOUNT WAVE A — FINAL TOLERANCE-ZERO REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Canonical source: `MCC_00_CANONICAL_FIGURES_REGISTER.md` §3.

> **Recommendation only. Boss is the sole Final Approver.**
> **Tolerance = 0. A `CONDITIONAL PASS` may not be used to bypass any row below.**

---

## 1. Position

> # **12 boundaries. `0` resolved. `0` opened by this round.**

**This is the first round in the programme's history to open no new tolerance-zero boundary.** That is
reported as a data point about *this round's scope*, not as evidence of convergence: this round did not
open the surfaces (reversal, referential actions, the 48 suppression tokens, DDL) from which the last
five came.

---

## 2. The 12

| id | Boundary | Status | Disposition this round |
|---|---|---|---|
| `T0-01` | **Entry balance** | `UNRESOLVED` | Unchanged. **Note `T0-11` and `T0-12` are both attacks on this same invariant from different directions** |
| `T0-02` | Posting without a measurement | `UNRESOLVED` | Unchanged |
| `T0-03` | Deletion or rewrite of a posted fact | `UNRESOLVED` | Unchanged |
| `T0-04` | **Tenant isolation** | `UNRESOLVED` | **Evidence strengthened, boundary not resolved.** `MCU-04` closed as a `VERIFIED DEFECT` **on** this boundary, and `FC-A1` adds a further member — the `ir.ui.menu` created by `_create_menu_item_for_report` has **no company field and no record rule** |
| `T0-05` | Over-reconciliation | `UNRESOLVED` | Unchanged |
| `T0-06` | Cross-company rewrite of a posted fact | `UNRESOLVED` | Unchanged |
| `T0-07` | **Cross-company rate resolution outside every record rule, undeclared fallbacks** | `UNRESOLVED` | **Widened by `FC-F2`/`FC-F3`.** 10 bypassing readers, **five** fallback semantics; and the resolution behaviour itself is now known to differ across **5 of 22** reference roots. Headline instance `BW-28a` |
| `T0-08` | Entry identity | `UNRESOLVED` | Unchanged — net **understated** per `MCC_J` |
| `T0-09` | **Declared-but-inert control** | `UNRESOLVED` | **Third instance identified this round:** `account.report.filter_multi_company` **reads** to a reviewer as a company control and is a **rendering option** — the source comment says so. Not bounded; floor of 30 declarations across 4 files |
| `T0-10` | Cross-company creation and revocation of the lock exception | `UNRESOLVED` | Unchanged — wider than registered |
| `T0-11` | **Entry-balance invariant enforced in ONE currency dimension only** | `UNRESOLVED` | Unchanged |
| **`T0-12`** | **The balance assertion itself is suppressible by context; 3 shipped production consumers. `unbalanced-and-posted` is reachable** | `UNRESOLVED` | **Unchanged, and it remains the single most severe open item in Wave A.** The taxonomy still has **no cell for it** |

---

## 3. Why `CONDITIONAL PASS` is unavailable

Not a judgement. **A rule.**

> The standard and the standing Boss instruction forbid using `CONDITIONAL PASS` to bypass an
> unresolved tolerance-zero boundary. **Twelve stand unresolved. The conditions would *be* the
> tolerance-zero items.** A conditional pass whose conditions are the tolerance-zero set is a `PASS`
> with a different label.

---

## 4. What each boundary needs

| Need | Boundaries |
|---|---|
| **Boss design decision** | `T0-04` (tenant model), `T0-06`, `T0-10` — and `T0-07` via `GB-08`/`MCU-21` |
| **Clean-room design decision** (reject the reference behaviour) | `T0-01`, `T0-11`, `T0-12`, `T0-02` |
| **Bounded further research** | `T0-09` (never bounded), `T0-05`, `T0-08` |
| **Executed test on a running instance** | `T0-07` runtime half, `T0-03` |

> **None of the twelve is closable by more source reading alone.** Four need a design decision, three
> need bounding, two need a running system, three need Boss. **This is why the correct recommendation is
> `HOLD` and not "research more".**

---

## 5. `T0-12` — carried forward verbatim, because it must not be lost

> **The debit = credit assertion is itself suppressible by context, with three shipped production
> consumers. `unbalanced-and-posted` is reachable.**
>
> That is a worse state than balanced-but-wrong, and the taxonomy has **no cell for it**. The
> suppression key sits inside a bucket of **48 generic tokens that was counted and never assessed** —
> it is that bucket's most severe member, and the bucket has still not been opened.

**Opening that bucket is a named Wave A residual.** It is not Wave B work and must not be routed there.
