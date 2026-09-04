# ACCOUNT WAVE A — MCC FINAL GATE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc`
Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001` · Standard `SMEPLUS-DR-MC-001`

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**
> All figures resolve against `MCC_00_CANONICAL_FIGURES_REGISTER.md`.

---

## 1. What was asked, and what happened

**Asked:** stop broad research. Close the chain
`GB-03 → FX-08 / MCU-13 → gating unknowns → denominators → negative claims → balanced-but-wrong →
fixed point → MC-01…MC-10 → expert challenge → reusable method`, at `VERY DEEP / L99999.99999`,
Tolerance = 0.

**Happened:** the chain was executed in order and to its end. Then two fresh convergence passes and
six fresh expert perspectives — none of them an author — returned **fifteen material deltas and twelve
accepted new findings**, **invalidated six of this round's own claims**, and demonstrated that
**`GB-06` was live inside the package that declares `GB-06`'s remedy exercised.**

---

## 2. The headline

> ### One of the four blockers the programme has carried as "closed with evidence" through two gate reports describes a state that cannot be constructed on this build.

`FX-08`'s recorded mechanism is *"the writer stores a branch company; the resolver looks for
root-or-null; the two do not intersect."* Three independent layers each foreclose the writer half:

1. a **model constraint** rejects any rate row naming a company that has a parent;
2. the company model **refuses any write containing the parent field** — the hierarchy is immutable
   after creation;
3. **the company currency is root-delegated**, so a branch cannot hold a currency of its own and the
   scenario is not merely blocked but **semantically empty**.

And the parent round's stated reason for not acting — *"a constraint can be bypassed by raw SQL: 62
sites"* — does not survive. Across every module tree in the source root there is **no raw-SQL write to
the rate table at all**, independently reproduced by a fresh reviewer on a line-wrap-tolerant method
across four version trees.

**What it does not mean.** The **other** half of `GB-03` — the company-less rate row — is untouched,
is worse than `FX-08` ever was, and is **wider on the version SMEsPlus is targeting**. And the
challenge then found a route to it that no enumeration in the programme contains: **deleting a company
converts its rate rows into company-less rows at the database layer, by a foreign key, with no ORM
call and no revalidation.**

---

## 3. Convergence test result

| Test | Verdict | Movement |
|---|---|---|
| `MC-01` Population Boundedness | **NOT MET** | one population fully bounded; the bounding denominator found wrong |
| `MC-02` Systematic Enumeration | `PARTIALLY MET` | method improved, result unchanged |
| `MC-03` Independent Delta | **NOT MET** | 15 deltas, 12 new findings |
| `MC-04` Repeatability | `PARTIALLY MET` | 15 of 15 and 20 of 24 reproduce; 3 denominators contradicted |
| `MC-05` Negative Claim Compliance | **NOT MET** | control materially stronger; baseline still unscanned |
| `MC-06` Unknown Classification | **NOT MET** | **▼ down from `MET`** |
| `MC-07` Contradiction Closure | **NOT MET** | channel now exists, and failed in this round's own hands |
| `MC-08` Tolerance-Zero Closure | **NOT MET** | ▼ 7 → **12** boundaries |
| `MC-09` Evidence Lineage | `PARTIALLY MET` | **▲ up** |
| `MC-10` New-Finding Delta | **NOT MET** | not close |

> ### **8 not met · 2 partially met · 0 met.** Parent: 7 / 2 / 1.
> **No criterion was weakened. The one that moved down did so because this round tested the register
> the parent had marked `MET` and found its denominator was not an enumeration.**

**Fixed point: `NOT REACHED`.** Six of seven criteria fail on **both** consecutive independent passes.
Only the gate recommendation is stable — and a recommendation reached by five passes that keep finding
new material is evidence of the recommendation, not of convergence.

---

## 4. Tolerance-zero position

**Twelve boundaries. Zero resolved.** Five were added this round; two of the five came from the
challenge and one of those two is the first of its kind in the programme:

> **`T0-12` — the debit = credit assertion is itself suppressible by context, with three shipped
> production consumers. `unbalanced-and-posted` is reachable.**
>
> That is a worse state than balanced-but-wrong, and the taxonomy this round spent a phase proving has
> **no cell for it**. The suppression key sits inside a bucket of 48 generic tokens that was **counted
> and never assessed** — it is that bucket's most severe member, and it was never opened.

`T0-11` is its companion: **the entry-balance invariant is enforced in one currency dimension only.**
A foreign-currency move has two, and the second — the input to unrealised revaluation, residual
tracking and realised FX — is unconstrained.

---

## 5. Blocker position

| # | Blocker | Position |
|---|---|---|
| `GB-01` | Cross-company / cross-tenant measurement crossing | **UNCHANGED — Boss decision — and it should now carry an enumerated SEVEN-ROW consequence table** so the decision is made against a list rather than a general statement |
| `GB-02` | Cross-company rewrite of a posted fact | **WIDENED THREE TIMES** — cross-branch reconciliation with raw-SQL settlement; a lock-exception path where **one record against a root relaxes the whole tree, for everyone, forever, from a create right alone**; and a lock-date wizard whose declared company field is inert over an elevated write |
| `GB-03` | Inconsistent company scoping over one rate table | **`PARTIAL`** — branch axis research-complete with a residual; null axis an unclosed verified defect, **now with a database-level route to it** |
| `GB-04` | Cross-boundary exposure not characterised | **UNCHANGED IN SUBSTANCE, WORSE IN SCOPE.** 192 sites bounded, 9 assessed — over a path set now known to exclude 962 modules. The challenge adds **245 crossing sites in one addon, 40 assessed** |
| `GB-05` | Affirmative safety claims unaudited | **UNCHANGED** |
| `GB-06` | No correction-propagation channel | **DOES NOT IMPROVE.** The channel was specified, demonstrated — **and then failed on this round's own last correction**. Re-specified as a **mechanism** (`MCC_00`), not an authoring rule |
| `GB-07` | The Wave A source surface is under-bounded | **CONFIRMED, WIDENED ON A NEW AXIS, AND ONE ELEMENT CORRECTED.** The **module tree** itself was under-bounded by 962 manifested modules. But the localisation figure was overstated — the correct denominator is 456, not 906, and **the Thai localisation is entirely inside the searched tree** |
| **`GB-08`** | **NEW — the reference implementation is not stable across the versions SMEsPlus spans** | A branch-preference behaviour exists in a later v18 point release and in **neither** v19 tree; v19 **adds** a rate resolver in the ORM core that bypasses every record rule and executes on essentially every grouped read. **A v18 → v19 migration widens the control surface.** And the v18 divergence is a **pure behavioural change with no schema change**, so it arrives with **no migration artefact to review** |

---

## 6. Gate recommendation

> # `RECOMMEND HOLD`

**Recommendation only. Boss is the sole Final Approver.**

### Why not `CONDITIONAL PASS`

**Unavailable by rule, not by judgement.** The standard and the standing Boss instruction forbid using
it to bypass an unresolved tolerance-zero boundary. **Twelve stand unresolved.** The conditions would
*be* the tolerance-zero items.

### Why not `PASS`

`MC-03` and `MC-10` fail without qualification. Two fresh passes and six fresh perspectives returned
fifteen material deltas and twelve accepted findings, and invalidated six of this round's own claims.
The fixed point is not reached on six of seven criteria, twice consecutively.

### Why not `FAIL`

**No veto was issued**, by either convergence pass or by the independent audit panel, which considered
five veto grounds and rejected each with its reason on the record. The positive ground for excluding
`FAIL` is stated rather than inferred from that absence — which is the inference `DR-NC-01` prohibits:
**the semantic model has now survived six adversarial rounds on evidence**, every finding has sharpened
the direction already chosen, and the mechanical evidence base reproduced under a **fourth** independent
recount.

### What the hold is on

**Not the semantic model, and not the evidence.** The hold is on the method's ability to bound its own
search — and, newly, on the package's ability to carry its own corrections **by mechanism rather than
by intention**.

---

## 7. For Boss attention

1. **A blocker carried as a verified defect through two gates does not exist as described.** `FX-08`
   was right about the resolver and wrong about the writer. No round could see that until the surface
   was bounded, and bounding it took one hour of mechanical work.
2. **`unbalanced-and-posted` is reachable, and nothing in the programme's taxonomy has a cell for it.**
   This is the single most severe finding of the round and it came from a fresh perspective, on the
   first pass, out of a bucket of 48 tokens that three rounds had counted and none had opened.
3. **A Thai statutory VAT filing artefact can contain another legal entity's invoices**, under this
   entity's VAT number and branch number, because the report handler carries no company filter while
   its sibling in the same module does. **This is inside the only localisation SMEsPlus deploys.**
4. **`MCU-04` is closable now.** The report-definition model has no company dimension, no record rule
   anywhere, and full create/write/unlink for the accounting-manager role. It was carried as a
   deferred tenant question; it is a verified defect. **A real closure this round left on the table,
   recovered by the challenge.**
5. **Three of the four objects this round reduced into `GB-01` are research-closed.** Routing a closed
   defect into an open design decision is the same class of move as routing a blocker to a later Wave
   — which this round forbids and re-tests for, and then did.
6. **`GB-06` failed in the hands of the author who had just written its remedy**, while propagating
   their own correction. That is the round's strongest evidence for its own conclusion, and the remedy
   is now a one-file, one-command mechanism, not a rule.
7. **The method blockers remain cheap; the design blockers remain expensive.** `GB-04`, `GB-06` and
   `GB-07` are days of mechanical work. `GB-01`, `GB-02`, `GB-03` and now `GB-08` need decisions —
   including **which reference build SMEsPlus freezes**, because the reference implementation's
   treatment of this one table is not stable across the versions the programme spans, and a
   behavioural-only point release leaves no artefact for a migration gate to inspect.
8. **What this round is good for.** The rate-table surface is the **first population in the
   programme's history at a proven path set and 100% evidence coverage**; nine gating unknowns closed
   against a prior record of zero; the `41`-vs-`59` mismatch is resolved and was never an arithmetic
   dispute; and the complete denominator rule — **`POPULATION` + `PATTERN` + `PATH SET` + `UNIT`, none
   author-chosen** — is now stated and is transferable to every remaining module unchanged.

---

## 8. Terminal state

> ## `ACCOUNT WAVE A — METHOD NOT CONVERGED / HOLD WITH EXACT REMAINING ENUMERATION AND GATING DEFECT`
>
> **Exact remaining enumeration defects:**
>
> 1. **The module tree itself was under-bounded** — 962 manifested modules outside the searched tree.
>    Every whole-tree negative in the programme's history is scoped to one tree of three. `GB-07`.
> 2. **The unit of count was never defined.** Two disciplined enumerations of one bounded surface
>    returned 12 and 14. A denominator is `POPULATION` + `PATTERN` + `PATH SET` + `UNIT`.
> 3. **Five populations remain enumerated nowhere:** the company-consistency enforcement surface;
>    referential actions (≈211 relations with no declared delete behaviour, one of which manufactures
>    the defect `GB-03`'s open axis is about); the Wave A state-control surface (floor 165 shipped
>    objects, 4 assessed, and one sub-population unbounded by construction); the 48 generic
>    suppression tokens (**one of which defeats the balance assertion**); and database-level DDL.
> 4. **Six of this round's own claims were invalidated by fresh passes; the author caught one.**
> 5. **`GB-06` failed inside the round that specified its remedy.**
>
> **Exact gating defect:** **twelve tolerance-zero boundaries stand unresolved**, two of them opened by
> the challenge, and one of those two — `T0-12` — establishes that an entry can be **posted without any
> debit = credit assertion at all**.
>
> **Eight blockers: `GB-01` … `GB-08`.** Four need a Boss design decision; three are closable by
> mechanical work; one — `GB-08` — needs a **build-freeze decision** before any Wave A conclusion can
> be relied on downstream.
>
> **Standing gating unknowns: 17**, membership almost entirely different from the 17 this round
> inherited.

**Not declared:** converged · final approved · final freeze · Wave A closed · any gate movement · any
implementation authorisation · Team B or Team C hand-off.
**Wave B has not started. No SMEsPlus or reference source code was modified. Nothing was merged or
deployed.**

---

> ### FIGURE-GOVERNANCE NOTICE
> `MCC_00_CANONICAL_FIGURES_REGISTER.md` governs every published figure and disposition in this
> package. Where a figure here differs from a row in `MCC_00`, **`MCC_00` governs**.
>
> ### PACKAGE-STATE NOTICE
> The independent audit panel recorded that this package **changed while it was under review**. The
> evidence manifest therefore carries a per-file SHA-256 and a roll-up digest, and any reviewer verdict
> should name the digest it reviewed. `MCC_J` `J-17`, `MCC_K` `ER-CORE-8`.
