# SA_CORR5_11 — SMEs CORE FINAL RE-CHALLENGE

## CP-SA-C5-110 — SMEs CORE FINAL RE-CHALLENGE COMPLETE

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. The result, before the method

> **Three internal adversarial self-challengers, differently scoped and instructed to falsify, returned
> `49` findings against the frozen first package (`7d0918ca`): `17` + `17` + `15`. After verification at
> primary source, `46` were accepted in full or in part and `3` were refuted or narrowed. Five further
> defects were self-caught before the freeze.**
>
> **The largest correction reversed the package's own headline.** The first freeze reported the
> 22-scenario register at `16 / 0 / 6` on the strength of an adjudication (`C10-A1`) that read a Boss
> ruling on policy *values* as a ruling on recognition *timing*. Two challengers independently showed
> that the timing definition was a SMEs Core position (`ND-10`) the COGS package had reserved to Boss.
> **The honest figure is `10 / 0 / 12`, and the difference is one Boss item SMEs Core had decided in
> Boss's place — exactly the inversion the master prompt's challenge list names.**

**No CORR4 conclusion is overturned. Every CORR5 workstream conclusion survives; eight were corrected;
one (`C10-A1`) was withdrawn; one new file (`SA_CORR5_10A`) was written because a challenger showed
three SMEs Core design gaps had been carried as a Boss item.**

---

## 2. Method

