# P11 — C10 · AAS+ CORR1 CONSOLIDATION

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C10 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **Independence limitation:** one commissioned panel, bounded to `11f473f`, plus P11's own execution.
> **P11 broke freeze-before-review** (`P11-E-30`), so the panel's coverage of everything after
> `11f473f` is **incomplete by construction**. Weight accordingly.

---

## 1. Agreements

1. **The peer intake was the round's real work and it holds** — 10 of 10 consumed, SHAs accurate, all
   ten publish a handoff pack. The panel could not break any of it.
2. **The population re-derivations were right to distrust the prompt** — 13 decisions not 12; 11
   tolerance-zero carried by id against 13 inherited. The panel expected 10 inherited *"and was wrong"*.
3. **`B-18`'s closure is evidenced**, with declared controls, over its declared population.
4. **`B-17`'s re-run is honest in direction** — it makes the headline worse and says so.

## 2. Disagreements — none standing

**18 findings raised, 18 accepted, 0 disputed.** P11 verified all three `CRITICAL`s at source before
accepting. As at `P11#04`, a `0`-disputed figure is **uninformative about deference, not reassuring** —
and this round supplies the reason it should be read that way: the panel's central finding is that P11
**quoted a peer's refusal to take a favourable reading, and then took it.**

## 3. Contradictions the round exposed inside P11

| Class | Instance |
|---|---|
| **A superseded artefact read as current** | `C-01`/`B-01` — `S8`. Right branch, right SHA, **wrong file**, twice |
| **A control that omits the step it exists to enforce** | `B-03` — `D-3b` v4 has no population element, so it certified *"2 of 2 ⇒ complete"* over a population of **≥9** |
| **A headline contradicting its own table** | `A-05` — *"5 strengthened"* against six marked rows. **The `P11-E-01` class, inside the correction round** |
| **A pattern that cannot see its own file** | `D-03` — a row-pattern missed *"ten named decisions"* in prose in the file it declared as authority |
| **Discharge on the wrong condition** | `C-05` — `B-12` discharged on *publication*; its condition was *contract establishment* |
| **A scope crossed that the source forbids** | `C-02` — a source-line (18.0) fact presented as deployed-estate evidence |
| **An embargoed inheritance** | `C-03` — `KRN-INV-00` is `CONTESTED` and *"must not be inherited downstream"* |
| **Freeze-before-review broken** | `D-07` — P11 edited the package under review, closing the only `CRITICAL` mid-review |

## 4. Risks

| id | Risk |
|---|---|
| `AASP-C1-R-01` | **The round's headline was wrong for ~90 minutes and was published.** It was withdrawn only because an independent panel opened a file P11 had not |
| `AASP-C1-R-02` | **`S8` is unbounded.** P11 checked two peers for superseding artefacts *after* being told. **Eight peers are unchecked**, and `P11-G-04` v1 would not have caught any of them |
| `AASP-C1-R-03` | **The Boss-decision population is a floor**, with ≈7 peer-routed decisions outside §31 and 3 P11 blockers Boss-required without ids |
| `AASP-C1-R-04` | **The dump population is a floor of 9**, and a **third format** exists that needs no client version — so `D-3b` v4 is already insufficient as specified |
| `AASP-C1-R-05` | **P11 closed the round's only `CRITICAL` while its own commissioned review was running.** The closure did not survive |

## 5. Vetoes

> ### `AASP-P11-C1-VETO-01` — **UPHELD and WIDENED.**
> **No part of this package may be relied on as a cross-process reconciliation.** Widened because the
> round demonstrated that P11 can consume the right peer at the right SHA and still read a **withdrawn**
> claim. Lift conditions: **(1)** every consumed artefact recorded by path **and** SHA, with a
> superseding-version check across **all ten** peers; **(2)** `D-3b` v5 with a population element;
> **(3)** the 18 findings corrected at source and **audited by text, not by disposition**.

> ### `AASP-P11-C1-VETO-02` — **UPHELD.**
> **No design position may seed implementation.** Unchanged, and now joined by `AASP-VETO-01` r3 from
> `P10`, which *"REMAINS AND IS STRENGTHENED … lifts only on both Boss decisions"* and **binds `D-5`
> and `T0-13`** — a veto P11 had not recorded until this round.

## 6. Verdict

> ## `NOT CONVERGED — P11 CORR2 REQUIRED`
>
> CORR1 **repaired real method integrity** — two tolerance-zero boundaries recovered, the decision
> population corrected, an eighth ordering surface found, the peer intake completed for the first time.
> **And its headline result was wrong and has been withdrawn.**
>
> **A round that both fixes the method and publishes a false headline has not converged. It has
> demonstrated the method working, on itself, one cycle late.**


---

## 7. ADDENDUM — `2026-09-05`, after `CP-P11C13`

**`AASP-C1-R-02` was under-stated by this consolidation and is corrected here rather than rewritten
above.** It read *"eight peers are unchecked"*. The check has now run over all ten
(`P11_S8_SUPERSESSION_RERUN_CORR1.md`):

> **`6 of 10` peers carried a later artefact P11 had not consumed — not two.** One chain
> (`P09` `S18_` → `S23_`) runs **two deep** and would be missed by any check asking *"is there a V2?"*,
> because both names are `S`-prefixed sequence numbers.

**What this does to the verdict above: nothing, and that is the point.** `NOT CONVERGED — P11 CORR2
REQUIRED` was already the finding. The re-run **enlarged the package it applies to**: blockers
`20 → 24` including a second `CRITICAL` (`B-21`, `om_data_remove` **installed** on a v19 database in
the estate), tolerance-zero `13 → 14`, decisions `13 → 16`, and a **second P11 claim withdrawn**
(*"nets to zero"*, now a sign-inverted **CREDIT** of `+3,595,851.11`).

**Two peer vetoes now bind P11's method directly** (`P06 AASP-VETO-04`, `P09 AAS+-VETO-04`) — accepted
without dispute, and `AASP-P11-C1-VETO-01`'s lift condition **(1)** is amended to require the
supersession check at **claim** level, not artefact level (`P11-G-04` v3).

**Against that, the round produced its first genuine cross-process convergence** (`P11-C-09`): three
processes independently requiring an identity, a date and a reversal link of a settlement event.
**It motivates `D-5`; it does not evidence it.**

> **The consolidation's own limitation, restated honestly:** this addendum was written by P11 about
> P11's own re-run, **after** the independent panel had closed. It is not independent review, and it
> should not be read as any. **The panel's coverage gap recorded at `P11-E-30` is now larger, not
> smaller.**
