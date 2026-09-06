# P10 — G02 AAS-03 CHALLENGE RECORD

Round `SMEPLUS-26-09-06-G02-P10-TBR-BOUNDED-DEEP-CLOSURE-DESIGN-INPUT-001`.
Four independent adversarial challenges, launched against the frozen-as-of-10:36 package.

> **Standing rule applied: INDEPENDENT REVIEW IS NOT TRUTH.** Every material claim below was
> re-verified by P10 against primary source or the peer's own artefact before acceptance.
> Two challenger claims are **narrowed** and one is **inverted** on re-verification.

---

## 1. Challenge Set and Coverage

| # | Lens | Findings raised | Accepted | Narrowed | Rejected |
|---|---|---|---|---|---|
| 1 | Leader Functional Design | 14 (`A3C1-`) | 11 | 2 | 1 |
| 2 | Leadership Database Design | 19 (`C2-`) | 16 | 3 | 0 |
| 3 | Lead Integration & Localization | 19 (`X3-F-`) | 17 | 2 | 0 |
| 4 | Lead Code & UI Architect | 19 (`C4-F-`) | 16 | 3 | 0 |
| | **Total** | **71** | **60** | **10** | **1** |

**P10 self-caught this round: 1** (the baseline-SHA discrepancy `G02-E-01`).
**Externally caught: 60.** The ratio is unchanged from every prior round and is the reason
the challenge step is not optional.

**All four challengers independently reported that the package was still being written while
they read it** (13 files at 10:29 → 20 at 10:36). That is a method defect owned by P10, not by
them, and it is recorded as `G02-R-16`. A package must be frozen before adversarial review opens;
each reviewer's coverage statement is therefore bounded to the 10:36 state.

---

## 2. The Denominator Correction — Executed, Not Merely Recorded

`X3-F-05` item 1 reported that **P02 issued P10 a correction, naming P10**, at `22` line 321 and
`23` line 135 (`CORRECTION ISSUED`):

> "**P02 CORRECTS THE DENOMINATOR: there are 6 distinct archives and all 6 are readable** with
> a newer database toolchain, which is installed. **P10's** and P01's evidence bases were bounded by the
> default binary. Routed back as a correction."

**P10 verified this against P02's own package at the pinned SHA and it is exact.** P10 had recorded
four archives, three readable. The correction was never consumed.

**P10 then executed it.** This is a Material Delta — **deeper on P10's own declared evidence
population, on a correction addressed to P10 by name**. It admits no new root, no new sweep and no
new process surface.

| MD | `MD-P10-G02-01` |
|---|---|
| **CQ affected** | `CQ-P10-04`, `CQ-P10-08`, `CQ-P10-12` |
| **Bounded surface** | The three deployed archives P10 had never opened, all inside the already-declared host path set |
| **Insufficiency** | P10's denominator was 4; the peer-verified distinct denominator is 6, and P10's own "at least ten" was an artefact count, not a database count |
| **Stop condition** | Deferral-entry count, deferral-window count and the five lock columns read from each; no other table |
| **Ran?** | **YES** |

### 2.1 Result — the complete corrected population

| # | Archive | Companies | **Deferral entries** | Lock dates set | Previously examined |
|---|---|---|---|---|---|
| A | Archive A | 44 | **0** | 0 | yes |
| B | Archive B | 44 | **0** | 0 | yes |
| C | Archive C | 1 | **0** | 0 | yes |
| D | Archive D | 1 | **0** | 4 | yes |
| **E** | **Archive E** | 1 | **0** | **4** | **NO — outside the declared path set** |
| **F** | **Archive F** | 1 | **0** | 0 | **NO — plain SQL inside a web-backup zip** |
| **G** | **Archive G** | 44 | **0** | 0 | **NO — recorded as permission-refused** |

**Positive control on every zero:** the deferral-entry-to-source link structure exists as a table in all seven
artefacts, with a a data-block header and zero data rows — an **empty** table, not an absent one. The
byte-size control that could not make this distinction is not used here.

