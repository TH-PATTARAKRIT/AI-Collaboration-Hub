# 41 — P03 PEER EVIDENCE RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

Peer branches were **fetched and read** this round, not taken from messages —
`smeplus-peer-intake-discipline`: *a peer's message is a summary; a peer's pushed branch is
the source.* That rule immediately paid: it corrected P03's own record (`27` §2).

---

## 1. Intake and classification

| Peer | Branch read? | Classification | Effect on P03 |
|---|---|---|---|
| **P04** Acquire-to-Retire | **Yes** — `06`, `10` | **CONTRADICTS then CONFIRMS** | Corrected P03's "nine" to **seven**; confirmed netting, help text, `DC-14`/`DC-15` |
| **P09** Plan-to-Analyze | **Yes** — file list + status | **CONFIRMS / EXTENDS** | Netting mechanism; `MA-11` adopted; plans have no company field |
| **P02** Order-to-Cash | status only | **EXTENDS** | Same database: 447,384 journal lines, **zero COGS lines** — verified identical count |
| **P01** Procure-to-Pay | status only | **PEER-OWNED** | `DEP-06` subcontract bill/receipt difference stays open |
| **P05** Expense-to-Pay | status only | **METHOD — and disconfirmed for P03** | P05's surface was in custom addons; **P03's is not** (`27` §7) |
| **P06** Bank-to-Reconcile | status only | **PEER-OWNED** | Fiscal-hierarchy-vs-legal-boundary; consistent with `res_company` parent paths seen in `BK12MAY26` |
| **P08** Record-to-Report | not read | **P11 RECONCILIATION REQUIRED** | `R-16` routed to it — §4 |
| **P10** Time-Based Recognition | status only | **EXTENDS** | *Recognition event collapsed into posting act* is the same root cause as `DC-09` |
| **P11** Core Reconciliation | status only | **P11 RECONCILIATION REQUIRED** | `DEP-11`, `P11-D-1..3` |

## 2. P02 — the same database, the other half of the story

P02 reports 447,384 journal lines and **zero COGS lines** in `iSMEs`. P03 independently
counted `account_move_line` = **447,384** in the same dump. **The figures match exactly**,
which cross-validates both sessions' extraction method.

Put together:

> Manufactured goods are carried at **material cost only** (P03), and when they are sold
> **no cost of sales is recognised at all** (P02).

Neither session can see this alone. Recorded jointly; **neither closes the other's finding.**

**Manufacturing cost creation ≠ COGS recognition.** P03 owns the first, P02 and the COGS
track own the second, and the two must not be conflated — `12` `OWN-05`/`OWN-08`.

## 3. P10 — a shared root cause

P10: *recognition event collapsed into posting act is the root cause*. P03 `DC-09`: the
labour entry is dated when posted, not when the work happened.

> **The same defect, in two processes: the system has no representation of *when an
> economic event occurred* that is independent of *when someone pressed the button*.**

Recorded as a **programme-level** root cause, not a P03 finding. Routed to P11; neither
session should fix it locally.

## 4. Handoff to P08 — Record-to-Report

| Item | Content |
|---|---|
| Cost posting | Two GL mechanisms (`M1`, `M2`); a third (`M8`) self-reverses; three different WIP account resolvers — `08` §2 |
| **Journal identity** | **`R-16`** — every entry from a business event needs an identity written **and read** as the duplication guard. `DC-15` is the manufacturing instance of Account Wave A's *no event identity* |
| Idempotence | `DC-15` — marker written, never read; only protection is the caller's state filter |
| Duplicate financial effect | None found for machine cost (`38` §4); analytic duplication only |
| WIP / FG consequences | `DC-03`, `DC-04` residues; account families never reconciled |
| Locked-period re-dating | **P04's finding, in the accounting core** — hits every programmatic post. P03 confirms it would hit `_post_labour`; **owner is P08** |

**P03 decides no core-ledger architecture.**

## 5. Handoff to P09 — Plan-to-Analyze

`33` §6 carries it. `SCOPE-Q-01` (analytic plan scope) stays **HOLD — SCOPE EVIDENCE
REQUIRED**; P09 reports plans have no company field at all, which makes it a P09/P11
question, not a P03 one.

## 6. Handoff to P02

`34` §5 and §2 above. P03 supplies the FG unit-cost formula and its measured inputs; P02
owns what happens at delivery.

## 7. What P03 did not do

- Did not re-run any peer's research.
- Did not adopt any peer claim without source verification — `25` §1 and this round's
  re-derivations in `29`, `33`, `36`.
- Did not wait for any peer. `PEER DEPENDENCY OPEN` recorded for P08 and P11; all
  unaffected work completed.
- Did not amend any peer's register.
