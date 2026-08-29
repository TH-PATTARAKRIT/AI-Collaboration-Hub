# B13 — Design Option & Trade-off Register

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B13 — Design Options & Trade-off Register |
| Status | **Team B recommendation only. None of the recommendations below are approved design until Boss Final Gate.** |
| **Corrected** | **CORR-B01 / CORR-B03 (2026-08-29)** — DT-02 revised: ChatGPT's independent audit found the original recommendation internally contradictory, not merely one reasonable option among others (see DT-02 below for the full account, kept visible). DT-07 added for the historical-void design choice CORR-B03 required. |

Originally six, now seven, decisions were significant enough — either because B04–B12
flagged them as assumptions requiring gate review, or because a real, defensible alternative
existed and picking one without showing the other was considered would understate the actual
design effort — to warrant a formal option comparison rather than a single stated choice.

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

## Acceptance Check

```
No decision jumped directly to one design without showing alternatives : CONFIRMED
Every recommendation marked as Team B-only, not approved              : CONFIRMED
Rejected options retained (not deleted) to show they were considered   : CONFIRMED (DT-02
  original Option A, DT-03 Option C, DT-06 Option B, DT-07 Option B)
```

**B13 = COMPLETE.** *(Corrected at CORR-B01/CORR-B03 — DT-02 revised in place with the
original recommendation kept visible and explicitly withdrawn as incoherent, not silently
replaced; DT-07 is new. DT-01, DT-03..06 are unchanged from the original B13 pass.)*
