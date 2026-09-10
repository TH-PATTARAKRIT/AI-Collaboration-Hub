# LESA_PREP003_RESOLUTION_REPORT.md
# Source-resolution loop — what the challenge round sent back to the evidence, and what came back

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
LESA responsibility per §13: resolve every challenge finding that turns on a question about the source
or the evidence base, by going back to the primary artefact — never to a summary of it.

---

## 1. What was sent back

Of 36 adopted findings, **eleven could only be settled at the source.** Each was re-opened against the
primary artefact, not against any register, report or prior conclusion.

| # | Question sent back | Primary artefact consulted | Answer |
|---|--------------------|---------------------------|--------|
| 1 | Do the 52 excluded buttons really invoke a method outside the domain? | the button declarations themselves, read at the cited file and line | **No — 48 of 52 do not invoke any method at all.** 41 carry no name attribute; 7 name a label that `special="cancel"` overrides and for which no definition exists anywhere in the reference tree |
| 2 | Are edition-restricted modules genuinely absent? | the 126 resolvable domain module manifests | **No — 71 are restricted (70 enterprise-licence, 1 proprietary), holding 1,411 population items (27.8%)** |
| 3 | Does the mutation predicate fire on deletion guards? | 15 guard bodies read in full | **Yes.** Each raises and writes nothing; each is counted as a mutation because its own identifier contains the token |
| 4 | Does the exception predicate fire on prose? | the one disagreeing body | **Yes** — a docstring containing the word *"except"*, no handler present |
| 5 | Is the entry-guard facet at entry? | offsets measured from the definition line | **Not for 45 of 102**; the worst sits 17 lines into a 60-line body |
| 6 | Is 98.9% unhandled a property of this domain? | a control over 120 randomly selected modules | **No — 97.2% platform-wide.** The figure carries no discriminating information about this domain |
| 7 | Does the cross-domain predicate distinguish another domain? | the pattern, tested against a same-domain and a cross-domain control | **No.** Both return the same answer |
| 8 | Is `EDGE = 2` derived? | the assigning code | **No** — a two-element identity list written by hand, both rows with empty evidence |
| 9 | Do the 17 process-verified items carry the twenty facets? | their own register rows | **No — none carries a facet record;** 10 sit at the lowest status |
| 10 | Are the 10 optional-module menus installed anywhere? | the deployments' installed-module records | **No.** They are graded observed by a prefix match, and the same package's census says they are not installed |
| 11 | Is the declared evidence base the whole of it? | a sweep of `$HOME` and every mounted volume, by format not extension | **No.** At least 12 further database identities exist, two of them full ERP databases holding the tables this package measures |

**Eleven questions, eleven answers against my published position.** Not one came back confirming it.

## 2. `LESA-F-01` — the pattern behind the pattern

Ten of the eleven have the same shape, and it is the shape this programme has catalogued more than any
other:

> **A predicate was written in the vocabulary of the thing being looked for, rather than the vocabulary
> of the corpus being searched — and then a control was drawn from the same wrong vocabulary, so it
> could not fire, and its silence was read as confirmation.**

- The button resolver looked for a Python method name and was handed an XML attribute.
- The edition-restriction classifier had **no branch** capable of emitting the class it declared absent.
- The mutation pattern's alternative matched the searched text's own identifiers.
- The cross-domain pattern's control was a cross-domain call, which the predicate reports identically to
  an in-domain call.

`CORR-F-37` was raised in the previous round for exactly this, restated in this package's own
configuration report as a standing rule, **and recurred four times inside the package that restates it.**
Writing the rule down did not make it operative. Only a differently-biased party running the instrument
did.

## 3. `LESA-F-02` — the evidence base is a claim, and it was not evidenced

The runtime report's §2 is headed *"Evidence base — declared, and the whole of it"* and asserts
*"the path set was swept and the population ranked before selection."* **Neither the sweep nor the path
set is published anywhere in the package** — the intention is stated, the command and its output are
not. The programme's own denominator contract requires the path set to be **declared and executed**.

An independent sweep found at least twelve further database identities on this host, two of them full
ERP databases carrying `stock_move`, `stock_quant`, the installed-module table and the menu table — and
both carrying the valuation table that `CRITICAL-GAP-01` turns on. One is owned by a role named for this
programme. A controlled-install lab sits on the same host with an evidence directory named for the
precise configuration that gap's closure statement says was never run; that lab is the prior generation
and does **not** discharge the current-generation requirement, but the closure statement asserts a
negative about an experiment while a lab built to run it goes unnamed.

**The heading is retracted.** What can be said is narrower and is now said: *five deployment identities
were located and examined; the path set that located them is not published, and the population of
database artefacts on this host is larger than five.*

## 4. `LESA-F-03` — what the source resolution did **not** overturn

Reported so that the eleven reversals are not mistaken for a total collapse of the evidence:

- **Generation basis holds.** Every row's generation is established by a **content** discriminator — a declarative construct present in the current series and absent before it — not by a directory name and not by a manifest version string. This is the control whose absence cost four rounds in another workstream.
- **AST resolution holds.** All 614 behaviour pointers resolve exactly to the named function; no fallback path ever executed; no name mismatch.
- **Parse coverage holds.** 169 of 169 files read and parsed; zero failures. The coverage assertion is real.
- **The configuration census holds** in every figure — 48 gates, 709 gated elements, the class split and all ten leading gates reproduce exactly under an independent re-derivation.
- **The fifteen Critical Areas are verbatim** from the frozen canonical rule.
- **The deployment extraction method holds.** Five identities across three generations, read without starting a database server, with the client-version failure treated as a blocker rather than as an absence.

## 5. Resolution status

| | |
|---|---|
| Findings requiring source resolution | 11 |
| Resolved at the primary artefact | **11** |
| Resolved in favour of the published position | **0** |
| Resolved against it | **11** |
| Left unresolvable from inside the frozen package | **1** — the 3,680-vs-14,441 movement denominator (`CH-17`); the dumps are outside the package and no query reachable from it settles which figure is the completed count |

**The one unresolved item is recorded as unresolved, not rounded to either side.** It sits underneath a
retraction and a re-stated Critical Gap, which is the worst place for an unreconciled denominator, and
it is carried to PMO as a blocking item rather than absorbed.
