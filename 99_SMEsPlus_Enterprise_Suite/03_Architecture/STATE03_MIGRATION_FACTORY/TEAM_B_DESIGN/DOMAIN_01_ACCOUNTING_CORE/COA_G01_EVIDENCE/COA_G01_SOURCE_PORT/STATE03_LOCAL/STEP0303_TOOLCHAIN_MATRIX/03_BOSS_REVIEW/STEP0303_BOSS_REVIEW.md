# STEP0303 — BOSS REVIEW

## STATUS
**Recommendations only.** Nothing selected, no development authorised, no code written.
All rows traceable to the frozen S2–S11 baseline or explicitly marked as judgment.

## HOW TO READ THE MATRIX
Every row is tagged **[E]** evidence-derived or **[J]** engineering judgment. Of the
recommendations: the persistence, authorisation, workflow, audit, rendering and integration
rows are largely **[E]**, anchored to specific frozen findings. The language, API style and
environment rows are **[J]** — convention, not proven need. Approving a [J] row means
accepting my judgment; approving an [E] row means accepting the evidence chain.

## THE THREE DECISIONS THAT MATTER MOST
1. **Authorisation as policy-as-data (§2.2).** S7 states plainly that retrofitting a
   tenant-administrable permission model onto code-declared roles is a rewrite. This is the
   highest-consequence row in the matrix.
2. **PostgreSQL + decimal money + effective-dated reference data (§2.1).** Follows from
   S2, S4 and S9 together. A float money column or an in-place rate update would each
   produce a wrong statutory filing.
3. **HTML→PDF via a real text engine (§2.5 + annex T3).** Thai has no inter-word spaces and
   stacks tone marks; a naive PDF library breaks lines mid-word. This is a correctness issue
   on statutory documents, not an aesthetic one.

## THAI ANNEX — WHAT A GENERIC TOOLCHAIN WILL MISS
T1 Buddhist Era dates (+543, with a pre-1941 caveat the reference code documents) ·
T2 Thai date formatting (a 433-line vendored implementation in the reference) ·
T3 Thai text shaping and line breaking · T4 Thai amount-in-words incl. satang ·
T5 PromptPay QR · T6 XLSX as statutory output · T7 tax branch + Thai legal title +
address hierarchy · T8 six Python dependencies needing verified Node equivalents.

## RULINGS REQUIRED
R1. Accept the [E] rows of the matrix as the toolchain baseline direction.
    BOSS: [ ] ACCEPT   [ ] AMEND ______________
R2. Rule on the [J] rows (TypeScript, API style, environments, transport) — accept on my
    judgment, or defer pending evidence.
    BOSS: [ ] ACCEPT   [ ] DEFER   [ ] AMEND ______________
R3. Confirm the authorisation model as policy-as-data (§2.2) — the highest-consequence row.
    BOSS: [ ] CONFIRM   [ ] AMEND ______________
R4. Accept the Thai localization annex T1–T8 as mandatory toolchain requirements.
    BOSS: [ ] ACCEPT   [ ] AMEND ______________
R5. Confirm the exclusions: no frontend stack, no hosting selection, no Thai report
    definitions — all deferred for lack of evidence (S1 still open).
    BOSS: [ ] CONFIRM   [ ] AMEND ______________
R6. Carried forward and still open from the freeze: authorise S1 route (b); correct the
    duplicate database artefact; generic WHT engine ruling; 8 residual localization modules;
    payroll WHT scope.
    BOSS: [ ] DIRECT   [ ] DEFER

## GATE STATUS
```
STEP0303 COMPLETE / TOOLCHAIN MATRIX PREPARED AS RECOMMENDATIONS
NOTHING SELECTED / NO DEVELOPMENT AUTHORISED
S1 STILL OPEN — THAI REPORT DEFINITIONS CANNOT BE SELECTED
```
Boss signature: ____________________  Date: ____________
