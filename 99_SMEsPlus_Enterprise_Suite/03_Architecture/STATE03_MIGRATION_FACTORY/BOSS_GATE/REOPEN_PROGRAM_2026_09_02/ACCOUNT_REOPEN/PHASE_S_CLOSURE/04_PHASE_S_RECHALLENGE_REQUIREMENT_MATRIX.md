# 04_PHASE_S_RECHALLENGE_REQUIREMENT_MATRIX

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-PHASE-S-CLOSURE-001]` · branch `audit/account-phase-s-closure-2026-09-06-001`

> **The rule (§7).** If a surface changed after the independent challenge, **the old challenge does not
> validate the new surface.** **This session launches no challenge, selects no challenger, satisfies no
> requirement, and declares no surface validated.**

## Disposition: CONSUMED BY REFERENCE

| | |
|---|---|
| **Authoritative artefact** | `05_CORRECTED_SURFACE_RECHALLENGE_REGISTER.md` |
| **Branch / SHA** | `audit/account-xrecon-2026-09-06-001` @ `32912109d37117aae1e91cb612c36c67c9be70a4` |
| **Path** | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_XRECON_2026_09_06/05_CORRECTED_SURFACE_RECHALLENGE_REGISTER.md` |

## 1. Requirement position — 6 required, 1 explicitly not required, 0 complete

| # | Surface | Owner | Status | Independence bar |
|---|---|---|---|---|
| **`RC-01`** | P09 corrected surface — 6 artefacts edited in place at `4778792` | P09 | **NOT CHALLENGED** (= `M-2`) | **P09 may not select its own challenger** |
| **`RC-02`** | P11 CORR3 post-challenge edits (`B-37`; 40 → 41) made **after** the four AAS-03 experts read `9356557` | P11 | **NOT RE-CHALLENGED** | **P11 may not draw CORR4's control set** — its own item 2 says so |
| **`RC-03`** | P06 IEV revised totals 18 → 25 / 15 → 19 / 3-of-4 → 4-of-4 | P06 IEV | **NOT CHALLENGED at the revised totals**; Expert 2's 12 findings adjudicated **by the verifier alone** | **barred to the P06 IEV actor twice over** — `AASP-VETO-07` §9 **and** `XRD-009` |
| **`RC-04`** | P06 source, once `XRD-003`/`XRD-004` repaired | P06 | **PRE-EMPTIVE — surface does not yet exist** | repairing party may not challenge its own repair |
| **`RC-05`** | P08 `58_` §1 item 1, once the figure is deleted and balances re-run in exact arithmetic | P08 | **PRE-EMPTIVE** | as above; **P11 must be re-notified** |
| **`RC-06`** | P11 `F-02` + the derived method rule, re-run against exact arithmetic | P11 | **PRE-EMPTIVE** | as above |
| **`RC-07`** | P08 repair-requirement numbering | P08 IEV | **NOT REQUIRED** — pointer-only, no substantive surface change | — |

**6 required · 0 launched · 0 complete · 0 challengers selected.**

## 2. The single constraint binding every row

**`AASP-P11-C3-VETO-04` — *no control set drawn by the party it controls*.** Adopted across the accounting
house; it binds all six.

> **A verifier cannot satisfy an independence requirement by writing its own control set, testing its own
> correction, reading its own result and calling the outcome independent.**

**Two of the three tracks in this programme have already done a version of exactly that, and both disclosed
it themselves.** That disclosure is the reason `XRD-009` is reserved to the Boss rather than repaired.

## 3. Why none can be launched now

**All six are downstream of surfaces that do not yet exist or of `PHASE-S/Q-BOSS-01`.**

- `RC-04`, `RC-05`, `RC-06` are **pre-emptive**: their surfaces are created *by* the corrections that
  `PHASE-S/Q-BOSS-01` gates. **Challenging them now would be challenging nothing.**
- `RC-01`, `RC-02`, `RC-03` have surfaces that **do** exist — but each requires a challenger the owner
  may not select, and **selecting and tasking a challenger is an execution act** under §5(G)–(H), which
  §4 bars until authorization is recorded.

**`RC-01` and `RC-03` are the two nearest-term items.** Both are challenges of surfaces already published,
needing no prior repair. **If the Boss authorizes narrowly, these two are executable first** — recorded as an
option in `06_`, **not** as a recommendation this session is entitled to make.

## 4. Re-challenge invalidation rule carried forward

Per §7(9): **any new material correction after a challenge invalidates that challenge for the changed
surface and requires a fresh challenge of the changed surface.** With 6 requirements already open and 13
corrections queued, **the completed-challenge count can fall as well as rise.** No closure arithmetic in
`05_` treats a challenge as permanently satisfied.
