# B10 — Canonical Migration Requirements

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B10 — Migration-Facing Canonical Requirements |
| Scope | Source-neutral — applies to migration from *any* source system, not written against the reference system's specific shape |
| Hard rule | **No source-system internal identifier is ever used as this domain's own identity** (B07 §4) |

| ID | Area | Canonical Requirement | Rationale |
|---|---|---|---|
| MG-C01 | Business identity | Every migrated Company, Account, and Entry receives a new, SMEsPlus-native identity at migration time (B07 §4). The source system's internal ID is never reused as this identity. | A source ID is an artifact of that system's own storage decisions, not a business fact this domain should depend on for identity. |
| MG-C02 | Source provenance | Every migrated fact carries a **provenance attribute** — source system name, source reference, migration batch, migration timestamp — recorded for traceability and reconciliation, but never used as an identity or as a lookup key for business logic (MG-C01 stays true even though provenance is retained). | Provenance is evidence, not identity — conflating the two would silently reintroduce source-system coupling through the back door. |
| MG-C03 | Opening balance | The first migrated position for each Company is expressed as ordinary, fully-governed Entries (B04 §7) dated at the cutover point — not a special, ungoverned "seed" concept. These Entries must independently satisfy MP-01 (Σdebit=Σcredit) exactly as any other Entry would. | "We already had this balance" is not an exemption from the balance invariant — if the opening position doesn't balance, that is itself a finding to resolve before go-live, not something to force through. |
| MG-C04 | Historical ledger | Whether full historical detail is migrated as individual committed Entries, or summarized into MG-C03's opening balance, is an explicit, documented decision per Company — never a silent default. Either way, **every migrated historical Entry dated before cutover is imported directly into a Consumed state** (B04 §4) — its originating period is, by definition, already closed from this system's perspective, so it is never available for in-place Amendment (BR-14) after migration. | Migrated history should not become *more* editable in the new system than it was intended to be in the source — importing it as already-consumed is what makes BINV-06 apply to it from day one, not after some arbitrary later event. |
| MG-C05 | Correction/reversal linkage | Where the source system recorded a correction or reversal relationship between two facts, that relationship is migrated as a real Correction Link (B07) between the two corresponding new Entries — never as two independent, coincidentally-offsetting Entries with no linkage. Where the relationship cannot be reliably reconstructed, this is a migration exception (MG-C12), flagged and resolved, not silently dropped. | The linkage is business data (B01 §8 MG-03) — losing it loses exactly the audit-trail property (BINV-05) this domain exists to protect. |
| MG-C06 | Currency | Every migrated amount carries both its original transaction currency and its functional-currency equivalent, using the **historical** exchange rate applicable at the original transaction date — never recomputed at migration time with a current-day rate. Where the source's historical rate is itself uncertain, this is recorded as a confidence flag on the migrated fact, not silently resolved either way. | Recomputing with today's rate would fabricate a different financial history than what actually happened (MP-05's recognition principle is date-anchored, not migration-date-anchored). |
| MG-C07 | Period | Historical dates map to Periods in the new system consistent with their original dates; any Period corresponding to already-migrated, pre-cutover history is created **already closed** (BINV-02), never open by default. | An open historical period in the new system would (incorrectly) suggest new activity could still post into it — contradicting MG-C04's Consumed-on-import requirement. |
| MG-C08 | Company | Each source company concept maps to exactly one Company (CAP-05) unless a split or merge is an explicit, separately documented migration decision — never inferred silently from source structure. Company identity follows MG-C01 (no source internal ID reuse). | Silent splits/merges would make MG-C05's linkage and MG-C06's currency context unreliable across the boundary that changed. |
| MG-C09 | Audit evidence | Where the source system's own change history (if any) shows a fact was altered after initial recording, that history is migrated into Audit Evidence (CAP-08) as the record of what actually happened — migration must not "launder" a messy source history into a falsely pristine one that looks as if BINV-06 had always held. | A clean-looking audit trail that is clean only because the messy parts weren't migrated is worse than an honestly incomplete one — it actively misleads an auditor. |
| MG-C10 | Validation | Every migrated Entry passes the same checks a newly-created Entry would (BR-01 balance, BR-04 valid account, BR-05 period validity against MG-C07's already-closed periods) — migration has no bypass lane through CAP-02. A source "posted" or "confirmed" state is never treated as proof of validity (B01 §8 MG-01). | This is the direct design response to Team A's CF-01 finding: source-system state alone was never sufficient evidence of balance, and migration is precisely the moment that gap becomes concrete and must be resolved, not inherited. |
| MG-C11 | Reconciliation | After migration, MP-09's trial-balance aggregation, evaluated in the new system as of the cutover date, must reconcile exactly to the source system's own trial balance as of the same date — any variance (e.g., from a rounding-method change, MP-04) must be individually explained and approved, never left as an unreconciled residual. | An unreconciled residual at cutover is a permanent, compounding unknown in every subsequent period — this is the one point where getting it wrong is nearly impossible to detect later without deliberately re-checking against the source. |
| MG-C12 | Exception handling | A source fact that cannot be cleanly migrated (fails MG-C10 validation, has an unreconstructable MG-C05 linkage, or carries an ambiguous MG-C06 currency basis) is routed to a migration exception queue. It blocks only that specific fact, never the whole migration batch, and is never silently dropped or silently force-corrected to make it pass. | Matches this project's "No Evidence = No Progress" principle applied to migration specifically — an exception queue is how that principle stays operational rather than aspirational under real migration pressure and deadlines. |
| MG-C13 | Unposted source activity at cutover *(added at B16 §11, Persona 4 fix)* | A source-system fact still in an unposted/draft/in-progress state at the moment of cutover must be explicitly dispositioned, not silently dropped or silently auto-posted: either (a) migrated as a new DRAFT Entry (B04 §2) for the business to complete in the target system, or (b) explicitly excluded and left for completion in the source system before that source is retired — the choice is a per-migration business decision, but silence is not an available third option. | The red-team pass (B16, Migration Architect persona) found B10 addressed only already-committed source data; a real migration project always has *something* mid-flight at cutover, and guessing what happens to it is exactly the kind of unrecorded assumption this project's evidence discipline exists to prevent. |

## Interaction With B05 Residual Assumptions

MG-C03/MG-C04/MG-C07's "already closed / already consumed" defaults are a Team B design
decision building on BINV-02/BINV-06, applied specifically to the migration boundary — they
are not separately evidenced by Team A (whose migration requirements, B01 §8, stop at "must
be independently validated," without specifying period/consumption state at import). Flagged
here for [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md)/[B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md)
review alongside MP-04's rounding default.

## Acceptance Check

```
All 12 mandated areas covered         : CONFIRMED
Source-neutral (no reference-system-specific requirement) : CONFIRMED
No source internal ID used as identity : CONFIRMED (MG-C01, MG-C08)
MG-C13 added post-hoc via B16 red-team review (13th item, beyond the 12 mandated) : CONFIRMED
```

**B10 = COMPLETE.**
