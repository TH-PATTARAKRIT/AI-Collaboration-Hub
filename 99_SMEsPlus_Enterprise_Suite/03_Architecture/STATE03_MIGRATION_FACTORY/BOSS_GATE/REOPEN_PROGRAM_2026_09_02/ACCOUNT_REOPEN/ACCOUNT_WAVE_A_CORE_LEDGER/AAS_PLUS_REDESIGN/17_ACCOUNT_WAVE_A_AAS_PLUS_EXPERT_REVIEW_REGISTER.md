# 17 — AAS+ EXPERT REVIEW REGISTER

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> Ten perspectives, each answering independently. **Disagreement is preserved until dispositioned** —
> §3 records what is still contested and does not resolve it by authority.

---

## 1. The perspectives, and what each concluded

### `P-01` Functional / Business Process Architecture

| Question | Position |
|---|---|
| Authoritative business fact | the **accounting event** — what the business recognised |
| Owner | the ledger, on the producer's declaration |
| Event that changes it | none. A further event supersedes it |
| Immutable | recognition, amounts, classification, currency, provenance |
| Derived | balances, residuals, ageing, results, current-year earnings |
| May be corrected, how | by counter-fact then corrected fact, linked |
| Failure modes remaining | `T-10` omitted event is **detected, never prevented** |
| Evidence | `BS-01`, `07`, `ST-09` |

**Contribution.** The 21-event enumeration is the strongest functional asset the parent produced.
**Concern raised:** the design removes un-posting entirely (`07 §5`) and the register does not
establish what operators use un-posting *for* today. Removing a path without knowing its business use
is how correct designs fail in adoption. Recorded as `X-A`.

### `P-02` Accounting / Financial Control Architecture

| Question | Position |
|---|---|
| Authoritative fact | the **financial fact** `F3` — a signed amount in a stated currency against a classification |
| Immutable | the whole core of `04 §2` |
| Never overridden | `Σ signed = 0`; sign **and magnitude** agreement; settlement ≤ residual; measurement present |
| Failure modes | `T-17` wrong measurement rule is **stated but unevidenced** |
| Evidence | `ST-03`, `COR-06`, `COR-09` |

**Position:** `Debit = Credit` is necessary and grossly insufficient — **7 of 19** balanced-but-wrong
classes are fully answered. **`P-02` declines to treat the design as sound while `T-17` has no
mechanism.**

### `P-03` Data / Identity / Temporal Architecture

| Question | Position |
|---|---|
| Canonical identity | independent of storage identifier, tenant-scoped |
| Immutable | identity, always |
| Derived | every label, every aggregate |
| Configurable | labels, presentation, template membership |
| Never overridden | identity, temporal validity |
| Failure modes | **`T0-08` is unresolved** — identity is journal-scoped, conditionally enforced, escapable by blanking the number |

**Position:** `VF-03` — no temporal validity anywhere — is the **most under-weighted finding in the
whole programme**. It is recorded as a consequence for comparative reporting; it is in fact a
constraint on *every* configuration change the system will ever make. Recorded as `X-B`.

### `P-04` SaaS / Tenant / Company Isolation Architecture

| Question | Position |
|---|---|
| Tenant-owned | every control-affecting configuration; all control evidence; template membership |
| Company-owned | journals, entries, items, liquidity accounts, locks |
| Configurable | labels, template customisation within bounds |
| Never overridden | tenant isolation — `Tolerance = 0` candidate (`CR-06`) |
| Failure modes | **unquantified.** 9 of 192 assessed, over a path set short by 962 modules |

**Position — and it is a veto, recorded in `18`:** no isolation claim may be made. `P-04` additionally
holds that `SB-01` alone (a control store with **no company dimension at all**) is sufficient to
prevent any multi-tenant deployment claim, independent of the other 191 sites.

### `P-05` Integration / Localization / Thai Statutory Architecture

| Question | Position |
|---|---|
| Authoritative fact | for tax, the **tax point** — which has **no carrier** |
| Owner | `WAVE-D TAX` owns content; **Wave A owns the carrier** |
| Failure modes | tax lock, return population and statutory extracts all operate on the accounting date — *the one date the user does not control and the system silently moves* |

**Position:** this is the sharpest Wave A finding for a Thai deployment, and `09 §1` is right to carry
the field even though the content is out of scope. **All statutory claims remain `HOLD / EVIDENCE
REQUIRED`** and none is used as design authority. `P-05` notes the localisation surface is itself
implicated: **904 of 906 localisations sit in the 962 unsearched modules** (`GB-07`).

### `P-06` Security / Authorization / Auditability Architecture

| Question | Position |
|---|---|
| Never overridden | immutability of an asserted fact; the irreversible close |
| Failure modes | `MCU-01` suppression reachability **open**; `T0-10` lock exception **open**; 93 elevation sites **0 assessed**; 62 raw-SQL sites **0 assessed** |

