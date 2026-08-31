# STEP0303R1 — BOSS REVIEW

## STATUS
Matrix complete across **17 domains**. Recommendations only, nothing selected,
no development authorised, no code written.

## COVERAGE AGAINST THE FROZEN BASELINE
Every frozen finding S2–S11 now has at least one corresponding toolchain row:
| Finding | Covered by |
|---|---|
| S2 WHT at payment | §2.1 persistence, decimal money |
| S3 Thai party identity | §2.12 i18n, annex T7 |
| S4 versioned reference data | §2.1 effective-dated rows |
| S5 tenant → entity → branch | §2.1 RLS, §2.8 tenant resolution, §2.9 job scoping |
| S6 payment gateway as service | §2.6 integration boundaries |
| S7 data-driven RBAC | §2.2 policy-as-data |
| S8 one approval abstraction | §2.3 workflow |
| S9 journal extensibility | §2.1 typed core + JSONB |
| S10 audit as platform service | §2.4 audit/eventing |
| S11 print layout as config | §2.5 rendering, annex T3 |

## THREE THINGS WORTH YOUR ATTENTION

**1. PDPA was missing from STEP0303, and that was a gap in my first pass — not a deferral.**
A column scan found **292 candidate personal and financial columns across 126 tables**
(`hr_employee` 18, `res_company` 16, `hr_version` 13, `account_move` 12). That spread makes
PDPA a cross-cutting architecture concern: classification must sit at the schema level and
flow into audit, export and erasure. It belongs in the baseline, and §2.13 now carries it.

**2. Evidence overturned the conventional i18n answer.**
The default instinct is a separate translations table. The reference system stores
translatable fields as **per-field JSONB keyed by language** — 503 jsonb columns, and the
Thai PND query itself reads `jsonb_extract_path_text(name, 'en_US')`. Recommendation follows
the evidence, not the convention.

**3. Frontend and hosting are now in the matrix but remain judgment, not evidence.**
STEP0303 excluded them because the frozen baseline does not constrain them. That is still
true. They are included so the matrix is complete and marked **[J]** throughout — approving
them means accepting my judgment, not an evidence chain. The cloud vendor I have not
recommended at all: it is a commercial decision.

## RULINGS REQUIRED
R1. Accept §2.8–§2.15 (the nine added platform domains) as toolchain baseline direction.
    BOSS: [ ] ACCEPT   [ ] AMEND ______________
R2. **Accept PDPA (§2.13) into the architecture baseline**, given the 292-column /
    126-table exposure.
    BOSS: [ ] ACCEPT   [ ] AMEND ______________
R3. Confirm the i18n storage model — per-field JSONB, following evidence over convention.
    BOSS: [ ] CONFIRM   [ ] AMEND ______________
R4. Rule on §2.16 frontend and §2.17 hosting — accept as judgment, or defer.
    BOSS: [ ] ACCEPT AS [J]   [ ] DEFER   [ ] AMEND ______________
R5. Confirm the gap-free statutory sequence requirement (§2.10) against Thai Revenue
    Department rules — I flagged it as unverified rather than assume it.
    BOSS: [ ] CONFIRM REQUIRED   [ ] NOT REQUIRED   [ ] INVESTIGATE
R6. Still open from the freeze: authorise S1 route (b); correct the duplicate database
    artefact; generic WHT engine ruling; 8 residual localization modules; payroll WHT scope.
    BOSS: [ ] DIRECT   [ ] DEFER

## GATE STATUS
```
STEP0303R1 COMPLETE / TOOLCHAIN MATRIX COMPLETE ACROSS 17 DOMAINS
S2-S11 COVERAGE COMPLETE / NOTHING SELECTED / NO DEVELOPMENT AUTHORISED
S1 STILL OPEN — THAI REPORT DEFINITIONS REMAIN UNSELECTABLE
```
Boss signature: ____________________  Date: ____________