### 2.2 What the correction does to P10's findings

- **`P10-F-G02-01` SURVIVES AND STRENGTHENS.** The deferral mechanism has generated **zero entries
  in 6 of 6 distinct deployed databases**, not 4 of 4. The finding did not depend on the missing two;
  correcting the denominator widened the support without changing the direction.
- **The lock population changes.** P10 published "the one deployed database that carries locks".
  **Two** do — archives D and E, both snapshots of one deployment line, four locks each at `2026-02-28`. Whether
  they are the same company at two dates is **not** established: `UNRESOLVED`.
- **Three P10 negatives about its own capability are withdrawn.** `G02-R-03` below.

---

## 3. Corrections Accepted and Applied — `G02-R-` Series

### `G02-R-03` — P10 published three false negatives about its own evidence base. `CONTRADICTED`.

| Was | Now |
|---|---|
| "The four deployed databases already examined" is the population | **Six distinct databases; all six examined.** The peer-verified unit is the database UUID |
| "At least ten deployed databases exist; six were never examined" | **Wrong unit.** Ten counted *artefacts*, including duplicate snapshots of the same database. The distinct count is six. P10 over-counted the population and under-counted its own coverage in the same sentence |
| "A snapshot dated later than every image P10 read exists on the host and **could not be read** — permission-refused" | **CONTRADICTED by execution.** It opens with an ordinary archive extractor. It holds 44 companies, 563 journal items, **zero deferral entries and zero lock dates** |

This is the **fourth** occurrence in this programme of an evidence-base negative that was never
re-tested, and the **third** of the exact archive-format/path-set pair. The rule was already written
down. It did not fire because P10 re-read its own prior conclusion instead of re-running the probe.

### `G02-R-04` — the version basis. Partially closed by execution.

`C4-F-01`…`C4-F-04` reported, correctly, that **every P10 source claim is bounded by PATH and never
by VERSION**: the read generation is 18.0+e, the examined estate runs **19.0+e**. `C4` declared the
differencing pass (`MD-C4-04`) and declined it for want of a 19 source tree.

**A 19 source tree was not required.** Archive F is a *plain-SQL* dump of the deployed generation and
carries its full DDL. P10 executed the differencing pass on the schema:

| Element | 18.0+e source (as P10 read it) | **Deployed 19.0+e (measured)** |
|---|---|---|
| Deferral window on the journal item | the two window-date fields | **both present** |
| Deferral entry ↔ source link | the deferral-entry-to-source link structure | **present** |
| **A recognition-period column on the deferral entry** | **none** | **none** — 71 columns, no period carrier |
| Asset period carrier | the period-beginning date | **present** on the journal entry |
| Company lock columns | five | **five** — general, tax, sales-document, purchase-document and irrevocable |
| Tax-period carrier | — | **a tax-period carrier on the journal entry, absent on the journal item** |
| Asset pause | — | **a paused-days counter present** |

> **The central P10 finding is now verified on the generation the estate actually runs.** The
> deferral entry carries no recognition period in 19.0+e, while the asset entry carries one. The
> collapse of recognition period into posting act, and its asymmetry against depreciation, are
> **not artefacts of reading an older generation.**

`CQ-P10-12` remains `UNRESOLVED` for *behaviour* — a schema is not a code path, and no 19 source was
read. The correct standing caveat, now carried in every G02 deliverable, is: **source claims are
verified against 18.0+e; the field sets they turn on are verified present and unchanged in the
deployed 19.0+e schema; behavioural equivalence is untested.**

### `G02-R-01` — P10 consumed a P02 finding its author had withdrawn. `CONFIRMED`.

