# P07 — AAS+ CONSOLIDATION

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
Reconciles the four AAS-03 challenges against the round's findings. **AAS+ does not adjudicate
between an expert and the evidence; it records what the challenge changed.**

## 1. What the Challenge Round Changed

Four challenges, **three of which changed a published statement before it was published**.

| challenge | verdict | effect on the finding |
|---|---|---|
| `CH-A` — the instrument counted fields **added**, not fields **read** for period placement | **ACCEPTED** | `P07-F-105` restated: *no carrier **added** by the Thai localisation.* Its scope shrank; its truth did not move. |
| `CH-B` — the 199 divergences are a rate-edit artefact, not a defect | **FAILED ON MEASUREMENT** (`EP-6b`) | `P07-F-109` **strengthened**: 151 of 199 cannot be a rate edit at all, and the other 48 carry no rate-edit signature. `P07-C-29`. |
| `CH-C` — `l10n_th*` is not the population "Thai tax code" | **ACCEPTED** | `P07-F-105` carries a binding scope note; `EP-1`'s widening control recorded as **insufficient** (`REV-E-95`); `REV-M-98` generalises it. |
| `CH-D` — `P07-F-108`'s severity assumes multi-record recompute is common | **PARTLY ACCEPTED** | The basis for `S2` is written down as `SUPPORTED INTERPRETATION` so a reader can weigh it down. `DIS-02` preserved. |

**The most useful single event of the round was a failed disproof.** `CH-B` tried to remove
`P07-F-109` and, in doing so, produced the measurement that makes it defensible — the 151/48
split. **A challenge that fails on measurement leaves the finding better evidenced than a
challenge that never ran**, and that is the argument for keeping a disproof mandate rather than
a review.

## 2. Convergence and Non-Convergence

**Converged** — all four perspectives agree, with no dissent recorded:

- The lineage gap is structural, and `L-3` — **no filed figure is stored anywhere** — is the
  single largest one in the P07 surface. Nothing can be reconciled to a filing that was never
  kept.
- No statutory position was taken this round, and none may be inferred from any behaviour.
- The domain boundary held: eight contamination stops, no peer's internals read.

**Not converged, and deliberately left so:**

| # | The disagreement | Why it is not resolved |
|---|---|---|
| `DIS-01` | `CH-B` will not attribute `P07-F-109` to `P07-F-108`; the round does not either | The evidence needed is a **write sequence**, which no database holds. `P07-U-35`. |
| `DIS-02` | `CH-D` holds *latent* understates a stored, queryable, invisible wrong figure; `P07-F-110` reports install state and no more | Both are true statements about different time horizons. |
| `DIS-04` | `CH-A` holds `PS-08`/`PS-09` read as recommendations | Deleting them loses the discovery; classing them harder does not stop a determined reader. |

## 3. The Round's Own Error Record

**Three errors, all caught before publication, and two of them the same kind.**

| # | Error | Kind | Caught by |
|---|---|---|---|
| `REV-E-93` | `tax_ids` on `account.move` read as a shadowing data carrier; it is `compute=`, unstored, a domain helper | **a source fact read as a runtime fact** | reading the definition instead of the AST summary |
| `REV-E-94` | `P07-F-109` drafted as **live** because a remittance document reads the stored value; that module is uninstalled in 6 of 7 and absent from the 7th's registry | **a source fact read as a runtime fact** | the latent-vs-live rule, applied before writing |
| `REV-E-95` | `EP-1`'s widening control answered the wrong question | **a control that could not detect its own failure** | `CH-C` |

**Two of three were the same defect class, committed twice in one round, by an author who holds a
written rule against it.** *Having the rule, recalling it, running it, and running it on the right
axis are four different things* — and the third instance was caught by a challenger, not by the
author, which is the same distribution this package has recorded in every previous round.

**The self-caught two were caught by a rule; the challenger-caught one was caught by a
perspective.** Scaling the rule harder would not have found `REV-E-95`, because the rule was
being followed — it was pointed the wrong way.

## 4. What AAS+ Will Not Certify

- **No exit criterion is met.** `EC-01`…`EC-08` are untouched by this round; `EC-04`'s
  tolerance-zero boundaries remain open in P07's own subject matter.
- **No blocker closed.** `X-07`, `X-08`, `X-09` gained a committed counterparty half and remain
  `BLOCKING for P07`.
- **`AASR-P07-VETO-01` is not discharged.** It rests on `P07-U-03` — the legal basis of the
  deferred input-tax claim — and no primary statutory source was obtained this round or is
  obtainable from this host.
- **No implementation, no merge, no freeze, no design.** PHASE B was not entered and AI EOS was
  not invoked.

## 5. AAS+ Position

The round did what a closure round should: it consumed published peer evidence, executed five
bounded passes against declared denominators with firing controls, **contradicted one peer
`FACT VERIFIED` on measurement**, produced seven findings and three open items, survived a
disproof attempt on its most consequential claim, and narrowed two of its own statements before
publishing them.

**It closed nothing, and it was not supposed to.** PHASE S discovers candidates. The candidate
pack is a candidate pack, the statutory questions are still statutory questions, and the one
category of evidence that would settle three of the oldest open items — a controlled execution —
is still not authorised.

`RECOMMEND HOLD` is upheld, unchanged and unchanged throughout.
