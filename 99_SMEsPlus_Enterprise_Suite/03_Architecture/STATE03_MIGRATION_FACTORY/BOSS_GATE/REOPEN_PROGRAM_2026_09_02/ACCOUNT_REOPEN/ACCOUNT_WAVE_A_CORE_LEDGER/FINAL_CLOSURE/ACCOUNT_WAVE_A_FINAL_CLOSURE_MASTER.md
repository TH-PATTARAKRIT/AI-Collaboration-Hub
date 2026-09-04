# ACCOUNT WAVE A — FINAL CLOSURE MASTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` (`aad8a1e`) · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Date `2026-09-04`

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**

---

## 1. What this session was asked to do, and what it did

**Asked:** finish Wave A correctly; publish the evidence verifiably; resolve `MCU-04`; package `GB-08`
for Boss; complete method convergence; prepare Wave B without starting it.

**Did:** all six. Two of them changed the answer the programme was carrying.

| # | Task | Result |
|---|---|---|
| 1 | GitHub publication | **PUSH CAPABILITY RECOVERED.** The parent's blocker is gone — see §6 |
| 2 | Jira publication | Sequenced **after** verified push, per `ER-CORE-10` |
| 3 | **`MCU-04`** | **`VERIFIED DEFECT`** — re-verified from primary source across 6 roots, not inherited |
| 4 | **`GB-08`** | **Boss Decision Package complete.** `BOSS DECISION REQUIRED` |
| 5 | Method convergence | **`NOT CONVERGED`** — **one** exact remaining defect, named |
| 6 | Wave B | **Prepared. NOT STARTED.** `NOT READY — EXACT DEPENDENCIES` |

---

## 2. The headline

> ### The programme has never declared which reference source root it is researching.
>
> A mechanical discovery — *every directory containing `addons/base/models/res_currency.py`* — returns
> **22 reference core roots** on the evidence volume. **Wave A searched one**, and no artefact says
> which, or that a choice was made.
>
> **Two consequences, both first-order:**
>
> 1. **Every class `A — VERIFIED ABSENCE` in Wave A's history is bounded to ≤1 root of 22 and none
>    declares it.** Under the programme's own `DR-NC-01`, that is class `E` wearing class `A`'s label.
> 2. **The Wave A rate-table research ran against a root where the branch-preference behaviour is
>    ABSENT — while the one root in the universe named `18.0.3_smeplus` has it PRESENT.**
>
> **This is not a new kind of finding. It is `GB-07` — the exact defect the parent round corrected —
> reappearing one level up.** The parent proved its *path set* inside a root it never proved.

**Method validation, stated before the claim was used.** This round applied its counting method to the
parent's **own** declared root and returned **1,753** manifested modules against the parent's declared
**791 + 961 = 1,752** (+1 root manifest). **Exact agreement.** The extension is a change of path set,
not of method — which is what makes it citable rather than a competing count.

---

## 3. `MCU-04` — closed

> # `VERIFIED DEFECT`

`account.report` — the model that defines the financial statements — has **no company dimension**, is
targeted by **no record rule** in any of 6 roots, and carries **full create/write/unlink** for the
accounting-manager role. Its sibling `account.report.external.value`, in the same security file, **is**
company-scoped. **The divergence is inside one module.**

**Amplified this round (`FC-A1`):** the bound server action creates an `ir.ui.menu`, and `ir.ui.menu`
has **no company field and no record rule** — so a report menu created by one company's manager is
visible to **every** user holding the group, in every company.

**Corrected this round (`FC-C1`, `FC-C2`):** the parent's *"arbitrary server-side code"* and
ordinary-user-escalation characterisations are **overstated**; the finding does not depend on them.

**Why the disposition changed:** not new evidence. The **ground** for holding it open — *"it is a tenant
question"* — was tested and failed. **The mechanism is fully determined by source and invariant under
every tenant mapping; only the blast radius varies.** Holding a determined mechanism open because its
consequence is policy-dependent is `ER-CORE-11`'s **backward** routing abuse.

**Not closed:** `MCU-11` (different mechanism), and **`T0-04` remains `UNRESOLVED`** — closing an
unknown does not resolve a boundary.

Full detail: `ACCOUNT_WAVE_A_MCU04_FINAL_DISPOSITION.md`.

---

## 4. `GB-08` — packaged, not decided

> # `BOSS DECISION REQUIRED — GB-08`

**Sharpened from the parent's statement.** `Δ1` (branch-preferred rate resolution) is a **three-line
diff**, present in **5 of 22 roots**, absent from **every v19 root**, and absent from the parent's own
research root. The behaviour is **non-monotonic: `absent → present → absent`.** `Δ3` (the v19 ORM-core
raw-SQL rate resolver — no record rule, converts at **today**, silent par fallback, emitted for **every**
monetary field in list, pivot and graph) is **new in v19** and was independently reproduced here.

**The schema is stable across all four trees diffed. The semantics are not. There is no migration
artefact for any of it, and a DDL-shaped migration gate cannot see it.**

Four options are stated with what the evidence does **and does not** support. **None is selected.**

Full detail: `ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md`.

---

