# P11 — CORR3 MANDATORY INTAKE CASE DISPOSITIONS

`[SMEPLUS-26-09-06-…-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-04` · **PHASE S**

> The five cases §7 of the controlling prompt names as minimum. **Each opened at the frozen SHA. No
> peer internal, database, module or source tree was opened for any of them.**

---

## `IC-01` — `P01` received-not-invoiced · **`B-28`**

**Opened:** `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md` §6 @ `b820b29`.

| Element | Owner's statement, verbatim where quoted |
|---|---|
| Position | **`฿29,029,467.66` tax-exclusive** across **1,580 PO lines**, *"received and not invoiced … **recognised nowhere in the ledger** — no receipt entry, no clearing balance, **no accrual**"* |
| **Decomposition P11 must carry** | **`฿27,490,865.80` on 1,411 lines is backed by an actual goods receipt**; the remaining **`฿1,538,601.86` on 169 service lines** is *"an operator-typed quantity with no receipt document and **should not be read as received**"* |
| Companies | 1 → `฿14,692,566.42` · 2 → `฿14,336,901.24` |
| Unit | **one PO line, tax-exclusive, THB**, rate 1.0 on all 13,887 orders, discount zero on every line (both by enumeration), **excluding `cancel` and `draft`** |
| Counterparts | **183 lines invoiced-not-received, `฿1,663,518.07`**; **18 lines over-received, `฿1,669,526.29`** |
| **Superseded figure** | ~~`฿30,080,689.78`~~ — *"summed two tax bases; 312 of the 1,580 lines carry VAT-inclusive unit prices. Overstated by `฿1,051,222.12`, 3.49 %"* — **`ERR-P01-28`**, corrected after adversarial challenge |
| Control | accrual control **0 of 15,522** entries carry `accru` in `ref`; **positive control 15,434 have a non-empty `ref`** |

> ### The owner's own disposition, which P11 adopts and does not exceed
> *"**This is a timing position, not a missing transaction**, and under periodic valuation no
> receipt-time entry is expected. It is a **completeness question at a reporting date**, and it is
> **P08's judgement and the Boss's decision**, not P01's."*

**Disposition: `CANDIDATE INPUT — NOT PROMOTED`.** CORR2 registered this as *"the largest unrecognised
accounting position in the frozen evidence"* — **that framing is withdrawn**. The owner classifies it
as a **timing position expected under periodic valuation**, and P11 has no evidence to classify it
otherwise. **`B-28` is re-worded**: the defect was P11's *non-intake*, not the position itself.
**Routed to `P08` (judgement) and `Boss` (decision).** `P11-E-41`.

## `IC-02` — `P02` *"What P11 Receives"* — the artefact CORR2's instrument could not see

**Opened:** `43_G02_P02_FINAL_CLEANROOM_HANDOFF.md` §5 @ `7cb1c27`. Found by `D2` only.

| P02 hands P11 | Content |
|---|---|
| **Three scope holds** | currency rate · chart of accounts · intercompany execution |
| **Six design candidates** | obligation position · **event identity** · **two-date model** · close-means-closed · deterministic account derivation · **deny-on-missing-scope** |
| **One invariant finding** | *"**one business fact → one canonical event owner → one accounting effect path** is **not** satisfied by the reference **at the correction/reversal stage**"* |

> **P02 reached the programme's governing invariant independently and located its failure precisely —
> at correction/reversal.** `P10` reached the same conclusion from the recognition side and said so.
> **Two processes, two routes, one invariant, one named failure point.**
>
> **This is a genuine convergence and it is the one CORR2 should have had** instead of `P11-C-09`.
> Registered **`P11-C-15`**, and — unlike `P11-C-09` — **the independence is testable and tested**:
> the two statements arise in different packages, from different evidence, neither citing the other.

**Disposition: `CANDIDATE INPUT — CONSUMED`.** Three of P02's six design candidates (**event identity**,
**two-date model**, **deny-on-missing-scope**) correspond to `D-5`, `CQ-P11-04` and the scope rule P11
already carries — **corroboration, not new obligation.**