**Position:** `CR-07` — *prove the executor of every declared control* — is the single most
transferable rule the programme has produced, and `T0-09` is its proof case: **16 declared guards that
do not execute at write — present in the view layer only, over a population floor of 30 declarations across 4 files of which one is named, leaving `T0-09` unbounded.** `P-06` holds that **no control in this design may be accepted on its declaration
alone**, including the controls this design itself proposes. Recorded as `X-C`.

### `P-07` UX / Operational Control Architecture

| Question | Position |
|---|---|
| Visible to the operator | every accounting event, including system-emitted ones |
| Failure modes | four events are invisible at the moment they occur (`VF-19`) |

**Position:** `AE-03` — re-dating on a document-date change, with **no lock configured** — is the worst
because it is invisible *and* routine. Under `VF-06` it fires on ordinary same-month entry.
**Concern:** `DP-04` ("where the system must choose a date it cannot derive, it stops and asks") is the
right rule and the least designed part of the package. Recorded as `X-D`.

### `P-08` Migration / Historical Continuity Architecture

| Question | Position |
|---|---|
| Authoritative fact | the opening position, **with provenance to its origin** |
| Failure modes | tamper-evidence **cannot survive migration** (`SB-03`); migrated rate rows never revalidated (`MCU-19`); opening valued at a 2010 rate (`BW-30`) |

**Position:** `D-14` is not a nice-to-have. **Tamper-evidence that breaks on migration is
tamper-evidence absent exactly when assurance is demanded.** `P-08` also flags that `MCU-19` — *"one
`SELECT` answers it"* — is the cheapest open item in the entire programme and remains unrun.

### `P-09` Reporting / Reconciliation Architecture

| Question | Position |
|---|---|
| Authoritative fact | the ledger; the report is a **projection** |
| Failure modes | **`T-19`** — nothing in the ledger is wrong and the reported figure still is |

**Position:** `T-19` is the class most likely to be under-defended, because it is the only class where
**every ledger invariant holds**. `MCU-04` (no company dimension on report definitions) and `MCU-11`
(caller-supplied scope, no defence in depth) are gating, and `BW-31`/`MCU-20` adds a v19 path that
aggregates at today's rate **outside every record rule**. `P-09` holds that reporting integrity is a
Wave A concern that has been routed to Wave G by convention rather than by evidence. Recorded as `X-E`.

### `P-10` Independent Audit Veto / Contradiction Review

Reported separately in file `18`, and augmented by two fresh independent reviewers with disjoint
adversarial assignments who did not author this package.

---

## 2. Cross-perspective agreement

**Unanimous across all ten:**

1. The accounting event must be separated from the entry (`D-01`).
2. Immutability must be unconditional and enforced below the application (`D-02`, `ADR-02`).
3. Correction is additive and the linkage must be constrained (`D-03`).
4. Provenance is part of the fact (`D-04`).
5. No measurement fallback of any kind (`D-09`).
6. **No tenant-isolation claim may be made from the current evidence.**

---

## 3. Preserved disagreements — NOT dispositioned

| id | Perspective | Disagreement | Why it is not resolved here |
|---|---|---|---|
| `X-A` | `P-01` vs `P-02` | Removing un-posting: `P-01` wants the operator's current use established first; `P-02` holds that a destructive path's business popularity is not an argument for retaining it | Both are right on their own axis. **Needs a business observation, not a research read** |
| `X-B` | `P-03` vs the package | `P-03` holds `VF-03` (no temporal validity) is under-weighted and should force `D-21` to `PROVISIONAL`; the package holds it at `PROVISIONAL` because it rests on `GAP-A03`, an **orphan unclassified id** | Resolvable by **classifying `GAP-A03`** — cheap and not on the parent worklist |
| `X-C` | `P-06` vs the package | `P-06` holds that no control this design proposes may be accepted on its declaration; the package states control rules without specifying executors | **Legitimate.** The design is at the level of *what must be true*, not *what enforces it*. Recorded as a known limit of this stage |
| `X-D` | `P-07` vs the package | `DP-04` is under-designed | Accepted as a gap, not resolved |
| `X-E` | `P-09` vs the routing | Is reporting integrity a Wave A or Wave G concern? | **Routing decision, not a research finding.** `MCU-04`/`MCU-11` are gating in Wave A regardless |

> **Five disagreements stand. None is resolved by authority in this file.** `X-B` is the only one
> closable by a cheap, well-defined action.

---

## 4. What the expert body will not say

No perspective states that the design is complete, converged, safe to implement, or ready for a gate.
`P-04` and `P-06` both hold that material components cannot be assessed at all on current evidence.
**The expert body's collective position is that this package is a candidate set, not an architecture.**