`X3-F-02`. Verified by P10 against P02 `34` at the pinned SHA — the correction banner `C-34`/`RE-29`
reads exactly as quoted. On the accounting (posted-only) basis, delivered-not-invoiced is **1,145**
against **792** billed-ahead — **1.4:1 toward delivery**. P02 states: *"the sentence 'the dominant
cut-off exposure is billing ahead of performance' is **WITHDRAWN** for Archive C."*

P10 published the withdrawn wording, with draft-basis figures, in **five** places. All five corrected.

**`P10-F-G02-01` does not depend on it** — it rests on P10's own measurement of zero deferral entries
— but its **framing** does, and the framing is what a Boss decision would be weighted by.

### `G02-R-02` — three written handoff conditions, none carried. `CONFIRMED`.

`X3-F-03`. P02 `48` §6 attaches conditions in writing to P10's handoff. Verified verbatim. All three
now carried in `P10_EVIDENCE_POPULATION_BOUNDARY.md` §7 and at the point of every P02-sourced figure.
P02 also forbade acting on the 792/2,564 before segmentation by product invoicing policy (`P02-F-34e`,
"accepted, not yet executed"); P10 acted on them unsegmented. Struck.

### `G02-R-05` — teardown is destructive, not orphaning. Severity ESCALATED.

`C2` §RISKY. P10's destructive-behaviour table said a schedule teardown "orphans posted entries with
their back-reference nulled — **the entries survive**." Verified at source: both back-references are
declared `ondelete='cascade'`. Under a cascade the posted, hashed, audit-trailed entries are
**deleted**, not orphaned. The nulling behaviour P10 described exists — but on a *different* path.

P10 confirms the ORM declaration and **does not** confirm the emitted SQL constraint. `UNRESOLVED —
EVIDENCE REQUIRED`; the discriminating read is two rows of the database's own constraint catalogue
and needs a restore. **P10 wrote a downgrade where the evidence supports an escalation.**

### `G02-R-06` — "no in-flight amendment path" is contradicted. `CONFIRMED, then NARROWED`.

`A3C1-01`, narrowed by `C4-F-18`. P10 verified all four legs at source: the window fields carry **no
`tracking`**, are **absent from the integrity-hash field set**, are **absent from the lock-protected
field sets**, and the module's only write guard raises for the account field alone.

**P10's own re-verification changes the reachability claim in both directions:**

- Challenger 1 read the guard as absent from the invoice form and present on the list view. **It is
  the reverse.** The Journal Items list carries `readonly="has_deferred_moves"`; the invoice form's
  line list carries **no readonly**, only a colour warning.
- Challenger 4 is right that the form's parent field is `readonly="state != 'draft'"`, so the UI hole
  is **not** open on a posted document — it opens in the **draft window created by resetting to
  draft**, where `has_deferred_moves` remains true because the entries were reversed rather than removed.

> **Corrected statement.** There is no in-flight amendment path that *re-derives*. There is one that
> *diverges*: at model level the window is editable by any import, API call or server action with no
> trace and no regeneration; through the UI it is reachable in the reset-to-draft window. The ledger
> keeps the original slices; the two deferral reports recompute the spread from the two date fields
> on every render. **A fourth correction outcome — `SILENTLY DIVERGENT` — is added to the algebra.**

### `G02-R-07` — the anchor is silently wiped. `CONFIRMED`, and P10 did not have it.

`C2` §2. Verified at source: the delete routine executes
`deferral_moves.deferred_original_move_ids.deferred_move_ids = False` — which clears the **entire**
relation on every original move, not only the link to the move being deleted. The grouped path's
duplicate filter reads exactly that relation. **Deleting one deferral entry re-arms duplicate
generation for every invoice grouped with it.** Added to the identity trace and the algebra.

### `G02-R-08` — a ticked deliverable that did not exist. `CONFIRMED`.

`A3C1-13`, `X3-F-01`, `C4` §7. `CQ-P10-13` was marked **✔** against
`P10_G02_TERMINALITY_RECORD.md`, and the file was absent. This is precisely the shape the programme
already named — a disposition column asserting a completion the artefact does not support — and it
occurred on **the one question that certifies the other twelve**. The record is now written; the
tick was false when made and is recorded as such rather than quietly satisfied.