## `IC-03` — `P09` `D26` / `D27` chain

**Opened:** `D26_P09_V18_DEPLOYMENT_CORROBORATION.md`, `D27_P09_EVIDENCE_BASE_CENSUS_B5_DISCHARGE.md`
@ `4778792`. Found by `D3` only, and `D26` only after the third instrument revision.

| Generation | Current statement |
|---|---|
| `D26` | **`B7` PARTIALLY WITHDRAWN** — *"Every mechanism claim in this programme is version-matched to at least two real deployments."* Two v18 deployments exist |
| `D27` | the `99.6507 % / 17,465` headline is *"**unchanged in value, narrowed in scope** — one artefact out of **17**, not one out of five"*; **`B5` NARROWED, NOT CLOSED**, 8 artefacts unread; issues **`NC-12`** coverage assertion and **`NC-13`** per-artefact positive control |
| **Newly read this round** | `P09_FINAL_BOUNDED_COMPLETION_REGISTER.md`: ~~*"NOT ESTABLISHABLE"*~~ → **the SOURCE generation is established: 18.0 Enterprise** — *"a discharge in P09's favour, **found by a challenger and not by the author**"* |

**And P09 publishes the ladder P11 needs for `B-21`:**
`source present` **YES** → `installed` **NOT ESTABLISHED** → `configured` **NOT ESTABLISHED** →
`exercised` **NOT ESTABLISHED** → `economically correct` **NOT ESTABLISHED`.
*"A translation header establishes a source generation, never a deployment."*

**Disposition: `CURRENT OWNER STATEMENT — CONSUMED`. `B-23` stays withdrawn.** `NC-12`/`NC-13` and the
five-rung ladder are **adopted into P11's method** (`P11-G-08`).

## `IC-04` — `P06` qualifier, and written-vs-delivered

**Opened:** `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` @ `1b018c1` (**changed** since CORR2).

- **Qualifier PRESERVED, verbatim:** `REACHABLE — DEPLOYMENT VERIFIED` *"on a v19 database **not
  confirmed to be the SMEsPlus target**"*, *"(v18 source chain: **SOURCE-REACHABLE / RUNTIME
  UNVERIFIED**)"*, *"**`iEVING` is a BHPRO database**"*. **P11 does not restate this as a platform
  property.**
- **Delta at the new head:** ~~58 blockers~~ → **65 at the current frozen surface**, marked
  `REV-E-23` as *"stale current claim … **invisible to the pattern declared for its class**"*.
  **P06 diagnoses in its own package the same instrument-class defect CORR3 diagnoses in P11's.**
- **Written vs delivered:** P06 states it *hands* items to P11. **No receipt evidence exists in either
  package.** → `P11-B-31`.

**Disposition: `CANDIDATE INPUT — CONSUMED, QUALIFIER INTACT`.**

## `IC-05` — `P08` veto evidence, and five corrections to claims P11 carried

**Opened:** `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` @ `00ccd66` (**changed** since CORR2),
`62_P08_AAS_PLUS_PHASE_S.md`, `63_P08_PMO_PHASE_S_REVIEW.md`.

### Veto status — recorded, not discharged
**`AAS+-VETO-01`'s two conditions remain UNDISCHARGED.** New `AAS+-PS-VETO-01`, consolidated from four
independent vetoes, *"**does not lift** `AAS+-VETO-01`"*. **P11 does not discharge a P08 veto.**
**`P08`'s own terminal state is `TERMINAL STATE C — EVIDENCE INTEGRITY OR DOMAIN-PURITY FAILURE`.**

### Five claims P11 carried that P08 has corrected at the new head

| P11 carried | `P08` current |
| *(row 1 below is itself superseded — see `Q-P11-04`: the `1e-7 = 3` figure has **no referent**; P08's independent verifier found **0 at exact equality**)* | |
|---|---|
| *"complete and arithmetically sound — 0 unbalanced posted entries across 169,143"* | **the word "complete" is WITHDRAWN** (`P08-CONTRA-73`); ~~0 holds **at tolerance ≥ 0.005** — *"at 1e-7 the answer is 3, all float artefacts on eight-figure sums"*~~ **SUPERSEDED `2026-09-08` (`P11-C6-01`): 0 at EXACT EQUALITY and at every tested tolerance, on both columns, across the four frozen RC-05 extracts. P08 `f0cf287ac9f4ad37b0c19145df4a0e396af84c13`. The `1e-7 = 3` figure has no referent and is deleted, not re-scoped.** **The `"complete"` withdrawal is UNAFFECTED and still stands** — it rests on a raw-SQL deletion path, not on arithmetic. |
| *"attribution 447,384 of 447,384"* | **unit note added**: that is the **all-states** item population; **the posted population is 417,700** |
| *"96.1 % of posted entries carry an origin pointer"* | **CORRECTED to 78.03 %** structured (`P08-CONTRA-63`). The 96.1 % counted **free-text reference**; the difference is **~30,750 entries whose only provenance is unparsed text** |
| *"no accounting-period object"* (`T0-15`) | **RE-SCOPED** (`P08-CONTRA-68`) — absent **in the declared 18.0 root set only**. *"The 19.0 line carries a dated, recurring return object, and both 19.0 deployed databases carry its linking column."* — ***"P11 must not receive the absolute"*** |
| *"settlement chronology untrustworthy — 46.4 % after / 44.3 % before"* | **WITHDRAWN** (`P08-CONTRA-57`) — the as-of date is *"computed by the accounting kernel as the later of the two items' accounting dates"*; the split compared a **write timestamp** against a **derived date** and *"**contains no defect**"* |

### And one new `CRITICAL` handoff — `P08-HO-13`

> **`P08-CONTRA-55`** — *"the single most consequential omission from this handoff."* A module
> ~~**installed in all three deployed databases**~~ → **installed in all FOUR frozen RC-05 extracts** **[`P11-C6-04`, 2026-09-08 — population premise re-pointed to P08 `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`.** The deletion module records an **installed** state in **all FOUR frozen RC-05 extracts**, read from each extract's own module registry. **Four frozen extracts are NOT an established deployment census** and P11 does not upgrade them into one. **`exercised` remains NOT ESTABLISHED** — install state is capability, not act.]** deletes, in unqualified raw SQL and in this order:
> the **settlement table**, then the **journal item table**, then the **journal entry table** — *"no
> company predicate, no state predicate, a commit after each table"* — and **resets the entry-number
> sequence to 1**.
>
> **P08 states the consequences against its own package:** the settlement graph it offered as
> reconcilable *"is deletable outside the object layer"*; posted entries *"are removed exactly as
> drafts are"*; the one control `56` §2 ranked as holding *"does not"*; and a sequence reset
> **permits previously-issued entry numbers to be re-issued**.
>
> **Execution:** *"Whether it has ever been executed on any deployment is **not verified by P08** — a
> peer has published an observation to that effect and it is recorded as **received and attributed,
> not re-derived**."* **P11 mirrors that discipline exactly.**

### The version standing P08 attaches to its own handoff

> *"This file carries **zero version markers across 29 table rows** … **Every kernel claim in this
> handoff rests on the 18.0 line. No deployed database runs it.** … **P11 must read every row of this
> handoff as an 18.0 statement until it is re-derived on the line the consumer actually runs.**"*
> — `P08-U-28`

**Disposition: `CANDIDATE INPUT — CONSUMED UNDER VETO AND UNDER `P08-U-28``.**

---

## Summary

| | |
|---|---|
| Mandatory cases | **5 of 5 dispositioned** |
| Artefacts opened this round | **21** |
| P11 claims corrected by intake | **6** (five from `P08`, one from `P01`) |
| New `CRITICAL` received | **1** (`P08-HO-13`) |
| New convergence, independence tested | **1** (`P11-C-15`) |
| Peer internals opened | **0** |

**`CP-P11C3-04` — COMPLETE — EVIDENCE VERIFIED.**
