# B13 — Design Option & Trade-off Register

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B13 — Design Options & Trade-off Register |
| Status | **Team B recommendation only. None of the recommendations below are approved design until Boss Final Gate.** |
| **Corrected** | **CORR-B01 / CORR-B03 (2026-08-29)** — DT-02 revised: ChatGPT's independent audit found the original recommendation internally contradictory, not merely one reasonable option among others (see DT-02 below for the full account, kept visible). DT-07 added for the historical-void design choice CORR-B03 required. |
| **Corrected (Round 2)** | **CORR-B2-01/02/03/04 (2026-08-29)** — DT-08 (Continuous vs. Segmented Ledger) and DT-09 (backdating rules) added, required by ChatGPT's Round 2 findings `M-AUD-04`/`M-AUD-05`. See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-05 (2026-08-29)** — DT-10 added (posted Fiscal-Year-Close Entry vs. no-posted-close derived-formula model for MP-11), required by ChatGPT's Round 3 finding `M-AUD-07`. DT-08's Option A description carried a now-superseded implementation detail (the posted MP-11 Entry) — annotated below, not silently edited; the Continuous-vs-Segmented decision itself is unaffected. See [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |
| **Corrected (Round 4)** | **CORR-B4-03 (2026-08-30)** — DT-11 added (boundary-driven vs. explicit-unclosed-component vs. mandatory-atomic-close models for Fiscal-Year reporting inclusion), required by ChatGPT's Round 4 finding `M-AUD-09`. See [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-05 (2026-08-30)** — DT-12 added (boundary immutability vs. versioned Fiscal Calendar models for historical safety), required by ChatGPT's Round 5 finding `M-AUD-12`. See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |
| **Corrected (Round 6)** | **CORR-B6-02 (2026-08-30)** — DT-13 added (prospective-only vs. atomic-retroactive-restatement models for post-reliance Fiscal-Year-membership change), required by ChatGPT's Round 6 finding `M-AUD-14`. See [CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md). |

Originally six, then seven, then nine, now **ten**, decisions were significant enough — either because
B04–B12 flagged them as assumptions requiring gate review, or because a real, defensible
alternative existed and picking one without showing the other was considered would understate
the actual design effort — to warrant a formal option comparison rather than a single stated
choice.

---

## DT-01 — Rounding Method

**Context:** MP-04 proposed round-half-up as a default; Team A's evidence left this
genuinely open (OQ-03/MR-06).

- **Option A — Round-half-up (arithmetic rounding).** Benefit: familiar, manually
  verifiable, the common default expectation on printed financial documents. Risk: has a
  slight statistical bias (rounds 0.5 up regardless of parity), immaterial at typical
  transaction volumes but not zero.
