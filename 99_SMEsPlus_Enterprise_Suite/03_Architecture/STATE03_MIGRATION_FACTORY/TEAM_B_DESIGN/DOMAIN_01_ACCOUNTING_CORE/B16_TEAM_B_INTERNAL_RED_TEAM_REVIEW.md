# B16 — Team B Internal Red-Team Review

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B16 — Internal Red-Team Review |
| Status | **This is Team B self-review, not independent approval.** Findings below are real — six
substantive gaps were found and fixed this phase; none were manufactured to appear thorough, and none were suppressed to appear clean. |

## Method

Ten adversarial personas, each asked the phase's mandated questions plus persona-specific
follow-ups. Where a persona found nothing beyond what B02–B15 already covers, that is stated
plainly rather than padded with restated content.

---

### Persona 1 — Senior Accountant

**Finding (real, fixed):** MP-02's proof that the accounting equation holds as a corollary
of MP-01 depends on "Account Category correctly determines normal balance side" — but B07's
Account Category entity never explicitly modeled a normal-balance-side property. The proof
cited a fact the conceptual model didn't actually contain. **Fixed:** B07 §1 amended to add
this property explicitly (see §11 below).

**Checked, no defect:** Whether BINV-09's category-lock-after-first-use is too rigid for a
miscategorized legacy account — reviewed, and the design's answer (create a new, correctly
categorized account; the old one's history stays honestly attributed to what it was) is
judged correct, not a gap, because the alternative (silent retroactive recategorization)
directly reintroduces the harm BINV-09 exists to prevent.

### Persona 2 — External Auditor

**Finding (real, boundary clarification, not a design defect):** This domain's control
objectives (B09) assume the application layer — CAP-02/03/04/08 — is the only path by which
the Ledger and Audit Evidence can change. A sufficiently privileged infrastructure-level
actor bypassing the application entirely is **not** something this domain's business-rule
design can prevent, and B09 did not say so explicitly anywhere. **Fixed:** noted explicitly
as a residual scope boundary (see §11).

### Persona 3 — CFO

**Checked, no defect:** Whether the correction/amendment distinction (BR-06/BR-07/BR-14) is
too heavy for a trivial, immediately-caught typo — no, BR-14 already permits free (logged)
in-place correction before consumption, which covers exactly this case.

**Checked, no defect:** Whether mandatory currency remeasurement (CAP-06/MP-06) burdens a
domestic-only SME — no, B07 §3 already makes Currency Context conditional on any Line
carrying a non-functional-currency amount; a single-currency business never triggers it.

### Persona 4 — Migration Architect

**Finding (real, fixed):** B10 addressed committed historical data (MG-C03, MG-C04) but
never addressed **source-system entries still in an unposted/draft state at cutover** — a
routine real-world migration scenario. Silence here would leave a migration team guessing.
**Fixed:** new requirement MG-C13 added to B10 (see §11).

### Persona 5 — SaaS Architect

**Finding (real, fixed):** CO-10 requires no capability to depend on cross-tenant shared
state, and B13 DT-06 correctly scoped CAP-07's document-numbering sequence per-company for
exactly this reason — but B07 §4 point 3 described Audit Event identity as drawn from "an
append-only sequence" without stating its scope. A single global sequence across all tenants
would leak relative cross-tenant activity volume through Audit Event identifiers alone, even
without exposing any Entry content — a subtle violation of CO-10's own stated principle by
its own author. **Fixed:** B07 §4 point 3 amended (see §11).

### Persona 6 — Security / Control Reviewer

**Finding (real, fixed):** Nothing in B02–B15 addresses an Entry left in DRAFT indefinitely.
Since DRAFT is invisible to the Ledger by design (B03 §2) — correctly, for normal
not-yet-final work — this creates an available (if clumsy) way to permanently defer or
effectively hide a transaction that should have been posted, simply by never posting it.
**Fixed:** new control objective CO-13 added to B09 (see §11).

**Checked, no defect:** Time-of-check-to-time-of-use gaps around the Consumption check
(BR-07) — already covered generally by B11 scenario 17's concurrency principle, which applies
to "any state-changing action," including a correction/amendment attempt against a
Consumption status that might change concurrently.

### Persona 7 — Multi-Company User

**Finding (real, fixed):** BINV-03 correctly forbids a single Entry from spanning companies,
but no document ever stated how a legitimate **inter-company transaction** (e.g., one company
paying an expense on behalf of a related one) should be modeled under that constraint — a
real, common multi-company business need the design was silent on, which could be read as
either "impossible" (wrong) or left to guesswork (bad). **Fixed:** clarification added to
B03 §4 (see §11): modeled as two independent, linked, per-company Entries — never a single
cross-company Entry.