## 5. Method convergence — one defect, named

> ## `NOT CONVERGED`
> ### Exact remaining enumeration defect: **the root set is undeclared.**

`MC-01`…`MC-10`: **7 not met · 2 partially met · 1 met** (parent: 8 / 2 / 0). **`MC-04` Repeatability
moved to `MET` — the first `MET` in the programme's convergence history.** Nothing moved down.

**Fixed point: `NOT REACHED`.** Three consecutive rounds each returned material new findings on first
independent contact. **The rate is not decaying.**

**New this round:** 4 material findings (`FC-F1`…`FC-F5`), 3 claim corrections, **0 new tolerance-zero
boundaries** — the first round to open none.

**`GB-06`'s fourth instance, and the worst:** **`MCC_00`** — the canonical figures register created to
end correction-propagation failure — **shipped with its §1 count contradicting its own §2
dispositions** (`FC-F1`). It closes ten ids and counts nine. No consumer, including an independent
sibling panel, noticed.

Full detail: `ACCOUNT_WAVE_A_FINAL_METHOD_CONVERGENCE_REPORT.md`.

---

## 6. Panel completion — tested, not assumed

The sibling **AAS+ Redesign** session (`…-AASR-001`) was **actively writing when this session began** —
20 files in 4 minutes, with an independent veto report appearing mid-session. It reached terminal state
at **13:56** (manifest written, 24 files, zero writes thereafter).

**Its terminal state is itself a non-convergence signal** — quoted as data:

> `ACCOUNT WAVE A — PROVISIONAL PARALLEL SYNTHESIS · AAS+ OUTPUT IS NOT CANONICAL`
> `AWAITING PARENT CONVERGENCE, REGISTER CLOSURE AND DELTA REVALIDATION`

with `AASR-VETO-01` upheld. **An independent downstream consumer of the Wave A evidence base could not
use it, and said so.** Its `V-SYS-2` — *"consumed the parent's findings but not the parent's
corrections"* — is `GB-06` reproduced independently, on a different task, by a different session.

---

## 7. Closure criteria — §7 of the round instruction, tested one by one

| # | Criterion | Status |
|---|---|---|
| 1 | All active Wave A expert/audit panels finished | **MET** — mechanically verified (§6). **It was NOT met when this session began** |
| 2 | Material contradictions dispositioned | **PARTIAL** — `FC-F1` and `FC-F5` are **newly opened and stand open**; the 14-item backlog is uncleared and now ≥18 |
| 3 | Gating unknowns closed or proven non-Wave-A-gating | **MET as an exercise** — all 17+ dispositioned, none routed forward. **8 remain ledger-gating** |
| 4 | Tolerance-zero findings dispositioned | **MET as an exercise** — **12 dispositioned, `0` resolved** |
| 5 | `MCU-04` final disposition | **MET** |
| 6 | `GB-08` Boss dependency packaged | **MET** |
| 7 | Method convergence final and evidence-backed | **MET as a determination** — the determination is **`NOT CONVERGED`** |
| 8 | Negative-Claim Standard compliance scan | **MET** — and it returns **`MC-05` `NOT MET`** programme-wide |
| 9 | Evidence manifest verified | **MET** — per-file SHA-256 + roll-up |
| 10 | GitHub publication verified | **see §8** |
| 11 | Jira publication after live GitHub verification | **see §8** |
| 12 | No implementation/build action performed | **MET** — no source file created, modified or deleted; nothing merged; nothing deployed |

> **Criteria 2, 3, 4 and 7 are met as *exercises* and fail as *outcomes*.** Every gating unknown is
> dispositioned and **8 remain gating**; every tolerance-zero boundary is dispositioned and **0 are
> resolved**; convergence is determined and the determination is **not converged**.
>
> **That distinction is the whole content of the recommendation.** Wave A's *research* is in good
> order. Wave A's *conclusions* are not yet safe to rely on downstream.

---

## 8. Publication

See `ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md` §GitHub and §Jira for the verified, timestamped
status. **The parent's blocker — a refused push — is gone in this session.**

---

## 9. Terminal state

> ## `ACCOUNT WAVE A — HOLD WITH EXACT REMAINING BLOCKERS`
>
> **Eight blockers `GB-01` … `GB-08`.** Four need a Boss decision; three are cheap mechanical work; one
> — `GB-08` — needs a build-freeze decision before any Wave A conclusion can be relied on downstream.
>
> **Twelve tolerance-zero boundaries, `0` resolved.** `CONDITIONAL PASS` is unavailable **by rule**.
>
> **One exact remaining enumeration defect: the root set is undeclared.** Cost to close: **hours,
> mechanical, no new research.** It is the last thing standing between the method and `MC-01`, and
> closing it re-scopes `GB-07`, `GB-08`, `MCU-18`, `MCU-19b` and every class `A` absence at once.

**Not declared:** converged · final approved · Wave A closed · any gate movement · any implementation
authorisation · Team B or Team C hand-off · the Very Deep standard as canonical.

**Wave B has not started.** No SMEsPlus or reference source code was read for modification, and none was
modified. Nothing was merged. Nothing was deployed.
