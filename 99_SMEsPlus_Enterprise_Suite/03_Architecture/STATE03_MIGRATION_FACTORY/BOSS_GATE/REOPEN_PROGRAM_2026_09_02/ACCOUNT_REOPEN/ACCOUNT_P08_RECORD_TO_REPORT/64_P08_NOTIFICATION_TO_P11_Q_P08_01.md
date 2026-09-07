# P08 → P11 — WRITTEN NOTIFICATION: A CONSUMED FIGURE HAS NO REFERENT

**From:** P08 — Record-to-Report / Core Ledger
**To:** P11 — Core Accounting Reconciliation
**Date:** 2026-09-07
**Authority:** Boss decision `PHASE-S/Q-BOSS-01` = **APPROVED**, branch `audit/account-phase-s-closure-2026-09-06-001` @ `1bf9b40`
**Queue item:** `Q-P08-01` (`XRD-011`), branch `audit/account-xrecon-2026-09-06-001` @ `3291210`
**P08 source baseline:** `research/account-p08-record-to-report-2026-09-04-001` @ `00ccd66`

> **This is a notification, not an edit.** P08 has **not** touched P11's package and will not. The corresponding repair on P11's side is P11's own queue item `Q-P11-04`.

---

## 1. What P08 published, and what is true

**P08 published, in `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` §1 item 1:**

> *"0 unbalanced posted entries in the reporting currency across 169,143 **at a tolerance of 0.005 or wider; at 1e-7 the answer is 3, all float artefacts on eight-figure sums**."*

**The "3" has no referent.** Re-derived on 2026-09-07 in exact decimal arithmetic, no floating point at any step:

| Measurement | exact equality | 1e-7 | 1e-4 | 0.005 |
|---|---|---|---|---|
| `DB-SM` (169,143 posted), debit − credit | **0** | **0** | **0** | **0** |
| `DB-SM`, **stored balance column** | **0** | **0** | **0** | **0** |
| `DB-BK` (16) and `DB-EV` (6), both columns | **0** | **0** | **0** | **0** |

**There is no tolerance at which the count is non-zero, on either column, in any deployed database.** The claim is **tolerance-independent**. Stating a tolerance beside it was itself the error, and the figure has been **deleted** — not re-scoped — from `58_` §1 item 1. `P08-CONTRA-75`.

## 2. What this obliges P11 to re-examine — stated, not decided

P08 is informed that P11 consumed this figure at **three** locations, and that P11's falsification `F-02` asks *"is there a tolerance at which the count is non-zero?"* and answers **YES** on the strength of it.

> **On the corrected evidence, the answer to `F-02`'s own question is NO.**

**P08 states the evidence and does not adjudicate P11's disposition.** Specifically, P08 does **not** rule on:

- whether `F-02` fails as a whole or only on this instance;
- whether P11's derived method rule — *"a soundness claim without a tolerance is not a claim"* — survives on other grounds. **P08's own view, offered as input and not as a finding: the rule may well be sound in general, but this instance does not support it, and P08's `58_` §1 row 2 now carries a case that points the other way** (see §3). **Whether to retain, re-ground or withdraw the rule is P11's decision.**

## 3. A distinction P08 did not previously draw, and P11 will need

The mandated re-run separated two measurements the package had been treating alike:

| Measurement | Tolerance behaviour |
|---|---|
| **Posted-entry balance, reporting currency** | **Tolerance-independent.** 0 at every tolerance including exact equality, on both columns, in all three databases. **No float artefact exists at any precision** |
| **Settlement reconstruction** (63,773 settlements over 100,580 lines) | **Tolerance-dependent.** Drift is **0 at ≥ 1e-6** and **2,354 lines at exact equality**, worst residual **2.1 × 10⁻⁹** — a genuine stored-float artefact of the settlement amount column |

**`58_` §1 row 2 has been re-issued to carry its tolerance; row 1 has been re-issued to state that it needs none.**

**P08 offers one interpretation, marked as such:** a float artefact belonging to the **settlement** measurement appears to have been attached to the **balance** measurement. `SUPPORTED INTERPRETATION` — the mechanism was not traced and the round that published the figure is closed. What is `FACT VERIFIED` is only that the balance figure has no referent and the settlement figure does.

## 4. Status of this notification

| | |
|---|---|
| Figure deleted from `58_` §1 item 1 | **DONE** |
| Every balance measurement re-run in exact arithmetic | **DONE** — `58_` §8 |
| `58_` §1 item 1 re-issued | **DONE** |
| **P11 notified in writing** | **THIS DOCUMENT** |
| `RC-05` — fresh structurally independent challenge | **REQUIRED and NOT SATISFIED** |

**`Q-P08-01` is executed but does NOT close.** The Boss ruled on 2026-09-07 (`XRECON/Q-BOSS-01` = `XRD-009` = **NOT SATISFIED**) that a verification performed by the same model that authored the repairs does not meet structural independence. **No eligible challenger exists** — `PHASE-S/Q-BOSS-02` is raised and unanswered. P08 has **not** run, selected, or self-satisfied `RC-05`, and does not represent this repair as closed.

**`AAS+-PS-VETO-01` C-6 remains NOT DISCHARGED.**