- **Option B — Round-half-to-even (banker's rounding).** Benefit: statistically unbiased
  over large volumes. Risk: less intuitive to a human manually checking a document by hand;
  more likely to prompt "why doesn't this match my calculator" support questions from
  SME-scale users, who are this project's stated target.
- **Option C — Currency/jurisdiction-configurable method.** Benefit: correct if different
  currencies or jurisdictions genuinely require different methods. Risk: configurability
  itself is a source of the exact silent-disagreement risk BINV-06/CO-08's tiering logic
  exists to prevent elsewhere — a wrongly-configured method is a subtler, harder-to-detect
  defect than a single fixed method would ever be.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Equal to B | Higher (human-checkable) | Lowest | Matches most source systems' likely convention | Neutral | Neutral | Highest | Neutral |
| B | Equal to A | Lower (needs explanation) | Low | May not match source | Neutral | Neutral | High | Neutral |
| C | Equal, if configured correctly | Lowest (which method applied is now itself a fact to audit) | Highest | Most flexible | Neutral | Marginal edge (per-tenant policy) | Lowest | Neutral |

**Recommendation:** **Option A**, as already proposed in MP-04 — SME-scale auditability and
manual verifiability outweigh Option B's statistical edge at this project's target volumes,
and Option C's configurability risk is disproportionate to its benefit absent an actual
evidenced jurisdictional requirement for a different method. **Not approved — requires
Boss confirmation, particularly given OQ-03 remains open.**

---

## DT-02 — Period Close vs. Consumption *(REVISED at CORR-B01 — original recommendation withdrawn as internally contradictory, not merely reconsidered)*

**Original context (kept visible, not deleted):** B04 §4 originally chose to treat period
close as an automatic, blanket consumption trigger for every Entry within it, and this
document's original DT-02 compared that against "consumption tracked only via explicit
triggers, period close unrelated" and recommended keeping the automatic-trigger design.
**ChatGPT's independent audit (`D01-B-AUD-01`) found that recommendation internally
contradictory**: B04 also described period reopen as restoring correctability, which cannot
be true if period-close-triggered consumption is, per BINV-07, permanent and never retracted.
This was not a legitimate trade-off between two coherent options — Option A as originally
written was not actually a coherent option at all once BINV-07 is taken seriously. The
comparison below replaces the original one.

- **Option A (original, now rejected as incoherent) — Period close is automatic, permanent
  consumption.** Cannot coexist with a reopen mechanism that restores correctability, given
  BINV-07. Rejecting this is not a preference — it is a requirement, once BINV-06/07 are held
  fixed (and they must be: they protect the domain's central invariant, INV-06/CF-06).
- **Option B (original) — Consumption tracked only via explicit triggers; period close
  unrelated.** Still valid as stated, but incomplete on its own: it never explained what (if
  anything) governs Amendment *timing* while a period is closed, leaving that question
  implicitly unanswered.
- **Option C (new, adopted) — Period Lock and Consumption as two independent, orthogonal
  gates on Amendment.** Period open/closed status (CAP-04/BINV-02) gates *whether Amendment
  is currently permitted*, reversibly, via authorized reopen (CO-08). Consumption
  (statutory filing / reconciliation / downstream reference — three triggers, not four)
  gates *whether Amendment is ever permitted again*, irreversibly (BINV-06/07, unchanged).
  Amendment requires both conditions to hold; either alone is not enough. This is Option B's
  correct trigger list, combined with an explicit, separate answer to the timing question
  Option B left implicit.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A (rejected) | Internally contradictory — not evaluable as a coherent design | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| B (superseded by C) | Correct trigger list, but silent on lock timing | High if complete; silently lower if a trigger is missed | Higher — needs a maintained, complete trigger taxonomy | Requires migration to also classify historical consumption event-by-event | Neutral | Neutral | Lower — trigger list must be revisited as new domains are added | Same target, weaker guarantee |
| C (adopted) | Correct: two independent, individually-sound conditions, matching Team A's own original insight ("safe to correct before external consumption") precisely | High — two separately verifiable rules, neither doing the other's job | Low-Medium — reuses existing Period (BINV-02) and Consumption (BINV-06/07) machinery, no new entity | Directly usable for MG-C04/C07 (migrated history: independently both consumed AND — since its period is imported already-closed — locked) | Neutral | Neutral | High — no special-case reconciliation between two mechanisms that used to silently conflict | Directly implements ADV-04/07, now without the contradiction |

**Recommendation:** **Option C**, adopted and applied to B04/B05/B08 in this corrective
round. This is not offered as one reasonable choice among equals the way DT-01's rounding
method is — Option A was not coherent, and Option C is the minimal, most precisely-scoped fix
available (reuses existing concepts, adds no new entity, and is a strict refinement of Option
B). **Still not independently approved by Boss** — flagged for Final Gate exactly as
before, but now as a corrected, internally consistent design rather than a contradictory one.

---

## DT-03 — Chart of Accounts Structure

**Context:** B07 §2 explicitly left chart-template mechanics open (GAP-D01-05), carrying it
here as instructed.

- **Option A — Fully independent chart per Company.** Benefit: maximal per-entity
  flexibility; no risk of one company's chart change affecting another. Risk: no reuse across
  companies in the same tenant; duplicated setup effort for multi-company SME tenants, which
  are an explicit target per this project's SaaS/SME identity.
- **Option B — Shared template with per-company override.** Benefit: faster onboarding for
  multi-company tenants (a common SME pattern — one owner, several related entities); still
  respects BINV-03/CAP-05's boundary since each company's actual chart remains its own
  instance, only *seeded* from a shared template. Risk: template-vs-instance drift must be
  clearly modeled so BINV-09 (category immutability after first use) still applies per
  Company, not per template — this needs to be designed carefully, not assumed automatic.
- **Option C — One global chart shared live across companies (no per-company instantiation).**
  Rejected outright, not merely disfavored: this would violate CAP-05/BINV-03's company
  boundary directly (an Account must belong to exactly one Company, B07 §3) — included here
  only to show it was considered and excluded on invariant grounds, not overlooked.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Equal to B | Equal to B | Lowest | Simplest — one chart per migrated company | Neutral (no reuse) | Neutral | High | Neutral |
| B | Equal to A, if instance/template distinction is respected | Equal to A | Higher — must model template vs. instance | Slightly more complex — must decide template vs. independent per migrated company | Positive — matches common SME multi-entity pattern | Positive — a template is itself a natural SaaS-tenant-level concept | Medium | Supports faster onboarding, a plausible future advancement angle beyond Team A's ADV list |
| C | Violates BINV-03 | N/A | N/A | N/A | Violates invariant | N/A | N/A | Rejected |

**Recommendation:** **Option B**, conditional on the template/instance distinction being
worked out at a later, more detailed design pass — this recommendation is directional, not a
complete design, and is offered because it best fits this project's stated SME/SaaS
multi-company identity. **Not approved — this was an explicitly open item (GAP-D01-05) and
requires its own follow-up design attention regardless of Boss's gate decision on the
direction.**

---

## DT-04 — Audit Trail Tamper-Evidence Scope

**Context:** CO-07 (B09) chose to extend tamper-evidence to the whole Audit Evidence stream
by independent design choice, beyond the narrowly evidenced legal requirement (RG-03/RG-04).

- **Option A — Broad: tamper-evidence across the entire Audit Evidence trail (chosen in
  CO-07).** Benefit: uniform, simpler mental model ("the trail is always tamper-evident");
  removes any temptation to under-invest in coverage for a document class that turns out
  later to be regulated. Risk: cost/complexity applied everywhere, including classes with no
  evidenced requirement for it.
- **Option B — Narrow: tamper-evidence only for the specifically evidenced classes
  (RG-03/RG-04), matching the reference system's own scoping philosophy (if not its
  opt-in mechanism).** Benefit: effort matches evidenced legal requirement exactly, no
  overclaim risk. Risk: reintroduces a two-tier trail (protected vs. unprotected), the exact
  shape of the reference system's actual weakness pattern (CF-02) — just with better default
  coverage of the two evidenced classes.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Equal | Highest — one guarantee, no exceptions to remember | Higher — applies uniformly, more to build once | Neutral | Neutral | Positive — a stronger default is easier to market/support across all tenants uniformly | High — one code path, not two | Directly extends AD-02 |
| B | Equal | Lower — two-tier trail persists, just with better defaults for the evidenced tier | Lower | Neutral | Neutral | Neutral | Medium — two tiers to maintain | Matches AD-02's letter, not its spirit |

**Recommendation:** **Option A**, as already chosen in CO-07 — the uniform-trail benefit to
auditability and maintainability is judged to outweigh the extra build effort, and CO-07
already correctly separates "we choose to do this" from "the law requires this," so Option A
does not risk an overclaim. **Not approved — Boss may reasonably prefer Option B on cost
grounds; this is presented as a genuine choice, not a foregone conclusion.**

---

## DT-05 — Correction Shape Mandate

**Context:** MP-08 deliberately left both full reversal-and-repost and single-delta-entry as
valid shapes for a correction, rather than mandating one.

- **Option A — Support both shapes (chosen in MP-08).** Benefit: matches different real
  correction scenarios naturally (a fully wrong entry vs. a partially wrong amount). Risk:
  two shapes to recognize when reading the ledger, a small cost to CO-05's "self-evident"
  objective.
- **Option B — Mandate a single shape (full reversal-and-repost only).** Benefit: maximally
  uniform, simplest possible reader mental model. Risk: for a large entry with one small
  error, forces two full-sized new entries where one small delta would tell the story more
  legibly — arguably *worse* for auditability in that case, not better.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Equal | High, if CO-05's self-evidence requirement is well built | Slightly higher (two shapes) | Neutral — MG-C05 preserves whatever shape the source used | Neutral | Neutral | Medium | Directly supports AD-04 without forcing an unnatural fit |
| B | Equal | High, uniformly | Lowest | Neutral | Neutral | Neutral | Highest | Supports AD-04 less naturally for small-error cases |

**Recommendation:** **Option A**, as already chosen — the flexibility is judged worth the
small added recognition cost, provided CO-05 is genuinely well built. **Not approved — a
reasonable case for Option B's simplicity exists and is not dismissed here.**

---

## DT-06 — Document-Numbering Sequence Scope

**Context:** CO-10/AD-09 rejected a platform-global sequence outright; the remaining choice
is between per-company and per-tenant scope.

- **Option A — Per-company sequence.** Benefit: matches the most common statutory
  expectation (a tax invoice sequence is typically an entity-level concept, not a
  group-level one) and requires no new cross-company concept. Risk: none identified as
  materially significant.
- **Option B — Per-tenant sequence spanning all companies in that tenant.** Benefit: none
  identified that outweighs the risk — this would blur exactly the company-boundary
  invariant (BINV-03) this domain otherwise strictly enforces, for no evidenced business
  requirement. Risk: directly in tension with BINV-03 and with RG-04's evidenced
  per-document-class scoping.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Matches evidenced statutory expectation | High | Lowest | Simplest — matches likely source-system scoping | Fully respects BINV-03 | Fully respects CO-10 | Highest | Neutral |
| B | Unclear statutory basis | Lower — sequence meaning becomes ambiguous across entities | Higher | Would require reconciling source sequences across companies with no evidenced need to | Tension with BINV-03 | Tension with CO-10 | Lower | None identified |

**Recommendation:** **Option A**, with high confidence — Option B was evaluated and found to
have no offsetting benefit against a real invariant tension. **Not approved pending Boss
review, though this is the lowest-controversy recommendation in this register.**

---

## DT-07 — Historical Void Semantics *(new, added at CORR-B03)*

**Context:** the original B04 §5 allowed an unconsumed COMMITTED Entry to move directly to
VOIDED via a status flip, and MP-09 excluded VOIDED Entries' Lines from aggregation based on
current status. ChatGPT's independent audit (`D01-B-AUD-03`) found this breaks historical
reproducibility: a later void changes what an earlier "as of" query reports.

- **Option A (adopted) — Voiding is always a dated, linked Correction Entry (a pure MP-07
  reversal, no replacement value).** Benefit: no new temporal-tracking machinery — MP-09's
  existing "date <= D" filter already produces correct, prospective-only semantics for free,
  since the voiding Entry's Lines are dated at the void's own (later) date. Unifies Void and
  Correction into one mechanism (simplification, not just a fix). Risk: a void is now always
  at least as "heavy" as any other correction — no lighter-weight status-flip path remains,
  though B04 §5 argues this cost is minimal given Amendment already requires full logging.
- **Option B — Keep Void as a distinct status; make MP-09 filter on the void's *effective
  date* rather than current status.** Benefit: preserves a conceptually distinct Void
  mechanism, closer to the original design's shape. Risk: raises an unresolved sub-question
  Option B does not itself answer — should "effective date" be the void *event's* date
  (prospective, correct) or the *original entry's* date (retroactive, and itself a
  reintroduction of the same historical-rewrite problem, just relocated to a different
  field)? Requires new machinery (tracking a void's effective date separately from its
  current status) that Option A does not need at all.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Correct — prospective semantics fall out of existing date-filtering, no new failure mode possible | High — a void is a fully evidenced Entry like any other | Lower — removes a special case from MP-09 rather than adding one | Neutral — MG-C05's linkage preservation already covers this shape | Neutral | Neutral | Highest — one mechanism (Correction Link) instead of two (status flip + Correction Link) | Directly resolves `D01-B-AUD-03` |