### `G02-R-09` — no P07 handoff, over an unmoved localisation negative. `CONFIRMED`.

`X3-F-12`, `X3-F-13`. P06, P08 and P11 each received a handoff; P07 received a table cell.
`NC-17` ("localisation modules do not alter time-based recognition") stands at **`C — NOT SEARCHED`**
with P10's own register recording *"must not be written"* — over a deployed estate carrying **nine
Thai localisation modules**. None of this appears in the closure package. `P10_TO_P07_HANDOFF.md`
is now published. The nine-versus-ten discrepancy inside P10's own lineage (`X3-F-13a`) is recorded
as `G02-R-17`, `UNRESOLVED`.

### `G02-R-10` — P10 published a ledger fact that the ledger owner refutes. `CONFIRMED`.

`X3-F-08`/`-09`. P10's lock matrix §2 asserts that the fiscal-year and irreversible locks "**bind**"
recognition entries. **P10's own §1 table one section earlier records `RELOCATE`**, and P08's
`PC-29a` is `FACT VERIFIED` that the irrevocable lock refuses a *reopen* and not a *posting*.
"Bind" is struck. P10 also imported a *fiscal-year* semantic the owner's enumeration does not carry,
and omitted both the **lock exception** route and the **entry seal**. Corrected, and the corrected
form is what the P08 handoff now carries.

### `G02-R-11` — the tax-lock exclusion rests on an untested premise. `OPEN`.

`X3-F-10`. P10 excluded the tax lock because "recognition entries carry no tax". P08 has
`FACT VERIFIED` a tax-period carrier populated on **61,157 posted entries**, differing from the
accounting date on 5,228. **P10's own differencing pass (§3 `G02-R-04`) confirms a tax-period carrier
exists on the journal entry and is absent from the journal item in the deployed 19.0+e schema** —
which corroborates P08 and leaves P10's premise untested. Routed to P08 as an exact question.

### `G02-R-12` — normative rows dispositioned as verified fact. `CONFIRMED`.