### Persona 8 — High-Volume Enterprise User

**Checked, correctly out of scope:** Unbounded Audit Evidence/Consumption Record growth
(BINV-07's "never retracted") and CAP-04 as a potential contention point at high transaction
volume are genuine operational concerns, but they are performance/implementation questions,
explicitly excluded from a conceptual domain-design phase (B02 §1, directive §12: "not
authorized: production code, physical database schema... API implementation"). Recorded as
reviewed, not silently ignored — carried forward as an implementation-phase concern, not a
domain-design defect.

### Persona 9 — Thai Compliance Reviewer

**Checked, no defect:** Re-verified RG-03/RG-04 scope discipline is held consistently across
every phase that cites it (already checked once in B15 §7; re-checked independently here from
a compliance-specific angle, same result). Re-verified CO-11's retention-floor language is
consistently stated as "evidenced for Thailand, extend by jurisdiction with evidence" and
never appears as a flat, jurisdiction-unqualified figure anywhere in B02–B15.

### Persona 10 — Clean-room Reviewer

**Checked, no defect:** Independent re-scan of B02–B15 for vendor field/method/table names
beyond the three explicitly reviewed comparison references already logged in B14 §3 — no
additional instances found.

**Honest answer to "is the design actually better than the reference":** Better on the
specific axes Team A identified as weaknesses — non-suppressible balance validation (vs.
CF-01), single-authority period control (vs. CF-03), structurally enforced immutability of
consumed facts (vs. CF-06, the domain's central weakness), automatic regulated-document
coverage (vs. CF-02) — each with a stated measurement criterion in B12, not merely asserted.
**Not claimed to be better everywhere**: CF-05 (exact-decimal money) was already correct in
the reference system; this design matches it, and MP-03 says so plainly rather than
manufacturing an improvement claim where none is needed. Overstating improvement on an
already-sound point would be exactly the kind of overclaim this project's provenance
discipline exists to prevent.

---

## 11. Fixes Applied This Phase

The following edits were made to already-published B0x documents, per directive §16
("fix non-governance defects autonomously... do not hide findings"). Each is a visible
addition, not a silent rewrite of prior content:

1. **B07 §1** — added "Normal Balance Side" as an explicit property of Account Category,
   closing the gap Persona 1 found in MP-02's proof.
2. **B09** — added a residual scope boundary note (Persona 2): application-layer controls
   assume application-layer access is the only path to the data; infrastructure-level bypass
   is outside this domain's boundary.
3. **B10** — added MG-C13 (Persona 4): source entries unposted at cutover must be explicitly
   dispositioned (migrated as new DRAFT, or excluded and left for source-side completion) —
   never silently dropped or silently auto-posted.
4. **B07 §4** — amended Audit Event identity scoping (Persona 5) to require per-company (at
   minimum) scope, consistent with CO-10.
5. **B09** — added CO-13 (Persona 6): Entries remaining in DRAFT beyond a policy-defined
   threshold must be surfaced for review — never auto-posted, never auto-deleted, but no
   longer silently invisible either.
6. **B03 §4** — added a clarification (Persona 7): inter-company transactions are modeled as
   two independent, linked, per-company Entries, never a single Entry spanning companies.

## 12. Acceptance Check

```
All 10 personas engaged with genuine, persona-specific questions : CONFIRMED
Findings recorded even where they required fixing prior phases    : CONFIRMED (6 fixes)
No finding hidden or suppressed                                   : CONFIRMED
Non-governance defects fixed autonomously                         : CONFIRMED (§11)
Design honestly assessed as better on SOME axes, not oversold on ALL : CONFIRMED (Persona 10)
```

## 13. Addendum — What This Review Missed *(added at CORR-B01/B02/B03)*

Recorded honestly, not to satisfy a checklist but because it is true and relevant: this
review's Senior Accountant, External Auditor, and Clean-room Reviewer personas (§ Persona 1,
2, 10) each touched the areas that turned out to contain the three BLOCKING defects the
subsequent ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`)
found — Persona 1 caught the *symptom* of the MP-02 gap (a missing Normal Balance Side
property) without catching the deeper mathematical incompleteness it was symptomatic of;
none of the ten personas questioned the period-close/consumption/reopen interaction or the
VOID/historical-aggregation interaction at all. This is recorded as a genuine limitation of
this review, not retroactively reframed as something it "basically" caught. The corrective
round's own findings and fixes are in
[CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) and
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §3a, not restated here — this addendum exists only
to correct this document's own implicit claim of thoroughness for future readers.

**B16 = COMPLETE.** *(Addendum added at CORR-B01/B02/B03; §1–§12 otherwise unchanged from
the original B16 pass.)*