| B | Correct only if effective-date is defined as the void event's date, and only once that new field is added and consistently populated | Medium — depends on a field not currently modeled | Higher — new effective-date concept, plus a design decision about what it means that Option A avoids entirely | Neutral | Neutral | Neutral | Lower — two mechanisms to keep synchronized | Also resolves the finding, at higher cost |

**Recommendation:** **Option A**, adopted and applied to B04/B07/B08 in this corrective
round — it resolves the audit finding with a net reduction in mechanism count, not an
addition, and does not leave an unresolved sub-question (Option B's effective-date semantics)
the way Option B would. **Not independently approved by Boss** — flagged for Final Gate
alongside the other six.

---

## DT-08 — Continuous Ledger vs. Segmented-Period Ledger *(new, added at CORR-B2-03/04)*

**Context:** ChatGPT's Round 2 audit (`M-AUD-05`) required comparing at least two conceptual
carry-forward models before choosing one.

- **Option A — Continuous Ledger (adopted).** Asset/Liability/Equity accounts accumulate
  all-time (MP-09); ordinary Period close is a posting lock only; ~~Fiscal Year Close posts
  exactly one Current-Earnings-transfer Entry (MP-11);~~ **corrected at CORR-B3-05: Fiscal
  Year Close posts no Entry — Current Earnings becomes part of Reported Retained Earnings via
  a derived formula, B07 §1e/B08 MP-11 as rewritten; see DT-10 below for that specific
  decision.** Revenue/Expense are Fiscal-Year-bounded by the aggregation formula itself, not
  reset by any posted action — this part was correct in Round 2 and is unchanged. Benefit: no
  opening-balance Entry is ever created for Balance Sheet categories, so there is nothing to
  double-count with historical activity — the double-counting risk is eliminated structurally,
  not managed procedurally. Risk: none identified that Option B avoids while Option A does not
  also avoid.
- **Option B — Segmented-Period Ledger.** Each Period has its own local ledger horizon;
  explicit opening-balance facts seed each new segment; aggregation sums only within the
  selected segment. Benefit: might match a mental model where "each period is a fresh start."
  Risk: requires MP-09 to know which segment a query falls in and to explicitly exclude prior
  segments' raw activity while still including their net effect via the opening fact — this
  is exactly the mechanism that, done even slightly wrong (as Round 1's design was), produces
  `M-AUD-05`'s double-count. It also does not match how Balance Sheet accounts actually work
  (a bank balance does not "restart" every month) — Option B would need special-casing to
  distinguish Balance Sheet from Income Statement categories to correctly model this,
  effectively rediscovering Option A's category-bounding from a more complex starting point.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A | Correct by construction — no redundant fact exists to disagree with historical activity | Highest — one continuous ledger, one aggregation rule, category-bounded | Lowest — fewer concepts (no per-segment opening-balance mechanism) | Simplest — MG-C03's opening balance is the ledger's one true seed, not a repeating pattern (B07 §1d) | Neutral | Neutral | Highest | Directly resolves `M-AUD-05` |
| B | Correct only if segment boundaries and category-specific exclusion are implemented exactly right — the exact class of defect that produced the finding being corrected | Lower — a reader must know which segment a number belongs to | Higher — needs an explicit segment concept MP-09 must resolve before aggregating | More complex — migration would need to map onto artificial segments | Neutral | Neutral | Lower | Also resolves the finding, at higher risk of reintroducing it |

**Recommendation:** **Option A**, with high confidence — Option B was evaluated and found to
reintroduce, by a different route, the exact risk this correction exists to close. **Not
independently approved by Boss** — flagged for Final Gate alongside the other assumptions,
though this recommendation is a required fix (per `M-AUD-05`'s acceptance criteria), not a
discretionary preference between two equally-valid options, the same category as DT-02's
Round-1 resolution.

---

## DT-09 — Backdating Rules for Ordinary Entries vs. Corrections *(new, added at CORR-B2-01/02)*

**Context:** ChatGPT's Round 2 audit (`M-AUD-04`) required comparing at least two defensible
approaches to backdated corrections rather than either banning all backdating or leaving the
original "no special rule" answer unchanged.

- **Option A — Query-layer safety only (adopted, combined with Option B below).** Rely
  entirely on MP-09 Mode 1's Recorded-At filtering (B08, corrected) to make backdated
  Corrections harmless to historical reproducibility, with no new restriction on what
  Corrections are allowed to do. Benefit: minimal new control machinery; CO-06's "safe path
  not harder" principle is fully preserved for genuinely low-risk cases. Risk alone: a human
  could still mistake a Mode-2 (current/restated) view for Mode-1 (as originally known),
  since nothing at the *write* layer distinguishes a routine same-day correction from a
  months-later backdated one.
- **Option B — Write-layer distinction: Restatement as a separate, higher-authorization
  correction purpose (adopted, combined with Option A above).** A Correction/Void whose
  target has independent Consumption AND whose Effective Date falls within the consumed
  period is classified as a Restatement (B04 §3a), requiring CO-15's stricter authorization
  and producing its own `Restated` event. Benefit: closes the human/process-error gap Option
  A alone leaves open — a Restatement is never silently indistinguishable from an ordinary
  correction, satisfying `M-AUD-04`'s explicit requirement. Risk: adds one new classification
  test and one new authorization tier — real but proportionate given the risk it addresses.
- **Option C — Ban all backdating into any previously-closed-then-reopened period.**
  Considered and rejected: unnecessarily rigid (Team A's own reasoning, carried since B04 §4's
  original design, already established that genuinely unconsumed corrections shortly after
  close are legitimate business practice), and not required once Option A makes backdating
  provably harmless to Mode-1 history regardless.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A+B (adopted) | Correct — structurally safe (A) plus explicit, auditable distinction (B) | Highest — Mode-1 provably stable; Restatements separately visible | Medium — one classification test, one new authorization tier | Neutral | Neutral | Neutral | High | Directly resolves `M-AUD-04` per its own stated acceptance requirement |
| A alone | Correct at the query layer, but silent at the write layer — exactly the "does not let one masquerade as the other" failure mode `M-AUD-04` warns against | Medium | Lowest | Neutral | Neutral | Neutral | Medium | Resolves the data-correctness half only |
| C (rejected) | Correct but unnecessarily conservative | High | Low | Neutral | Neutral | Neutral | High | Does not address the human/process-error gap either, and forecloses legitimate low-risk corrections |

**Recommendation:** **A+B combined**, adopted and applied to B04 §3a, B08 MP-09, B09 CO-15,
B11 scenario 10. **Not independently approved by Boss** — flagged for Final Gate; this is a
required fix to satisfy `M-AUD-04`'s explicit acceptance requirement, not a discretionary
choice among equals.

---

## DT-10 — Fiscal Year Close: Posted Closing Entry vs. Derived Reporting Formula *(new, added at CORR-B3-05)*

**Context:** ChatGPT's Round 3 audit (`M-AUD-07`) found MP-11 (as drafted at CORR-B2-03/04)
internally contradictory — it described a posted Entry debiting Revenue and crediting Expense,
directly conflicting with this same design's repeated claim that Revenue/Expense are never
reset by a posted action — and, traced literally, a genuine arithmetic bug (such an Entry,
dated within the year it closes, would corrupt that year's own historical MP-09 query). The
audit's own direction was explicit: resolve by choosing exactly one coherent model, not by
retaining both. Two candidate models were compared.

- **Option A — Posted Fiscal-Year-Close Entry (Round 2's model, superseded).** Fiscal Year
  Close commits exactly one ordinary, balanced Entry: debit every Revenue account, credit every
  Expense account, net difference (Current Earnings) posted to a designated Equity account.
  Benefit: conceptually familiar (mirrors a traditional manual "closing entry" bookkeeping
  step); Equity's new balance is a stored fact, not a computation, so any consumer reading
  Equity directly sees the post-close figure with no formula to evaluate. Risk (fatal, not
  merely a tradeoff): the Entry's own Effective Date necessarily falls either inside the
  closing Fiscal Year (corrupting that year's own MP-09 query, per `M-AUD-07`'s traced defect)
  or inside the new Fiscal Year (posting into the NEW year's Revenue/Expense, which is exactly
  the "never reset by a posted action" claim being violated, just shifted one day forward) —
  there is no dating choice under Option A that avoids one of these two defects, because the
  defect is structural to positing an Entry at all, not a wording problem.
- **Option B — Derived Reporting Formula, no posted Entry (adopted).** Fiscal Year Close posts
  no Entry. It is a purely declarative Audit Event (`FiscalYearClosed`, B04) marking a Fiscal
  Year's Current Earnings as closed. Reported Retained Earnings (B07 §1e, new) is computed at
  report time as the formally-designated Retained Earnings account's own direct-posting balance
  plus the sum, over every closed Fiscal Year, of that year's Current Earnings (MP-09 Mode 2,
  Fiscal-Year-bounded). Benefit: structurally immune to both of Option A's defects — there is no
  Entry to mis-date, so no historical query can ever be corrupted by the close action itself,
  and Revenue/Expense truly are never reset by any posted action, resolving the contradiction
  exactly as `M-AUD-07` required. A later Restatement (B04 §3c) of a closed Fiscal Year's
  Current Earnings flows through Reported Retained Earnings automatically, with no separate
  "prior period adjustment" entry needed — the same property B19 Test 11 originally (if for the
  wrong, unqualified reason) concluded. Risk: Equity is no longer a single stored balance a
  naive query can read directly — any consumer that wants "current Equity including all closed
  earnings" must evaluate the formula (or a maintained, explicitly-derived materialized view of
  it), not just sum one account. This is a real implementation-complexity cost, not a modeling
  flaw — it is the same category of cost MP-09 Mode 1/Mode 2 already impose for temporal
  correctness, and is judged worth paying for the same reason: correctness over convenience.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A (superseded) | **Incorrect** — internally contradictory, and a genuine arithmetic bug under this domain's own aggregation model; no dating choice rescues it | Medium — the closing Entry is itself auditable, but its presence actively misleads a reader of the closing year's own history | Lower on paper, but only because the defect is hidden rather than absent | Neutral | Neutral | Neutral | Low — every future reader must re-discover why the closing Entry looks like it corrupts YTD figures | Does not resolve `M-AUD-07`; would need re-correcting again |
| B (adopted) | Correct by construction — no posted fact exists that could ever corrupt a historical query or contradict the never-reset claim | Highest — one declarative event, one formula, both fully traceable | Higher implementation cost (a derived figure, possibly requiring a materialized view) but lower conceptual cost (fewer contradictory claims to reconcile) | Neutral — MG-C03 unaffected (re-verified, B10) | Neutral | Neutral | Highest | Directly resolves `M-AUD-07`; also retroactively validates B19 Test 11's original conclusion with a correct rationale |

**Recommendation:** **Option B**, with high confidence — Option A was not a reasonable
alternative retained for balance; it is the specific defect this correction exists to remove,
and no variant of it (including changing the Entry's date) avoids the underlying structural
problem. **Not independently approved by Boss** — flagged for Final Gate; this is a required
fix to satisfy `M-AUD-07`'s explicit acceptance requirement (resolve the contradiction by
choosing exactly one coherent model), the same category as DT-02's Round-1 resolution and
DT-08/DT-09's Round-2 resolutions.

---

## DT-11 — Fiscal-Year Reporting Inclusion: Boundary-Driven vs. Explicit-Unclosed-Component vs. Mandatory-Atomic-Close *(new, added at CORR-B4-03)*

**Context:** ChatGPT's Round 4 audit (`M-AUD-09`) found the Round-3 formula (B07 §1e, before
this round's correction) gated a Fiscal Year's inclusion in Reported Retained Earnings on the
`FiscalYearClosed` *declaration*, not on the Fiscal Year's own calendar boundary — meaning a
routine, expected delay in the operational close process (reconciliation, review — commonly
days to weeks) would silently omit real, already-elapsed earnings from every report until the
declaration finally happened. The audit required comparing at least two models; the CORR-B4-001
directive explicitly required three. All three are evaluated below.

- **Option A — Boundary-driven reporting (adopted).** A Fiscal Year's Current Earnings enter
  Reported Retained Earnings automatically the instant its own End Date passes (B07 §1e's
  "Elapsed" test) — a pure calendar fact, never gated on any declaration. `FiscalYearClosed`
  (CAP-09) continues to govern posting-lock scope only (identical in kind to ordinary
  `PeriodClosed`, just wider). Benefit: eliminates the reporting hole structurally — there is no
  "waiting" state for Reported Retained Earnings to be wrong in, since the declaration was never
  one of the formula's inputs. Reuses the "orthogonal gates" pattern this domain already
  established for Period Lock vs. Consumption (CORR-B01) and Period Lock vs. Fiscal-Year-Lock
  (CORR-B2-03/04) rather than inventing a new mechanism. Risk: Reported Retained Earnings for an
  elapsed-but-undeclared year continues to update as ordinary pre-close entries are added
  (exactly as it always did before elapse, and exactly as any Mode-2 figure already does after a
  later Restatement) — this is a genuine, intended property (the figure is always "current best
  understanding"), not a defect, but it does mean the number can still move during the close
  window, which some readers may initially find less "final-feeling" than a formally closed
  figure — mitigated by CO-14's mode-labeling (a report can always show the Mode-1 "as known at
  T" figure instead, which IS fixed, alongside the Mode-2 figure, per B07 §1g).
- **Option B — Explicit Unclosed Prior-Year Earnings component (rejected).** Completed-but-
  not-yet-declared-closed earnings remain a separate, named reported-equity line item until the
  declaration, at which point they reclassify into Reported Retained Earnings proper — with the
  directive's own required property that total Reported Equity is unchanged by the
  reclassification. Benefit: gives `FiscalYearClosed` continued reporting-visible meaning beyond
  pure lock/governance (an auditor can see "is this figure final or still provisional" as its
  own line), which arguably mirrors how some real financial statements distinguish
  "Current Year Earnings" from "Retained Earnings" pending formal close. Risk: introduces a
  second stored/tracked reported-equity component and a reclassification step that must itself
  be proven equation-preserving (extra proof surface, extra implementation surface) — and the
  provisional/final distinction it buys is already available more simply: CAP-04's own Period
  Lock status (extended to Fiscal-Year scope by `FiscalYearClosed`) already answers "is this
  year still open to ordinary posting," without needing a second dollar-value component to
  encode the same distinction. Rejected as unnecessary complexity given Option A already
  achieves the required invariant with fewer moving parts.
- **Option C — Mandatory atomic close before the next Fiscal Year may open (rejected).** Block
  all new-Fiscal-Year postings until the prior year's `FiscalYearClosed` is declared, or make
  the close-and-open transition a single atomic action. Benefit: would eliminate the gap by
  construction, same as Option A, if actually achievable instantaneously. Risk (fatal): real
  close processes (reconciliation, adjusting entries, review) take genuine calendar time — this
  option would either force an artificial "atomic" close that skips real review (undermining the
  close process's own purpose) or block legitimate new-year business activity for days or weeks
  while the prior year is finalized, which no real business would accept and which B01/B02's own
  evidence never authorized as a requirement. The directive explicitly warned against adopting
  this "merely to save the current formula" — evaluated on its own operational merits, it fails
  independently of that warning: it does not survive contact with how closing actually works.
  Rejected outright, not merely disfavored.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A (adopted) | Correct by construction — no declaration-dependent state for the reporting equation to be wrong in | High — Mode-1/Mode-2 labeling (CO-14, extended) already distinguishes "still moving" from "fixed as of T" | Lowest — reuses the existing Elapsed/Closed orthogonal-gates pattern, no new component | Neutral — MG-C03/MG-C15 unaffected | Neutral (per-Company Fiscal Year boundaries, unchanged) | Neutral | Highest | Directly resolves `M-AUD-09` |
| B (rejected) | Correct, if the reclassification step is proven equation-preserving (extra proof burden) | High, but via a second component rather than reusing existing lock-status visibility | Higher — new stored component, new reclassification step | Neutral | Neutral | Neutral | Medium — two components to keep synchronized | Also resolves the finding, at higher implementation cost for no proven benefit over A |
| C (rejected) | Would be correct if truly atomic, but operationally unachievable — real close takes real time | High in theory, blocked in practice by the operational conflict below | Low conceptually, but only by ignoring an operational requirement | Neutral | Neutral | Negative — blocks legitimate new-period activity, a real SaaS-usability regression | Low — fights the reality of how closing works | Does not resolve `M-AUD-09` without an unrealistic operational constraint |

**Recommendation:** **Option A**, with high confidence — it resolves `M-AUD-09` with the least
new mechanism, is consistent with this domain's existing orthogonal-gates design language, and
Option C fails on operational grounds independent of the audit's own caution against adopting it
reflexively. **Not independently approved by Boss** — flagged for Final Gate; this is a required
fix to satisfy `M-AUD-09`'s explicit acceptance requirement (prove identical Reported Equity
immediately before/after the declaration), the same category as DT-08/DT-09/DT-10's resolutions.

---

## DT-12 — Fiscal Calendar Historical Safety: Boundary Immutability vs. Versioned Calendar *(new, added at CORR-B5-05)*

**Context:** ChatGPT's Round 5 audit (`M-AUD-12`) found no protection against a Fiscal Year's
Start/End boundary being silently edited after it had already governed real accounting facts —
required comparing at least two models rather than asserting a fix.

- **Option A — Boundary immutability after first authoritative use.** Once a Fiscal Year
  contains any COMMITTED Entry, is Elapsed, or has been referenced by an issued/consumed
  report, its Start/End become permanently frozen; a future calendar adjustment always creates
  a new, separate Fiscal Year definition. Benefit: the simplest possible rule — one boolean,
  no versioning machinery, trivial to audit ("is it frozen, yes or no"). Risk: a genuine
  configuration mistake caught almost immediately (before anything of substance has relied on
  the specific boundary) is treated identically to a change requested after months of real
  reliance — both permanently blocked, forcing an "abandon and recreate" workaround even for
  the harmless, zero-consequence case.
- **Option B — Versioned Fiscal Calendar (adopted).** A Fiscal Year's boundary is itself a
  versioned, effective-dated fact, mirroring the Effective-Date/Recorded-At split (§1c) and the
  Known/Current split (§1g) this design already uses elsewhere — not a new kind of mechanism,
  the same one applied one level up, to the calendar definition instead of to an Entry. Before
  first authoritative use, a correction updates the one current version harmlessly (no report
  or Entry yet exists that could have "known" a different boundary, so there is nothing for a
  Known view to diverge from). After first use, a change is a formal, CO-15-tier-or-stricter,
  audited action (a new `FiscalYearBoundaryChanged` Audit Event, B04), never a silent overwrite
  — the old version remains permanently queryable for Known-viewpoint reconstruction, and an
  existing Entry's Fiscal-Year membership is never moved without a further, separately-gated
  reclassification. Benefit: strictly generalizes Option A's protection everywhere it actually
  matters (post-reliance behavior is functionally Option A's rule) while adding a narrow,
  harmless escape hatch for the pre-reliance case. Risk: more machinery than Option A in the
  abstract — a genuine versioning concept plus an authorization tier — but this exactly mirrors
  machinery this design already accepted for Restatement (CO-15) and for Entry temporal
  properties (§1c), not a new category of complexity.
- **Option C — a different model.** Considered and rejected: no alternative was found that
  preserves historical reproducibility as strongly as Option B while being simpler. A bespoke
  third mechanism would only duplicate versioning + authorization-tiering machinery this design
  already has, under a different name, for no proven benefit over reusing it directly.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A (rejected) | Correct once frozen, but forces an awkward workaround for harmless pre-reliance corrections | High — one boolean, trivial to check | Lowest in the abstract | Neutral — MG-C16 addresses migration-time setup either way | Neutral | Negative — a trivial early config typo becomes a forced "recreate the Fiscal Year" operation, a real SaaS-usability cost | High once frozen, low during the awkward pre-reliance workaround | Resolves `M-AUD-12`, at a real, avoidable operational cost |
| B (adopted) | Correct in both the pre- and post-reliance cases, by construction | Highest — versioned facts, an Audit Event, Known-view reconstruction all explicit | Higher machinery in the abstract, but all of it reused from existing design patterns (§1c, §1g, CO-15) | Neutral — MG-C16 confirms initial calendar setup is always pre-reliance | Neutral (per-Company, unchanged) | Neutral — no harmless case is over-gated | Highest — one consistent pattern (versioned fact + Known/Current) instead of a special-cased "frozen bit" | Directly resolves `M-AUD-12`, with no operational cost for the harmless case |
| C (rejected) | Unproven — no candidate model was found | N/A | N/A | N/A | N/A | N/A | N/A | Does not resolve `M-AUD-12` without first being specified and shown at least equivalent to B |

**Recommendation:** **Option B**, with high confidence — it strictly dominates Option A (same
protection where protection matters, less operational friction where it doesn't) and reuses
this design's own established vocabulary rather than inventing a parallel "frozen bit" concept
that would exist nowhere else in the domain. **Not independently approved by Boss** — flagged
for Final Gate; the exact authorization tier for a post-reliance change is additionally flagged
as a new, seventh Team B assumption ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6), distinct
from this DT's own recommendation (Option B vs. A vs. C), which IS a required fix to satisfy
`M-AUD-12`'s acceptance requirement, the same category as DT-08 through DT-11's resolutions.

---

## DT-13 — Post-Reliance Fiscal-Year Membership Change: Prospective-Only vs. Atomic Retroactive Restatement *(new, added at CORR-B6-02)*

**Context:** ChatGPT's Round 6 audit (`M-AUD-14`) found DT-12's adopted Versioned Fiscal
Calendar model (Option B there) under-specified for Current-viewpoint reporting once a
post-reliance boundary version and old Entry membership can coexist — a distinct question from
DT-12's own (whether the boundary can be protected/versioned at all): this DT asks what
Current-viewpoint reporting does once a legitimate post-reliance change is underway.

- **Option A — Prospective-Only Change After Reliance.** The ordinary boundary-versioning
  mechanism (`FiscalYearBoundaryChanged`, DT-12's Option B) may never reach backward over any
  date reliance already covers. Historical membership stays frozen; genuine historical
  correction requires a separate, dedicated, atomic mechanism.
- **Option B — Retroactive Change with Atomic Restatement/Reclassification.** The ordinary
  boundary-versioning mechanism itself may reach backward, PROVIDED it also reclassifies every
  affected Entry's membership in the same atomic action.
- **Option C — a different model.** Considered and rejected: no alternative was found that
  resolves the coherence requirement (one authoritative membership per viewpoint, no reachable
  hybrid state) with less machinery than a refined Option A already reuses.

| | Accounting correctness | Auditability | Complexity | Migration impact | Multi-company | SaaS impact | Maintainability | Advancement potential |
|---|---|---|---|---|---|---|---|---|
| A (adopted, refined) | Correct by construction — no reachable hybrid state, since the lightweight mechanism is constitutionally barred from reliance and the heavyweight mechanism is atomic by definition | Highest — two cleanly separated mechanisms, each with an unambiguous, narrow purpose | Slightly higher than a single overloaded mechanism (two named events, not one), but each individually simpler than a "sometimes-atomic" version of one mechanism | Neutral — MG-C16 (pre-reliance migration setup) is unaffected either way | Neutral (per-Company, unchanged) | Positive — the common, lightweight case (pre-reliance/future correction) stays cheap; the rare, heavy case is clearly and separately gated | Highest — mirrors this design's existing Correction-vs-Restatement separation (CO-06/CO-15) for Entries, applied one level up, rather than inventing new machinery | Directly resolves `M-AUD-14`, completing Option A's own referenced-but-unspecified reclassification path |
| B (rejected as the general mechanism) | Correct only if the atomicity requirement is followed without exception — nothing in Round 5's own text (before this round) enforced that, which is exactly how `M-AUD-14` arose | High, if implemented correctly, but the mechanism itself must additionally guarantee atomicity as a special case some invocations need and others don't | Lower on paper (one mechanism) but effectively higher in practice — that one mechanism must behave differently (atomic vs. not) depending on whether reliance exists, which is exactly the ambiguity that produced the finding | Neutral | Neutral | Neutral — but the single mechanism's dual purpose makes its authorization/UX harder to reason about for both the lightweight and heavyweight cases | Lower — one mechanism serving two purposes is harder to keep coherent than two mechanisms each serving one, as this round's own finding demonstrates | Resolves `M-AUD-14` only if the atomicity requirement this round adds is bolted onto the existing event — functionally converges on Option A's two-mechanism shape anyway, under one name instead of two |
| C (rejected) | Unproven — no candidate model was found | N/A | N/A | N/A | N/A | N/A | N/A | Does not resolve `M-AUD-14` without first being specified and shown at least equivalent to A |

**Recommendation:** **Option A, refined** — with high confidence. Round 5's own design was
already, in substance, an incompletely-specified Option B (a boundary version was permitted to
exist "unless a separate...action is taken," leaving the two actions independently timed); that
gap, not the concept of retroactive correction itself, produced `M-AUD-14`. Rather than forcing
strict atomicity onto the existing `FiscalYearBoundaryChanged` event (Option B, literally read),
this design keeps that event scoped to its original, lightweight, pre-reliance/future-only
purpose and introduces one new, dedicated, atomic mechanism (`FiscalYearMembershipRestated`,
[B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1j, [B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md))
for the rare case that reaches into reliance — mirroring, not duplicating, this design's
existing Correction-vs-Restatement separation for Entries. **Not independently approved by
Boss** — flagged for Final Gate, same status as DT-12; the authorization tier question DT-12
already flagged as Team B assumption #7 is unchanged by this DT (it selects WHICH mechanism
applies WHEN, not WHAT tier governs either one).

---

## Acceptance Check

```
No decision jumped directly to one design without showing alternatives : CONFIRMED
Every recommendation marked as Team B-only, not approved              : CONFIRMED
Rejected options retained (not deleted) to show they were considered   : CONFIRMED (DT-02
  original Option A, DT-03 Option C, DT-06 Option B, DT-07 Option B, DT-08 Option B,
  DT-09 Option C, DT-10 Option A, DT-11 Options B and C, DT-12 Options A and C, DT-13 Option B)
```

**B13 = COMPLETE.** *(Corrected at CORR-B01/CORR-B03/CORR-B2-03/04/CORR-B3-05/CORR-B4-03/
CORR-B5-05/CORR-B6-02 — DT-02 revised in place with the original recommendation kept visible and
explicitly withdrawn as incoherent, not silently replaced; DT-07 new at Round 1 close-out,
DT-08/DT-09 new at Round 2, DT-10 new at Round 3, DT-11 new at Round 4, DT-12 new at Round 5,
DT-13 new this round. DT-01, DT-03..06 are unchanged from the original B13 pass. DT-08's
Option A description carries a Round-3 annotation correcting a stale implementation detail; the
Continuous-vs-Segmented decision itself is unaffected.)*