`C2` §8. All 13 rows of the scope matrix were headed `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.
Only the **Reference** column is a fact; the **SMEsPlus** column is a determination. Rows assigning
TENANT to an object the reference scopes COMPANY are re-classed **`DESIGN CANDIDATE`**. This is the
same category error the programme condemns in peers, committed against P10's own determinations.

Two consequences P10 had not drawn, both accepted: a tenant-scoped window referenced by
company-scoped facts is coherent **only** if the window is immutable-once-referenced or versioned;
and if the recognition *pattern* is COMPANY-scoped while the obligation is TENANT-scoped, two
companies of one tenant can recognise one obligation on two patterns. Added as `UNRESOLVED`.

### `G02-R-13` — the convention count, and a clean-room hazard. `CONFIRMED`.

`C2` §3, `C4-F-09`. "Three engines" counts **modules**, not conventions: there are **four in-house
conventions across three modules** (two of them selected by one setting inside the asset module),
plus a library of **eight named standards**. The deferral convention is `30E/360 ISDA` with its
February clause removed — P10 said "a named 30/360 standard" and never named it.

**The clean-room point is material and P10 missed it.** The library is a **verbatim MIT-licensed
third-party file vendored into a module licensed a proprietary licence**. P10's sentence "a complete standards-named
library already exists inside the declared root" invites a clean-room team to lift code out of a
proprietary module. **The correct route is the upstream MIT package; the reference is not the source.**
Two further cautions accepted: the February handling is gated on a loan-payment flag and is **not**
in the default convention, so adopting the function naively reintroduces the defect; and the selected
convention is **never persisted** — the wizard is transient and discards it.

### `G02-R-14` — a capability written in exposure language. `CONFIRMED`.

`C4-F-11`. `P10-F-21` ("one screen shows one number and posts another") is carried as **Material**.
P10's own four-state matrix forbids this: the button that triggers the path is rendered **only** when
the company method is `manual`, and all 44 companies are `on_validation`; and the substitution changes
a figure only where the two computation methods differ, which they do nowhere. State on P10's own
scale: **capability present · configuration not reachable · not exposed · not observed**. Re-classed.
It is one of the round's most quotable lines and it is not exposure evidence.

### `G02-R-15` — orphan peer identifiers. `CONFIRMED`.

`X3-F-06`. `T0-13`, `P11-B-16`, `UAE-05` and the peer design veto appear **nowhere by identifier** in
the closure package; every reference is descriptive. The substance was faithful — verified verbatim
against P11's register in three places — but a peer cannot resolve a description to a register row.
All named.

---

## 4. Claims Narrowed or Rejected on P10 Re-verification

| Claim | Challenger | P10 disposition |
|---|---|---|
| The window-edit hole is open on a posted invoice; the form view is unguarded and the list view guarded | `A3C1-01` | **Guard mapping INVERTED** — the list view carries the readonly, the form does not. And the form's parent field is state-gated, so the UI hole opens in the reset-to-draft window, not on a posted document. **Model level is unguarded unconditionally.** Accepted as narrowed |
| "One domain with a direction switch" is a functional claim contradicted by P10's own §3 | `A3C1-10` | **Accepted.** Restated as **one engine, two domains** |
| The three-primitive algebra is incomplete | `A3C1-09` | **Accepted.** Fourth outcome `SILENTLY DIVERGENT` added |
| Partial recognition is missing and actively foreclosed | `A3C1-08` | **Accepted as the largest single omission.** Raised as `CQ-P10-14`-candidate; P10 does not add closure questions, so it is routed to the Boss as an unasked question rather than answered |
| "P10 recognises revenue on billing **by omission**" prejudges a Boss-reserved decision | `A3C1-12`, `X3-F-11` | **Accepted.** Re-worded to *"recognition follows billing in practice; the configured deferral policy is present, unexercised and unenforced"* — same evidence, no imputed intent |
| The grouped path "recomputes the whole position each run" | `C2` §5 | **Narrowed.** True of the amount, false of the population: work is line-wise, exclusion is move-wise |
| "The setting changes the weights, never the dates" | `C4-F-06` | **Narrowed** — zero-suppression removes entries, changing the surviving set |
| The accrual is "the pattern to copy" | `X3-F-16`…`-19` | **Narrowed to the requirement.** `X-02` restated as the rule; the accrual cited only as the sole observed scope refusal, on an operator path, with none of its other controls carried across |
| `AL-4`'s "reason" clause is a preference, not an absence | `C2` §4 | **Accepted.** Re-classed `DESIGN CANDIDATE`; actor and prior-version stay `FACT-SUPPORTED` |
| P10 must state whether SMEsPlus reproduces a prior statement or only reconciles a correction | `C2` §7 | **Accepted, and it is not P10's to answer.** Routed |
| The design pack's ten functions are the wrong ten | `A3C1` §9.4 | **REJECTED as stated.** The ten are what the round was directed to produce. The *substance* — that partial recognition and the unbilled position have no home among them — is accepted and recorded above |

---

## 5. What the Challenges Did Not Reach

Stated so the coverage claim is honest:

- **No challenger tested P10's arithmetic independently except by re-deriving the two figures P10
  had already published.** Both reproduced to the digit. Nothing else was recomputed.
- **No challenger read the deployed generation's source.** Neither did P10. The differencing pass in
  `G02-R-04` is a *schema* result and is bounded as one.
- **Three challengers inherited P10's four-database denominator.** Only the integration lens found
  the peer correction, and it found it in P02's register rather than by probing. **The evidence base
  is still the surface the controls are weakest on** — four rounds after that was first written down.
