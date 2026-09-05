# P01 — AAS+ TARGETED CONSOLIDATION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Dissent preserved, not averaged.

---

## 1. THE TWO STATEMENTS THAT MATTER MOST

> **1. No inventory value reaches the general ledger by any route in the deployed v19 systems.**
> Not at receipt — that route was **removed by design**, v19 recognising inventory *at
> invoicing*. Not at invoicing — **no valuation account resolves anywhere**: category 0/37,
> company journal 0/44, location 0/525, account-level variation 0/544. Not periodically — the
> inventory closing period is `manual` on 87 of 88 company rows.

> **2. A cross-tenant financial-effect path is reachable today.** Three unrelated corporate
> groups share one schema; every company partner is selectable from every company; the declared
> access guard **cannot execute**, because the deployed "create as" user is the superuser on
> 44 of 44 companies.

The first is an accounting-integrity finding. The second is a tolerance-zero isolation finding.
**Neither was in the package at the start of this round in its current form.**

---

## 2. AGREEMENTS

1. The vendor bill is the **only** universal accounting event in procure-to-pay.
2. Purchase order confirmation creates **no** accounting effect.
3. The purchase documents carry **no capital-versus-expense classification** — independently
   reached by P01 and P04.
4. Three-way matching is **advisory, not a control**, wherever it is installed.
5. Period locks **re-date rather than refuse** anything that creates an accounting fact.
6. Correction of a posted bill **hard-deletes** derived journal items, preserving only account
   and amount in a weakly-protected audit record.
7. Several controls that would mitigate the above **ship switched off** and are off in every
   analysed deployment.

---

## 3. DISAGREEMENTS AND MINORITY POSITIONS — PRESERVED

| Subject | Positions | Status |
|---|---|---|
| Is the v19 receipt absence design or misconfiguration? | **Design** (expert, verified) vs misconfiguration (this session, earlier) | **Both are components of the truth**; the session's earlier framing is superseded, not deleted |
| Does bill correction destroy lineage? | **Strong form contradicted** — an audit record survives; but it is deletable, incomplete, and absent entirely in the v16 deployment | **MIXED** — dissent between the source capability and the deployed reality is retained |
| Is the WHT overlap "Low"? | P05's rating **survives**; its justification was retired by P05 itself; P01's two supporting statements were **partly wrong** | **`BOTH PARTIAL`** |
| Subcontract credit split | **Verified for v18, contradicted for v19** | Both retained, version-bound |

---

## 4. CONSOLIDATED RISK

### 4.1 Accounting integrity
Inventory never capitalised (§1.1) · period locks re-date · correction by deletion · landed cost
silently loses value when goods are already sold · advance to a vendor defaults to an **expense**
account.

### 4.2 Tax
Repeated **full** withholding on every partial payment — linear over-withholding · two
contradictory certificate mappings, **neither of which governs** because an operator picks the
form · a third withholding engine latent · one subsystem files without certifying while the other
certifies without filing. **Every statutory question is held and routed to P07.**

### 4.3 Scope and isolation
**Tolerance-zero, live.** See §1.2. Plus: the full-reconciliation object has no company scoping
and no record rule in either generation, with full CRUD granted.

### 4.4 Evidence-base risk — new, and the most instructive
The generation the source analysis targets, **v18, has no deployed representative in this
estate**. The deployed comparison actually spans **v16 → v19**, three major versions. And the
single most relevant database was excluded for a whole round by an untested tooling assumption.

---

## 5. WHAT CHANGED IN THE PROGRAMME'S UNDERSTANDING

| Before this round | After |
|---|---|
| v19 lacks a receipt-to-bill bridge | v19 **replaced** it with invoice-time recognition — a different accounting model, deliberately chosen |
| The deployments are misconfigured | The deployments are misconfigured **and** the design changed; the two combine into total silence |
| Withholding compounds geometrically | Withholding repeats **linearly**, by a different mechanism, in code no deployment demonstrably runs |
| Three-way match and subcontracting are installed nowhere | Both are installed — in the database that was excluded |
| Cross-company effect is a latent risk | **It is reachable today, and its one guard cannot execute** |

---

## 6. VETO AND HOLD POSITIONS

| # | Position |
|---|---|
| `AASV-P01-01` | **Tolerance-zero HOLD** on financial company ownership. Under `EC-04` no conditional outcome may bypass it |
| `AASV-P01-02` | **HOLD on any design inheriting a receipt-to-bill clearing bridge** until Boss rules which generation is the target — the two candidate generations use **fundamentally different accounting models**, and one of them has no deployed representative here |
| `AASV-P01-03` | **HOLD on treating any P01 finding as runtime-verified.** Nothing in this package was executed |

---

## 7. WHAT AAS+ REFUSES TO DO

- Convert any class B, C or D negative into a class A absence.
- Present a corrected finding as though it had always been stated that way — all eight
  corrections are logged with their originals intact.
- Claim convergence. **Sixteen contradictions, zero closed, and the count has risen in every
  round.**
- Treat expert agreement as verification, or treat a peer's summary as their position.
- Make a target-architecture decision or a Boss-level decision anywhere.
