# 05_CORRECTED_SURFACE_RECHALLENGE_REGISTER

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`

> **The rule.** If a surface was changed after the independent challenge, **the old challenge does not
> validate the new surface.** This applies to wording that carries substantive meaning, denominator,
> classifier, predicate, regex, search instrument, population, union, handoff, table, producer, control and
> evidence reference.
>
> **This session generates the challenge requirement. It does not launch, run or satisfy any of them.**

---

## 1. Register

| # | Surface | Owner | What changed after challenge | Challenge status | Requirement |
|---|---|---|---|---|---|
| **`RC-01`** | **P09 corrected surface** — 6 artefacts edited **in place** at `4778792` | **P09** | `L-1`…`L-8` closures; the `ZERO` claim struck; `CO-02b` marked superseded; the `CH-09` *deleted* disposition superseded by a tombstone; **the false *"P11 has published no branch"* withdrawn in 3 files** | **NOT CHALLENGED.** P09 names this itself as **`M-2`** | **FRESH BOUNDED CHALLENGE REQUIRED** on the corrected surface only |
| **`RC-02`** | **P11 CORR3 package** post-challenge edits | **P11** | `B-37` correction to `P11_AUTO_RESUME_STATE.md` (CORR2 heads → CORR3 heads, error count 40 → 41) — made **after** the four AAS-03 experts read the frozen surface `9356557` | **NOT RE-CHALLENGED.** P11 names it as CORR4 item 7 | **FRESH BOUNDED CHALLENGE REQUIRED** |
| **`RC-03`** | **P06 IEV totals** 18 → 25 / 15 → 19 / 3-of-4 → 4-of-4 | **P06 IEV** | The addendum revised five headline totals **after** publication at `dac6ac3` and **after** its own challenge round closed | **NOT CHALLENGED at the revised totals.** Expert 2's 12 findings were adjudicated by the verifier alone | **FRESH BOUNDED CHALLENGE REQUIRED** — and, per `XRD-009`, **not by the same actor** |
| **`RC-04`** | **P06 source package**, once `XRD-003`/`XRD-004` are repaired | **P06** | four count families corrected; the archive negative re-run on a firing pattern; `FTB-F-07` re-stated | **PRE-EMPTIVE** — the surface does not yet exist | **FRESH BOUNDED CHALLENGE REQUIRED** at repair completion |
| **`RC-05`** | **P08 `58_` §1 item 1**, once the *"3 at 1e-7"* is deleted and balances re-run in exact arithmetic | **P08** | the outbound figure and every balance measurement | **PRE-EMPTIVE** | **FRESH BOUNDED CHALLENGE REQUIRED**, and **P11 must be re-notified** — `XRD-011` |
| **`RC-06`** | **P11 `F-02`** and the derived method rule, once re-run against exact arithmetic | **P11** | a falsification result and a standing method rule | **PRE-EMPTIVE** | **FRESH BOUNDED CHALLENGE REQUIRED** |
| **`RC-07`** | **P08 repair-requirement numbering**, once `XRD-007` is fixed | **P08 IEV** | a cross-reference only | **NOT REQUIRED** — pointer-only, no substantive surface changes | none |

**Six fresh bounded challenges required. One explicitly not required.**

## 2. The independence constraint on every one of them

**`AASP-P11-C3-VETO-04` — *no control set drawn by the party it controls*.** Adopted across the accounting
house. It binds every row above:

- **`RC-01`** — P09 may not select its own challenger for `M-2`.
- **`RC-02`** — P11 may not draw CORR4's control set. Its own CORR4 item 2 already states this:
  *"re-certify on a control set P11 did not choose — the full published twelve, `S06` included"*.
- **`RC-03`** — barred to the P06 IEV actor twice over: by `AASP-VETO-07` §9 (discharge reserved to *"an
  independent verifier that completes this prompt"*, which that verifier states it is not) and by
  `XRD-009`.
- **`RC-04`, `RC-05`, `RC-06`** — the repairing party may not challenge its own repair.

**A verifier cannot satisfy an independence requirement by writing its own control set, testing its own
correction, reading its own result and calling the outcome independent.** Recorded here because two of the
three tracks in this reconciliation have already done a version of it, and both disclosed it themselves.

## 3. What this session did NOT do

| | |
|---|---|
| Launched any challenge | **NO** |
| Satisfied any challenge requirement | **NO** |
| Selected any challenger | **NO** |
| Declared any surface validated | **NO** |

**Every requirement above is routed into `07_` and `08_` as a child-prompt obligation.**