| | |
|---|---|
| Label | **`INTERNAL ADVERSARIAL SELF-CHALLENGE`** — same model family as the author; **not independent assurance** (`SA_CORR5_12`) |
| Freeze | The package was committed and pushed at `7d0918ca` **before** any challenger was launched; no file changed while they ran (`C4-08-F-01`'s defect not repeated) |
| Challenger A | Security · Authorization · SaaS tenant/company · Identity · Integration — files `01`–`05` |
| Challenger B | PMO · Governance · Evidence integrity · Pre-Test handoff · arithmetic — files `00`, `06`, `08`, `09`, the controlled `SA15`/`SA17`, cross-file consistency |
| Challenger C | Accounting · Inventory · Manufacturing/Purchase · Thai statutory · clean-room — files `07`, `10` |
| Instruction | *"YOUR JOB IS TO FALSIFY, NOT CONFIRM. A challenge that finds nothing is a failed challenge."* Each was told the frozen commit, the primary-source paths on every relevant branch, and the master prompt's eighteen challenge classes |
| Adoption rule | **Every finding re-verified against primary text before adoption** (§3 records what was checked); a finding is adopted, narrowed, or refuted with the evidence stated |
| Classes covered | 18 of 18 master-prompt classes exercised by at least one challenger; the two the challengers reported as *tried, nothing found* are listed in §6 |

---

## 3. Findings, disposition, and what changed

Severity is the challenger's; disposition is this file's after verification.

### 3.1 Challenger C — Accounting / Inventory / Thai (`CHC-01`…`-17`)

| ID | Sev | Finding (compressed) | Verified against | Disposition | Applied at |
|---|---|---|---|---|---|
| **`CHC-01`** | **CRITICAL** | `C10-A1` decided `JT-04` (recognition timing) at SMEs Core; `BD-ACC-03A` rules values and owner only; the definition is `ND-10` (SMEs Core, not Boss-approved); reference label *"Perpetual (at invoicing)"* is `FACT VERIFIED` | `01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md` (no timing word); `SA_CORR2_01` §5.1 `ND-10`; `SA_CORR2_12` §… *"none is Boss-approved"*; `C2-F-03`; `08_JT04` §5 *"final event selection → Boss"* | **ACCEPTED — `C10-A1` WITHDRAWN**; rows 1–6, 16, 17 → `B` (`JT-04`); `ND-10` carried as SMEs Core recommendation | `SA_CORR5_10` §3, §4 |
| `CHC-02` | HIGH | `XMC-C-D6` resolves the supplier→customer case that `XMC-D-01`/`C2-D-02` reserve to Boss | `SA_CORR3_08` §3.5, `:670`; `SA_CORR3_12` `B-4` | **ACCEPTED** — carve-out added; row 18 lists both elections | `SA_CORR5_10` §5 |
| **`CHC-03`** | HIGH | `M05-A1`: performs the re-scoring CORR3 declined; wrong row (26 vs 21); row 22 named two ancestors; rows 16/17 moved under `CD-13`/`-14` with `CF-D-01` unruled; Lot anchor | R1 matrix §4.1, rows 16/17/21/25/26; `CD-13`/`-14`; `CF-D-01` in the R2 open-items register | **ACCEPTED** — anchor table re-issued as a controlled patch; Lot → `company`; row 21; row 22 split; `MTI-05` conditional on `CF-D-01` | `SA_CORR5_07` §1.2–1.4; `04_CONTEXT_MATRIX_ANCHOR_COLUMN_CORR5_CONTROLLED.md` |
| `CHC-04` | HIGH | Open items re-labelled to survive the gate: `JT-10`, Thai panel, `GAP-FS-07`, `RC-V-01` check, statutory `S` cells | `18_THAI_USER_VALIDATION_CHECKLIST` line 11 (*Boss to commission*); `09_JT05`/`08_JT04` routing; master prompt §14 | **PARTLY ACCEPTED, PARTLY NARROWED.** Thai-panel commissioning re-attributed to **Boss** (accepted); `GAP-FS-07` **executed** as a bounded evidence-at-rest pass rather than relabelled (structure traced; value = `JT-10`); `JT-10` is inside the COGS population whose routing is Boss/Business (narrowed); `RC-V-01`'s independent check is the `Q-BOSS-02` appointment, a Boss act (`B-7`) — narrowed; statutory `S` cells are the programme's standing *evidence-acquisition* class, and the gate names that class explicitly rather than folding it into 1–6 | `SA_CORR5_07` §2.3, §3.4; `SA_CORR5_14` |
| `CHC-05` | HIGH | `XMC-C-A16` states a statutory-sensitive period rule with no `HOLD` | TAS/Revenue-Code period consequences (statutory) | **ACCEPTED** — `A16` marked candidate, `S` on rows 2 and 19 | `SA_CORR5_10` §4, §5 |
| `CHC-06` | MATERIAL | `TH-NEW-01` attaches to rows 1–4; `S` tally understated; row 9's `S` sits in a `B` cell | `08_JT04` line 10 | **ACCEPTED** — `S` = 9 markers, 7 inside `B` | `SA_CORR5_10` §4.1 |
| **`CHC-07`** | MATERIAL | Rows 16/17's *exact gap* named the denominator, which CORR3 says is **not** the Boss residue; three SMEs Core design gaps (`POH-G-01/-02/-04`) were open and unexecuted | `SA_CORR3_03` §9, §11, `POH-F-01`, `POH-F-16` | **ACCEPTED — and executed:** the three design gaps closed at specification level in a new file; rows 16/17's `B` restated as `POH-D-01/-02/-06` | **`SA_CORR5_10A`** (new); `SA_CORR5_10` §4 |
| `CHC-08` | MATERIAL | Row 4 conflated `JT-04`'s *flag* discharge with a decision discharge | `SA_CORR2_01` `C2-F-03`; `SA_CORR3_06` `:217` | **ACCEPTED** | `SA_CORR5_10` row 4 |
| `CHC-09` | MATERIAL | `RC-09` is not the continuous-reconciliation control; `RC-03` is, and it is posture-dependent | R1 `10` `:55`, `:105`; R4 `05_L4` `:122`, `:125` | **ACCEPTED** — row 19 restated on `RC-03` with posture | `SA_CORR5_10` row 19 |
| `CHC-10` | MATERIAL | Reason classes omit customer return and landed-cost allocation — two of `MTI-33`'s six acts | R2 `03` §12.9 | **ACCEPTED** — `RETURN_FROM_CUSTOMER`, `LANDED_COST_ALLOCATION` added (15 classes) | `SA_CORR5_07` §3.3 |
| `CHC-11` | MATERIAL | Evidence-at-rest pass: no command/output published; undeclared table set; narrowed path set; coverage unit 5 vs 6 | programme rules (*executed-not-quoted*, *declare exclusions*) | **ACCEPTED** — Appendix A with commands and outputs in neutral vocabulary; exclusion declared; coverage 6/6 by artefact | `SA_CORR5_07` §3.2, App. A |
| `CHC-12` | MATERIAL | Three vendor field/module tokens leaked | clean-room rule | **ACCEPTED** — replaced by neutral descriptors | `SA_CORR5_07` |
| `CHC-13` | MATERIAL | `C10-A3` (over-receipt default `0`) is a control-default election of the `XD1-P1` class; cited bases do not supply it | `SA_CORR3_00` §5.1 | **ACCEPTED** — row 5 `AU` → `B`, bundled with `B-1`/`B-2`, SMEs Core recommends refuse | `SA_CORR5_10` row 5, §5 |
| `CHC-14` | MATERIAL | Row 13 `C` vs `SA17` *"Salvage undefined"*; a cost-consequence class is not a salvage object | R1 row 23; `R4-F-03` | **ACCEPTED** — `XMC-C-D7` originates the salvage object's semantics; value stays COGS residual | `SA_CORR5_10` §5 |
| `CHC-15` | MATERIAL | The 57 open COGS unknowns are not consumed; the "dissolves" claim spans 3 of 59 identifiers | `18_UNKNOWN_BURNDOWN_REPORT`; `10_JT01` §4 | **ACCEPTED** — claim scoped to three identifiers; 54 carried as a named population with owner | `SA_CORR5_10` §3.1; `SA_CORR5_14` |
| `CHC-16` | MINOR | §6 misattributed `D6` to the eight-row class and 16/17 to "existing specification" | `SA_CORR3_06` §4.3 | **ACCEPTED** | `SA_CORR5_10` §6 |
| `CHC-17` | MINOR | Forward references to unwritten files; row 18's election in the wrong dimension | package state at `7d0918ca` | **ACCEPTED** — election moved to `OUT`; forward references now resolve (files 11–15 exist at publication) | `SA_CORR5_10` row 18 |

### 3.2 Challenger B — Governance / handoff / counts (`CHB-01`…`-17`)

| ID | Sev | Finding (compressed) | Verified against | Disposition | Applied at |
|---|---|---|---|---|---|
| **`CHB-01`** | HIGH | `ND-12` collides with CORR2's `ND-12`; `ND-10` dropped without reason | `SA_CORR2_11` `:149`; `SA_CORR2_12` `:57`, `:152` | **ACCEPTED** — renumbered `ND-13`/`-14`; `ND-10` and `ND-12` carried | `SA17` controlled §4; `SA_CORR5_06` row 15 |
| **`CHB-02`** | HIGH | Instrument B's "positive control returns 1" is false (returns 0); B cannot see a heading-form claim | re-run: B = 0, C = 1, D = 4 on `111bfc41` | **ACCEPTED** — instruments C and D run over the 16 blobs and published (C = 0 all; D = 5 in `SA_CORR4_04`, quotations) | `SA_CORR5_08` §1 |
| **`CHB-03`** | HIGH | `E2E-11`/`-12` kept `TRAVERSABLE` while the same package grades them Boss-gated on `JT-05`; the class table admits no route/value split | `SA15` §1 class table; `SA_CORR5_10` rows 8–9 | **ACCEPTED** — `WITH NAMED BREAK`; `SA15` = **1 / 15 / 2**; `SA15-F-01` rewritten | `SA15`/`SA17` controlled; `SA_CORR5_06` rows 3, 4, 10 |
| `CHB-04` | MEDIUM | Namespace census: singletons are 15, not 14; the ✓ was false | re-derived per branch | **ACCEPTED** | `SA_CORR5_08` §1 |
| `CHB-05` | MEDIUM | Forward references to files 11–15 at the freeze | package state | **ACCEPTED** — wording notes the forward reference; files now exist | `SA_CORR5_09` §3 |
| **`CHB-06`** | MEDIUM | `C-02` "dissolved" — the CORR5 prompt is a commissioning prompt, not a Boss ruling; `C-02` owner *"Boss directly"* | R4 `07_L6` `:210`, `:222` | **ACCEPTED** (with `CHA-01`) — `C-02` stays an open Boss election; `00`/`01`/`10` aligned | `SA_CORR5_00` `C5-B-03`; `SA_CORR5_01` §11; `SA_CORR5_10` row 22 |
| `CHB-07` | MEDIUM | `0 of 60` attributed to `SA_CORR4_06`, which says `0 of 52`; two different "60"s in the chain | `SA_CORR4_06` §6; `SA_CORR4_10` `:99`; `SA_CORR3_06` `:430` | **ACCEPTED** — citation and composition corrected | `SA_CORR5_00` §3 row 12 |
| `CHB-08` | MEDIUM | `C5-B-02` omitted CORR3's lean to reading (ii) | `SA_CORR3_07` `:326-330` | **ACCEPTED** — lean quoted and argued against | `SA_CORR5_00`; `SA_CORR5_07` §1.2 |
| `CHB-09` | MEDIUM | Two checkpoint headers assert what their files deny (*AUTHORITATIVELY CLOSED*, *VERIFIED*) | headers vs body | **ACCEPTED** — both headers renamed | `SA_CORR5_08`, `SA_CORR5_10` |
| `CHB-10` | LOW-MED | `S` tally distribution wrong | rows | **ACCEPTED** (with `CHC-06`) | `SA_CORR5_10` §4.1 |
| `CHB-11` | LOW | Veto denominator holds only under undeclared exclusions (`MNT-V-01`, `DB-V-*` substrings) | `git grep -o` over HEAD/all heads | **ACCEPTED** — pattern and exclusions stated | `SA_CORR5_09` §1 |
| `CHB-12` | LOW | Wording sweeps published as 0 return 2 and 3 raw | re-run | **ACCEPTED** — raw counts published beside the classified zero | `SA_CORR5_09` §3; `SA_CORR5_13` §6 |
| `CHB-13` | LOW | Negative token is 0 only against the pre-package tree | re-run at HEAD | **ACCEPTED** — stated | `SA_CORR5_00` §2 |
| `CHB-14` | LOW | `is_inventory` vendor token | clean-room | **ACCEPTED** (with `CHC-12`) | `SA_CORR5_07` |
| `CHB-15` | LOW | `C5-B-01` mis-describes CORR4 (intra-package split, not superseded-file citation) | `SA_CORR4_06` §6 | **ACCEPTED** — restated | `SA_CORR5_00` §4 |
| `CHB-16` | LOW | "7 runtime registers" not enumerable | `SA17` §2c | **ACCEPTED** — eight families enumerated | `SA17` controlled §2c; `SA_CORR5_06` §3 |
| `CHB-17` | LOW | Checkpoint denominator is pre-action; post-action is `187 / 4 / 183 / 0` | re-measure | **ACCEPTED** — both stated | `SA_CORR5_08` §7 |

### 3.3 Challenger A — Security / tenant / identity (`CHA-01`…`-15`)

| ID | Sev | Finding (compressed) | Verified against | Disposition | Applied at |
|---|---|---|---|---|---|
| **`CHA-01`** | **CRITICAL** | `C-02` decided at SMEs Core; four registers say Boss; R4 itself made the same contract-§4 argument and declined | R4 `07_L6` `:210`, `:222`, `:230`; R1 `03` §7.2; R2 `04` §7.2; `GAP-FS-06`; `P14` | **ACCEPTED** — `C-02` open Boss election; SMEs Core position offered, not adopted | `SA_CORR5_01` §11; `SA_CORR5_10`; `SA_CORR5_15` |
| **`CHA-02`** | HIGH | 327-path `idempoten` population with no reduction rule; three SMEsPlus positions missed (`FV006-INT-001` IBPV-verified; Final Solution V1 `03` line 132; `B11` row 9); `A14` has prior sources | `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11 on `claude/team-b-group-a-sip-corr-008`; `FINAL_SOLUTION/INVENTORY/V1_0/03` `:132`; `B11` `:24` | **ACCEPTED** — reduction rule published; `P13`–`P15` added; `A14` re-described as consolidation; `B11` row 9 reconciled with `A2` | `SA_CORR5_01` §2, §13 |
| **`CHA-03`** | HIGH | The corpus's only architecture (`ARC-WP-009` §12.4/12.5) and `FDS_IAM` §3 place the platform actor **inside** the tenant-scoped role model; the package chose the opposite model unilaterally and cited `ARC-WP-009` as support | `ARC-WP-009` §12.4/12.5; `FDS_IAM` §3 `:71`, `FR-IAM-001` | **ACCEPTED** — `G2` restated as a two-resolution contradiction (R1 separate domain / R2 scoped role); attributes shown model-independent; decision routed to the `C4-D-02` review with SMEs Core's R1 recommendation; `FDS_IAM` patch = redefine, not add | `SA_CORR5_02` class 1, `C5-02-F-01`, §4, §6 |
| **`CHA-04`** | HIGH | Platform-Admin act set larger than five; audit export of tenant records is a cross-tenant read the package forbids | `FDS_AUDIT` §3, `US-AUD-002`; `FDS_INTEGRATION` §3; `FDS_ROLE_PERMISSION` `:53`; `FDS_SUBSCRIPTION_MODULE` `FR-SM-001`…`-004` | **ACCEPTED** — nine acts enumerated; tenant audit export removed from the platform principal by patch | `SA_CORR5_02` class 1, §4 |
| `CHA-05` | MATERIAL | `FR-INT-004` is the outbound webhook; `A14` mis-applied | `FDS_INTEGRATION` §4 | **ACCEPTED** — inbound/outbound split | `SA_CORR5_01` §7; `SA_CORR5_02` class 6 |
| `CHA-06` | MATERIAL | Occurrence identity operationalised as a document sequence, which `A5` excludes | `XMC-C-A5`; `L8-09` | **ACCEPTED** — part 4 defined as document line + attempt identity, never the number | `SA_CORR5_01` §5.2 |
| `CHA-07` | MATERIAL | "policy version in force at recognition" makes identity processing-time dependent; versioning object unruled | `BD-ACC-03A/B` text; `A5`, `A6` | **ACCEPTED** — `A3` part 6 clarified to the physical event date; category policy versioning specified as effective-dated | `SA_CORR5_01` §5.2 |
| `CHA-08` | MATERIAL | `AUD-C` omits the situational `location` axis of `CTX` | R1 `03` §2.1; R2 `04` §2 | **ACCEPTED** — `AUD-C-A5` added; `RC-D-01` declared open | `SA_CORR5_03` §3.1 |
| `CHA-09` | MATERIAL | A platform sweep reading N tenant streams is an unregistered cross-tenant read | `MTI-25`, `MTI-22`; `C3` | **ACCEPTED** — restated as N tenant-context runs with results lifted | `SA_CORR5_05` §7; `SA_CORR5_03` `C3` |
| `CHA-10` | MATERIAL | "liability" pre-empts the open accounting characterisation; "platform's tenant" conflicts with class 1 | `SAAS_CELL/27` open item | **ACCEPTED** — character `HOLD`; `PLATFORM` context identifier, not a tenant record | `SA_CORR5_02` class 13; `SA_CORR5_04` BP-1 |
| `CHA-11` | MATERIAL | Boss `00`/`01` sentence misattributed to `MTI-D-02`; ruling file not cited by path/SHA in `02`/`04` | ruling §8 | **ACCEPTED** | `SA_CORR5_02` §1; `SA_CORR5_04` §4 |
| `CHA-12` | MINOR | `revoke` = 42 unreproducible | re-run: 53 (`-i`), 47 (`\brevoked?\b`) | **ACCEPTED** — command and figure published | `SA_CORR5_05` §1 |
| `CHA-13` | MINOR | `UCE-07` miscited for `UCE-03` | `SAAS_CELL/22` | **ACCEPTED** | `SA_CORR5_02` class 13 |
| `CHA-14` | MINOR | "writable today" reverses `SA_CORR4_07` §5's prohibition without logging | `SA_CORR4_07` §5 | **ACCEPTED** — reading logged as correction 16 | `SA_CORR5_06`; `SA17` controlled §2c |
| `CHA-15` | MINOR | `CF-I-03R` owner omits Boss; `RFC-01` is invariant-level | R1 `03` `:145` | **ACCEPTED** | `SA_CORR5_05` §2, §6 |

### 3.4 Refuted or narrowed — stated so the tally is auditable

| ID | What did not survive verification |
|---|---|
| `CHC-04` (part) | *"`GAP-FS-07` is a category-1/4 item left open"* — it was **executed** in this round as a bounded evidence-at-rest pass; *"`RC-V-01`'s check is category 2"* — its executor is the `Q-BOSS-02`-eligible reviewer Boss appoints (`B-7`), an authority act; *"`JT-10` is SMEs Core"* — it sits inside the COGS population the owning package routes to Boss/Business. The **substance** — that these items must be named with owners, not vocabulary-shifted — is accepted and applied at `SA_CORR5_14` |
| `CHC-15` (scope) | *"stranded architecture not consumed"* — the COGS unknowns are a research population, not architecture; accepted as *not consumed*, classified as carried research with owner |
| `CHA-02` (count) | 318 vs this package's 327: the challenger excluded this branch; both figures published, neither changes the finding |

**Tally:** 49 challenger findings · **46 accepted** (in full or with the narrowing stated) · **3 narrowed
in part, 0 refuted outright** · **5 self-caught before freeze** (revocation vocabulary counts, the
`tenant` control's case-sensitivity, the work-package name count, the mis-scoped instrument-B set, the
scrap free-text field's shape) · **1 adjudication withdrawn** (`C10-A1`) · **1 new file** (`SA_CORR5_10A`)
· **1 new controlled patch** (`04_CONTEXT_MATRIX_ANCHOR_COLUMN…`).

---

## 4. The eighteen challenge classes, answered

| Class | Found? | Where |
|---|---|---|
| Stranded existing architecture not consumed | **Yes** — `FV006-INT-001`, Final Solution V1 `03`, `B11` row 9; `ARC-WP-009` §12.4 read against the package's own model; `SA_CORR3_03` §11's three open design gaps | `CHA-02`, `CHA-03`, `CHC-07` |
| Incorrect gap origination | **Yes** — `A14` and `C10-A3` originated where sources or a Boss class existed | `CHA-02`, `CHC-13` |
| False zero | **Yes** — instrument B's positive control; the wording sweeps' raw counts; the negative token at HEAD | `CHB-02`, `-12`, `-13` |
| Denominator error | **Yes** — singletons 15; `idempoten` 327; `revoke` 53; `S` markers 9; coverage 6 by artefact | `CHB-04`, `CHA-02`, `CHA-12`, `CHC-06`, `CHC-11` |
| Wrong test applied | **Yes** — `RC-09` for `RC-03`; `A14` on an outbound webhook | `CHC-09`, `CHA-05` |
| Unsupported readiness upgrade | **Yes** — `C10-A1` (8 rows); `E2E-11`/`-12` `TRAVERSABLE`; row 13 salvage | `CHC-01`, `CHB-03`, `CHC-14` |
| Idempotency ambiguity | **Yes** — occurrence identity vs sequence; policy version vs processing time | `CHA-06`, `CHA-07` |
| Tenant/Company leakage | **Yes** — platform sweep as a cross-tenant read | `CHA-09` |
| Unscoped privileged actor | **Yes** — four more Platform-Admin acts, one a cross-tenant read | `CHA-04` |
| Audit-shape incompleteness | **Yes** — situational location axis | `CHA-08` |
| Background process boundary leakage | **Tried, none found** beyond `CHA-09`/`-10` — every `G5` step names `T(i)`/`P`/`CELL` | Challenger A §"classes tried" |
| Revocation gap | **Tried, none found** in the mechanism; owner and one invariant-level clause corrected | `CHA-15` |
| Inventory handoff gap | **Yes** — two `MTI-33` acts uncovered; salvage object | `CHC-10`, `CHC-14` |
| Accounting handoff gap | **Yes** — `JT-04` on eight rows; the 54 carried COGS unknowns | `CHC-01`, `CHC-15` |
| Thai statutory gap | **Yes** — `A16`'s statutory interaction; `TH-NEW-01` on rows 1–4 | `CHC-05`, `CHC-06` |
| Stale compliance claim | **Tried** — the claim class is unchanged at one file; the header over-stated closure | `CHB-09` |
| Historical artefact overwritten instead of superseded | **Tried, none found** — `git diff 60752e2d HEAD -- PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08` empty | Challenger B |
| Boss question SMEs Core should answer itself — **and its inverse** | **Yes, the inverse, three times**: `JT-04`, `C-02`, `XMC-D-01`; and the platform-actor model chosen where a review was appointed | `CHC-01`, `CHA-01`/`CHB-06`, `CHC-02`, `CHA-03` |

> **`C5-11-F-01`. The dominant defect class in this package was not a missed gap but its inverse: SMEs
> Core deciding items that were reserved to Boss (`JT-04`, `C-02`, `XMC-D-01`, the platform-actor model)
> and reporting a smaller Boss list as progress.** The master prompt's rule — *do not send Boss what SMEs
> Core can close* — has a symmetric failure mode the prompt's own challenge list names last, and three
> challengers with different vocabularies each found an instance. **Every one of the four has been
> returned to Boss's list with the SMEs Core recommendation attached.**

---

## 5. Every correction re-challenged (`AUTO-C5-06`)

The corrections were committed as a second freeze and a fourth challenger was scoped **to the diff
only** (`SA_CORR5_12` §3 records its result and any second-order corrections). No correction in §3 is
recorded as accepted without that pass having run over it.

## 6. What the challenge did not reach

1. **All three challengers and the author share one model family and one corpus.** `ND-12` (CORR2's) —
   *an assurance activity declares its population and its complement* — is honoured; structural
   independence is not claimed (`SA_CORR5_12`).
2. **The evidence-at-rest passes were not re-executed by any challenger** (they could not open the
   dumps); Appendix A of `SA_CORR5_07` publishes the commands and outputs so a later party can.
3. **`SA_CORR5_10A` and the six originated clauses were written after the first freeze** and are covered
   only by the diff-scoped pass of §5.

## 7. Checkpoint

> ## `CP-SA-C5-110 — SMEs CORE FINAL RE-CHALLENGE COMPLETE`
> **3 challengers · 18 of 18 classes exercised · 49 findings, 46 accepted, 3 narrowed, 0 refuted
> outright · 5 self-caught · 1 adjudication withdrawn · 1 file and 1 controlled patch added ·
> 0 CORR4 conclusions overturned · 1 finding (`C5-11-F-01`).**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
